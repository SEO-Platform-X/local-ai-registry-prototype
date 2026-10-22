"""Mobile business profile board (M3), rebuilt to match the finalized desktop profile (Main).
Self-contained: writes docs/MProfile.html (standalone, not run through the brand layer) and
prototype/MProfile.dc.html. Run from the repo root: python3 generators/mobile/profile_v2.py"""
import os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

SK = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
def ic(p, s=22): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" {SK} aria-hidden="true">{p}</svg>'
I = dict(
 back='<path d="M15 5l-7 7 7 7"/>', share='<path d="M12 3v12M7 8l5-5 5 5"/><path d="M5 13v7h14v-7"/>',
 x='<path d="M6 6l12 12M18 6L6 18"/>', chev='<path d="M9 5l7 7-7 7"/>', down='<path d="M6 9l6 6 6-6"/>',
 lock='<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 info='<circle cx="12" cy="12" r="8"/><path d="M12 11v5M12 8h.01"/>', img='<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M21 16l-5-5-8 8"/>',
 flag='<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>', pencil='<path d="M4 20h4L20 8l-4-4L4 16z"/>',
 tag='<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8" r="1.4"/>', plus='<path d="M12 5v14M5 12h14"/>',
 pin='<path d="M12 21s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 phone='<path d="M5 4h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 globe='<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
 clock='<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>', syringe='<path d="M18 3l3 3M16 5l3 3M17 6L8 15l-3 1 1-3 9-9zM6 15l-3 3"/>',
 lips='<path d="M3 12c3-4 6-5 9-3 3-2 6-1 9 3-3 4-6 5-9 5s-6-1-9-5z"/><path d="M3 12h18"/>',
 drop='<path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/>', waves='<path d="M3 8c3-2 6 2 9 0s6 2 9 0M3 13c3-2 6 2 9 0s6 2 9 0M3 18c3-2 6 2 9 0s6 2 9 0"/>',
 chat='<path d="M4 5h16v11H9l-5 4z"/>',
)
PH = {
 'Treatment room': 'https://images.unsplash.com/photo-1761819922656-d1b77eef49c0?fm=jpg&q=70&w=900&auto=format&fit=crop',
 'Dr. Nair, consult': 'https://images.unsplash.com/photo-1785861001619-b263ebd4e615?fm=jpg&q=70&w=900&auto=format&fit=crop',
 'Results wall': 'https://images.unsplash.com/photo-1595871151608-bc7abd1caca3?fm=jpg&q=70&w=900&auto=format&fit=crop',
 'Front desk': 'https://images.unsplash.com/photo-1731514693674-a32211b63996?fm=jpg&q=70&w=900&auto=format&fit=crop',
 'Storefront': 'https://images.unsplash.com/photo-1788781537938-e96aea5838d3?fm=jpg&q=70&w=900&auto=format&fit=crop',
}
def photo(label, style='', extra=''):
    return f'<div class="pho" style="background-image:url(\'{PH[label]}\');{style}"><span class="cap">[{label}]</span>{extra}</div>'
LAUREL = '<svg width="16" height="34" viewBox="0 0 22 46" aria-hidden="true"><g {T} fill="#0f1a33"><path d="M18 44C9 38 5 27 8 10" fill="none" stroke="#0f1a33" stroke-width="1.8" stroke-linecap="round"/><ellipse cx="8" cy="39" rx="5.5" ry="2.4" transform="rotate(35 8 39)"/><ellipse cx="5" cy="31" rx="5.5" ry="2.4" transform="rotate(60 5 31)"/><ellipse cx="4.5" cy="23" rx="5.5" ry="2.4" transform="rotate(80 4.5 23)"/><ellipse cx="6" cy="15" rx="5" ry="2.2" transform="rotate(100 6 15)"/><ellipse cx="10" cy="8" rx="4.5" ry="2" transform="rotate(120 10 8)"/><ellipse cx="13.5" cy="33" rx="4.5" ry="2" transform="rotate(-25 13.5 33)"/><ellipse cx="12" cy="24" rx="4.5" ry="2" transform="rotate(-45 12 24)"/></g></svg>'
def laurel(): return LAUREL.replace('{T}', '') + '<b>AI<br>Score</b>' + LAUREL.replace('{T}', 'transform="translate(22 0) scale(-1 1)"')
MK = {'c': '<i class="mk c" title="Confirmed"></i>', 'v': '<i class="mk v" title="Visitor submitted"></i>', 'a': '<i class="mk a" title="AI guess"></i>', '': ''}

