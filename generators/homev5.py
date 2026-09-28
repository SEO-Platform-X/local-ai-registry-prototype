import re,sys
sys.path.insert(0,'/tmp/gen')
exec(open('/tmp/gen/homev4.py').read().split("s=s[:he]+BODY+s[ph:]")[0])   # reuse v4 pieces: search, feed, CHAT, brands, CSS
G='#237233'
search=search.replace('placeholder="Search a place, or ask a question"','placeholder="Search a place or ask"')
def mk(k): return {'c':'<i class="mk c"></i>','v':'<i class="mk v"></i>','a':'<i class="mk a"></i>'}[k]
ROWS=[('Known for','Natural lip filler','c','Confirmed by the owner'),('Who injects','Dr. Nair, every time','c','Confirmed by the owner'),('Consult','$75, credited if you book','c','Confirmed by the owner'),('Mondays','Closed','v','From turtle_rock_ren\'s heads-up, Sep 22'),('Parking','Structure B, level 3','v','From 4 locals\' tips'),('Lip filler','From $450','a','AI guess, not confirmed yet'),('Busiest','Saturday afternoons','a','AI guess from old reviews')]
rows=''.join(f'<div class="v5-fr{" hl" if i in (0,3,5) else ""}"><span class="k">{k}</span><span class="v">{v} {mk(m)}</span><span class="src {m}">{src}</span></div>' for i,(k,v,m,src) in enumerate(ROWS))
TIPS=[('aisha_m','went','"Dr. Nair talked me down to half a syringe."',41),('turtle_rock_ren','local','"They stopped opening Mondays. Call first."',12),('maria_k','went','"Ask for the numbing cream, it helps a lot."',9)]
tips=''.join(f'<div class="v5-tip"><span class="v5-tu"><b>{u}</b> <i>{h}</i></span><span>{q}</span><span class="v5-tv">▲ {v}</span></div>' for u,h,q,v in TIPS)
PROF=f'''<div class="v5-pw"><div class="v5-bar"><span class="d"></span><span class="d"></span><span class="d"></span><span class="url">localairegistry.com/lumen-aesthetics</span></div>
<div class="v5-p"><div class="v5-gal"><span style="background: #f0dcc4;">Treatment room</span><span style="background: #e3e6dc;">Dr. Nair</span><span style="background: #dfe3ea;">Results wall</span></div>
<div class="v5-ph"><span style="display: flex; flex-direction: column; gap: 2px;"><b style="font-size: 26px; font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 500;">Lumen Aesthetics</b><span class="v5-mu">Med spa · Irvine Spectrum · ★ 4.9</span></span><span class="v4-bd g" style="height: 28px; font-size: 12px;">✓ Claimed by the owner</span></div>
<div class="v5-cols"><div class="v5-facts"><span class="v4-lb">The record</span>{rows}</div><div class="v5-tips"><span class="v4-lb">Where it came from</span>{tips}<span class="v5-mu" style="font-size: 12px;">23 locals wrote this record</span></div></div></div>
</div>'''
CARDS=[('KC','Kettle &amp; Co Coffee','Cafe · Woodbridge','#8a5a2b',[('Known for','Oat cortado','c'),('Laptops','OK before noon','v'),('Wifi','Fast','v')],'18 locals · Owner confirmed',True),
('BT','Backyard Tacos','Tacos · Irvine','#d52b1e',[('Known for','Birria, kid-friendly lawn','v'),('Open late','Until 11 on Fridays','c'),('Parking','Street only','a')],'31 locals · Owner confirmed',True),
('IA','Irvine Auto Care','Auto repair · Irvine','#1f3a5f',[('Known for','Tesla repairs','c'),('Upselling','"Never pushed me"','v'),('Loaner cars','Probably not','a')],'12 locals · Owner confirmed',True),
('SS','Spectrum Smiles','Dentist · Irvine','#2b59d9',[('New patients','This week','c'),('Kids','Great with kids','v'),('Sat hours','9 to 1','a')],'9 locals · Not claimed yet',False),
('GB','Glow Bar Irvine','Med spa · Irvine','#c2708a',[('Known for','Hydrafacials','v'),('Wait time','About 20 min','v'),('Hydrafacial','About $199','a')],'14 locals · Not claimed yet',False),
('YP','Yoga on Park','Yoga · Tustin','#3a6b35',[('Known for','Beginner flow','c'),('Mats','Bring your own','v'),('Showers','Probably yes','a')],'7 locals · Owner confirmed',True),
('HN','Harvest Noodle','Ramen · Irvine','#c9a400',[('Known for','Spicy miso','v'),('Wait','30 min at 7 PM','v'),('Vegan','Ask for broth','a')],'22 locals · Not claimed yet',False),
('CM','Coastline MedSpa','Med spa · Newport Beach','#13203a',[('Known for','Morpheus8','c'),('Consult','Free','c'),('Parking','Validated','v')],'40 locals · Owner confirmed',True)]
def card(ini,n,cat,col,fs,foot,claimed):
    fr=''.join(f'<div class="v5-cf"><span>{k}</span><b>{v} {mk(m)}</b></div>' for k,v,m in fs)
    return f'<a href="ExploreSearch.dc.html" class="v5-card"><span class="v5-ch"><span class="v5-ci" style="background: {col};">{ini}</span><span style="display: flex; flex-direction: column; min-width: 0;"><b>{n}</b><span class="v5-mu" style="font-size: 12px;">{cat}</span></span></span>{fr}<span class="v5-foot{" ok" if claimed else ""}">{foot}</span></a>'
