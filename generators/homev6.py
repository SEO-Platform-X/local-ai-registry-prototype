import re,sys
sys.path.insert(0,'/tmp/gen')
exec(open('/tmp/gen/homev4.py').read().split("s=s[:he]+BODY+s[ph:]")[0])
def cur(x,y,col,name,msg,flip=False,owner=False,act=''):
    arrow=f'<svg width="22" height="24" viewBox="0 0 22 24" aria-hidden="true"><path d="M2 2l17 8-7 2.5L9 21z" fill="{col}" stroke="#ffffff" stroke-width="1.6" stroke-linejoin="round"/></svg>'
    tag=f'<span class="v6-tag" style="background: {col};">{name}{" · owner" if owner else ""}</span>'
    bub=f'<span class="v6-bub" style="border-color: {col};"><span class="v6-act" style="color: {col};">{act}</span>{msg}</span>'
    return f'<div class="v6-cur{" fl" if flip else ""}" style="left: {x}px; top: {y}px;">{arrow}<div class="v6-cb">{tag}{bub}</div></div>'
CARD='''<div class="v6-card"><div class="v6-img"></div><div class="v6-cbody"><b class="v6-name">Lumen Aesthetics</b><span class="v6-meta">Med spa · Irvine · ★ 4.9</span>
<div class="v6-f"><span>Known for</span><b>Natural lip filler <i class="mk c"></i></b></div><div class="v6-f hl"><span>Mondays</span><b>Closed <i class="mk v"></i> <em class="v6-new">Updated 2m ago</em></b></div><div class="v6-f"><span>Parking</span><b>Structure B, level 3 <i class="mk v"></i></b></div><div class="v6-f"><span>Consult</span><b>$75, credited <i class="mk c"></i></b></div></div></div>'''
CURS=''.join([cur(0,30,'#d6457a','aisha_m','Yes, Dr. Nair injects herself.',act='Answered a question'),
              cur(440,0,'#e8740c','turtle_rock_ren','Mondays: now closed',act='Suggested an edit'),
              cur(512,250,'#237233','maria_k','Parking validated in Structure B',act='Added a tip'),
              cur(10,470,'#13203a','Lumen','Consult: $75, credited',owner=True,act='Confirmed a fact'),
              cur(410,470,'#2b59d9','jordan_p','Do they take HSA cards?',act='Asked')])
STAGE=f'<div class="v6-stage">{CARD}{CURS}</div>'
BRS7=''.join(f'<span class="v4-br"><span class="v4-bi" style="color: {BD[n][4]}; background: {tint(BD[n][4])};">{ico(BD[n][3],20)}</span>{n}</span>' for n in BR[:6])
BRROW=f'<div class="v6-brow"><span class="v4-lb">Already on the registry</span>{BRS7}<span class="v4-br" style="background: #13203a; color: #ffffff; border-color: #13203a;">+ 12,400 more</span></div>'
BODY=BODY.replace(BODY[BODY.index('<div class="v4-feed">'):BODY.index('</div></div>',BODY.index('See all 1,904 conversations'))+12],STAGE+'</div>',1)
BODY=BODY.replace('<div class="v4-sec">',BRROW+'<div class="v4-sec">',1)
# add live feed section right after the hero
FEEDSEC=f'<div class="v4-sec" style="align-items: start;"><div class="v4-h"><span class="v6-live"><i></i>Live</span><h2>Right now in <em>Irvine</em>.</h2><p>Every answer adds to a page.</p></div><div class="v4-feed">{feed}<a href="Explore.dc.html" class="v4-all">See all 1,904 conversations ⟶</a></div></div>'
i=BODY.index('<div class="v4-sec">'); BODY=BODY[:i]+FEEDSEC+BODY[i:]
CSS6=CSS+'''
.v6-stage{position:relative;height:560px}
.v4-hero{padding:32px 64px 20px !important}
.v6-brow{display:flex;flex-wrap:nowrap;align-items:center;gap:8px;padding:16px 64px 26px}
.v6-brow .v4-lb{margin-right:8px}
.v6-brow .v4-br{height:46px;font-size:21px;padding:0 14px 0 5px;border-radius:23px;white-space:nowrap}.v6-brow .v4-bi{width:36px;height:36px}
.v6-card{position:absolute;left:120px;top:78px;width:380px;border-radius:18px;background:#ffffff;border:1px solid #e4ded2;box-shadow:0 30px 70px rgba(19,32,58,0.16);overflow:hidden}
.v6-img{height:120px;background:linear-gradient(135deg,#f0dcc4,#e8d2b5)}
.v6-cbody{padding:18px 22px 20px;display:flex;flex-direction:column;gap:6px}
.v6-name{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:32px;line-height:34px;color:#13203a}
.v6-meta{font-size:14px;color:#5b6474;margin-bottom:6px}
.v6-f{display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-top:1px solid #f0ebe1;font-size:15px;color:#5b6474}.v6-f b{color:#13203a}
.v6-cur{position:absolute;display:flex;align-items:flex-start;gap:0;z-index:2}
.v6-cb{display:flex;flex-direction:column;align-items:flex-start;gap:4px;margin-top:16px;margin-left:-2px}
.v6-tag{height:22px;padding:0 9px;border-radius:6px;color:#ffffff;font-size:12px;font-weight:700;display:inline-flex;align-items:center;white-space:nowrap}
.v6-act{display:block;font-size:10px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:2px}
.v6-f.hl{background:#fff4e6;margin:0 -10px;padding:10px}
.v6-new{font-style:normal;font-size:10px;font-weight:700;color:#b35a00;margin-left:6px}
.v6-bub{padding:8px 13px;border-radius:4px 14px 14px 14px;background:#ffffff;border:2px solid;font-size:14px;font-weight:600;color:#13203a;white-space:nowrap;box-shadow:0 8px 20px rgba(19,32,58,0.12)}
.v6-live{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#e5482d}.v6-live i{width:10px;height:10px;border-radius:50%;background:#e5482d;box-shadow:0 0 0 4px rgba(229,72,45,0.18)}
.mk.a{width:0;height:0;border-radius:0;border-left:5px solid transparent;border-right:5px solid transparent;border-bottom:9px solid #8a93a3;background:none}
'''
s=s[:he]+BODY+s[ph:]
for m_ in ['/*v3*/','/*hv*/','/*v4*/']:
    if m_ in s:
        a=s.index(m_); e=s.index('</style>',a); s=s[:a]+s[e:]
j=s.rfind('</style>',0,s.index('</helmet>')); s=s[:j]+CSS6+s[j:]
open(P+'Home.dc.html','w').write(s); print('ok',len(s))
