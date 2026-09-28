import sys,re; sys.path.insert(0,'/tmp/gen'); from common import *
from headers import LOGO
P2='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
SH=r'''.cf-top{height:64px;box-sizing:border-box;padding:0 32px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #e4ded2;background:#f3efe7}
.cf{display:grid;grid-template-columns:500px 1fr;height:836px;overflow:hidden}
.cf-l{background:#f5e3cc;border-right:1px solid #e6cfb2;padding:36px 44px 24px;display:flex;flex-direction:column;gap:22px;box-sizing:border-box;overflow:hidden;height:836px}
.cf-st{display:flex;flex-direction:column;gap:0}
.cf-s{display:grid;grid-template-columns:28px 1fr;gap:12px;align-items:start;padding:7px 0;font-size:14px;color:#8a7b69}
.cf-s .d{width:24px;height:24px;border-radius:50%;border:1.5px solid #c9b59a;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;box-sizing:border-box}
.cf-s.done{color:#3d4658}.cf-s.done .d{background:#237233;border-color:#237233;color:#fff}
.cf-s.on{color:#13203a;font-weight:700}.cf-s.on .d{background:#13203a;border-color:#13203a;color:#fff}
.cf-sub{padding-left:40px;font-size:13px;color:#8a7b69;line-height:22px}.cf-sub b{color:#13203a}
.cf-vis{flex-grow:1;display:flex;flex-direction:column;justify-content:center;gap:14px}
.cf-vis .big{font-family:"Cormorant Garamond",Georgia,serif;font-size:40px;line-height:44px;color:#13203a}
.cf-vis .big em{color:#e5482d}
.cf-vis p{margin:0;font-size:15px;line-height:24px;color:#3d4658;max-width:380px}
.cf-rep{display:flex;flex-direction:column;gap:12px;padding:16px 18px;border-radius:8px;background:#fbf4ea;border:1px solid #e6cfb2}
.cf-kb{height:38px;padding:0 16px;border-radius:9999px;background:#13203a;color:#ffffff;display:inline-flex;align-items:center;font-size:13px;font-weight:600;text-decoration:none;white-space:nowrap}
.cf-rep .av{width:40px;height:40px;border-radius:50%;background:#dfe8f5;color:#13203a;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;flex-shrink:0}
.cf-r{display:flex;flex-direction:column;min-height:0}
.cf-body{flex:1;overflow:auto;padding:44px 72px 24px;box-sizing:border-box}
.cf-in{max-width:560px;display:flex;flex-direction:column;gap:0}
.cf-in h1{margin:4px 0 12px;font-size:44px;line-height:48px}
.cf-in .kf{gap:12px !important;margin-top:4px}
.cf-in .kc{height:48px !important;padding:0 20px !important;font-size:15px !important}
.cf-in > span{display:block}
.cf-foot{height:96px;flex-shrink:0;box-sizing:border-box;border-top:1px solid #e4ded2;padding:0 72px;display:flex;align-items:center;justify-content:space-between;background:#f3efe7}
.cf-next{display:inline-flex;align-items:center;justify-content:center;gap:12px;height:56px;min-width:260px;padding:0 32px;border-radius:9999px;background:#13203a;color:#ffffff;font-size:16px;font-weight:600;text-decoration:none;cursor:pointer}
.cf-back{font-size:15px;font-weight:600;color:#3d4658;text-decoration:none;cursor:pointer}
.lab{font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#3d4658;margin:18px 0 7px}
.fin{height:48px;border:1px solid #e0dbd0;border-radius:6px;background:#ffffff;display:flex;align-items:center;padding:0 14px;font-size:15px;color:#98a0ad;box-sizing:border-box}
.cc{display:flex;align-items:center;gap:6px;height:46px;padding:0 14px;border-right:1px solid #e0dbd0;background:#ffffff;font-size:14px;font-weight:600;color:#13203a;border-radius:6px 0 0 6px}
.hint{font-size:12px;color:#5b6474;margin-top:6px}
.ck{display:grid;grid-template-columns:20px 1fr;gap:10px;margin-top:16px}
.ck i{width:16px;height:16px;border:1.5px solid #3d4658;border-radius:3px;margin-top:1px;display:block}.ck i.on{background:#13203a;border-color:#13203a}
.ck strong{font-size:12px;display:block;margin-bottom:2px}.ck span{font-size:11px;line-height:16px;color:#5b6474}
.cf-in .fr{display:grid !important;grid-template-columns:1fr auto !important;grid-template-areas:"k acts" "v acts";gap:4px 16px !important;align-items:center;padding:16px 0 !important;border-top:1px solid #e4ded2 !important}
.cf-in .fr .k{grid-area:k;font-size:11px !important;font-weight:700 !important;letter-spacing:0.12em;text-transform:uppercase;color:#5b6474 !important}
.cf-in .fr .v{grid-area:v;font-size:16px !important;line-height:23px;color:#13203a;display:block !important}
.cf-in .fr .v .mk{display:inline-block;margin-right:8px;vertical-align:1px}.cf-in .fr .v s{margin-left:8px}
.cf-in .fr .acts{grid-area:acts;display:flex;gap:6px}
.cf-in .chipb{height:34px !important;padding:0 14px !important;border-radius:9999px !important;font-size:13px !important;border:1px solid #13203a !important;background:#ffffff !important;color:#13203a !important}
.cf-in .chipb.ok{background:#237233 !important;border-color:#237233 !important;color:#ffffff !important}
.cf-in .chipb.no{background:#efeae0 !important;border-color:#efeae0 !important;color:#8a8a8a !important}
.cf-in .kc{border-radius:9999px !important;background:#ffffff !important}
.cf-in .kc.on{border:2px solid #13203a !important;background:#fbf4ea !important}
.cf-in .kc .n{background:#13203a !important}
.otpb{display:flex;gap:10px;margin-top:24px}.otpb span{width:56px;height:64px;border:1px solid #e0dbd0;border-radius:8px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:600;color:#13203a}.otpb span.f{border:2px solid #13203a}
'''
STORE='''<svg viewBox="0 0 240 150" width="240" height="150" aria-hidden="true" fill="none" stroke="#13203a" stroke-width="1.4"><rect x="40" y="40" width="160" height="96"/><path d="M34 40h172l-8-18H42z" fill="#fbf4ea"/><path d="M40 70h160"/><path d="M52 70 60 56h120l8 14" fill="#e5482d" fill-opacity="0.18" stroke="#e5482d"/><rect x="104" y="90" width="32" height="46" fill="#dfe8f5"/><rect x="54" y="88" width="36" height="30"/><rect x="150" y="88" width="36" height="30"/><path d="M20 136h200" stroke-width="1"/><text x="120" y="35" font-size="9" text-anchor="middle" fill="#13203a" stroke="none" font-family="Figtree,sans-serif" letter-spacing="2">LUMEN</text></svg>'''
STEPS=['Claim','Text code','Confirm info','Verify ownership']
SUB=['Basics','Services','Known for','Team','Links']
def left(cur, big, para, subcur=None):
    st=''
    for i,t in enumerate(STEPS,1):
        c='done' if i<cur else ('on' if i==cur else '')
        st+=f'<div class="cf-s {c}"><span class="d">{"✓" if i<cur else i}</span><span>{t}</span></div>'
        if i==3 and cur==3:
            st+='<div class="cf-sub">'+' · '.join(f'<b>{x}</b>' if subcur==x else x for x in SUB) if not subcur else '<div class="cf-sub">{{subLine}}</div>'
            if not subcur: st+='</div>'
    return f'''<div class="cf-l"><div class="cf-st">{st}</div><div class="cf-vis">{STORE}<span class="big">{big}</span><p>{para}</p></div><div class="cf-rep"><div style="display: flex; align-items: center; gap: 12px;"><span class="av">KM</span><span style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1;"><strong style="font-size: 14px;">Kody Muffoletto</strong><span style="font-size: 12px; color: #5b6474;">Your rep. He can do this with you in 15 minutes.</span></span><a href="#" class="cf-kb">Book with Kody</a></div><div style="height: 1px; background: #e6cfb2;"></div><div style="font-size: 13px; color: #3d4658;">Or contact support at <a href="mailto:support@localairegistry.com" style="color: #13203a; font-weight: 600;">support@localairegistry.com</a></div></div></div>'''