CSS = r'''
@import url("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Hanken+Grotesk:wght@400;500;600;700&display=swap");
:root{--paper:#f4efe6;--peach:#f5dfc8;--navy:#0f1a33;--ink2:#4a5570;--ink3:#7d8599;--coral:#ef5b3c;--blue:#2b59d9;--green:#2f6b3a;--orange:#e8740c;--line:rgba(15,26,51,0.12);--glass:rgba(250,246,238,0.78);--edge:rgba(255,255,255,0.75)}
body{margin:0;color:var(--navy);font-family:"Hanken Grotesk","Helvetica Neue",Arial,sans-serif;-webkit-font-smoothing:antialiased}
.S{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;letter-spacing:-0.01em}
.mb{position:relative;z-index:1;display:flex;flex-direction:column;padding:44px 48px 64px;gap:30px;box-sizing:border-box}
.mb-h{display:flex;align-items:baseline;gap:22px}.mb-h h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:52px;letter-spacing:-0.01em}.mb-h p{margin:0;font-size:15px;line-height:22px;color:var(--ink2);max-width:880px}
.mrow{display:flex;gap:44px;align-items:flex-start}
.ph{display:flex;flex-direction:column;gap:12px;width:390px;flex-shrink:0}
.ph-l{display:flex;flex-direction:column;gap:3px;min-height:74px}.ph-l b{font-size:14px}.ph-l span{font-size:12.5px;line-height:18px;color:var(--ink2)}
.scr{width:390px;height:844px;border-radius:46px;background:var(--paper);box-shadow:0 0 0 10px var(--navy),0 30px 60px rgba(15,26,51,0.28);overflow:hidden;position:relative;display:flex;flex-direction:column;font-size:15px;line-height:22px}
.scr a{color:inherit;text-decoration:none}
.sb{height:47px;flex-shrink:0;display:flex;align-items:center;justify-content:space-between;padding:0 30px 0 36px;font-size:16px;font-weight:600;box-sizing:border-box;position:relative;z-index:6}
.sb i{font-style:normal;display:flex;gap:6px;align-items:center;letter-spacing:1px}.sb s{display:block;width:26px;height:12px;border-radius:3px;border:1.5px solid currentColor;box-sizing:border-box;position:relative}.sb s::after{content:"";position:absolute;inset:1.5px 5px 1.5px 1.5px;background:currentColor;border-radius:1px}
.sb.dk{color:#fff}
.hi{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);width:134px;height:5px;border-radius:3px;background:var(--navy);z-index:20}
.bd{flex:1;min-height:0;overflow:hidden;display:flex;flex-direction:column;padding:0 20px;gap:14px;box-sizing:border-box}
/* photos */
.pho{position:relative;background-color:#8796b0;background-size:cover;background-position:center;background-blend-mode:luminosity;overflow:hidden}
.pho::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,26,51,0.05),rgba(15,26,51,0.32))}
.pho > *{position:relative;z-index:1}
.pho .cap{display:none;position:absolute;right:12px;top:12px;font-size:11px;font-weight:700;color:var(--navy);background:rgba(244,239,230,0.8);padding:1px 6px;border-radius:4px}
.nocode{position:absolute;left:12px;top:12px;display:inline-flex;align-items:center;gap:5px;height:26px;padding:0 10px;border-radius:999px;background:rgba(15,26,51,0.78);color:#fff;font-size:12px;font-weight:600}
.glassbtn{display:inline-flex;align-items:center;gap:7px;height:36px;padding:0 14px;border-radius:14px;background:rgba(246,241,232,0.94);color:var(--navy);font-size:13.5px;font-weight:600;box-shadow:0 6px 18px -8px rgba(15,26,51,0.5)}
.icb{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:var(--navy)}
.icb.g{background:rgba(246,241,232,0.94);box-shadow:0 4px 14px -6px rgba(15,26,51,0.5)}
/* type */
.crumb{font-size:13px;color:var(--ink2)}.crumb a{text-decoration:underline;text-decoration-color:rgba(239,91,60,0.5);text-underline-offset:3px}.crumb b{color:var(--navy);font-weight:600}
.name{margin:0;font-size:44px;line-height:44px}
.unc{display:inline-flex;align-items:center;height:28px;padding:0 11px;border-radius:999px;border:1px solid rgba(239,91,60,0.35);background:#f6f1e8;color:var(--coral);font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-weight:600;font-size:17px;vertical-align:8px;margin-left:6px}
.sub{font-size:13px;line-height:19px;color:var(--ink2)}
.mu{color:var(--ink2)}
.mk{display:inline-block;width:8px;height:8px;margin-left:6px;vertical-align:1px;flex-shrink:0}.mk.c{background:#1f8a2e;border-radius:50%}.mk.v{border:1.6px solid var(--orange);border-radius:50%;box-sizing:border-box}
.mk.a{width:0;height:0;border-left:5px solid transparent;border-right:5px solid transparent;border-bottom:9px solid #9097a6;position:relative}
.legend{display:flex;gap:16px;font-size:12.5px;color:var(--ink2)}.legend .mk{margin:0 5px 0 0}
/* glass card */
.gl{background:var(--glass);border:1px solid var(--edge);border-radius:24px;box-shadow:0 1px 0 rgba(255,255,255,0.9) inset,0 24px 50px -30px rgba(15,26,51,0.3)}
/* AI score */
.ai{background:rgba(245,223,200,0.85);border-radius:24px;padding:16px 0 14px;display:flex;flex-direction:column;gap:12px;box-shadow:0 24px 50px -30px rgba(15,26,51,0.35)}
.ai-h{display:flex;align-items:center;gap:12px;padding:0 18px}
.ai-b{display:flex;align-items:center;gap:1px;flex-shrink:0}.ai-b b{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-weight:600;font-size:17px;line-height:16px;text-align:center}
.ai-h .t{font-size:15px;font-weight:600;line-height:20px}
.ai-s{display:flex;gap:0;overflow:hidden;padding:0 18px;-webkit-mask-image:linear-gradient(90deg,#000 82%,transparent);mask-image:linear-gradient(90deg,#000 82%,transparent)}
.st{display:flex;flex-direction:column;gap:4px;padding:0 16px;border-left:1px solid rgba(15,26,51,0.16);flex-shrink:0;min-width:84px}.st:first-child{padding-left:0;border-left:0}
.st .v{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:38px;line-height:40px;white-space:nowrap}.st .v.r{color:#c13515}
.st .x{height:22px;display:flex;align-items:flex-end}
.st .l{font-size:12.5px;line-height:16px;color:var(--ink2);white-space:nowrap}
.segb{display:grid;grid-template-columns:repeat(11,5px);gap:2px}.segb i{height:8px;background:rgba(15,26,51,0.22);border-radius:1px}
.srow{display:flex;flex-direction:column;gap:2px;width:64px}.srow i{display:block;height:2px;background:var(--navy)}.srow i.o{background:rgba(15,26,51,0.25)}
.ghg{display:grid;grid-template-columns:repeat(14,4px);gap:1.5px}.ghg i{height:4px;background:rgba(15,26,51,0.2)}
.spk{display:flex;align-items:flex-end;gap:3px}.spk i{width:5px;background:rgba(15,26,51,0.25);border-radius:1px}.spk i.on{background:#1f8a2e}
a.ai{color:inherit}
.ai-top{display:flex;align-items:center;gap:14px;padding:0 18px}.ai-top .big{font-family:"Cormorant Garamond",Georgia,serif;font-size:56px;line-height:52px;color:#c13515}.ai-top .l{font-size:12.5px;color:var(--ink2)}
.grid{display:grid;grid-template-columns:1fr 1fr;margin:0 18px;border-top:1px solid rgba(15,26,51,0.14)}
.gc{display:flex;flex-direction:column;gap:3px;padding:10px 0 8px}.gc:nth-child(odd){padding-right:12px;border-right:1px solid rgba(15,26,51,0.14)}.gc:nth-child(even){padding-left:14px}.gc:nth-child(n+3){border-top:1px solid rgba(15,26,51,0.14)}
.gc .v{font-family:"Cormorant Garamond",Georgia,serif;font-size:30px;line-height:32px;white-space:nowrap}.gc .x{height:18px;display:flex;align-items:flex-end}.gc .l{font-size:12px;line-height:15px;color:var(--ink2);white-space:nowrap}
.ai .more{display:flex;align-items:center;justify-content:space-between;margin:0 18px;padding-top:10px;border-top:1px solid rgba(15,26,51,0.14);font-size:14px;font-weight:600}
.dotg{display:inline-block;width:8px;height:8px;border-radius:50%;background:#1f8a2e;margin-right:8px;vertical-align:middle;box-shadow:0 0 0 4px rgba(31,138,46,0.18)}
/* owner */
.own{display:flex;align-items:center;gap:12px}
.ava{width:42px;height:42px;border-radius:50%;background:#c9d3cf;display:flex;align-items:center;justify-content:center;font-size:10px;color:var(--ink2);flex-shrink:0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:40px;padding:0 14px;border-radius:14px;background:#f6f1e8;border:1px solid var(--line);font-size:14px;font-weight:600;white-space:nowrap;color:var(--navy)}
.bp{display:flex;align-items:center;justify-content:center;gap:10px;height:52px;border-radius:16px;background:var(--navy);color:#fff !important;font-size:16px;font-weight:600;box-shadow:0 14px 30px -14px rgba(15,26,51,0.6);white-space:nowrap}
.bp::after{content:"⟶";font-weight:400}
.bp.nx::after{content:none}
/* cashback */
.cb{display:flex;align-items:center;gap:10px}.cb .ti{width:28px;height:28px;border-radius:50%;background:var(--coral);color:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cb b{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-weight:600;color:var(--coral);font-size:19px;line-height:21px}
.cbc{background:var(--peach);border-radius:18px;padding:13px 16px}
/* sticky bars */
.top{flex-shrink:0;background:rgba(244,239,230,0.97);box-shadow:0 1px 0 var(--line);position:relative;z-index:4}
.ab{height:52px;display:flex;align-items:center;gap:6px;padding:0 10px}
.ab .t{flex:1;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:24px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-align:center}
.tabs{display:flex;gap:20px;padding:0 20px;overflow:hidden;white-space:nowrap}
.tabs span{display:flex;align-items:baseline;gap:4px;height:44px;align-items:center;font-family:"Cormorant Garamond",Georgia,serif;font-size:20px;color:var(--ink2);flex-shrink:0}
.tabs span sup{font-family:"Hanken Grotesk",sans-serif;font-size:11px;font-weight:700;color:var(--ink2);vertical-align:6px}
.tabs span.on{color:var(--navy);box-shadow:inset 0 -2px 0 var(--coral)}
.bar{position:absolute;left:0;right:0;bottom:0;z-index:8;padding:12px 18px 30px;background:rgba(244,239,230,0.97);box-shadow:0 -1px 0 var(--line);display:flex;align-items:center;gap:12px}
.bar .cb{flex:1;min-width:0}.bar .cb b{font-size:17px;white-space:nowrap}
.bar .bp{padding:0 18px;height:50px;font-size:15.5px}
/* sections */
.h2{margin:0;font-size:32px;line-height:34px}
.h3{margin:0;font-size:24px;line-height:28px}
.hrow{display:flex;align-items:baseline;justify-content:space-between;gap:10px}
/* locals */
.comp{display:flex;gap:8px;align-items:center}
.inp{flex:1;height:46px;border-radius:16px;background:#f6f1e8;border:1px solid var(--line);display:flex;align-items:center;padding:0 14px;font-family:"Cormorant Garamond",Georgia,serif;font-size:18px;color:var(--ink3);box-sizing:border-box;white-space:nowrap;overflow:hidden}
.inp.f{border:2px solid var(--navy);color:var(--navy)}
.chips{display:flex;gap:8px;flex-shrink:0;overflow:hidden}
.chip{display:inline-flex;align-items:center;gap:5px;height:34px;padding:0 13px;border-radius:999px;background:#f6f1e8;border:1px solid var(--line);font-size:13.5px;font-weight:600;white-space:nowrap;flex-shrink:0}
.chip.on{background:var(--navy);border-color:var(--navy);color:#fff}
.chip em{font-style:normal;font-weight:500;opacity:0.65}
.sort{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--ink2)}.sort span.sel{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 10px 0 12px;border-radius:12px;background:#f6f1e8;border:1px solid var(--line);font-family:"Cormorant Garamond",Georgia,serif;font-size:17px;color:var(--navy)}
.post{display:flex;gap:10px;padding:14px 0;border-top:1px solid var(--line)}
.vote{display:flex;flex-direction:column;align-items:center;width:26px;flex-shrink:0;font-size:12.5px;font-weight:700;color:var(--ink2);line-height:15px;padding-top:4px}.vote i{font-style:normal;font-size:10px;color:var(--ink3)}
.post .g{flex:1;min-width:0;display:flex;flex-direction:column;gap:3px}
.post .pt{font-family:"Cormorant Garamond",Georgia,serif;font-weight:600;font-size:22px;line-height:24px;letter-spacing:-0.005em}
.meta{font-size:12.5px;line-height:18px;color:var(--ink2)}.meta a{color:var(--navy)}
.kd{font-size:10.5px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;margin-right:6px}.kd.q{color:var(--blue)}.kd.t{color:var(--green)}.kd.h{color:var(--navy)}
.acts{display:flex;gap:12px;font-size:12px;color:var(--ink2)}.acts b{color:#c13515;font-weight:600}
/* services */
.kf{display:flex;gap:10px;overflow:hidden;flex-shrink:0}
.kfc{width:150px;flex-shrink:0;border-radius:20px;overflow:hidden;background:var(--glass);border:1px solid var(--edge);box-shadow:0 18px 40px -28px rgba(15,26,51,0.35)}
.kfc .pho{height:84px}.kfc .pho .cap{display:none}
.kfc div.t{padding:9px 12px 11px;display:flex;flex-direction:column;gap:1px}
.kfc b{font-size:14.5px}.kfc span{font-size:12px;color:var(--ink2)}
.menu .it{display:flex;gap:12px;padding:12px 0;border-top:1px solid var(--line);align-items:flex-start}
.menu .it svg{flex-shrink:0;margin-top:1px}
.menu .it .g{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}
.menu .it b{font-size:15px;line-height:20px}.menu .it .d{font-size:13px;line-height:18px;color:var(--ink2)}
.menu .it .p{font-weight:700;font-size:14px;white-space:nowrap;text-align:right}
/* visit */
.wv{padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.lbl{font-size:11px;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:var(--ink2)}
.qn{font-size:12px;font-weight:600;color:var(--green);letter-spacing:0;text-transform:none;margin-left:8px}
.hm{display:grid;grid-template-columns:38px repeat(7,1fr);gap:2px;font-size:10.5px;color:var(--ink2)}
.hm span{display:flex;align-items:center}.hm span.dy{justify-content:center;font-weight:600;color:var(--navy);height:16px}
.hm i{height:12px;border-radius:2px}.hm > span:not(.dy){height:12px;font-size:10px}
.fact{padding:14px 16px;display:flex;flex-direction:column;gap:4px}
.fact b{font-size:15.5px;line-height:21px}
.fr{display:flex;align-items:flex-start;gap:10px;padding:11px 0;border-top:1px solid var(--line);font-size:14px}.fr:first-child{border-top:0}
.fr .k{width:86px;flex-shrink:0;color:var(--ink2);display:flex;gap:7px;align-items:center}.fr .v{flex:1;text-align:right;font-weight:500}
/* updates */
.up{display:flex;flex-direction:column;gap:8px;padding:14px 0;border-top:1px solid var(--line)}
.up .who{display:flex;align-items:center;gap:10px}.up .who .l{width:32px;height:32px;border-radius:50%;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px}
.up .who b{font-size:14px;display:block;line-height:18px}.up .who span{font-size:12px;color:var(--ink2)}
.up p{margin:0;font-size:15px;line-height:21px}
.up .pho{height:150px;border-radius:16px}
.cm{display:flex;gap:8px;font-size:13.5px;padding-left:10px;border-left:2px solid rgba(239,91,60,0.45)}.cm b{font-weight:700}
/* sheets */
.scrim{position:absolute;inset:0;background:rgba(15,26,51,0.42);z-index:9}
.sheet{position:absolute;left:0;right:0;bottom:0;z-index:10;background:#f6f1e8;border-radius:26px 26px 0 0;box-shadow:0 -12px 40px rgba(15,26,51,0.25);padding:10px 20px 38px;display:flex;flex-direction:column;gap:14px;box-sizing:border-box}
.sheet .gr{width:40px;height:5px;border-radius:3px;background:rgba(15,26,51,0.2);align-self:center}
.sheet .sh{display:flex;align-items:center;justify-content:space-between}
.sheet .sh b{font-size:20px}
.sl{font-size:14px;font-weight:700;margin-bottom:-6px}
.seg{display:flex;padding:4px;border-radius:16px;background:#e9e2d5;gap:4px}.seg span{flex:1;height:38px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:14.5px;font-weight:600}.seg span.on{background:var(--navy);color:#fff}
.bk{border:1px solid rgba(15,26,51,0.25);border-radius:14px;overflow:hidden;background:#fbf8f3}
.bk .rw{display:flex}.bk .rw + .rw{border-top:1px solid rgba(15,26,51,0.25)}
.bk .c{flex:1;padding:10px 12px;display:flex;flex-direction:column}.bk .c + .c{border-left:1px solid rgba(15,26,51,0.25)}
.bk .c small{font-size:10.5px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase}.bk .c span{font-size:15px}
.note{font-size:13px;color:var(--ink2);text-align:center}
.bin{height:50px;border-radius:14px;background:#fbf8f3;border:1px solid var(--line);display:flex;align-items:center;padding:0 14px;font-size:15px;box-sizing:border-box}.bin.f{border:2px solid var(--navy)}
/* bottom of page */
.pal .r{display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1px solid var(--line)}.pal .r:first-of-type{border-top:0}
.pal .r.me{background:rgba(239,91,60,0.07);margin:0 -10px;padding:10px;border-radius:12px}
.pal .lg{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}
.pal .g{flex:1;min-width:0}.pal .g b{font-size:14.5px;display:block;line-height:19px}.pal .g span{font-size:12px;color:var(--ink2)}
.pal .sc{display:flex;align-items:center;gap:8px;font-weight:700;font-size:16px}.pal .sc i{width:40px;height:5px;border-radius:3px;background:rgba(15,26,51,0.12);position:relative;overflow:hidden}.pal .sc i u{position:absolute;left:0;top:0;bottom:0}
.refs .rf{display:flex;gap:8px;padding:9px 0;border-top:1px solid var(--line);font-size:12.5px;line-height:17px}.refs .rf .n{color:var(--ink3);width:22px;flex-shrink:0}
.refs .rf .k{font-size:10px;font-weight:700;letter-spacing:0.12em;color:var(--ink2);margin-right:4px}
.tg{display:flex;gap:18px;font-family:"Cormorant Garamond",Georgia,serif;font-size:20px}.tg span{color:var(--ink2)}.tg span.on{color:var(--navy);box-shadow:inset 0 -2px 0 var(--coral)}
.acc{display:block;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:12px 0}.acc + .acc{border-top:0}
.acc summary{list-style:none;display:flex;align-items:center;cursor:pointer}.acc summary::-webkit-details-marker{display:none}
.acc[open] summary svg{transform:rotate(180deg)}
.refbox{display:flex;flex-direction:column;gap:8px}
.more-refs summary{list-style:none;cursor:pointer;display:flex;flex-direction:column}.more-refs summary::-webkit-details-marker{display:none}
.more-refs .peek{display:block;max-height:40px;overflow:hidden;-webkit-mask-image:linear-gradient(180deg,#000 10%,transparent);mask-image:linear-gradient(180deg,#000 10%,transparent)}
.more-refs .showall{display:flex;align-items:center;justify-content:center;gap:6px;height:44px;border-radius:14px;background:#f6f1e8;border:1px solid rgba(15,26,51,0.22);font-size:14.5px;font-weight:600;margin-top:2px}
.more-refs[open] .peek{max-height:none;-webkit-mask-image:none;mask-image:none}.more-refs[open] .showall{display:none}
.sig{display:flex;flex-direction:column}.sg{display:grid;grid-template-columns:1fr 92px 28px;gap:10px;align-items:center;padding:7px 0;border-top:1px solid var(--line);font-size:13.5px}.sg:first-child{border-top:0}
.sg .nm em{font-style:normal;font-size:11px;font-weight:700;color:var(--ink3);margin-left:6px}.sg b{text-align:right;font-size:14px}
.br{display:block;height:6px;border-radius:3px;background:rgba(15,26,51,0.1);position:relative;overflow:hidden}.br u{position:absolute;left:0;top:0;bottom:0;border-radius:3px;background:#0f1a33}
.eng{display:flex;flex-direction:column}.er{display:grid;grid-template-columns:132px 1fr 38px;gap:10px;align-items:center;padding:6px 0;font-size:13.5px}.er b{text-align:right}
.pdots{display:grid;grid-template-columns:repeat(11,1fr);gap:5px}.pdots i{height:18px;border-radius:5px;background:rgba(15,26,51,0.12)}.pdots i.on{background:#c13515}
.pq{display:flex;flex-direction:column;gap:4px;padding:10px 0;border-top:1px solid var(--line)}
.ok{font-size:12px;font-weight:700;color:#2f6b3a;background:rgba(47,107,58,0.1);padding:2px 8px;border-radius:999px}.no{font-size:12px;font-weight:700;color:#c13515;background:rgba(193,53,21,0.08);padding:2px 8px;border-radius:999px}
.bub{background:#fbf8f3;border:1px solid var(--line);border-radius:18px 18px 18px 4px;padding:12px 14px;font-size:14px;line-height:20px}.bub .who{display:block;font-size:11px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink2);margin-bottom:4px}
.bub mark{background:rgba(239,91,60,0.16);color:#a3270f;text-decoration:underline;text-decoration-color:#c13515;text-underline-offset:3px}
.fc{display:flex;flex-direction:column;gap:2px;padding:8px 0;border-top:1px solid var(--line)}.fc .f{font-size:12px;font-weight:700;color:var(--ink2)}.fc .row{display:flex;justify-content:space-between;gap:10px;font-size:13.5px}
.fc .fa{color:var(--navy)}.fc .fa.bad{color:#a3270f;text-decoration:line-through;text-decoration-color:rgba(193,53,21,0.6)}.fc .rc{text-align:right;font-weight:600}
.ddots{display:grid;grid-template-columns:repeat(20,1fr);gap:4px}.ddots i{height:12px;border-radius:3px;background:rgba(15,26,51,0.12)}.ddots i.on{background:#0f1a33}.ddots i.bad{background:#c13515}
.sw{display:inline-block;width:9px;height:9px;border-radius:2px;margin:0 5px 0 8px;vertical-align:0}
.sov{display:flex;height:14px;border-radius:7px;overflow:hidden;gap:2px}.sov u{display:block}
.sovl{display:flex;flex-wrap:wrap;gap:4px 6px;font-size:12.5px;color:var(--ink2)}.sovl .sw{margin-left:0}
.ed{padding:14px 16px;display:flex;flex-direction:column;gap:6px;border-radius:18px}
.kt{display:grid;grid-template-columns:70px 1fr;font-size:13px}.kt span{padding:5px 0;border-top:1px solid var(--line)}.kt span:nth-child(odd){color:var(--ink2)}
/* history */
.hs{display:flex;gap:10px;padding:12px 0;border-top:1px solid var(--line)}
.hs .mk{margin:6px 0 0}
.hs .g{flex:1;display:flex;flex-direction:column;gap:1px}.hs .g b{font-size:15px}.hs .g s{color:var(--ink3);font-size:13px}.hs .g .w{font-size:12.5px;color:var(--ink2)}
.hs .d{font-size:12px;color:var(--ink2);white-space:nowrap}
/* photos grid */
.pg{display:grid;grid-template-columns:repeat(3,1fr);gap:3px}.pg .pho{height:124px}.pg .pho .cap{display:none}
'''

