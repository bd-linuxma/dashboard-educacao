#!/usr/bin/env python3
"""
Dashboard Educação Listada Brasil — +A Educação
Agente de atualização semanal.

Executa:
  python build_dashboard.py

Gera: output/index.html (dashboard completo com dados frescos)
Fonte de mercado: Fundamentus (scraping público)
Dados operacionais: curados dos últimos earnings releases (atualizar manualmente após cada trimestre)
"""

import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
NOW = datetime.now().strftime('%d/%m/%Y %H:%M')
TK = ['COGN3', 'YDUQ3', 'ANIM3', 'SEER3', 'CSED3']

# ══════════════════════════════════════════════════════════════
# 1. FETCHER — Dados de mercado do Fundamentus (atualiza sozinho)
# ══════════════════════════════════════════════════════════════

def parse_br(t):
    if not t or t.strip() in ['-', '']: return None
    t = t.strip().replace('%','').replace('?','').replace('R$','').replace('.','').replace(',','.')
    try: return float(t)
    except: return None

def fetch_fundamentus(ticker):
    """Scrape Fundamentus para um ticker. Retorna dict com ~30 indicadores."""
    r = requests.get(f'https://www.fundamentus.com.br/detalhes.php?papel={ticker}', headers=HEADERS, timeout=20)
    soup = BeautifulSoup(r.text, 'html.parser')
    d = {'ticker': ticker}
    tables = soup.find_all('table', class_='w728')
    if len(tables) < 5:
        print(f'  WARN: {ticker} retornou {len(tables)} tabelas')
        return d

    # Table 0: Info básica
    for row in tables[0].find_all('tr'):
        c = [x.get_text(strip=True) for x in row.find_all('td')]
        if len(c) >= 4:
            if 'Cotação' in c[2]: d['price'] = parse_br(c[3])
            if 'Vol' in c[2]: d['adtv'] = parse_br(c[3])
            if 'Empresa' in c[0]: d['name'] = c[1]

    # Table 1: Mercado
    for row in tables[1].find_all('tr'):
        c = [x.get_text(strip=True) for x in row.find_all('td')]
        if len(c) >= 4:
            if 'Valor de mercado' in c[0]: d['market_cap'] = parse_br(c[1])
            if 'Valor da firma' in c[0]: d['ev'] = parse_br(c[1])

    # Table 2: Indicadores + oscilações
    mapping = {
        'Dia':'var_day','Mês':'var_month','30 dias':'var_30d','12 meses':'var_12m',
        '2026':'var_ytd','2025':'var_2025','2024':'var_2024',
        'P/L':'pl','P/VP':'pvp','PSR':'psr','P/EBIT':'pebit','P/Ativos':'p_ativos',
        'LPA':'lpa','VPA':'vpa',
        'Marg. Bruta':'marg_bruta','Marg. EBIT':'marg_ebit','Marg. Líquida':'marg_liq',
        'EBIT / Ativo':'ebit_ativo','ROIC':'roic','ROE':'roe',
        'Div. Yield':'div_yield','EV / EBITDA':'ev_ebitda','EV / EBIT':'ev_ebit',
        'Liquidez Corr':'liq_corrente','Div Br/ Patrim':'debt_equity',
        'Cres. Rec (5a)':'cagr_5y','Giro Ativos':'asset_turnover',
    }
    for row in tables[2].find_all('tr'):
        c = [x.get_text(strip=True) for x in row.find_all('td')]
        for i, cell in enumerate(c):
            clean = cell.replace('?','').strip()
            if clean in mapping and i+1 < len(c):
                d[mapping[clean]] = parse_br(c[i+1])

    # Table 3: Balanço
    for row in tables[3].find_all('tr'):
        c = [x.get_text(strip=True) for x in row.find_all('td')]
        if len(c) >= 4:
            if 'Ativo' in c[0] and 'Circ' not in c[0]: d['total_assets'] = parse_br(c[1])
            if 'Disponibilidades' in c[0]: d['cash'] = parse_br(c[1])
            if 'Ativo Circulante' in c[0]: d['current_assets'] = parse_br(c[1])
            if 'Dív. Bruta' in c[2]: d['gross_debt'] = parse_br(c[3])
            if 'Dív. Líquida' in c[2]: d['net_debt'] = parse_br(c[3])
            if 'Patrim' in c[2]: d['equity'] = parse_br(c[3])

    # Table 4: DRE
    for row in tables[4].find_all('tr'):
        c = [x.get_text(strip=True) for x in row.find_all('td')]
        if len(c) >= 4:
            if 'Receita' in c[0]:
                d['revenue_12m'] = parse_br(c[1]); d['revenue_3m'] = parse_br(c[3])
            if 'EBIT' in c[0]:
                d['ebit_12m'] = parse_br(c[1]); d['ebit_3m'] = parse_br(c[3])
            if 'Lucro' in c[0]:
                d['net_income_12m'] = parse_br(c[1]); d['net_income_3m'] = parse_br(c[3])
    return d