TOP=f'<div class="cf-top"><a href="Home.dc.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">{LOGO}<span style="font-weight: 700; font-size: 16px; color: #13203a;">Local AI Registry</span></a><a href="Main.dc.html" style="font-size: 14px; font-weight: 600; color: #3d4658; text-decoration: none;">Save and exit</a></div>'
def shell(cur,big,para,inner,foot,subcur=None):
    return TOP+f'<div class="cf">{left(cur,big,para,subcur)}<div class="cf-r"><div class="cf-body"><div class="cf-in">{inner}</div></div><div class="cf-foot">{foot}</div></div></div>'
TX='By checking this box, I consent to receive transactional messages related to my account, orders, or services I have requested. These messages may include appointment reminders, order confirmations, and account notifications. Message frequency may vary. Message &amp; data rates may apply. Reply HELP for help or STOP to opt out.'
MK='By checking this box, I consent to receive marketing and promotional messages, including special offers, discounts, and product updates. Message frequency may vary. Message &amp; data rates may apply. Reply HELP for help or STOP to opt out.'
claim=f'''<h1>Claim Lumen Aesthetics</h1><span style="font-size: 14px; color: #5b6474;">71 Fortune Dr, Irvine, CA 92618</span>
<span class="lab">Your name</span><div class="fin">Your name</div>
<span class="lab">Your mobile</span><div class="fin" style="padding: 0;"><span class="cc">🇺🇸 +1 ▾</span><span style="padding: 0 12px;">(415) 555 1234</span></div><span class="hint">Your own mobile, not the business's listed number. We text you a code.</span>
<span class="lab">Your work email</span><div class="fin">you@lumenirvine.com</div>
<div class="ck"><i class="on"></i><div><strong>Transactional Messages Opt-In</strong><span>{TX}</span></div></div>
<div class="ck"><i></i><div><strong>Marketing Messages Opt-In</strong><span>{MK}</span></div></div>'''
FOOT=lambda back,label,href: f'<a href="{back}" class="cf-back">‹ Back</a><a href="{href}" class="cf-next">{label} <span>⟶</span></a>'
open(P2+'Claim.dc.html','w').write(page('Claim',SH,shell(1,'Your record, <em>yours</em>.','Answer the 18 questions locals asked about Lumen, fix the 3 facts AI gets wrong, and see your AI Score every month. Free, about 3 minutes.',claim,FOOT('Main.dc.html','Text me a code','OTP.dc.html')),'    return {};'))
otp='''<h1>Enter your code</h1><span style="font-size: 15px; line-height: 23px; color: #3d4658;">We texted a 6-digit code to (415) 555-1234.</span><div class="otpb"><span class="f">4</span><span class="f">8</span><span>1</span><span></span><span></span><span></span></div><span style="font-size: 14px; color: #5b6474; margin-top: 20px;">Didn't get it? <a href="#">Resend in 30s</a> · <a href="ClaimIssue.dc.html">Get help</a></span>'''
open(P2+'OTP.dc.html','w').write(page('Text code',SH,shell(2,'One text. <em>That is it.</em>','No password to remember. The code proves the page is yours.',otp,FOOT('Claim.dc.html','Confirm code','Setup.dc.html')),'    return {};'))
# SETUP: reuse setup2 content
s=open(P2+'Setup.dc.html').read()
css=s[s.index('<style>')+7:s.index('</style>')]
js=s[s.index('<script type="text/x-dc" data-dc-script>'):s.rindex('</script>')+9]
i=s.index('<div class="pane">')+len('<div class="pane">')
b=s.index('<span class="btn" onClick="{{back}}"',i); fstart=s.rfind('<div',0,b)
foot_old=s[fstart:s.index('</div>',s.index('Finish and go to your dashboard',fstart))+6]
inner=s[i:fstart]
inner=re.sub(r'<h1>(\{\{h\}\})</h1>',r'<h1>\1</h1>',inner)
foot='<span class="cf-back" onClick="{{back}}" style="visibility: {{backV}};">‹ Back</span><sc-if value="{{notLast}}" hint-placeholder-val="{{ true }}"><span class="cf-next" onClick="{{next}}">Confirm and continue <span>⟶</span></span></sc-if><sc-if value="{{last}}" hint-placeholder-val="{{ false }}"><a href="OwnerHome.dc.html" class="cf-next">Finish and go to dashboard <span>⟶</span></a></sc-if>'
body=shell(3,'Confirm what AI <em>should</em> say.','Solid green is confirmed. Hollow orange is from a visitor. The triangle is what AI engines guess. Confirm, fix, or mark it not us.',inner,foot,subcur=True)
out=page('Confirm info',css+SH+'.cf-vis svg{display:none}.cf-vis .big{font-size:34px;line-height:38px}',body,'    return {};')
out=out[:out.index('<script type="text/x-dc" data-dc-script>')]+js+out[out.rindex('</script>')+9:]
# subLine var
out=out.replace("return {","return { subLine: ['Basics', 'Services', 'Known for', 'Team', 'Links'].map((x, k) => k === (typeof si === 'number' ? si : 0) ? '• ' + x : x).join('  ·  '),",1) if False else out
open(P2+'Setup.dc.html','w').write(out)
print('ok')
