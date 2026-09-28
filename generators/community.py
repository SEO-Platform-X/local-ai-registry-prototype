# shared community data (JS) and templates
FIXES_JS=r"""    const fixes = [
      ['Lumen Aesthetics', 'Irvine', 'Hours on Monday', 'Open 10 AM to 6 PM', 'Closed Mondays', 'Tom H.', 'called on a Monday, no answer, door locked', '2 days ago', 'Confirmed by 3 neighbors and the owner', 1],
      ['Spectrum Aesthetics MD', 'Irvine', 'Who does Botox', 'Aestheticians', 'Dr. Chen or a nurse practitioner', 'Aisha M.', 'had Botox there in August', '5 hours ago', 'Confirmed by the state license lookup', 1],
      ['Pho Saigon Bay', 'Tustin', 'Parking', 'Street parking only', 'Free lot behind the building', 'Diego R.', 'parked there last Friday', '1 hour ago', 'Waiting for a second neighbor', 0],
      ['Harbor Family Dental', 'Costa Mesa', 'Takes Delta Dental', 'No', 'Yes, PPO plans', 'Linh T.', 'used it for a cleaning in September', 'Yesterday', 'Confirmed by the owner', 1],
      ['Glow Bar Irvine', 'Irvine', 'Open Sundays', 'Closed', 'Open 10 AM to 4 PM', 'Priya S.', 'went last Sunday', '3 hours ago', 'Waiting for a second neighbor', 0],
      ['Coastline MedSpa', 'Newport Beach', 'Speaks Spanish', 'Not mentioned', 'Yes, two nurses', 'Carmen V.', 'booked her mom there in Spanish', '4 days ago', 'Confirmed by 2 neighbors', 1]
    ].map(x => ({ b: x[0], city: x[1], f: x[2], old: x[3], nw: x[4], who: x[5], how: x[6], when: x[7], st: x[8], stc: x[9] ? '#237233' : '#b86a00', mk: x[9] ? 'site' : 'vis', ai: x[9] ? 'AI now repeats the fix' : 'AI still says the old one' }));
    const openQs = [
      ['Does Lumen Aesthetics take HSA cards?', 'Lumen Aesthetics', '14', '3 hours ago'],
      ['Is there parking at Pho Saigon Bay on weekends?', 'Pho Saigon Bay', '9', 'Yesterday'],
      ['Which dentist in Costa Mesa sees kids on Saturdays?', 'Costa Mesa dentists', '22', '2 days ago'],
      ['Does Glow Bar do facials for sensitive skin?', 'Glow Bar Irvine', '6', '5 hours ago']
    ].map(x => ({ q: x[0], b: x[1], up: x[2], when: x[3] }));
    const experts = [
      ['Maria K.', 'MK', 'Irvine Spectrum regular', '42', '9'],
      ['Tom H.', 'TH', 'Woodbridge', '31', '7'],
      ['Linh T.', 'LT', 'Costa Mesa parent', '27', '6'],
      ['Diego R.', 'DR', 'Tustin food scene', '58', '12']
    ].map(x => ({ n: x[0], i: x[1], t: x[2], f: x[3], w: x[4] }));
"""
CSS=r'''.fix{display:flex;flex-direction:column;gap:8px;padding:18px 20px;border-radius:14px;background:#ffffff;border:1px solid #e6e1d8}
.fix .old{font-size:14px;color:#a0a0a0;text-decoration:line-through}
.fix .nw{font-size:17px;font-weight:600;display:flex;align-items:center}
.fix .by{font-size:13px;line-height:19px;color:#5a5a5a}
.fix .ft{display:flex;justify-content:space-between;gap:10px;font-size:12px;font-weight:600;padding-top:8px;border-top:1px solid #f0ece5}
.oq{display:grid;grid-template-columns:52px 1fr auto;gap:14px;align-items:center;padding:14px 16px;border-radius:12px;background:#ffffff;border:1px solid #e6e1d8}
.oq .up{display:flex;flex-direction:column;align-items:center;font-size:15px;font-weight:700;color:#222222}
.ex{display:flex;align-items:center;gap:12px;padding:14px 16px;border-radius:12px;background:#ffffff;border:1px solid #e6e1d8}
.ex .av{width:44px;height:44px;border-radius:50%;background:#e8e2d6;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14px;flex-shrink:0}
'''
FIX_CARD='<div class="fix"><span style="display: flex; justify-content: space-between; gap: 8px; font-size: 13px;"><strong>{{x.b}}</strong><span style="color: #8a8a8a;">{{x.city}} · {{x.when}}</span></span><span style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #8a8a8a;">{{x.f}}</span><span class="old">AI said: {{x.old}}</span><span class="nw"><span class="mk mk-{{x.mk}}"></span>{{x.nw}}</span><span class="by">{{x.who}} {{x.how}}.</span><span class="ft"><span style="color: {{x.stc}};">{{x.st}}</span><span style="color: #8a8a8a;">{{x.ai}}</span></span></div>'
OQ='<div class="oq"><span class="up"><span style="font-size: 11px; color: #8a8a8a;">▲</span>{{x.up}}</span><span style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 15px;">{{x.q}}</strong><span style="font-size: 12px; color: #8a8a8a;">{{x.b}} · asked {{x.when}} · {{x.up}} people want to know</span></span><a href="Main.dc.html" class="btn b-sm" style="border-color: #d8d2c6;">Answer</a></div>'
EX='<div class="ex"><span class="av">{{x.i}}</span><span style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 15px;">{{x.n}}</strong><span style="font-size: 12px; color: #8a8a8a;">{{x.t}}</span><span style="font-size: 13px;">{{x.f}} facts added · {{x.w}} fixes AI now repeats</span></span></div>'