# ══════════════════════════════════════════════════════════════
# 2. DADOS CURADOS — Atualizar manualmente após cada trimestre
# ══════════════════════════════════════════════════════════════
# Última atualização: 4T25 (março 2026)

SUPPLEMENTARY = {
    'COGN3': {
        'fn': 'Cogna', 'brands': 'Kroton, Vasta, Saber, Anhanguera, Anglo',
        'seg': [['Kroton',4200,8.5],['Vasta',1600,12],['Saber',1200,7]],
        'st':1150,'sp':250,'se':750,'sm':2.5,'tp':650,'te':180,'tm':8500,'vm':420,
        'pdd':12.5,'evs':22,'dl_ebitda':1.22,'fcf':1200,'fcf_ebitda':44,'goodwill_pct':42,
        'ead_exp':45,'pr':350,'pg':15,
        'rec':'Compra','tgt':5.50,
        'hl':'Fechou capital Vasta R$434M. Adq. Fac. Med. Dourados. Vendas NEM postergadas p/ 1T26.',
    },
    'YDUQ3': {
        'fn': 'Yduqs', 'brands': 'Estácio, IBMEC, IDOMED, Wyden',
        'seg': [['Premium',1800,15],['Presencial',2200,-2],['Digital',1500,1]],
        'st':850,'sp':300,'se':430,'sm':5.0,'tp':800,'te':220,'tm':12546,'vm':1200,
        'pdd':14.0,'evs':24,'dl_ebitda':1.46,'fcf':1050,'fcf_ebitda':61,'goodwill_pct':35,
        'ead_exp':35,'pr':480,'pg':34,
        'rec':'Compra','tgt':18.00,
        'hl':'4T25 frustrou. Prejuízo R$49,5M. Captação 1S26: híbrido +74%, pres -5%, EAD -37%.',
    },
    'ANIM3': {
        'fn': 'Ânima', 'brands': 'São Judas, Una, UniBH, Inspirali',
        'seg': [['Core',2800,6],['Inspirali',800,10],['Lifelong',400,20]],
        'st':400,'sp':200,'se':150,'sm':4.0,'tp':900,'te':250,'tm':6211,'vm':800,
        'pdd':10.5,'evs':20,'dl_ebitda':2.66,'fcf':600,'fcf_ebitda':48,'goodwill_pct':55,
        'ead_exp':15,'pr':400,'pg':20,
        'rec':'Compra','tgt':7.00,
        'hl':'Reverteu prejuízo. Inspirali ticket caiu R$7.4k→R$6.2k. DL/EBITDA 2,66x.',
    },
    'SEER3': {
        'fn': 'Ser Educacional', 'brands': 'Uninassau, Unifael, UNAMA',
        'seg': [['Presencial',1300,8],['Digital',500,15],['Medicina',350,20]],
        'st':300,'sp':150,'se':120,'sm':2.0,'tp':700,'te':200,'tm':9000,'vm':350,
        'pdd':11.0,'evs':23,'dl_ebitda':1.35,'fcf':300,'fcf_ebitda':52,'goodwill_pct':28,
        'ead_exp':20,'pr':120,'pg':12,
        'rec':'Neutro','tgt':12.00,
        'hl':'CEO vê marco EAD positivo. Foco saúde. Alavancagem 1,35x.',
    },
    'CSED3': {
        'fn': 'Cruzeiro do Sul', 'brands': 'Cruzeiro do Sul, Universidade Positivo',
        'seg': [['Presencial',1400,5],['Digital',1000,10],['Outros',350,8]],
        'st':450,'sp':180,'se':230,'sm':1.5,'tp':750,'te':210,'tm':9500,'vm':250,
        'pdd':9.5,'evs':21,'dl_ebitda':0.57,'fcf':400,'fcf_ebitda':53,'goodwill_pct':38,
        'ead_exp':40,'pr':200,'pg':10,
        'rec':'Neutro','tgt':8.00,
        'hl':'Rebaixada Santander. Baixa liquidez. Potencial M&A.',
    },
}