def sb(dark=False): return f'<div class="sb{" dk" if dark else ""}"><span>9:41</span><i>●●● <s></s></i></div>'
def scr(label, note, inner, dark=False):
    return f'<div class="ph"><div class="ph-l"><b>{label}</b><span>{note}</span></div><div class="scr">{inner}<div class="hi"></div></div></div>'
TABS = [('Locals', '22'), ('Services', '34'), ('Team', '14'), ('Visit', ''), ('Reputation', '612'), ('Updates', '9'), ('AI', '')]
def tabs(on, shift=0):
    out = ''
    for t, n in TABS:
        lab = t
        out += f'<span class="{"on" if t == on else ""}">{lab}{f"<sup>{n}</sup>" if n else ""}</span>'
    return f'<div class="tabs" style="margin-left:-{shift}px">{out}</div>'
def topbar(on, shift=0):
    return f'<div class="top">{sb()}<div class="ab"><a class="icb" href="Explore.html">{ic(I["back"])}</a><span class="t">Lumen Aesthetics</span><a class="icb" href="#">{ic(I["share"], 20)}</a></div>{tabs(on, shift)}</div>'
CASH = f'<span class="cb"><span class="ti">{ic(I["tag"], 15)}</span><b>Eligible for 20% cashback</b></span>'
BAR = f'<div class="bar"><span class="cb"><span class="ti">{ic(I["tag"], 15)}</span><span style="display:flex;flex-direction:column"><span style="font-size:12px;line-height:14px;color:var(--ink2)">Eligible for</span><b>20% cashback</b></span></span><a class="bp" href="Book.html">Request a booking</a></div>'

