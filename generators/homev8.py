import re,sys
sys.path.insert(0,'/tmp/gen')
exec(open("/tmp/gen/homev7.py").read().rsplit("s=s[:he]+BODY+s[ph:]",1)[0])
OWN=BODY[BODY.index('<div class="v4-own">'):].replace('<p>See what locals and AI say. Free.</p>','<p>See what locals and AI say. Free.</p><p style="font-size: 17px; line-height: 26px;">We keep your record complete, answer locals&#39; questions and fix what AI gets wrong.</p><div class="v13-trust"><span><i>✓</i>Public record</span><span><i>✓</i>Sourced facts</span><span><i>✓</i>No pay-to-rank</span></div>',1)
CHATSEC=f'<div class="v4-sec v4-dark"><div class="v4-h"><h2 style="color: #ffffff;">Then AI <em>repeats it</em>.</h2><p style="color: #c9d0dc;">ChatGPT, Gemini and Claude read the record.</p></div>{CHAT}</div>'
# ---------- Docs-style hero visual
def ln(w,extra=''): return f'<span class="v8-ln" style="width: {w}%;{extra}"></span>'
def hl(w,col,name,left=0,strike=False):
    return f'<span class="v8-hlw" style="margin-left: {left}%;"><span class="v8-flag" style="background: {col};">{name}</span><span class="v8-hl" style="width: {w}px; background: {col}33; border-bottom: 2px solid {col};{" text-decoration: line-through;" if strike else ""}"></span></span>'
PINK='#d6457a';ORG='#e8740c';GRN='#237233';BLU='#2b59d9';NAV='#13203a';GRY='#8a93a3'
SV='fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
IC_={'store':'<path d="M4 10h16v10H4z"/><path d="M3 10l2-6h14l2 6"/><path d="M10 20v-5h4v5"/>','chat':'<path d="M4 5h16v11H9l-5 4z"/>','cam':'<rect x="3" y="7" width="18" height="13" rx="3"/><circle cx="12" cy="13.5" r="3.5"/><path d="M8 7l2-3h4l2 3"/>','seal':'<path d="M6 3h9l4 4v14H6z"/><circle cx="12" cy="13" r="3"/><path d="M10.5 16l-1 4 2.5-1.5 2.5 1.5-1-4"/>','check':'<path d="M5 12l5 5 9-10"/>','clock':'<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>','pin':'<path d="M12 21s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>','phone':'<path d="M5 4h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>','tag':'<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>','star':'<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" fill="currentColor"/>','user':'<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>','shield':'<path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z"/>'}
def I_(k,s=16): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" {SV} aria-hidden="true">{IC_[k]}</svg>'
PINK='#d6457a';ORG='#e8740c';GRN='#1f9d55';NAV='#13203a';BLU='#2b59d9';PUR='#7c4dff';TEAL='#0e9aa7'
def row(icon,lw,vw,col=None,src=None):
    if col:
        v=f'<span class="v10-hw"><span class="v10-flag" style="background: {col};">{I_(src,12)}</span><span class="v10-hl" style="width: {vw}px; background: {col}2e; border-bottom: 2px solid {col};"></span></span>'
    else:
        v=f'<span class="v10-g" style="width: {vw}px;"></span>'
    return f'<div class="v10-fr"><span class="v10-ic">{I_(icon,15)}</span><span class="v10-g" style="width: {lw}px;"></span><span style="flex: 1;"></span>{v}</div>'
def msg(col,w1,w2):
    return f'<div class="v10-msg" style="border-left-color: {col};"><span class="v10-av" style="background: {col};">{I_("user",12)}</span><span style="display: flex; flex-direction: column; gap: 6px; flex: 1;"><span class="v10-g" style="width: {w1}%;"></span><span class="v10-g" style="width: {w2}%;"></span></span><span class="v10-src" style="color: {col};">{I_("chat",13)}</span></div>'
def HLt(w,col,src,inline=False):
    return f'<span class="v11-hw"><span class="v10-flag" style="background: {col};">{I_(src,12)}</span><span class="v11-hl" style="width: {w}px; background: {col}2e; border-bottom: 2px solid {col};"></span></span>'
