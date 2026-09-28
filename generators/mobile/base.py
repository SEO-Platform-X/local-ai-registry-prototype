import sys,json; sys.path.insert(0,'/tmp/gen'); from common import page
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
exec(open('/tmp/gen/ill.py').read())
SK='fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
def ic(p,s=24): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" {SK} aria-hidden="true">{p}</svg>'
I=dict(
 home='<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>',
 search='<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
 plus='<path d="M12 5v14M5 12h14"/>',
 bell='<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
 user='<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',
 store='<path d="M4 9l1-5h14l1 5M4 9v11h16V9M4 9h16"/><path d="M10 20v-6h4v6"/>',
 inbox='<path d="M3 13l3-8h12l3 8v6H3z"/><path d="M3 13h5l1 2h6l1-2h5"/>',
 cal='<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 menu='<path d="M4 7h16M4 12h16M4 17h16"/>',
 back='<path d="M15 5l-7 7 7 7"/>', x='<path d="M6 6l12 12M18 6L6 18"/>', share='<path d="M12 3v12M7 8l5-5 5 5"/><path d="M5 13v7h14v-7"/>',
 map='<path d="M9 4l-6 2v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>', list='<path d="M8 6h13M8 12h13M8 18h13"/><circle cx="4" cy="6" r="1"/><circle cx="4" cy="12" r="1"/><circle cx="4" cy="18" r="1"/>',
 chev='<path d="M9 5l7 7-7 7"/>', pencil='<path d="M4 20h4L20 8l-4-4L4 16z"/>', filter='<path d="M4 6h16M7 12h10M10 18h4"/>', check='<path d="M5 12l5 5 9-10"/>', up='<path d="M12 5l7 8H5z"/>',
 chat='<path d="M4 5h16v11H9l-5 4z"/>', pin='<path d="M12 21s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>', phone='<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>', mail='<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>', lock='<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>', star='<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>', gear='<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/>', help='<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01"/>', team='<circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c.8-3.4 3.2-5 6-5s5.2 1.6 6 5M15 15c3 0 5 1.6 5.5 4.5"/>', gift='<rect x="3" y="9" width="18" height="12" rx="1"/><path d="M3 13h18M12 9v12M12 9c-2-4-6-4-6-1.5S10 9 12 9zm0 0c2-4 6-4 6-1.5S14 9 12 9z"/>', card='<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/>', note='<path d="M6 3h9l4 4v14H6z"/><path d="M9 12h7M9 16h5"/>', code='<path d="M8 8l-4 4 4 4M16 8l4 4-4 4"/>', google='<circle cx="12" cy="12" r="9"/><path d="M12 12h8M12 3a9 9 0 0 1 6.4 2.6"/>')