def stat(v, x, l, cls=''):
    return f'<div class="st"><span class="v {cls}">{v}</span><span class="x">{x}</span><span class="l">{l}</span></div>'
def cell(v, x, l):
    return f'<div class="gc"><span class="v">{v}</span><span class="x">{x}</span><span class="l">{l}</span></div>'
AISCORE = (f'<a class="ai" href="#ai"><div class="ai-h"><span class="ai-b">{laurel()}</span><span style="display:flex;flex-direction:column"><span class="t">AI names Lumen less than most Irvine med spas</span><span class="sub">Scored from 8 signals across search and AI.</span></span></div>'
  '<div class="ai-top"><span class="big">58</span><span style="flex:1;display:flex;flex-direction:column;gap:4px">'
  '<svg width="100%" height="22" viewBox="0 0 200 22" preserveAspectRatio="none"><rect x="0" y="9" width="200" height="4" rx="2" fill="rgba(15,26,51,0.14)"/><rect x="0" y="9" width="116" height="4" rx="2" fill="#c13515"/><line x1="142" y1="3" x2="142" y2="19" stroke="#0f1a33" stroke-width="2"/></svg>'
  f'<span class="l">Lumen 58 · Irvine avg 71{MK["c"]}</span></span></div>'
  '<div class="grid">'
  + cell('<span style="color:#c13515">0</span>', '<span class="segb">' + '<i></i>' * 22 + '</span>', 'answered of 22')
  + cell('78%', '<span class="srow"><i></i><i></i><i></i><i></i><i class="o"></i></span>', 'would go back' + MK['c'])
  + cell('0', '<span class="ghg">' + '<i></i>' * 42 + '</span>', 'updates, last 30 days' + MK['c'])
  + cell('<span class="dotg"></span>Quiet', '<span class="spk">' + ''.join(f'<i class="{"on" if k==1 else ""}" style="height:{h}px"></i>' for k, h in enumerate([5, 8, 14, 18, 16, 13, 10, 12, 9])) + '</span>', 'right now' + MK['c'])
  + f'</div><span class="more">See how the score works{ic(I["chev"], 16)}</span></a>')
OWNER = (f'<div class="own"><span class="ava">[Photo]</span><span style="flex:1;min-width:0;display:flex;flex-direction:column"><b style="font-size:14px;white-space:nowrap">Owned by Dr. Priya Nair, MD{MK["a"]}</b>'
         f'<span class="sub" style="white-space:nowrap;font-size:12.5px"><b style="color:var(--navy)">Unclaimed · Never replied</b> · 10 yrs{MK["a"]}</span></span><a class="btn" href="Claim.html" style="height:34px;padding:0 10px;font-size:13px">Claim it</a></div>')
LEGEND = f'<div class="legend"><span><i class="mk c"></i>Confirmed</span><span><i class="mk v"></i>Visitor submitted</span><span><i class="mk a" style="margin-right:5px"></i>AI guess</span></div>'

# 1. Profile, top
gallery = (f'<div style="position:relative;height:300px;flex-shrink:0;margin-top:-47px">'
  + photo('Treatment room', 'position:absolute;inset:0;', f'<span class="nocode" style="top:106px;left:14px">{ic(I["info"], 13)}No code detected</span>')
  + f'<div style="position:absolute;top:53px;left:14px;right:14px;display:flex;justify-content:space-between;z-index:2"><a class="icb g" href="Explore.html">{ic(I["back"])}</a><a class="icb g" href="#">{ic(I["share"], 19)}</a></div>'
  + f'<div style="position:absolute;left:14px;right:14px;bottom:14px;display:flex;justify-content:space-between;align-items:center;z-index:2"><span class="glassbtn">{ic(I["lock"], 15)}Add media AI can read</span><a class="glassbtn" href="Photos.html">{ic(I["img"], 15)}1 / 51</a></div></div>')
p_top = (f'<div class="sb dk">{sb(True)[19:-6]}</div>' if False else sb(True)) + gallery + (
  '<div class="bd" style="padding-top:16px;gap:10px">'
  '<span class="crumb"><a href="Explore.html">Irvine, CA</a> › <a href="Explore.html">Med spas</a></span>'
  '<h1 class="name S">Lumen Aesthetics</h1><span><span class="unc" style="margin:0;vertical-align:0">Unclaimed</span></span>'
  '<div style="display:flex;flex-direction:column;gap:2px"><b style="font-size:16px">Med spa at Irvine Spectrum, Irvine, CA</b>'
  f'<span style="font-size:14px">★ 4.9 · 612 reviews{MK["c"]} · Open today until 7 PM{MK["c"]}</span></div>'
  '<p style="margin:0;font-size:14.5px;line-height:21px">Lumen Aesthetics is a physician-led med spa at the Irvine Spectrum Center, offering Botox, dermal filler, lip filler, Sculptra… <u style="font-weight:600;text-underline-offset:3px">More</u></p>'
  + AISCORE + '</div>' + BAR)
