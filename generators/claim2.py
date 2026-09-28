import sys,re; sys.path.insert(0,'/tmp/gen'); from common import *
exec(open('/tmp/ed61.py').read().split("CL=['Claim'")[0])
REP='''<span style="display: flex; justify-content: flex-end; align-items: center; gap: 12px;"><span style="width: 34px; height: 34px; border-radius: 50%; background: #dfe8f5; color: #13203a; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700;">KM</span><span style="display: flex; flex-direction: column; line-height: 17px;"><span style="font-size: 13px;"><span class="mu">Your rep,</span> <strong>Kody</strong> · <a href="#" style="font-weight: 600;">Book a meeting</a></span><a href="mailto:support@localairegistry.com" style="font-size: 12px; color: #667085;">support@localairegistry.com</a></span></span>'''
FL=r'''.cw{display:grid;grid-template-columns:minmax(0,560px) 380px;gap:64px;justify-content:center;align-items:start;padding:36px 40px 40px}.fw{display:flex;flex-direction:column;gap:0}.side{margin-top:8px;padding:26px;border-radius:6px;background:#f5e3cc;border:1px solid #e6cfb2;display:flex;flex-direction:column;gap:14px}.side .ey{font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#5b6474}.side p{margin:0;font-size:14px;line-height:22px;color:#3d4658}.side .li{display:flex;gap:10px;font-size:14px;line-height:21px;color:#13203a}
.fw h1{margin:0 0 6px;font-size:38px;line-height:42px}
.lab{font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#3d4658;margin:16px 0 6px}
.fin{height:44px;border:1px solid #e0dbd0;border-radius:6px;background:#ffffff;display:flex;align-items:center;padding:0 14px;font-size:15px;color:#98a0ad;box-sizing:border-box}
.cc{display:flex;align-items:center;gap:6px;height:44px;padding:0 12px;border-right:1px solid #e0dbd0;background:#f3efe7;font-size:14px;color:#13203a;border-radius:6px 0 0 6px}
.hint{font-size:12px;color:#3d4658;margin-top:6px}
.ck{display:grid;grid-template-columns:20px 1fr;gap:10px;margin-top:14px}
.ck i{width:16px;height:16px;border:1.5px solid #3d4658;border-radius:3px;margin-top:2px;display:block}
.ck i.on{background:#13203a;border-color:#13203a}
.ck strong{font-size:12px;display:block;margin-bottom:2px}.ck span{font-size:11px;line-height:16px;color:#5b6474}
.nbtn{height:48px;border-radius:9999px;gap:10px;background:#13203a;color:#ffffff;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:600;text-decoration:none;margin-top:20px}
'''
T='Your name, mobile and work email. We text you a code to confirm it is you.'
TX='By checking this box, I consent to receive transactional messages related to my account, orders, or services I have requested. These messages may include appointment reminders, order confirmations, and account notifications. Message frequency may vary. Message &amp; data rates may apply. Reply HELP for help or STOP to opt out.'
MK='By checking this box, I consent to receive marketing and promotional messages, including special offers, discounts, and product updates. Message frequency may vary. Message &amp; data rates may apply. Reply HELP for help or STOP to opt out.'
B=fhead(['Claim','Text code','Confirm info','Verify ownership'],1,'')
B=re.sub(r'<span style="display: flex; justify-content: flex-end;">.*?</span></header>',REP+'</header>',B,flags=re.S) if '</header>' in B else B
B+=f'''<div class="cw"><div class="fw"><h1>Claim Lumen Aesthetics</h1><span style="font-size: 13px; color: #3d4658;">71 Fortune Dr, Irvine, CA 92618, USA</span><span style="font-size: 15px; line-height: 24px; color: #3d4658; margin-top: 12px;">{T}</span>
<span class="lab">Your name</span><div class="fin">Your name</div>
<span class="lab">Your mobile</span><div class="fin" style="padding: 0;"><span class="cc">🇺🇸 +1 ▾</span><span style="padding: 0 12px;">(415) 555 1234</span></div><span class="hint">Your own mobile, not the business's listed number.</span>
<span class="lab">Your work email</span><div class="fin">you@lumenirvine.com</div>
<div class="ck"><i class="on"></i><div><strong>Transactional Messages Opt-In</strong><span>{TX}</span></div></div>
<div class="ck"><i></i><div><strong>Marketing Messages Opt-In</strong><span>{MK}</span></div></div>
<a href="OTP.dc.html" class="nbtn">Text me a code <span>⟶</span></a><span style="font-size: 13px; color: #3d4658; margin-top: 12px;">Phone doesn't match or already claimed? <a href="ClaimIssue.dc.html">Get help</a></span></div><div class="side"><span class="ey">What you get</span><span style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 28px; line-height: 32px; color: #13203a;">Your record, <em style="color: #e5482d;">yours</em>.</span><div class="li"><span>✓</span>Answer the 18 questions locals asked about Lumen</div><div class="li"><span>✓</span>Fix the 3 facts AI gets wrong</div><div class="li"><span>✓</span>See your AI Score every month</div><p>Free. No card, no contract. About 3 minutes.</p></div></div>'''
open(P+'Claim.dc.html','w').write(page('Claim',FL,B,'    return {};'))
# SIGN IN
SI=r'''.sw{display:flex;flex-direction:column;align-items:center;padding:110px 0 80px}
.box{position:relative;width:368px;padding:40px 36px;margin-top:36px}
.box i{position:absolute;width:14px;height:14px;border-color:#8a8a8a;border-style:solid}
.box .a{top:0;left:0;border-width:1px 0 0 1px}.box .b{top:0;right:0;border-width:1px 1px 0 0}.box .c{bottom:0;left:0;border-width:0 0 1px 1px}.box .d{bottom:0;right:0;border-width:0 1px 1px 0}
.box h1{margin:0 0 12px;font-size:38px;line-height:42px}
.lab2{display:flex;justify-content:space-between;font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#3d4658;margin:26px 0 8px}
.lab2 a{font-size:12px;letter-spacing:0;text-transform:none;font-weight:500;color:#3d4658}
.fin2{height:48px;border:1px solid #e0dbd0;background:#ffffff;display:flex;align-items:center;justify-content:flex-end;padding:0 14px;box-sizing:border-box}
.b1{height:44px;border-radius:4px;background:#13203a;color:#ffffff;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600;margin-top:20px}
.or{display:flex;align-items:center;gap:14px;margin:26px 0;font-size:11px;font-weight:700;letter-spacing:0.14em;color:#667085}.or::before,.or::after{content:"";flex:1;height:1px;background:#dcd5c7}
.b2{height:46px;border:1px solid #e0dbd0;background:#ffffff;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600}
'''
L='<svg width="18" height="18" viewBox="0 0 30 30" aria-hidden="true"><path d="M15 3 27.5 27h-8.2L15 18.6 10.7 27H2.5L15 3Z" fill="#2b59d9"></path><path d="M15 18.6 19.3 27h-8.6L15 18.6Z" fill="#e5482d"></path></svg>'
B2=f'''<div class="sw"><span style="display: flex; align-items: center; gap: 6px; font-size: 17px; font-weight: 700;">{L}Local AI Registry</span><div class="box"><i class="a"></i><i class="b"></i><i class="c"></i><i class="d"></i><h1>Sign in to your record.</h1><span style="font-size: 13px; line-height: 21px; color: #3d4658;">The registry keeps a file on every business. Sign in to read yours and keep it current.</span><span class="lab2">Email</span><div class="fin2"></div><span class="lab2">Password<a href="#">Forgot it?</a></span><div class="fin2">👁</div><a href="OwnerHome.dc.html" class="b1" style="text-decoration: none;">Sign in</a><span class="or">OR</span><div class="b2">Sign in with Google</div></div><span style="font-size: 13px; color: #3d4658; margin-top: 28px;">Not in the registry yet? <a href="Business.dc.html">Register your business</a></span></div>'''
open(P+'SignIn.dc.html','w').write(page('Sign in',SI,B2,'    return {};'))
# rep header on the rest of onboarding
for f in ['OTP.dc.html','Setup.dc.html','Next.dc.html','Upgrade.dc.html','Checkout.dc.html']:
    s=open(P+f).read()
    s2=re.sub(r'<span style="display: flex; justify-content: flex-end;"><a [^>]*>[^<]*</a></span></header>',REP+'</header>',s)
    open(P+f,'w').write(s2); print(f, s2!=s)
print('ok')
