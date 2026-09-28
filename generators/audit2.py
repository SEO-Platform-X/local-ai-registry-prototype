import sys; sys.path.insert(0,'/tmp/gen'); from common import *
from headers import LOGO
exec(open('/tmp/gen/ill.py').read())
P2='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
CSS=r'''.at-top{height:64px;box-sizing:border-box;padding:0 32px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #e4ded2;background:#f3efe7}
.at{display:grid;grid-template-columns:440px 1fr;height:836px;overflow:hidden}
.at-l{background:#f5e3cc;border-right:1px solid #e6cfb2;padding:36px 40px 28px;display:flex;flex-direction:column;gap:18px;box-sizing:border-box;height:836px}
.at-l .big{font-family:"Cormorant Garamond",Georgia,serif;font-size:34px;line-height:38px;color:#13203a}
.at-l .big em{color:#e5482d}
.at-l p{margin:0;font-size:15px;line-height:23px;color:#3d4658}
.slots{display:grid;grid-template-columns:1fr 1fr;gap:8px}.slots span{height:42px;border-radius:6px;border:1px solid #13203a;background:#fbf4ea;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;color:#13203a;cursor:pointer}.slots span.on{background:#13203a;color:#fff}
.kbtn{height:52px;border-radius:9999px;background:#13203a;color:#fff;display:flex;align-items:center;justify-content:center;gap:10px;font-size:15px;font-weight:600;text-decoration:none}
.sup{padding-top:14px;border-top:1px solid #e6cfb2;font-size:14px;color:#3d4658}.sup a{color:#13203a;font-weight:600}
.at-r{display:flex;flex-direction:column;min-height:0}
.at-body{flex:1;overflow:hidden;padding:44px 72px 20px;box-sizing:border-box;display:flex;flex-direction:column;gap:18px}
.at-foot{height:92px;flex-shrink:0;box-sizing:border-box;border-top:1px solid #e4ded2;padding:0 72px;display:flex;align-items:center;justify-content:space-between;background:#f3efe7}
.dots{display:flex;gap:8px}.dots i{width:28px;height:4px;border-radius:2px;background:#dcd5c7;display:block}.dots i.on{background:#13203a}.dots i.done{background:#8a93a3}
.nx{display:inline-flex;align-items:center;justify-content:center;gap:12px;height:56px;min-width:240px;padding:0 30px;border-radius:9999px;background:#13203a;color:#fff;font-size:16px;font-weight:600;text-decoration:none;cursor:pointer}
.bk{font-size:15px;font-weight:600;color:#3d4658;cursor:pointer}
.ey{font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#5b6474}
.st{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:52px;line-height:56px;color:#13203a;max-width:820px}
.st em{color:#e5482d}
.lead{margin:0;font-size:17px;line-height:27px;color:#3d4658;max-width:720px}
.crd{background:#ffffff;border:1px solid #e4ded2;border-radius:8px;padding:20px 22px}
.row3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.kpi{display:flex;flex-direction:column;gap:4px}.kpi b{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:56px;line-height:58px}.kpi span{font-size:13px;color:#3d4658;line-height:19px}
.wr{display:grid;grid-template-columns:150px 1fr 1fr;gap:14px;align-items:center;padding:14px 0;border-top:1px solid #efeae0;font-size:15px}.wr:first-of-type{border-top:none}
.wr .no{color:#c13515;text-decoration:line-through}.wr .ok{color:#1c5f2a;font-weight:600}
.bar{height:34px;border-radius:4px;display:flex;align-items:center;padding:0 12px;color:#fff;font-size:13px;font-weight:700;box-sizing:border-box}
.pl3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.pc{display:flex;flex-direction:column;gap:8px;padding:20px;border-radius:8px;background:#fff;border:1px solid #e4ded2;text-decoration:none;color:#13203a}
.pc.hot{border:2px solid #13203a;background:#fbf4ea}
.pc b{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:30px}
.pc > span:last-child{font-weight:400}.pc{cursor:pointer}
.pc ul{margin:0;padding-left:18px;font-size:13px;line-height:20px;color:#3d4658}
.load{display:flex;flex-direction:column;gap:12px}.ln{display:flex;align-items:center;gap:12px;font-size:16px}.ln i{width:22px;height:22px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-style:normal;font-size:12px;font-weight:700}
.ln.d i{background:#237233;color:#fff}.ln.r i{border:2px solid #13203a}.ln.q{color:#8a93a3}.ln.q i{border:1.5px solid #c9c3b6}
'''
AI_SVG='''<svg viewBox="0 0 520 250" width="520" height="250" aria-hidden="true" font-family="Figtree,sans-serif"><g fill="none" stroke="#13203a" stroke-width="1.4"><circle cx="420" cy="125" r="46" fill="#13203a"/></g><text x="420" y="130" font-size="15" fill="#fff" text-anchor="middle" font-weight="700">AI</text>
<g font-size="12" fill="#13203a">'''+''.join(f'<rect x="20" y="{12+i*40}" width="150" height="30" rx="6" fill="{c}" stroke="{s}"/><text x="34" y="{32+i*40}">{t}</text><path d="M170 {27+i*40} C 280 {27+i*40}, 300 125, 374 125" fill="none" stroke="{s}" stroke-width="{w}" {d}/>' for i,(t,c,s,w,d) in enumerate([('Yelp: open Mondays','#fdecea','#c13515','1.4','stroke-dasharray="4 4"'),('Old website: 9 to 8','#fdecea','#c13515','1.4','stroke-dasharray="4 4"'),('Google: aestheticians','#fdecea','#c13515','1.4','stroke-dasharray="4 4"'),('Directory: old phone','#fdecea','#c13515','1.4','stroke-dasharray="4 4"'),('Your record: correct','#eaf5ec','#237233','3','')]))+'</g></svg>'
CHART='''<svg viewBox="0 0 620 190" width="100%" aria-hidden="true" font-family="Figtree,sans-serif"><g stroke="#efeae0">'''+''.join(f'<line x1="40" x2="560" y1="{y}" y2="{y}"/>' for y in [30,70,110,150])+'''</g><g font-size="10" fill="#8a93a3"><text x="10" y="34">90</text><text x="10" y="74">70</text><text x="10" y="114">50</text><text x="10" y="154">30</text></g>
<polyline points="50,122 110,114 170,108 230,100 290,94" fill="none" stroke="#2b59d9" stroke-width="2.5"/><polyline points="290,94 350,82 410,70 470,60 530,50" fill="none" stroke="#237233" stroke-width="2.5" stroke-dasharray="6 5"/><polyline points="290,94 350,88 410,80 470,72 530,66" fill="none" stroke="#2b59d9" stroke-width="2" stroke-dasharray="6 5"/><polyline points="290,94 350,92 410,88 470,84 530,84" fill="none" stroke="#8a93a3" stroke-width="1.6" stroke-dasharray="6 5" fill="none" stroke="#237233" stroke-width="2.5" stroke-dasharray="6 5"/><polyline points="290,94 350,93 410,92 470,91 530,90" fill="none" stroke="#c9c3b6" stroke-width="2" stroke-dasharray="3 4"/>
<circle cx="290" cy="94" r="5" fill="#13203a"/><text x="290" y="84" font-size="11" fill="#13203a" text-anchor="middle" font-weight="700">58 today</text><g font-size="11" text-anchor="start"><text x="536" y="53" fill="#237233" font-weight="700">80 Authority</text><text x="536" y="69" fill="#2b59d9" font-weight="700">72 Trust</text><text x="536" y="84" fill="#5b6474" font-weight="700">63 Fix</text><text x="536" y="98" fill="#8a93a3">60 no plan</text></g>
<g font-size="10" fill="#8a93a3"><text x="50" y="180">Jun</text><text x="170" y="180">Aug</text><text x="290" y="180">Oct</text><text x="410" y="180">Dec</text><text x="520" y="180">Mar</text></g></svg>'''
SL=[
('Running your audit','Checking what AI says about <em>Lumen</em>.','About 2 minutes. You can book with Kody on the left while it runs.',
 '''<div class="crd load"><div style="height: 8px; border-radius: 4px; background: #ece6da; overflow: hidden;"><div style="width: 62%; height: 100%; background: #2b59d9;"></div></div>
<span class="ln d"><i>✓</i>Asked ChatGPT 40 questions people ask about med spas in Irvine</span><span class="ln d"><i>✓</i>Asked Gemini the same 40</span><span class="ln r"><i></i>Asking Claude, 26 of 40</span><span class="ln q"><i></i>Reading 612 reviews on 6 sites</span><span class="ln q"><i></i>Checking your website and 31 directories</span><span class="ln q"><i></i>Finding who AI names instead of you</span></div>'''),
('What AI says','AI mentions Lumen in <em>38%</em> of answers.','When people ask ChatGPT, Gemini and Claude about med spas in Irvine, most of the time you are not in the answer.',
 '''<div class="row3"><div class="crd kpi"><b style="color: #c13515;">38%</b><span>of AI answers mention Lumen</span></div><div class="crd kpi"><b>3 of 8</b><span>top questions where ChatGPT names you</span></div><div class="crd kpi"><b style="color: #c13515;">58</b><span>AI Score. Irvine average is 71</span></div></div>
<div class="crd" style="display: flex; flex-direction: column; gap: 8px;"><span class="ey">Asked on ChatGPT, Oct 1</span><span style="font-size: 15px;"><b>"Best med spa for natural lip filler in Irvine?"</b></span><span style="font-size: 15px; color: #3d4658;">"Coastline Med Spa and Glow Bar Irvine are popular choices..." <span style="color: #c13515; font-weight: 600;">Lumen not mentioned.</span></span></div>'''),
('What AI gets wrong','AI has <em>3 facts</em> wrong about you.','These come from old listings and other sites. People believe them, and some of them decide not to book.',
 '''<div class="crd"><div class="wr" style="font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #8a93a3;"><span>Fact</span><span>What AI says</span><span>What is true</span></div><div class="wr"><b>Mondays</b><span class="no">Open 9 to 6</span><span class="ok">Closed</span></div><div class="wr"><b>Who injects</b><span class="no">Licensed aestheticians</span><span class="ok">Dr. Nair or a nurse injector</span></div><div class="wr"><b>Consult</b><span class="no">Free</span><span class="ok">$75, credited if you book</span></div></div>'''),
('Why fixing it here is not enough','You fixed your record. <em>AI has not noticed yet.</em>','AI does not read one page. It reads dozens of sources, and most of them still have the old information. Until those agree with your record, AI keeps repeating the wrong thing.',
 '<div class="crd" style="display: flex; justify-content: center;">'+AI_SVG+'</div>'),
('Who AI recommends instead','Right now AI sends people to <em>Coastline</em>.','Same rating as you. They answer questions, their listings agree, and they have press AI trusts.',
 '''<div class="crd" style="display: flex; flex-direction: column; gap: 12px;"><span class="ey">Share of AI answers, med spas in Irvine</span>
<div style="display: grid; grid-template-columns: 160px 1fr; gap: 12px; align-items: center;"><b>Coastline Med Spa</b><div class="bar" style="width: 78%; background: #13203a;">78%</div><b>Glow Bar Irvine</b><div class="bar" style="width: 61%; background: #5b6474;">61%</div><b>Spectrum Aesthetics</b><div class="bar" style="width: 44%; background: #8a93a3;">44%</div><b style="color: #c13515;">Lumen</b><div class="bar" style="width: 38%; background: #e5482d;">38%</div></div></div>'''),
('How we fix it','We make the sources agree, then make AI <em>recommend you</em>.','Every piece is approved by you before it goes out. Here is what each plan does, and where your AI Score goes.',
 '''<div style="display: grid; grid-template-columns: 1fr 560px; gap: 18px; align-items: start;"><div class="pl3" style="grid-template-columns: 1fr;">
<a class="pc {{cFix}}" onClick="{{pFix}}"><span style="display: flex; justify-content: space-between; align-items: baseline;"><strong style="font-size: 16px;">Fix</strong><b>$500<span style="font-size: 14px; font-family: Figtree, sans-serif;">/mo</span></b></span><span style="font-size: 13px; color: #3d4658;">Gets your correct info onto a new directory every day. AI Score about 63 by March.</span></a>
<a class="pc {{cTrust}}" onClick="{{pTrust}}"><span style="display: flex; justify-content: space-between; align-items: baseline;"><strong style="font-size: 16px;">Trust <span style="font-size: 11px; background: #13203a; color: #fff; padding: 2px 8px; border-radius: 9px; vertical-align: 2px;">Most picked</span></strong><b>$1,500<span style="font-size: 14px; font-family: Figtree, sans-serif;">/mo</span></b></span><span style="font-size: 13px; color: #3d4658;">Plus review replies, answers to locals, press releases and Google posts. About 72 by March.</span></a>
<a class="pc {{cAuthority}}" onClick="{{pAuthority}}"><span style="display: flex; justify-content: space-between; align-items: baseline;"><strong style="font-size: 16px;">Authority</strong><b>$3,000<span style="font-size: 14px; font-family: Figtree, sans-serif;">/mo</span></b></span><span style="font-size: 13px; color: #3d4658;">Plus your website, articles and the story only you can tell. About 80 by March.</span></a></div>
<div class="crd"><span class="ey">Your AI Score, forecast</span>'''+CHART+'''</div></div>'''),
]
N=len(SL)
slides=''
for i,(ey,t,lead,body) in enumerate(SL):
    slides+=f'<sc-if value="{{{{s{i}}}}}" hint-placeholder-val="{{{{ {"true" if i==0 else "false"} }}}}"><span class="ey">{ey}</span><h1 class="st">{t}</h1><p class="lead">{lead}</p>{body}</sc-if>'