# 1 needs the dark status bar to sit over the photo
p_top = p_top.replace('<div class="sb dk">', '<div class="sb dk" style="background:transparent">', 1)

# 2. Profile, scrolling
p_scroll = sb() + ('<div class="bd" style="gap:14px;padding-top:6px">'
  + AISCORE + OWNER + LEGEND +
  '<span class="sub" style="padding-top:2px;border-top:1px solid var(--line);padding-top:12px">AI checked this page at 6:10 AM today. Last activity 3 hours ago, a question from ella_v_irvine.</span>'
  + f'<div style="margin:2px -20px 0;box-shadow:0 -1px 0 var(--line), 0 1px 0 var(--line)">{tabs("Locals")}</div>'
  + '<div class="hrow"><h2 class="h2 S">Locals</h2><span class="sub"><b style="color:var(--navy)">18</b> asked · <b style="color:var(--navy)">0</b> answered by Lumen</span></div>'
  + '<div class="comp"><span class="inp">Ask, share a tip, or a heads-up</span><a class="bp nx" style="height:46px;padding:0 16px;font-size:15px">Post</a></div>'
  + '</div>' + BAR)

def post(v, t, kind, who, n, need=False):
    k = {'Question': 'q', 'Tip': 't', 'Heads-up': 'h'}[kind]
    return (f'<div class="post"><div class="vote"><i>▲</i>{v}<i>▼</i></div><div class="g"><span class="pt">{t}</span>'
            f'<span class="meta"><span class="kd {k}">{kind}</span>by <a>{who}</a></span>'
            f'<span class="acts"><span>{n} comments</span>{"<b>Needs an answer</b>" if need else ""}<span>share</span></span></div></div>')
# 3. Locals
p_locals = topbar('Locals') + ('<div class="bd" style="padding-top:14px;gap:10px">'
  '<div class="comp"><span class="inp">Ask, share a tip, or a heads-up</span><a class="bp nx" style="height:46px;padding:0 16px;font-size:15px">Post</a></div>'
  '<div style="display:flex;justify-content:space-between;align-items:center"><div class="chips"><span class="chip">? Question</span><span class="chip">✦ Tip</span><span class="chip">! Heads-up</span></div>'
  f'<span class="sort"><span class="sel">Hot {ic(I["down"], 14)}</span></span></div>'
  '<div style="margin-top:2px">'
  + post(26, 'Closed Saturday, Oct 3 for staff training. Google still shows them open.', 'Heads-up', 'kellyw_irvine · 3h · researching', 4, True)
  + post(4, 'Is there a wait list for Morpheus8 Body?', 'Question', 'ella_v_irvine · 3h · comparing', 3, True)
  + post(31, 'Park on level 3 of Structure B. It is the only level with an elevator straight to the second floor.', 'Tip', 'kellyw_irvine · 2d · going', 3)
  + post(15, 'Is the first consult free?', 'Question', 'quiet_quail_22 · 1d · went', 9)
  + '</div></div>' + BAR)

# 4. Services
def mi(icon, n, mk, cat, desc, price, pmk):
    return (f'<div class="it">{ic(I[icon], 20)}<div class="g"><b>{n}{MK[mk]}</b><span class="d">{cat} · {desc}</span></div><span class="p">{price}{MK[pmk]}</span></div>')
p_svc = topbar('Services') + ('<div class="bd" style="padding-top:14px;gap:12px">'
  '<div><h2 class="h2 S">Services</h2><span class="sub">What Lumen offers, what it costs, and what people come for.</span></div>'
  '<h3 class="h3 S">Known for</h3>'
  '<div class="kf">'
  + ''.join(f'<div class="kfc">{photo(ph)}<div class="t"><b>{n}</b><span>{pct} of reviews</span><span>{pr}{MK["a"]}</span></div></div>' for n, ph, pct, pr in [
      ('Dermal filler', 'Results wall', '41%', '$780 a syringe'), ('Botox', 'Treatment room', '29%', '$12 a unit'), ('Lip filler', 'Dr. Nair, consult', '9%', '$780 a syringe')])
  + '</div>'
  '<div class="hrow" style="margin-top:4px"><h3 class="h3 S">The menu</h3><a class="btn" style="height:34px;font-size:13px">' + ic(I['plus'], 14) + 'Add a service</a></div>'
  '<div class="menu">'
  + mi('syringe', 'Dermal filler, cheeks, lips, jaw', 'c', 'Medical spa', '45 minutes, results right away', '$780 / syringe', 'a')
  + mi('syringe', 'Botox', 'c', 'Medical spa', 'Forehead, frown and crow\'s feet lines', '$12 / unit', 'a')
  + mi('lips', 'Lip filler', 'c', 'Medical spa', 'Half syringes offered', '$780 / syringe', 'a')
  + mi('drop', 'Filler dissolving', 'c', 'Medical spa', 'Including work from another provider', '$450 est.', 'a')
  + mi('waves', 'Morpheus8, face', 'c', 'Skin care clinic', 'Microneedling plus radiofrequency', '$1,100', 'v')
  + '</div></div>' + BAR)

# 5. Visit
HEAT = {'Sun': [0]*10, 'Mon': [0]*10,
        'Tue': [1,2,2,3,3,2,2,2,2,1], 'Wed': [1,2,3,4,4,3,3,2,2,1], 'Thu': [1,2,3,4,4,3,3,2,2,1],
        'Fri': [1,2,3,4,4,3,3,2,2,1], 'Sat': [1,1,2,3,3,2,2,1,1,1]}
HC = ['#e6ebf5', '#c8d6f1', '#8fb0e8', '#4f82dd', '#2257d6']
HRS = ['9 AM', '10', '11', '12 PM', '1', '2', '3', '4', '5', '6 PM']
hm = '<div class="hm"><span></span>' + ''.join(f'<span class="dy">{d[0] if d!="Thu" else "T"}</span>' for d in HEAT)
hm = '<div class="hm"><span></span>' + ''.join(f'<span class="dy">{d}</span>' for d in HEAT)
for r, h in enumerate(HRS):
    hm += f'<span>{h}</span>' + ''.join(f'<i style="background:{HC[HEAT[d][r]]}"></i>' for d in HEAT)
hm += '</div>'
p_visit = topbar('Visit') + ('<div class="bd" style="padding-top:14px;gap:12px">'
  '<div><h2 class="h2 S">Visit</h2><span class="sub">When it\'s quiet, where to park, and what\'s nearby.</span></div>'
  '<div class="gl wv"><span class="lbl">When to visit<span class="qn"><span class="mk c" style="margin:0 5px 0 0"></span>Quiet right now</span></span>'
  '<b style="font-size:18px;line-height:23px">Tuesday or Wednesday, before 11 AM.</b>'
  f'<span class="sub">Busiest Wednesday and Thursday from noon to 2. Saturday afternoons run about 25 minutes behind.{MK["a"]}</span>'
  '<a class="bp" href="Book.html" style="margin-top:6px;height:46px;font-size:15px">Request Tuesday 10 AM</a></div>'
  '<div class="hrow"><h3 class="h3 S">Busy times</h3><span class="sub" style="font-size:12px">12 weeks. Darker is busier.</span></div>'
  '<div class="gl" style="padding:12px 12px 10px">' + hm + '</div>'
  '<div class="gl fact"><span class="lbl">Best place to park</span><b>Structure B, level 3. Validated for 2 hours.</b>'
  f'<span class="sub">Ask the front desk for the validation sticker.{MK["v"]}</span></div>'
  '</div>' + BAR)

# 6. Updates
def upd(src, when, text, ph, votes, n, comments):
    cm = ''.join(f'<div class="cm"><b>{u}</b><span>{c}</span></div>' for u, c in comments)
    return (f'<div class="up"><div class="who"><span class="l">L</span><span><b>Lumen Aesthetics</b><span>{src} · {when}{MK["c"]}</span></span></div>'
            f'<p>{text}</p>{photo(ph)}<span class="acts"><span>▲ {votes}</span><span>{n} comments</span><span>share</span></span>{cm}</div>')
p_upd = topbar('Updates', 150) + ('<div class="bd" style="padding-top:14px;gap:10px">'
  '<div class="hrow"><h2 class="h2 S">Updates</h2><a class="btn" style="height:34px;font-size:13px">Post an update</a></div>'
  '<div class="chips"><span class="chip on">All <em>9</em></span><span class="chip">Instagram <em>2</em></span><span class="chip">Facebook <em>1</em></span><span class="chip">TikTok <em>1</em></span><span class="chip">Google post <em>2</em></span></div>'
  '<div>' + upd('Instagram', '2 days ago', 'Morpheus8 Body is here. Arms, stomach and knees. Consults open October 1 with Dr. Nair.', 'Treatment room', 142, 9,
               [('kellyw_irvine', 'Finally! Booking for my arms.'), ('oc_skin_nerd', 'Is it the same as the face version?')])
  + upd('Facebook', '4 days ago', 'Skin Night is Thursday, October 15, 6 to 9 PM. Live demos with Dr. Nair and $50 off anything booked that night.', 'Front desk', 88, 5, [])
  + '</div></div>' + BAR)

