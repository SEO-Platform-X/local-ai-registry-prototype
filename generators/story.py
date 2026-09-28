import sys; sys.path.insert(0,'/tmp/gen'); from common import *
TRI="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22'%3E%3Cpath d='M11 3.5L19.5 18.5H2.5Z' fill='none' stroke='%238a8a8a' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E\") center / 100% 100% no-repeat"
PEN="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23222222' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 20h4L19 9l-4-4L4 16v4Z'/%3E%3Cpath d='M13.5 6.5l4 4'/%3E%3C/svg%3E\")"
CSS=r'''.wrap{padding:40px 56px 64px;display:flex;flex-direction:column;gap:40px;background:#f7f7f7}
.flowh{display:flex;flex-direction:column;gap:6px}
.flowh h2{margin:0;font-size:28px;font-weight:700}
.flowh span{font-size:15px;color:#6a6a6a}
.frames{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:start}
.fr{display:flex;flex-direction:column;gap:10px}
.fr .lb{font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#8a8a8a}
.fr .lb b{color:#ff385c}
.scr{background:#ffffff;border-radius:18px;box-shadow:0 4px 20px rgba(0,0,0,0.08);padding:22px;display:flex;flex-direction:column;gap:14px;min-height:420px;box-sizing:border-box}
.mh{display:flex;align-items:center;justify-content:space-between;padding-bottom:12px;border-bottom:1px solid #ebebeb}
.mh strong{font-size:17px}
.x{font-size:18px;color:#6a6a6a}
.fl{display:flex;flex-direction:column;gap:6px}
.fl label{font-size:13px;font-weight:600}
.inp{height:44px;border:1px solid #b0b0b0;border-radius:10px;padding:0 12px;display:flex;align-items:center;font-size:14px;color:#222222;box-sizing:border-box}
.inp.ta{height:72px;align-items:flex-start;padding-top:10px}
.inp.focus{border:2px solid #222222}
.opt{display:flex;align-items:center;gap:10px;padding:11px 12px;border:1px solid #dddddd;border-radius:10px;font-size:14px}
.opt.on{border:2px solid #222222;background:#fafafa}
.opt .rdo{width:16px;height:16px;border-radius:50%;border:2px solid #b0b0b0;box-sizing:border-box;flex-shrink:0}
.opt.on .rdo{border:5px solid #222222}
.chips{display:flex;gap:6px;flex-wrap:wrap}
.chip{display:inline-flex;align-items:center;height:30px;padding:0 12px;border-radius:15px;border:1px solid #dddddd;font-size:12px;font-weight:600}
.chip.on{background:#222222;border-color:#222222;color:#ffffff}
.mk{position:relative;display:inline-block;width:11px;height:11px;margin:0 6px 1px 0;vertical-align:middle;flex-shrink:0}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.6px solid #e8740c;border-radius:50%}
.mk-ai::after{inset:0;background:'''+TRI+'''}
.row{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 0;border-bottom:1px solid #f0f0f0;font-size:14px}
.row .k{color:#6a6a6a}
.pen{display:inline-block;width:26px;height:26px;border-radius:50%;border:1px solid #d6d6d6;background:#ffffff '''+PEN+''' center / 13px 13px no-repeat;box-shadow:0 1px 3px rgba(0,0,0,0.08);vertical-align:middle}
.pen.hov{border-color:#222222;box-shadow:0 0 0 4px rgba(255,56,92,0.18)}
.old{color:#a0a0a0;text-decoration:line-through;font-size:13px}
.note{padding:12px 14px;border-radius:12px;background:#f7f5f1;font-size:13px;line-height:19px;color:#484848}
.warn{padding:12px 14px;border-radius:12px;background:#fff4e5;font-size:13px;line-height:19px;color:#7a4a00}
.okb{padding:14px;border-radius:12px;background:#e8f5ea;font-size:14px;line-height:20px;color:#1c5f2a}
.push{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 12px;border-radius:12px;background:#fff1ec;font-size:13px;color:#a8452c}
.big{display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;padding:20px 0}
.big .ic{width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px}
'''
def frame(n,lbl,inner): return f'<div class="fr"><span class="lb"><b>{n}</b> · {lbl}</span><div class="scr">{inner}</div></div>'
def flow(title,sub,frames,cols=3): return f'<div style="display: flex; flex-direction: column; gap: 18px;"><div class="flowh"><h2>{title}</h2><span>{sub}</span></div><div class="frames" style="grid-template-columns: repeat({cols}, minmax(0, 1fr));">{"".join(frames)}</div></div>'
# ---------- REPORT (public) ----------
s1=frame('1','Visitor taps Suggest an edit',f'''<div class="mh"><strong>Suggest an edit</strong><span class="x">✕</span></div>
<div class="fl"><label>What needs fixing?</label><div class="chips"><span class="chip on">Hours</span><span class="chip">Phone</span><span class="chip">Price</span><span class="chip">Service</span><span class="chip">Team</span><span class="chip">Something else</span></div></div>
<div class="fl"><label>Monday hours right now</label><div class="row" style="padding: 6px 0;"><span><span class="mk mk-ai"></span>9 AM to 6 PM</span><span class="mu" style="font-size: 12px;">AI guess</span></div></div>
<div class="fl"><label>What should it say?</label><div class="inp focus">Closed Mondays</div></div>
<div class="fl"><label>How do you know?</label><div class="chips"><span class="chip on">I called</span><span class="chip">I went there</span><span class="chip">Their website or sign</span><span class="chip">I work there</span></div></div>
<div class="fl"><label>When? <span class="mu" style="font-weight: 400;">(optional photo helps)</span></label><div class="inp">Monday, Sep 21, 2026 · + Add a photo</div></div>
<span class="btn b-dark" style="margin-top: auto;">Submit</span>''')
s2=frame('2','Submitted',f'''<div class="big"><span class="ic" style="background: #fff1e0; color: #e8740c;">○</span><strong style="font-size: 20px;">Thanks, Tom.</strong><span style="font-size: 14px; line-height: 21px; color: #484848;">Your fix shows on the page right away, marked as visitor submitted.</span></div>
<div class="note"><strong>What happens next</strong><br>When a second neighbor or Lumen agrees, it turns into a confirmed fact, and it is what AI starts repeating. We let Lumen know about your fix today.</div>
<div class="note" style="background: #ffffff; border: 1px solid #ebebeb;">We'll tell you when it's confirmed. Your fixes so far: <strong>4 confirmed</strong></div>
<span class="btn" style="margin-top: auto;">Back to Lumen</span>''')
s3=frame('3','What the next visitor sees',f'''<strong style="font-size: 16px;">Hours</strong>
<div class="row"><span class="k">Monday</span><span><span class="mk mk-vis"></span><strong>Closed</strong> <sup style="font-size: 10px; color: #6a6a6a;">[4]</sup></span></div>
<div class="row"><span class="k">Tuesday</span><span><span class="mk mk-site"></span>9 AM to 6 PM <sup style="font-size: 10px; color: #6a6a6a;">[5]</sup></span></div>
<div class="row"><span class="k">Wednesday</span><span><span class="mk mk-site"></span>9 AM to 6 PM <sup style="font-size: 10px; color: #6a6a6a;">[5]</sup></span></div>
<span style="display: flex; gap: 8px; align-items: center; font-size: 13px;"><span class="mu">Been there on a Monday?</span><span class="btn b-sm b-dark">It's closed</span><span class="btn b-sm">It's open</span></span>
<div style="border-top: 1px solid #ebebeb; padding-top: 12px; display: flex; flex-direction: column; gap: 6px;"><span style="display: flex; justify-content: space-between; align-items: baseline;"><strong style="font-size: 13px;">References</strong><a href="#history" style="font-size: 12px; font-weight: 600;">Change history</a></span>
<span style="font-size: 11px; line-height: 16px; color: #6a6a6a;"><strong style="color: #222222;">[4]</strong> <span class="mk mk-vis"></span>Visitor submitted · Tom H. called, Sep 21 · Evidence: call screenshot · <a href="#history" style="font-weight: 600;">History (3)</a></span>
<span style="font-size: 11px; line-height: 16px; color: #6a6a6a;"><strong style="color: #222222;">[5]</strong> <span class="mk mk-site"></span>Confirmed · Google Business Profile, Sep 26</span></div>''')
s4=frame('4','Change history','<div id="history" class="mh"><strong>Monday hours, history</strong><span class="x">✕</span></div>'+''.join(f'<div style="display: flex; gap: 12px; padding: 10px 0; border-bottom: 1px solid #f0f0f0;"><span class="mk mk-{m}" style="margin-top: 4px;"></span><span style="display: flex; flex-direction: column; gap: 2px; font-size: 13px; line-height: 18px;"><strong>{v}</strong><span class="mu">{w}</span><span style="color: #484848;">{d}</span></span></div>' for m,v,w,d in [('vis','Closed','Today · Aisha M., visited','Second neighbor agrees. Photo of the door sign. One more, or the owner, makes it confirmed.'),('vis','Closed','Sep 21, 2026 · Tom H., called','First report. Voicemail said closed Mondays.'),('ai','9 AM to 6 PM','Aug 2, 2026 · What ChatGPT and Gemini say','AI engines repeat this from an old listing.'),('site','9 AM to 6 PM','Jun 10, 2026 · Google Business Profile','Original source, not updated since.')])+'<span class="mu" style="font-size: 12px;">Every change to every fact is kept here, newest first. Nothing is ever deleted.</span>')
f1=flow('A visitor fixes a fact','From "Suggest an edit" under the booking card. The fix shows with a hollow circle and a reference, never crossed out.',[s1,s2,s3,s4],4)
r1=frame('1','Visitor taps Report this listing',f'''<div class="mh"><strong>Why are you reporting this listing?</strong><span class="x">✕</span></div>
<span class="mu" style="font-size: 13px; margin-top: -4px;">This won't be shared with the business.</span>
<div class="opt"><span class="rdo"></span>Some information is wrong</div><div class="opt"><span class="rdo"></span>This business closed or moved</div><div class="opt"><span class="rdo"></span>It's a duplicate of another page</div><div class="opt on"><span class="rdo"></span>The person who claimed it isn't the owner</div><div class="opt"><span class="rdo"></span>Fake, offensive or spam content</div>
<span class="btn b-dark" style="margin-top: auto;">Next</span>''')
r2=frame('2','Not the owner: prove it',f'''<div class="mh"><strong>Who owns Lumen Aesthetics?</strong><span class="x">✕</span></div>
<div class="fl"><label>You are</label><div class="chips"><span class="chip on">The owner</span><span class="chip">A manager</span><span class="chip">Someone else</span></div></div>
<div class="fl"><label>Your name and work email</label><div class="inp">Dr. Priya Nair · priya@lumenirvine.com</div></div>
<div class="fl"><label>Fastest proof</label><span class="btn b-dark">Connect Google Business Profile</span><span class="mu" style="font-size: 12px; text-align: center;">or upload a business license, utility bill or state license</span></div>
<div class="warn">While we review, the page is locked so nobody can edit it. The current claimant is told a dispute was opened, not who opened it. Most reviews take 2 business days.</div>
<span class="btn" style="margin-top: auto;">Submit dispute</span>''')
r3=frame('3','Dispute opened',f'''<div class="big"><span class="ic" style="background: #eef2fb; color: #2d4a8a;">⚑</span><strong style="font-size: 20px;">We're on it.</strong><span style="font-size: 14px; line-height: 21px; color: #484848;">Case LAIR-20931. We'll email you within 2 business days.</span></div>
<div class="note"><strong>On the public page, meanwhile</strong><br>A small "Ownership under review" note shows next to the name. Edits are paused. Neighbors can still post.</div>
<div class="okb">If you connected Google Business Profile, we can usually confirm you on the spot and move the page to you today.</div>''')
f2=flow('A visitor reports the listing','From "Report this listing" under the booking card. The owner dispute is the case that needs the most care.',[r1,r2,r3])
BODY=header('<a href="Main.dc.html" class="btn b-sm">Back to the profile</a>')+f'<div class="wrap">{f1}{f2}</div>'
open(P+'Report.dc.html','w').write(page('Suggest an edit and report this listing',CSS,BODY,'    return {};')); print('report')
# ---------- EDIT (owner) ----------
e1=frame('1','Owner sees a pencil on everything',f'''<strong style="font-size: 16px;">Hours</strong>
<div class="row"><span class="k">Monday</span><span style="display: flex; align-items: center; gap: 8px;"><span class="mk mk-ai"></span>9 AM to 6 PM<span class="pen hov"></span></span></div>
<div class="row"><span class="k">Tuesday</span><span style="display: flex; align-items: center; gap: 8px;"><span class="mk mk-site"></span>9 AM to 6 PM<span class="pen"></span></span></div>
<div class="row"><span class="k">Wednesday</span><span style="display: flex; align-items: center; gap: 8px;"><span class="mk mk-site"></span>9 AM to 6 PM<span class="pen"></span></span></div>
<div class="row"><span class="k">Thursday</span><span style="display: flex; align-items: center; gap: 8px;"><span class="mk mk-vis"></span>9 AM to 8 PM<span class="pen"></span></span></div>
<span class="mu" style="font-size: 12px;">Every fact, section and photo has one. Only you see them.</span>''')
e2=frame('2','Edit panel',f'''<div class="mh"><strong>Edit Monday hours</strong><span class="x">✕</span></div>
<div class="fl"><label>Right now</label><div class="row" style="padding: 4px 0;"><span><span class="mk mk-ai"></span>9 AM to 6 PM</span><span class="mu" style="font-size: 12px;">What ChatGPT and Gemini say</span></div></div>
<div class="fl"><label>Change it to</label><div class="chips"><span class="chip on">Closed</span><span class="chip">Open</span></div></div>
<div class="fl"><label>Note for your customers <span class="mu" style="font-weight: 400;">(optional)</span></label><div class="inp ta">We take Monday calls for Tuesday bookings.</div></div>
<div class="opt" style="opacity: 0.55;"><span class="rdo"></span><span>Also update Google Business Profile<span class="mu" style="display: block; font-size: 12px;">Verify ownership first</span></span></div>
<span class="btn b-dark" style="margin-top: auto;">Save</span>''')
e3=frame('3','Saved: tracked change and push to AI',f'''<strong style="font-size: 16px;">Hours</strong>
<div class="row"><span class="k">Monday</span><span style="display: flex; flex-direction: column; align-items: flex-end; gap: 2px;"><span style="display: flex; align-items: center; gap: 8px;"><span class="mk mk-site"></span><strong>Closed</strong><span class="pen"></span></span><span class="old">9 AM to 6 PM</span></span></div>
<div class="push"><span>AI is still showing the old hours.</span><strong>Push it to AI</strong></div>
<div class="note">The crossed-out value is only visible to you. Customers see <strong>Closed</strong> with a confirmed mark, dated today.</div>
<div class="note" style="background: #ffffff; border: 1px solid #ebebeb;"><strong>Push it to AI</strong> sends the change to Google, Apple Maps, Yelp, Bing and 40 directories, the sources AI repeats. Included in every paid plan. <a href="Upgrade.dc.html" style="font-weight: 600;">See plans</a></div>''')
f3=flow('The owner edits a fact','Same flow for every field: hours, prices, services, team, photos, policies.',[e1,e2,e3])
BODY=header('<a href="Dashboard.dc.html" class="btn b-sm">Back to your page</a>')+f'<div class="wrap">{f3}</div>'
open(P+'Edit.dc.html','w').write(page('How editing works',CSS,BODY,'    return {};')); print('edit')
