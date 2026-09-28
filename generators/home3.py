import sys; sys.path.insert(0,'/tmp/gen'); from common import *
SERIF='family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap'
CSS=HNL_CSS+'.hero,.vsx,.two,.nums,.tr,.ft,header{flex-shrink:0}\n'+r'''.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.nl{font-size:14px;font-weight:600;color:#222222;text-decoration:none}
.hero{padding:90px 120px 70px;display:flex;flex-direction:column;align-items:center;gap:22px;text-align:center;background:#f3f0ea}
.sbox{display:flex;align-items:center;gap:12px;width:760px;height:66px;padding:0 8px 0 24px;border-radius:33px;background:#ffffff;box-shadow:0 8px 30px rgba(19,32,58,0.12);box-sizing:border-box}
.sbox input{flex-grow:1;border:none;outline:none;font-family:inherit;font-size:17px;background:transparent;color:#222222}
.sug{width:760px;border-radius:18px;background:#ffffff;box-shadow:0 8px 30px rgba(19,32,58,0.10);text-align:left;overflow:hidden}
.sug .h{padding:12px 20px 4px;font-size:11px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8a8a8a}
.sug a{display:flex;align-items:center;gap:14px;padding:10px 20px;text-decoration:none;color:#222222}
.sug a:hover{background:#f7f7f7}
.sug .ic{width:36px;height:36px;border-radius:10px;background:#f1ece3;display:flex;align-items:center;justify-content:center;font-size:16px}
.chips{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.chip{display:inline-flex;align-items:center;height:34px;padding:0 14px;border-radius:17px;border:1px solid #d9d2c4;background:rgba(255,255,255,0.6);font-size:13px;font-weight:600;color:#13203a;text-decoration:none}
.vsx{padding:72px 120px 24px;display:flex;flex-direction:column;gap:32px}
.eyb2{font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:#a8452c}
.vsg{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.vc{display:flex;flex-direction:column;gap:10px;padding:28px;border-radius:20px;border:1px solid #e6e6e6;background:#ffffff}
.vc.us{border:2px solid #13203a;box-shadow:0 12px 34px rgba(19,32,58,0.12)}
.vh{font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8a8a8a}
.vq{margin-top:auto;padding:12px 14px;border-radius:12px;background:#f5f5f5;font-size:14px;font-weight:600;color:#6a6a6a}
.kf{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:12px;font-weight:700;color:#6a6a6a;text-transform:uppercase;letter-spacing:0.06em}
.kf b{text-transform:none;letter-spacing:0;font-size:14px;color:#13203a;background:#f3f0ea;padding:5px 12px;border-radius:14px}
.lt{display:flex;gap:10px;align-items:baseline;font-size:15px;line-height:22px;padding:8px 0;border-top:1px solid #f0f0f0}
.lt i{font-style:normal;color:#ff5a3c;font-weight:800;width:12px}
.lt em{font-style:normal;font-size:12px;color:#8a8a8a;margin-left:auto;white-space:nowrap;padding-left:10px}
.name{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid #e6e0d4;border-bottom:1px solid #e6e0d4}
.name div{display:flex;flex-direction:column;gap:6px;padding:22px 24px;border-left:1px solid #e6e0d4}
.name div:first-child{border-left:none}
.name b{font-family:"Cormorant Garamond",Georgia,serif;font-size:40px;line-height:40px;font-weight:600;color:#13203a}
.name span{font-size:14px;line-height:21px;color:#484848}
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px;padding:56px 120px 24px}
.pc{display:flex;flex-direction:column;gap:12px;padding:32px;border-radius:20px;text-decoration:none;color:#222222}
.pc h3{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-size:36px;line-height:38px;font-weight:600;color:#13203a}
.pc p{margin:0;font-size:15px;line-height:23px;color:#484848}
.nums{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:32px 120px;border-radius:20px;background:#13203a;color:#ffffff;overflow:hidden}
.nums div{padding:26px 28px;display:flex;flex-direction:column;gap:4px;border-left:1px solid rgba(255,255,255,0.1)}
.nums div:first-child{border-left:none}
.nums b{font-family:"Cormorant Garamond",Georgia,serif;font-size:44px;line-height:44px;font-weight:600}
.nums span{font-size:13px;color:#c3c9d6}
.tr{padding:24px 120px 72px;display:flex;flex-direction:column;gap:16px}
.tg{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.tc{display:flex;flex-direction:column;gap:8px;padding:20px;border:1px solid #e6e6e6;border-radius:16px;text-decoration:none;color:#222222}
.tc .cz{font-size:12px;color:#6a6a6a}
.tc strong{font-size:16px;line-height:22px}
.tc p{margin:0;font-size:14px;line-height:20px;color:#484848}
.ft{padding:28px 120px;border-top:1px solid #ebebeb;display:flex;justify-content:space-between;font-size:13px;color:#6a6a6a}
'''
BODY=header(PUB_R)+'''
<div class="hero"><span style="font-size: 13px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #8a7a5c;">The public record of local businesses</span>
<h1 class="srf" style="margin: 0; font-size: 76px; line-height: 76px; max-width: 980px;">What locals <em>actually</em> know.</h1>
<span style="font-size: 18px; line-height: 27px; color: #484848; max-width: 700px;">What a place is really known for, the tips only regulars know, and heads-ups when something changes. From neighbors who have been there, not ads or star ratings.</span>
<label class="sbox"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg><input type="text" value="{{q}}" placeholder="Search a business name or a city" aria-label="Search a business or city" onChange="{{onQ}}"><a href="ExploreLumen.dc.html" class="btn b-coral" style="border-radius: 26px; height: 50px; padding: 0 26px;">Search</a></label>
<sc-if value="{{hasQ}}" hint-placeholder-val="{{ true }}"><div class="sug"><span class="h" style="display: block;">Businesses</span><a href="ExploreLumen.dc.html"><span class="ic">✦</span><span style="display: flex; flex-direction: column;"><strong>Lumen Aesthetics</strong><span class="mu" style="font-size: 13px;">Med spa · Irvine Spectrum, Irvine</span></span></a><a href="ExploreLumen.dc.html"><span class="ic">✦</span><span style="display: flex; flex-direction: column;"><strong>Lumen Eye Care</strong><span class="mu" style="font-size: 13px;">Eye doctor · Costa Mesa</span></span></a><span class="h" style="display: block;">Cities</span><a href="Explore.dc.html"><span class="ic">⌖</span><span style="display: flex; flex-direction: column;"><strong>Irvine, CA</strong><span class="mu" style="font-size: 13px;">4,812 neighbors · 1,904 conversations</span></span></a></div></sc-if>
<span class="chips"><span class="mu" style="font-size: 13px; align-self: center;">Try</span><a href="Explore.dc.html" class="chip">Irvine, CA</a><a href="Explore.dc.html" class="chip">Costa Mesa</a><a href="Explore.dc.html" class="chip">Newport Beach</a><a href="ExploreLumen.dc.html" class="chip">Lumen Aesthetics</a></span></div>
<div class="vsx"><div style="display: flex; flex-direction: column; gap: 10px; align-items: center; text-align: center;"><span class="eyb2">Why not just Google or Yelp?</span><h2 class="srf" style="margin: 0; font-size: 52px; line-height: 54px; max-width: 900px;">Stars tell you it's good. <em>Locals tell you what it's good for.</em></h2></div>
<div class="vsg"><div class="vc"><span class="vh">Google and Yelp</span><strong style="font-size: 20px;">Lumen Aesthetics</strong><span style="font-size: 15px;">★ 4.9 · 612 reviews · Med spa</span><span class="mu" style="font-size: 14px; line-height: 21px;">Open 9 AM to 6 PM. 612 reviews to read through, most saying "great experience."</span><span class="vq">So... is it the right place for your first lip filler?</span></div>
<div class="vc us"><span class="vh" style="color: #a8452c;">Local AI Registry</span><strong style="font-size: 20px;">Lumen Aesthetics</strong><span class="kf"><span>Known for</span><b>Natural lip filler</b><b>Morpheus8</b></span><span class="lt"><i>✦</i>Dr. Nair talks you out of overdoing it. <em>31 locals</em></span><span class="lt"><i>✦</i>Park on level 3 of Structure B. <em>Tip, 4 locals</em></span><span class="lt"><i>!</i>Closed Saturday, Oct 3. <em>Heads-up, confirmed by Lumen</em></span><span class="lt"><i>✦</i>Tuesday mornings are nearly empty. <em>Measured</em></span></div></div>
<div class="name"><div><b>Local</b><span>From the people who actually went, not marketing copy.</span></div><div><b>AI</b><span>The facts that hold up become what ChatGPT and Google repeat.</span></div><div><b>Registry</b><span>A public record. Every fact shows who said it and when.</span></div></div></div>
<div class="two"><a href="Explore.dc.html" class="pc" style="background: #eef0ea;"><span style="font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #5c6b57;">For everyone</span><h3>Find out from people who went.</h3><p>Browse what your city is talking about on a map. Ask a question, share a tip, or give a heads-up when something changes.</p><span class="btn b-sm b-dark" style="align-self: flex-start; margin-top: 6px;">Explore Irvine</span></a>
<a href="Business.dc.html" class="pc" style="background: #fdece6;"><span style="font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #a8452c;">For business owners</span><h3>See what AI says about you. Free.</h3><p>Your page is already live. Claim it, fix what is wrong, answer your neighbors, and get the right facts into ChatGPT, Gemini and Claude.</p><span class="btn b-sm b-coral" style="align-self: flex-start; margin-top: 6px;">Look up your business</span></a></div>
<div class="nums"><div><b>4,812</b><span>neighbors in Irvine</span></div><div><b>1,904</b><span>questions answered</span></div><div><b>12,400</b><span>businesses on the record</span></div><div><b>41</b><span>cities</span></div></div>
<div class="tr"><div style="display: flex; justify-content: space-between; align-items: baseline;"><h2 class="srf" style="margin: 0; font-size: 36px;">Trending in <em>Irvine</em></h2><a href="Explore.dc.html" style="font-size: 14px; font-weight: 600;">See the map</a></div>
<div class="tg"><a href="Explore.dc.html" class="tc"><span class="cz"><b style="color: #222222;">Food</b> · Backyard Tacos · 11 answers</span><strong>Where can I take my kids to eat where they can also run around?</strong><p>Maria K.: fenced lawn right next to the patio, you can see the kids from every table.</p></a><a href="Explore.dc.html" class="tc"><span class="cz"><b style="color: #222222;">Beauty</b> · Lumen Aesthetics · 23 answers</span><strong>First time getting lip filler. Who will not overdo it?</strong><p>Aisha M.: Dr. Nair talked me down to half a syringe.</p></a><a href="Explore.dc.html" class="tc"><span class="cz"><b style="color: #222222;">Car</b> · Irvine Auto Care · 6 answers</span><strong>Who actually knows Teslas and will not upsell me?</strong><p>Jordan P.: they told me my brakes had another 15,000 miles.</p></a></div></div>
<div class="ft"><span>Local AI Registry · Irvine, California</span><span><a href="Business.dc.html" style="color: #6a6a6a;">For business</a> · <a href="Flow.dc.html" style="color: #6a6a6a;">About</a> · Privacy · Terms</span></div>'''
JS='''    const q = (this.state && this.state.q !== undefined) ? this.state.q : 'Lumen';
    return { q, hasQ: q.length > 0, onQ: (e) => this.setState({ q: e.target.value }) };'''
out=page('Local AI Registry: what locals actually know',CSS,BODY,JS)
out=out.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap',SERIF)
open(P+'Home.dc.html','w').write(out); print('ok', out.count('\u2014'))