# Row 2
SHEET_BG = lambda inner: f'<div style="opacity:0.55;display:flex;flex-direction:column;flex:1;min-height:0">{inner}</div><div class="scrim"></div>'
locals_bg = p_locals.split('<div class="bar">')[0]
visit_bg = p_visit.split('<div class="bar">')[0]
p_book = SHEET_BG(locals_bg) + ('<div class="sheet"><span class="gr"></span>'
  + f'<div class="cbc">{CASH}</div>'
  '<div class="seg"><span class="on">Book a visit</span><span>Post</span></div>'
  '<div class="bk"><div class="rw"><div class="c"><small>Day</small><span>Tue, Sep 29</span></div><div class="c"><small>Time</small><span>Morning</span></div></div>'
  f'<div class="rw"><div class="c" style="flex-direction:row;align-items:center;justify-content:space-between"><span style="display:flex;flex-direction:column"><small>Service</small><span>Consultation</span></span>{ic(I["down"], 18)}</div></div></div>'
  '<a class="bp" href="Book.html">Request a booking</a><span class="note">Takes 30 seconds. You won\'t be charged.</span>'
  f'<div style="display:flex;justify-content:center;gap:22px;font-size:13.5px"><a style="display:flex;gap:6px;align-items:center;text-decoration:underline;text-underline-offset:3px">{ic(I["flag"], 15)}Report this listing</a><a style="display:flex;gap:6px;align-items:center;text-decoration:underline;text-underline-offset:3px" href="Report.html">{ic(I["pencil"], 15)}Suggest an edit</a></div>'
  '</div>')

p_edit = SHEET_BG(visit_bg) + ('<div class="sheet"><span class="gr"></span>'
  f'<div class="sh"><b>Suggest an edit</b><a class="icb" style="width:32px;height:32px">{ic(I["x"], 18)}</a></div>'
  '<span class="sl">What needs fixing?</span><div class="chips" style="flex-wrap:wrap"><span class="chip on">Hours</span><span class="chip">Phone</span><span class="chip">Price</span><span class="chip">Service</span><span class="chip">Team</span><span class="chip">Something else</span></div>'
  f'<span class="sl">Monday hours right now</span><div style="display:flex;justify-content:space-between;font-size:15px;padding:2px 0 8px;border-bottom:1px solid var(--line)"><span><i class="mk a" style="margin:0 6px 0 0"></i>9 AM to 6 PM</span><span class="sub">AI guess</span></div>'
  '<span class="sl">What should it say?</span><div class="bin f">Closed Mondays</div>'
  '<span class="sl">How do you know?</span><div class="chips" style="flex-wrap:wrap"><span class="chip on">I called</span><span class="chip">I went there</span><span class="chip">Their website or sign</span><span class="chip">I work there</span></div>'
  '<a class="bp">Submit</a></div>')

p_done = SHEET_BG(visit_bg) + ('<div class="sheet" style="align-items:center;text-align:center;gap:12px;padding-top:14px"><span class="gr"></span>'
  '<span style="width:56px;height:56px;border-radius:50%;background:#fbe4d3;display:flex;align-items:center;justify-content:center;margin-top:6px"><i class="mk v" style="width:16px;height:16px;margin:0;border-width:2px"></i></span>'
  '<b style="font-size:24px" class="S">Thanks, Tom.</b>'
  '<span style="font-size:15px;font-weight:600;line-height:21px">Your fix shows on the page right away, marked as visitor submitted.</span>'
  '<div class="gl" style="padding:14px 16px;text-align:left;border-radius:18px"><b style="font-size:14px">What happens next</b><br><span class="sub">When a second neighbor or Lumen agrees, it turns into a confirmed fact, and it is what AI starts repeating. We let Lumen know about your fix today.</span></div>'
  '<span class="sub">We\'ll tell you when it\'s confirmed. Your fixes so far: <b style="color:var(--navy)">4 confirmed</b></span>'
  '<a class="btn" style="width:100%;height:50px;box-sizing:border-box;font-size:15px">Back to Lumen</a></div>')

p_photos = sb() + (f'<div class="ab"><a class="icb" href="Main.html">{ic(I["back"])}</a><span class="t">51 photos</span><span style="width:42px"></span></div>'
  '<div style="padding:0 16px 10px;display:flex;flex-direction:column;gap:10px"><div class="chips"><span class="chip on">All</span><span class="chip">Results</span><span class="chip">Space</span><span class="chip">Team</span></div>'
  f'<div class="cbc" style="background:rgba(15,26,51,0.06);display:flex;gap:10px;align-items:center;padding:11px 14px"><span style="flex:1" class="sub"><b style="color:var(--navy)">No code detected</b> on any photo. AI can\'t tell what they show.</span><span class="btn" style="height:34px;font-size:13px">{ic(I["lock"], 14)}Add media</span></div></div>'
  '<div class="pg">' + ''.join(photo(k) for i, k in enumerate(list(PH) * 4)) + '</div>')

REFS = [f'<div class="rf"><span class="n">[{n}]</span><span><i class="mk {m}" style="margin:0 6px 0 0"></i><span class="k">{k}</span><b>{t}</b> <span class="mu">{d}</span></span></div>' for n, m, k, t, d in [
      (1, 'c', 'LOCALS', 'Answers about hours, prices and services', 'Lumen\'s website and Google Business Profile. Checked Sep 25, 2026.'),
      (2, 'v', 'LOCALS', 'First consult is $75 and credited', 'Marcus D., in person, Mar 12, 2026.'),
      (3, 'v', 'LOCALS', 'Nadia is the one to see for lips', '3 visitors, after treatment, Aug 2026.'),
      (4, 'v', 'LOCALS', 'Coastline replies faster than Lumen', 'Sam K., called both, Sep 10, 2026.'),
      (5, 'a', 'LOCALS', 'Answers marked AI', 'Summaries of reviews and the record. Not medical advice.'),
      (6, 'c', 'SERVICES', 'Botox $12 per unit, filler $780 per syringe', 'lumenaesthetics.com/pricing. Checked Sep 25, 2026.')]]
def pal(lg, bg, n, sub, sc, col, me=False):
    return f'<div class="r{" me" if me else ""}"><span class="lg" style="background:{bg}">{lg}</span><span class="g"><b>{n}</b><span>{sub}</span></span><span class="sc"><i><u style="width:{sc}%;background:{col}"></u></i><span style="color:{"#2f6b3a" if sc>70 else "var(--navy)"}">{sc}</span></span></div>'
p_end = sb() + ('<div class="bd" style="padding-top:6px;gap:14px">'
  '<div class="gl" style="padding:14px 16px" ><div class="pal"><div class="hrow" style="margin-bottom:6px"><b style="font-size:16px">People also look at</b><span class="sub" style="font-size:12px">AI Score, out of 100</span></div>'
  + pal('LA', '#fbdfe0', 'Lumen Aesthetics', '612 reviews · you are here', 58, '#c13515', True)
  + pal('CM', '#e3defa', 'Coastline MedSpa', '1,102 reviews · Newport Beach, 6 mi', 84, '#1f8a2e')
  + pal('DC', '#dce9fa', 'Derm + Co', '640 reviews · Tustin, 5 mi', 79, '#1f8a2e')
  + pal('PS', '#dff0e4', 'Pacific Skin Studio', '217 reviews · Irvine, 3 mi', 44, '#c13515')
  + '</div></div>'
  + '<div class="refbox"><div class="hrow"><span class="S" style="font-size:26px;line-height:30px">References</span><span class="sub">53 sources</span></div>' + LEGEND
  + '<div class="refs">' + ''.join(REFS[:2]) + '</div>'
  + '<details class="more-refs"><summary><span class="peek refs">' + REFS[2] + '</span><span class="showall">Show all 53 references' + ic(I['down'], 16) + '</span></summary>'
  + '<div class="refs">' + ''.join(REFS[3:]) + f'</div><a class="btn" style="height:34px;font-size:13px;margin-top:8px">{ic(I["plus"], 13)}Add a reference</a></details></div>'
  + f'<a class="acc" href="History.html" style="display:flex;align-items:center"><span style="flex:1;display:flex;flex-direction:column"><span class="S" style="font-size:24px;line-height:28px">Change history</span><span class="sub">Every change to every fact, newest first</span></span>{ic(I["chev"], 20)}</a>'
  + '</div>' + BAR)

