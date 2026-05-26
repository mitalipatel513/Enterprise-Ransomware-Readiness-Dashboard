import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="NovaDrive | Cybersecurity Capstone",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL STYLES
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

:root {
    --bg:       #07111f;
    --panel:    #0d1b2d;
    --panel2:   #11243b;
    --line:     rgba(173,200,255,0.14);
    --text:     #eaf2ff;
    --muted:    #b7c7df;
    --soft:     #8fa6c7;
    --accent:   #7cc6ff;
    --accent2:  #8b9dff;
    --good:     #80d7a5;
    --warn:     #ffcf7d;
    --danger:   #ff9a9a;
}

html, body, [data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 90% 5%,  rgba(124,198,255,0.09), transparent 22%),
        radial-gradient(circle at 5%  5%,  rgba(139,157,255,0.10), transparent 18%),
        linear-gradient(180deg, #07111f 0%, #091425 100%) !important;
    color: var(--text) !important;
    font-family: 'Inter', sans-serif;
}

#MainMenu, header, footer,
[data-testid="stSidebar"],
[data-testid="collapsedControl"] { display: none !important; }

[data-testid="stMainBlockContainer"] {
    max-width: 1380px;
    padding: 2rem 2.5rem 5rem !important;
}

/* ── Typography ── */
h1,h2,h3,h4 { color: var(--text) !important; font-family:'Inter',sans-serif !important; letter-spacing:-0.02em; }
p, li { color: var(--muted); font-size: 0.94rem; line-height: 1.72; }
strong { color: var(--text); }

/* ── Hero ── */
.hero {
    position: relative; overflow: hidden;
    background: linear-gradient(135deg, rgba(17,36,59,0.96), rgba(9,20,37,0.97));
    border: 1px solid var(--line); border-radius: 24px;
    padding: 2rem 2.2rem 1.7rem; margin-bottom: 1.2rem;
    box-shadow: 0 20px 50px rgba(0,0,0,0.26);
}
.hero::after {
    content:""; position:absolute; inset:0;
    background: radial-gradient(circle at 88% 8%, rgba(124,198,255,0.16), transparent 22%);
    pointer-events: none;
}
.hero h1 { font-size: 2.7rem; font-weight: 800; line-height: 1.05; margin: 0 0 0.75rem; max-width: 820px; }
.hero p   { font-size: 0.97rem; max-width: 700px; margin-bottom: 1rem; color: var(--muted); }
.hero-chips { display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:0.4rem; }
.chip {
    background: rgba(124,198,255,0.10); color:#dff2ff;
    border: 1px solid rgba(124,198,255,0.18);
    padding: 0.42rem 0.7rem; border-radius: 999px;
    font-size: 0.76rem; font-weight: 600;
}
.eyebrow {
    display:inline-block; font-family:'JetBrains Mono',monospace;
    font-size:0.72rem; text-transform:uppercase; letter-spacing:0.18em;
    color:var(--accent); margin-bottom:0.8rem;
}

/* ── Top nav radio ── */
.stRadio > label { display:none !important; }
div[role="radiogroup"] {
    display:flex !important; flex-wrap:wrap;
    gap:0.5rem; margin:0.1rem 0 1.1rem;
}
div[role="radiogroup"] label {
    border: 1px solid rgba(173,200,255,0.16) !important;
    background: rgba(13,27,45,0.88) !important;
    border-radius: 999px !important;
    padding: 0.5rem 1rem !important;
    min-height: unset !important;
    cursor: pointer;
    transition: all 0.15s;
}
div[role="radiogroup"] label:hover {
    border-color: rgba(124,198,255,0.32) !important;
    box-shadow: 0 0 0 3px rgba(124,198,255,0.06);
}
div[role="radiogroup"] label p {
    color: var(--muted) !important; font-size:0.85rem !important; font-weight:600 !important;
}
div[role="radiogroup"] label[data-selected="true"] {
    background: linear-gradient(180deg,rgba(124,198,255,0.18),rgba(124,198,255,0.10)) !important;
    border-color: rgba(124,198,255,0.40) !important;
    box-shadow: 0 0 0 4px rgba(124,198,255,0.06);
}
div[role="radiogroup"] label[data-selected="true"] p { color: var(--text) !important; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid rgba(173,200,255,0.12); gap:0;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important; color: var(--soft) !important;
    border: none !important; border-bottom: 2px solid transparent !important;
    font-family: 'Inter', sans-serif !important; font-size: 0.82rem !important;
    font-weight: 600 !important; padding: 0.65rem 1.1rem !important;
    letter-spacing: 0.01em !important;
}
.stTabs [aria-selected="true"] { color: var(--accent) !important; border-bottom-color: var(--accent) !important; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 1.4rem !important; }

/* ── Section header ── */
.sec-head {
    display:flex; align-items:flex-end; justify-content:space-between;
    gap:1rem; padding-bottom:1rem; margin-bottom:1rem;
    border-bottom:1px solid rgba(173,200,255,0.10);
}
.sec-kicker {
    font-family:'JetBrains Mono',monospace; text-transform:uppercase;
    letter-spacing:0.14em; color:var(--accent); font-size:0.7rem; margin-bottom:0.3rem;
}
.sec-title { font-size:1.55rem; font-weight:800; color:var(--text); margin:0; }
.sec-note  { color:var(--soft); font-size:0.9rem; line-height:1.6; max-width:520px; }

/* ── Cards ── */
.card {
    background: linear-gradient(180deg,rgba(13,27,45,0.98),rgba(9,20,34,0.98));
    border: 1px solid var(--line); border-radius: 20px;
    padding: 1.15rem 1.2rem; height:100%;
}
.card h3 { margin:0 0 0.65rem; font-size:0.98rem; font-weight:700; color:var(--text) !important; }
.card p, .card li { font-size:0.92rem; line-height:1.70; color:var(--muted) !important; }
.card ul { padding-left:1.1rem; margin:0.3rem 0; }
.card li { margin-bottom:0.3rem; }

/* ── Accent card variants ── */
.card.accent  { border-left: 3px solid var(--accent);  }
.card.danger  { border-left: 3px solid var(--danger);  }
.card.warn    { border-left: 3px solid var(--warn);    }
.card.good    { border-left: 3px solid var(--good);    }

/* ── Metric grid ── */
.met-grid {
    display:grid; grid-template-columns:repeat(4,minmax(0,1fr));
    gap:0.85rem; margin:0.6rem 0 1rem;
}
.met-card {
    background: linear-gradient(180deg,rgba(17,36,59,0.96),rgba(10,21,36,0.96));
    border: 1px solid var(--line); border-radius: 18px;
    padding: 1rem 1rem 0.9rem; min-height:100px;
}
.met-label {
    font-family:'JetBrains Mono',monospace; text-transform:uppercase;
    letter-spacing:0.11em; font-size:0.66rem; color:var(--soft); margin-bottom:0.5rem;
}
.met-value { font-size:1.65rem; font-weight:800; color:var(--text); line-height:1; margin-bottom:0.35rem; }
.met-sub   { font-size:0.84rem; color:var(--muted); line-height:1.5; }

/* ── Timeline ── */
.tl-item {
    display:grid; grid-template-columns:88px 1fr; gap:1rem;
    align-items:start; padding:0.9rem 0;
    border-bottom:1px solid rgba(173,200,255,0.09);
}
.tl-item:last-child { border-bottom:none; }
.tl-week {
    font-family:'JetBrains Mono',monospace; color:var(--accent);
    font-size:0.76rem; text-transform:uppercase; letter-spacing:0.08em;
    padding-top:0.12rem;
}
.tl-desc { color:var(--muted); line-height:1.65; font-size:0.92rem; }

/* ── Callout / info band ── */
.callout {
    border-left:3px solid var(--accent); background:rgba(124,198,255,0.07);
    padding:0.85rem 1rem; border-radius:12px; margin:0.7rem 0;
    color:var(--muted); font-size:0.92rem; line-height:1.65;
}
.callout.warn   { border-left-color:var(--warn);   background:rgba(255,207,125,0.07); }
.callout.danger { border-left-color:var(--danger);  background:rgba(255,154,154,0.07); }
.callout.good   { border-left-color:var(--good);   background:rgba(128,215,165,0.07); }

/* ── Placeholder ── */
.placeholder {
    border: 1px dashed rgba(173,200,255,0.22);
    background: rgba(173,200,255,0.04);
    border-radius:14px; padding:0.9rem 1rem;
    color:#7a9fc0; font-size:0.88rem; font-style:italic;
}

/* ── Mini tag row ── */
.mini-tag {
    display:inline-block; margin:0 0.3rem 0.38rem 0;
    padding:0.36rem 0.6rem; border-radius:999px;
    font-size:0.73rem; font-weight:650; color:var(--text);
    background:rgba(139,157,255,0.12); border:1px solid rgba(139,157,255,0.18);
}

/* ── Table ── */
.nd-table { width:100%; border-collapse:collapse; margin-top:0.4rem; }
.nd-table th {
    font-family:'JetBrains Mono',monospace; font-size:0.66rem;
    text-transform:uppercase; letter-spacing:0.12em; color:var(--text);
    padding:0.7rem 0.75rem; border-bottom:1px solid rgba(173,200,255,0.14);
    text-align:left; background:rgba(0,0,0,0.12);
}
.nd-table td {
    padding:0.78rem 0.75rem; border-bottom:1px solid rgba(173,200,255,0.07);
    font-size:0.88rem; color:var(--muted); vertical-align:top; line-height:1.6;
}
.nd-table tr:hover td { background:rgba(124,198,255,0.025); }
.nd-table strong { color:var(--text); }

/* ── Maturity bar ── */
.mat-row {
    display:flex; align-items:center; gap:1rem; margin-bottom:0.7rem;
    padding:0.9rem 1rem; background:rgba(13,27,45,0.9);
    border:1px solid var(--line); border-radius:14px;
}
.mat-label { font-size:0.88rem; color:var(--muted); min-width:220px; flex-shrink:0; }
.mat-wrap  { flex:1; }
.mat-sublabel { font-size:0.66rem; color:var(--soft); letter-spacing:0.08em; text-transform:uppercase; margin-bottom:3px; font-family:'JetBrains Mono',monospace; }
.mat-track { height:4px; background:rgba(173,200,255,0.10); border-radius:3px; overflow:hidden; margin-bottom:8px; }
.mat-fill  { height:100%; border-radius:3px; }
.mat-score { font-family:'JetBrains Mono',monospace; font-size:0.74rem; color:var(--soft); min-width:38px; text-align:right; flex-shrink:0; }