def G(w): return f'<span class="v10-g" style="width: {w}px;"></span>'
def line(*parts): return '<div class="v11-line">'+''.join(parts)+'</div>'
def chat(col,x,y,w1,w2):
    return f'<div class="v11-fl" style="left: {x}px; top: {y}px; border-left: 4px solid {col};"><span class="v10-av" style="background: {col};">{I_("user",12)}</span><span style="display: flex; flex-direction: column; gap: 6px; flex: 1;"><span class="v10-g" style="width: {w1}%;"></span><span class="v10-g" style="width: {w2}%;"></span></span><span style="color: {col}; display: flex;">{I_("chat",15)}</span></div>'
PROFILE=f"""<div class="v11-card">
<div class="v11-gal"><span></span><span class="hl" style="border-color: {TEAL};"><i class="v10-flag" style="background: {TEAL}; left: 6px; top: 6px;">{I_("cam",12)}</i></span><span></span><span></span><span></span></div>
<div class="v11-body">
<div class="v11-title"><b>Main Street Med Spa</b><span class="v10-stars">{"".join(I_("star",14) for _ in range(5))}<span class="v10-g" style="width: 46px; margin-left: 6px;"></span></span></div>
<div class="v10-tabs"><span class="on"></span><span></span><span></span><span></span></div>
<div class="v11-para">{line(G(150),HLt(120,PINK,"chat"),G(90))}{line(G(330))}{line(G(60),G(120),HLt(96,PUR,"seal"))}{line(G(210))}</div>
<div class="v11-chips"><span></span><span></span><span class="hl" style="border-color: {GRN}; background: {GRN}1f;"><i class="v10-flag" style="background: {GRN}; left: -8px; top: -10px;">{I_("chat",11)}</i></span><span></span></div>
<div class="v11-rows"><div class="v10-fr"><span class="v10-ic">{I_("clock",15)}</span>{G(60)}<span style="width: 40px;"></span>{HLt(88,ORG,"chat")}<span style="flex: 1;"></span></div><div class="v10-fr"><span class="v10-ic">{I_("pin",15)}</span>{G(70)}<span style="flex: 1;"></span>{HLt(110,NAV,"check")}</div></div>
</div></div>"""
FLOATS=(chat(PINK,-50,340,90,60)+chat(ORG,540,300,80,50)+chat(GRN,-40,500,70,55)
 +f'<div class="v11-fl" style="left: 520px; top: 30px;"><span class="v10-pimg"></span><span style="display: flex; flex-direction: column; gap: 6px; flex: 1;"><span class="v10-g" style="width: 80%;"></span><span class="v10-g" style="width: 50%;"></span></span><span class="v10-badge" style="background: {TEAL};">{I_("cam",13)}</span></div>'
 +f'<div class="v11-fl" style="left: 200px; top: 600px; border-left: 4px solid {NAV};"><span class="v10-av" style="background: {NAV};">{I_("store",13)}</span><span style="display: flex; flex-direction: column; gap: 6px; flex: 1;"><span class="v10-g" style="width: 70%;"></span><span class="v10-g" style="width: 45%;"></span></span><span class="v10-badge" style="background: #1f9d55;">{I_("check",13)}</span></div>'
 +f'<div class="v11-fl" style="left: 480px; top: 610px;"><span class="v10-doc">{I_("seal",18)}</span><span style="display: flex; flex-direction: column; gap: 6px; flex: 1;"><span class="v10-g" style="width: 70%;"></span><span class="v10-g" style="width: 40%;"></span></span><span class="v10-badge" style="background: {PUR};">{I_("seal",13)}</span></div>')
DOC=f'<div class="v11-stage">{PROFILE}{FLOATS}</div>'
HERO=f'''<div class="v8-hero"><div class="v8-l"><h1>What locals know,<br><em class="v12-em">AI recommends</em>.</h1><p class="v4-sub">Reviews can be bought. Your neighbors can&#39;t. Their tips become the public record AI reads, pointing people to the places that earn it.</p>{search}<a href="Business.dc.html" class="v13-own"><span class="v13-shop">{I_('shield',14)}</span>Own a business? <b>See if AI recommends you. Free</b> ⟶</a><div class="v4-proof"><b>4,812</b> neighbors · <b>1,904</b> edits this month · <b>12,400</b> places</div></div>{DOC}</div>'''


