import re,sys
sys.path.insert(0,'/tmp/gen')
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
_src=open('/tmp/gen/brands.py').read(); exec(_src[_src.index("S='fill"):_src.index('def card')])
def tint(col,a=0.12):
    r,g,b=int(col[1:3],16),int(col[3:5],16),int(col[5:7],16); return f'rgb({round(r*a+255*(1-a))}, {round(g*a+255*(1-a))}, {round(b*a+255*(1-a))})'
s=open(P+'Home.dc.html').read()
he=s.index('</header>',s.index('</helmet>'))+9
ph=s.index('<div id="phSections"')
old=s[he:ph]
search=old[old.index('<label class="sbox">'):old.index('</sc-if>',old.index('<label class="sbox">'))+8]
search=search.replace('placeholder="Search a business name or a city"','placeholder="Search a place, or ask a question"')
UP='<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 5l8 10H4z"/></svg>'
FEED=[(41,'First time getting lip filler. Who will not overdo it?','Lumen Aesthetics','Beauty','2h','aisha_m','went','Dr. Nair talked me down to half a syringe. Looked like me, just better.','owner',23),
      (33,'Where can kids eat and actually run around?','Backyard Tacos','Food','5h','maria_k','went','Fenced lawn next to the patio. You can see them from every table.','',11),
      (27,'Who knows Teslas and will not upsell me?','Irvine Auto Care','Car','1d','jordan_p','went','Told me my brakes had another 15,000 miles. Honest.','owner',6),
      (19,'Is Saturday parking at Spectrum a nightmare?','Irvine Spectrum','Heads-up','3h','turtle_rock_ren','local','Structure B, level 3. Always open before 11.','',9),
      (7,'Does Dr. Nair do the filler herself or a nurse?','Lumen Aesthetics','Beauty','1h','irvine_regular_42','researching','','need',0)]
def row(v,t,biz,cat,when,who,how,ans,flag,n):
    badge={'owner':'<span class="v4-bd g">✓ Owner answered</span>','need':'<span class="v4-bd r">Needs an answer</span>'}.get(flag,'')
    a=f'<span class="v4-ans"><b>{who}</b> <i>{how}</i> {ans}</span>' if ans else ''
    return f'<a href="{"Thread.dc.html" if flag!="need" else "Thread.dc.html"}" class="v4-row"><span class="v4-v">{UP}<b>{v}</b></span><span class="v4-g"><span class="v4-m"><b>{biz}</b> · {cat} · {when}</span><span class="v4-t">{t}</span>{a}<span class="v4-m">{n} answers {badge}</span></span></a>'