LOGO='<svg width="22" height="20" viewBox="0 0 24 22" aria-hidden="true"><path d="M12 1L1 21h11z" fill="#2b59d9"/><path d="M12 1l11 20H12z" fill="#e5482d"/></svg>'
CSS=r'''
.mb{display:flex;flex-direction:column;background:#e9e3d8;padding:40px 48px 56px;box-sizing:border-box;gap:28px;font-family:Figtree,sans-serif}
.mb-h{display:flex;align-items:baseline;gap:18px}.mb-h h1{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:48px;color:#13203a}.mb-h p{margin:0;font-size:15px;color:#3d4658;max-width:900px}
.mrow{display:flex;gap:44px;align-items:flex-start}
.ph{display:flex;flex-direction:column;gap:12px;width:390px;flex-shrink:0}
.ph-l{display:flex;flex-direction:column;gap:3px;min-height:52px}.ph-l b{font-size:14px;color:#13203a}.ph-l span{font-size:12px;line-height:17px;color:#5b6474}
.scr{width:390px;height:844px;border-radius:44px;background:#f3efe7;box-shadow:0 0 0 10px #13203a,0 30px 60px rgba(19,32,58,0.28);overflow:hidden;position:relative;display:flex;flex-direction:column;color:#13203a;font-size:17px;line-height:25px}
.scr{font-family:Figtree,sans-serif;font-weight:400}
.scr a{color:inherit;text-decoration:none;font-weight:inherit}
.scr .lk{text-decoration:underline}
.ab .t{font-family:Figtree,sans-serif}
.sb{height:47px;flex-shrink:0;display:flex;align-items:center;justify-content:space-between;padding:0 30px 0 34px;font-size:16px;font-weight:600;box-sizing:border-box}
.sb i{font-style:normal;display:flex;gap:6px;align-items:center}.sb i s{display:block;width:26px;height:12px;border-radius:3px;border:1.5px solid #13203a;box-sizing:border-box;text-decoration:none;position:relative}.sb i s::after{content:"";position:absolute;inset:1.5px;right:5px;background:#13203a;border-radius:1px}
.sb.dk{color:#fff}.sb.dk i s{border-color:#fff}.sb.dk i s::after{background:#fff}
.ab{height:56px;flex-shrink:0;display:flex;align-items:center;gap:12px;padding:0 16px;box-sizing:border-box}
.ab .t{font-size:17px;font-weight:700;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ab .t.c{text-align:center}
.icb{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;color:#13203a;text-decoration:none;position:relative}
.icb.w{background:#ffffff;box-shadow:0 1px 4px rgba(19,32,58,0.12)}
.dot{position:absolute;top:6px;right:6px;min-width:18px;height:18px;border-radius:9px;background:#e5482d;color:#fff;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;padding:0 4px;box-sizing:border-box}
.bd{flex:1;min-height:0;overflow:hidden;display:flex;flex-direction:column;padding:4px 20px 20px;gap:16px;box-sizing:border-box}
.bd.np{padding:0}
.tb{height:84px;flex-shrink:0;border-top:1px solid #e4ded2;background:#fbf8f3;display:grid;grid-template-columns:repeat(5,1fr);padding:6px 4px 0;box-sizing:border-box}
.tb a{display:flex;flex-direction:column;align-items:center;gap:3px;font-size:11px;font-weight:600;color:#8a93a3;text-decoration:none;position:relative}
.tb a.on{color:#13203a}.tb a.on::before{content:"";position:absolute;top:-6px;width:28px;height:3px;border-radius:2px;background:#13203a}
.tb a.pp span.pl{width:48px;height:34px;border-radius:17px;background:#e5482d;color:#fff;display:flex;align-items:center;justify-content:center}
.tb .n{position:absolute;top:-2px;left:52%;min-width:16px;height:16px;border-radius:8px;background:#e5482d;color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;padding:0 3px;box-sizing:border-box}
.hi{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);width:134px;height:5px;border-radius:3px;background:#13203a;opacity:0.9;z-index:9}
.cta{flex-shrink:0;padding:12px 20px 34px;border-top:1px solid #e4ded2;background:#f3efe7;display:flex;flex-direction:column;gap:10px;box-sizing:border-box}
.bp{height:56px;border-radius:9999px;background:#13203a;color:#fff !important;display:flex;align-items:center;justify-content:center;gap:10px;font-size:17px;font-weight:600;text-decoration:none;flex-shrink:0}
.bp.r{background:#e5482d}.bp.o{background:#ffffff;color:#13203a !important;border:1.5px solid #13203a}.bp.sm{height:44px;font-size:15px;padding:0 18px}
.lk{font-size:15px;font-weight:600;text-align:center;text-decoration:underline;text-underline-offset:3px}
.T{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:38px;line-height:40px;letter-spacing:-0.01em}
.T em{color:#e5482d}.T2{margin:0;font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:28px;line-height:31px}
.ey{font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#5b6474}
.mu{color:#5b6474}.sm{font-size:14px;line-height:20px}.xs{font-size:12px;line-height:17px}
.cd{background:#ffffff;border:1px solid #e4ded2;border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:10px}
.cd.pe{background:#f5e3cc;border-color:#e6cfb2}.cd.nv{background:#13203a;border-color:#13203a;color:#fff}
.rw{display:flex;align-items:center;gap:12px;min-height:56px;border-bottom:1px solid #ece6da;text-decoration:none}.rw:last-child{border-bottom:none}
.rw .g:not(.pill){flex:1;min-width:0;display:flex;flex-direction:column}.rw .g b{font-size:16px;line-height:21px;font-weight:600}.rw .g span{font-size:13px;line-height:18px;color:#5b6474}
.av{width:40px;height:40px;border-radius:50%;background:#13203a;color:#fff;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;flex-shrink:0}
.av.lt{background:#e4ded2;color:#13203a}.av.bl{background:#dfe8f5;color:#13203a}
.chs{display:flex;gap:8px;overflow:hidden;flex-shrink:0}.ch{height:40px;padding:0 16px;border-radius:9999px;border:1px solid #dcd5c7;background:#fff;display:inline-flex;align-items:center;gap:6px;font-size:15px;font-weight:600;white-space:nowrap;flex-shrink:0}.ch.on{background:#13203a;border-color:#13203a;color:#fff}
.srch{height:52px;border-radius:26px;background:#fff;box-shadow:0 2px 10px rgba(19,32,58,0.12);display:flex;align-items:center;gap:10px;padding:0 18px;font-size:16px;color:#8a93a3;flex-shrink:0}
.srch.f{box-shadow:0 0 0 2px #13203a;color:#13203a}
.inp{height:56px;border-radius:12px;border:1.5px solid #cfc8ba;background:#fff;display:flex;align-items:center;padding:0 16px;font-size:17px;box-sizing:border-box}.inp.f{border:2px solid #13203a}.inp.ta{height:auto;min-height:96px;align-items:flex-start;padding:14px 16px}
.lb{font-size:14px;font-weight:700;margin-bottom:-8px}
.mk{display:inline-block;width:9px;height:9px;border-radius:50%;margin-left:6px;vertical-align:1px}.mk.c{background:#237233}.mk.v{border:1.5px solid #e8740c;box-sizing:border-box}.mk.a{width:0;height:0;border-radius:0;border-left:5px solid transparent;border-right:5px solid transparent;border-bottom:9px solid #8a93a3}
.sh{position:absolute;left:0;right:0;bottom:0;background:#fbf8f3;border-radius:22px 22px 0 0;box-shadow:0 -10px 40px rgba(19,32,58,0.22);display:flex;flex-direction:column;gap:14px;padding:10px 20px 40px;box-sizing:border-box;z-index:5}
.sh .gr{width:40px;height:5px;border-radius:3px;background:#cfc8ba;align-self:center;margin-bottom:4px}
.scrim{position:absolute;inset:0;background:rgba(19,32,58,0.42);z-index:4}
.tabs{display:flex;gap:22px;border-bottom:1px solid #e4ded2;padding:0 20px;flex-shrink:0;overflow:hidden}.tabs span{height:46px;display:flex;align-items:center;font-size:15px;font-weight:600;color:#8a93a3;white-space:nowrap;border-bottom:2.5px solid transparent}.tabs span.on{color:#13203a;border-color:#13203a}
.pill{display:inline-flex;align-items:center;height:26px;padding:0 10px;border-radius:13px;font-size:12px;font-weight:700}.pill.g{background:#e6f2e8;color:#1c5f2a}.pill.o{background:#fff1e0;color:#9a5200}.pill.r{background:#fdecea;color:#b42318}.pill.n{background:#13203a;color:#fff}.pill.l{background:#ece6da;color:#3d4658}
.fr{display:flex;justify-content:space-between;gap:14px;padding:13px 0;border-bottom:1px solid #ece6da;font-size:16px}.fr:last-child{border-bottom:none}.fr .k{color:#5b6474}.fr .v{font-weight:600;text-align:right;white-space:nowrap}
.vote{display:flex;flex-direction:column;align-items:center;gap:0;width:34px;flex-shrink:0;font-size:13px;font-weight:700}
.post{display:flex;gap:10px;padding:14px 0;border-bottom:1px solid #ece6da}.post > .g{flex:1;display:flex;flex-direction:column;gap:4px}.post b{font-size:16px;line-height:21px}
.meta{font-size:12px;color:#5b6474;display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.stp{display:flex;gap:6px;flex-shrink:0}.stp i{flex:1;height:4px;border-radius:2px;background:#dcd5c7}.stp i.on{background:#13203a}
.ph-img{border-radius:14px;display:flex;align-items:flex-end;padding:10px;font-size:11px;font-weight:700;color:#5b6474;box-sizing:border-box}
.sw{width:44px;height:26px;border-radius:13px;background:#dcd5c7;position:relative;flex-shrink:0}.sw::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff}.sw.on{background:#13203a}.sw.on::after{left:21px}
.kbar{flex-shrink:0;margin:0 16px 8px;padding:10px 10px 10px 12px;border-radius:14px;background:#f5e3cc;border:1px solid #e6cfb2;display:flex;align-items:center;gap:10px}
.otp{display:flex;gap:10px}.otp span{flex:1;height:64px;border-radius:12px;border:1.5px solid #cfc8ba;background:#fff;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700}.otp span.f{border:2px solid #13203a}
.key{display:grid;grid-template-columns:repeat(3,1fr);background:#d6d0c4;padding:6px 6px 30px;gap:6px;flex-shrink:0}.key span{height:46px;border-radius:6px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:22px}
.kb{background:#d6d0c4;padding:8px 4px 34px;display:flex;flex-direction:column;gap:10px;flex-shrink:0}.kb div{display:flex;gap:6px;justify-content:center}.kb span{flex:1;max-width:34px;height:42px;border-radius:6px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 1px 0 #a9a298}.kb div:last-child span{max-width:none;font-size:14px}
.big{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;font-size:52px;line-height:52px}
'''
def sb(dark=False): return f'<div class="sb{" dk" if dark else ""}"><span>9:41</span><i>●●● <s></s></i></div>'
PUBT=[('home','Explore','MExplore.dc.html'),('search','Search','MExplore.dc.html'),('plus','Post','MLocals.dc.html'),('bell','Alerts','MLocals.dc.html'),('user','Me','MLocals.dc.html')]
OWNT=[('home','Home','MOwner.dc.html'),('store','Business','MOwner.dc.html'),('inbox','Inbox','MOwner.dc.html'),('cal','Premium','MOwner.dc.html'),('menu','More','MAccount.dc.html')]
def tabbar(kind,on,badges={}):
    T=PUBT if kind=='pub' else OWNT; out=''
    for k,l,h in T:
        n=f'<span class="n">{badges[l]}</span>' if l in badges else ''
        if l=='Post': out+=f'<a href="{h}" class="pp"><span class="pl">{ic(I["plus"],22)}</span>{l}</a>'
        else: out+=f'<a href="{h}" class="{"on" if l==on else ""}">{ic(I[k])}{n}{l}</a>'
    return f'<div class="tb">{out}</div>'
