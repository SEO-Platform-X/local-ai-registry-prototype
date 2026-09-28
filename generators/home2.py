import sys; sys.path.insert(0,'/tmp/gen'); from common import *; from community import *
TRI="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22'%3E%3Cpath d='M11 3.5L19.5 18.5H2.5Z' fill='none' stroke='%238a8a8a' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E\") center / 100% 100% no-repeat"
HEADX=HEAD.replace('family=Figtree:wght@400;500;600;700;800&amp;display=swap','family=Figtree:wght@400;500;600;700;800&amp;family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&amp;display=swap')
CSSH=r'''body{background:#f3f0ea}
.srf{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em;color:#13203a}
.srf em{font-style:italic;color:#ff5a3c}
.tgl{display:inline-flex;padding:4px;border-radius:24px;background:#ffffff;border:1px solid #e3ddd2}
.tgl span{height:34px;padding:0 18px;border-radius:18px;display:inline-flex;align-items:center;font-size:11px;font-weight:700;letter-spacing:0.12em;color:#5a6378;cursor:pointer}
.tgl span.on{background:#13203a;color:#ffffff}
.ul{display:flex;align-items:center;gap:14px;width:560px;height:52px;border-bottom:1px solid #9aa0ad}
.ul input{flex-grow:1;border:none;background:transparent;outline:none;font-family:inherit;font-size:17px;color:#13203a}
.ul a{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:20px;color:#2d55e6;text-decoration:none;white-space:nowrap}
.nl{font-size:14px;color:#3d4659;text-decoration:none;font-weight:500}
.mk{position:relative;display:inline-block;width:12px;height:12px;margin:0 8px 1px 0;vertical-align:middle;flex-shrink:0}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.7px solid #e8740c;border-radius:50%}
.mk-ai::after{inset:0;background:'''+TRI+'''}
.life{display:grid;grid-template-columns:1fr 40px 1fr 40px 1fr;align-items:stretch}
.stg{display:flex;flex-direction:column;gap:10px;padding:22px;border-radius:16px;background:#ffffff;border:1px solid #e6e1d8;animation:glow 9s infinite}
.stg:nth-of-type(3){animation-delay:3s}.stg:nth-of-type(5){animation-delay:6s}
@keyframes glow{0%,30%{box-shadow:0 0 0 2px #13203a,0 12px 30px rgba(19,32,58,0.12)}34%,100%{box-shadow:0 0 0 0 transparent}}
.arw{display:flex;align-items:center;justify-content:center;font-size:22px;color:#b3aa9a}
.big{font-family:"Cormorant Garamond",Georgia,serif;font-size:120px;line-height:100px;font-weight:500;color:#13203a}
.stp3{display:flex;flex-direction:column;gap:8px;padding:24px;border-radius:16px;background:#ffffff;border:1px solid #e6e1d8}
.stp3 .n{font-family:"Cormorant Garamond",Georgia,serif;font-size:40px;line-height:40px;color:#ff5a3c;font-style:italic}
'''+CSS
LOGO2='<svg width="22" height="20" viewBox="0 0 22 20" aria-hidden="true"><path d="M11 1L21 19H1Z" fill="#2d55e6"></path><path d="M11 8L15.5 16H6.5Z" fill="#f3f0ea"></path></svg>'
MK=lambda c:f'<span class="mk mk-{c}"></span>'
BODY=f'''<header style="height: 72px; padding: 0 64px; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; gap: 24px;">
<a href="Home.dc.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: #13203a; font-weight: 600; font-size: 16px;">{LOGO2}Local AI Registry</a>
<label style="display: flex; align-items: center; gap: 8px; width: 260px; height: 36px; border-bottom: 1px solid #9aa0ad; color: #7a8193; font-size: 14px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#5a6378" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-4-4"></path></svg>Search the registry</label>
<div style="display: flex; align-items: center; gap: 22px; justify-content: flex-end;"><a href="Explore.dc.html" class="nl">Explore</a><a href="Flow.dc.html" class="nl">About</a><a href="#" class="nl">Sign in</a><a href="Claim.dc.html" class="btn b-sm" style="border-color: #13203a; color: #13203a; background: transparent; border-radius: 20px;">Claim your business</a></div>
</header>
<div style="padding: 24px 120px 0; display: flex; flex-direction: column; align-items: center; gap: 44px;">
<span class="tgl"><span class="{{{{bOn}}}}" onClick="{{{{pickB}}}}">FOR BUSINESS</span><span class="{{{{pOn}}}}" onClick="{{{{pickP}}}}">FOR PEOPLE</span></span>
<sc-if value="{{{{isBiz}}}}" hint-placeholder-val="{{{{ true }}}}"><div style="display: flex; flex-direction: column; align-items: center; gap: 26px; padding: 30px 0 20px;"><h1 class="srf" style="margin: 0; font-size: 92px; line-height: 92px; text-align: center; max-width: 1080px;">Your neighbors are telling AI who to <em>recommend</em>.</h1><p style="margin: 0; font-size: 19px; line-height: 30px; color: #4a5367; text-align: center; max-width: 600px;">Make sure it's you. Reviews, questions and fixes from your community feed ChatGPT, Gemini and Perplexity. Look up your business and see what they're saying.</p><div class="ul"><input type="text" placeholder="Enter your business name" aria-label="Business name"><a href="Main.dc.html">Look it up →</a></div></div></sc-if>
<sc-if value="{{{{isPpl}}}}" hint-placeholder-val="{{{{ false }}}}"><div style="display: flex; flex-direction: column; align-items: center; gap: 26px; padding: 30px 0 20px;"><h1 class="srf" style="margin: 0; font-size: 88px; line-height: 88px; text-align: center; max-width: 1100px;">Ask AI about a business in your town. Then help it get the answer <em>right</em>.</h1><p style="margin: 0; font-size: 19px; line-height: 30px; color: #4a5367; text-align: center; max-width: 600px;">Every local business has a page here, built from what neighbors know. Look one up, add what you know, and AI listens.</p><div class="ul"><input type="text" placeholder="Search a business, or ask a question" aria-label="Search"><a href="Explore.dc.html">Look it up →</a></div></div></sc-if>
</div>
<div style="padding: 70px 120px 0; display: flex; flex-direction: column; gap: 22px;">
<div style="display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center;"><span style="font-size: 12px; font-weight: 700; letter-spacing: 0.12em; color: #7a8193;">HOW A FACT GETS RIGHT</span><h2 class="srf" style="margin: 0; font-size: 52px; line-height: 56px;">AI guesses. Neighbors <em>know</em>.</h2></div>
<div class="life">
<div class="stg"><span style="display: flex; align-items: center; font-size: 12px; font-weight: 700; letter-spacing: 0.08em; color: #8a8a8a;">{MK('ai')}WHAT AI SAYS</span><span class="srf" style="font-size: 30px; line-height: 34px;">"Lumen is open Mondays, 10 to 6."</span><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">ChatGPT got it from a Yelp listing nobody has touched since 2021.</span></div>
<span class="arw">→</span>
<div class="stg"><span style="display: flex; align-items: center; font-size: 12px; font-weight: 700; letter-spacing: 0.08em; color: #b86a00;">{MK('vis')}A NEIGHBOR ADDS</span><span class="srf" style="font-size: 30px; line-height: 34px;">"I called on a Monday. Door was locked."</span><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">Tom H., Woodbridge. Dated, and he says how he knows.</span></div>
<span class="arw">→</span>
<div class="stg"><span style="display: flex; align-items: center; font-size: 12px; font-weight: 700; letter-spacing: 0.08em; color: #237233;">{MK('site')}CONFIRMED</span><span class="srf" style="font-size: 30px; line-height: 34px;">"Closed Mondays."</span><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">Two more neighbors and the owner agreed. AI now repeats the fix.</span></div>
</div>
</div>
<div style="padding: 80px 120px 0;"><div style="display: grid; grid-template-columns: auto 1fr; gap: 48px; align-items: center; padding: 44px 48px; border-radius: 20px; background: #13203a; color: #ffffff;"><span class="big" style="color: #ffffff;">312</span><div style="display: flex; flex-direction: column; gap: 14px;"><span class="srf" style="font-size: 38px; line-height: 42px; color: #ffffff;">things Irvine neighbors fixed that AI got wrong, <em>this week</em>.</span><span style="display: flex; gap: 36px; font-size: 14px; color: #c3c9d6;"><span><strong style="color: #ffffff; font-size: 18px;">1,904</strong> questions answered</span><span><strong style="color: #ffffff; font-size: 18px;">12,400</strong> businesses</span><span><strong style="color: #ffffff; font-size: 18px;">41</strong> cities in Orange County</span></span></div></div></div>
<sc-if value="{{{{isBiz}}}}" hint-placeholder-val="{{{{ true }}}}">
<div style="padding: 80px 120px 0; display: flex; flex-direction: column; gap: 20px;"><div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 24px;"><h2 class="srf" style="margin: 0; font-size: 46px; line-height: 50px; max-width: 760px;">Neighbors fixed 41 things about Irvine med spas this month. Is <em>yours</em> right?</h2><a href="Explore.dc.html" class="nl" style="white-space: nowrap;">See every fix →</a></div><div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px;"><sc-for list="{{{{fixesBiz}}}}" as="x" hint-placeholder-count="3">{FIX_CARD}</sc-for></div></div>
<div style="padding: 80px 120px 0; display: flex; flex-direction: column; gap: 20px;"><h2 class="srf" style="margin: 0; font-size: 46px; line-height: 50px; text-align: center;">Your page is already <em>here</em>.</h2><div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px;">
<div class="stp3"><span class="n">1</span><strong style="font-size: 18px;">Claim it, free</strong><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">Two minutes. We match you to the phone on your Google listing.</span></div>
<div class="stp3"><span class="n">2</span><strong style="font-size: 18px;">Confirm what neighbors and AI say</strong><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">Walk the facts, answer the questions waiting for you, fix what is wrong.</span></div>
<div class="stp3"><span class="n">3</span><strong style="font-size: 18px;">Help AI catch up</strong><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">AI keeps repeating old listings until the web agrees with you. We can push your record out everywhere it reads.</span></div>
</div><div style="display: flex; justify-content: center; padding-top: 8px;"><div class="ul"><input type="text" placeholder="Enter your business name" aria-label="Business name"><a href="Main.dc.html">Look it up →</a></div></div></div>
</sc-if>
<sc-if value="{{{{isPpl}}}}" hint-placeholder-val="{{{{ false }}}}">
<div style="padding: 80px 120px 0; display: flex; flex-direction: column; gap: 20px;"><div style="display: flex; align-items: flex-end; justify-content: space-between;"><h2 class="srf" style="margin: 0; font-size: 46px; line-height: 50px;">Fixed by <em>neighbors</em></h2><a href="Explore.dc.html" class="nl">See every fix near you →</a></div><div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px;"><sc-for list="{{{{fixes}}}}" as="x" hint-placeholder-count="6">{FIX_CARD}</sc-for></div></div>
<div style="padding: 80px 120px 0; display: grid; grid-template-columns: 1.4fr 1fr; gap: 32px; align-items: start;"><div style="display: flex; flex-direction: column; gap: 12px;"><h2 class="srf" style="margin: 0 0 6px; font-size: 40px; line-height: 44px;">Questions waiting for <em>you</em></h2><sc-for list="{{{{openQs}}}}" as="x" hint-placeholder-count="4">{OQ}</sc-for></div><div style="display: flex; flex-direction: column; gap: 12px;"><h2 class="srf" style="margin: 0 0 6px; font-size: 40px; line-height: 44px;">Local <em>experts</em></h2><sc-for list="{{{{experts}}}}" as="x" hint-placeholder-count="4">{EX}</sc-for></div></div>
<div style="padding: 80px 120px 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px;">
<div class="stp3"><span class="n">1</span><strong style="font-size: 18px;">Look it up</strong><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">See what AI says about any business in town, and what is actually confirmed.</span></div>
<div class="stp3"><span class="n">2</span><strong style="font-size: 18px;">Add what you know</strong><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">Hours, parking, who treated you, what it cost. Say how you know, and it is dated.</span></div>
<div class="stp3"><span class="n">3</span><strong style="font-size: 18px;">AI listens</strong><span style="font-size: 14px; line-height: 21px; color: #5a5a5a;">Once a second neighbor or the owner agrees, it is confirmed, and AI starts repeating it.</span></div>
</div>
</sc-if>
<footer style="margin-top: 90px; padding: 32px 64px; border-top: 1px solid #e0d9cc; display: flex; justify-content: space-between; font-size: 13px; color: #6a7183;"><span>Local AI Registry · Irvine, CA</span><span style="display: flex; gap: 20px;"><a href="Explore.dc.html" class="nl" style="font-size: 13px;">Explore</a><a href="#" class="nl" style="font-size: 13px;">How records are built</a><a href="#" class="nl" style="font-size: 13px;">For developers</a><a href="Claim.dc.html" class="nl" style="font-size: 13px;">For businesses</a></span></footer>'''
JS=FIXES_JS+r'''    const aud = (this.state && this.state.aud) || 'biz';
    const isBiz = aud === 'biz';
    const fixesBiz = fixes.filter(f => ['Lumen Aesthetics', 'Spectrum Aesthetics MD', 'Coastline MedSpa'].includes(f.b));
    return { isBiz, isPpl: !isBiz, bOn: isBiz ? 'on' : '', pOn: isBiz ? '' : 'on', pickB: () => this.setState({ aud: 'biz' }), pickP: () => this.setState({ aud: 'ppl' }), fixes, fixesBiz, openQs, experts };'''
t=HEADX.replace('<title>Lumen Aesthetics on Local AI Registry</title>','<title>Local AI Registry</title>')
out=t+'\n'+CSSH+'\n</style>\n</helmet>\n<div style="width: 1440px; box-sizing: border-box; display: flex; flex-direction: column; background: #f3f0ea; position: relative;">\n'+BODY+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+JS+'\n  }\n}\n</script>\n</body>\n</html>\n'
open(P+'Home.dc.html','w').write(out); print('ok')
