import sys; sys.path.insert(0,'/tmp/gen'); from common import *
SERIF='family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap'
CSS=HNL_CSS+'.wrap,header{flex-shrink:0}\n'+r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.uav{width:38px;height:38px;border-radius:50%;background:#e8e2d6;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;margin-left:6px}
.wrap{display:grid;grid-template-columns:340px 1fr;gap:40px;padding:40px;align-items:start}
.side{display:flex;flex-direction:column;gap:16px;padding:28px;border:1px solid #e6e6e6;border-radius:20px;position:sticky;top:20px}
.big{width:96px;height:96px;border-radius:50%;background:#e8e2d6;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700}
.badge{display:inline-flex;align-items:center;height:24px;padding:0 10px;border-radius:12px;background:#13203a;color:#ffffff;font-size:12px;font-weight:700;align-self:flex-start}
.st{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.st div{display:flex;flex-direction:column;gap:2px;padding:12px;border-radius:12px;background:#f7f7f5}
.st b{font-size:22px}
.st span{font-size:12px;color:#6a6a6a}
.tabs{display:flex;gap:4px;border-bottom:1px solid #ebebeb}
.tabs span{height:46px;padding:0 14px;display:inline-flex;align-items:center;font-size:15px;font-weight:600;color:#717171;border-bottom:2px solid transparent;margin-bottom:-1px;cursor:pointer}
.tabs span.on{color:#222222;border-bottom-color:#222222}
.ai{display:flex;flex-direction:column;gap:10px;padding:22px 24px;border-radius:18px;background:#13203a;color:#ffffff}
.ai .r{display:flex;gap:12px;padding:10px 0;border-top:1px solid rgba(255,255,255,0.12);font-size:14px;line-height:20px}
.ai .r:first-of-type{border-top:none}
.po{display:flex;flex-direction:column;gap:6px;padding:16px 0;border-top:1px solid #efefef}
.po .cz{font-size:12px;color:#6a6a6a}
.po strong{font-size:16px;line-height:22px}
.po p{margin:0;font-size:14px;line-height:21px;color:#484848}
.po .ft{display:flex;gap:16px;font-size:12px;font-weight:600;color:#6a6a6a}
.kind{display:inline-flex;align-items:center;height:18px;padding:0 7px;border-radius:9px;font-size:10px;font-weight:700;margin-right:4px}
.k-a{background:#eef2fb;color:#2d4a8a}.k-t{background:#e8f4ea;color:#1c5f2a}.k-h{background:#fff1e0;color:#9a5200}
.fol{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.fc{display:flex;flex-direction:column;gap:6px;padding:16px;border:1px solid #e6e6e6;border-radius:14px;text-decoration:none;color:#222222}
.ok{display:inline-flex;align-items:center;gap:5px;font-size:12px;font-weight:700;color:#1c5f2a}
'''
R='<a href="ExploreMe.dc.html" class="hnl">Explore</a><a href="Business.dc.html" class="hnl">For business</a><span style="font-size: 16px; padding: 0 8px;">🔔</span><a href="Me.dc.html" class="uav" style="text-decoration: none; color: #222222;">MK</a>'
BODY=header(R)+'''<div class="wrap"><div class="side"><span class="big">MK</span><span style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 24px;">Maria K.</strong><span class="mu" style="font-size: 14px;">Woodbridge, Irvine · joined March 2026</span></span><span class="badge">Local expert · Food</span><span style="font-size: 14px; line-height: 21px; color: #484848;">Mom of two, eats out way too much, will tell you where the kids can run around.</span>
<div class="st"><div><b>212</b><span>answers</span></div><div><b>38</b><span>tips confirmed</span></div><div><b>12</b><span>heads-ups</span></div><div><b>4,100</b><span>people helped</span></div></div>
<span class="btn b-sm">Edit profile</span><span class="mu" style="font-size: 12px;">Your name shows on posts. Your email and phone never do.</span></div>
<div style="display: flex; flex-direction: column; gap: 22px;"><div class="ai"><span style="font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #aab4c8;">Now what AI says</span><strong style="font-size: 20px;">3 of your tips are what ChatGPT tells people.</strong><div class="r"><span class="ok" style="color: #7fdc8a;">●</span><span>Backyard Tacos has a fenced lawn next to the patio, and you can see the kids from every table.</span></div><div class="r"><span class="ok" style="color: #7fdc8a;">●</span><span>Great Park Pilates keeps its $25 intro class to 6 people.</span></div><div class="r"><span class="ok" style="color: #7fdc8a;">●</span><span>Sol Cocina's bottomless brunch is $22 with any entree.</span></div></div>
<div class="tabs"><span class="on">Posts and answers</span><span>Places you follow</span><span>Saved</span></div>
<div><div class="po"><span class="cz"><span class="kind k-a">Answer</span><b style="color: #222222;">Food</b> · Backyard Tacos · 2 hours ago · ▲ 64</span><strong>Where can I take my kids to eat where they can also run around?</strong><p>Backyard Tacos has a fenced lawn right next to the patio. You can see the kids from every table.</p><span class="ft"><span class="ok">● Confirmed by 3 neighbors and the owner</span><span>11 answers</span><a href="ExploreMe.dc.html" style="color: #6a6a6a;">See thread</a></span></div>
<div class="po"><span class="cz"><span class="kind k-t">Tip</span><b style="color: #222222;">Fitness</b> · Great Park Pilates · 5 days ago · ▲ 18</span><strong>Great for total beginners</strong><p>The intro class is $25 and they keep it to 6 people.</p><span class="ft"><span class="ok">● Now what AI says</span><span>5 answers</span></span></div>
<div class="po"><span class="cz"><span class="kind k-h">Heads-up</span><b style="color: #222222;">Food</b> · Kinjiro Ramen · 1 week ago · ▲ 9</span><strong>Kitchen closes at 11 on weeknights now</strong><p>Asked the host. Weekends are still until 12:45.</p><span class="ft"><span style="color: #9a5200;">○ Waiting for a second neighbor</span><span>2 answers</span></span></div></div>
<h2 style="margin: 8px 0 0; font-size: 20px;">Places you follow</h2><div class="fol"><a href="Main.dc.html" class="fc"><strong>Backyard Tacos</strong><span class="mu" style="font-size: 13px;">Patio is heated now · 1 hour ago</span></a><a href="Main.dc.html" class="fc"><strong>Lumen Aesthetics</strong><span class="mu" style="font-size: 13px;">Heads-up: closed Oct 3 · 3 hours ago</span></a><a href="Main.dc.html" class="fc"><strong>Blue Door Coffee</strong><span class="mu" style="font-size: 13px;">Your Wi-Fi tip confirmed · Yesterday</span></a></div></div></div>'''
out=page('Maria K. on Local AI Registry',CSS,BODY,'    return {};').replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap',SERIF)
open(P+'Me.dc.html','w').write(out); print('ok', out.count('\u2014'))
