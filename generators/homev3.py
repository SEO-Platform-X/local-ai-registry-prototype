import re,sys
sys.path.insert(0,'/tmp/gen')
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
_src=open('/tmp/gen/brands.py').read(); exec(_src[_src.index("S='fill"):_src.index('def card')])
def tint(col,a=0.12):
    r,g,b=int(col[1:3],16),int(col[3:5],16),int(col[5:7],16); return f'rgb({round(r*a+255*(1-a))}, {round(g*a+255*(1-a))}, {round(b*a+255*(1-a))})'
def span_end(s,a,tag='div'):
    d=0
    for m in re.finditer(r'<(/?)'+tag+r'\b[^>]*>',s[a:]):
        d+= -1 if m.group(1) else 1
        if d==0: return a+m.end()
s=open(P+'Home.dc.html').read()
he=s.index('</header>',s.index('</helmet>'))+9
ph=s.index('<div id="phSections"')
old=s[he:ph]
search=old[old.index('<label class="sbox">'):old.index('</a></span>',old.index('<span class="chips">'))+11]
a=old.index('<div class="vsg">'); vsg=old[a:span_end(old,a)]
a=old.index('<div class="tg">'); tg=old[a:span_end(old,a)]
N='#13203a'; R='#e5482d'; G='#237233'; O='#e8740c'
# ---------- the explainer (SVG): locals say -> owner confirms -> AI answers
EXP=f'''<svg viewBox="0 0 600 560" width="600" height="560" role="img" aria-label="Locals share what is true, the owner confirms it, and AI repeats it" font-family="Figtree,sans-serif">
<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#b9b0a0"/></marker></defs>
<g><circle cx="40" cy="46" r="20" fill="#dfe8f5"/><text x="40" y="51" font-size="12" font-weight="700" text-anchor="middle" fill="{N}">AM</text>
<rect x="72" y="18" width="300" height="56" rx="16" fill="#ffffff" stroke="#e4ded2"/><text x="92" y="42" font-size="15" font-weight="600" fill="{N}">"Dr. Nair will not overdo filler."</text><text x="92" y="62" font-size="12" fill="#8a93a3">aisha_m · went · ▲ 41</text>
<circle cx="248" cy="118" r="20" fill="#fdecea"/><text x="248" y="123" font-size="12" font-weight="700" text-anchor="middle" fill="{N}">TR</text>
<rect x="280" y="90" width="300" height="56" rx="16" fill="#ffffff" stroke="#e4ded2"/><text x="300" y="114" font-size="15" font-weight="600" fill="{N}">"Closed Mondays now. Park level 3."</text><text x="300" y="134" font-size="12" fill="#8a93a3">turtle_rock_ren · heads-up</text></g>
<text x="16" y="178" font-size="11" font-weight="700" letter-spacing="2" fill="{R}">1  LOCALS SAY IT</text>
<path d="M300 150 C 300 170, 300 176, 300 196" stroke="#b9b0a0" stroke-width="2" fill="none" stroke-dasharray="4 4" marker-end="url(#ar)"/>
<g transform="translate(90 204)"><rect width="420" height="176" rx="16" fill="#ffffff" stroke="{N}" stroke-width="2"/>
<rect x="20" y="20" width="44" height="44" rx="10" fill="{N}"/><text x="42" y="47" font-size="14" font-weight="700" text-anchor="middle" fill="#fff">LA</text>
<text x="78" y="38" font-size="18" font-weight="700" fill="{N}">Lumen Aesthetics</text><text x="78" y="58" font-size="12" fill="#5b6474">Med spa · Irvine · record</text>
<rect x="296" y="24" width="104" height="26" rx="13" fill="#e6f2e8"/><text x="348" y="41" font-size="11" font-weight="700" text-anchor="middle" fill="{G}">✓ Owner confirmed</text>
<line x1="20" y1="80" x2="400" y2="80" stroke="#ece6da"/>
<text x="20" y="104" font-size="14" fill="#5b6474">Known for</text><text x="380" y="104" font-size="14" font-weight="700" text-anchor="end" fill="{N}">Natural lip filler</text><circle cx="392" cy="99" r="5" fill="{G}"/>
<text x="20" y="132" font-size="14" fill="#5b6474">Mondays</text><text x="380" y="132" font-size="14" font-weight="700" text-anchor="end" fill="{N}">Closed</text><circle cx="392" cy="127" r="5" fill="{G}"/>
<text x="20" y="160" font-size="14" fill="#5b6474">Parking</text><text x="380" y="160" font-size="14" font-weight="700" text-anchor="end" fill="{N}">Structure B, level 3</text><circle cx="392" cy="155" r="4.5" fill="none" stroke="{O}" stroke-width="1.6"/></g>
<text x="16" y="404" font-size="11" font-weight="700" letter-spacing="2" fill="{R}">2  THE RECORD HOLDS IT</text>
<path d="M300 384 C 300 404, 300 410, 300 428" stroke="#b9b0a0" stroke-width="2" fill="none" stroke-dasharray="4 4" marker-end="url(#ar)"/>
<g transform="translate(40 436)"><rect width="520" height="110" rx="18" fill="{N}"/>
<rect x="300" y="14" width="204" height="30" rx="15" fill="#2a3a5c"/><text x="402" y="34" font-size="13" text-anchor="middle" fill="#e6e9f0">Best lip filler in Irvine?</text>
<circle cx="30" cy="68" r="14" fill="#2b59d9"/><text x="30" y="73" font-size="11" font-weight="700" text-anchor="middle" fill="#fff">AI</text>
<text x="54" y="64" font-size="15" font-weight="600" fill="#ffffff">"Lumen Aesthetics. Locals say Dr. Nair</text><text x="54" y="84" font-size="15" font-weight="600" fill="#ffffff">keeps it natural. Closed Mondays."</text>
<text x="54" y="102" font-size="11" fill="#aeb6c6">Source: localairegistry.com/lumen</text></g>
<text x="16" y="556" font-size="11" font-weight="700" letter-spacing="2" fill="{R}">3  AI REPEATS IT</text></svg>'''
BR=["Equinox","In-N-Out","Trader Joe's","Lululemon","Patagonia","IKEA","SoulCycle","Sephora"]
BD={x[1]:x for x in B}
strip=''.join(f'<a href="ExploreSearch.dc.html" class="v3-b" data-logo="logos/{BD[n][0]}.svg"><span class="v3-bi" style="color: {BD[n][4]}; background: {tint(BD[n][4])};">{ico(BD[n][3],20)}</span>{n}</a>' for n in BR)
MAP=f'''<svg viewBox="0 0 520 380" width="520" height="380" role="img" aria-label="Map of Irvine with conversations by neighborhood" font-family="Figtree,sans-serif"><rect width="520" height="380" rx="16" fill="#e8e2d4"/>
<g stroke="#f7f3ea" stroke-width="12" fill="none"><path d="M-10 110 L530 80"/><path d="M-10 270 L530 300"/><path d="M130 -10 L170 390"/><path d="M360 -10 L400 390"/></g>
<g stroke="#f7f3ea" stroke-width="5" fill="none"><path d="M-10 190 L530 200"/><path d="M250 -10 L270 390"/></g>
<path d="M420 150 q40 20 100 10 v80 q-60 10 -100 -20z" fill="#cfdcc5"/><path d="M20 300 q50 -30 110 0 v80 h-110z" fill="#cfdcc5"/>'''
for x,y,n,t,big in [(300,150,23,'Irvine Spectrum',True),(110,90,11,'Woodbridge',False),(430,250,9,'Turtle Rock',False),(210,300,14,'UCI',False),(60,210,6,'Northwood',False)]:
    r=30 if big else 22
    MAP+=f'<circle cx="{x}" cy="{y}" r="{r+10}" fill="{R}" opacity="0.14"/><circle cx="{x}" cy="{y}" r="{r}" fill="{R if big else N}"/><text x="{x}" y="{y+6}" font-size="{17 if big else 14}" font-weight="700" text-anchor="middle" fill="#fff">{n}</text><text x="{x}" y="{y+r+18}" font-size="12" font-weight="700" text-anchor="middle" fill="{N}">{t}</text>'