def hs(d, f, new, old, who, m):
    return f'<div class="hs"><i class="mk {m}"></i><div class="g"><b>{f}</b><span>{new}</span>{f"<s>{old}</s>" if old else ""}<span class="w">{who}</span></div><span class="d">{d}</span></div>'
p_hist = sb() + (f'<div class="ab"><a class="icb" href="Main.html">{ic(I["back"])}</a><span class="t"></span><span style="width:42px"></span></div>'
  '<div class="bd" style="gap:10px"><h2 class="h2 S" style="font-size:38px;line-height:40px">Change history</h2><span class="sub" style="margin-top:-6px">Every change to every fact on Lumen\'s page, newest first. Nothing is ever deleted.</span>'
  '<div class="chips"><span class="chip on">All</span><span class="chip">Hours</span><span class="chip">Services</span><span class="chip">Prices</span><span class="chip">Team</span></div><div>'
  + hs('Today', 'Monday hours', 'Closed', '9 AM to 6 PM', 'Aisha M., visited on a Monday · Photo of the door sign', 'v')
  + hs('Sep 26', 'Saturday, Oct 3', 'Closed for staff training', 'Open', 'Lumen, confirmed as the owner', 'c')
  + hs('Sep 25', 'Botox', '$12 a unit', '$14 a unit', 'lumenaesthetics.com/pricing · Archived copy', 'c')
  + hs('Sep 24', 'Parking tip', 'Level 3 of Structure B has the elevator', '', 'Kelly W., goes every month · Thread 4821', 'v')
  + hs('Sep 21', 'Morpheus8 Body', 'Added, consults from Oct 1', '', 'Lumen\'s Instagram post · Archived copy', 'c')
  + hs('Aug 2', 'Monday hours', '9 AM to 6 PM', '', 'What ChatGPT and Gemini said on this date', 'a')
  + '</div></div>')


# ---------------- AI tab (where the AI Score card goes)
SIG = [('Retrieval grounding', 26, 60, 'Can AI find a clear, matching answer about Lumen when it searches?'),
       ('Off-property attestation', 20, 50, 'Do other sites say the same things Lumen says?'),
       ('AI visibility', 14, 45, 'How often AI names Lumen when people ask'),
       ('Reviews and response', 12, 70, 'Volume, rating, recency and owner replies'),
       ('Backlink and citation authority', 8, 60, 'Trusted sites that link to or mention Lumen'),
       ('Google Business Profile', 8, 72, 'Complete, current and active'),
       ('Speed and mobile', 7, 80, 'How fast their site loads on a phone'),
       ('Content freshness and schema', 5, 30, 'Recent content and code AI can read')]
def col(v): return '#2f6b3a' if v >= 70 else ('#0f1a33' if v >= 50 else '#c13515')
gauge = ('<svg width="300" height="160" viewBox="0 0 300 160" aria-hidden="true">'
  '<path d="M30 150 A120 120 0 0 1 270 150" fill="none" stroke="rgba(15,26,51,0.12)" stroke-width="16" stroke-linecap="round"/>'
  '<path d="M30 150 A120 120 0 0 1 270 150" fill="none" stroke="#c13515" stroke-width="16" stroke-linecap="round" pathLength="100" stroke-dasharray="58 100"/>'
  + ''.join(f'<g transform="rotate({-180 + v*1.8} 150 150)"><line x1="262" y1="150" x2="286" y2="150" stroke="#0f1a33" stroke-width="2"/></g>' for v in (71, 84))
  + '<text x="236" y="38" font-family="Hanken Grotesk, sans-serif" font-size="11" font-weight="700" fill="#0f1a33">71</text><text x="284" y="88" font-family="Hanken Grotesk, sans-serif" font-size="11" font-weight="700" fill="#0f1a33">84</text>'
  + '<text x="150" y="132" text-anchor="middle" font-family="Cormorant Garamond, Georgia, serif" font-size="68" fill="#c13515">58</text>'
  + '<text x="150" y="152" text-anchor="middle" font-family="Hanken Grotesk, sans-serif" font-size="12" fill="#4a5570">out of 100</text></svg>')
p_ai1 = topbar('AI', 330) + ('<div class="bd" style="padding-top:14px;gap:10px">'
  '<div><h2 class="h2 S">How AI sees Lumen</h2><span class="sub">The AI Score, how it is built, and what AI engines say about Lumen. Checked Sep 25, 2026.</span></div>'
  '<div class="gl" style="padding:14px 16px 12px;display:flex;flex-direction:column;align-items:center;gap:4px">' + gauge +
  '<div style="display:flex;gap:16px;font-size:12.5px;color:var(--ink2)"><span><b style="color:var(--navy)">71</b> Irvine avg</span><span><b style="color:var(--navy)">84</b> Coastline, top in Irvine</span></div></div>'
  '<div class="hrow" style="margin-top:4px"><h3 class="h3 S">8 signals</h3><span class="sub" style="font-size:12px">weight · Lumen\'s score</span></div><div class="sig">'
  + ''.join(f'<div class="sg"><span class="nm">{n}<em>{w}%</em></span><span class="br"><u style="width:{v}%;background:{col(v)}"></u></span><b style="color:{col(v)}">{v}</b></div>' for n, w, v, d in SIG)
  + '</div><span class="sub" style="font-size:12px">Each signal is scored 0 to 100, then weighted. Same method for every business, never for sale.</span>'
  '</div>' + BAR)

ENG = [('ChatGPT', 36), ('Gemini', 41), ('Perplexity', 27), ('Google AI Overviews', 23), ('Claude', 32)]
PROMPTS = [('Best med spa in Irvine', None, 'Coastline, Derm + Co, Pacific Skin'),
           ('Natural-looking lip filler in Irvine', 2, ''),
           ('Board-certified dermatologist for Botox near Irvine Spectrum', 1, ''),
           ('Where can I get Morpheus8 near Irvine?', None, 'Coastline, Derm + Co'),
           ('Affordable Botox in Orange County', None, 'Pacific Skin, Coastline')]
def pr(q, rank, others):
    tag = (f'<span class="ok">Named #{rank}</span>' if rank else f'<span class="no">Not named</span><span class="mu" style="font-size:12px">AI named {others}</span>')
    return f'<div class="pq"><span class="S" style="font-size:19px;line-height:22px">“{q}”</span><span style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">{tag}</span></div>'
dots = ''.join(f'<i class="{"on" if k in (2, 5, 8, 11, 14, 17, 20) else ""}"></i>' for k in range(22))
p_ai2 = topbar('AI', 330) + ('<div class="bd" style="padding-top:14px;gap:12px">'
  '<div><h3 class="h3 S">What AI says when people ask</h3><span class="sub">22 questions people ask about Irvine med spas, asked in 5 AI engines.</span></div>'
  '<div class="gl" style="padding:14px 16px;display:flex;flex-direction:column;gap:8px"><div style="display:flex;align-items:baseline;gap:8px"><span class="S" style="font-size:44px;line-height:44px;color:#c13515">7</span><span style="font-size:15px">of 22 answers name Lumen</span></div>'
  f'<div class="pdots">{dots}</div><span class="sub" style="font-size:12px">Coastline is named in 15 of 22.</span></div>'
  '<div class="eng">' + ''.join(f'<div class="er"><span>{n}</span><span class="br"><u style="width:{v}%"></u></span><b>{v}%</b></div>' for n, v in ENG) + '</div>'
  '<div>' + ''.join(pr(*x) for x in PROMPTS[:4]) + '</div>'
  '</div>' + BAR)

def fc(field, ai, rec, mk, right):
    return (f'<div class="fc"><span class="f">{field}</span><span class="row"><span class="fa {"" if right else "bad"}">AI: {ai}</span>'
            f'<span class="rc">Record: {rec}{MK[mk]}</span></span></div>')
THEMES = [('Results', 92), ('Staff', 88), ('Price', 54), ('Wait time', 41), ('Calling back', 22)]
p_ai3 = topbar('AI', 330) + ('<div class="bd" style="padding-top:14px;gap:12px">'
  '<div><h3 class="h3 S">What AI gets wrong</h3><span class="sub">How ChatGPT described Lumen on Sep 25, checked against the record.</span></div>'
  '<div class="bub"><span class="who">ChatGPT</span>Lumen Aesthetics is a med spa at the Irvine Spectrum known for natural-looking filler. '
  'It is <mark>open Monday, 9 AM to 6 PM</mark>, and Botox runs about <mark>$14 a unit</mark>. Reviewers praise the results but say the front desk is slow to call back.</div>'
  '<div>' + fc('Monday hours', 'Open 9 AM to 6 PM', 'Closed', 'v', False) + fc('Botox', '$14 a unit', '$12 a unit', 'c', False)
  + fc('Known for', 'Natural-looking filler', 'Dermal filler, Botox, lip filler', 'c', True) + fc('Parking', 'Not mentioned', 'Structure B, level 3', 'v', False) + '</div>'
  '<div class="hrow"><h3 class="h3 S">How AI reads reviews</h3><span class="sub" style="font-size:12px">% positive</span></div>'
  '<div class="eng">' + ''.join(f'<div class="er"><span>{n}</span><span class="br"><u style="width:{v}%;background:{col(v)}"></u></span><b style="color:{col(v)}">{v}%</b></div>' for n, v in THEMES) + '</div>'
  '</div>' + BAR)