INTL = [
    {'t':'LAUR','n':'Laureate','c':'🇺🇸🇲🇽🇵🇪','p':34.47,'mc':5.08,'ev_eb':12.5,'me':15,'roe':18,'v12':66.1,
     'f':'LatAm higher ed','rel':'Comp direta: presença LatAm, ed. superior, pós, saúde'},
    {'t':'ATGE','n':'Adtalem','c':'🇺🇸','p':93.83,'mc':3.4,'ev_eb':9.5,'me':20,'roe':25,'v12':2.5,
     'f':'Healthcare education (Chamberlain, Ross, Walden)','rel':'Análoga vertical Health/Artmed da +A'},
    {'t':'LOPE','n':'Grand Canyon','c':'🇺🇸','p':158.06,'mc':4.4,'ev_eb':10.8,'me':30,'roe':35,'v12':-5,
     'f':'Ed services B2B asset-light','rel':'Análogo modelo Plataforma A/Vasta (B2B)'},
    {'t':'STRA','n':'Strategic Ed','c':'🇺🇸🇦🇺','p':92,'mc':2.1,'ev_eb':8.5,'me':18,'roe':15,'v12':15,
     'f':'Adult learners online (Capella, Strayer)','rel':'Ref. em EAD para adultos'},
    {'t':'COUR','n':'Coursera','c':'🌐','p':9.5,'mc':1.4,'ev_eb':0,'me':-5,'roe':0,'v12':20,
     'f':'Edtech plataforma global B2B/B2C','rel':'Ref. edtech/plataforma — análogo Plataforma A'},
    {'t':'AFYA','n':'Afya','c':'🇧🇷','p':13.5,'mc':2.5,'ev_eb':7.5,'me':25,'roe':20,'v12':30,
     'f':'Líder medicina BR + digital health','rel':'Ref. direta: medicina + digital health = Artmed'},
]

NEWS = [
    ['15/03','YDUQ3','Yduqs despenca 14% após balanço 4T25 frustrar expectativas','↓'],
    ['14/03','COGN3','Cogna recua 6,9% após lucro cair 76% no 4T25','↓'],
    ['12/03','ANIM3','Ânima reporta 4T25 — mercado aguarda Inspirali','→'],
    ['11/03','COGN3','Cogna atualiza guidance: vendas NEM postergadas p/ 1T26','→'],
    ['11/03','YDUQ3','Yduqs: lucro ajustado R$60,2M (-2,5%); captação 1S26 mista','↓'],
    ['26/02','SETOR','MEC publica nova portaria ajustando regras EAD','↑'],
    ['20/01','SETOR','Enamed: 30% cursos medicina insuficientes; 99 sob supervisão','→'],
    ['19/01','SETOR','8 cursos suspensos, 13 com -50% vagas, 33 com -25%','↓'],
    ['15/01','COGN3','Cogna conclui fechamento capital Vasta R$434M','↑'],
]


# ══════════════════════════════════════════════════════════════
# 3. LOGO SVG — Baixado de maisaedu.com.br (versão negativa)
# ══════════════════════════════════════════════════════════════

def fetch_logo():
    """Tenta baixar o logo oficial. Fallback para versão simplificada."""
    try:
        r = requests.get('https://maisaedu.com.br/hubfs/site-grupo-a/logo-mais-a-educacao-negativo.svg',
                        headers=HEADERS, timeout=10)
        if r.status_code == 200 and len(r.content) > 500:
            svg = r.text.replace('width="87" height="64"',
                                'width="140" height="103" style="max-width:140px;display:block;margin:0 auto;"')
            return svg
    except:
        pass
    # Fallback
    return '<svg width="140" height="40" viewBox="0 0 140 40" xmlns="http://www.w3.org/2000/svg"><text x="10" y="28" font-family="Poppins,sans-serif" font-size="20" font-weight="700" fill="#FFF">+a educação</text></svg>'


# ══════════════════════════════════════════════════════════════
# 4. HTML BUILDER
# ══════════════════════════════════════════════════════════════

def vc(v): return '#2BABB3' if v and v > 0 else '#BB243E' if v and v < 0 else '#B9B7B6'
def fp(v):
    if v is None: return 'N/D'
    return f'{v:+.1f}%'
def fn(v):
    if v is None: return 'N/D'
    if abs(v) >= 1e9: return f'R${v/1e9:.1f}B'
    if abs(v) >= 1e6: return f'R${v/1e6:.0f}M'
    return f'R${v:,.0f}'