WALL=''.join(card(*c) for c in CARDS)
LEG=f'<div class="v5-leg"><span>{mk("c")} Confirmed by the owner</span><span>{mk("v")} Said by locals</span><span>{mk("a")} AI guess, not confirmed yet</span></div>'
BODY=f'''<div id="v4Body">
<div class="v5-hero"><div class="v5-l"><h1>Written by <em>locals</em>. Read by AI.</h1><p class="v4-sub">Every fact on a page comes from someone who went.</p>{search}{LEG}<div class="v4-proof"><b>4,812</b> neighbors · <b>1,904</b> answers · <b>12,400</b> places</div></div>{PROF}</div>
<div class="v5-wall"><div class="v5-wh"><h2>Every place. <em>Every fact, sourced.</em></h2>{LEG}</div><div class="v5-grid">{WALL}</div><a href="Explore.dc.html" class="v4-all" style="padding-top: 22px;">Browse 12,400 places ⟶</a></div>
<div class="v4-sec" style="grid-template-columns: 420px minmax(0,1fr); align-items: start;"><div class="v4-h"><span class="v5-live"><i></i>Live</span><h2>Right now in <em>Irvine</em>.</h2><p>Every answer here adds to a record.</p></div><div class="v4-feed">{"".join(row(*x) for x in FEED[:4])}<a href="Explore.dc.html" class="v4-all">See all 1,904 conversations ⟶</a></div></div>
<div class="v4-sec v4-dark"><div class="v4-h"><h2 style="color: #ffffff;">Then AI <em>repeats it</em>.</h2><p style="color: #c9d0dc;">ChatGPT, Gemini and Claude read the record.</p></div>{CHAT}</div>
<div class="v4-own"><div class="v4-ol"><span class="v4-lb" style="color: #a8452c;">For business owners</span><h2>Your business <em>already has a page</em>.</h2><p>See what locals and AI say. Free.</p><a href="ExploreSearch.dc.html" class="v4-os"><span style="color: #13203a;">Lumen Aesthetics</span><span class="v4-go">See my page ⟶</span></a><div class="v4-brs"><span class="v4-lb">Already on the registry</span><div style="display: flex; flex-wrap: wrap; gap: 8px;">{brands}<span class="v4-br" style="background: #13203a; color: #ffffff; border-color: #13203a;">+ 12,400 more</span></div></div></div>
<a href="ExploreSearch.dc.html" class="v4-peek"><span class="v4-lb">Your page, right now</span><b style="font-size: 22px;">Lumen Aesthetics</b><span class="v4-pk"><span class="v4-big" style="color: #c13515;">58</span><span>AI Score<br><span class="v4-mu">Irvine average is 71</span></span></span><span class="v4-pr"><b>3</b> facts AI gets wrong</span><span class="v4-pr"><b>7</b> locals waiting for an answer</span><span class="v4-pr"><b>0</b> of 23 questions answered</span><span class="v4-go" style="align-self: stretch; justify-content: center;">Claim it free ⟶</span></a></div>
<div style="display: flex; align-items: center; gap: 16px; padding: 56px 64px 0; color: #8a93a3; font-size: 13px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase;"><span style="flex: 1; height: 1px; background: #d9d2c4;"></span>From here down: today's live homepage<span style="flex: 1; height: 1px; background: #d9d2c4;"></span></div>
</div>'''
CSS5=CSS+'''
.mk.a{width:0;height:0;border-radius:0;border-left:5px solid transparent;border-right:5px solid transparent;border-bottom:9px solid #8a93a3;background:none}
.v5-hero{display:grid;grid-template-columns:430px minmax(0,1fr);gap:48px;align-items:center;padding:40px 64px 56px}
.v5-l{display:flex;flex-direction:column;gap:18px}
.v5-l h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:64px;line-height:62px;letter-spacing:-0.02em;color:#13203a}.v5-l h1 em{color:#e5482d}
.v5-hero .sbox{width:100% !important;max-width:100% !important;box-sizing:border-box}
.v5-leg{display:flex;flex-direction:column;gap:8px;font-size:14px;color:#3d4658}
.v5-leg span{display:flex;align-items:center;gap:8px}
.v5-pw{position:relative;border-radius:16px;background:#ffffff;border:1px solid #d9d2c4;box-shadow:0 30px 70px rgba(19,32,58,0.16);overflow:visible}
.v5-bar{display:flex;align-items:center;gap:6px;height:38px;padding:0 14px;border-bottom:1px solid #ece6da;background:#fbf8f3;border-radius:16px 16px 0 0}
.v5-bar .d{width:10px;height:10px;border-radius:50%;background:#dcd5c7}.v5-bar .url{margin-left:12px;height:24px;padding:0 12px;border-radius:12px;background:#ffffff;border:1px solid #ece6da;display:flex;align-items:center;font-size:12px;color:#5b6474}
.v5-p{padding:14px 20px 18px;display:flex;flex-direction:column;gap:12px}
.v5-gal{display:grid;grid-template-columns:2fr 1fr 1fr;gap:4px;height:92px}.v5-gal span{border-radius:8px;display:flex;align-items:flex-end;padding:6px 8px;font-size:10px;font-weight:700;color:#5b6474}
.v5-ph{display:flex;justify-content:space-between;align-items:center}
.v5-mu{font-size:13px;color:#5b6474}
.v5-cols{display:grid;grid-template-columns:1.35fr 1fr;gap:18px}
.v5-facts,.v5-tips{display:flex;flex-direction:column;gap:6px}
.v5-fr{display:grid;grid-template-columns:96px 1fr;column-gap:10px;padding:6px 8px;border-radius:8px;font-size:14px}
.v5-fr .k{color:#5b6474}.v5-fr .v{font-weight:700;color:#13203a}
.v5-fr .src{grid-column:2;font-size:11px;font-weight:700}.v5-fr .src.c{color:#237233}.v5-fr .src.v{color:#b35a00}.v5-fr .src.a{color:#6b7280}
.v5-fr{border-left:3px solid transparent}.v5-fr.hl{background:#fbf4ea}.v5-fr:has(.src.c){border-left-color:#237233}.v5-fr:has(.src.v){border-left-color:#e8740c}.v5-fr:has(.src.a){border-left-color:#b9b0a0}
.v5-tip{display:flex;flex-direction:column;gap:3px;padding:10px 12px;border-radius:10px;background:#f3efe7;font-size:14px;line-height:19px;color:#13203a}
.v5-tu{font-size:12px}.v5-tu i{font-style:normal;font-size:10px;font-weight:700;text-transform:uppercase;color:#a8452c;margin-left:4px}
.v5-tv{font-size:11px;color:#8a93a3}
.v5-call{position:absolute;height:30px;padding:0 12px;border-radius:15px;display:inline-flex;align-items:center;font-size:12px;font-weight:700;box-shadow:0 8px 20px rgba(19,32,58,0.18);white-space:nowrap}
.v5-call.c1{left:-26px;top:236px;background:#237233;color:#ffffff}
.v5-call.c2{left:-26px;top:380px;background:#e8740c;color:#ffffff}
.v5-call.c3{left:-26px;top:440px;background:#5b6474;color:#ffffff}
.v5-wall{padding:90px 64px 80px;border-top:1px solid #e4ded2;background:#fbf8f3}
.v5-wh{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;margin-bottom:28px}
.v5-wh h2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:54px;line-height:56px;color:#13203a}.v5-wh h2 em{color:#e5482d}
.v5-wh .v5-leg{flex-direction:row;gap:18px;flex-shrink:0}.v5-leg span{white-space:nowrap}
.v5-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.v5-card{font-weight:400;display:flex;flex-direction:column;gap:8px;padding:18px;border-radius:14px;background:#ffffff;border:1px solid #e4ded2;text-decoration:none !important;color:#13203a}
.v5-ch{display:flex;gap:10px;align-items:center;margin-bottom:4px}.v5-ch b{font-size:16px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.v5-ci{width:38px;height:38px;border-radius:10px;color:#ffffff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}
.v5-cf{display:flex;justify-content:space-between;gap:8px;font-size:13px;color:#5b6474;padding:6px 0;border-top:1px solid #f0ebe1}.v5-cf b{color:#13203a;text-align:right}
.v5-foot{margin-top:4px;font-size:11px;font-weight:700;color:#8a93a3}.v5-foot.ok{color:#237233}
.v5-live{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#e5482d}.v5-live i{width:10px;height:10px;border-radius:50%;background:#e5482d;box-shadow:0 0 0 4px rgba(229,72,45,0.18)}
'''
s=s[:he]+BODY+s[ph:]
for m_ in ['/*v3*/','/*hv*/','/*v4*/']:
    if m_ in s:
        a=s.index(m_); e=s.index('</style>',a); s=s[:a]+s[e:]
j=s.rfind('</style>',0,s.index('</helmet>')); s=s[:j]+CSS5+s[j:]
open(P+'Home.dc.html','w').write(s); print('ok',len(s))
open('/tmp/gen/v5parts.py','w').write('ROWS='+repr(ROWS)+'\nCARDS='+repr(CARDS)+'\n')