LEFT=f'''<div class="at-l">{WAVE}<span class="big">Go through it <em>with Kody</em>.</span><p>Kody Muffoletto, your representative, walks you through your audit in 30 minutes and answers anything.</p>
<span style="font-size: 13px; font-weight: 700; color: #13203a;">Thursday, Oct 1 · Pacific</span><div class="slots"><span>9:00 AM</span><span class="on">10:30 AM</span><span>1:00 PM</span><span>3:30 PM</span></div><a href="#" class="kbtn">Book Thursday, 10:30 AM</a>
<span style="flex-grow: 1;"></span><div class="sup">Rather write? Email support at <a href="mailto:support@localairegistry.com">support@localairegistry.com</a></div></div>'''
TOP=f'<div class="at-top"><a href="OwnerHome.dc.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">{LOGO}<span style="font-weight: 700; font-size: 16px; color: #13203a;">Local AI Registry</span></a><span style="display: flex; align-items: center; gap: 18px;"><span class="mu" style="font-size: 13px;">Free AI audit · Lumen Aesthetics</span><a href="OwnerHome.dc.html" style="font-size: 14px; font-weight: 600; color: #3d4658; text-decoration: none;">Back to dashboard</a></span></div>'
FOOT='<span class="bk" onClick="{{back}}" style="visibility: {{bv}};">‹ Back</span><span class="dots"><sc-for list="{{dots}}" as="d" hint-placeholder-count="6"><i class="{{d}}"></i></sc-for></span><sc-if value="{{notLast}}" hint-placeholder-val="{{ true }}"><span class="nx" onClick="{{next}}">{{nxl}} <span>⟶</span></span></sc-if><sc-if value="{{last}}" hint-placeholder-val="{{ false }}"><span style="display: flex; gap: 16px; align-items: center;"><a href="Audit.dc.html" class="bk" style="text-decoration: none;">See the full report</a><a href="Checkout.dc.html" class="nx">Start {{pk}} <span>⟶</span></a></span></sc-if>'
BODY=TOP+f'<div class="at">{LEFT}<div class="at-r"><div class="at-body">{slides}</div><div class="at-foot">{FOOT}</div></div></div>'
JS=f'''    const S = this.state || {{}}; const i = S.i || 0, N = {N};
    const v = {{ dots: Array.from({{ length: N }}, (_, k) => k === i ? 'on' : (k < i ? 'done' : '')), back: () => this.setState({{ i: Math.max(0, i - 1) }}), next: () => this.setState({{ i: Math.min(N - 1, i + 1) }}), bv: i === 0 ? 'hidden' : 'visible', notLast: i < N - 1, last: i === N - 1, nxl: i === 0 ? 'Show me the results' : 'Next' }};
    for (let k = 0; k < N; k++) v['s' + k] = k === i;
    const pk = S.pk || 'Trust'; v.pk = pk; ['Fix', 'Trust', 'Authority'].forEach(n => {{ v['c' + n] = pk === n ? 'hot' : ''; v['p' + n] = () => this.setState({{ pk: n }}); }});
    return v;'''
open(P2+'Next.dc.html','w').write(page('Free AI audit',CSS,BODY,JS)); print('ok')