/* ── RACI badges ── */
.raci-r { color:#7cc6ff; font-weight:700; font-family:'JetBrains Mono',monospace; }
.raci-a { color:#80d7a5; font-weight:700; font-family:'JetBrains Mono',monospace; }
.raci-c { color:#ffcf7d; font-weight:700; font-family:'JetBrains Mono',monospace; }
.raci-i { color:#4a6080; font-weight:700; font-family:'JetBrains Mono',monospace; }

/* ── Attack flow ── */
.flow-grid {
    display:grid; grid-template-columns:repeat(6,1fr);
    border:1px solid var(--line); border-radius:16px; overflow:hidden; margin:1rem 0;
}
.flow-step {
    padding:1rem 0.9rem; background:rgba(13,27,45,0.95);
    border-right:1px solid rgba(173,200,255,0.09);
}
.flow-step:last-child { border-right:none; }
.flow-num  { font-family:'JetBrains Mono',monospace; font-size:0.6rem; color:var(--soft); display:block; margin-bottom:0.4rem; }
.flow-name { font-family:'Inter',sans-serif; font-size:0.78rem; font-weight:700; color:var(--text); display:block; margin-bottom:0.3rem; }
.flow-desc { font-size:0.74rem; color:var(--soft); line-height:1.5; }

/* ── Phase block ── */
.phase-block {
    background: rgba(13,27,45,0.94); border:1px solid var(--line);
    border-radius:16px; padding:1.1rem 1.2rem; margin-bottom:0.75rem;
}
.phase-label { font-family:'JetBrains Mono',monospace; font-size:0.66rem; letter-spacing:0.16em; text-transform:uppercase; display:block; margin-bottom:0.4rem; }
.phase-title { font-size:1rem; font-weight:700; color:var(--text); margin-bottom:0.8rem; }
.phase-item  { display:grid; grid-template-columns:180px 1fr; gap:0.6rem; padding:0.6rem 0; border-bottom:1px solid rgba(173,200,255,0.07); font-size:0.88rem; }
.phase-item:last-child { border-bottom:none; }
.phase-item-key { color:var(--accent2); font-weight:600; }
.phase-item-val { color:var(--muted); }

/* SOC tier */
.soc-tier {
    display:grid; grid-template-columns:100px 1fr; border:1px solid var(--line);
    border-radius:16px; overflow:hidden; margin-bottom:0.7rem;
}
.soc-num-col {
    background:rgba(13,27,45,0.98); border-right:1px solid var(--line);
    display:flex; flex-direction:column; align-items:center;
    justify-content:center; padding:1rem; text-align:center;
}
.soc-tier-lbl { font-family:'JetBrains Mono',monospace; font-size:0.58rem; color:var(--soft); letter-spacing:0.12em; text-transform:uppercase; display:block; margin-bottom:4px; }
.soc-tier-num { font-size:1.4rem; font-weight:800; }
.soc-content  { padding:1rem 1.2rem; background:rgba(9,20,34,0.95); }
.soc-tier-title { font-size:0.88rem; font-weight:700; margin-bottom:0.55rem; }
.soc-bullets li { font-size:0.84rem; color:var(--soft); line-height:1.7; margin-bottom:0.2rem; }

/* divider */
.pill-div { height:1px; background:rgba(173,200,255,0.09); margin:0.8rem 0; }

@media(max-width:1100px){ .met-grid{grid-template-columns:repeat(2,1fr);} }
@media(max-width:700px){  .met-grid{grid-template-columns:1fr;} .flow-grid{grid-template-columns:1fr;} }

/* ── Executive Visual Additions ── */
.exec-grid {
    display:grid; grid-template-columns:repeat(5,minmax(0,1fr));
    gap:0.85rem; margin:1rem 0 1.1rem;
}
.exec-step {
    position:relative; min-height:185px;
    background:linear-gradient(180deg,rgba(17,36,59,0.96),rgba(8,18,31,0.98));
    border:1px solid rgba(173,200,255,0.14); border-radius:20px;
    padding:1rem 0.95rem; overflow:hidden;
}
.exec-step::after {
    content:"→"; position:absolute; right:-0.15rem; top:42%;
    color:rgba(124,198,255,0.42); font-size:1.7rem; font-weight:800;
}
.exec-step:last-child::after { content:""; }
.exec-num {
    font-family:'JetBrains Mono',monospace; font-size:0.63rem; color:var(--accent);
    letter-spacing:0.14em; text-transform:uppercase; margin-bottom:0.55rem;
}
.exec-icon { font-size:1.65rem; margin-bottom:0.5rem; }
.exec-title { color:var(--text); font-weight:800; font-size:0.92rem; line-height:1.25; margin-bottom:0.45rem; }
.exec-copy { color:var(--soft); font-size:0.75rem; line-height:1.55; }

.impact-strip {
    display:grid; grid-template-columns:1.1fr 0.8fr 1.1fr;
    gap:0.85rem; margin:0.7rem 0 1rem;
}
.impact-card {
    background:rgba(13,27,45,0.94); border:1px solid var(--line);
    border-radius:18px; padding:1rem; text-align:center;
}
.impact-card .big { font-size:1.8rem; font-weight:800; color:var(--text); line-height:1; margin-bottom:0.4rem; }
.impact-card .small { color:var(--soft); font-size:0.82rem; line-height:1.55; }

.gov-org {
    display:grid; grid-template-columns:1fr; gap:0.7rem; margin:0.7rem 0 1.1rem;
}
.gov-top {
    max-width:360px; margin:auto; text-align:center;
    background:linear-gradient(180deg,rgba(124,198,255,0.18),rgba(124,198,255,0.07));
    border:1px solid rgba(124,198,255,0.28); border-radius:20px;
    padding:1rem 1.2rem;
}
.gov-role { font-size:1.05rem; font-weight:800; color:var(--text); }
.gov-sub { font-size:0.76rem; color:var(--soft); margin-top:0.25rem; }
.gov-line { height:28px; width:1px; background:rgba(124,198,255,0.28); margin:auto; }
.gov-branches {
    display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0.75rem;
}
.gov-branch {
    text-align:center; background:rgba(13,27,45,0.94); border:1px solid var(--line);
    border-radius:18px; padding:0.95rem 0.8rem; min-height:116px;
}
.gov-branch .icon { font-size:1.4rem; margin-bottom:0.35rem; }
.gov-branch .name { color:var(--text); font-weight:800; font-size:0.86rem; margin-bottom:0.25rem; }
.gov-branch .desc { color:var(--soft); font-size:0.72rem; line-height:1.45; }

.policy-grid {
    display:grid; grid-template-columns:repeat(5,minmax(0,1fr));
    gap:0.8rem; margin:0.8rem 0 1rem;
}
.policy-card {
    background:linear-gradient(180deg,rgba(13,27,45,0.98),rgba(9,20,34,0.98));
    border:1px solid var(--line); border-radius:20px; padding:1rem 0.85rem;
    text-align:center; min-height:170px;
}
.policy-card .pol-icon { font-size:1.75rem; margin-bottom:0.5rem; }
.policy-card .pol-title { color:var(--text); font-weight:800; font-size:0.84rem; line-height:1.25; margin-bottom:0.45rem; }
.policy-card .pol-gap { color:var(--soft); font-size:0.72rem; line-height:1.45; }

.raci-mini {
    display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:0.8rem; margin:0.75rem 0 1rem;
}
.raci-mini-card {
    background:rgba(13,27,45,0.95); border:1px solid var(--line); border-radius:18px;
    padding:1rem; text-align:center;
}
.raci-mini-card .letter { font-family:'JetBrains Mono',monospace; font-size:1.6rem; font-weight:800; margin-bottom:0.3rem; }
.raci-mini-card .label { color:var(--text); font-weight:800; font-size:0.88rem; margin-bottom:0.2rem; }
.raci-mini-card .example { color:var(--soft); font-size:0.72rem; line-height:1.45; }

@media(max-width:1100px){
    .exec-grid,.policy-grid{grid-template-columns:repeat(2,minmax(0,1fr));}
    .gov-branches,.raci-mini{grid-template-columns:repeat(2,minmax(0,1fr));}
    .impact-strip{grid-template-columns:1fr;}
}
@media(max-width:700px){
    .exec-grid,.policy-grid,.gov-branches,.raci-mini{grid-template-columns:1fr;}
    .exec-step::after{display:none;}
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def sec_header(kicker, title, note=""):
    st.markdown(f"""
    <div class="sec-head">
        <div>
            <div class="sec-kicker">{kicker}</div>
            <div class="sec-title">{title}</div>
        </div>
        <div class="sec-note">{note}</div>
    </div>""", unsafe_allow_html=True)

def card(title, body, variant=""):
    st.markdown(f'<div class="card {variant}"><h3>{title}</h3>{body}</div>', unsafe_allow_html=True)

def placeholder(label="ENTER INFO HERE"):
    st.markdown(f'<div class="placeholder">{label}</div>', unsafe_allow_html=True)

def callout(text, variant=""):
    st.markdown(f'<div class="callout {variant}">{text}</div>', unsafe_allow_html=True)

def tag_row(tags):
    st.markdown("".join(f'<span class="mini-tag">{t}</span>' for t in tags), unsafe_allow_html=True)

def met_grid(items):
    html = "".join(
        f'<div class="met-card"><div class="met-label">{lbl}</div><div class="met-value">{val}</div><div class="met-sub">{sub}</div></div>'
        for val, lbl, sub in items
    )
    st.markdown(f'<div class="met-grid">{html}</div>', unsafe_allow_html=True)

def mat_row(label, pol, proc, color):
    pw = pol * 20
    prw = proc * 20
    st.markdown(f"""
    <div class="mat-row">
        <div class="mat-label">{label}</div>
        <div class="mat-wrap">
            <div class="mat-sublabel">Policy</div>
            <div class="mat-track"><div class="mat-fill" style="width:{pw}%;background:{color};"></div></div>
            <div class="mat-sublabel">Process</div>
            <div class="mat-track"><div class="mat-fill" style="width:{prw}%;background:{color};"></div></div>
        </div>
        <div class="mat-score">L{pol} / L{proc}</div>
    </div>""", unsafe_allow_html=True)

def raci_table(rows):
    cls = {"R": "raci-r", "A": "raci-a", "C": "raci-c", "I": "raci-i"}
    head = "<thead><tr><th>Activity</th><th>CISO</th><th>IT Team</th><th>Cloud Team</th><th>OT Team</th><th>Executives</th></tr></thead>"
    body = "".join(
        f"<tr><td><strong>{r[0]}</strong></td>"
        + "".join(f'<td style="text-align:center"><span class="{cls[v]}">{v}</span></td>' for v in r[1:])
        + "</tr>"
        for r in rows
    )
    st.markdown(f'<table class="nd-table">{head}<tbody>{body}</tbody></table>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="eyebrow">Georgia State University &nbsp;·&nbsp; CIS 8397 &nbsp;·&nbsp; MSIS Cybersecurity Capstone</div>
    <h1>NovaDrive Cybersecurity<br>Consulting Engagement</h1>
    <p>Ransomware Readiness &amp; Cloud Security Assessment — a comprehensive enterprise cybersecurity engagement covering threat modeling, current-state assessment, gap analysis, architecture design, governance, and implementation planning.</p>
    <div class="hero-chips">
        <span class="chip">MITRE ATT&amp;CK</span>
        <span class="chip">NIST CSF 2.0 &amp; 800-82</span>
        <span class="chip">Zero Trust Architecture</span>
        <span class="chip">Cloud: AWS &amp; Azure</span>
        <span class="chip">IT / OT Convergence</span>
        <span class="chip">8-Week Engagement</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TOP NAVIGATION
# ─────────────────────────────────────────────────────────────────────────────
st.markdown('<p style="color:var(--soft);font-size:0.85rem;margin-bottom:0.2rem;">Navigate between sections using the pills below.</p>', unsafe_allow_html=True)
page = st.radio("nav", ["Overview", "Part 1", "Part 2", "Part 3"], horizontal=True, label_visibility="collapsed")

# ══════════════════════════════════════════════════════════════════════════════
# OVERVIEW
# ══════════════════════════════════════════════════════════════════════════════
if page == "Overview":

    sec_header("Project Summary", "Engagement Overview",
               "A high-level landing page covering NovaDrive's profile, consulting focus, and section roadmap.")

    met_grid([
        ("7", "Facilities", "Headquarters, 4 manufacturing plants, and 2 distribution centers across the U.S."),
        ("AWS · Azure · Private", "Cloud Footprint", "Hybrid multi-cloud environment supporting engineering and operations."),
        ("Ransomware", "Primary Threat", "Focus on ransomware pathways, containment, detection, and recovery."),
        ("8 Weeks", "Program Length", "Capstone schedule for analysis, architecture, governance, and delivery."),
    ])

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        card("Organization", """
<p>NovaDrive is a mid-sized advanced manufacturing company specializing in robotics, automated material handling, and industrial IoT-enabled production systems. The environment blends corporate IT, cloud platforms (AWS, Azure, and a private cloud), and OT operations including PLCs, SCADA, HMIs, AMRs, and private 5G infrastructure.</p>
<p>The organization operates in a high-risk space where production uptime, engineering IP, and supply chain reliability are tightly linked to cybersecurity maturity.</p>""")
    with c2:
        card("Consulting Focus", """
<p>This project centers on ransomware readiness within NovaDrive's cloud environment and the related governance, architecture, monitoring, and recovery capabilities needed to reduce operational risk.</p>
<p>NovaDrive's current architecture includes flat networks, limited monitoring, inconsistent identity controls, and ungoverned vendor access — all of which elevate operational and financial risk.</p>""")

    st.markdown('<div class="pill-div"></div>', unsafe_allow_html=True)
    tag_row(["Project Charter", "Threat Modeling", "Current-State Assessment",
             "Gap Analysis & Maturity", "Security Architecture",
             "Governance & Policy", "Roadmap & Financials"])

# ══════════════════════════════════════════════════════════════════════════════
# PART 1 — PROJECT CHARTER
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Part 1":

    sec_header("Part 1", "Project Charter & Engagement Definition",
               "Scope, stakeholders, assumptions, milestones, and measurable outcomes.")

    t1, t2, t3 = st.tabs(["Background & Scope", "Assumptions & Milestones", "Success Metrics"])

    with t1:
        met_grid([
            ("IT + OT + Cloud", "Connected Environment", "One weakness can affect multiple systems."),
            ("JIT", "Business Model", "Downtime quickly creates production and contract risk."),
            ("Ransomware", "Primary Challenge", "Main focus of the engagement."),
            ("Cloud Controls", "Project Scope", "Assessment focuses on cloud ransomware readiness."),
        ])

        callout(
            "<strong>Business problem:</strong> NovaDrive must protect its interconnected IT, OT, and cloud environment from ransomware because one exposed cloud resource or stolen credential can spread into production systems.",
            "danger"
        )

        st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Business Risk Chain</h3>", unsafe_allow_html=True)

        st.markdown("""
        <div class="flow-grid" style="grid-template-columns:repeat(4,1fr);">
            <div class="flow-step">
                <span class="flow-num">01</span>
                <span class="flow-name">Cloud Misconfiguration</span>
                <span class="flow-desc">Exposed storage or weak access controls create entry points.</span>
            </div>
            <div class="flow-step">
                <span class="flow-num">02</span>
                <span class="flow-name">Credential Compromise</span>
                <span class="flow-desc">Attackers use stolen credentials to access internal systems.</span>
            </div>
            <div class="flow-step">
                <span class="flow-num">03</span>
                <span class="flow-name">IT/OT Spread</span>
                <span class="flow-desc">Flat networks allow movement toward production systems.</span>
            </div>
            <div class="flow-step">
                <span class="flow-num">04</span>
                <span class="flow-name">JIT Disruption</span>
                <span class="flow-desc">Production delays create financial and contractual penalties.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Stakeholder Map</h3>", unsafe_allow_html=True)

        c1, c2, c3, c4, c5 = st.columns(5, gap="medium")

        with c1:
            card("👔 Executive", """
<p><strong>CFO · CISO · CIO</strong></p>
<p>Own risk appetite, budget approval, cyber insurance, and strategic alignment.</p>
""", "accent")

        with c2:
            card("💻 Technical", """
<p><strong>IT · Cloud · SOC · IR</strong></p>
<p>Implement IAM, CSPM, SIEM, segmentation, monitoring, and response controls.</p>
""", "good")

        with c3:
            card("🏭 Operational", """
<p><strong>Plant Engineers · OT Teams</strong></p>
<p>Ensure security improvements do not disrupt production uptime or safety.</p>
""", "warn")

        with c4:
            card("⚖️ Compliance", """
<p><strong>Legal · Risk · OEMs</strong></p>
<p>Support contractual, regulatory, audit, and customer trust requirements.</p>
""", "danger")

        with c5:
            card("🔗 External Partners", """
<p><strong>OEMs · Vendors · Supply Chain</strong></p>
<p>Production delays from ransomware can disrupt contracts, create penalties, and damage long-term partner trust.</p>
""", "danger")

        st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Scope Boundaries</h3>", unsafe_allow_html=True)

        st.markdown("""
        <table class="nd-table">
            <thead>
                <tr>
                    <th>In Scope</th>
                    <th>Out of Scope</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Cloud IAM</strong><br>Identity, access, MFA, least privilege</td>
                    <td><strong>Full OT/ICS Redesign</strong><br>Plant-floor redesign requires separate long-term effort</td>
                </tr>
                <tr>
                    <td><strong>Cloud Configuration</strong><br>CSPM readiness and misconfiguration detection</td>
                    <td><strong>Physical Security</strong><br>Facilities and physical access are outside this cloud-focused assessment</td>
                </tr>
                <tr>
                    <td><strong>Logging & Monitoring</strong><br>Cloud logs, SIEM inputs, detection readiness</td>
                    <td><strong>ERP Modernization</strong><br>Business system replacement is outside engagement scope</td>
                </tr>
                <tr>
                    <td><strong>Incident Response & Backups</strong><br>Cloud IR, recovery, ransomware resilience</td>
                    <td><strong>Vendor Contract Renegotiation</strong><br>Vendor terms may be reviewed later but are not redesigned here</td>
                </tr>
                <tr>
                    <td><strong>Cloud Segmentation & Training</strong><br>Reducing ransomware spread and employee risk</td>
                    <td><strong>Endpoint Security Program</strong><br>EDR, patching, and device hardening remain Corporate IT responsibilities</td>
                </tr>
            </tbody>
        </table>
        """, unsafe_allow_html=True)

    with t2:
        met_grid([
            ("Existing IAM", "Assumption", "AWS Directory Service + IAM Identity Center remain in place."),
            ("Cloud Misconfig", "Primary Entry Risk", "Cloud exposure is treated as the main ransomware pathway."),
            ("Minimal Downtime", "Constraint", "JIT manufacturing limits disruptive testing."),
            ("Budget Limits", "Constraint", "Tool selection may depend on available funding."),
        ])

        c1, c2 = st.columns(2, gap="medium")

        with c1:
            card("Defined Assumptions", """
<ul>
<li>NovaDrive will continue using AWS Directory Service integrated with IAM Identity Center.</li>
<li>Cloud misconfiguration remains the primary ransomware entry point.</li>
<li>Cloud and IT teams are available for interviews and data gathering.</li>
<li>No major cloud migration will occur during the project.</li>
</ul>
""", "accent")

        with c2:
            card("Constraints", """
<ul>
<li>JIT manufacturing requires minimal downtime during assessment.</li>
<li>OT systems cannot be significantly altered due to legacy dependencies.</li>
<li>Budget limitations may affect tool selection such as CSPM and SIEM/SOC.</li>
<li>Vendor-managed robotics create uncontrolled access pathways.</li>
</ul>
""", "warn")

        st.markdown(
        "<h3 style='margin-top:1.5rem;color:var(--text);'>8-Week Milestone Timeline</h3>",
            unsafe_allow_html=True
    )

        components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
body {
    background: transparent;
    margin: 0;
    font-family: Arial, sans-serif;
}

.timeline-wrap {
    background: #0d1b2d;
    border: 1px solid rgba(173,200,255,0.18);
    border-radius: 18px;
    padding: 95px 34px 55px;
    overflow: visible;
}

.timeline {
    position: relative;
    width: 100%;
    height: 160px;
    overflow: visible;
}

.line {
    position: absolute;
    top: 52px;
    left: 2%;
    right: 2%;
    height: 4px;
    background: linear-gradient(90deg, #7cc6ff, #8b9dff, #ffcf7d, #80d7a5);
    border-radius: 999px;
}

.node {
    position: absolute;
    top: 42px;
    width: 24px;
    height: 24px;
    background: #07111f;
    border: 3px solid #7cc6ff;
    border-radius: 50%;
    cursor: pointer;
    transform: translateX(-50%);
    transition: 0.2s ease;
    z-index: 2;
}

.node:hover {
    background: #7cc6ff;
    transform: translateX(-50%) scale(1.18);
}

.label {
    position: absolute;
    top: 78px;
    left: 50%;
    transform: translateX(-50%);
    color: #b7c7df;
    font-size: 12px;
    white-space: nowrap;
    font-weight: 700;
}

.tooltip {
    visibility: hidden;
    opacity: 0;
    width: 260px;
    background: #11243b;
    color: #eaf2ff;
    text-align: left;
    padding: 12px 14px;
    border-radius: 12px;
    position: absolute;
    bottom: 48px;
    left: 50%;
    transform: translateX(-50%);
    transition: 0.2s ease;
    border: 1px solid rgba(173,200,255,0.25);
    box-shadow: 0 12px 30px rgba(0,0,0,0.35);
    font-size: 13px;
    line-height: 1.45;
    z-index: 999;
}

.tooltip b {
    color: #7cc6ff;
    display: block;
    margin-bottom: 4px;
}

.node:hover .tooltip {
    visibility: visible;
    opacity: 1;
}

.small-note {
    color: #8fa6c7;
    font-size: 13px;
    margin-top: 45px;
    text-align: center;
}
                        
.node.edge-left .tooltip {
    left: 0;
    transform: translateX(0);
}

.node.edge-right .tooltip {
    left: auto;
    right: 0;
    transform: translateX(0);
}
</style>
</head>

<body>
<div class="timeline-wrap">
    <div class="timeline">
        <div class="line"></div>

        <div class="node edge-left" style="left:2%;">
            <div class="tooltip"><b>Week 1 — Project Charter</b>Start engagement definition, scope, assumptions, and stakeholders.</div>
            <div class="label">Week 1</div>
        </div>

        <div class="node" style="left:16%;">
            <div class="tooltip"><b>Week 2 — Charter Complete</b>Finalize charter and begin threat modeling.</div>
            <div class="label">Week 2</div>
        </div>

        <div class="node" style="left:30%;">
            <div class="tooltip"><b>Week 3 — Threat Modeling</b>Continue MITRE ATT&CK mapping and attack path analysis.</div>
            <div class="label">Week 3</div>
        </div>

        <div class="node" style="left:44%;">
            <div class="tooltip"><b>Week 4 — Assessment Complete</b>Complete threat modeling and begin architecture design.</div>
            <div class="label">Week 4</div>
        </div>

        <div class="node" style="left:58%;">
            <div class="tooltip"><b>Week 5 — Architecture Design</b>Continue target-state architecture and governance planning.</div>
            <div class="label">Week 5</div>
        </div>

        <div class="node" style="left:72%;">
            <div class="tooltip"><b>Week 6 — Report Buildout</b>Compile written report and presentation materials.</div>
            <div class="label">Week 6</div>
        </div>

        <div class="node" style="left:86%;">
            <div class="tooltip"><b>Week 7 — Finalize Design</b>Complete architecture, governance, and final deliverables.</div>
            <div class="label">Week 7</div>
        </div>

        <div class="node edge-right" style="left:98%;">
            <div class="tooltip"><b>Week 8 — Final Delivery</b>Submit written report and deliver formal presentation.</div>
            <div class="label">Week 8</div>
        </div>
    </div>

    <div class="small-note">Hover over each node to view milestone details.</div>
</div>
</body>
</html>
""", height=360)

    with t3:
        for num, title, metric, outcome in [
            ("01", "Milestone & Schedule Adherence",
             "On-time delivery of all project phases.",
             "100% of the 4 primary milestones (Discovery, Assessment, Risk Analysis, and Final Recommendations) submitted by the end of Week 8."),
            ("02", "Technical Accuracy & Framework Alignment",
             "Proper application of industry-standard frameworks (e.g., NIST, STRIDE, or Zero Trust).",
             "100% of identified threats and proposed solutions are mapped to specific framework controls or academic principles discussed in the MSIS program."),
            ("03", "Deliverable Quality & Professionalism",
             "Submission of Executive-Ready artifacts.",
             "Final documentation contains zero critical formatting errors and includes at least three professional artifacts (e.g., Network Diagrams, Budget Tables, or Risk Heat Maps)."),
        ]:
            st.markdown(f"""
            <div class="card accent" style="margin-bottom:0.8rem;display:flex;gap:1.2rem;align-items:flex-start;">
                <div style="font-size:1.6rem;font-weight:800;color:rgba(173,200,255,0.18);flex-shrink:0;line-height:1;padding-top:2px;">{num}</div>
                <div>
                    <h3 style="margin:0 0 0.5rem;font-size:0.96rem;">{title}</h3>
                    <p style="margin-bottom:0.4rem;"><strong>Metric:</strong> {metric}</p>
                    <p><strong>Outcome:</strong> {outcome}</p>
                </div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PART 2 — THREAT MODELING + 2A + 2B
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Part 2":

    sec_header("Part 2", "Threat Modeling, Assessment & Gap Analysis",
               "MITRE ATT&CK adversary analysis, current-state review, and maturity scoring.")

    main_tabs = st.tabs([
        "Threat Modeling & Adversary Analysis",
        "02A — Current-State Assessment",
        "02B — Gap Analysis & Maturity",
    ])

    # ════════════════════════════════════
    # THREAT MODELING
    # ════════════════════════════════════
    with main_tabs[0]:
        threat_inner = st.tabs(["MITRE ATT&CK & Attack Path", "Likelihood & Impact Analysis", "Risk Register"])

        with threat_inner[0]:
            callout("The MITRE ATT&CK Framework provides a structured knowledge base of real-world adversary tactics and techniques to help organizations understand, detect, and defend against cybercrimes. The relevant techniques based on NovaDrive's architecture have been applied below.")
            met_grid([
                ("5", "Attack Stages", "From cloud entry to ransomware impact."),
                ("3", "Highest-Risk Themes", "Cloud misconfiguration, weak IAM, and flat networks."),
                ("JIT", "Business Exposure", "Downtime immediately affects production and contracts."),
                ("Zero Trust", "Defensive Direction", "Verify access, contain movement, and recover quickly."),
            ])

            st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Attack Path: How Ransomware Reaches Production</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="exec-grid">
                <div class="exec-step">
                    <div class="exec-num">Step 01</div>
                    <div class="exec-icon">☁️</div>
                    <div class="exec-title">Cloud Misconfiguration</div>
                    <div class="exec-copy">An exposed Azure/AWS resource creates the first opening for attackers.</div>
                </div>
                <div class="exec-step">
                    <div class="exec-num">Step 02</div>
                    <div class="exec-icon">🔑</div>
                    <div class="exec-title">Credential Access</div>
                    <div class="exec-copy">Weak MFA and overly permissive roles allow unauthorized access.</div>
                </div>
                <div class="exec-step">
                    <div class="exec-num">Step 03</div>
                    <div class="exec-icon">↔️</div>
                    <div class="exec-title">Lateral Movement</div>
                    <div class="exec-copy">Flat networks let malware move from cloud/IT toward OT systems.</div>
                </div>
                <div class="exec-step">
                    <div class="exec-num">Step 04</div>
                    <div class="exec-icon">🏭</div>
                    <div class="exec-title">OT Compromise</div>
                    <div class="exec-copy">PLCs, SCADA, robotics, and vendor pathways become exposed.</div>
                </div>
                <div class="exec-step">
                    <div class="exec-num">Step 05</div>
                    <div class="exec-icon">🚨</div>
                    <div class="exec-title">Ransomware Impact</div>
                    <div class="exec-copy">Production systems are encrypted, delaying shipments and triggering penalties.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="impact-strip">
                <div class="impact-card">
                    <div class="big">Entry</div>
                    <div class="small">Cloud misconfiguration and phishing create the most likely starting points.</div>
                </div>
                <div class="impact-card">
                    <div class="big">Spread</div>
                    <div class="small">Weak IAM and limited segmentation increase blast radius.</div>
                </div>
                <div class="impact-card">
                    <div class="big">Impact</div>
                    <div class="small">Ransomware can stop JIT manufacturing and create financial/contractual losses.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)


            components.html("""
<style>
.wrapper {
    overflow-x: auto;
    padding: 10px 0;
}

.flow {
    display: flex;
    align-items: center;
    gap: 18px;
    width: max-content;
}

/* BIG CARDS */
.card {
    min-width: 340px;
    max-width: 360px;
    background: #0d1b2d;
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(173,200,255,0.12);
    color: #eaf2ff;
}

.card h4 {
    margin-bottom: 12px;
    font-size: 20px;
}

.card p {
    margin: 8px 0;
    font-size: 14.5px;
    color: #b7c7df;
    line-height: 1.5;
}

/* COLORS MATCH YOUR ORIGINAL */
.red    { border-left: 4px solid #ff9a9a; }
.yellow { border-left: 4px solid #ffcf7d; }
.blue   { border-left: 4px solid #7cc6ff; }

.label {
    color: #7cc6ff;
    font-weight: 600;
}

/* ARROWS */
.arrow {
    font-size: 30px;
    color: #7cc6ff;
}
</style>

<div class="wrapper">
<div class="flow">

<!-- 1 -->
<div class="card red">
<h4>Initial Access</h4>
<p><span class="label">Technique:</span> phishing or cloud misconfiguration</p>
<p><span class="label">NovaDrive risk:</span> exposed AWS/Azure resources allow attackers into the cloud and corporate environment.</p>
<p><span class="label">Control:</span> CSPM scanning, secure cloud baselines, phishing simulations.</p>
</div>

<div class="arrow">→</div>

<!-- 2 -->
<div class="card yellow">
<h4>Credential Access</h4>
<p><span class="label">Technique:</span> stolen or weak credentials</p>
<p><span class="label">NovaDrive risk:</span> unauthorized access to cloud platforms, ERP, engineering data, and contracts.</p>
<p><span class="label">Control:</span> universal MFA, least privilege IAM, RBAC cleanup.</p>
</div>

<div class="arrow">→</div>

<!-- 3 -->
<div class="card red">
<h4>Lateral Movement</h4>
<p><span class="label">Technique:</span> movement across internal systems</p>
<p><span class="label">NovaDrive risk:</span> ransomware spreads from IT/cloud toward OT and production systems.</p>
<p><span class="label">Control:</span> micro-segmentation, VPC isolation, ZTNA, network monitoring.</p>
</div>

<div class="arrow">→</div>

<!-- 4 -->
<div class="card blue">
<h4>Persistence</h4>
<p><span class="label">Technique:</span> long-term hidden access</p>
<p><span class="label">NovaDrive risk:</span> attackers remain undetected, increasing damage and data exposure.</p>
<p><span class="label">Control:</span> SIEM, CloudTrail, SOC monitoring, anomaly detection.</p>
</div>

<div class="arrow">→</div>

<!-- 5 -->
<div class="card yellow">
<h4>Data Exfiltration</h4>
<p><span class="label">Technique:</span> stealing sensitive information</p>
<p><span class="label">NovaDrive risk:</span> engineering designs, contracts, production data, and employee records are exposed.</p>
<p><span class="label">Control:</span> encryption, DLP-style monitoring, unusual access alerts.</p>
</div>

<div class="arrow">→</div>

<!-- 6 -->
<div class="card red">
<h4>Impact: Ransomware</h4>
<p><span class="label">Technique:</span> encryption for operational disruption</p>
<p><span class="label">NovaDrive risk:</span> production shutdown affects JIT contracts and creates major financial loss.</p>
<p><span class="label">Control:</span> immutable backups, automated IR playbooks, rapid recovery process.</p>
</div>

</div>
</div>
""", height=260)

            callout("<strong>Main takeaway:</strong> NovaDrive's greatest ransomware risk is not one isolated technical flaw. It is the chain reaction created when cloud misconfiguration, weak identity controls, and flat IT/OT networks combine into one attack path.", "warn")

            st.markdown("<h3 style='margin-top:1.3rem;color:var(--text);'>Attack Path Narrative</h3>", unsafe_allow_html=True)

            with st.expander("1. What happens first?", expanded=False):
                st.write(
        "An attacker identifies a misconfigured cloud resource and uses exposed credentials "
        "to authenticate into NovaDrive’s environment. Because MFA is not universal and IAM roles "
        "are too broad, the attacker has a realistic path to escalate privileges."
                )

            with st.expander("2. Why does it spread?", expanded=False):
                st.write(
        "Several parts of the environment still rely on flat network architecture. Once inside, "
        "the attacker can pivot from cloud-connected IT systems toward operational technology "
        "with limited resistance."
                )

            with st.expander("3. Why does OT matter?", expanded=False):
                st.write(
        "OT systems control robotics, PLCs, SCADA, and production workflows. If these systems "
        "are disrupted, NovaDrive does not just lose data; it loses manufacturing uptime."
                )

            with st.expander("4. What is the business result?", expanded=False):
                st.write(
        "A ransomware event can halt JIT production, delay shipments, trigger contractual penalties, "
        "and damage customer trust. This is why the recommended architecture prioritizes identity, "
        "segmentation, monitoring, and recovery."
                )

        # ── Sub-tab 1: Likelihood & Impact ──
        with threat_inner[1]:

            def lvl_color(val):
                return {"Very High": "#ff9a9a", "High": "#ffcf7d", "Medium": "#7cc6ff", "Low": "#80d7a5"}.get(val, "#8fa6c7")

            threat_df = pd.DataFrame([
                {"Threat": "Cloud Misconfiguration", "Likelihood": "High",   "Impact": "High",      "L": 3, "I": 3, "Rationale": "Azure storage already misconfigured."},
                {"Threat": "Identity Compromise",     "Likelihood": "High",   "Impact": "High",      "L": 3, "I": 3, "Rationale": "MFA not universal; overly permissive IAM."},
                {"Threat": "OT Disruption",           "Likelihood": "Medium", "Impact": "Very High", "L": 2, "I": 4, "Rationale": "Legacy protocols + vendor access."},
                {"Threat": "Lateral Movement",        "Likelihood": "High",   "Impact": "High",      "L": 3, "I": 3, "Rationale": "Flat networks in older plants."},
                {"Threat": "Data Exfiltration",       "Likelihood": "Medium", "Impact": "High",      "L": 2, "I": 3, "Rationale": "Sensitive engineering data stored in cloud."},
                {"Threat": "Ransomware Deployment",   "Likelihood": "High",   "Impact": "Very High", "L": 3, "I": 4, "Rationale": "No SIEM, no SOC, no immutable backups."},
            ])

            # Dropdown filter
            lf_col, _, _ = st.columns([2, 2, 2])
            with lf_col:
                lik_filter = st.selectbox("Filter by Likelihood", ["All", "High", "Medium", "Low"], key="lik_filter")
            ft = threat_df if lik_filter == "All" else threat_df[threat_df["Likelihood"] == lik_filter]

            # Heat map
            color_map_h = {3: "#ff9a9a", 2: "#ffcf7d", 1: "#80d7a5", 4: "#cc4444"}
            mcolors = [color_map_h.get(min((r["L"] * r["I"]) // 3, 4), "#7cc6ff") for _, r in ft.iterrows()]
            fig_heat = go.Figure()
            for zone in [
                (0.5,0.5,1.5,1.5,"rgba(128,215,165,0.10)"),
                (1.5,1.5,2.5,2.5,"rgba(255,207,125,0.10)"),
                (2.5,2.5,3.5,4.5,"rgba(255,154,154,0.14)"),
                (1.5,2.5,2.5,4.5,"rgba(255,154,154,0.08)"),
                (2.5,0.5,3.5,2.5,"rgba(255,207,125,0.08)"),
            ]:
                fig_heat.add_shape(type="rect", x0=zone[0], y0=zone[1], x1=zone[2], y1=zone[3], fillcolor=zone[4], line_width=0)
            fig_heat.add_trace(go.Scatter(
                x=ft["L"], y=ft["I"],
                mode="markers+text",
                text=ft["Threat"],
                textposition="top center",
                textfont=dict(size=11, color="#eaf2ff"),
                marker=dict(size=18, color=mcolors, line=dict(color="rgba(255,255,255,0.2)", width=1)),
                customdata=ft[["Rationale","Likelihood","Impact"]].values,
                hovertemplate="<b>%{text}</b><br>Likelihood: %{customdata[1]}<br>Impact: %{customdata[2]}<br><i>%{customdata[0]}</i><extra></extra>",
            ))
            fig_heat.update_layout(
                title=dict(text="Threat Heat Map — Likelihood × Impact (hover for rationale)", font=dict(color="#eaf2ff", size=14)),
                paper_bgcolor="rgba(9,20,34,0)", plot_bgcolor="rgba(13,27,45,0.6)",
                font=dict(color="#b7c7df", family="Inter"),
                xaxis=dict(title="Likelihood", tickvals=[1,2,3], ticktext=["Low","Medium","High"],
                           range=[0.5,3.5], gridcolor="rgba(173,200,255,0.08)", zeroline=False,
                           title_font=dict(color="#8fa6c7"), tickfont=dict(color="#8fa6c7")),
                yaxis=dict(title="Impact", tickvals=[1,2,3,4], ticktext=["Low","Medium","High","Very High"],
                           range=[0.5,4.5], gridcolor="rgba(173,200,255,0.08)", zeroline=False,
                           title_font=dict(color="#8fa6c7"), tickfont=dict(color="#8fa6c7")),
                height=430, margin=dict(l=60, r=20, t=55, b=50),
            )
            st.plotly_chart(fig_heat, use_container_width=True)

            # Bar charts
            bc1, bc2 = st.columns(2, gap="medium")
            with bc1:
                lc = ft["Likelihood"].value_counts().reindex(["High","Medium","Low"], fill_value=0)
                fig_l = go.Figure(go.Bar(x=lc.index, y=lc.values, marker_color=["#ff9a9a","#ffcf7d","#80d7a5"],
                                         text=lc.values, textposition="outside", textfont=dict(color="#eaf2ff"),
                                         hovertemplate="%{x}: %{y} threats<extra></extra>"))
                fig_l.update_layout(title=dict(text="Threats by Likelihood", font=dict(color="#eaf2ff", size=13)),
                    paper_bgcolor="rgba(9,20,34,0)", plot_bgcolor="rgba(13,27,45,0.6)", font=dict(color="#b7c7df", family="Inter"),
                    xaxis=dict(gridcolor="rgba(173,200,255,0.08)", tickfont=dict(color="#8fa6c7")),
                    yaxis=dict(gridcolor="rgba(173,200,255,0.08)", tickfont=dict(color="#8fa6c7"), title="Count"),
                    height=300, margin=dict(l=40, r=20, t=45, b=40))
                st.plotly_chart(fig_l, use_container_width=True)
            with bc2:
                ic = ft["Impact"].value_counts().reindex(["Very High","High","Medium","Low"], fill_value=0)
                fig_i = go.Figure(go.Bar(x=ic.index, y=ic.values, marker_color=["#cc4444","#ff9a9a","#ffcf7d","#80d7a5"],
                                         text=ic.values, textposition="outside", textfont=dict(color="#eaf2ff"),
                                         hovertemplate="%{x}: %{y} threats<extra></extra>"))
                fig_i.update_layout(title=dict(text="Threats by Impact", font=dict(color="#eaf2ff", size=13)),
                    paper_bgcolor="rgba(9,20,34,0)", plot_bgcolor="rgba(13,27,45,0.6)", font=dict(color="#b7c7df", family="Inter"),
                    xaxis=dict(gridcolor="rgba(173,200,255,0.08)", tickfont=dict(color="#8fa6c7")),
                    yaxis=dict(gridcolor="rgba(173,200,255,0.08)", tickfont=dict(color="#8fa6c7"), title="Count"),
                    height=300, margin=dict(l=40, r=20, t=45, b=40))
                st.plotly_chart(fig_i, use_container_width=True)

            # Threat table
            st.markdown("""<div style="display:grid;grid-template-columns:2fr 1fr 1fr 2.5fr;
                background:rgba(0,0,0,0.18);border:1px solid rgba(173,200,255,0.14);
                border-radius:14px 14px 0 0;padding:0.6rem 1rem;">
                <span style="font-family:'JetBrains Mono',monospace;font-size:0.63rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--text);">Threat</span>
                <span style="font-family:'JetBrains Mono',monospace;font-size:0.63rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--text);">Likelihood</span>
                <span style="font-family:'JetBrains Mono',monospace;font-size:0.63rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--text);">Impact</span>
                <span style="font-family:'JetBrains Mono',monospace;font-size:0.63rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--text);">Rationale</span>
            </div>""", unsafe_allow_html=True)
            for _, row in ft.iterrows():
                st.markdown(f"""<div style="display:grid;grid-template-columns:2fr 1fr 1fr 2.5fr;
                    border-left:1px solid rgba(173,200,255,0.10);border-right:1px solid rgba(173,200,255,0.10);
                    border-bottom:1px solid rgba(173,200,255,0.08);background:rgba(13,27,45,0.6);padding:0.75rem 1rem;">
                    <span style="font-size:0.87rem;font-weight:600;color:var(--text);">{row['Threat']}</span>
                    <span style="font-size:0.82rem;font-weight:700;color:{lvl_color(row['Likelihood'])};">{row['Likelihood']}</span>
                    <span style="font-size:0.82rem;font-weight:700;color:{lvl_color(row['Impact'])};">{row['Impact']}</span>
                    <span style="font-size:0.83rem;color:var(--muted);">{row['Rationale']}</span>
                </div>""", unsafe_allow_html=True)

        # ── Sub-tab 2: Risk Register ──
        with threat_inner[2]:

            risk_df = pd.DataFrame([
                {"Risk": "Misconfigured cloud storage",   "Likelihood": "High",   "Impact": "High",      "L": 3, "I": 3, "Owner": "Cloud Engineering", "Mitigation": "Implement CSPM and private-by-default storage configurations."},
                {"Risk": "Weak IAM governance",            "Likelihood": "High",   "Impact": "High",      "L": 3, "I": 3, "Owner": "IT Security",        "Mitigation": "Enforce MFA, least privilege access, and regular IAM access reviews."},
                {"Risk": "No SIEM/SOC",                    "Likelihood": "High",   "Impact": "Very High", "L": 3, "I": 4, "Owner": "CISO",               "Mitigation": "Deploy SIEM + cloud-native SOC (e.g., Microsoft Sentinel)."},
                {"Risk": "Flat OT network separation",     "Likelihood": "Medium", "Impact": "Very High", "L": 2, "I": 4, "Owner": "OT Engineering",     "Mitigation": "Implement network segmentation, VPCs, and hardware-level separation."},
                {"Risk": "Vendor remote access",           "Likelihood": "Medium", "Impact": "High",      "L": 2, "I": 3, "Owner": "OT + Security",      "Mitigation": "Implement Zero-Trust vendor access, session recording, and JIT access."},
                {"Risk": "Legacy OT protocols",            "Likelihood": "Medium", "Impact": "High",      "L": 2, "I": 3, "Owner": "OT Engineering",     "Mitigation": "Utilize network isolation and compensating controls (e.g., protocol gateways)."},
                {"Risk": "Inconsistent logging integrity", "Likelihood": "High",   "Impact": "High",      "L": 3, "I": 3, "Owner": "IT + OT",            "Mitigation": "Establish centralized logging, CloudTrail monitoring, and log-integrity checks."},
            ])
            risk_df["Score"] = risk_df["L"] * risk_df["I"]

            # Dropdowns
            rc1, rc2, rc3 = st.columns([2, 2, 2])
            with rc1:
                owner_f = st.selectbox("Filter by Owner", ["All Owners"] + sorted(risk_df["Owner"].unique().tolist()), key="owner_f")
            with rc2:
                impact_f = st.selectbox("Filter by Impact", ["All", "Very High", "High", "Medium"], key="impact_f")
            with rc3:
                sort_f = st.selectbox("Sort by", ["Risk Score (High→Low)", "Owner", "Likelihood"], key="sort_f")

            fr = risk_df.copy()
            if owner_f != "All Owners":
                fr = fr[fr["Owner"] == owner_f]
            if impact_f != "All":
                fr = fr[fr["Impact"] == impact_f]
            if sort_f == "Risk Score (High→Low)":
                fr = fr.sort_values("Score", ascending=False)
            elif sort_f == "Owner":
                fr = fr.sort_values("Owner")
            else:
                fr = fr.sort_values("L", ascending=False)

            # Bubble chart
            fig_bub = go.Figure()
            for _, row in fr.iterrows():
                sc = row["Score"]
                bc = "#cc4444" if sc >= 9 else "#ff9a9a" if sc >= 6 else "#ffcf7d"
                fig_bub.add_trace(go.Scatter(
                    x=[row["L"]], y=[row["I"]], mode="markers+text",
                    text=[row["Risk"]], textposition="top center",
                    textfont=dict(size=10, color="#eaf2ff"),
                    marker=dict(size=sc * 8, color=bc, opacity=0.75, line=dict(color="rgba(255,255,255,0.2)", width=1)),
                    hovertemplate=f"<b>{row['Risk']}</b><br>Owner: {row['Owner']}<br>Score: {sc}<br>{row['Mitigation']}<extra></extra>",
                    showlegend=False,
                ))
            fig_bub.update_layout(
                title=dict(text="Risk Register — Bubble Size = Risk Score · Hover for Mitigation", font=dict(color="#eaf2ff", size=14)),
                paper_bgcolor="rgba(9,20,34,0)", plot_bgcolor="rgba(13,27,45,0.6)",
                font=dict(color="#b7c7df", family="Inter"),
                xaxis=dict(title="Likelihood", tickvals=[1,2,3], ticktext=["Low","Medium","High"],
                           range=[0.5,3.5], gridcolor="rgba(173,200,255,0.08)", zeroline=False,
                           title_font=dict(color="#8fa6c7"), tickfont=dict(color="#8fa6c7")),
                yaxis=dict(title="Impact", tickvals=[1,2,3,4], ticktext=["Low","Medium","High","Very High"],
                           range=[0.5,4.5], gridcolor="rgba(173,200,255,0.08)", zeroline=False,
                           title_font=dict(color="#8fa6c7"), tickfont=dict(color="#8fa6c7")),
                height=430, margin=dict(l=60, r=20, t=55, b=50),
            )
            st.plotly_chart(fig_bub, use_container_width=True)

            # Horizontal bar + donut
            bar_col, donut_col = st.columns([1.3, 1], gap="medium")
            with bar_col:
                sb = fr.sort_values("Score")
                bcs = ["#cc4444" if s >= 9 else "#ff9a9a" if s >= 6 else "#ffcf7d" for s in sb["Score"]]
                fig_bar2 = go.Figure(go.Bar(
                    x=sb["Score"], y=sb["Risk"], orientation="h",
                    marker_color=bcs, text=sb["Score"],
                    textposition="outside", textfont=dict(color="#eaf2ff"),
                    hovertemplate="%{y}: %{x}<extra></extra>",
                ))
                fig_bar2.update_layout(
                    title=dict(text="Prioritized Risk Scores", font=dict(color="#eaf2ff", size=13)),
                    paper_bgcolor="rgba(9,20,34,0)", plot_bgcolor="rgba(13,27,45,0.6)",
                    font=dict(color="#b7c7df", family="Inter"),
                    xaxis=dict(title="Score", range=[0,14], gridcolor="rgba(173,200,255,0.08)",
                               tickfont=dict(color="#8fa6c7"), title_font=dict(color="#8fa6c7")),
                    yaxis=dict(gridcolor="rgba(173,200,255,0.08)", tickfont=dict(color="#eaf2ff", size=11)),
                    height=max(280, len(sb) * 52), margin=dict(l=200, r=50, t=45, b=40),
                )
                st.plotly_chart(fig_bar2, use_container_width=True)

            with donut_col:
                oc = fr["Owner"].value_counts()
                fig_donut2 = go.Figure(go.Pie(
                    labels=oc.index, values=oc.values, hole=0.55,
                    marker=dict(colors=["#7cc6ff","#8b9dff","#80d7a5","#ffcf7d","#ff9a9a"]),
                    textfont=dict(color="#eaf2ff", size=11),
                    hovertemplate="%{label}: %{value} risks<extra></extra>",
                ))
                fig_donut2.update_layout(
                    title=dict(text="Risk by Owner", font=dict(color="#eaf2ff", size=13)),
                    paper_bgcolor="rgba(9,20,34,0)", font=dict(color="#b7c7df", family="Inter"),
                    legend=dict(font=dict(color="#b7c7df", size=11), bgcolor="rgba(0,0,0,0)"),
                    height=320, margin=dict(l=10, r=10, t=45, b=10),
                )
                st.plotly_chart(fig_donut2, use_container_width=True)

                # Score legend
                for label, color, desc in [
                    ("Critical 9–12", "#cc4444", "Immediate action required"),
                    ("High 6–8",      "#ff9a9a", "Priority — Phase 1–2 roadmap"),
                    ("Medium 3–5",    "#ffcf7d", "Address within program scope"),
                ]:
                    st.markdown(f"""<div style="display:flex;align-items:center;gap:0.7rem;padding:0.55rem 0.8rem;
                        background:rgba(13,27,45,0.8);border:1px solid rgba(173,200,255,0.10);
                        border-left:3px solid {color};border-radius:8px;margin-bottom:0.4rem;">
                        <span style="font-family:'JetBrains Mono',monospace;font-size:0.76rem;font-weight:700;color:{color};min-width:100px;">{label}</span>
                        <span style="font-size:0.82rem;color:var(--muted);">{desc}</span>
                    </div>""", unsafe_allow_html=True)

            # Full risk register table
            st.markdown("<h3 style='color:var(--text);margin-top:1.2rem;margin-bottom:0.6rem;'>Full Risk Register</h3>", unsafe_allow_html=True)
            cols = ["Risk", "Likelihood", "Impact", "Score", "Owner", "Mitigation Strategy"]
            hdr_html = "<div style=\"display:grid;grid-template-columns:2fr 1fr 1fr 0.6fr 1fr 2.8fr;background:rgba(0,0,0,0.18);border:1px solid rgba(173,200,255,0.14);border-radius:14px 14px 0 0;padding:0.6rem 0.9rem;\">"
            for c in cols:
                hdr_html += f"<span style=\"font-family:'JetBrains Mono',monospace;font-size:0.63rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--text);\">{c}</span>"
            hdr_html += "</div>"
            st.markdown(hdr_html, unsafe_allow_html=True)
            for _, row in fr.iterrows():
                sc = row["Score"]
                sc_c = "#cc4444" if sc >= 9 else "#ff9a9a" if sc >= 6 else "#ffcf7d"
                st.markdown(f"""<div style="display:grid;grid-template-columns:2fr 1fr 1fr 0.6fr 1fr 2.8fr;
                    border-left:1px solid rgba(173,200,255,0.10);border-right:1px solid rgba(173,200,255,0.10);
                    border-bottom:1px solid rgba(173,200,255,0.08);background:rgba(13,27,45,0.55);
                    padding:0.72rem 0.9rem;align-items:center;">
                    <span style="font-size:0.85rem;font-weight:600;color:var(--text);">{row['Risk']}</span>
                    <span style="font-size:0.82rem;font-weight:700;color:{lvl_color(row['Likelihood'])};">{row['Likelihood']}</span>
                    <span style="font-size:0.82rem;font-weight:700;color:{lvl_color(row['Impact'])};">{row['Impact']}</span>
                    <span style="font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:{sc_c};">{sc}</span>
                    <span style="font-size:0.79rem;color:var(--accent2);">{row['Owner']}</span>
                    <span style="font-size:0.82rem;color:var(--muted);">{row['Mitigation']}</span>
                </div>""", unsafe_allow_html=True)
            st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    # ════════════════════════════════════
    # 02A — CURRENT-STATE ASSESSMENT
    # ════════════════════════════════════
    with main_tabs[1]:
        inner = st.tabs(["Architecture & Assets", "Controls & Governance", "Tooling", "Threat Landscape & Framework"])

        with inner[0]:
            st.markdown("""
            <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0.75rem;margin-bottom:1rem;">
                <div style="background:rgba(13,27,45,0.95);border:1px solid rgba(173,200,255,0.14);border-top:2px solid var(--accent);border-radius:16px;padding:1rem;text-align:center;">
                    <div style="font-size:1.7rem;font-weight:800;color:var(--text);">7</div>
                    <div style="font-family:'JetBrains Mono',monospace;font-size:0.66rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--soft);margin-top:4px;">U.S. Facilities</div>
                    <div style="font-size:0.78rem;color:var(--muted);margin-top:6px;">HQ · 4 Plants · 2 DCs</div>
                </div>
                <div style="background:rgba(13,27,45,0.95);border:1px solid rgba(173,200,255,0.14);border-top:2px solid var(--accent2);border-radius:16px;padding:1rem;text-align:center;">
                    <div style="font-size:1.7rem;font-weight:800;color:var(--text);">1,500</div>
                    <div style="font-family:'JetBrains Mono',monospace;font-size:0.66rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--soft);margin-top:4px;">Employees</div>
                    <div style="font-size:0.78rem;color:var(--muted);margin-top:6px;">IT · OT · Logistics · Remote</div>
                </div>
                <div style="background:rgba(13,27,45,0.95);border:1px solid rgba(173,200,255,0.14);border-top:2px solid var(--warn);border-radius:16px;padding:1rem;text-align:center;">
                    <div style="font-size:1.7rem;font-weight:800;color:var(--text);">2</div>
                    <div style="font-family:'JetBrains Mono',monospace;font-size:0.66rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--soft);margin-top:4px;">Cloud Platforms</div>
                    <div style="font-size:0.78rem;color:var(--muted);margin-top:6px;">AWS · Azure </div>
                </div>
                <div style="background:rgba(13,27,45,0.95);border:1px solid rgba(173,200,255,0.14);border-top:2px solid var(--danger);border-radius:16px;padding:1rem;text-align:center;">
                    <div style="font-size:1.7rem;font-weight:800;color:var(--danger);">Partial</div>
                    <div style="font-family:'JetBrains Mono',monospace;font-size:0.66rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--soft);margin-top:4px;">MFA Coverage</div>
                    <div style="font-size:0.78rem;color:var(--muted);margin-top:6px;">High-risk users only</div>
                </div>
            </div>
            <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.75rem;margin-bottom:1rem;">
                <div style="background:rgba(13,27,45,0.9);border:1px solid rgba(173,200,255,0.10);border-left:3px solid var(--accent);border-radius:14px;padding:0.9rem 1rem;">
                    <div style="font-size:0.78rem;font-weight:700;color:var(--accent);margin-bottom:0.4rem;">Corporate IT</div>
                    <div style="font-size:0.8rem;color:var(--muted);line-height:1.6;">Windows 11 endpoints · ERP · HR/Payroll · M365 · AWS Directory + IAM Identity Center (SSO/RBAC) · SD-WAN across all sites</div>
                </div>
                <div style="background:rgba(13,27,45,0.9);border:1px solid rgba(173,200,255,0.10);border-left:3px solid var(--warn);border-radius:14px;padding:0.9rem 1rem;">
                    <div style="font-size:0.78rem;font-weight:700;color:var(--warn);margin-bottom:0.4rem;">OT Environment</div>
                    <div style="font-size:0.8rem;color:var(--muted);line-height:1.6;">PLCs · SCADA · HMIs · AMRs · Private 5G · IIoT sensors · Vendor-managed robotics · Inconsistent monitoring by facility</div>
                </div>
                <div style="background:rgba(13,27,45,0.9);border:1px solid rgba(173,200,255,0.10);border-left:3px solid var(--danger);border-radius:14px;padding:0.9rem 1rem;">
                    <div style="font-size:0.78rem;font-weight:700;color:var(--danger);margin-bottom:0.4rem;">Cloud — Risk Areas</div>
                    <div style="font-size:0.8rem;color:var(--muted);line-height:1.6;">Misconfigured Azure storage · Overly permissive IAM · No CSPM · S3 data lakes · CI/CD pipelines · private cloud</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Asset Inventory & Classification</h3>", unsafe_allow_html=True)
            st.markdown("""
            <table class="nd-table">
            <thead><tr><th>Category</th><th>Criticality</th><th>Key Assets</th><th>Significance</th></tr></thead>
            <tbody>
            <tr>
                <td><strong>IT Assets</strong></td>
                <td><span style="color:var(--warn);font-weight:600;">High</span></td>
                <td>Windows 11 laptops/desktops, shared workstations · VMware/Hyper-V servers · ERP, HR, payroll, financial systems · Microsoft 365 · File storage and shared drives</td>
                <td>Directly impacts business operations, finance, and communication.</td>
            </tr>
            <tr>
                <td><strong>OT Assets</strong></td>
                <td><span style="color:var(--danger);font-weight:600;">Very High</span></td>
                <td>PLCs, HMIs, SCADA platforms · Autonomous Mobile Robots (AMRs) · Inspection robots and assembly robotics · Private 5G network infrastructure · IIoT sensors and edge computing nodes</td>
                <td>Essential for JIT manufacturing and production uptime.</td>
            </tr>
            <tr>
                <td><strong>Cloud Assets</strong></td>
                <td><span style="color:var(--warn);font-weight:600;">High</span></td>
                <td>AWS workloads, IAM Identity Center, S3 data lakes · Azure storage containers · private cloud · Virtual Engineering Workbench and CI/CD pipelines</td>
                <td>Stores engineering data, contracts, and operational telemetry.</td>
            </tr>
            <tr>
                <td><strong>Identity & Access Assets</strong></td>
                <td><span style="color:var(--warn);font-weight:600;">High</span></td>
                <td>AWS Directory Service · IAM Identity Center · MFA systems (partial enforcement)</td>
                <td>Compromise leads to lateral movement and cloud takeover.</td>
            </tr>
            </tbody>
            </table>
            """, unsafe_allow_html=True)

        with inner[1]:
            # ── CONTROLS & GOVERNANCE ────────────────────────────────────────
            st.markdown("<div class='sec-kicker' style='margin-bottom:0.5rem;'>Existing Control Environment</div>", unsafe_allow_html=True)

            # Control status grid: each domain with status pills
            control_domains = [
                {
                    "name": "Identity Controls",
                    "color": "#ffcf7d",
                    "status": "Partial",
                    "status_color": "#ffcf7d",
                    "items": [
                        ("AWS Directory Service + IAM Identity Center", "good"),
                        ("MFA enforced — high-risk users only", "warn"),
                        ("RBAC implemented — not consistently audited", "warn"),
                        ("No structured IAM lifecycle management", "danger"),
                    ],
                },
                {
                    "name": "Endpoint & Network Controls",
                    "color": "#ffcf7d",
                    "status": "Partial",
                    "status_color": "#ffcf7d",
                    "items": [
                        ("Antivirus & firewall monitoring", "good"),
                        ("Centrally managed device configs", "good"),
                        ("VPN for remote access", "good"),
                        ("SD-WAN connecting all facilities", "good"),
                        ("Flat networks in older plants", "danger"),
                    ],
                },
                {
                    "name": "Cloud Controls",
                    "color": "#ff9a9a",
                    "status": "Weak",
                    "status_color": "#ff9a9a",
                    "items": [
                        ("AWS IAM roles and SSO", "good"),
                        ("Azure storage for engineering/contract data", "warn"),
                        ("No CSPM or misconfiguration scanning", "danger"),
                        ("Misconfigured Azure storage container", "danger"),
                    ],
                },
                {
                    "name": "Monitoring & Detection",
                    "color": "#ff9a9a",
                    "status": "Critical Gap",
                    "status_color": "#ff9a9a",
                    "items": [
                        ("Email filtering & attachment scanning", "good"),
                        ("Manual log review only", "warn"),
                        ("No SIEM", "danger"),
                        ("No SOC", "danger"),
                        ("Inconsistent OT logging", "danger"),
                    ],
                },
                {
                    "name": "Backup & Recovery",
                    "color": "#ff9a9a",
                    "status": "Critical Gap",
                    "status_color": "#ff9a9a",
                    "items": [
                        ("Backups exist but connected to main network", "warn"),
                        ("No immutable backups", "danger"),
                        ("No automated workload isolation", "danger"),
                    ],
                },
            ]

            status_icon = {"good": "✓", "warn": "⚠", "danger": "✕"}
            status_clr  = {"good": "#80d7a5", "warn": "#ffcf7d", "danger": "#ff9a9a"}

            for dom in control_domains:
                c = dom["color"]
                sc = dom["status_color"]
                items_html = ""
                for label, stype in dom["items"]:
                    ic  = status_clr[stype]
                    ico = status_icon[stype]
                    items_html += (
                        '<div style="display:flex;align-items:center;gap:0.5rem;padding:0.38rem 0;'
                        'border-bottom:1px solid rgba(173,200,255,0.06);">'
                        '<span style="color:' + ic + ';font-size:0.72rem;flex-shrink:0;">' + ico + '</span>'
                        '<span style="font-size:0.83rem;color:#b7c7df;">' + label + '</span>'
                        '</div>'
                    )
                html = (
                    '<div style="background:rgba(13,27,45,0.95);border:1px solid ' + c + '22;border-left:3px solid ' + c + ';'
                    'border-radius:14px;padding:0.85rem 1rem;margin-bottom:0.65rem;">'
                    '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.55rem;">'
                    '<span style="font-size:0.9rem;font-weight:700;color:' + c + ';">' + dom["name"] + '</span>'
                    '<span style="font-family:JetBrains Mono,monospace;font-size:0.62rem;font-weight:700;'
                    'color:' + sc + ';background:' + sc + '18;border:1px solid ' + sc + '33;'
                    'padding:0.2rem 0.55rem;border-radius:999px;">' + dom["status"] + '</span>'
                    '</div>'
                    + items_html +
                    '</div>'
                )
                st.markdown(html, unsafe_allow_html=True)

            # ── POLICY & GOVERNANCE MATURITY ──────────────────────────────────
            st.markdown("<h3 style='color:#eaf2ff;margin:1.4rem 0 0.5rem;'>Policy & Governance Maturity</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#8fa6c7;font-size:0.88rem;margin-bottom:0.9rem;'>Governance posture shows fragmentation across identity, cloud, and OT environments. Each domain rated 1–5 against a target of 4+.</p>", unsafe_allow_html=True)

            gov_items = [
                ("Identity Governance",    1, 4, "#ff9a9a", "MFA not universal · No IAM lifecycle management · RBAC inconsistently audited"),
                ("Cloud Governance",       1, 4, "#ff9a9a", "No baseline config standards · No CSPM · Misconfigured Azure storage"),
                ("OT Governance",          2, 4, "#ffcf7d", "Varies by facility · Inconsistent logging, monitoring, vendor access"),
                ("Security Governance",    1, 4, "#ff9a9a", "No SIEM · No SOC · No unified incident response framework"),
                ("Vendor Access Governance", 1, 4, "#ff9a9a", "Minimal controls · Remote robotics via external firmware · No zero-trust"),
            ]

            for label, current, target, color, note in gov_items:
                pct_current = (current / 5) * 100
                pct_target  = (target  / 5) * 100
                html = (
                    '<div style="background:rgba(13,27,45,0.9);border:1px solid rgba(173,200,255,0.1);'
                    'border-radius:12px;padding:0.8rem 1rem;margin-bottom:0.55rem;">'
                    '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem;">'
                    '<span style="font-size:0.86rem;font-weight:600;color:#eaf2ff;">' + label + '</span>'
                    '<div style="display:flex;gap:0.8rem;align-items:center;">'
                    '<span style="font-family:JetBrains Mono,monospace;font-size:0.7rem;color:' + color + ';">Current: L' + str(current) + '</span>'
                    '<span style="font-family:JetBrains Mono,monospace;font-size:0.7rem;color:#80d7a5;">Target: L' + str(target) + '</span>'
                    '</div></div>'
                    '<div style="position:relative;height:6px;background:rgba(173,200,255,0.08);border-radius:4px;margin-bottom:0.5rem;">'
                    '<div style="position:absolute;left:0;top:0;height:100%;width:' + str(pct_target) + '%;background:rgba(128,215,165,0.15);border-radius:4px;"></div>'
                    '<div style="position:absolute;left:0;top:0;height:100%;width:' + str(pct_current) + '%;background:' + color + ';border-radius:4px;"></div>'
                    '</div>'
                    '<div style="font-size:0.76rem;color:#8fa6c7;font-style:italic;">' + note + '</div>'
                    '</div>'
                )
                st.markdown(html, unsafe_allow_html=True)

            callout("<strong>Overall:</strong> Controls exist but lack maturity, automation, and consistency across facilities. Governance gaps contribute directly to ransomware exposure and operational risk.", "warn")

        with inner[2]:
            # ── TOOLING VISUALIZATION ─────────────────────────────────────────
            st.markdown("<div class='sec-kicker' style='margin-bottom:0.5rem;'>Security Tooling & Technology Stack</div>", unsafe_allow_html=True)

            # Have vs Need comparison
            c1, c2 = st.columns(2, gap="medium")

            with c1:
                st.markdown("<h3 style='color:#80d7a5;margin:0 0 0.6rem;'>Existing Tools</h3>", unsafe_allow_html=True)
                existing = [
                    ("Antivirus & Endpoint Protection", "Deployed on all corporate endpoints", "#80d7a5"),
                    ("Firewalls",                       "At each of 7 facilities", "#80d7a5"),
                    ("Email Filtering",                 "Attachment scanning enabled", "#80d7a5"),
                    ("VPN",                             "Remote access for employees", "#80d7a5"),
                    ("AWS IAM Identity Center",         "SSO across cloud workloads", "#7cc6ff"),
                    ("Basic Log Review",                "Manual, inconsistent processes", "#ffcf7d"),
                ]
                for name, desc, clr in existing:
                    html = (
                        '<div style="display:flex;gap:0.7rem;align-items:flex-start;padding:0.65rem 0.8rem;'
                        'background:rgba(128,215,165,0.05);border:1px solid rgba(128,215,165,0.14);'
                        'border-radius:12px;margin-bottom:0.45rem;">'
                        '<span style="color:' + clr + ';font-size:1rem;flex-shrink:0;margin-top:1px;">✓</span>'
                        '<div><div style="font-size:0.84rem;font-weight:600;color:#eaf2ff;">' + name + '</div>'
                        '<div style="font-size:0.76rem;color:#8fa6c7;margin-top:2px;">' + desc + '</div></div>'
                        '</div>'
                    )
                    st.markdown(html, unsafe_allow_html=True)

            with c2:
                st.markdown("<h3 style='color:#ff9a9a;margin:0 0 0.6rem;'>Missing / Insufficient Tools</h3>", unsafe_allow_html=True)
                missing = [
                    ("SIEM",               "No centralized log aggregation or correlation", "Critical"),
                    ("SOC",                "No real-time monitoring or incident response center", "Critical"),
                    ("CSPM",               "Cloud misconfigurations undetected", "Critical"),
                    ("Automated IR",       "No automated incident response workflows", "High"),
                    ("Immutable Backups",  "Backups vulnerable to ransomware", "Critical"),
                    ("OT Monitoring",      "No ICS/SCADA-specific detection tools", "Critical"),
                    ("Anomaly Detection",  "No behavioral analytics for cloud or OT", "High"),
                ]
                sev_clr = {"Critical": "#ff9a9a", "High": "#ffcf7d"}
                for name, desc, sev in missing:
                    clr = sev_clr[sev]
                    html = (
                        '<div style="display:flex;gap:0.7rem;align-items:flex-start;padding:0.65rem 0.8rem;'
                        'background:rgba(255,154,154,0.05);border:1px solid rgba(255,154,154,0.16);'
                        'border-radius:12px;margin-bottom:0.45rem;">'
                        '<span style="color:#ff9a9a;font-size:1rem;flex-shrink:0;margin-top:1px;">✕</span>'
                        '<div style="flex:1;">'
                        '<div style="display:flex;justify-content:space-between;align-items:center;">'
                        '<span style="font-size:0.84rem;font-weight:600;color:#eaf2ff;">' + name + '</span>'
                        '<span style="font-family:JetBrains Mono,monospace;font-size:0.6rem;font-weight:700;color:' + clr + ';'
                        'background:' + clr + '18;border:1px solid ' + clr + '33;padding:0.15rem 0.45rem;border-radius:999px;">' + sev + '</span>'
                        '</div>'
                        '<div style="font-size:0.76rem;color:#8fa6c7;margin-top:2px;">' + desc + '</div>'
                        '</div></div>'
                    )
                    st.markdown(html, unsafe_allow_html=True)

            st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

            # Tooling coverage radar-style summary bar chart
            st.markdown("<h3 style='color:#eaf2ff;margin:0.8rem 0 0.5rem;'>Tooling Coverage by Security Domain</h3>", unsafe_allow_html=True)
            tool_domains = [
                ("Identity & Access",     65, "#ffcf7d"),
                ("Endpoint Protection",   60, "#ffcf7d"),
                ("Network Security",      50, "#ffcf7d"),
                ("Cloud Security",        10, "#ff9a9a"),
                ("Monitoring & Detection", 8, "#ff9a9a"),
                ("OT / ICS Security",      5, "#ff9a9a"),
                ("Incident Response",     10, "#ff9a9a"),
                ("Backup & Recovery",     25, "#ffcf7d"),
            ]
            fig_tool = go.Figure()
            fig_tool.add_trace(go.Bar(
                x=[d[0] for d in tool_domains],
                y=[d[1] for d in tool_domains],
                marker_color=[d[2] for d in tool_domains],
                marker_line_width=0,
                hovertemplate="%{x}<br>Coverage: %{y}%<extra></extra>",
            ))
            fig_tool.add_hline(y=70, line_dash="dot", line_color="rgba(128,215,165,0.4)",
                               annotation_text="Minimum acceptable", annotation_position="top right",
                               annotation_font=dict(size=10, color="#80d7a5"))
            fig_tool.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Inter, sans-serif", color="#b7c7df", size=11),
                height=300, margin=dict(t=30, b=10, l=10, r=10),
                xaxis=dict(tickfont=dict(size=10), gridcolor="rgba(173,200,255,0.06)", zeroline=False),
                yaxis=dict(title="Coverage %", range=[0,105], ticksuffix="%",
                           tickfont=dict(size=10), gridcolor="rgba(173,200,255,0.08)", zeroline=False),
            )
            st.plotly_chart(fig_tool, use_container_width=True, config={"displayModeBar": False})

            callout("The absence of SIEM, SOC, CSPM, and OT monitoring significantly increases the likelihood of undetected ransomware activity across NovaDrive's 7 facilities.", "danger")

        with inner[3]:
            # ── THREAT LANDSCAPE ──────────────────────────────────────────────
            st.markdown("<div class='sec-kicker' style='margin-bottom:0.5rem;'>Threat Landscape — Automotive Manufacturing</div>", unsafe_allow_html=True)

            threats = [
                ("Ransomware Groups",        "#ff9a9a", "Critical",
                 "Attackers prioritize industries with high uptime requirements and JIT production. Downtime creates immediate financial loss exceeding $1M/day at NovaDrive.",
                 ["Manufacturing is top-3 targeted sector", "Double-extortion: encrypt + exfiltrate", "JIT environments face maximum pressure to pay"]),
                ("Cloud Misconfiguration",   "#ffcf7d", "High",
                 "A misconfigured Azure storage container exposed sensitive engineering data — a common initial access vector in cloud-heavy environments.",
                 ["Exposed storage containers accessible publicly", "No CSPM to detect drift", "Credentials embedded in accessible files"]),
                ("OT / ICS Attacks",         "#ff9a9a", "Critical",
                 "Legacy protocols (Modbus, OPC-UA) and vendor-controlled firmware create exploitable pathways directly into production systems.",
                 ["No authentication on Modbus/OPC-UA", "Vendor firmware unaudited", "IT-OT flat networks allow pivot"]),
                ("Supply Chain & Vendor",    "#ffcf7d", "High",
                 "Remote vendor access to robotics introduces backdoor opportunities for lateral movement into OT.",
                 ["Vendor sessions unmonitored", "No JIT or time-bound access", "Firmware updates unverified"]),
                ("Phishing & Social Eng.",   "#ffcf7d", "High",
                 "Email remains the primary entry point for credential theft. Floor operators and admin staff are high-value targets.",
                 ["No role-based security training", "No phishing simulation program", "Shared workstations increase exposure"]),
                ("Data Exfiltration / IP",   "#ff9a9a", "Critical",
                 "Engineering CAD/CAM designs, contracts, and production data are high-value targets for industrial espionage.",
                 ["No DLP controls", "Cloud storage poorly governed", "No encryption enforcement"]),
            ]

            sev_clr = {"Critical": "#ff9a9a", "High": "#ffcf7d"}
            for t_name, t_color, t_sev, t_desc, t_bullets in threats:
                clr = sev_clr[t_sev]
                bul_html = "".join(
                    '<div style="display:flex;gap:0.4rem;margin-bottom:3px;">'
                    '<span style="color:' + t_color + ';flex-shrink:0;font-size:0.7rem;">›</span>'
                    '<span style="font-size:0.78rem;color:#8fa6c7;">' + b + '</span></div>'
                    for b in t_bullets
                )
                html = (
                    '<div style="background:rgba(13,27,45,0.95);border:1px solid ' + t_color + '22;border-left:3px solid ' + t_color + ';'
                    'border-radius:14px;padding:0.85rem 1rem;margin-bottom:0.6rem;display:grid;grid-template-columns:1fr auto;gap:0.8rem;">'
                    '<div>'
                    '<div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.4rem;">'
                    '<span style="font-size:0.9rem;font-weight:700;color:' + t_color + ';">' + t_name + '</span>'
                    '<span style="font-family:JetBrains Mono,monospace;font-size:0.6rem;font-weight:700;color:' + clr + ';'
                    'background:' + clr + '18;border:1px solid ' + clr + '33;padding:0.15rem 0.45rem;border-radius:999px;">' + t_sev + '</span>'
                    '</div>'
                    '<p style="font-size:0.83rem;color:#b7c7df;margin:0 0 0.5rem;">' + t_desc + '</p>'
                    + bul_html +
                    '</div></div>'
                )
                st.markdown(html, unsafe_allow_html=True)

            # ── FRAMEWORK SELECTION ───────────────────────────────────────────
            st.markdown("<h3 style='color:#eaf2ff;margin:1.4rem 0 0.5rem;'>Framework Selection Justification</h3>", unsafe_allow_html=True)

            fw_cols = st.columns(2, gap="medium")
            with fw_cols[0]:
                st.markdown("""
                <div style="background:rgba(124,198,255,0.06);border:1px solid rgba(124,198,255,0.2);border-top:3px solid #7cc6ff;border-radius:16px;padding:1rem;">
                    <div style="font-size:0.98rem;font-weight:700;color:#7cc6ff;margin-bottom:0.3rem;">NIST CSF 2.0</div>
                    <div style="font-family:JetBrains Mono,monospace;font-size:0.62rem;color:#8fa6c7;margin-bottom:0.65rem;">Primary Framework</div>
                    <div style="display:flex;flex-direction:column;gap:0.3rem;">
                        <div style="display:flex;gap:0.4rem;font-size:0.82rem;color:#b7c7df;"><span style="color:#7cc6ff;">✓</span> Covers identity, cloud, OT, and governance</div>
                        <div style="display:flex;gap:0.4rem;font-size:0.82rem;color:#b7c7df;"><span style="color:#7cc6ff;">✓</span> Supports maturity scoring (L1–L5)</div>
                        <div style="display:flex;gap:0.4rem;font-size:0.82rem;color:#b7c7df;"><span style="color:#7cc6ff;">✓</span> Widely adopted in manufacturing sector</div>
                        <div style="display:flex;gap:0.4rem;font-size:0.82rem;color:#b7c7df;"><span style="color:#7cc6ff;">✓</span> Aligns with Zero Trust architecture goals</div>
                    </div>
                </div>""", unsafe_allow_html=True)
            with fw_cols[1]:
                st.markdown("""
                <div style="background:rgba(255,207,125,0.06);border:1px solid rgba(255,207,125,0.2);border-top:3px solid #ffcf7d;border-radius:16px;padding:1rem;">
                    <div style="font-size:0.98rem;font-weight:700;color:#ffcf7d;margin-bottom:0.3rem;">NIST 800-82</div>
                    <div style="font-family:JetBrains Mono,monospace;font-size:0.62rem;color:#8fa6c7;margin-bottom:0.65rem;">OT / ICS Security Standard</div>
                    <div style="display:flex;flex-direction:column;gap:0.3rem;">
                        <div style="display:flex;gap:0.4rem;font-size:0.82rem;color:#b7c7df;"><span style="color:#ffcf7d;">✓</span> Addresses ICS, PLCs, SCADA, and robotics</div>
                        <div style="display:flex;gap:0.4rem;font-size:0.82rem;color:#b7c7df;"><span style="color:#ffcf7d;">✓</span> Relevant to NovaDrive smart factory architecture</div>
                        <div style="display:flex;gap:0.4rem;font-size:0.82rem;color:#b7c7df;"><span style="color:#ffcf7d;">✓</span> IT/OT segmentation requirements</div>
                        <div style="display:flex;gap:0.4rem;font-size:0.82rem;color:#b7c7df;"><span style="color:#ffcf7d;">✓</span> Vendor and remote access governance</div>
                    </div>
                </div>""", unsafe_allow_html=True)

            # ── RISK → BUSINESS OBJECTIVES MAPPING ───────────────────────────
            st.markdown("<h3 style='color:#eaf2ff;margin:1.4rem 0 0.5rem;'>Risk Mapping to Business Objectives</h3>", unsafe_allow_html=True)

            objectives = [
                "Continuous JIT Manufacturing",
                "High Uptime Across All Facilities",
                "Rapid Production Cycles",
                "Protection of Engineering IP",
                "Supply Chain Reliability",
                "Regulatory & Contractual Compliance",
            ]
            risk_matrix = [
                # (risk_name, color, [affected_objectives by index 0-5])
                ("Cloud Misconfigurations",   "#ff9a9a", [3, 5]),
                ("Weak IAM",                  "#ff9a9a", [0, 1, 3, 4]),
                ("No SIEM / SOC",             "#ff9a9a", [0, 1, 2]),
                ("Flat OT Networks",          "#ff9a9a", [0, 1, 2, 4]),
                ("Vendor Access Risks",       "#ffcf7d", [0, 4]),
                ("Legacy OT Protocols",       "#ffcf7d", [0, 1, 2]),
                ("Inconsistent Logging",      "#ffcf7d", [0, 5]),
            ]

            # Build header row
            obj_abbr = ["JIT Mfg", "Uptime", "Prod. Speed", "IP Protect", "Supply Chain", "Compliance"]
            header = (
                '<div style="display:grid;grid-template-columns:180px repeat(6,1fr);gap:2px;margin-bottom:4px;">'
                '<div style="font-size:0.68rem;color:#8fa6c7;"></div>'
                + "".join(
                    '<div style="font-family:JetBrains Mono,monospace;font-size:0.58rem;color:#8fa6c7;'
                    'text-align:center;padding:0.3rem 0.2rem;line-height:1.3;">' + a + '</div>'
                    for a in obj_abbr
                ) + '</div>'
            )

            rows_html = ""
            for risk_name, risk_color, affected in risk_matrix:
                cells = "".join(
                    '<div style="background:' + (risk_color + '33' if j in affected else 'rgba(13,27,45,0.6)') + ';'
                    'border:1px solid ' + (risk_color + '55' if j in affected else 'rgba(173,200,255,0.06)') + ';'
                    'border-radius:6px;display:flex;align-items:center;justify-content:center;'
                    'font-size:0.75rem;color:' + (risk_color if j in affected else 'transparent') + ';height:32px;">'
                    + ('●' if j in affected else '') + '</div>'
                    for j in range(6)
                )
                rows_html += (
                    '<div style="display:grid;grid-template-columns:180px repeat(6,1fr);gap:2px;margin-bottom:3px;">'
                    '<div style="display:flex;align-items:center;padding-right:0.5rem;">'
                    '<span style="font-size:0.8rem;font-weight:600;color:' + risk_color + ';">' + risk_name + '</span>'
                    '</div>' + cells + '</div>'
                )

            st.markdown(
                '<div style="background:rgba(9,20,34,0.8);border:1px solid rgba(173,200,255,0.1);'
                'border-radius:14px;padding:0.9rem 1rem;">'
                + header + rows_html +
                '<div style="margin-top:0.7rem;font-size:0.75rem;color:#8fa6c7;font-style:italic;">'
                '● = Risk directly threatens this business objective</div>'
                '</div>',
                unsafe_allow_html=True
            )

            callout("A ransomware event would immediately halt JIT production, violate contractual obligations, cause financial penalties exceeding $1M/day, and cause lasting damage to customer trust and IP.", "danger")

   # ════════════════════════════════════════════════════════════════════════
    # 02B — GAP ANALYSIS & MATURITY
    # ════════════════════════════════════════════════════════════════════════
    with main_tabs[2]:
        inner2 = st.tabs(["Maturity Scoring", "Control Gaps", "Compliance & Weaknesses"])

        # --- TAB 1: MATURITY SCORING (RESTORED) ---
        with inner2[0]:
            card("NIST CSF 2.0 Maturity Scale", """
            <table style="width:100%;border-collapse:collapse;margin-top:0.4rem;">
            <thead><tr style="border-bottom:1px solid rgba(173,200,255,0.14);">
            <th style="padding:0.6rem 0.75rem;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--text);">Level</th>
            <th style="padding:0.6rem 0.75rem;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--text);">Policy Expectation</th>
            <th style="padding:0.6rem 0.75rem;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--text);">Process Expectation</th>
            </tr></thead>
            <tbody>
            <tr><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Level 1 — Initial</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Policy or standard does not exist or is not formally approved</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Standard process does not exist</td></tr>
            <tr><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Level 2 — Repeatable</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Policy exists but not reviewed in more than 2 years</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Ad-hoc process exists and is done informally</td></tr>
            <tr><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Level 3 — Defined</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Formal management approval; exceptions &lt;5%</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Formal documented process; evidence for most activities; &lt;10% exceptions</td></tr>
            <tr><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Level 4 — Managed</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Formal approval; exceptions &lt;3%</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;border-bottom:1px solid rgba(173,200,255,0.07);">Detailed metrics; &lt;5% exceptions; minimal recurring exceptions</td></tr>
            <tr><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;">Level 5 — Optimizing</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;">Formal approval; exceptions &lt;0.5%</td><td style="padding:0.65rem 0.75rem;color:var(--muted);font-size:0.88rem;">Continually improving; &lt;1% exceptions</td></tr>
            </tbody></table>""")

            st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Current Maturity Scores</h3>", unsafe_allow_html=True)
            mat_row("Identity and Access", 1, 1, "#ff9a9a")
            mat_row("Cloud Configuration", 1, 1, "#ff9a9a")
            mat_row("Cloud Detection & Monitoring", 1, 1, "#ff9a9a")
            mat_row("IR, Protection & Recovery", 2, 2, "#ffcf7d")
            mat_row("Network Segmentation", 1, 1, "#ff9a9a")
            mat_row("Employee Awareness", 2, 2, "#ffcf7d")
            mat_row("Ops & Business Continuity", 1, 1, "#ff9a9a")

        # --- TAB 2: CONTROL GAPS (DROPDOWNS) ---
        with inner2[1]:
            st.markdown("<div class='sec-kicker' style='margin-bottom:1rem;'>Identified Control Gaps (Click to Expand)</div>", unsafe_allow_html=True)
            
            control_gaps = [
                {"name": "Identity & Access Security", "color": "#ff9a9a", "status": "Critical", "items": [("MFA not consistently enforced across cloud", "danger"), ("IAM permissions too broad for zero-trust", "danger"), ("No structured IAM governance/lifecycle", "danger"), ("No automated detection of risky roles", "danger")]},
                {"name": "Cloud Configuration Security", "color": "#ff9a9a", "status": "Critical", "items": [("No CSPM tool in place", "danger"), ("Cloud resources potentially exposed", "warn"), ("No automated drift detection", "danger"), ("No baseline cloud security standards", "warn")]},
                {"name": "Cloud Detection & Monitoring", "color": "#ffcf7d", "status": "Weak", "items": [("Lack of cloud-specific analytics", "danger"), ("No automated anomaly detection", "danger"), ("CloudTrail logs may be unmonitored", "warn"), ("No unified SOC for cloud response", "danger")]},
                {"name": "IR, Protection & Recovery", "color": "#ff9a9a", "status": "Critical", "items": [("Backups vulnerable to ransomware", "danger"), ("No automated containment workflows", "danger"), ("No cloud-specific IR playbooks", "warn"), ("Recovery not aligned with JIT uptime", "danger")]},
                {"name": "Network Segmentation", "color": "#ffcf7d", "status": "Weak", "items": [("Network too flat for containment", "danger"), ("No cloud-native segmentation strategy", "warn"), ("OT systems exposed to cloud threats", "danger"), ("No micro-segmentation in place", "warn")]},
                {"name": "Security Awareness", "color": "#7cc6ff", "status": "Partial", "items": [("Workforce not trained for cloud threats", "warn"), ("No ransomware tabletop simulations", "danger"), ("Training not aligned with ZT goals", "warn")]},
                {"name": "Operational & Continuity", "color": "#ff9a9a", "status": "Critical", "items": [("Posture doesn't match JIT risk", "danger"), ("No ransomware-resilient architecture", "danger"), ("No automated recovery for ops", "danger"), ("OT vulnerable via cloud controls", "danger")]}
            ]

            status_icon = {"good": "✓", "warn": "⚠", "danger": "✕"}
            status_clr  = {"good": "#80d7a5", "warn": "#ffcf7d", "danger": "#ff9a9a"}

            for dom in control_gaps:
                c = dom["color"]
                # Display the expander
                with st.expander(f"{dom['name']} — {dom['status']}", expanded=False):
                    items_html = ""
                    for label, stype in dom["items"]:
                        ic, ico = status_clr[stype], status_icon[stype]
                        items_html += (
                            f'<div style="display:flex;align-items:center;gap:0.7rem;padding:0.5rem 0;'
                            f'border-bottom:1px solid rgba(173,200,255,0.06);">'
                            f'<span style="color:{ic};font-size:0.8rem;flex-shrink:0;">{ico}</span>'
                            f'<span style="font-size:0.85rem;color:#b7c7df;">{label}</span>'
                            f'</div>'
                        )
                    st.markdown(f'<div style="border-left:3px solid {c}; padding-left:15px; margin-top:5px;">{items_html}</div>', unsafe_allow_html=True)

        with inner2[2]:
             # ── Benchmark Comparison ──────────────────────────────────────────
            st.markdown("<h3 style='margin-top:0.2rem;color:var(--text);'>Benchmark &amp; Compliance Alignment</h3>", unsafe_allow_html=True)

            card("Framework Gap Overview", """
<p>NovaDrive's current security posture shows several misalignments with major cybersecurity frameworks including
<strong>NIST CSF 2.0</strong>, <strong>CIS Controls</strong>, <strong>NIST 800-82</strong> (OT security),
<strong>PCI DSS</strong>, and <strong>GDPR/CCPA</strong>. The gaps primarily relate to identity governance,
cloud configuration, monitoring, OT segmentation, and data protection.</p>""", "accent")

            # ── Toggle: which frameworks to compare ─────────────────────────
            st.markdown("<p style='color:var(--soft);font-size:0.85rem;margin:0.8rem 0 0.3rem;'>Select frameworks to include in the comparison chart:</p>", unsafe_allow_html=True)

            fw_options = ["NIST CSF 2.0", "CIS Controls", "NIST 800-82", "PCI DSS", "GDPR/CCPA"]
            selected_fw = st.multiselect(
                "Frameworks",
                options=fw_options,
                default=fw_options,
                label_visibility="collapsed",
            )

            show_target = st.toggle("Show Target State (post-remediation)", value=False)

            # ── Data ─────────────────────────────────────────────────────────
            domains = [
                "Identity & Access",
                "Cloud Configuration",
                "Monitoring & Detection",
                "OT / ICS Segmentation",
                "Data Protection",
            ]

            # Current compliance scores per domain per framework (0–100 %)
            current_scores = {
                "NIST CSF 2.0":  [30, 15, 25, 20, 35],
                "CIS Controls":  [25, 10, 20, 15, 30],
                "NIST 800-82":   [35, 20, 30, 10, 40],
                "PCI DSS":       [40, 20, 30, 25, 20],
                "GDPR/CCPA":     [30, 25, 20, 35, 25],
            }

            target_scores = {
                "NIST CSF 2.0":  [85, 80, 85, 80, 85],
                "CIS Controls":  [80, 85, 80, 80, 80],
                "NIST 800-82":   [80, 75, 85, 90, 80],
                "PCI DSS":       [85, 80, 80, 75, 90],
                "GDPR/CCPA":     [80, 80, 75, 80, 85],
            }

            palette_current = {
                "NIST CSF 2.0": "#ff9a9a",
                "CIS Controls":  "#ffcf7d",
                "NIST 800-82":   "#ff9a9a",
                "PCI DSS":       "#ffcf7d",
                "GDPR/CCPA":     "#ff9a9a",
            }
            palette_target = {
                "NIST CSF 2.0": "#80d7a5",
                "CIS Controls":  "#7cc6ff",
                "NIST 800-82":   "#80d7a5",
                "PCI DSS":       "#7cc6ff",
                "GDPR/CCPA":     "#80d7a5",
            }

            if not selected_fw:
                st.info("Select at least one framework above to render the chart.")
            else:
                fig = go.Figure()

                for fw in selected_fw:
                    fig.add_trace(go.Bar(
                        name=f"{fw} — Current",
                        x=domains,
                        y=current_scores[fw],
                        marker_color=palette_current[fw],
                        marker_line_width=0,
                        opacity=0.88,
                        hovertemplate=f"<b>{fw}</b><br>Domain: %{{x}}<br>Current: %{{y}}%<extra></extra>",
                    ))
                    if show_target:
                        fig.add_trace(go.Bar(
                            name=f"{fw} — Target",
                            x=domains,
                            y=target_scores[fw],
                            marker_color=palette_target[fw],
                            marker_line_width=0,
                            opacity=0.65,
                            hovertemplate=f"<b>{fw}</b><br>Domain: %{{x}}<br>Target: %{{y}}%<extra></extra>",
                        ))

                fig.update_layout(
                    barmode="group",
                    bargap=0.22,
                    bargroupgap=0.06,
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(family="Inter, sans-serif", color="#b7c7df", size=12),
                    legend=dict(
                        bgcolor="rgba(13,27,45,0.9)",
                        bordercolor="rgba(173,200,255,0.16)",
                        borderwidth=1,
                        font=dict(size=11),
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="left",
                        x=0,
                    ),
                    xaxis=dict(
                        tickfont=dict(size=11, color="#8fa6c7"),
                        gridcolor="rgba(173,200,255,0.07)",
                        zeroline=False,
                    ),
                    yaxis=dict(
                        title="Compliance Score (%)",
                        range=[0, 105],
                        ticksuffix="%",
                        tickfont=dict(size=11, color="#8fa6c7"),
                        gridcolor="rgba(173,200,255,0.09)",
                        zeroline=False,
                    ),
                    margin=dict(t=60, b=20, l=10, r=10),
                    height=420,
                )

                # Threshold reference lines
                fig.add_hline(y=70, line_dash="dot", line_color="rgba(255,207,125,0.40)",
                              annotation_text="Acceptable threshold (70%)",
                              annotation_position="top right",
                              annotation_font=dict(size=10, color="#ffcf7d"))
                fig.add_hline(y=90, line_dash="dot", line_color="rgba(128,215,165,0.35)",
                              annotation_text="Target maturity (90%)",
                              annotation_position="top right",
                              annotation_font=dict(size=10, color="#80d7a5"))

                st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

            # ── Per-domain breakdown ─────────────────────────────────────────
            st.markdown("<h3 style='margin-top:1.4rem;color:var(--text);'>Domain-Level Compliance Details</h3>", unsafe_allow_html=True)

            domain_details = [
                ("Identity & Access Management (IAM)", "accent", [
                    ("Relevant Frameworks", "NIST CSF PR.AC · CIS Controls 5 & 6 · GDPR/CCPA"),
                    ("Current Gaps", "MFA not universally enforced · Overly permissive IAM roles · No formal identity governance program"),
                    ("Framework Misalignment", "NIST CSF requires strong access control and identity verification · CIS Controls require least privilege and continuous access review · GDPR/CCPA require strict access restrictions to personal data"),
                    ("Impact", "Over-permissive roles increase credential theft risk, unauthorized access, and lateral movement across frameworks"),
                ]),
                ("Cloud Configuration & Governance", "danger", [
                    ("Relevant Frameworks", "CIS Control 4 · NIST CSF PR.IP · NIST CSF PR.DS"),
                    ("Current Gaps", "Misconfigured Azure storage containers (public exposure) · No CSPM tool · No cloud governance or automated compliance checks"),
                    ("Framework Misalignment", "CIS Control 4 requires secure configuration baselines and continuous scanning · NIST CSF requires configuration management and protection of cloud data"),
                    ("Impact", "Misconfigurations create direct ransomware and data exposure risks; CSPM absence means no compliance visibility"),
                ]),
                ("Monitoring & Detection", "warn", [
                    ("Relevant Frameworks", "NIST CSF DE.CM · CIS Control 8 · NIST 800-82"),
                    ("Current Gaps", "No SIEM for centralized log correlation · No SOC for real-time monitoring · OT logging inconsistent across plants"),
                    ("Framework Misalignment", "NIST CSF requires continuous monitoring across IT and OT · CIS Controls require centralized logging and alerting · NIST 800-82 requires ICS/OT monitoring"),
                    ("Impact", "Without SIEM/SOC, NovaDrive cannot detect ransomware indicators, suspicious access, or OT anomalies — significantly increasing dwell time"),
                ]),
                ("OT/ICS Security & Network Segmentation", "danger", [
                    ("Relevant Frameworks", "NIST 800-82 · NIST CSF PR.PT-5 · CIS Control 12"),
                    ("Current Gaps", "Flat networks at several facilities · Legacy OT protocols (Modbus, OPC-UA) lack modern controls · Unregulated vendor remote access"),
                    ("Framework Misalignment", "NIST 800-82 requires segmentation between IT and OT · NIST CSF mandates protective technologies to limit lateral movement · CIS Controls require secure network architecture"),
                    ("Impact", "Attackers can move from IT to OT without barriers, threatening JIT manufacturing uptime across all four plants"),
                ]),
                ("Data Protection, Privacy & ERP Systems", "warn", [
                    ("Relevant Frameworks", "PCI DSS · GDPR/CCPA · NIST CSF PR.DS"),
                    ("Current Gaps", "Employee and engineering data lack encryption and access controls · ERP systems not segmented or monitored · No privacy governance or data retention policies"),
                    ("Framework Misalignment", "PCI DSS requires strict segmentation, monitoring, and access control for financial systems · GDPR/CCPA require protection of personal data · NIST CSF requires data-at-rest and in-transit protections"),
                    ("Impact", "Weak data protection increases risk of data theft, regulatory violations, and reputational damage; ERP especially vulnerable"),
                ]),
            ]

            for title, variant, rows in domain_details:
                rows_html = "".join(
                    f"""<div style="display:grid;grid-template-columns:160px 1fr;gap:0.5rem;padding:0.6rem 0;
                         border-bottom:1px solid rgba(173,200,255,0.07);font-size:0.86rem;">
                        <div style="color:var(--soft);font-weight:600;font-size:0.78rem;">{k}</div>
                        <div style="color:var(--muted);line-height:1.6;">{v}</div>
                    </div>"""
                    for k, v in rows
                )
                st.markdown(
                    f'<div class="card {variant}" style="margin-bottom:0.7rem;">'
                    f'<h3>{title}</h3>{rows_html}</div>',
                    unsafe_allow_html=True
                )

            st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)
            card("Compliance Alignment Note", """
<p>The Bottom Line:</b> While exempt from HIPAA/GDPR, NovaDrive is currently in <b>non-compliance</b> with mandatory U.S. commercial standards:</p>
<ul>
    <li><b>Contractual Liability:</b> Failing PCI DSS levels mandated by OEM customer contracts.</li>
    <li><b>Legal Exposure:</b> Non-alignment with CCPA/CPRA due to California partner commerce.</li>
    <li><b>Critical Gaps:</b> ERP segmentation and encryption failures represent immediate business risk.</li>
</ul>
<p><i>Status: Below widely accepted U.S. regulatory baselines.</i></p>
""")
 
            callout("""<strong>Systemic Weaknesses vs. Isolated Control Failures:</strong><br>
<strong>Structural (Systemic) — The Root Cause:</strong><br>
Foundation-wide gaps including flat network design, lack of centralized monitoring (No SIEM/SOC), and inconsistent identity enforcement. These allow minor threats to propagate across IT, OT, and Cloud layers.
<br><br>
<strong>Technical (Isolated) — The Symptoms:</strong><br>
Specific errors like misconfigured storage containers or overly permissive roles. While local, these act as the <b>initial spark</b> for a wider chain reaction.
<br><br>
<strong>Executive Summary:</strong> Fixing isolated bugs will not reduce risk without addressing the systemic lack of security maturity.""", "warn")

# ══════════════════════════════════════════════════════════════════════════════
# PART 3 — ARCHITECTURE + GOVERNANCE + ROADMAP
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Part 3":

    sec_header("Part 3", "Architecture, Governance & Implementation",
               "Target-state security architecture, governance model, and phased implementation roadmap.")

    main_tabs = st.tabs([
        "03A — Security Architecture",
        "03B — Governance & Policy",
        "03C — Roadmap & Financials",
    ])
    # ════════════════════════════════════
    # 03A — SECURITY ARCHITECTURE
    # ════════════════════════════════════
    with main_tabs[0]:
        inner = st.tabs(["Architecture Layers", "Zero Trust & IAM", "Control Enhancements", "Technology Stack", "SOC & IR Model"])

        with inner[0]:
            # ── LAYERED ARCHITECTURE DIAGRAM (stacked blocks) ─────────────────
            st.markdown("<div class='sec-kicker' style='margin-bottom:0.6rem;'>Target-State Architecture</div>", unsafe_allow_html=True)

            # Alert-flow banner
            st.markdown("""
            <div style="background:rgba(124,198,255,0.06);border:1px solid rgba(124,198,255,0.18);border-radius:12px;
                        padding:0.65rem 1.1rem;margin-bottom:1.2rem;display:flex;align-items:center;gap:0.6rem;flex-wrap:wrap;">
                <span style="font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:var(--accent);text-transform:uppercase;letter-spacing:0.1em;">Log & Alert Flow</span>
                <span style="color:rgba(173,200,255,0.3);">|</span>
                <span style="font-size:0.82rem;color:var(--muted);">
                  <span style="color:#7cc6ff;">Cloud</span> → SIEM &nbsp;·&nbsp;
                  <span style="color:#8b9dff;">IT</span> → SIEM &nbsp;·&nbsp;
                  <span style="color:#ffcf7d;">OT</span> → SIEM &nbsp;·&nbsp;
                  <span style="color:#bc8cff;">SIEM</span> → SOC &nbsp;·&nbsp;
                  <span style="color:#80d7a5;">SOC</span> → IR Team
                </span>
            </div>
            """, unsafe_allow_html=True)

            # Stacked layer blocks with sub-control pills
            layer_data = [
                {
                    "num": "L1", "name": "Cloud Security Layer",
                    "scope": "AWS · Azure · Private Cloud ",
                    "color": "#7cc6ff", "bg": "rgba(124,198,255,0.06)",
                    "summary": "Ensures cloud environments are continuously monitored, securely configured, and protected against misconfigurations and unauthorized access.",
                    "groups": [
                        ("Cloud Posture & Visibility", ["CSPM", "Cloud logging → SIEM", "Cloud workload protection"]),
                        ("Data & Access Hardening",    ["Encryption everywhere", "IAM hardening", "Secure API gateways"]),
                    ],
                },
                {
                    "num": "L2", "name": "Corporate IT Layer",
                    "scope": "Corporate Network · Endpoints · ERP · HR · M365",
                    "color": "#8b9dff", "bg": "rgba(139,157,255,0.06)",
                    "summary": "A hardened IT environment with strong identity controls, segmentation, monitoring, and recovery capabilities.",
                    "groups": [
                        ("Identity & Access",       ["Universal MFA", "RBAC cleanup", "PAM", "Conditional access", "Identity lifecycle automation"]),
                        ("Network Segmentation",    ["Micro-segmentation", "ZTNA", "SD-WAN segmentation", "Modern firewall rules"]),
                        ("Monitoring & Detection",  ["SIEM", "EDR/XDR", "Threat intelligence", "Alert correlation"]),
                        ("Incident Response",       ["IR playbooks", "Automated containment", "Tabletop exercises", "Forensics readiness"]),
                        ("Backup & Recovery",       ["Immutable backups", "Offline backups", "Backup segmentation", "RTO/RPO improvements"]),
                    ],
                },
                {
                    "num": "L3", "name": "OT Layer",
                    "scope": "Robotics · PLCs · SCADA · HMIs · Private 5G",
                    "color": "#ffcf7d", "bg": "rgba(255,207,125,0.06)",
                    "summary": "Isolates critical manufacturing systems, secures legacy protocols, and governs vendor access to reduce operational and supply-chain risk.",
                    "groups": [
                        ("OT Isolation",    ["OT DMZ", "OT segmentation", "Secure gateways (Modbus, OPC-UA)", "Private 5G segmentation", "OT logs → SIEM"]),
                        ("Vendor Controls", ["Just-In-Time vendor access", "Session recording", "Contractual security requirements", "Vendor monitoring"]),
                    ],
                },
                {
                    "num": "L4", "name": "Security Operations & Governance",
                    "scope": "SOC · IR Team · Governance Committees",
                    "color": "#bc8cff", "bg": "rgba(188,140,255,0.06)",
                    "summary": "Provides centralized visibility, coordinated incident response, and executive oversight across all layers.",
                    "groups": [
                        ("SOC Tiers",             ["Tier 1: Alert Triage", "Tier 2: Investigation", "Tier 3: Advanced Escalation"]),
                        ("IR Team",               ["IR Lead", "Forensics Analyst", "Containment Engineer", "Communications Lead", "OT Liaison"]),
                        ("Governance Committees", ["Cybersecurity Steering Committee", "Risk & Compliance Committee", "Architecture Review Board"]),
                    ],
                },
                {
                    "num": "L5", "name": "Zero Trust Foundation",
                    "scope": "Spans All Layers",
                    "color": "#ff9a9a", "bg": "rgba(255,154,154,0.06)",
                    "summary": "Zero Trust serves as the foundation for all layers, ensuring continuous verification and minimizing the blast radius of any compromise.",
                    "groups": [
                        ("Core Principles", ["Never trust, always verify", "Identity + device + network context", "Continuous monitoring", "Restricted lateral movement"]),
                    ],
                },
            ]

            for layer in layer_data:
                c  = layer["color"]
                bg = layer["bg"]
                groups_html = ""
                for grp_name, pills in layer["groups"]:
                    pills_html = "".join(
                        '<span style="display:inline-block;margin:0 0.3rem 0.32rem 0;padding:0.28rem 0.6rem;'
                        'border-radius:999px;font-size:0.72rem;font-weight:600;color:' + c +
                        ';background:rgba(0,0,0,0.25);border:1px solid ' + c + '33;">' + p + '</span>'
                        for p in pills
                    )
                    groups_html += (
                        '<div style="margin-bottom:0.55rem;">'
                        '<div style="font-family:JetBrains Mono,monospace;font-size:0.62rem;'
                        'text-transform:uppercase;letter-spacing:0.1em;color:' + c + ';opacity:0.7;margin-bottom:0.28rem;">'
                        + grp_name + '</div><div>' + pills_html + '</div></div>'
                    )
                html = (
                    '<div style="background:' + bg + ';border:1px solid ' + c + '33;border-left:4px solid ' + c + ';'
                    'border-radius:16px;padding:1rem 1.2rem;margin-bottom:0.6rem;">'
                    '<div style="display:flex;align-items:flex-start;gap:1rem;margin-bottom:0.75rem;">'
                    '<div style="flex-shrink:0;text-align:center;min-width:52px;">'
                    '<div style="font-family:JetBrains Mono,monospace;font-size:0.58rem;color:' + c + ';opacity:0.7;text-transform:uppercase;">'
                    + layer["num"] + '</div>'
                    '<div style="font-size:1.4rem;font-weight:800;color:' + c + ';line-height:1;">' + layer["num"][-1] + '</div>'
                    '</div>'
                    '<div style="flex:1;">'
                    '<div style="font-size:0.98rem;font-weight:700;color:' + c + ';margin-bottom:2px;">' + layer["name"] + '</div>'
                    '<div style="font-size:0.74rem;color:#8fa6c7;">' + layer["scope"] + '</div>'
                    '</div></div>'
                    '<div style="padding-left:68px;">' + groups_html
                    + '<p style="margin:0.6rem 0 0;font-size:0.84rem;color:#b7c7df;font-style:italic;'
                    'border-top:1px solid ' + c + '22;padding-top:0.55rem;">' + layer["summary"] + '</p></div></div>'
                )
                st.markdown(html, unsafe_allow_html=True)

            # ── CONTROL ENHANCEMENTS — Expandable sections with KPI cards ─────
        with inner[1]:
            st.markdown("<p style='color:var(--soft);margin-bottom:1.2rem;'>Explore the core pillars of NovaDrive's Zero Trust framework (NIST 800-207), then use the interactive Policy Evaluator below to simulate real access decisions across NovaDrive's environment.</p>", unsafe_allow_html=True)

            # ── Pillar Cards ──────────────────────────────────────────────
            p1, p2, p3 = st.columns(3, gap="small")
            with p1:
                card("Identity & Access (IAM)", """
<ul style='margin-top:0;'>
<li><strong>Universal MFA:</strong> Enforced for all 1,500 employees — ending the current high-risk-only model.</li>
<li><strong>Least Privilege (PoLP):</strong> AWS &amp; Azure admin rights granted only when needed and revoked immediately after use.</li>
<li><strong>IGA &amp; PAM:</strong> Automated lifecycle management and fully recorded vendor sessions on robotic systems.</li>
</ul>""", "accent")
            with p2:
                card("Network Segmentation", """
<ul style='margin-top:0;'>
<li><strong>Micro-segmentation:</strong> Isolates all 4 plants (TN, OH, WA, VA) — stops lateral ransomware movement.</li>
<li><strong>Industrial DMZ (IDMZ):</strong> Secure buffer between corporate IT and OT networks.</li>
<li><strong>Legacy Isolation:</strong> Deep-packet inspection of Modbus / OPC-UA traffic on factory-floor controllers.</li>
</ul>""", "warn")
            with p3:
                card("Continuous Monitoring", """
<ul style='margin-top:0;'>
<li><strong>Centralized SIEM:</strong> Aggregates IT, OT, and Cloud logs from all 8 facilities.</li>
<li><strong>EDR &amp; Passive OT:</strong> Real-time threat hunting without polling or crashing legacy gear.</li>
<li><strong>SOAR:</strong> Automated firewall blocking the moment the SIEM detects a breach.</li>
</ul>""", "good")

            st.markdown("<hr style='border: none; height: 1px; background: rgba(173,200,255,0.09); margin: 1.5rem 0;'>", unsafe_allow_html=True)

            # ── Zero Trust Policy Simulator ───────────────────────────────
            st.markdown("<h3 style='color:var(--text);margin-bottom:0.3rem;'>⚙️ Zero Trust Access Simulator — NIST 800-207</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:var(--muted);font-size:0.9rem;margin-bottom:1.2rem;'>Demonstrate NovaDrive's <em>'Never Trust, Always Verify'</em> policy engine. Select the conditions of an incoming access request to see how the new architecture evaluates and responds.</p>", unsafe_allow_html=True)

            with st.form("zt_simulator"):
                sc1, sc2, sc3, sc4, sc5 = st.columns(5)
                with sc1:
                    user_type = st.selectbox("👤 User Identity", [
                        "Corporate Employee (Atlanta HQ)",
                        "OT Engineer (Plant Floor)",
                        "Third-Party Vendor / Technician",
                        "Executive / C-Suite",
                    ])
                with sc2:
                    device_health = st.selectbox("💻 Device Posture", [
                        "Managed & Compliant (Windows 11)",
                        "Managed — Missing Critical Patches",
                        "Unmanaged / BYOD",
                    ])
                with sc3:
                    network_loc = st.selectbox("🌐 Network Location", [
                        "Internal SD-WAN (HQ / Plant)",
                        "Remote via ZTNA Portal",
                        "Public Internet (No VPN)",
                    ])
                with sc4:
                    mfa_status = st.selectbox("🔐 MFA Verified?", ["Yes", "No"])
                with sc5:
                    resource_target = st.selectbox("🏭 Target Resource", [
                        "Corporate ERP / M365",
                        "OT / SCADA / Robotics",
                        "Cloud (AWS / Azure Admin)",
                        "Engineering File Servers",
                    ])

                submit_zt = st.form_submit_button("▶ Evaluate Access Policy", use_container_width=True)

            if submit_zt:
                st.markdown("<br>", unsafe_allow_html=True)

                # ── Decision engine ──────────────────────────────────────
                denied   = False
                quarant  = False
                elevated = False
                verdict  = ""
                detail   = ""
                controls = []

                # Hard denials
                if mfa_status == "No":
                    denied = True
                    verdict = "❌ ACCESS DENIED — MFA Not Verified"
                    detail  = (
                        "NovaDrive's Zero Trust policy mandates Universal MFA for all 1,500 employees, "
                        "OT engineers, and vendors — regardless of location or device. "
                        "The Policy Engine has rejected this request because identity cannot be confirmed. "
                        "**NIST 800-207 § 2.1:** No implicit trust is granted based on network location alone."
                    )
                    controls = ["SIEM alert raised", "Failed login logged to audit trail", "Account flagged for review by SOC Tier 1"]

                elif device_health == "Unmanaged / BYOD" and user_type not in ["Third-Party Vendor / Technician"]:
                    denied = True
                    verdict = "❌ ACCESS DENIED — Unmanaged Endpoint Rejected"
                    detail  = (
                        "NovaDrive employees must use corporate-managed Windows 11 endpoints with full EDR coverage. "
                        "Unmanaged devices cannot be trusted as they lack EDR, patch compliance, and disk encryption — "
                        "all required by NovaDrive's device posture policy. "
                        "**NIST 800-207 § 3.3:** Device health is a mandatory signal in the Policy Engine."
                    )
                    controls = ["Device blocked at NAC layer", "SIEM event created", "Employee notified to use managed endpoint"]

                elif user_type == "Third-Party Vendor / Technician" and network_loc == "Internal SD-WAN (HQ / Plant)":
                    denied = True
                    verdict = "❌ ACCESS DENIED — Vendor Direct Network Access Prohibited"
                    detail  = (
                        "Third-party vendors and OEM technicians (e.g., robotics maintenance crews) are **never** permitted "
                        "to connect directly to the internal SD-WAN. All vendor access must route through the secure ZTNA portal "
                        "with Just-in-Time provisioning and session recording via PAM. "
                        "**NovaDrive Control:** Vendor ZTNA Portal + PAM session recording mandated by supply-chain risk policy."
                    )
                    controls = ["Connection blocked at perimeter firewall", "PAM alert raised", "Vendor IT contact notified"]

                elif resource_target in ["OT / SCADA / Robotics"] and user_type not in ["OT Engineer (Plant Floor)", "Third-Party Vendor / Technician"]:
                    denied = True
                    verdict = "❌ ACCESS DENIED — OT Resource Requires Explicit OT Role"
                    detail  = (
                        "NovaDrive's IDMZ strictly separates corporate IT from the OT network. "
                        "SCADA systems, PLCs, and robotic controllers at all 4 manufacturing plants "
                        "are only accessible to authorized OT engineers and credentialed vendors via Just-in-Time access. "
                        "Corporate employees and executives have **no path** into OT without a formal access request. "
                        "**NovaDrive Control:** IDMZ + micro-segmentation isolates OT from IT at all 4 plant sites."
                    )
                    controls = ["Firewall drop at IDMZ boundary", "SOC Tier 2 alerted — potential insider threat signal", "SIEM correlation rule triggered"]

                elif resource_target == "Cloud (AWS / Azure Admin)" and device_health == "Managed — Missing Critical Patches":
                    quarant = True
                    verdict = "⚠️ CONDITIONAL ACCESS — Device Quarantined Pending Patch"
                    detail  = (
                        "Cloud admin access to AWS or Azure requires fully compliant device posture. "
                        "This device is managed but missing critical security patches — "
                        "it is automatically routed to NovaDrive's remediation VLAN until patching is confirmed. "
                        "Admin privileges will not be granted until the device passes the next posture check. "
                        "**NIST 800-207 § 3.3:** Continuous device validation, not one-time checks."
                    )
                    controls = ["Routed to remediation VLAN", "IT Helpdesk ticket auto-opened", "Re-evaluation triggered post-patch via CSPM"]

                elif device_health == "Managed — Missing Critical Patches":
                    quarant = True
                    verdict = "⚠️ CONDITIONAL ACCESS — Restricted to Remediation VLAN"
                    detail  = (
                        "Device posture check has detected missing critical patches. "
                        "Per NovaDrive's IGA-enforced device policy, this endpoint is granted restricted access only. "
                        "Full resource access is suspended until the endpoint is updated and re-evaluated. "
                        "**NovaDrive Control:** Automated posture enforcement via IGA + NAC integration."
                    )
                    controls = ["Partial access to non-sensitive resources only", "Auto-remediation script pushed via MDM", "SIEM low-severity alert created"]

                elif user_type == "Third-Party Vendor / Technician" and resource_target == "OT / SCADA / Robotics":
                    elevated = True
                    verdict = "✅ ACCESS GRANTED — JIT Vendor Session (PAM Monitored)"
                    detail  = (
                        "Vendor identity verified via MFA through the ZTNA portal. "
                        "Just-in-Time access has been provisioned — limited to the specific robotic system requiring maintenance "
                        "at the requested plant. The PAM platform is recording the full session. "
                        "Access will automatically expire in 4 hours. "
                        "**NovaDrive Control:** PAM session recording + ZTNA JIT access — no standing permissions for vendors."
                    )
                    controls = ["PAM session recording active", "SIEM audit log entry created", "Access scoped to single device — lateral movement blocked by micro-segmentation"]

                else:
                    verdict = "✅ ACCESS GRANTED — Standard Policy Compliant"
                    detail  = (
                        f"All Zero Trust signals verified: MFA confirmed, device posture compliant, "
                        f"network location and resource access within policy bounds for a **{user_type}**. "
                        f"Access to **{resource_target}** is granted with continuous monitoring active. "
                        "SIEM and EDR remain engaged for behavioral analytics throughout the session. "
                        "**NIST 800-207:** Continuous validation — trust is never permanent."
                    )
                    controls = ["Session monitored by EDR", "SIEM behavioral baseline active", "Access expires at session end — no standing privilege"]

                # ── Render result ────────────────────────────────────────
                if denied:
                    border = "var(--danger)"; bg = "rgba(255,154,154,0.07)"
                elif quarant:
                    border = "var(--warn)";   bg = "rgba(255,207,125,0.07)"
                elif elevated:
                    border = "var(--good)";   bg = "rgba(128,215,165,0.07)"
                else:
                    border = "var(--good)";   bg = "rgba(128,215,165,0.07)"

                st.markdown(f"""
<div style='border-left:3px solid {border};background:{bg};border-radius:14px;padding:1.1rem 1.3rem;margin-bottom:1rem;'>
  <div style='font-size:1.05rem;font-weight:700;color:var(--text);margin-bottom:0.5rem;'>{verdict}</div>
  <p style='margin:0 0 0.8rem;font-size:0.92rem;line-height:1.7;'>{detail}</p>
  <div style='font-family:"JetBrains Mono",monospace;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--soft);margin-bottom:0.4rem;'>Automated Controls Triggered</div>
  <ul style='margin:0;padding-left:1.2rem;'>
    {''.join(f"<li style='font-size:0.88rem;color:var(--muted);margin-bottom:0.25rem;'>{c}</li>" for c in controls)}
  </ul>
</div>""", unsafe_allow_html=True)

                # ── Signal summary bar ───────────────────────────────────
                st.markdown("<div style='font-family:\"JetBrains Mono\",monospace;font-size:0.68rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--soft);margin:0.8rem 0 0.4rem;'>Policy Signal Summary</div>", unsafe_allow_html=True)
                sig_cols = st.columns(5)
                signals = [
                    ("Identity", user_type.split("(")[0].strip(), mfa_status == "Yes"),
                    ("Device",   device_health.split("—")[0].strip() if "—" in device_health else device_health.split("(")[0].strip(), device_health == "Managed & Compliant (Windows 11)"),
                    ("Network",  network_loc.split("(")[0].strip(), network_loc != "Public Internet (No VPN)"),
                    ("MFA",      mfa_status, mfa_status == "Yes"),
                    ("Resource", resource_target.split("(")[0].strip(), not denied),
                ]
                for col, (label, val, ok) in zip(sig_cols, signals):
                    color = "var(--good)" if ok else "var(--danger)"
                    icon  = "✓" if ok else "✗"
                    col.markdown(f"""
<div style='background:rgba(13,27,45,0.9);border:1px solid rgba(173,200,255,0.12);border-radius:12px;padding:0.7rem 0.8rem;text-align:center;'>
  <div style='font-family:"JetBrains Mono",monospace;font-size:0.62rem;text-transform:uppercase;letter-spacing:0.1em;color:var(--soft);margin-bottom:0.3rem;'>{label}</div>
  <div style='font-size:0.8rem;color:var(--muted);margin-bottom:0.3rem;line-height:1.3;'>{val}</div>
  <div style='font-size:1rem;color:{color};font-weight:700;'>{icon}</div>
</div>""", unsafe_allow_html=True)

        with inner[2]:
            st.markdown("<h3 style='color:var(--text);margin:1.8rem 0 0.5rem;'>Control Enhancements & New Capabilities</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:var(--soft);font-size:0.88rem;margin-bottom:1rem;'>Expand each domain to see targeted enhancements and key performance indicators.</p>", unsafe_allow_html=True)

            enhancements = [
                {
                    "title": "Identity & Access Management Enhancements",
                    "color": "#7cc6ff",
                    "kpis": [
                        ("1,500", "Employees covered by Universal MFA"),
                        ("100%",  "Accounts under least-privilege RBAC"),
                        ("0",     "Orphaned accounts post-IGA rollout"),
                        ("JIT",   "PAM access model for privileged users"),
                    ],
                    "bullets": [
                        "Universal MFA for all users across IT, OT, and cloud environments.",
                        "RBAC cleanup to remove unnecessary privileges and enforce least privilege.",
                        "Privileged Access Management (PAM) for administrative and high-risk accounts.",
                        "Conditional access policies evaluating device health, user location, and risk level.",
                        "Automated identity lifecycle management to eliminate orphaned accounts.",
                    ],
                    "impact": "Significantly reduces credential theft, unauthorized access, and lateral movement — major risks highlighted in the current-state assessment.",
                },
                {
                    "title": "Network Segmentation & Zero Trust Architecture",
                    "color": "#8b9dff",
                    "kpis": [
                        ("4+2",   "Plants + DCs micro-segmented"),
                        ("ZTNA",  "Replaces VPN for all vendor access"),
                        ("IDMZ",  "Dedicated OT demilitarized zone"),
                        ("0",     "Flat broadcast domains remaining"),
                    ],
                    "bullets": [
                        "Micro-segmentation divides flat networks into controlled security zones across IT, OT, cloud, and user networks.",
                        "Dedicated OT DMZ separating industrial systems from corporate IT.",
                        "ZTNA for remote employees and vendors, enforcing identity-based access.",
                        "Modernized firewall rule sets with application-aware filtering.",
                        "SD-WAN segmentation ensuring consistent security across all sites.",
                    ],
                    "impact": "Prevents attackers from moving freely across the environment, directly addressing ransomware lateral-movement risks.",
                },
                {
                    "title": "Monitoring & Detection Enhancements",
                    "color": "#80d7a5",
                    "kpis": [
                        ("24/7",  "SOC visibility across IT, OT, Cloud"),
                        ("SIEM",  "Centralized log aggregation & correlation"),
                        ("EDR",   "All endpoints, servers & workstations"),
                        ("↓",     "Reduced dwell time via automated alerts"),
                    ],
                    "bullets": [
                        "Enterprise SIEM ingesting logs from IT, OT, cloud, identity, and network systems.",
                        "EDR/XDR deployed on all endpoints, servers, and shared workstations.",
                        "OT monitoring for PLCs, SCADA, HMIs, and industrial protocols.",
                        "Threat intelligence integration to detect ransomware and supply-chain threats earlier.",
                        "Automated alert correlation to reduce false positives and improve response time.",
                    ],
                    "impact": "Significantly reduces dwell time and improves early detection of ransomware activity.",
                },
                {
                    "title": "OT Isolation & Secure Vendor Access",
                    "color": "#ffcf7d",
                    "kpis": [
                        ("JIT",   "Time-bound vendor access sessions"),
                        ("100%",  "Vendor sessions recorded"),
                        ("IDMZ",  "IT/OT buffer enforced"),
                        ("5G",    "Private industrial wireless segmented"),
                    ],
                    "bullets": [
                        "Secure vendor access portal with MFA, session recording, and time-bound access.",
                        "OT network isolation using firewalls, segmentation, and OT DMZ.",
                        "Secure gateways for legacy protocols such as Modbus and OPC-UA.",
                        "Private 5G segmentation to isolate industrial wireless traffic.",
                        "OT log forwarding into the SIEM for centralized monitoring.",
                    ],
                    "impact": "Prevents unauthorized access to critical manufacturing systems and reduces likelihood of OT ransomware incidents.",
                },
                {
                    "title": "Cloud Security Enhancements",
                    "color": "#7cc6ff",
                    "kpis": [
                        ("CSPM",  "Automated misconfiguration detection"),
                        ("0",     "Publicly exposed storage containers"),
                        ("API GW","Locked-down secure API gateways"),
                        ("AES",   "Mandatory encryption for all data"),
                    ],
                    "bullets": [
                        "CSPM response protocol to instantly isolate misconfigured resources.",
                        "Automated revocation of overly permissive access policies.",
                        "Centralized cloud log analysis and workload protection data review.",
                        "IAM credential rotation and least-privilege enforcement after any breach.",
                        "Secure API gateways locked down to prevent data exfiltration.",
                    ],
                    "impact": "Cloud vulnerabilities are neutralized before they can be exploited in double-extortion ransomware schemes.",
                },
                {
                    "title": "Backup & Recovery Enhancements",
                    "color": "#80d7a5",
                    "kpis": [
                        ("3-2-1-1","Backup strategy (air-gapped copy)"),
                        ("Immutable","Backups ransomware-proof"),
                        ("↓ RTO", "Faster recovery for JIT continuity"),
                        ("Isolated","Backup network segmented from IT"),
                    ],
                    "bullets": [
                        "Immutable backups that cannot be encrypted or deleted by ransomware.",
                        "3-2-1-1 backup strategy: 3 copies, 2 media types, 1 offsite, 1 air-gapped.",
                        "Backup traffic segmentation to isolate recovery environment from corporate network.",
                        "Automated recovery triggers to support JIT manufacturing uptime requirements.",
                    ],
                    "impact": "Ensures NovaDrive can recover rapidly from any ransomware event without paying ransom, meeting JIT RTO/RPO targets.",
                },
                {
                    "title": "Vendor & Third-Party Controls",
                    "color": "#ffcf7d",
                    "kpis": [
                        ("JIT",   "Access granted per-task only"),
                        ("100%",  "Vendor sessions monitored"),
                        ("SLA",   "Security requirements in all contracts"),
                        ("Cont.", "Continuous vendor risk monitoring"),
                    ],
                    "bullets": [
                        "Just-in-Time access: vendor permissions granted only for the duration of a specific task.",
                        "Security requirements integrated into all production contracts.",
                        "Continuous vendor monitoring to detect supply-chain spillover risks.",
                        "Vendor governance aligned with Zero Trust principles.",
                    ],
                    "impact": "Manages digital transformation risk from private 5G, robotics, and third-party integrations.",
                },
                {
                    "title": "Training & Policy Enhancements",
                    "color": "#8b9dff",
                    "kpis": [
                        ("Role-based","Phishing sims per job function"),
                        ("OT-specific","Floor operator security training"),
                        ("Quarterly", "Recurring simulation cadence"),
                        ("Change Mgmt","Security review for every change"),
                    ],
                    "bullets": [
                        "Recurring phishing simulations tailored to engineering and administrative roles.",
                        "OT-specific security training for floor operators targeting social engineering and physical access.",
                        "Updated security policies and rigorous change management process.",
                        "Security review requirement for every technical change to prevent configuration drift.",
                    ],
                    "impact": "Shifts NovaDrive toward a resilient, security-first posture — closing the human-element attack vector.",
                },
            ]

            for enh in enhancements:
                c = enh["color"]
                with st.expander(f"  {enh['title']}", expanded=False):
                    # KPI row
                    kpi_html = "".join(
                        f'<div style="background:rgba(0,0,0,0.3);border:1px solid {c}33;border-top:2px solid {c};'
                        f'border-radius:14px;padding:0.75rem 0.8rem;text-align:center;">'
                        f'<div style="font-size:1.3rem;font-weight:800;color:{c};line-height:1;">{v}</div>'
                        f'<div style="font-size:0.68rem;color:var(--soft);margin-top:4px;line-height:1.4;">{lbl}</div>'
                        f'</div>'
                        for v, lbl in enh["kpis"]
                    )
                    st.markdown(
                        f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:0.6rem;margin-bottom:0.9rem;">{kpi_html}</div>',
                        unsafe_allow_html=True
                    )
                    # Bullets
                    bullets_html = "".join(f"<li>{b}</li>" for b in enh["bullets"])
                    st.markdown(
                        f'<ul style="padding-left:1.2rem;margin:0 0 0.6rem;">{bullets_html}</ul>',
                        unsafe_allow_html=True
                    )
                    # Impact callout
                    st.markdown(
                        f'<div style="border-left:3px solid {c};background:{c}11;padding:0.6rem 0.9rem;'
                        f'border-radius:10px;font-size:0.85rem;color:var(--muted);">'
                        f'<strong style="color:{c};">Impact:</strong> {enh["impact"]}</div>',
                        unsafe_allow_html=True
                    )


        with inner[3]:
            st.markdown("<p style='color:var(--soft);'>Select a technology layer below to review its vendor-neutral solution and business justification, then use the form to approve the architecture.</p>", unsafe_allow_html=True)

            # Data dictionary for the tech stack
            tech_stack = {
                "Cloud Security": {"tech": "CSPM (Cloud Security Posture Management)", "justification": "Directly prevents the initial entry point risk. Automates discovery of misconfigured storage buckets and overly permissive policies in Azure/AWS."},
                "Identity": {"tech": "IGA (Identity Governance and Administration)", "justification": "Solves identity fragmentation. Ensures that 1,500 employees have consistent MFA and that access is revoked automatically when roles change."},
                "Network": {"tech": "Micro-segmentation (Software-Defined)", "justification": "Limits the blast radius. By isolating the 4 manufacturing plants and the 2 distribution centers, a breach in Atlanta cannot stop production in Ohio."},
                "OT Defense": {"tech": "Passive Industrial IDS (Intrusion Detection)", "justification": "Protects legacy systems. Monitors Modbus and OPC-UA traffic for anomalies without polling devices — preventing crashes of sensitive legacy controllers."},
                "Monitoring": {"tech": "SIEM & SOAR (Security Orchestration)", "justification": "Provides centralized visibility. Collects logs from multi-state facilities and automates containment of threats, reducing the burden on a small security team."},
                "Access": {"tech": "ZTNA (Zero Trust Network Access)", "justification": "Replaces traditional VPNs for vendors. Grants Just-in-Time access to robotic systems, ensuring technicians only see the specific machine they are fixing."},
                "Resilience": {"tech": "Immutable Backup Vaults", "justification": "Ensures JIT continuity. These backups cannot be deleted or encrypted by ransomware, providing a guaranteed recovery path if primary systems fail."}
            }

            # Interactive Stack Explorer
            selected_layer = st.selectbox("🔍 Select Technology Layer to Review:", list(tech_stack.keys()))

            # Display selected info using your custom card styling
            selected_tech = tech_stack[selected_layer]["tech"]
            selected_just = tech_stack[selected_layer]["justification"]

            c1, c2 = st.columns([1, 1.5], gap="medium")
            with c1:
                card("Vendor-Neutral Technology", f"<p style='font-size:1.1rem;font-weight:700;color:var(--accent);margin-top:0.5rem;'>{selected_tech}</p>", "accent")
            with c2:
                card("Business & Technical Justification", f"<p>{selected_just}</p>")

            st.markdown("<hr style='border: none; height: 1px; background: rgba(173,200,255,0.09); margin: 2rem 0;'>", unsafe_allow_html=True)

            # ── Diagrams ──────────────────────────────────────────────────
            st.markdown("<h3 style='color:var(--text);margin-bottom:1rem;'>Security Coverage Diagrams</h3>", unsafe_allow_html=True)
            diag_col1, diag_col2 = st.columns(2, gap="medium")

            # Radar chart — security coverage scores per layer
            with diag_col1:
                radar_layers = ["Cloud Security", "Identity", "Network", "OT Defense", "Monitoring", "Access", "Resilience"]
                radar_scores = [92, 88, 85, 78, 90, 83, 80]
                fig_radar = go.Figure()
                fig_radar.add_trace(go.Scatterpolar(
                    r=radar_scores + [radar_scores[0]],
                    theta=radar_layers + [radar_layers[0]],
                    fill="toself",
                    fillcolor="rgba(124,198,255,0.15)",
                    line=dict(color="#7cc6ff", width=2),
                    name="Coverage Score"
                ))
                fig_radar.update_layout(
                    polar=dict(
                        bgcolor="rgba(13,27,45,0)",
                        radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(color="#8fa6c7", size=10), gridcolor="rgba(173,200,255,0.12)"),
                        angularaxis=dict(tickfont=dict(color="#eaf2ff", size=11), gridcolor="rgba(173,200,255,0.12)")
                    ),
                    paper_bgcolor="rgba(13,27,45,0.0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#eaf2ff"),
                    title=dict(text="Security Coverage by Layer", font=dict(color="#eaf2ff", size=14)),
                    showlegend=False,
                    margin=dict(t=60, b=20, l=40, r=40)
                )
                st.plotly_chart(fig_radar, use_container_width=True)

            # Horizontal bar chart — implementation priority score
            with diag_col2:
                priority_labels = ["Resilience", "Access", "OT Defense", "Network", "Identity", "Cloud Security", "Monitoring"]
                priority_values = [80, 83, 78, 85, 88, 92, 90]
                bar_colors = ["#7cc6ff"] * 7
                fig_bar = go.Figure(go.Bar(
                    x=priority_values,
                    y=priority_labels,
                    orientation="h",
                    marker=dict(color=bar_colors, opacity=0.82, line=dict(width=0)),
                    text=[f"{v}%" for v in priority_values],
                    textposition="outside",
                    textfont=dict(color="#eaf2ff", size=11)
                ))
                fig_bar.update_layout(
                    paper_bgcolor="rgba(13,27,45,0.0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#eaf2ff"),
                    title=dict(text="Implementation Priority Score", font=dict(color="#eaf2ff", size=14)),
                    xaxis=dict(range=[0, 110], showgrid=True, gridcolor="rgba(173,200,255,0.10)", tickfont=dict(color="#8fa6c7")),
                    yaxis=dict(showgrid=False, tickfont=dict(color="#eaf2ff")),
                    margin=dict(t=60, b=20, l=10, r=60)
                )
                st.plotly_chart(fig_bar, use_container_width=True)

            st.markdown("<hr style='border: none; height: 1px; background: rgba(173,200,255,0.09); margin: 2rem 0;'>", unsafe_allow_html=True)

            # Interactive Approval Form
            st.markdown("<h3 style='color:var(--text);margin-bottom:1rem;'>Architecture Approval Form</h3>", unsafe_allow_html=True)

            with st.form("tech_stack_form"):
                st.write("Review and approve the proposed technology stack implementations for the target-state architecture.")

                approved_items = []
                for layer, details in tech_stack.items():
                    if st.checkbox(f"Approve {layer} : {details['tech']}", value=True):
                        approved_items.append(layer)

                st.markdown("<br>", unsafe_allow_html=True)
                comments = st.text_area("Additional Architecture Comments or Risk Notes:")

                submitted = st.form_submit_button("Submit Architecture Review")

                if submitted:
                    if len(approved_items) == len(tech_stack):
                        st.success("✅ All technology layers approved successfully! Ready for Phase 1 Implementation.")
                    elif len(approved_items) > 0:
                        st.warning(f"⚠️ Partial approval submitted. ({len(approved_items)}/{len(tech_stack)} layers approved). Pending Architecture Review Board review.")
                    else:
                        st.error("❌ Architecture rejected. No layers were approved.")

        with inner[4]:
            # ── SOC TIERED STRUCTURE ───────────────────────────────────────────
            st.markdown("<div class='sec-kicker' style='margin-bottom:0.5rem;'>Operational Model</div>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:var(--text);margin:0 0 0.3rem;'>Security Operations Center — Hybrid SOC</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:var(--soft);font-size:0.88rem;margin-bottom:1rem;'>Addresses NovaDrive's current absence of centralized monitoring, SIEM integration, and real-time threat detection across IT, OT, and cloud environments.</p>", unsafe_allow_html=True)

            for num, title, color, bullets in [
                ("01", "Alert Triage", "#7cc6ff", [
                    "Monitors SIEM alerts, EDR events, cloud logs, and OT telemetry",
                    "Performs initial triage, identifies false positives, and escalates suspicious activity",
                    "Ensures continuous visibility across AWS, Azure, ERP systems, OT gateways, firewalls, and EDR agents",
                ]),
                ("02", "Investigation & Threat Analysis", "#8b9dff", [
                    "Conducts deeper investigations into incidents escalated by Tier 1",
                    "Correlates events across IT and OT systems to identify attack patterns",
                    "Performs threat hunting using behavioral analytics and threat intelligence",
                    "Determines root causes and identifies lateral movement attempts",
                ]),
                ("03", "Advanced Response & Escalation", "#80d7a5", [
                    "Handles complex or high-severity incidents",
                    "Coordinates directly with the IR team for containment and recovery",
                    "Executes actions such as isolating endpoints, disabling compromised accounts, and blocking malicious network traffic",
                    "Communicates critical findings to leadership and ensures rapid escalation",
                ]),
            ]:
                li_html = "".join(f"<li>{b}</li>" for b in bullets)
                st.markdown(f"""
                <div class="soc-tier">
                    <div class="soc-num-col">
                        <span class="soc-tier-lbl">Tier</span>
                        <span class="soc-tier-num" style="color:{color};">{num}</span>
                    </div>
                    <div class="soc-content">
                        <div class="soc-tier-title" style="color:{color};">{title}</div>
                        <ul class="soc-bullets">{li_html}</ul>
                    </div>
                </div>""", unsafe_allow_html=True)

            # ── IR TEAM ────────────────────────────────────────────────────────
            st.markdown("<h3 style='color:var(--text);margin:1.4rem 0 0.5rem;'>Incident Response (IR) Team</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:var(--soft);font-size:0.88rem;margin-bottom:0.8rem;'>The IR team manages security incidents from detection through recovery, addressing the lack of structured response processes identified in Part 2.</p>", unsafe_allow_html=True)

            ir_members = [
                ("IR Lead",                        "#7cc6ff",  "Oversees incident handling and coordinates with executives"),
                ("Forensics Analyst",              "#8b9dff",  "Collects evidence, performs root-cause analysis, and documents findings"),
                ("Containment & Recovery Eng.",    "#80d7a5",  "Isolates affected systems, removes malware, restores services, and validates backups"),
                ("Communications Lead",            "#ffcf7d",  "Manages internal and external communication, including customer and executive updates"),
                ("OT Liaison",                     "#ff9a9a",  "Ensures OT-related incidents are handled safely without disrupting production"),
            ]
            ir_html = "".join(
                f'<div style="display:flex;align-items:flex-start;gap:0.8rem;padding:0.7rem 0;border-bottom:1px solid rgba(173,200,255,0.07);">'
                f'<div style="flex-shrink:0;width:10px;height:10px;border-radius:50%;background:{c};margin-top:4px;"></div>'
                f'<div><div style="font-size:0.86rem;font-weight:700;color:{c};">{role}</div>'
                f'<div style="font-size:0.82rem;color:var(--muted);">{desc}</div></div></div>'
                for role, c, desc in ir_members
            )
            st.markdown(
                f'<div style="background:rgba(13,27,45,0.95);border:1px solid rgba(173,200,255,0.14);border-radius:16px;padding:0.8rem 1.1rem;margin-bottom:1.2rem;">{ir_html}</div>',
                unsafe_allow_html=True
            )

            # ── IR LIFECYCLE FLOWCHART (Graphviz-style using HTML/CSS) ─────────
            st.markdown("<h3 style='color:var(--text);margin:1.4rem 0 0.6rem;'>IR Lifecycle — Workflow Cycle</h3>", unsafe_allow_html=True)

            ir_steps = [
                ("01", "Detection",       "#7cc6ff", "Via SOC alerts, EDR events, cloud log anomalies"),
                ("02", "Validation",      "#8b9dff", "IR team confirms incident severity and scope"),
                ("03", "Containment",     "#ffcf7d", "Isolate systems, disable accounts, block traffic"),
                ("04", "Eradication",     "#ff9a9a", "Remove malware, patch vulnerabilities"),
                ("05", "Recovery",        "#80d7a5", "Restore systems, validate backups, rebuild"),
                ("06", "Lessons Learned", "#bc8cff", "Update playbooks, policies, and controls"),
            ]

            # Build the flowchart as a horizontal chain with arrows
            steps_html = ""
            for i, (num, title, color, desc) in enumerate(ir_steps):
                arrow = f'<div style="display:flex;align-items:center;padding:0 4px;"><div style="width:28px;height:2px;background:{color}44;"></div><div style="width:0;height:0;border-top:5px solid transparent;border-bottom:5px solid transparent;border-left:8px solid {color}66;"></div></div>' if i < len(ir_steps) - 1 else ""
                steps_html += (
                    f'<div style="display:flex;align-items:center;">'
                    f'<div style="background:rgba(13,27,45,0.96);border:1px solid {color}44;border-top:3px solid {color};'
                    f'border-radius:14px;padding:0.75rem 0.7rem;text-align:center;min-width:110px;max-width:130px;">'
                    f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.58rem;color:{color};opacity:0.7;margin-bottom:3px;">{num}</div>'
                    f'<div style="font-size:0.8rem;font-weight:700;color:{color};margin-bottom:4px;">{title}</div>'
                    f'<div style="font-size:0.68rem;color:#8fa6c7;line-height:1.4;">{desc}</div>'
                    f'</div>'
                    f'{arrow}'
                    f'</div>'
                )

            st.markdown(
                f'<div style="display:flex;align-items:stretch;overflow-x:auto;padding:0.5rem 0 0.8rem;gap:0;">{steps_html}</div>',
                unsafe_allow_html=True
            )


            # Playbook coverage note
            st.markdown("""
            <div style="background:rgba(124,198,255,0.05);border:1px solid rgba(124,198,255,0.14);border-radius:12px;
                        padding:0.7rem 1rem;margin-top:0.4rem;font-size:0.84rem;color:var(--muted);">
                <strong style="color:var(--accent);">Playbooks created for:</strong>
                Ransomware &nbsp;·&nbsp; Phishing &nbsp;·&nbsp; OT Compromise &nbsp;·&nbsp; Cloud Breaches &nbsp;·&nbsp; Vendor-Related Incidents
            </div>
            """, unsafe_allow_html=True)

            # ── GOVERNANCE COMMITTEES FLOWCHART ────────────────────────────────
            st.markdown("<h3 style='color:var(--text);margin:1.8rem 0 0.5rem;'>Governance Committee Structure</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:var(--soft);font-size:0.88rem;margin-bottom:1rem;'>Multi-layer governance ensuring accountability, oversight, and alignment with business objectives. Committees meet monthly (operational) and quarterly (executive-level).</p>", unsafe_allow_html=True)

            # Central CISO node + 3 committees
            st.markdown("""
            <div style="display:flex;flex-direction:column;align-items:center;gap:0;margin-bottom:1.2rem;">
                <!-- CISO hub -->
                <div style="background:linear-gradient(135deg,rgba(124,198,255,0.18),rgba(139,157,255,0.12));
                            border:2px solid rgba(124,198,255,0.4);border-radius:20px;
                            padding:0.9rem 2rem;text-align:center;min-width:260px;">
                    <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:var(--accent);text-transform:uppercase;letter-spacing:0.12em;">Central Authority</div>
                    <div style="font-size:1.1rem;font-weight:800;color:var(--text);margin-top:3px;">CISO</div>
                    <div style="font-size:0.75rem;color:var(--muted);margin-top:3px;">Centralized Security Governance</div>
                </div>
                <!-- Connector line -->
                <div style="width:2px;height:28px;background:rgba(173,200,255,0.2);"></div>
                <!-- Horizontal connector bar -->
                <div style="width:80%;height:2px;background:rgba(173,200,255,0.15);position:relative;">
                    <div style="position:absolute;left:0;top:-4px;width:2px;height:10px;background:rgba(173,200,255,0.25);"></div>
                    <div style="position:absolute;left:50%;transform:translateX(-50%);top:-4px;width:2px;height:10px;background:rgba(173,200,255,0.25);"></div>
                    <div style="position:absolute;right:0;top:-4px;width:2px;height:10px;background:rgba(173,200,255,0.25);"></div>
                </div>
                <div style="width:80%;display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.75rem;margin-top:0;">
                    <!-- short drop lines -->
                </div>
            </div>
            """, unsafe_allow_html=True)

            gov_committees = [
                {
                    "name": "Cybersecurity Steering Committee",
                    "color": "#7cc6ff",
                    "members": "CISO · CIO · OT Director · Compliance Officer · HR · Legal · CFO",
                    "cadence": "Monthly / Quarterly",
                    "responsibilities": [
                        "Review enterprise risk posture",
                        "Approve major security initiatives",
                        "Oversee Zero Trust implementation",
                        "Review incident reports and metrics",
                        "Ensure alignment with business strategy",
                    ],
                },
                {
                    "name": "Risk & Compliance Committee",
                    "color": "#80d7a5",
                    "members": "Compliance Officer · Legal · IT · Cloud",
                    "cadence": "Monthly",
                    "responsibilities": [
                        "Align with NIST CSF 2.0 and NIST 800-82",
                        "Track remediation progress",
                        "Review audit findings",
                        "Ensure policy and regulatory adherence",
                    ],
                },
                {
                    "name": "Architecture Review Board",
                    "color": "#bc8cff",
                    "members": "CISO · Cloud Engineering · IT · OT Director",
                    "cadence": "Per-project / Quarterly",
                    "responsibilities": [
                        "Approve network segmentation changes",
                        "Review cloud and OT integrations",
                        "Validate identity and access changes",
                        "Ensure secure design principles",
                    ],
                },
            ]

            g1, g2, g3 = st.columns(3, gap="small")
            for col, gc in zip([g1, g2, g3], gov_committees):
                c = gc["color"]
                li = "".join(f"<li>{r}</li>" for r in gc["responsibilities"])
                with col:
                    st.markdown(f"""
                    <div style="background:rgba(13,27,45,0.95);border:1px solid {c}33;border-top:3px solid {c};
                                border-radius:16px;padding:1rem;height:100%;">
                        <div style="font-size:0.84rem;font-weight:700;color:{c};margin-bottom:0.5rem;">{gc['name']}</div>
                        <div style="font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:var(--soft);
                                    margin-bottom:0.4rem;">{gc['cadence']}</div>
                        <div style="font-size:0.74rem;color:var(--muted);margin-bottom:0.6rem;padding-bottom:0.5rem;
                                    border-bottom:1px solid rgba(173,200,255,0.08);">{gc['members']}</div>
                        <ul style="padding-left:1rem;margin:0;font-size:0.8rem;color:var(--muted);">{li}</ul>
                    </div>""", unsafe_allow_html=True)

    # ════════════════════════════════════
    # 03B — GOVERNANCE & POLICY
    # ════════════════════════════════════
    with main_tabs[1]:
        inner = st.tabs(["Governance Model", "Policy Frameworks", "RACI Matrix", "Training & Metrics"])

        with inner[0]:
            callout("<strong>Recommendation:</strong> NovaDrive needs a single governance model that connects cloud, IT, OT, compliance, and leadership decisions to production uptime and ransomware resilience.")

            met_grid([
                ("CISO", "Single Owner", "Central accountability for enterprise security risk."),
                ("4", "Core Functions", "IT, Cloud, OT, and Compliance aligned under one model."),
                ("Monthly", "Risk Review", "Regular steering committee updates before issues become outages."),
                ("JIT", "Business Focus", "Governance decisions prioritize uptime and contractual reliability."),
            ])

            st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Centralized Security Governance Model</h3>", unsafe_allow_html=True)
            st.markdown("""
            <div class="gov-org">
                <div class="gov-top">
                    <div class="gov-role">CISO</div>
                    <div class="gov-sub">Enterprise security accountability · policy direction · executive reporting</div>
                </div>
                <div class="gov-line"></div>
                <div class="gov-branches">
                    <div class="gov-branch">
                        <div class="icon">💻</div>
                        <div class="name">Corporate IT</div>
                        <div class="desc">endpoints · ERP · identity support · incident response</div>
                    </div>
                    <div class="gov-branch">
                        <div class="icon">☁️</div>
                        <div class="name">Cloud Engineering</div>
                        <div class="desc">AWS/Azure security · CSPM · logging · IAM</div>
                    </div>
                    <div class="gov-branch">
                        <div class="icon">🏭</div>
                        <div class="name">OT / Manufacturing</div>
                        <div class="desc">PLCs · SCADA · robotics · production safety</div>
                    </div>
                    <div class="gov-branch">
                        <div class="icon">⚖️</div>
                        <div class="name">Compliance & Legal</div>
                        <div class="desc">policy evidence · audits · contracts · reporting</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2, c3 = st.columns(3, gap="medium")
            with c1:
                card("Cybersecurity Steering Committee", """
<p><strong>Members:</strong> CISO, CIO, OT Director, Compliance, HR, Legal, CFO</p>
<p><strong>Purpose:</strong> approve priorities, funding, risk decisions, and Zero Trust direction.</p>
<p><strong>CEO value:</strong> one view of cyber risk tied to business impact.</p>""", "accent")
            with c2:
                card("Risk & Compliance Committee", """
<p><strong>Members:</strong> Compliance, Legal, IT, Cloud</p>
<p><strong>Purpose:</strong> track remediation, review audits, and measure framework alignment.</p>
<p><strong>CEO value:</strong> evidence that controls are improving and risk is not hidden.</p>""", "warn")
            with c3:
                card("Architecture Review Board", """
<p><strong>Members:</strong> CISO, IT, Cloud, OT leadership</p>
<p><strong>Purpose:</strong> approve segmentation, identity, and integration changes.</p>
<p><strong>CEO value:</strong> prevents insecure changes from weakening production resilience.</p>""", "good")

        with inner[1]:
            callout("<strong>Policy objective:</strong> each policy below closes a specific gap already identified in the assessment.")

            st.markdown("""
            <div class="policy-grid">
                <div class="policy-card">
                    <div class="pol-icon">🔐</div>
                    <div class="pol-title">IAM Policy</div>
                    <div class="pol-gap">Closes: weak MFA, excessive privileges, and inconsistent access reviews.</div>
                </div>
                <div class="policy-card">
                    <div class="pol-icon">☁️</div>
                    <div class="pol-title">Cloud Security Policy</div>
                    <div class="pol-gap">Closes: misconfigured storage, missing baselines, and cloud drift.</div>
                </div>
                <div class="policy-card">
                    <div class="pol-icon">🌐</div>
                    <div class="pol-title">Segmentation Policy</div>
                    <div class="pol-gap">Closes: flat IT/OT networks and uncontrolled lateral movement.</div>
                </div>
                <div class="policy-card">
                    <div class="pol-icon">🚨</div>
                    <div class="pol-title">Incident Response Policy</div>
                    <div class="pol-gap">Closes: slow response, unclear escalation, and weak containment.</div>
                </div>
                <div class="policy-card">
                    <div class="pol-icon">🛡️</div>
                    <div class="pol-title">Data Protection Policy</div>
                    <div class="pol-gap">Closes: weak encryption, data handling, and extortion exposure.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<h3 style='margin-top:1.1rem;color:var(--text);'>Policy → Executive Benefit</h3>", unsafe_allow_html=True)
            st.markdown("""
            <table class="nd-table">
            <thead><tr><th>Policy Area</th><th>What It Controls</th><th>Executive Benefit</th></tr></thead>
            <tbody>
            <tr><td><strong>Identity</strong></td><td>MFA, least privilege, access lifecycle</td><td>Reduces likelihood of unauthorized access and privilege escalation</td></tr>
            <tr><td><strong>Cloud</strong></td><td>Secure baselines, CSPM, configuration standards</td><td>Prevents avoidable ransomware entry points</td></tr>
            <tr><td><strong>Network</strong></td><td>Segmentation, ZTNA, IT/OT isolation</td><td>Limits blast radius and protects unaffected facilities</td></tr>
            <tr><td><strong>Incident Response</strong></td><td>Escalation, containment, recovery actions</td><td>Shortens downtime and improves crisis decision-making</td></tr>
            <tr><td><strong>Data Protection</strong></td><td>Encryption, classification, access monitoring</td><td>Protects engineering IP, contracts, and employee records</td></tr>
            </tbody>
            </table>
            """, unsafe_allow_html=True)

        with inner[2]:
            callout("The RACI model turns governance into accountability. During a ransomware event, NovaDrive should not be guessing who owns identity lockout, cloud containment, OT safety, or executive reporting.")

            st.markdown("""
            <div class="raci-mini">
                <div class="raci-mini-card">
                    <div class="letter raci-r">R</div>
                    <div class="label">Responsible</div>
                    <div class="example">Team doing the work — IT, Cloud, or OT.</div>
                </div>
                <div class="raci-mini-card">
                    <div class="letter raci-a">A</div>
                    <div class="label">Accountable</div>
                    <div class="example">CISO owns security outcomes and escalation.</div>
                </div>
                <div class="raci-mini-card">
                    <div class="letter raci-c">C</div>
                    <div class="label">Consulted</div>
                    <div class="example">Teams providing expertise before decisions.</div>
                </div>
                <div class="raci-mini-card">
                    <div class="letter raci-i">I</div>
                    <div class="label">Informed</div>
                    <div class="example">Executives kept updated on risk and progress.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            raci_table([
                ("Governance",              "A","C","C","C","I"),
                ("IAM Overview",            "A","R","R","C","I"),
                ("Cloud Security",          "A","C","R","C","I"),
                ("OT Security / Monitoring","A","C","C","R","I"),
                ("Incident Response",       "A","R","R","R","C"),
                ("Employee Training Program","A","R","C","C","I"),
                ("Risk Reporting / Metrics","A","C","C","C","R"),
            ])

            callout("<strong>Main takeaway:</strong> The CISO is accountable, technical teams are responsible for execution, OT is consulted where production safety matters, and executives receive business-level risk reporting.", "good")

        with inner[3]:
            callout("<strong>Training strategy:</strong> NovaDrive should train people based on the risk they can create or reduce. The goal is fewer successful phishing clicks, faster reporting, and stronger response during ransomware events.")

            components.html("""<!DOCTYPE html>
<html>
<head>
<style>
  html, body { margin:0; padding:0; background:#0d1b2d; }
  .nd-wrap {
    background:#0d1b2d;
    border:1px solid rgba(173,200,255,0.18);
    border-left:3px solid #7cc6ff;
    border-radius:16px;
    padding:1.1rem 1.1rem 0.9rem;
  }
  .nd-label {
    font-family:'Courier New',monospace;
    font-size:0.65rem;
    letter-spacing:0.16em;
    text-transform:uppercase;
    color:#7cc6ff;
    margin-bottom:0.85rem;
  }
</style>
</head>
<body>
<div class="nd-wrap">
  <div class="nd-label">Role-Based Training Flow</div>

  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 500" style="width:100%;display:block;">
    <defs>
      <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M2 1L8 5L2 9" fill="none" stroke="#7cc6ff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </marker>
    </defs>

    <!-- Tier 1 -->
    <rect x="205" y="10" width="350" height="66" rx="14"
          fill="#0f2540" stroke="#7cc6ff" stroke-width="1" stroke-opacity="0.45"/>
    <text x="380" y="38" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="14" font-weight="700" fill="#eaf2ff">Basic Security Training</text>
    <text x="380" y="58" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">All employees · phishing · MFA · reporting</text>

    <!-- Split arrows -->
    <line x1="310" y1="76" x2="145" y2="150" stroke="#7cc6ff" stroke-width="1.2" stroke-opacity="0.55" marker-end="url(#arr)"/>
    <line x1="380" y1="76" x2="380" y2="150" stroke="#7cc6ff" stroke-width="1.2" stroke-opacity="0.55" marker-end="url(#arr)"/>
    <line x1="450" y1="76" x2="615" y2="150" stroke="#7cc6ff" stroke-width="1.2" stroke-opacity="0.55" marker-end="url(#arr)"/>

    <!-- Role 1 -->
    <rect x="20" y="150" width="230" height="110" rx="14"
          fill="#171a33" stroke="#8b9dff" stroke-width="1" stroke-opacity="0.5"/>
    <text x="135" y="177" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="13" font-weight="700" fill="#8b9dff">IT &amp; Cloud Teams</text>
    <text x="135" y="199" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">AWS/Azure security</text>
    <text x="135" y="215" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">misconfiguration risk</text>
    <text x="135" y="231" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">least privilege</text>

    <!-- Role 2 -->
    <rect x="265" y="150" width="230" height="110" rx="14"
          fill="#24210f" stroke="#ffcf7d" stroke-width="1" stroke-opacity="0.5"/>
    <text x="380" y="177" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="13" font-weight="700" fill="#ffcf7d">OT / Manufacturing Staff</text>
    <text x="380" y="199" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">abnormal machine behavior</text>
    <text x="380" y="215" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">safe escalation</text>
    <text x="380" y="231" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">production safety</text>

    <!-- Role 3 -->
    <rect x="510" y="150" width="230" height="110" rx="14"
          fill="#0f2019" stroke="#80d7a5" stroke-width="1" stroke-opacity="0.5"/>
    <text x="625" y="177" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="13" font-weight="700" fill="#80d7a5">Executives &amp; Management</text>
    <text x="625" y="199" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">tabletop exercises</text>
    <text x="625" y="215" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">risk decisions</text>
    <text x="625" y="231" text-anchor="middle" font-family="Inter,Arial,sans-serif" font-size="11" fill="#8fa6c7">crisis communication</text>

    <!-- Merge lines to center -->
    <line x1="135" y1="260" x2="300" y2="325" stroke="#7cc6ff" stroke-width="1.2" stroke-opacity="0.5" marker-end="url(#arr)"/>
    <line x1="380" y1="260" x2="380" y2="325" stroke="#7cc6ff" stroke-width="1.2" stroke-opacity="0.5" marker-end="url(#arr)"/>
    <line x1="625" y1="260" x2="460" y2="325" stroke="#7cc6ff" stroke-width="1.2" stroke-opacity="0.5" marker-end="url(#arr)"/>

    <!-- Final box 1 -->
    <rect x="100" y="325" width="260" height="82" rx="14"
          fill="#10253b" stroke="#7cc6ff" stroke-width="1" stroke-opacity="0.55"/>
    <text x="230" y="356" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="13" font-weight="700" fill="#eaf2ff">Continuous Training</text>
    <text x="230" y="377" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="10.5" fill="#8fa6c7">quarterly refreshers · short videos</text>
    <text x="230" y="392" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="10.5" fill="#8fa6c7">scenarios · required completion</text>

    <!-- Final box 2 -->
    <rect x="400" y="325" width="260" height="82" rx="14"
          fill="#201818" stroke="#ff9a9a" stroke-width="1" stroke-opacity="0.55"/>
    <text x="530" y="356" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="13" font-weight="700" fill="#eaf2ff">Attack Simulations</text>
    <text x="530" y="377" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="10.5" fill="#8fa6c7">phishing simulations · ransomware drills</text>
    <text x="530" y="392" text-anchor="middle"
          font-family="Inter,Arial,sans-serif" font-size="10.5" fill="#8fa6c7">hands-on response practice</text>

  </svg>
</div>
</body>
</html>""", height=675)

            st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Executive Metrics Dashboard</h3>", unsafe_allow_html=True)
            met_grid([
                ("↓ MTTD", "Detect Faster", "Mean Time to Detect should trend downward."),
                ("↓ MTTR", "Respond Faster", "Mean Time to Respond should trend downward."),
                (">95%", "Training Completion", "Baseline awareness coverage across employees."),
                ("<5%", "Phishing Failure", "Lower click rate means lower human-entry risk."),
            ])

            st.markdown("""
            <table class="nd-table">
            <thead><tr><th>Metric</th><th>Target</th><th>Why Executives Care</th></tr></thead>
            <tbody>
            <tr><td><strong>Suspicious Activity Reporting</strong></td><td>Quarter-over-quarter increase</td><td>Employees become an early warning layer.</td></tr>
            <tr><td><strong>Tabletop Participation</strong></td><td>100% of required leaders</td><td>Confirms leadership can make decisions during a ransomware event.</td></tr>
            <tr><td><strong>Repeat Non-Compliance</strong></td><td>Downward trend</td><td>Highlights departments needing management intervention.</td></tr>
            </tbody>
            </table>
            """, unsafe_allow_html=True)

            callout("<strong>Reporting cadence:</strong> monthly review by the CISO and steering committee, with a quarterly executive summary focused on trends, outliers, business risk, and remediation actions.", "good")

    # ════════════════════════════════════
    # 03C — ROADMAP & FINANCIALS
    # ════════════════════════════════════
    with main_tabs[2]:
        tab1, tab2, tab3 = st.tabs([
            "Phased Implementation Plan",
            "Resource Requirements",
            "Budget Estimation & Justification"
        ])

    # ─────────────────────────────────────────────
    # 1. PHASED IMPLEMENTATION PLAN
    # ─────────────────────────────────────────────
        with tab1:
            callout(
                "<strong>Roadmap logic:</strong> Start by reducing immediate ransomware risk, then build visibility and containment, and finally optimize toward long-term Zero Trust maturity.",
                "accent"
            )

            phases = [
                {
                    "phase": "Phase 1",
                    "title": "Short-Term",
                    "timeline": "0–6 Months",
                    "focus": "Immediate Risk Mitigation",
                    "items": [
                        "Universal MFA for all employees",
                        "IAM audit and removal of overly permissive roles",
                        "CSPM deployment for AWS/Azure misconfiguration detection",
                        "Immutable backups for critical systems",
                        "Mandatory awareness training"
                    ],
                    "color": "var(--danger)"
                },
                {
                    "phase": "Phase 2",
                    "title": "Mid-Term",
                    "timeline": "6–18 Months",
                    "focus": "Visibility & Containment",
                    "items": [
                        "Network segmentation using VPCs and NACLs",
                        "SIEM and SOC deployment",
                        "Zero Trust vendor access",
                        "Incident response playbooks",
                        "Centralized logging integration (CloudTrail, Azure logs)"
                    ],
                    "color": "var(--warn)"
                },
                {
                    "phase": "Phase 3",
                    "title": "Long-Term",
                    "timeline": "18+ Months",
                    "focus": "Optimization & Resilience",
                    "items": [
                        "Full Zero Trust maturity across all environments",
                        "Automated disaster recovery triggers",
                        "Advanced anomaly detection (AI-assisted)",
                        "Continuous improvement and executive reporting"
                    ],
                    "color": "var(--good)"
                }
            ]

            for p in phases:
                items_html = "".join(f"<li>{item}</li>" for item in p["items"])
                st.markdown(f"""
                <div class="phase-block" style="border-left:4px solid {p['color']};">
                    <span class="phase-label" style="color:{p['color']};">{p['phase']} · {p['timeline']}</span>
                    <div class="phase-title">{p['title']} — {p['focus']}</div>
                    <ul style="margin-top:0.4rem;">{items_html}</ul>
                </div>
                """, unsafe_allow_html=True)

            callout(
                "<strong>Main takeaway:</strong> This roadmap prioritizes controls that reduce ransomware likelihood first, then builds detection, containment, and long-term resilience.",
                "good"
            )

    # ─────────────────────────────────────────────
    # 2. RESOURCE REQUIREMENTS
    # ─────────────────────────────────────────────
        with tab2:
            callout(
                "<strong>Resource strategy:</strong> Staffing, tools, and training investments directly support ransomware prevention, detection, and recovery.",
                "accent"
            )

            c1, c2, c3 = st.columns(3, gap="medium")

            with c1:
                card("👥 Staffing", """
<ul>
<li><strong>Cybersecurity Architect:</strong> IT/OT segmentation and architecture oversight</li>
<li><strong>SOC Analysts:</strong> SIEM monitoring and incident escalation</li>
<li><strong>Contracted IR Team:</strong> on-call ransomware response support</li>
</ul>
""", "accent")

            with c2:
                card("🛠️ Tools", """
<ul>
<li><strong>CSPM:</strong> cloud misconfiguration detection</li>
<li><strong>SIEM / EDR:</strong> centralized logging and endpoint visibility</li>
<li><strong>Immutable Storage:</strong> ransomware-resistant backups</li>
</ul>
""", "warn")

            with c3:
                card("🎓 Training", """
<ul>
<li><strong>Security Awareness:</strong> employee phishing and reporting training</li>
<li><strong>OT Training:</strong> plant-specific threat awareness</li>
<li><strong>Security Champions:</strong> local advocates across facilities</li>
</ul>
""", "good")

    # ─────────────────────────────────────────────
    # 3. BUDGET ESTIMATION & JUSTIFICATION
    # ─────────────────────────────────────────────
    with tab3:
        callout(
            "<strong>Estimated Investment: $500,000–$700,000 Year 1</strong><br><br>"
            "NovaDrive’s reliance on Just-In-Time manufacturing means a single day of total outage could exceed "
            "<strong>$1M in penalties and lost productivity</strong>. This investment acts as an insurance policy "
            "against catastrophic ransomware disruption.",
            "warn"
        )

        met_grid([
            ("$500K–$700K", "Year 1 Budget", "Estimated investment for staffing, tools, training, and response readiness."),
            ("$1M+", "Potential Daily Loss", "Possible penalties and productivity loss from a major outage."),
            ("80%", "Likelihood Reduction", "Estimated reduction from closing Azure/cloud entry points."),
            ("90%", "Blast Radius Reduction", "Estimated reduction through Zero Trust segmentation and containment."),
        ])

        st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Cost-Benefit Analysis</h3>", unsafe_allow_html=True)

        c1, c2 = st.columns(2, gap="medium")

        with c1:
            card("🛡️ Operational Resilience", """
<ul>
<li><strong>Downtime mitigation:</strong> contains incidents to smaller network segments.</li>
<li><strong>Shortened RTO:</strong> restores systems in hours instead of weeks using immutable backups.</li>
<li><strong>Cyber insurance readiness:</strong> MFA, backups, and monitoring support eligibility requirements.</li>
</ul>
""", "good")

        with c2:
            card("⚔️ Strategic Enablement", """
<ul>
<li><strong>Supplier right to play:</strong> improves competitiveness during OEM cybersecurity audits.</li>
<li><strong>IP protection:</strong> safeguards CAD/CAM files and electronic control module schematics.</li>
<li><strong>Organizational trust:</strong> supports future investment in 5G, robotics, and smart-factory systems.</li>
</ul>
""", "accent")

        st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Risk Reduction Quantification</h3>", unsafe_allow_html=True)

        st.markdown("""
        <div class="flow-grid" style="grid-template-columns:repeat(2,1fr);">
            <div class="flow-step">
                <span class="flow-num">Likelihood Reduction</span>
                <span class="flow-name">Cloud Entry Point Closure</span>
                <span class="flow-desc">CSPM, IAM cleanup, and secure cloud baselines reduce opportunistic attack success by addressing exposed Azure/AWS resources.</span>
            </div>
            <div class="flow-step">
                <span class="flow-num">Impact Reduction</span>
                <span class="flow-name">Blast Radius Containment</span>
                <span class="flow-desc">Zero Trust segmentation prevents a localized ransomware event from spreading across all facilities and production systems.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<h3 style='margin-top:1.2rem;color:var(--text);'>Change Management Considerations</h3>", unsafe_allow_html=True)

        st.markdown("""
        <table class="nd-table">
            <thead>
                <tr>
                    <th>Challenge</th>
                    <th>Strategy</th>
                    <th>Goal</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Workflow Impact</strong><br>MFA and segment-specific logins may change daily user workflows.</td>
                    <td>Pilot Program at Tennessee Plant</td>
                    <td>Refine rollout before expanding to all facilities.</td>
                </tr>
                <tr>
                    <td><strong>Operational Continuity</strong><br>Security changes must not disrupt production cycles.</td>
                    <td>Coordinated Governance with Plant Managers</td>
                    <td>Maintain zero-downtime integration and safety compliance.</td>
                </tr>
                <tr>
                    <td><strong>Productivity Perception</strong><br>Employees may view security as slowing down operations.</td>
                    <td>Security Champions Program</td>
                    <td>Build peer-to-peer advocacy and cultural buy-in.</td>
                </tr>
            </tbody>
        </table>
        """, unsafe_allow_html=True)

        callout(
            "<strong>Main takeaway:</strong> The budget is justified because the cost of prevention is significantly lower than the cost of a ransomware-driven production outage.",
            "good"
        )