CITES = [('Google profile', 41), ('Yelp', 22), ('RealSelf', 14), ('lumenaesthetics.com', 9), ('Local AI Registry', 8), ('OC Register', 6)]
SOV = [('Coastline', 34, '#0f1a33'), ('Derm + Co', 26, '#4a5570'), ('Lumen', 14, '#c13515'), ('Pacific Skin', 8, '#9aa3b5'), ('Others', 18, 'rgba(15,26,51,0.14)')]
dirs = ''.join(f'<i class="{"on" if k < 4 else ("bad" if k < 7 else "")}"></i>' for k in range(40))
p_ai4 = topbar('AI', 330) + ('<div class="bd" style="padding-top:14px;gap:12px">'
  '<div><h3 class="h3 S">Where AI gets its answers</h3><span class="sub">The sites AI cited when it talked about Lumen.</span></div>'
  '<div class="eng">' + ''.join(f'<div class="er"><span>{n}</span><span class="br"><u style="width:{v*2}%"></u></span><b>{v}%</b></div>' for n, v in CITES) + '</div>'
  '<div class="gl" style="padding:14px 16px;display:flex;flex-direction:column;gap:8px"><b style="font-size:15px">Listed on 7 of 40 directories AI checks</b>'
  f'<div class="ddots">{dirs}</div><span class="sub" style="font-size:12px"><i class="sw" style="background:#0f1a33"></i>Listed, matches <i class="sw" style="background:#c13515"></i>Listed, hours disagree <i class="sw" style="background:rgba(15,26,51,0.14)"></i>Missing</span></div>'
  '<div style="display:flex;flex-direction:column;gap:8px"><b style="font-size:15px">Share of AI answers, Irvine med spas</b>'
  '<div class="sov">' + ''.join(f'<u style="width:{v}%;background:{c}"></u>' for n, v, c in SOV) + '</div>'
  '<div class="sovl">' + ''.join(f'<span><i class="sw" style="background:{c}"></i>{n} {v}%</span>' for n, v, c in SOV[:4]) + '</div></div>'
  '<div class="cbc" style="display:flex;flex-direction:column;gap:8px"><b style="font-size:16px">Is this your business?</b><span class="sub">Claim it free, correct the record, and Local AI Registry pushes the fixes to the sites AI reads.</span><a class="bp" href="Claim.html" style="height:46px;font-size:15px">Claim it free</a></div>'
  '</div>' + BAR)

p_ai5 = topbar('AI', 330) + ('<div class="bd" style="padding-top:14px;gap:10px">'
  '<div><h3 class="h3 S">What AI reads</h3><span class="sub">The page ChatGPT, Gemini, Perplexity and Google read about Lumen. The code version is exactly what their crawlers get.</span></div>'
  '<div class="seg"><span class="on">Page</span><span>Code</span></div>'
  '<div class="gl ed"><span class="lbl" style="font-size:10px">Local AI Registry · Med spas in Irvine, CA · Editorial</span>'
  '<span class="S" style="font-size:24px;line-height:27px;font-weight:600">Lumen Aesthetics, Irvine: a physician-owned med spa at the Irvine Spectrum (2026 guide)</span>'
  '<span class="sub" style="font-size:12px">By Steve Lee, founder and CEO of Local AI Registry. Fact-checked against 69 sources. Updated Sep 25, 2026.</span>'
  '<b style="font-size:14px;margin-top:4px">In short</b><span style="font-size:13.5px;line-height:19px">Lumen Aesthetics is a physician-owned med spa on the second floor of the Irvine Spectrum Center in Irvine, California, open since 2016. It is led by Dr. Priya Nair, MD, a board-certified dermatologist, and is best known for natural-looking dermal filler and Botox.</span>'
  '<b style="font-size:14px;margin-top:4px">Key facts</b><div class="kt">'
  + ''.join(f'<span>{k}</span><span>{v}</span>' for k, v in [('Type', 'Physician-owned med spa'), ('Hours', 'Tue to Sat, 9 AM to 7 PM'), ('Rating', '4.9 across 612 reviews'), ('Prices', 'Botox $12 a unit, filler $780 a syringe')])
  + '</div></div></div>' + BAR)

ROWS = [
 [scr('Profile, top', 'Same order as desktop: photos, name and Unclaimed, category, rating and hours, description, then the AI Score strip. Cashback and booking stay pinned to the bottom.', p_top),
  scr('Profile, scrolling', 'All five stats show at once, no hidden scroll. The whole card taps through to the AI tab. Owner, legend and the AI check line come before the tabs.', p_scroll),
  scr('Locals tab', 'Name and tabs stick. Serif post titles lead, with the vote column and colored kind label from desktop.', p_locals),
  scr('Services tab', 'Known for cards, then the menu with icons, marks and the same prices as desktop.', p_svc),
  scr('Visit tab', 'When to visit, then the same day-by-hour busy grid as desktop, then parking.', p_visit),
  scr('Updates tab', 'Source chips with counts. Posts read like the desktop feed, with photos and comments.', p_upd)],
 [scr('Request a booking', 'Tapping Request a booking opens the desktop booking card as a sheet: cashback, Book a visit or Post, day, time, service.', p_book),
  scr('Suggest an edit', 'The desktop form as a sheet: what needs fixing, what it says now, the fix, and how you know.', p_edit),
  scr('Fix submitted', 'Same confirmation as desktop. The fix shows right away as visitor submitted.', p_done),
  scr('All photos', 'Three across with filters. Photos AI cannot read say so, with a way to add media.', p_photos),
  scr('Bottom of the page', 'Two references show, the third fades out, and a full-width button says how many more there are. All 53 stay in the page code for search engines and AI.', p_end),
  scr('Change history', 'Newest first. New value, old value crossed out, who, and how they know.', p_hist)],
 [scr('AI tab: the score', 'Tapping the AI Score card opens this tab. The score against Irvine and the top competitor, then the 8 weighted signals behind it.', p_ai1),
  scr('AI tab: what AI says', 'How often AI names Lumen across 22 real questions and 5 engines, then the questions it wins and loses.', p_ai2),
  scr('AI tab: what AI gets wrong', 'A real AI answer with the wrong facts marked, checked against the record, then how AI reads the reviews.', p_ai3),
  scr('AI tab: where AI looks', 'The sites AI cites, directory coverage, and share of answers against competitors. Ends in Claim.', p_ai4),
  scr('AI tab: what AI reads', 'The editorial page AI crawlers read, with the switch to the code version, same as desktop.', p_ai5)],
]
TITLE = 'M3 · Mobile: business profile'
H1 = 'Mobile · Business profile'
SUB = 'Matches the desktop profile. Tapping the AI Score opens the AI tab (bottom row). Photos, name, AI Score, owner, then serif tabs that stick once you scroll. Cashback and Request a booking stay pinned to the bottom, and booking and edits open as sheets so you never lose your place.'
n = max(len(r) for r in ROWS); W = 96 + n * 390 + (n - 1) * 44; H = 160 + len(ROWS) * (844 + 120)
body = f'<div class="mb"><div class="mb-h"><h1>{H1}</h1><p>{SUB}</p></div>' + ''.join(f'<div class="mrow">{"".join(r)}</div>' for r in ROWS) + '</div>'
BG = '<link rel="stylesheet" href="brand.css?v=12">'  # paper and texture only; this page has no #dc-root so the overrides skip it

html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width={W}"><meta name="robots" content="noindex">'
        f'<title>{TITLE} · Local AI Registry prototype</title>{BG}<style>{CSS}</style></head><body>{body}</body></html>')
open(os.path.join(ROOT, 'docs', 'MProfile.html'), 'w').write(html)
dc = (f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>{TITLE}</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n<style>{CSS}</style>\n</helmet>\n'
      + body.replace('href="', 'href="').replace('.html"', '.dc.html"') + '\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n    return {};\n  }\n}\n</script>\n</body>\n</html>\n')
open(os.path.join(ROOT, 'prototype', 'MProfile.dc.html'), 'w').write(dc)
cj = os.path.join(ROOT, 'prototype', 'canvas.json'); c = json.load(open(cj))
c['boards']['MProfile.dc.html'].update({'w': W, 'h': H}); json.dump(c, open(cj, "w"))
print('wrote MProfile', W, H)
