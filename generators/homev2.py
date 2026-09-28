import re,sys
sys.path.insert(0,'/tmp/gen')
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
_src=open('/tmp/gen/brands.py').read(); exec(_src[_src.index("S='fill"):_src.index('def card')])
exec(open('/tmp/gen/ill.py').read())
def tint(col,a=0.12):
    r,g,b=int(col[1:3],16),int(col[3:5],16),int(col[5:7],16); return f'rgb({round(r*a+255*(1-a))}, {round(g*a+255*(1-a))}, {round(b*a+255*(1-a))})'
BD={x[1]:x for x in B}
TOP=["Equinox","In-N-Out","Trader Joe's","Lululemon","Patagonia","IKEA","SoulCycle","Sephora"]
def tile(n):
    slug,nm,cat,k,col=BD[n]
    return f'<a href="ExploreSearch.dc.html" class="hv-t" data-logo="logos/{slug}.svg"><span class="hv-st" style="background: {col};"></span><span class="hv-ic" style="color: {col}; background: {tint(col)};">{ico(k,26)}</span><span class="hv-nm">{nm}</span><span class="hv-ct">{cat}</span></a>'
MOS='<div style="display: flex; flex-direction: column; gap: 12px;"><span style="font-size: 12px; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; color: #8a93a3;">Already on the registry</span><div class="hv-mos">'+''.join(tile(n) for n in TOP)+'<a href="ExploreSearch.dc.html" class="hv-t hv-more"><span class="hv-nm" style="color: #ffffff; font-size: 26px;">+ 12,400 more</span><span class="hv-ct" style="color: #c9d0dc;">Find yours ⟶</span></a></div></div>'
REST=[x[1] for x in B if x[1] not in TOP]
CSS='''/*hv*/
.hv{display:grid;grid-template-columns:minmax(0,1fr) 600px;gap:56px;align-items:center;padding:44px 64px 40px;box-sizing:border-box}
.hv .sbox{width:100% !important;max-width:100% !important;box-sizing:border-box}
.hv .chips{justify-content:flex-start !important}
.hv-l{display:flex;flex-direction:column;gap:18px}
.hv-l h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:70px;line-height:70px;letter-spacing:-0.015em;color:#13203a}
.hv-l h1 em{color:#e5482d}
.hv-proof{display:flex;align-items:center;gap:10px;font-size:14px;color:#3d4658}.hv-proof b{color:#13203a}
.hv-mos{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.hv-t{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:8px;height:176px;padding:20px 18px 16px;box-sizing:border-box;border-radius:14px;background:#ffffff;border:1px solid #e4ded2;text-decoration:none !important;color:#13203a}
.hv-st{position:absolute;top:0;left:0;right:0;height:5px}
.hv-ic{width:50px;height:50px;border-radius:14px;display:flex;align-items:center;justify-content:center}
.hv-nm{margin-top:auto;font-family:"Cormorant Garamond",Georgia,serif;font-size:30px;line-height:31px;white-space:nowrap}
.hv-ct{font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#8a93a3}
.hv-more{background:#13203a;border-color:#13203a;justify-content:flex-end}
.hv-band{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;row-gap:6px;gap:18px;padding:22px 64px;border-top:1px solid #e4ded2;border-bottom:1px solid #e4ded2;background:#fbf8f3;overflow:hidden}
.hv-band span.l{font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#8a93a3;white-space:nowrap}
.hv-band span.n{font-family:"Cormorant Garamond",Georgia,serif;font-size:24px;color:#13203a;white-space:nowrap}
.hv-band i{font-style:normal;color:#e5482d}
.hw{padding:110px 64px;display:flex;flex-direction:column;gap:40px}
.hw-h{display:flex;flex-direction:column;align-items:center;text-align:center;gap:12px}
.hw-h h2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:64px;line-height:66px;color:#13203a;max-width:1000px}.hw-h h2 em{color:#e5482d}
.hw-g{display:grid;grid-template-columns:1fr 48px 1fr 48px 1fr;align-items:stretch}
.hw-a{display:flex;align-items:center;justify-content:center;color:#b9b0a0;font-size:30px}
.hw-c{display:flex;flex-direction:column;gap:14px;padding:26px;border-radius:14px;background:#ffffff;border:1px solid #e4ded2}
.hw-n{font-family:"Cormorant Garamond",Georgia,serif;font-size:44px;line-height:44px;color:#e5482d}
.hw-c h3{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:32px;line-height:34px;color:#13203a}
.hw-c p{margin:0;font-size:15px;line-height:23px;color:#3d4658}
.hw-demo{margin-top:auto;border-radius:10px;background:#f3efe7;padding:14px 16px;display:flex;flex-direction:column;gap:8px;font-size:14px;line-height:20px}
.hw-fr{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid #e4ded2;padding-bottom:6px}.hw-fr:last-child{border-bottom:none;padding-bottom:0}
.hw-mk{display:inline-block;width:9px;height:9px;border-radius:50%;margin-left:6px}
.cmp{display:flex;flex-direction:column;align-self:stretch;width:100%;box-sizing:border-box;border:1px solid #e4ded2;border-radius:14px;overflow:hidden;background:#ffffff}
.cmp-r{display:grid !important;width:100%;grid-template-columns:220px minmax(0,1fr) minmax(0,1fr) minmax(0,1.3fr) !important;align-items:stretch;border-top:1px solid #ece6da}.cmp-r:first-child{border-top:none}
.cmp-r span{padding:16px 20px;font-size:15px;line-height:22px;color:#3d4658}
.cmp-r .k{font-weight:700;color:#13203a}
.cmp-r .us{background:#fbf4ea;color:#13203a;font-weight:600}
.cmp-h span{font-size:12px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#8a93a3}.cmp-h .us{color:#a8452c}
.hn-h{display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px;padding:90px 64px 0}
.hn-h h2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:64px;line-height:66px;color:#13203a}.hn-h h2 em{color:#e5482d}
'''
def hero(old_hero):
    # keep the existing search box, dropdown and chips from the old hero
    a=old_hero.index('<label class="sbox">'); e=old_hero.index('</a></span>',old_hero.index('<span class="chips">'))+11
    search=old_hero[a:e]
    return f'''<div class="hv" id="hvHero"><div class="hv-l"><span style="font-size: 13px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #8a7a5c;">Built by your neighbors</span><h1>Where locals tell AI <em>what is actually good</em>.</h1><span style="font-size: 19px; line-height: 29px; color: #3d4658; max-width: 620px;">Local AI Registry is the public record of every local business, written by the people who go there and confirmed by the owners. It is what ChatGPT, Gemini and Claude read before they recommend anyone.</span>{search}<span class="hv-proof"><b>4,812</b> neighbors in Irvine · <b>1,904</b> questions answered this month</span></div>{MOS}</div>
<div class="hv-band"><span class="l">Also on the registry</span>{"<i>·</i>".join(f'<span class="n">{n}</span>' for n in REST)}</div>'''
MK=lambda c: f'<span class="hw-mk" style="background: {c};"></span>' if c!='v' else '<span class="hw-mk" style="border: 1.5px solid #e8740c; box-sizing: border-box;"></span>'
HOW=f'''<div class="hw" id="hvHow"><div class="hw-h"><span class="eyb2">What the name means</span><h2>Local. AI. Registry. <em>Here is how it works.</em></h2><span style="font-size: 18px; line-height: 28px; color: #3d4658; max-width: 760px;">Your neighbors already know which places are good. We turn that into a public record, and that record is what AI reads.</span></div>
<div class="hw-g"><div class="hw-c"><span class="hw-n">Local</span><h3>Your neighbors share what is true</h3><p>Tips, questions and heads-ups from people who actually went. No account needed.</p><div class="hw-demo"><b>First time getting lip filler. Who will not overdo it?</b><span style="color: #3d4658;">aisha_m, went: "Dr. Nair talked me down to half a syringe."</span><span style="font-size: 12px; color: #8a93a3;">▲ 41 · 23 answers</span></div></div><span class="hw-a">⟶</span>
<div class="hw-c"><span class="hw-n">Registry</span><h3>It becomes the public record</h3><p>Owners confirm the facts. Every fact shows who said it and when. Nobody can pay to rank.</p><div class="hw-demo"><span class="hw-fr"><span>Mondays</span><b>Closed{MK("#237233")}</b></span><span class="hw-fr"><span>Consult</span><b>$75, credited{MK("#237233")}</b></span><span class="hw-fr"><span>Parking</span><b>Structure B, level 3{MK("v")}</b></span></div></div><span class="hw-a">⟶</span>
<div class="hw-c" style="background: #13203a; border-color: #13203a;"><span class="hw-n">AI</span><h3 style="color: #ffffff;">AI reads the record</h3><p style="color: #c9d0dc;">ChatGPT, Gemini and Claude use it to recommend the right place, for the right reason.</p><div class="hw-demo" style="background: #1f2d4a; color: #e6e9f0;"><span style="font-size: 12px; font-weight: 700; color: #aeb6c6;">ChatGPT</span><span>"For natural lip filler in Irvine, locals point to Lumen Aesthetics. Dr. Nair does every injection herself."</span><span style="font-size: 12px; color: #aeb6c6;">Source: localairegistry.com/lumen</span></div></div></div></div>'''
CMP='<div class="cmp"><div class="cmp-r cmp-h"><span></span><span>Yelp</span><span>Google Business Profile</span><span class="us">Local AI Registry</span></div>'+''.join(f'<div class="cmp-r"><span class="k">{k}</span><span>{a}</span><span>{b}</span><span class="us">{c}</span></div>' for k,a,b,c in [("Who writes it","Reviewers","The owner","Locals, confirmed by the owner"),("What you get","Stars and long reviews","Hours, photos, a listing","Answers to real questions, what it is known for, tips and heads-ups"),("Paid placement?","Yes, sponsored ads","Yes, sponsored ads","No. Nobody can pay to rank."),("Built for","People scrolling","Google Search","People and AI answers: ChatGPT, Gemini, Claude")])+'</div>'
NEED='<div class="hn-h" id="hvNeed"><span class="eyb2">For both sides of the counter</span><h2>Whichever side you are on, <em>this is for you</em>.</h2></div>'
s=open(P+'Home.dc.html').read()
he=s.index('</helmet>')
hs=s.index('<div class="hero"',he) if '<div class="hero"' in s else s.index('<div class="hv"',he)
# old hero end = start of next block
nxt=s.index('<div class="vsx">',hs)
old=s[hs:nxt]
if 'id="hvHero"' in old:  # rerun: recover search from current
    pass