MAP+='</svg>'
CSS='''/*v3*/
.v3h{display:grid;grid-template-columns:minmax(0,1fr) 600px;gap:48px;align-items:center;padding:40px 64px 36px}
.v3h-l{display:flex;flex-direction:column;gap:20px}
.v3h-l h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:96px;line-height:90px;letter-spacing:-0.02em;color:#13203a}
.v3h-l h1 em{color:#e5482d}
.v3h-l .sub{font-size:21px;line-height:30px;color:#3d4658}
.v3h .sbox{width:100% !important;max-width:100% !important;box-sizing:border-box}.v3h .chips{justify-content:flex-start !important}
.v3-strip{display:flex;align-items:center;gap:10px;padding:18px 64px;border-top:1px solid #e4ded2;border-bottom:1px solid #e4ded2;background:#fbf8f3;flex-wrap:wrap}
.v3-strip .l{font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#8a93a3;margin-right:6px}
.v3-b{display:inline-flex;align-items:center;gap:8px;height:44px;padding:0 14px 0 6px;border-radius:9999px;background:#ffffff;border:1px solid #e4ded2;font-family:"Cormorant Garamond",Georgia,serif;font-size:21px;color:#13203a !important;text-decoration:none !important}
.v3-bi{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.v3-more{font-size:14px;font-weight:700;color:#13203a;margin-left:4px}
.v3s{padding:96px 64px 0;display:flex;flex-direction:column;gap:30px}
.v3s h2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:64px;line-height:64px;color:#13203a;letter-spacing:-0.01em}
.v3s h2 em{color:#e5482d}
.v3-live{display:grid;grid-template-columns:520px minmax(0,1fr);gap:28px;align-items:start}
.v3-live .tg{display:flex !important;flex-direction:column;gap:12px}
.v3-live .tc{width:auto !important}
.v3-stats{display:flex;gap:28px;font-size:15px;color:#3d4658}.v3-stats b{font-family:"Cormorant Garamond",Georgia,serif;font-size:34px;font-weight:500;color:#13203a;margin-right:6px}
.v3-dot{display:inline-block;width:12px;height:12px;border-radius:50%;background:#e5482d;margin-right:14px;vertical-align:14px;box-shadow:0 0 0 5px rgba(229,72,45,0.18)}
.v3-two{display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:96px 64px 40px}
.v3-c{display:flex;flex-direction:column;gap:14px;padding:40px;border-radius:16px;text-decoration:none !important;color:#13203a !important}
.v3-c h3{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:48px;line-height:50px}
.v3-c .go{align-self:flex-start;height:52px;padding:0 26px;border-radius:26px;display:inline-flex;align-items:center;font-size:16px;font-weight:700;color:#ffffff}
'''
BODY=f'''<div id="v3Body">
<div class="v3h"><div class="v3h-l"><h1>Locals know. <em>Now AI does too.</em></h1><span class="sub">The public record of every local business.</span>{search}</div><div>{EXP}</div></div>
<div class="v3-strip"><span class="l">Already here</span>{strip}<span class="v3-more">+ 12,400 more</span></div>
<div class="v3s"><div style="display: flex; justify-content: space-between; align-items: flex-end;"><h2><span class="v3-dot"></span>Right now in <em>Irvine</em>.</h2><div class="v3-stats"><span><b>4,812</b>neighbors</span><span><b>1,904</b>answers</span><span><b>41</b>cities</span></div></div><div class="v3-live"><a href="Explore.dc.html">{MAP}</a>{tg}</div></div>
<div class="v3s"><h2>Stars say good. <em>Locals say why.</em></h2>{vsg}</div>
<div class="v3-two"><a href="Explore.dc.html" class="v3-c" style="background: #eef0ea;"><span class="hx">For locals</span><h3>Going somewhere? <em style="color: #e5482d;">Ask who went.</em></h3><span class="go" style="background: #13203a;">Explore Irvine</span></a><a href="ExploreSearch.dc.html" class="v3-c" style="background: #fdece6;"><span class="hx">For owners</span><h3>See what AI says <em style="color: #e5482d;">about you.</em></h3><span class="go" style="background: #e5482d;">Look up my business</span></a></div>
<div style="display: flex; align-items: center; gap: 16px; padding: 40px 64px 0; color: #8a93a3; font-size: 13px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase;"><span style="flex: 1; height: 1px; background: #d9d2c4;"></span>From here down: today's live homepage<span style="flex: 1; height: 1px; background: #d9d2c4;"></span></div><span id="v3End"></span></div>'''
BODY=BODY.replace('<span class="hx">','<span style="font-size: 12px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: #5b6474;">')
s=s[:he]+BODY+s[ph:]
if '/*v3*/' in s:
    a=s.index('/*v3*/'); e=s.index('</style>',a); s=s[:a]+CSS+s[e:]
else:
    j=s.rfind('</style>',0,s.index('</helmet>')); s=s[:j]+CSS+s[j:]
open(P+'Home.dc.html','w').write(s); print('ok',len(s))
open('/tmp/gen/v3parts.py','w').write('EXP='+repr(EXP)+'\nMAP='+repr(MAP)+'\n')
