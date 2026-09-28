import re,sys
sys.path.insert(0,'/tmp/gen')
exec(open('/tmp/gen/homev4.py').read().split("s=s[:he]+BODY+s[ph:]")[0])
X='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="#c13515" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
SRC=[('s1',18,6,-3,'Review sites','<span class="v7-stars">★★★★★</span><b>4.9 · 612 reviews</b><span class="v7-q">"Great experience!!"</span>','Says it is good. Not why.'),
     ('s2',8,132,2,'Google listing','<b>Open Mondays 9 to 6</b><span class="v7-x">'+X+' Actually closed now</span>','Wrong hours'),
     ('s3',30,256,-2,'Instagram','<b>@lumenaesthetics</b><span class="v7-q">"New Morpheus8 promo! Link in bio"</span>','Buried in a feed'),
     ('s4',6,380,2,'Old directory','<b>(949) 555-0100</b><span class="v7-x">'+X+' Old number</span>','Out of date'),
     ('s5',40,500,-1,'Your neighbor','<span class="v7-q">"Ask for Dr. Nair. She will not overdo it."</span>','Only in her head')]
cards=''.join(f'<div class="v7-src" style="left: {x}px; top: {y}px; transform: rotate({r}deg);"><span class="v7-sl">{lab}</span>{body}<span class="v7-cap">{cap}</span></div>' for _,x,y,r,lab,body,cap in SRC)
lines=''.join(f'<path d="M292 {y+54} C 360 {y+54}, 380 300, 440 300" fill="none" stroke="#b9b0a0" stroke-width="2" stroke-dasharray="5 5"/>' for _,x,y,r,lab,body,cap in SRC)
REC7='''<div class="v7-rec"><span class="v7-sl" style="color: #237233;">One record</span><b style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 28px; font-weight: 500;">Lumen Aesthetics</b>
<div class="v7-f"><span>Mondays</span><b>Closed <i class="mk v"></i></b></div><div class="v7-f"><span>Phone</span><b>(949) 555-0148 <i class="mk c"></i></b></div><div class="v7-f"><span>Known for</span><b>Natural lip filler <i class="mk c"></i></b></div><div class="v7-f"><span>Ask for</span><b>Dr. Nair <i class="mk v"></i></b></div>
<span class="v7-ai"><span class="v4-aiav" style="width: 22px; height: 22px; font-size: 9px;">AI</span>Read by ChatGPT, Gemini and Claude</span></div>'''
STAGE=f'<div class="v7-stage"><svg class="v7-lines" viewBox="0 0 760 620" width="760" height="620" aria-hidden="true">{lines}<path d="M430 300l10 0" stroke="#b9b0a0" stroke-width="2"/></svg>{cards}{REC7}</div>'
HERO=f'''<div class="v4-hero" style="grid-template-columns: 460px minmax(0,1fr); align-items: center;"><div class="v4-l"><h1 style="font-size: 72px; line-height: 70px;">Stars don&#39;t say what&#39;s good. <em>Locals do.</em></h1><p class="v4-sub">The real answers are scattered. We put them in one place, and AI reads it.</p>{search}<div class="v4-try"><span>Try</span><a href="ExploreSearch.dc.html">Natural lip filler?</a><a href="Explore.dc.html">Tacos open late?</a><a href="Explore.dc.html">Honest Tesla mechanic?</a></div><div class="v4-proof"><b>4,812</b> neighbors · <b>1,904</b> answers this month · <b>12,400</b> places</div></div>{STAGE}</div>'''
a=BODY.index('<div class="v4-hero">'); e=BODY.index('<div class="v4-sec">')
FEEDSEC=f'<div class="v4-sec" style="align-items: start; border-top: 1px solid #e4ded2;"><div class="v4-h"><span class="v7-live"><i></i>Live near you</span><h2>See it <em>working</em>.</h2><p>Real questions, answered by people who went.</p></div><div class="v4-feed"><div class="v4-fh"><b style="font-size: 16px;">Irvine ▾</b><span class="v7-loc">Based on your location</span><span class="v4-tabs"><span class="on">Hot</span><span>New</span><span>Needs an answer</span></span></div>{feed}<a href="Explore.dc.html" class="v4-all">See all conversations near you ⟶</a></div></div>'
BODY=BODY[:a]+HERO+FEEDSEC+BODY[e:]
CSS7=CSS+'''
.v7-stage{position:relative;height:620px}
.v7-lines{position:absolute;left:0;top:0}
.v7-src{position:absolute;width:280px;box-sizing:border-box;padding:10px 16px;border-radius:12px;background:#ffffff;border:1px solid #e4ded2;box-shadow:0 10px 26px rgba(19,32,58,0.08);display:flex;flex-direction:column;gap:3px;font-size:14px;line-height:19px;color:#13203a;opacity:0.94}
.v7-sl{font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#8a93a3}
.v7-stars{color:#e8b400;letter-spacing:2px}
.v7-q{color:#3d4658}
.v7-x{display:flex;align-items:center;gap:6px;font-size:12px;font-weight:700;color:#c13515}
.v7-cap{margin-top:2px;font-size:12px;font-weight:700;color:#a8452c}
.v7-rec{position:absolute;left:446px;top:150px;width:310px;box-sizing:border-box;padding:20px 22px;border-radius:16px;background:#ffffff;border:2px solid #13203a;box-shadow:0 30px 70px rgba(19,32,58,0.18);display:flex;flex-direction:column;gap:6px;color:#13203a}
.v7-f{display:flex;justify-content:space-between;gap:10px;padding:8px 0;border-top:1px solid #f0ebe1;font-size:14px;color:#5b6474}.v7-f b{color:#13203a}
.v7-ai{display:flex;align-items:center;gap:8px;margin-top:8px;padding:8px 10px;border-radius:10px;background:#13203a;color:#ffffff;font-size:12px;font-weight:700}
.v7-live{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#e5482d}.v7-live i{width:10px;height:10px;border-radius:50%;background:#e5482d;box-shadow:0 0 0 4px rgba(229,72,45,0.18)}
.v7-loc{font-size:12px;color:#8a93a3}
'''
s=s[:he]+BODY+s[ph:]
for m_ in ['/*v3*/','/*hv*/','/*v4*/']:
    if m_ in s:
        a=s.index(m_); e=s.index('</style>',a); s=s[:a]+s[e:]
j=s.rfind('</style>',0,s.index('</helmet>')); s=s[:j]+CSS7+s[j:]
open(P+'Home.dc.html','w').write(s); print('ok',len(s))