# ---------- trending grid of well-known brands with the comment trending on each
_bsrc=open('/tmp/gen/brands.py').read(); exec(_bsrc[_bsrc.index("S='fill"):_bsrc.index('def card')])
BD={x[1]:x for x in B}
TR=[("Equinox","Is the 6 AM spin class OK for beginners?","irvine_runner",38,14),("In-N-Out","Best time to skip the drive-thru line?","night_owl_uci",52,21),("Trader Joe's","Which location has the best flower selection?","woodbridge_mom",44,17),("Lululemon","Do they still hem pants here?","spectrum_regular",29,9),
    ("Patagonia","Anyone tried the Worn Wear trade-in here?","trail_dad_92",21,6),("IKEA","Is weekday morning pickup faster?","new_in_tustin",33,12),("SoulCycle","Which instructor is best for a first ride?","aisha_m",27,11),("Sephora","Can you book a makeover before a wedding?","bride_2026",41,15)]
LOC=[("Irvine Spectrum","Irvine"),("Tustin Market Place","Tustin"),("Woodbridge Village","Irvine"),("The District","Tustin"),("Fashion Island","Newport Beach"),("South Coast Plaza","Costa Mesa"),("University Center","Irvine"),("Culver Plaza","Irvine"),("Westpark","Irvine"),("Heritage Plaza","Irvine"),("Quail Hill","Irvine"),("Orchard Hills","Irvine"),("Diamond Jamboree","Irvine"),("Walnut Village","Irvine"),("Crystal Cove","Newport Beach"),("The Camp","Costa Mesa"),("Old Town","Tustin"),("Great Park","Irvine"),("Northwood","Irvine"),("Turtle Rock","Irvine"),("Park Place","Irvine")]
_li=[0]
def tc(n,q,u,v,a,w):
    slug,nm,cat,k,col=BD[n]
    loc,city=LOC[_li[0]%len(LOC)]; _li[0]+=1
    pin='<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M12 21s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>'
    return f'<a href="ExploreSearch.dc.html" class="v10-bc v12-bc" style="width: {w}px;" data-logo="logos/{slug}.svg"><span class="v12-left"><span class="v11-logo"><span class="v11-bn">{nm}</span></span><span class="v12-spot"><span class="v12-img" data-photo="locations/{slug}.jpg"></span><span class="v12-addr"><span class="v12-pin">{pin}</span><span style="display: flex; flex-direction: column; min-width: 0;"><b>{loc}</b><span>{city}, CA</span></span></span></span></span><span class="v10-br"><span class="v10-vote"><span class="up">▲</span><b>{v}</b><span class="dn">▼</span></span><span style="display: flex; flex-direction: column; gap: 6px; flex: 1; min-width: 0;"><span class="v10-q">"{q}"</span><span class="v10-u"><b>{u}</b> · {a} answers</span></span></span></a>'
EXTRA=[("Costco","Which gas station has the shortest line?","costco_dad",36,13),("Warby Parker","Is the free eye exam worth booking?","four_eyes_oc",19,7),("Chick-fil-A","Does the drive-thru move faster at lunch?","uci_junior",47,22),("Aesop","Can you refill bottles here?","green_irvine",15,5),("Barry's","Which class is best for a first timer?","fit_in_irvine",23,8),("REI","Worth joining the co-op for rentals?","hike_socal",31,10),
       ("Lush","Do they do free hand demos here?","bath_bomb_bea",18,6),("Supreme","What time does the drop line start?","hype_kid",42,19),("Kith","Is the treats counter worth the wait?","sneaker_sam",26,9),("Brandy Melville","Does this location restock on weekdays?","teen_mom_oc",14,4),("Alo Yoga","Are the in-store classes free?","flow_with_jo",22,8),("Harley-Davidson","Can you test ride without booking?","route66_rick",17,5),("Chrome Hearts","Do they resize rings in store?","silver_lining",20,6)]
