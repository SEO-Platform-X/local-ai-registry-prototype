import sys; sys.path.insert(0,'/tmp/gen'); from common import *
TRI="url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 22 22'%3E%3Cpath d='M11 3.5L19.5 18.5H2.5Z' fill='none' stroke='%238a8a8a' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E\") center / 100% 100% no-repeat"
CSS=HNL_CSS+'''.wrapH{padding:32px 40px 60px;display:flex;flex-direction:column;gap:20px;max-width:1100px}
.flt{display:flex;gap:8px;flex-wrap:wrap}
.fb{display:inline-flex;align-items:center;height:34px;padding:0 14px;border-radius:17px;border:1px solid #dddddd;font-size:13px;font-weight:600;cursor:pointer;background:#ffffff}
.fb.on{background:#222222;border-color:#222222;color:#ffffff}
.lg{display:grid;grid-template-columns:130px 180px 1fr 230px;gap:16px;align-items:start;padding:14px 0;border-top:1px solid #efefef;font-size:14px}
.lg.hd{font-size:11px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#8a8a8a;padding:8px 0}
.lg .chg{display:flex;flex-direction:column;gap:3px}
.lg .chg s{color:#a0a0a0;font-size:13px}
.lg .who{display:flex;gap:8px;align-items:flex-start;font-size:13px;line-height:18px;color:#484848}
.mk{position:relative;display:inline-block;width:11px;height:11px;flex-shrink:0;margin-top:3px}
.mk::after{content:"";position:absolute;inset:0}
.mk-site::after{inset:2px;background:#008a05;border-radius:50%}
.mk-vis::after{inset:2px;border:1.6px solid #e8740c;border-radius:50%}
.mk-ai::after{inset:0;background:'''+TRI+'''}
'''
BODY=header(PUB_R)+'''<div class="wrapH"><a href="Main.dc.html" style="font-size: 13px; font-weight: 600; color: #484848;">← Lumen Aesthetics</a><div style="display: flex; flex-direction: column; gap: 4px;"><h1 style="margin: 0; font-size: 30px;">Change history</h1><span class="mu" style="font-size: 15px;">Every change to every fact on Lumen's page, newest first. Nothing is ever deleted.</span></div>
<div class="flt"><sc-for list="{{fl}}" as="f" hint-placeholder-count="7"><span class="fb {{f.on}}" onClick="{{f.pick}}">{{f.t}}</span></sc-for></div>
<div><div class="lg hd"><span>When</span><span>Fact</span><span>Change</span><span>Who, and how they know</span></div><sc-for list="{{rows}}" as="r" hint-placeholder-count="12"><div class="lg"><span class="mu" style="font-size: 13px;">{{r.d}}</span><strong>{{r.f}}</strong><span class="chg"><span>{{r.n}}</span><s style="display: {{r.od}};">{{r.o}}</s></span><span class="who"><span class="mk mk-{{r.m}}"></span><span>{{r.w}}<a href="#" style="display: {{r.ed}}; font-size: 12px; font-weight: 600;">{{r.e}}</a></span></span></div></sc-for></div></div>'''
JS=r'''    const S = this.state || {}; const f = S.f || 'All';
    const R = [
      ['Today', 'Hours', 'Monday hours', 'Closed', '9 AM to 6 PM', 'vis', 'Aisha M., visited on a Monday', 'Photo of the door sign'],
      ['Sep 26, 2026', 'Hours', 'Saturday, Oct 3', 'Closed for staff training', 'Open', 'site', 'Lumen, confirmed as the owner', ''],
      ['Sep 26, 2026', 'Team', 'Owner', 'Dr. Priya Nair, MD', '', 'site', 'Lumen claimed the page, verified by text code', ''],
      ['Sep 25, 2026', 'Prices', 'Botox', '$12 a unit', '$14 a unit', 'site', 'lumenaesthetics.com/pricing', 'Archived copy'],
      ['Sep 24, 2026', 'Locals', 'Parking tip', 'Level 3 of Structure B has the elevator', '', 'vis', 'Kelly W., goes every month', 'Thread 4821'],
      ['Sep 21, 2026', 'Hours', 'Monday hours', 'Closed', '9 AM to 6 PM', 'vis', 'Tom H., called', 'Call screenshot'],
      ['Sep 21, 2026', 'Services', 'Morpheus8 Body', 'Added, consults from Oct 1', '', 'site', "Lumen's Instagram post", 'Archived copy'],
      ['Sep 12, 2026', 'Services', 'HSA cards', 'Accepted', '', 'vis', 'Tom H., used his card', 'Thread 4702'],
      ['Aug 2, 2026', 'Hours', 'Monday hours', '9 AM to 6 PM', '', 'ai', 'What ChatGPT and Gemini said on this date', ''],
      ['Jul 14, 2026', 'Phone', 'Phone', '(949) 555-0148', '(949) 555-0199', 'site', 'Google Business Profile', 'Archived copy'],
      ['Jun 10, 2026', 'Hours', 'Weekday hours', '9 AM to 6 PM', '', 'site', 'Google Business Profile', 'Archived copy'],
      ['Mar 2, 2026', 'Page', 'Page created', 'Built from public sources', '', 'site', 'Local AI Registry', '']
    ];
    const F = ['All', 'Hours', 'Services', 'Prices', 'Team', 'Phone', 'Locals'];
    const fl = F.map(x => ({ t: x, on: x === f ? 'on' : '', pick: () => this.setState({ f: x }) }));
    const rows = R.filter(r => f === 'All' || r[1] === f).map(r => ({ d: r[0], f: r[2], n: r[3], o: r[4], od: r[4] ? 'inline' : 'none', m: r[5], w: r[6] + (r[7] ? ' · ' : ''), e: r[7], ed: r[7] ? 'inline' : 'none' }));
    return { fl, rows };'''
open(P+'History.dc.html','w').write(page('Change history, Lumen Aesthetics',CSS,BODY,JS)); print('ok')