def build_chart_data(cos):
    """Monta o objeto JSON com todos os dados para os 34 charts."""
    return {
        'tickers': TK,
        'mcap': [round(cos[t].get('market_cap', 0) / 1e9, 2) for t in TK],
        'var12m': [cos[t].get('var_12m', 0) for t in TK],
        'var12m_colors': [vc(cos[t].get('var_12m')) for t in TK],
        'ev_ebitda': [cos[t].get('ev_ebitda', 0) or 0 for t in TK],
        'pl': [cos[t].get('pl', 0) or 0 for t in TK],
        'marg_bruta': [cos[t].get('marg_bruta', 0) for t in TK],
        'marg_ebit': [cos[t].get('marg_ebit', 0) for t in TK],
        'marg_liq': [cos[t].get('marg_liq', 0) for t in TK],
        'revenue': [round(cos[t].get('revenue_12m', 0) / 1e9, 2) for t in TK],
        'roic': [cos[t].get('roic', 0) or 0 for t in TK],
        'roe': [cos[t].get('roe', 0) or 0 for t in TK],
        'div_yield': [cos[t].get('div_yield', 0) or 0 for t in TK],
        'net_debt': [round(cos[t].get('net_debt', 0) / 1e9, 2) for t in TK],
        'cash': [round(cos[t].get('cash', 0) / 1e9, 2) for t in TK],
        'lucro12m': [round(cos[t].get('net_income_12m', 0) / 1e6, 0) for t in TK],
        'lucro3m': [round(cos[t].get('net_income_3m', 0) / 1e6, 0) for t in TK],
        # Operacional
        'st': [cos[t].get('st', 0) for t in TK],
        'sp': [cos[t].get('sp', 0) for t in TK],
        'se': [cos[t].get('se', 0) for t in TK],
        'sm': [cos[t].get('sm', 0) for t in TK],
        'evs': [cos[t].get('evs', 0) for t in TK],
        'tp': [cos[t].get('tp', 0) for t in TK],
        'te': [cos[t].get('te', 0) for t in TK],
        'tm': [cos[t].get('tm', 0) for t in TK],
        'vm': [cos[t].get('vm', 0) for t in TK],
        'pr': [cos[t].get('pr', 0) for t in TK],
        'pg': [cos[t].get('pg', 0) for t in TK],
        'pg_colors': [vc(cos[t].get('pg')) for t in TK],
        'seg1': [cos[t]['seg'][0][1] for t in TK],
        'seg2': [cos[t]['seg'][1][1] for t in TK],
        'seg3': [cos[t]['seg'][2][1] for t in TK],
        # Alavancagem
        'dl_ebitda': [cos[t].get('dl_ebitda', 0) for t in TK],
        'fcf': [cos[t].get('fcf', 0) for t in TK],
        'fcf_ebitda': [cos[t].get('fcf_ebitda', 0) for t in TK],
        'goodwill_pct': [cos[t].get('goodwill_pct', 0) for t in TK],
        # Inadimplência
        'pdd': [cos[t].get('pdd', 0) for t in TK],
        'pmr': [75, 85, 65, 70, 60],
        'fies_pct': [8, 12, 5, 10, 7],
        'prouni_pct': [15, 18, 12, 14, 10],
        'proprio_pct': [10, 15, 8, 5, 12],
        'ead_exp': [cos[t].get('ead_exp', 0) for t in TK],
        # Radar
        'radar_labels': ['Receita','Margem EBIT','ROIC','Crescimento 5a','Liquidez','Baixa Alavancagem'],
        'radar_cogn': [100,100,64,88,77,75],
        'radar_yduq': [79,57,75,53,65,65],
        'radar_anim': [57,102,98,78,100,30],
        'radar_seer': [31,67,95,100,59,70],
        'radar_csed': [39,71,100,94,67,100],
        # Analistas
        'targets': [cos[t].get('tgt', 0) for t in TK],
        'prices': [cos[t].get('price', 0) for t in TK],
        # Internacional
        'intl_tk': [d['t'] for d in INTL],
        'intl_mc': [d['mc'] for d in INTL],
        'intl_ev_eb': [d['ev_eb'] for d in INTL],
        'intl_me': [d['me'] for d in INTL],
        'intl_roe': [d['roe'] for d in INTL],
        'all_tk': TK + [d['t'] for d in INTL],
        'all_ev_eb': [cos[t].get('ev_ebitda', 0) or 0 for t in TK] + [d['ev_eb'] for d in INTL],
        'all_me': [cos[t].get('marg_ebit', 0) for t in TK] + [d['me'] for d in INTL],
        'all_roe': [cos[t].get('roe', 0) or 0 for t in TK] + [d['roe'] for d in INTL],
        # Bubble scatter
        'bubble': (
            [{'label':t,'x':cos[t].get('ev_ebitda',0) or 0,'y':cos[t].get('marg_ebit',0),
              'r':max(5,round(cos[t].get('market_cap',1e9)/1e9*2)),
              'bg':c+'90','bw':0,'bc':'transparent'}
             for t,c in zip(TK,['#2BABB3','#BB243E','#B9B7B6','#FF9F0A','#3D3C3C'])] +
            [{'label':d['t'],'x':d['ev_eb'],'y':d['me'],'r':max(5,round(d['mc']*1.5)),
              'bg':c+'30','bw':2,'bc':c}
             for d,c in zip(INTL,['#2BABB3','#BB243E','#3D3C3C','#B9B7B6','#FF9F0A','#8B5CF6'])]
        ),
    }