def appbar(left='',title='',right='',c=False): return f'<div class="ab">{left}<span class="t{" c" if c else ""}">{title}</span>{right}</div>'
def brand(): return f'<div class="ab">{LOGO}<span class="t" style="font-size: 16px;">Local AI Registry</span><a class="icb" href="#">{ic(I["bell"])}</a><a class="icb" href="MLocals.dc.html"><span class="av lt" style="width: 34px; height: 34px; font-size: 12px;">MT</span></a></div>'
def bk(t='',right='',href='#'): return appbar(f'<a class="icb" href="{href}">{ic(I["back"])}</a>',t,right or '<span style="width: 44px;"></span>',c=True)
def scr(label,note,inner,dark=False,bg=''):
    st=f' style="background: {bg};"' if bg else ''
    return f'<div class="ph"><div class="ph-l"><b>{label}</b><span>{note}</span></div><div class="scr"{st}>{sb(dark)}{inner}<div class="hi"></div></div></div>'
BOARDS=[]
def board(fname,title,h1,sub,rows):
    body=f'<div class="mb"><div class="mb-h"><h1>{h1}</h1><p>{sub}</p></div>'+''.join(f'<div class="mrow">{"".join(r)}</div>' for r in rows)+'</div>'
    n=max(len(r) for r in rows); w=96+n*390+(n-1)*44
    h=150+len(rows)*(844+110)
    open(P+fname,'w').write(page(h1,CSS,body,'    return {};',w=w))
    BOARDS.append((fname,title,w,h))
