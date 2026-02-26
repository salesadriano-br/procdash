
import streamlit as st

st.set_page_config(page_title="Painel de Processos BV", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
:root { color-scheme: light !important; }
* { box-sizing: border-box; }
html, body { background: #F4F6F9 !important; color: #1A2332 !important; }
.stApp { background: #F4F6F9 !important; }
.block-container { padding-top: 0.5rem !important; padding-left: 1rem !important; padding-right: 1rem !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none !important; }
header[data-testid="stHeader"] { display: none !important; } .stApp > div:first-child { margin-top: -4rem !important; }
#MainMenu, footer { display: none !important; }
.bv-header { background: linear-gradient(135deg,#002868 0%,#0057A8 100%); padding: 14px 32px; display: flex; align-items: center; gap: 20px; border-bottom: 3px solid #00A499; }
.bv-logo-box { width: 130px; height: 38px; border: 1px solid rgba(255,255,255,.3); border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 500; color: rgba(255,255,255,.55); letter-spacing:.12em; text-transform: uppercase; }
.bv-header-title { font-size: 15px; font-weight: 600; color: rgba(255,255,255,.88); letter-spacing:.07em; text-transform: uppercase; }
.bv-section-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing:.13em; color: #6C7A8D; margin-bottom: 8px; margin-top: 20px; }
.bv-proc-item { border: 1px solid #D0D5DD; border-radius: 8px; padding: 10px 12px; margin-bottom: 6px; background: white; }
.bv-proc-title { font-size: 13px; font-weight: 600; color: #1A2332; margin-bottom: 2px; }
.bv-proc-meta { font-size: 11px; color: #6C7A8D; }
.bv-card { background: white; border-radius: 10px; border: 1px solid #D0D5DD; padding: 20px 24px; margin-bottom: 16px; }
.bv-card-title { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing:.09em; color: #002868; margin-bottom: 4px; }
.bv-card-sub { font-size: 12px; color: #6C7A8D; margin-bottom: 14px; }
.bv-step { border: 1px solid #D0D5DD; border-radius: 8px; padding: 11px 14px 11px 42px; margin-bottom: 8px; position: relative; background: white; }
.bv-step-num { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); width: 22px; height: 22px; background: #0057A8; color: white; border-radius: 50%; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; }
.bv-step-name { font-size: 13px; font-weight: 600; color: #1A2332; margin-bottom: 3px; }
.bv-step-meta { font-size: 11px; color: #6C7A8D; }
.bv-badge { display: inline-block; background: #EEF4FF; color: #0057A8; font-size: 10px; font-weight: 600; padding: 2px 8px; border-radius: 999px; margin-right: 4px; margin-top: 4px; }
.bv-flow-wrapper { background: #F4F6F9; border: 1px solid #D0D5DD; border-radius: 10px; padding: 24px; overflow-x: auto; }
.bv-flow-row { display: flex; align-items: center; flex-wrap: nowrap; gap: 0; }
.bv-node { border: 1.5px solid #0057A8; background: white; color: #1A2332; padding: 8px 16px; border-radius: 8px; font-size: 12px; font-weight: 500; white-space: nowrap; min-width: 120px; text-align: center; }
.bv-arrow { color: #00A499; font-size: 18px; font-weight: 700; padding: 0 8px; flex-shrink: 0; }
.bv-kpi { flex: 1; border: 1px solid #D0D5DD; border-radius: 8px; padding: 16px; background: white; border-top: 3px solid #00A499; }
.bv-kpi-label { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing:.11em; color: #6C7A8D; margin-bottom: 8px; }
.bv-kpi-value { font-size: 30px; font-weight: 700; color: #002868; line-height: 1; margin-bottom: 6px; }
.bv-kpi-detail { font-size: 11px; color: #6C7A8D; line-height: 1.7; }
.stTabs [data-baseweb="tab-list"] { border-bottom: 1px solid #D0D5DD !important; background: transparent !important; gap: 0 !important; }
.stTabs [data-baseweb="tab"] { font-size: 12px !important; font-weight: 500 !important; color: #6C7A8D !important; padding: 8px 22px !important; border-bottom: 2px solid transparent !important; background: transparent !important; }
.stTabs [aria-selected="true"] { color: #0057A8 !important; border-bottom: 2px solid #0057A8 !important; font-weight: 600 !important; }
.stTextInput > div > div > input { border-radius: 8px !important; border: 1px solid #D0D5DD !important; font-size: 13px !important; color: #1A2332 !important; background: white !important; }
.stButton > button { border-radius: 8px !important; border: 1px solid #D0D5DD !important; font-size: 12px !important; color: #1A2332 !important; background: white !important; padding: 6px 14px !important; font-weight: 500 !important; }
.stButton > button:hover { border-color: #0057A8 !important; color: #0057A8 !important; background: #EEF4FF !important; }
div[data-testid="stExpander"] { border: 1px solid #D0D5DD !important; border-radius: 8px !important; margin-bottom: 8px !important; background: white !important; }
div[data-testid="stExpander"] summary p { font-size: 13px !important; font-weight: 500 !important; color: #1A2332 !important; }
</style>
""", unsafe_allow_html=True)

MOCK_PROCESSOS = [
    {"id": "PRC-001", "nome": "Onboarding de Clientes PJ", "area_principal": "Comercial",
     "areas": ["Comercial", "Risco", "Operacoes"],
     "etapas": [
         {"nome": "Prospeccao Inicial", "area": "Comercial", "responsavel": "Gerente de Relacionamento",
          "detalhes": "Contato inicial com o cliente, levantamento de necessidades e pre-qualificacao."},
         {"nome": "Analise de Credito", "area": "Risco", "responsavel": "Analista de Credito Senior",
          "detalhes": "Coleta de documentacao, consulta a bureaus de credito e definicao de limite."},
         {"nome": "Abertura Cadastral", "area": "Operacoes", "responsavel": "Backoffice",
          "detalhes": "Cadastro no sistema core, validacao KYC e criacao de conta digital."},
         {"nome": "Formalizacao Contratual", "area": "Juridico", "responsavel": "Advogado Corporativo",
          "detalhes": "Preparacao, revisao e assinatura digital dos contratos de relacionamento."},
         {"nome": "Ativacao Digital", "area": "Tecnologia", "responsavel": "Especialista de Onboarding",
          "detalhes": "Habilitacao de acessos ao internet banking, app mobile e perfis de seguranca."},
     ]},
    {"id": "PRC-002", "nome": "Renegociacao de Contratos", "area_principal": "Cobranca",
     "areas": ["Cobranca", "Juridico", "Financeiro"],
     "etapas": [
         {"nome": "Identificacao do Inadimplente", "area": "Cobranca", "responsavel": "Analista de Cobranca",
          "detalhes": "Identificacao de clientes em atraso e segmentacao por perfil de risco."},
         {"nome": "Contato e Proposta", "area": "Cobranca", "responsavel": "Negociador",
          "detalhes": "Apresentacao de proposta com novas condicoes de prazo, taxa e amortizacao."},
         {"nome": "Adequacao Contratual", "area": "Juridico", "responsavel": "Advogado",
          "detalhes": "Revisao de clausulas, ajuste de garantias e elaboracao do novo instrumento."},
         {"nome": "Lancamento Financeiro", "area": "Financeiro", "responsavel": "Analista Financeiro",
          "detalhes": "Baixa do contrato antigo, lancamento do novo e ajuste de provisoes."},
     ]},
    {"id": "PRC-003", "nome": "Aprovacao de Credito PF", "area_principal": "Risco",
     "areas": ["Risco", "Comercial", "Compliance"],
     "etapas": [
         {"nome": "Solicitacao do Cliente", "area": "Comercial", "responsavel": "Gerente de Conta",
          "detalhes": "Recepcao da solicitacao de credito e pre-analise."},
         {"nome": "Score e Politica", "area": "Risco", "responsavel": "Analista de Risco",
          "detalhes": "Aplicacao dos modelos de score e validacao na politica de credito."},
         {"nome": "Validacao Compliance", "area": "Compliance", "responsavel": "Analista de Compliance",
          "detalhes": "Verificacao de listas restritivas, PEP e checagens regulatorias."},
         {"nome": "Deliberacao Final", "area": "Risco", "responsavel": "Comite de Credito",
          "detalhes": "Aprovacao ou recusa formal com registro em ata e comunicacao ao cliente."},
     ]},
]

if "proc_ativo" not in st.session_state:
    st.session_state.proc_ativo = MOCK_PROCESSOS[0]["id"]
if "busca" not in st.session_state:
    st.session_state.busca = ""
if "fullscreen" not in st.session_state:
    st.session_state.fullscreen = False

st.markdown('''<div class="bv-header"><div class="bv-logo-box">Logo BV</div><div class="bv-header-title">Painel Executivo de Processos</div></div>''', unsafe_allow_html=True)

col_sb, col_main = st.columns([1, 3], gap="small")

with col_sb:
    busca = st.text_input("Buscar processo", value=st.session_state.busca, placeholder="Nome, sigla ou area...")
    if st.button("Buscar", use_container_width=True, type="primary"):
        st.session_state.busca = busca
    st.session_state.busca = busca
    if busca.strip():
        res = [p for p in MOCK_PROCESSOS if busca.lower() in p["nome"].lower() or busca.lower() in p["id"].lower()]
        st.markdown(f"<div style='font-size:11px;color:#6C7A8D;margin-bottom:8px'>Resultado para <strong>{busca}</strong></div>", unsafe_allow_html=True)
        if res:
            for r in res:
                rid  = r["id"]
                rnm  = r["nome"]
                rap  = r["area_principal"]
                ret  = len(r["etapas"])
                st.markdown(f"<div class='bv-proc-item'><div class='bv-proc-title'>{rid} &middot; {rnm}</div><div class='bv-proc-meta'>{rap} &middot; {ret} etapas</div></div>", unsafe_allow_html=True)
                if st.button("Ver", key=f"r_{rid}", use_container_width=True):
                    st.session_state.proc_ativo = r["id"]
                    st.session_state.busca = ""
                    st.rerun()
        else:
            st.info("Nenhum processo encontrado.")
        if st.button("Limpar pesquisa", use_container_width=True):
            st.session_state.busca = ""
            st.rerun()
    else:
        st.markdown("<div class='bv-section-label'>Base de Conhecimento</div>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:11px;color:#6C7A8D'>Conectado ao Firestore. Selecione um processo.</p>", unsafe_allow_html=True)
        for p in MOCK_PROCESSOS:
            pid = p["id"]
            pnm = p["nome"]
            pap = p["area_principal"]
            pet = len(p["etapas"])
            st.markdown(f"<div class='bv-proc-item'><div class='bv-proc-title'>{pid} &middot; {pnm}</div><div class='bv-proc-meta'>{pap} &middot; {pet} etapas</div></div>", unsafe_allow_html=True)
            if st.button("Abrir", key=f"m_{pid}", use_container_width=True):
                st.session_state.proc_ativo = p["id"]
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with col_main:
    proc = next((p for p in MOCK_PROCESSOS if p["id"] == st.session_state.proc_ativo), MOCK_PROCESSOS[0])
    proc_id   = proc["id"]
    proc_nome = proc["nome"]
    proc_area = proc["area_principal"]
    n_etapas  = len(proc["etapas"])
    n_areas   = len(set(proc["areas"]))

    st.markdown(
        f"<div class='bv-card' style='margin-top:12px'>"
        f"<div class='bv-card-title'>{proc_id} &mdash; {proc_nome}</div>"
        f"<div class='bv-card-sub'>Area principal: <strong>{proc_area}</strong>"
        f" &nbsp;&middot;&nbsp; {n_etapas} etapas"
        f" &nbsp;&middot;&nbsp; {n_areas} areas envolvidas</div>",
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["Passo a Passo", "Diagrama de Fluxo"])

    with tab1:
        for idx, etapa in enumerate(proc["etapas"], start=1):
            en = etapa["nome"]
            ea = etapa["area"]
            er = etapa["responsavel"]
            ed = etapa["detalhes"]
            with st.expander(f"Etapa {idx}  ·  {en}", expanded=False):
                st.markdown(
                    f"<div class='bv-step'>"
                    f"<div class='bv-step-num'>{idx}</div>"
                    f"<div class='bv-step-name'>{en}</div>"
                    f"<div><span class='bv-badge'>{ea}</span>"
                    f"<span class='bv-badge' style='background:#F0FBF9;color:#00706A'>{er}</span></div>"
                    f"<div class='bv-step-meta' style='margin-top:6px'>{ed}</div></div>",
                    unsafe_allow_html=True
                )

    with tab2:
        nodes_html = ""
        areas_html = ""
        for i, e in enumerate(proc["etapas"]):
            nm = e["nome"]
            ar = e["area"]
            nodes_html += f"<div class='bv-node'>{nm}</div>"
            areas_html += f"<div style='min-width:120px;text-align:center;font-size:10px;color:#6C7A8D;padding:0 8px'>{ar}</div>"
            if i < len(proc["etapas"]) - 1:
                nodes_html += "<div class='bv-arrow'>&#8594;</div>"
                areas_html += "<div style='padding:0 8px'></div>"
        c1, c2 = st.columns([5, 1])
        with c1:
            st.markdown(
                f"<div class='bv-flow-wrapper'>"
                "<div style='font-size:10px;font-weight:700;text-transform:uppercase;"
                "letter-spacing:.1em;color:#6C7A8D;margin-bottom:12px'>Fluxo do Processo</div>"
                f"<div class='bv-flow-row'>{nodes_html}</div>"
                f"<div class='bv-flow-row' style='margin-top:6px'>{areas_html}</div></div>",
                unsafe_allow_html=True
            )
        with c2:
            if st.button("Tela cheia", use_container_width=True):
                st.session_state.fullscreen = True
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    areas_u   = sorted(set(proc["areas"]))
    areas_str = " &middot; ".join(areas_u)
    n_et2     = len(proc["etapas"])
    n_ar2     = len(areas_u)
    st.markdown(
        "<div class='bv-card'><div class='bv-card-title'>Resumo do Processo</div>"
        "<div class='bv-card-sub'>Visao consolidada das metricas operacionais.</div>",
        unsafe_allow_html=True
    )
    k1, k2 = st.columns(2)
    with k1:
        st.markdown(
            f"<div class='bv-kpi'><div class='bv-kpi-label'>Total de Etapas</div>"
            f"<div class='bv-kpi-value'>{n_et2}</div>"
            "<div class='bv-kpi-detail'>Etapas mapeadas no fluxo operacional.</div></div>",
            unsafe_allow_html=True
        )
    with k2:
        st.markdown(
            f"<div class='bv-kpi'><div class='bv-kpi-label'>Areas Impactadas</div>"
            f"<div class='bv-kpi-value'>{n_ar2}</div>"
            f"<div class='bv-kpi-detail'>{areas_str}</div></div>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)