def build_html(cos, logo_svg):
    """Gera o HTML completo do dashboard."""

    chart_data = build_chart_data(cos)
    data_json = json.dumps(chart_data, ensure_ascii=False)

    # Read the current dashboard as template
    # We'll use the latest version from output if it exists, otherwise build from scratch
    template_path = os.path.join(os.path.dirname(__file__), 'output', 'index.html')

    # Since we already have a working HTML, we copy it and just update the dynamic parts
    # But for the standalone agent, let's read from the saved template
    current_dir = os.path.dirname(os.path.abspath(__file__))
    existing = os.path.join(current_dir, 'template.html')

    if os.path.exists(existing):
        with open(existing, 'r', encoding='utf-8') as f:
            html = f.read()
        # Update the D = {...} block
        import re
        html = re.sub(r'const D = \{.*?\};', f'const D = {data_json};', html, count=1, flags=re.DOTALL)
        # Update timestamp
        html = re.sub(r'Atualizado em [\d/]+ [\d:]+', f'Atualizado em {NOW}', html)
        # Update ticker prices in ticker bar
        for t in TK:
            d = cos[t]
            price = d.get('price', 0)
            var = d.get('var_day', 0)
            # Update price spans
            old_pattern = f'(<span class="s">{t}</span><span class="p">)R\\$[\\d.]+(<\\/span>)'
            html = re.sub(old_pattern, f'\\1R${price:.2f}\\2', html)
        return html

    # If no template exists, we need to signal that
    print("  WARN: template.html não encontrado. Usando dashboard existente.")
    return None


# ══════════════════════════════════════════════════════════════
# 5. MAIN
# ══════════════════════════════════════════════════════════════

def main():
    print('=' * 60)
    print(f'Dashboard Educação Listada — +A Educação')
    print(f'Agente de atualização: {NOW}')
    print('=' * 60)

    # Fetch market data
    print('\n[1/4] Buscando dados de mercado (Fundamentus)...')
    mkt = {}
    for t in TK:
        print(f'  {t}...', end=' ')
        try:
            mkt[t] = fetch_fundamentus(t)
            print(f'OK — R${mkt[t].get("price", "?")}')
        except Exception as e:
            print(f'ERRO: {e}')
            mkt[t] = {'ticker': t}

    # Merge with supplementary
    print('\n[2/4] Mesclando dados operacionais curados...')
    cos = {}
    for t in TK:
        cos[t] = {**mkt[t], **SUPPLEMENTARY[t]}

    # Fetch logo
    print('\n[3/4] Baixando logo...')
    logo = fetch_logo()
    print(f'  Logo: {len(logo)} chars')

    # Build HTML
    print('\n[4/4] Gerando dashboard...')
    os.makedirs('output', exist_ok=True)

    # Try template-based update first
    html = build_html(cos, logo)

    if html is None:
        # No template — copy current dashboard if available
        src = os.path.join(os.path.dirname(__file__), 'template.html')
        if not os.path.exists(src):
            print('  ERRO: Nenhum template encontrado.')
            print('  Copie o dashboard_educacao.html gerado pelo Claude como template.html')
            return

    output_path = os.path.join('output', 'index.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'\n✅ Dashboard atualizado!')
    print(f'   Arquivo: {output_path}')
    print(f'   Tamanho: {len(html):,} chars')
    print(f'   Gráficos: {html.count("new Chart(")}')
    print(f'   Timestamp: {NOW}')

    # Also save a data snapshot
    snapshot = {
        'timestamp': NOW,
        'market_data': {t: {k: v for k, v in mkt[t].items() if v is not None} for t in TK},
    }
    with open(os.path.join('output', 'data.json'), 'w', encoding='utf-8') as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False, default=str)
    print(f'   Snapshot: output/data.json')


if __name__ == '__main__':
    main()