feed=''.join(row(*x) for x in FEED)
N='#13203a'
REC=f'''<div class="v4-rec"><div class="v4-rh"><span class="v4-av">LA</span><span style="display: flex; flex-direction: column; gap: 2px; flex: 1;"><b style="font-size: 22px;">Lumen Aesthetics</b><span class="v4-mu">Med spa · Irvine Spectrum · ★ 4.9</span></span><span class="v4-bd g" style="height: 30px; font-size: 13px;">✓ Owner confirmed</span></div>
<div class="v4-rg"><div class="v4-col"><span class="v4-lb">The facts</span>
<span class="v4-fr"><span>Known for</span><b>Natural lip filler <i class="mk c"></i></b></span><span class="v4-fr"><span>Who injects</span><b>Dr. Nair herself <i class="mk c"></i></b></span><span class="v4-fr"><span>Consult</span><b>$75, credited <i class="mk c"></i></b></span><span class="v4-fr"><span>Mondays</span><b>Closed <i class="mk v"></i></b></span></div>
<div class="v4-col"><span class="v4-lb">What locals say</span><span class="v4-q">"Talked me out of overdoing it." <em>31 locals</em></span><span class="v4-q">"Park on level 3 of Structure B." <em>Tip, 4 locals</em></span><span class="v4-q">"Tuesday mornings are empty." <em>Measured</em></span></div></div>
<div class="v4-legend"><span><i class="mk c"></i> Confirmed by owner</span><span><i class="mk v"></i> Said by a visitor</span><span>23 locals wrote this record</span></div></div>'''
CHAT=f'''<div class="v4-chat"><div class="v4-ch"><span class="v4-dotw"></span><span class="v4-dotw"></span><span class="v4-dotw"></span><span style="margin-left: 10px; font-size: 13px; color: #aeb6c6;">ChatGPT</span></div>
<div class="v4-ub">What is the best place for natural lip filler in Irvine?</div>
<div class="v4-ai"><span class="v4-aiav">AI</span><span style="display: flex; flex-direction: column; gap: 12px;"><span>Locals point to <b>Lumen Aesthetics</b> at Irvine Spectrum. Dr. Nair does every injection herself and is known for keeping it natural. Consults are $75, credited if you book. Note: closed Mondays.</span><span class="v4-cite">Source: localairegistry.com/lumen-aesthetics</span></span></div></div>'''
BR=["Equinox","In-N-Out","Trader Joe's","Lululemon","Patagonia","IKEA","SoulCycle","Sephora"]
BD={x[1]:x for x in B}
brands=''.join(f'<span class="v4-br"><span class="v4-bi" style="color: {BD[n][4]}; background: {tint(BD[n][4])};">{ico(BD[n][3],18)}</span>{n}</span>' for n in BR)
BODY=f'''<div id="v4Body">
<div class="v4-hero"><div class="v4-l"><h1>What locals <em>really</em> say about Irvine.</h1><p class="v4-sub">Real answers from people who went.</p>{search}<div class="v4-try"><span>Try</span><a href="ExploreSearch.dc.html">Natural lip filler?</a><a href="Explore.dc.html">Tacos open late?</a><a href="Explore.dc.html">Honest Tesla mechanic?</a></div><div class="v4-proof"><b>4,812</b> neighbors · <b>1,904</b> answers this month · <b>41</b> cities</div></div>
<div class="v4-feed"><div class="v4-fh"><b style="font-size: 16px;">Irvine ▾</b><span class="v4-tabs"><span class="on">Hot</span><span>New</span><span>Needs an answer</span></span><a href="Explore.dc.html" style="font-size: 14px; font-weight: 700;">See the map</a></div>{feed}<a href="Explore.dc.html" class="v4-all">See all 1,904 conversations ⟶</a></div></div>
<div class="v4-sec"><div class="v4-h"><span class="v4-n">1</span><h2>Every place gets a <em>public record</em>.</h2><p>Written by locals. Confirmed by owners.</p></div>{REC}</div>
<div class="v4-sec v4-dark"><div class="v4-h"><span class="v4-n" style="background: #e5482d;">2</span><h2 style="color: #ffffff;">Then AI <em>repeats it</em>.</h2><p style="color: #c9d0dc;">ChatGPT, Gemini and Claude read the record.</p></div>{CHAT}</div>
<div class="v4-own"><div class="v4-ol"><span class="v4-lb" style="color: #a8452c;">For business owners</span><h2>Your business <em>already has a page</em>.</h2><p>See what locals and AI say. Free.</p><a href="ExploreSearch.dc.html" class="v4-os"><span style="color: #13203a;">Lumen Aesthetics</span><span class="v4-go">See my page ⟶</span></a><div class="v4-brs"><span class="v4-lb">Already on the registry</span><div style="display: flex; flex-wrap: wrap; gap: 8px;">{brands}<span class="v4-br" style="background: #13203a; color: #ffffff; border-color: #13203a;">+ 12,400 more</span></div></div></div>
<a href="ExploreSearch.dc.html" class="v4-peek"><span class="v4-lb">Your page, right now</span><b style="font-size: 22px;">Lumen Aesthetics</b><span class="v4-pk"><span class="v4-big" style="color: #c13515;">58</span><span>AI Score<br><span class="v4-mu">Irvine average is 71</span></span></span><span class="v4-pr"><b>3</b> facts AI gets wrong</span><span class="v4-pr"><b>7</b> locals waiting for an answer</span><span class="v4-pr"><b>0</b> of 23 questions answered</span><span class="v4-go" style="align-self: stretch; justify-content: center;">Claim it free ⟶</span></a></div>
<div style="display: flex; align-items: center; gap: 16px; padding: 56px 64px 0; color: #8a93a3; font-size: 13px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase;"><span style="flex: 1; height: 1px; background: #d9d2c4;"></span>From here down: today's live homepage<span style="flex: 1; height: 1px; background: #d9d2c4;"></span></div>
</div>'''
CSS='''/*v4*/
.v4-hero{display:grid;grid-template-columns:500px minmax(0,1fr);gap:56px;align-items:start;padding:48px 64px 64px}
.v4-l{display:flex;flex-direction:column;gap:18px;padding-top:24px}
.v4-l h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:76px;line-height:74px;letter-spacing:-0.02em;color:#13203a}
.v4-l h1 em{color:#e5482d}
.v4-sub{margin:0;font-size:20px;line-height:28px;color:#3d4658}
.v4-hero .sbox{width:100% !important;max-width:100% !important;box-sizing:border-box}
.v4-try{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:13px;color:#8a93a3}
.v4-try a{height:36px;padding:0 14px;border-radius:18px;background:#ffffff;border:1px solid #e4ded2;display:inline-flex;align-items:center;font-size:14px;font-weight:600;color:#13203a;text-decoration:none}
.v4-proof{font-size:14px;color:#5b6474}.v4-proof b{color:#13203a}
.v4-feed{background:#ffffff;border:1px solid #e4ded2;border-radius:16px;overflow:hidden;box-shadow:0 20px 50px rgba(19,32,58,0.08)}
.v4-fh{display:flex;align-items:center;gap:18px;padding:14px 20px;border-bottom:1px solid #ece6da}
.v4-tabs{display:flex;gap:6px;flex:1}.v4-tabs span{height:32px;padding:0 12px;border-radius:16px;display:inline-flex;align-items:center;font-size:13px;font-weight:700;color:#5b6474}.v4-tabs span.on{background:#13203a;color:#ffffff}
.v4-row{display:flex;gap:14px;padding:14px 20px;border-bottom:1px solid #f0ebe1;text-decoration:none !important;color:#13203a}
.v4-v{width:36px;flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:2px;color:#e5482d;font-size:14px}.v4-v b{color:#13203a}
.v4-g{flex:1;display:flex;flex-direction:column;gap:4px;min-width:0}
.v4-m{font-size:12px;color:#8a93a3;display:flex;gap:8px;align-items:center}.v4-m b{color:#13203a}
.v4-t{font-size:17px;line-height:23px;font-weight:700}
.v4-ans{font-weight:400;font-size:14px;line-height:20px;color:#3d4658;border-left:3px solid #f5e3cc;padding-left:10px}.v4-ans i{font-style:normal;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:#a8452c;margin-right:4px}
.v4-bd{display:inline-flex;align-items:center;height:22px;padding:0 9px;border-radius:11px;font-size:11px;font-weight:700}.v4-bd.g{background:#e6f2e8;color:#1c5f2a}.v4-bd.r{background:#fdecea;color:#b42318}
.v4-all{display:flex;justify-content:center;padding:14px;font-size:14px;font-weight:700;color:#2b59d9 !important;text-decoration:none}
.v4-sec{padding:100px 64px;display:grid;grid-template-columns:420px minmax(0,1fr);gap:56px;align-items:center;border-top:1px solid #e4ded2}
.v4-dark{background:#13203a;border-top:none}
.v4-h{display:flex;flex-direction:column;gap:14px}
.v4-h h2,.v4-ol h2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:60px;line-height:60px;letter-spacing:-0.01em;color:#13203a}
.v4-h h2 em,.v4-ol h2 em{color:#e5482d}
.v4-h p,.v4-ol p{margin:0;font-size:19px;line-height:28px;color:#3d4658}
.v4-n{width:40px;height:40px;border-radius:50%;background:#13203a;color:#ffffff;display:flex;align-items:center;justify-content:center;font-weight:700}
.v4-rec{background:#ffffff;border:2px solid #13203a;border-radius:16px;padding:26px 28px;display:flex;flex-direction:column;gap:18px}
.v4-rh{display:flex;align-items:center;gap:14px}
.v4-av{width:52px;height:52px;border-radius:12px;background:#13203a;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700}
.v4-mu{font-size:14px;color:#5b6474}
.v4-rg{display:grid;grid-template-columns:1fr 1fr;gap:26px;border-top:1px solid #ece6da;padding-top:18px}
.v4-col{display:flex;flex-direction:column;gap:10px}
.v4-lb{font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#8a93a3}
.v4-fr{display:flex;justify-content:space-between;gap:10px;font-size:15px;color:#5b6474;padding-bottom:8px;border-bottom:1px solid #f0ebe1}.v4-fr b{color:#13203a}
.v4-q{font-weight:400;font-size:15px;line-height:21px;color:#13203a}.v4-q em{display:block;font-style:normal;font-size:12px;color:#8a93a3}
.mk{display:inline-block;width:9px;height:9px;border-radius:50%;margin-left:4px;vertical-align:1px}.mk.c{background:#237233}.mk.v{border:1.6px solid #e8740c;box-sizing:border-box}
.v4-legend{display:flex;gap:22px;font-size:13px;color:#5b6474;border-top:1px solid #ece6da;padding-top:14px}
.v4-chat{background:#1b2945;border-radius:18px;padding:22px 26px 28px;display:flex;flex-direction:column;gap:18px;color:#e6e9f0;font-size:18px;line-height:28px}
.v4-ch{display:flex;align-items:center;gap:6px}.v4-dotw{width:10px;height:10px;border-radius:50%;background:#3a4763}
.v4-ub{align-self:flex-end;max-width:70%;background:#2d3d5e;border-radius:18px;padding:12px 18px;font-size:16px}
.v4-ai{display:flex;gap:14px}.v4-aiav{width:34px;height:34px;border-radius:50%;background:#2b59d9;color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}
.v4-cite{align-self:flex-start;height:34px;padding:0 14px;border-radius:17px;background:#e5482d;color:#fff;display:inline-flex;align-items:center;font-size:13px;font-weight:700}
.v4-own{display:grid;grid-template-columns:minmax(0,1fr) 440px;gap:56px;align-items:center;padding:100px 64px;background:#f5e3cc;border-top:1px solid #e6cfb2}
.v4-ol{display:flex;flex-direction:column;gap:16px}
.v4-os{display:flex;align-items:center;justify-content:space-between;height:64px;border-radius:32px;background:#ffffff;padding:0 8px 0 26px;font-size:18px;box-shadow:0 10px 30px rgba(19,32,58,0.12);text-decoration:none !important;max-width:620px}
.v4-go{display:inline-flex;align-items:center;height:50px;padding:0 24px;border-radius:25px;background:#e5482d;color:#ffffff !important;font-size:16px;font-weight:700}
.v4-brs{display:flex;flex-direction:column;gap:10px;margin-top:14px}
.v4-br{display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 12px 0 5px;border-radius:19px;background:#ffffff;border:1px solid #e6cfb2;font-family:"Cormorant Garamond",Georgia,serif;font-size:18px;color:#13203a}
.v4-bi{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.v4-peek{display:flex;flex-direction:column;gap:12px;padding:28px;border-radius:16px;background:#ffffff;border:1px solid #e6cfb2;box-shadow:0 24px 60px rgba(19,32,58,0.14);text-decoration:none !important;color:#13203a}
.v4-pk{display:flex;align-items:center;gap:14px;font-size:15px;font-weight:700}
.v4-big{font-family:"Cormorant Garamond",Georgia,serif;font-size:72px;line-height:66px;font-weight:500}
.v4-pr{display:flex;gap:10px;align-items:baseline;font-size:15px;color:#3d4658;padding:10px 0;border-top:1px solid #f0ebe1}.v4-pr b{font-size:20px;color:#c13515}
'''
s=s[:he]+BODY+s[ph:]
for mk in ['/*v3*/','/*hv*/','/*v4*/']:
    if mk in s:
        a=s.index(mk); e=s.index('</style>',a); s=s[:a]+s[e:]
j=s.rfind('</style>',0,s.index('</helmet>')); s=s[:j]+CSS+s[j:]
open(P+'Home.dc.html','w').write(s); print('ok',len(s))
open('/tmp/gen/v4parts.py','w').write('FEED='+repr(FEED)+'\nREC='+repr(REC)+'\nCHAT='+repr(CHAT)+'\n')