ALL=TR+EXTRA
W=[[430,380,460,400,440,390,420],[400,450,380,470,410,440,390],[450,400,430,380,460,410,440]]
rows=[''.join(tc(*x,W[r][i%7]) for i,x in enumerate(ALL[r::3])) for r in range(3)]
GRID=f'''<div class="v10-sea"><div class="v8-th" style="padding: 0 64px; margin-bottom: 48px;"><span class="v7-live"><i></i>Trending right now</span><h2>Stars say it&#39;s good.<br>Locals say <em class="v12-em">what&#39;s good</em>.</h2></div><div class="v10-track" style="margin-left: -60px;">{rows[0]}{rows[0]}</div><div class="v10-track" style="margin-left: -260px;">{rows[1]}{rows[1]}</div><div class="v10-track" style="margin-left: -150px;">{rows[2]}{rows[2]}</div><a href="Explore.dc.html" class="v4-all">See all 12,400 places ⟶</a></div>'''
HOW=f'''<div class="v4-sec" style="grid-template-columns: 400px minmax(0,1fr);"><div class="v4-h"><span class="v4-lb">How it works</span><h2>We gather it. <em>All in one place.</em></h2><p>Reviews, listings, social posts, and what locals know.</p></div>{STAGE}</div>'''
BODY=f'''<div id="v4Body">{HERO}{GRID}{HOW}{CHATSEC}{OWN}'''
CSS8=CSS7+'''
.v8-hero{display:grid;grid-template-columns:540px minmax(0,1fr);gap:56px;align-items:center;padding:48px 64px 64px}
.v8-l{display:flex;flex-direction:column;gap:20px}
.v8-l h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:54px;line-height:58px;letter-spacing:-0.02em;color:#13203a;white-space:nowrap}.v8-l h1 em{color:#e5482d}
.v8-hero .sbox{width:100% !important;max-width:100% !important;box-sizing:border-box}
.v8-doc{position:relative;border-radius:18px;background:#ffffff;border:1px solid #e4ded2;box-shadow:0 30px 80px rgba(19,32,58,0.14);padding:0 0 26px}
.v8-top{display:flex;align-items:center;gap:12px;padding:16px 20px 10px}
.v8-logo{width:30px;height:30px;border-radius:8px;background:#13203a;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px}
.v8-tt{display:flex;flex-direction:column;line-height:17px;flex:1}.v8-tt b{font-size:15px;color:#13203a}.v8-tt span{font-size:12px;color:#8a93a3}
.v8-avs{display:flex}.v8-avs i{width:28px;height:28px;border-radius:50%;border:2px solid #fff;margin-left:-8px;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:11px;font-weight:700;color:#fff}
.v8-share{height:32px;padding:0 14px;border-radius:16px;background:#dfe8f5;color:#1e4fb8;font-size:13px;font-weight:700;display:inline-flex;align-items:center}
.v8-tool{display:flex;gap:10px;margin:0 20px;padding:10px 14px;border-radius:12px;background:#f1f3f6}.v8-tool span{height:8px;border-radius:4px;background:#d8dde6}
.v8-page{margin:16px 20px 0 20px;padding:26px 30px;border-radius:12px;background:#fbfbfc;border:1px solid #eef0f3;display:flex;flex-direction:column;gap:18px;width:62%;box-sizing:border-box}
.v8-row{display:flex;align-items:flex-end;gap:8px;height:12px}
.v8-ln{display:block;height:10px;border-radius:5px;background:#e3e6ec}
.v8-hlw{position:relative;display:inline-flex}
.v8-flag{position:absolute;left:0;bottom:16px;height:20px;padding:0 7px;border-radius:4px 4px 4px 0;color:#fff;font-size:11px;font-weight:700;display:inline-flex;align-items:center;white-space:nowrap}
.v8-hl{display:block;height:14px;border-radius:2px}
.v8-tbl{display:flex;flex-direction:column;gap:8px;padding:10px 12px;border-radius:8px;border:1px solid #eef0f3;margin-top:4px}
.v8-tr{display:flex;align-items:center;gap:10px}.v8-td{display:block;height:8px;border-radius:4px;background:#e3e6ec}.v8-dot{width:9px;height:9px;border-radius:50%}
.v8-cmt{position:absolute;right:20px;top:118px;width:230px;padding:14px;border-radius:14px;background:#eef3fc;display:flex;gap:10px;font-size:13px;line-height:18px;color:#13203a;box-shadow:0 10px 26px rgba(19,32,58,0.10)}
.v8-cmt.c2{top:258px;background:#eef6ef}
.v8-cmt b{font-size:13px}.v8-cm{font-size:11px;font-weight:700;color:#8a93a3}
.v8-cav{width:28px;height:28px;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;flex-shrink:0}
.v9{padding:0 !important;overflow:hidden}
.v9-gal{display:grid;grid-template-columns:2fr 1fr 1fr;gap:4px;height:120px}.v9-gal span{display:block}
.v9-main{display:grid;grid-template-columns:minmax(0,1fr) 250px;gap:22px;padding:18px 22px 22px}
.v9-l{display:flex;flex-direction:column;gap:4px}
.v9-title{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px}.v9-title b{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:30px;line-height:32px;color:#13203a}
.v9-tabs{display:flex;gap:18px;border-bottom:1px solid #eceff3;margin-bottom:6px}.v9-tabs span{padding:8px 0;font-size:12px;font-weight:700;color:#a0a7b3}.v9-tabs span.on{color:#13203a;border-bottom:2px solid #13203a}
.v9-fr{display:grid;grid-template-columns:96px 1fr;align-items:center;height:44px;border-bottom:1px solid #f1f3f6}
.v9-k{font-size:13px;color:#8a93a3}
.v9-v{display:flex;align-items:center;justify-content:flex-end;gap:8px}
.v9-mk{width:8px;height:8px;border-radius:50%}
.v9-r{display:flex;flex-direction:column;gap:12px}
.v9-book{display:flex;flex-direction:column;gap:8px;padding:14px;border-radius:12px;border:1px solid #eceff3;background:#fbfbfc}
.v9-bx{display:block;height:26px;border-radius:6px;background:#f1f3f6;border:1px solid #e6e9ee}
.v9-btn{display:block;height:30px;border-radius:15px;background:#13203a}
.v9c{position:static !important;width:auto !important;box-shadow:none !important}
.v10{position:relative;border-radius:18px;background:#ffffff;border:1px solid #e4ded2;box-shadow:0 30px 80px rgba(19,32,58,0.14);overflow:hidden}
.v10-gal{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:62px 62px;gap:4px}.v10-gal span{background:#e6e9ee;display:block}.v10-gal span:first-child{grid-row:span 2}
.v10-main{display:grid;grid-template-columns:minmax(0,1fr) 250px;gap:22px;padding:18px 22px 22px}
.v10-l{display:flex;flex-direction:column}
.v10-title{display:flex;flex-direction:column;gap:6px;margin-bottom:12px}.v10-title b{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:32px;line-height:34px;color:#13203a}
.v10-stars{display:flex;align-items:center;gap:2px;color:#c9ced8}
.v10-g{display:block;height:9px;border-radius:5px;background:#e3e6ec}
.v10-tabs{display:flex;gap:14px;border-bottom:1px solid #eceff3;padding-bottom:10px;margin-bottom:4px}.v10-tabs span{display:block;width:52px;height:9px;border-radius:5px;background:#e3e6ec}.v10-tabs span.on{background:#9aa2b1}
.v10-fr{display:flex;align-items:center;gap:10px;height:44px;border-bottom:1px solid #f1f3f6}
.v10-ic{color:#b4bac5;display:flex}
.v10-hw{position:relative;display:inline-flex}
.v10-flag{position:absolute;left:-10px;top:-12px;width:22px;height:22px;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2px #fff}
.v10-hl{display:block;height:14px;border-radius:2px}
.v10-map{margin-top:14px;height:74px;border-radius:10px;background:#eef0f3;display:flex;align-items:center;justify-content:center;color:#b4bac5}
.v10-r{display:flex;flex-direction:column;gap:12px}
.v10-book{display:flex;flex-direction:column;gap:8px;padding:14px;border-radius:12px;border:1px solid #eceff3;background:#fbfbfc}
.v10-bx{display:block;height:26px;border-radius:6px;background:#f1f3f6;border:1px solid #e6e9ee}.v10-btn{display:block;height:30px;border-radius:15px;background:#c9ced8}
.v10-chat{display:flex;flex-direction:column;gap:8px}
.v10-msg{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:12px;background:#f6f7f9;border-left:3px solid}
.v10-av{width:24px;height:24px;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.v10-src{display:flex}
.v10-ext{display:flex;flex-direction:column;gap:8px}
.v10-post{position:relative;display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:12px;border:1px solid #eceff3;background:#ffffff}
.v10-pimg{width:34px;height:34px;border-radius:8px;background:#e6e9ee;flex-shrink:0}
.v10-doc{width:34px;height:34px;border-radius:8px;background:#f1f3f6;color:#b4bac5;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.v10-badge{width:24px;height:24px;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.v11-stage{position:relative;height:690px}
.v13-tog{display:inline-flex;align-self:flex-start;padding:4px;border-radius:24px;background:#ffffff;border:1px solid #e4ded2}.v13-tog span{height:36px;padding:0 16px;border-radius:18px;display:inline-flex;align-items:center;font-size:14px;font-weight:700;color:#5b6474;cursor:pointer}.v13-tog span.on{background:#13203a;color:#ffffff}
.v13-look svg{color:#8a93a3;flex-shrink:0}
.v13-own{display:inline-flex;align-items:center;gap:8px;align-self:flex-start;height:40px;padding:0 16px 0 6px;border-radius:20px;background:#ffffff;border:1px solid #e4ded2;font-size:14px;color:#3d4658 !important;text-decoration:none !important}.v13-own b{color:#13203a}
.v13-shop{width:28px;height:28px;border-radius:50%;background:#13203a;color:#ffffff;display:flex;align-items:center;justify-content:center}
.v13-trust{display:flex;gap:18px;flex-wrap:wrap;font-size:14px;font-weight:700;color:#13203a}.v13-trust span{display:inline-flex;align-items:center;gap:6px}.v13-trust i{font-style:normal;color:#237233}
.v11-card{position:absolute;left:50px;top:70px;width:560px;border-radius:18px;background:#ffffff;border:1px solid #e4ded2;box-shadow:0 30px 80px rgba(19,32,58,0.14);overflow:visible}
.v11-gal{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:60px 60px;gap:4px;border-radius:18px 18px 0 0;overflow:hidden}.v11-gal span{background:#e6e9ee;display:block;position:relative;box-sizing:border-box}.v11-gal span:first-child{grid-row:span 2}
.v11-gal span.hl{border:3px solid;background:#e0f2f3}
.v11-gal .v10-flag{position:absolute}
.v11-body{padding:18px 24px 22px;display:flex;flex-direction:column;gap:12px}
.v11-title{display:flex;flex-direction:column;gap:6px}.v11-title b{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:32px;line-height:34px;color:#13203a}
.v11-para{display:flex;flex-direction:column;gap:12px;padding:4px 0 2px}
.v11-line{display:flex;align-items:center;gap:8px;height:12px}
.v11-hw{position:relative;display:inline-flex}.v11-hw .v10-flag{left:-10px;top:-14px}
.v11-hl{display:block;height:14px;border-radius:2px}
.v11-chips{display:flex;gap:8px;padding-top:4px}.v11-chips span{position:relative;display:block;width:78px;height:26px;border-radius:13px;background:#f1f3f6;border:2px solid transparent;box-sizing:border-box}.v11-chips .v10-flag{position:absolute}
.v11-rows{display:flex;flex-direction:column}
.v11-fl{position:absolute;width:220px;box-sizing:border-box;display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:14px;background:#ffffff;border:1px solid #e4ded2;box-shadow:0 16px 36px rgba(19,32,58,0.14);z-index:3}
.v10-sea{padding:130px 0 110px;border-top:1px solid #e4ded2;background:#fbf8f3;overflow:hidden}
.v10-track{display:flex;gap:22px;width:max-content;margin-bottom:22px}
.v10-bc{display:grid;grid-template-columns:1fr 1fr;height:170px;border-radius:16px;overflow:hidden;background:#ffffff;border:1px solid #e4ded2;text-decoration:none !important;color:#13203a;font-weight:400;flex-shrink:0}
.v12-em{font-style:normal !important;font-weight:700;color:#e5482d}
.v12-bc{height:220px !important}
.v12-left{display:flex;flex-direction:column;border-right:1px solid #f0ebe1;min-width:0}
.v12-left .v11-logo{flex:1;border-right:none !important;padding:16px !important}
.v12-spot{display:flex;flex-direction:column;border-top:1px solid #f0ebe1}
.v12-img{display:block;height:58px;background:linear-gradient(135deg,#e9e4da,#dcd5c7)}
.v12-addr{display:flex;align-items:center;gap:6px;padding:7px 10px;font-size:11px;line-height:14px;color:#8a93a3}
.v12-addr b{font-size:12px;color:#13203a;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.v12-pin{color:#e5482d;display:flex;flex-shrink:0}
.v11-logo{display:flex;align-items:center;justify-content:center;padding:28px;background:#ffffff;border-right:1px solid #f0ebe1}
.v11-bn{font-family:"Cormorant Garamond",Georgia,serif;font-size:28px;line-height:30px;font-weight:500;color:#13203a;text-align:center}
.v10-bl{display:flex;flex-direction:column;justify-content:space-between;padding:18px}
.v10-bi{display:flex}
.v10-bn{font-family:"Cormorant Garamond",Georgia,serif;font-size:30px;line-height:31px;font-weight:500;color:#13203a}
.v10-br{display:flex;gap:12px;padding:18px 16px}
.v10-vote{display:flex;flex-direction:column;align-items:center;gap:2px;font-size:12px;color:#b4bac5}.v10-vote .up{color:#e5482d}.v10-vote b{font-size:14px;color:#13203a}
.v10-q{font-size:15px;line-height:21px;font-weight:700;color:#13203a}
.v10-u{margin-top:auto;font-size:12px;color:#8a93a3;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.v10-u b{color:#3d4658}
.v8-trend{padding:90px 64px 70px;border-top:1px solid #e4ded2;background:#fbf8f3}
.v8-th{display:flex;flex-direction:column;gap:10px;margin-bottom:30px}
.v8-th h2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:60px;line-height:60px;color:#13203a}.v8-th h2 em{color:#e5482d}
.v8-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.v8-tc{display:flex;flex-direction:column;gap:12px;padding:24px;border-radius:16px;background:#ffffff;border:1px solid #e4ded2;text-decoration:none !important;color:#13203a;font-weight:400}
.v8-tl{width:84px;height:84px;border-radius:22px;display:flex;align-items:center;justify-content:center}
.v8-tn{font-family:"Cormorant Garamond",Georgia,serif;font-size:34px;line-height:36px;font-weight:500}
.v8-tq{font-size:16px;line-height:23px;font-weight:600;color:#13203a;flex:1}
.v8-tm{font-size:12px;color:#8a93a3}.v8-tm b{color:#3d4658}
'''
JS='class Component extends DCLogic {\n  renderVals() {\n    const q = (this.state && this.state.q !== undefined) ? this.state.q : \'\';\n    return { q, hasQ: q.length > 0, onQ: (e) => this.setState({ q: e.target.value }) };\n  }\n}'
s=s[:he]+BODY+s[ph:]
for m_ in ['/*v3*/','/*hv*/','/*v4*/']:
    if m_ in s:
        a=s.index(m_); e=s.index('</style>',a); s=s[:a]+s[e:]
j=s.rfind('</style>',0,s.index('</helmet>')); s=s[:j]+CSS8+s[j:]
s=re.sub(r'class Component extends DCLogic \{.*?\n\}', lambda m: JS, s, count=1, flags=re.S)
open(P+'Home.dc.html','w').write(s); print('ok',len(s))
open('/tmp/gen/v8parts.py','w').write('TR='+repr(TR)+'\n')
