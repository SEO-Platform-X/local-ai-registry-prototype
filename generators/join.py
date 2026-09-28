import sys; sys.path.insert(0,'/tmp/gen'); from common import *
from headers import pub
C=r'''.jw{max-width:1080px;margin:0 auto;padding:72px 40px 80px;display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center}
.ey{font-family:"Cormorant Garamond",Georgia,serif;font-style:italic;font-size:22px;color:#5b6474}
.jw h1{margin:0;font-size:56px;line-height:60px;font-weight:500}
.lead{font-size:17px;line-height:27px;color:#3d4658;max-width:560px;margin:4px 0 30px}
.jg{display:grid;grid-template-columns:1fr 1fr;gap:28px;width:100%;text-align:left}
.jc{display:flex;flex-direction:column;gap:14px;padding:34px 32px;border-radius:6px;background:#f5e3cc;border:1px solid #e6cfb2;text-decoration:none;color:#13203a}
.jc.b{background:#f7f4ee;border-color:#e4ded2}
.jc .lb{font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:#5b6474}
.jc h2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-size:36px;line-height:40px;font-weight:500}
.jc h2 em{color:#e5482d}
.jc p{margin:0;font-size:15px;line-height:24px;color:#3d4658;font-weight:400}
.go{align-self:flex-start;display:inline-flex;align-items:center;gap:12px;height:48px;padding:0 24px;border-radius:9999px;background:#13203a;color:#ffffff;font-size:15px;font-weight:600;margin-top:10px}
'''
B=pub()+'''<div class="jw"><span class="ey">Join the registry</span><h1>Which one are you?</h1><p class="lead">Locals share what they actually know. Owners keep their record right. Both are free.</p><div class="jg">
<a href="Post.dc.html" class="jc"><svg viewBox="0 0 120 90" width="120" height="90" aria-hidden="true" fill="none" stroke="#13203a" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M14 16h62a8 8 0 0 1 8 8v26a8 8 0 0 1-8 8H40l-14 12V58H14a8 8 0 0 1-8-8V24a8 8 0 0 1 8-8z" fill="#fbf4ea"/><path d="M22 32h46M22 42h30"/><path d="M70 40h36a8 8 0 0 1 8 8v18a8 8 0 0 1-8 8h-6v10l-12-10H70a8 8 0 0 1-8-8V48" fill="#e5482d" fill-opacity="0.15" stroke="#e5482d"/><circle cx="80" cy="57" r="1.6" fill="#e5482d" stroke="none"/><circle cx="88" cy="57" r="1.6" fill="#e5482d" stroke="none"/><circle cx="96" cy="57" r="1.6" fill="#e5482d" stroke="none"/></svg><span class="lb">For locals</span><h2>Share what you <em>know</em>.</h2><p>Ask a question, leave a tip, give a heads-up. Pick an anonymous username. When a business accepts your fix, you become a Local expert.</p><span class="go">Join as a local <span>⟶</span></span></a>
<a href="ExploreSearch.dc.html" class="jc b"><svg viewBox="0 0 120 90" width="120" height="90" aria-hidden="true" fill="none" stroke="#13203a" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="20" y="30" width="80" height="52" fill="#fbf4ea"/><path d="M14 30h92l-6-12H20z" fill="#e5482d" fill-opacity="0.18" stroke="#e5482d"/><rect x="50" y="54" width="20" height="28" fill="#dfe8f5"/><rect x="28" y="42" width="14" height="12"/><rect x="78" y="42" width="14" height="12"/><path d="M6 82h108" stroke-width="1"/></svg><span class="lb">For owners</span><h2>Claim your <em>record</em>.</h2><p>Your business already has a page. Claim it, answer locals, and see what ChatGPT, Gemini and Claude say about you.</p><span class="go">Find my business <span>⟶</span></span></a></div></div>'''
open(P+'Join.dc.html','w').write(page('Join',C,B,'    return {};')); print('ok')