s=s[:hs]+hero(old)+s[nxt:]
# remove big brand wall from vsx, add How it works before the comparison
if '<div class="brs">' in s:
    a=s.index('<div class="brs">'); e=s.index('</span></div>',s.index('class="note"',a))+len('</span></div>'); s=s[:a]+s[e:]
if 'id="hvHow"' in s:
    a=s.index('<div class="hw" id="hvHow">'); depth=0
    for m in re.finditer(r'<(/?)div\b[^>]*>',s[a:]):
        depth+= -1 if m.group(1) else 1
        if depth==0: e=a+m.end(); break
    s=s[:a]+s[e:]
s=s.replace('<div class="vsx">',HOW+'<div class="vsx">',1)
if 'id="hvNeed"' in s:
    a=s.index('<div class="hn-h" id="hvNeed">'); e=s.index('</h2></div>',a)+11; s=s[:a]+s[e:]
s=s.replace('<div class="two"',NEED+'<div class="two"',1)
if '<div class="name">' in s:
    a=s.index('<div class="name">'); depth=0
    for m in re.finditer(r'<(/?)div\b[^>]*>',s[a:]):
        depth+= -1 if m.group(1) else 1
        if depth==0: e=a+m.end(); break
    s=s[:a]+CMP+s[e:]
if '/*hv*/' in s:
    a=s.index('/*hv*/'); e=s.index('</style>',a); s=s[:a]+CSS+s[e:]
else:
    j=s.rfind('</style>',0,s.index('</helmet>')); s=s[:j]+CSS+s[j:]
s=s.replace("const q = (this.state && this.state.q !== undefined) ? this.state.q : 'Lumen';","const q = (this.state && this.state.q !== undefined) ? this.state.q : '';")
open(P+'Home.dc.html','w').write(s); print('ok')
