import sys, json; sys.path.insert(0,'/tmp/gen'); from common import *
CSS=r'''.onav{height:68px;padding:0 40px;display:flex;align-items:center;gap:6px;border-bottom:1px solid #e6e6e6;background:#ffffff;position:relative;z-index:30}
.onav .lg{display:flex;align-items:center;gap:10px;text-decoration:none;margin-right:14px}
.locsw{position:relative;display:flex;align-items:center;gap:10px;height:44px;padding:0 12px 0 6px;border:1px solid #e3e3e3;border-radius:12px;cursor:pointer;margin-right:18px}
.locsw:hover{background:#fafafa}
.lav{width:30px;height:30px;border-radius:8px;background:#13203a;color:#ffffff;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;flex-shrink:0}
.locm2{position:absolute;top:52px;left:0;width:320px;border-radius:16px;background:#ffffff;box-shadow:0 12px 40px rgba(0,0,0,0.18);padding:8px;display:flex;flex-direction:column;z-index:40;cursor:default}
.locm2 a{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:10px;font-size:14px;color:#222222;text-decoration:none}
.locm2 a:hover{background:#f7f7f7}
.locm2 .sep{height:1px;background:#ebebeb;margin:6px 4px}
.oni{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;height:68px;padding:0 16px;font-size:12px !important;font-size:14px;font-weight:600;color:#6a6a6a;text-decoration:none;border-bottom:2px solid transparent;box-sizing:border-box}
.oic{position:relative;display:flex}.oic .bdg{position:absolute;top:-6px;right:-12px}
.oni.on{color:#222222;border-bottom-color:#222222}
.bdg{min-width:18px;height:18px;padding:0 5px;border-radius:9px;background:#c13515;color:#ffffff;font-size:11px;font-weight:700;display:inline-flex;align-items:center;justify-content:center;box-sizing:border-box}
.bell{position:relative;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer}
.bell:hover,.me:hover{background:#f5f5f5}
.bell .bdg{position:absolute;top:2px;right:0}
.dropn{position:absolute;top:56px;right:90px;width:380px;border-radius:16px;background:#ffffff;box-shadow:0 12px 40px rgba(0,0,0,0.18);padding:10px;display:flex;flex-direction:column;z-index:40}
.dropn .it{display:flex;gap:12px;padding:10px;border-radius:10px;font-size:13px;line-height:18px;text-decoration:none;color:#222222}
.dropn .it:hover{background:#f7f7f7}
.dropn .dt{width:8px;height:8px;border-radius:50%;background:#ff385c;margin-top:6px;flex-shrink:0}
.me{display:flex;align-items:center;gap:8px;height:40px;padding:0 8px 0 4px;border-radius:20px;border:1px solid #dddddd;cursor:pointer;position:relative}
.av{width:32px;height:32px;border-radius:50%;background:#e8d9cf;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700}
.menu{position:absolute;top:48px;right:0;width:320px;border-radius:8px;background:#fbf8f3;border:1px solid #e4ded2;box-shadow:0 18px 40px rgba(19,32,58,0.16);padding:10px;display:flex;flex-direction:column;z-index:40;cursor:default}
.mm-h{display:flex;gap:12px;align-items:center;padding:8px 10px 14px;border-bottom:1px solid #e4ded2;margin-bottom:6px}
.mm-i{display:flex !important;justify-content:space-between !important;font-size:14px !important;font-weight:600;color:#13203a !important;padding:10px !important;border-radius:6px !important}
.mm-i .mu{font-weight:500;font-size:12px}
.mm-ref{display:flex !important;flex-direction:column !important;align-items:flex-start !important;gap:3px !important;margin:6px 0 4px;padding:12px 14px !important;border-radius:6px !important;background:#f5e3cc !important;border:1px solid #e6cfb2;color:#13203a !important}
.mm-ref strong{font-family:'Cormorant Garamond',Georgia,serif;font-size:20px;font-weight:500}
.mm-ref span{font-size:12px;line-height:17px;color:#3d4658}
.mm-g{font-size:10px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#8a93a3;padding:10px 10px 4px}
.menu a{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:11px 12px;border-radius:10px;font-size:14px;color:#222222;text-decoration:none}
.menu a:hover{background:#f7f7f7}
.menu .hl{background:#fff1ec;color:#a8452c;font-weight:700}
.menu .hl:hover{background:#ffe6dc}
.menu .sep{height:1px;background:#ebebeb;margin:6px 4px}
.pbar{display:flex;align-items:center;gap:8px;padding:7px 40px;background:#1f1f1f;color:#ffffff;font-size:12px}
.pbar .l{font-weight:700;letter-spacing:0.06em;text-transform:uppercase;font-size:10px;color:#b0b0b0;margin-right:4px}
.pbar span.p{display:inline-flex;align-items:center;height:26px;padding:0 12px;border-radius:13px;border:1px solid #4a4a4a;color:#dddddd;cursor:pointer}
.pbar span.p.on{background:#ffffff;color:#222222;border-color:#ffffff;font-weight:600}
.main{padding:32px 40px 56px;display:flex;flex-direction:column;gap:24px;background:#fbfbfa;min-height:900px;box-sizing:border-box}
.ttl1{margin:0;font-size:30px;font-weight:700;letter-spacing:-0.01em}
.card{background:#ffffff;border:1px solid #e6e6e6;border-radius:16px;padding:22px 24px;display:flex;flex-direction:column;gap:14px}
.sh{margin:0;font-size:18px;font-weight:700}
.trk{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative}
.ts{display:flex;align-items:center;gap:12px;padding:6px 0}
.ts .c{width:34px;height:34px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700;flex-shrink:0}
.ts.done .c{background:#237233;color:#ffffff}
.ts.now .c{background:#ffffff;border:2px solid #ff385c;color:#ff385c;box-shadow:0 0 0 5px rgba(255,56,92,0.14)}
.ts strong{font-size:15px}
.ts span.s{font-size:12px;color:#6a6a6a}
.bar{height:6px;border-radius:3px;background:#ececec;overflow:hidden}
.bar i{display:block;height:100%;background:linear-gradient(90deg,#237233,#ff385c)}
.gmb{display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:center}
.gbtn{display:inline-flex;align-items:center;gap:10px;height:50px;padding:0 20px;border-radius:12px;border:1px solid #dadce0;background:#ffffff;font-size:15px;font-weight:600;color:#222222;text-decoration:none;box-shadow:0 1px 3px rgba(0,0,0,0.08)}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.rfw{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;align-items:center;padding:36px 40px;border-radius:8px;background:#f5e3cc;border:1px solid #e6cfb2}
.rfv{display:flex;flex-direction:column;align-items:center;gap:16px}
.rfs{display:flex;gap:10px}.rfs span{display:flex;flex-direction:column;align-items:center;padding:10px 14px;border-radius:6px;background:#fbf4ea;border:1px solid #e6cfb2;font-size:12px;color:#3d4658}.rfs b{font-size:13px;color:#13203a}
.kody{display:flex;align-items:center;gap:16px;padding:18px 22px;border-radius:8px;background:#fbf4ea;border:1px solid #e6cfb2}
.tmg{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.tmc{display:flex;gap:14px;padding:20px 22px;border-radius:8px;background:#ffffff;border:1px solid #e4ded2}
.tav{width:46px;height:46px;border-radius:50%;background:#13203a;color:#ffffff;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;flex-shrink:0}
.tro{font-size:11px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#2b59d9}
.tmr{display:grid;grid-template-columns:46px minmax(0,1.2fr) minmax(0,1fr) auto;gap:16px;align-items:center;padding:16px 22px;border-top:1px solid #efeae0}.tmr:first-child{border-top:none}
.rsel{display:inline-flex;align-self:flex-start;height:30px;padding:0 12px;border-radius:9999px;border:1px solid #dcd5c7;align-items:center;font-size:13px;font-weight:600;background:#fbf8f3}
.tgs{display:flex;gap:12px}.tg2{display:flex;align-items:center;gap:6px;font-size:12px;color:#667085}.tg2 i{width:30px;height:18px;border-radius:9px;background:#dcd5c7;position:relative;display:block}.tg2 i::after{content:"";position:absolute;top:2px;left:2px;width:14px;height:14px;border-radius:50%;background:#fff}.tg2.on{color:#13203a}.tg2.on i{background:#13203a}.tg2.on i::after{left:14px}
.apv{display:flex;align-items:center;gap:24px;padding:26px 28px;border-radius:8px;background:#13203a;color:#ffffff}
.rls{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.rls span{display:flex;flex-direction:column;gap:3px;font-size:13px;line-height:19px;color:#3d4658}.rls b{color:#13203a;font-size:14px}
.vhero{display:grid;grid-template-columns:1.3fr 1fr;gap:28px;padding:30px 32px;border-radius:8px;background:#f5e3cc;border:1px solid #e6cfb2}
.vhero p{margin:0;font-size:15px;line-height:24px;color:#3d4658;max-width:560px}
.vh{margin:0;font-family:'Cormorant Garamond',Georgia,serif;font-size:38px;line-height:42px;font-weight:500;color:#13203a}
.eyb2{font-size:11px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#5b6474}
.vsafe{display:flex;flex-direction:column;gap:10px;padding:22px 24px;border-radius:6px;background:#fbf4ea;border:1px solid #e6cfb2;font-size:14px;line-height:21px;color:#3d4658;align-self:start}
.sech{font-size:12px;font-weight:700;letter-spacing:0.14em;text-transform:uppercase;color:#5b6474;margin-top:8px}
.chk{display:flex;flex-direction:column;border:1px solid #e4ded2;border-radius:8px;background:#ffffff;overflow:hidden}
.chr{display:flex;align-items:center;gap:16px;padding:16px 22px;border-top:1px solid #efeae0}.chr:first-child{border-top:none}
.cst{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;flex-shrink:0;border:1.5px solid #c9c3b6;color:#8a93a3}
.cst.done{background:#237233;border-color:#237233;color:#ffffff}.cst.now{border-color:#13203a;color:#13203a}
.g3d{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.dt3{display:flex;flex-direction:column;gap:6px;padding:24px;border-radius:18px;background:#ffffff;border:1px solid #e4ded2;text-decoration:none;color:#13203a;min-height:230px;box-sizing:border-box}
.dt3:hover{box-shadow:0 6px 20px rgba(0,0,0,0.08)}
.dt3 .k{font-size:12px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:#667085}
.dt3 b{font-size:54px;line-height:60px;font-family:'Cormorant Garamond',Georgia,serif;font-weight:500}
.dt3 .l{font-size:16px;font-weight:700}
.dt3 .s{font-size:13px;line-height:19px;color:#3d4658}
.dt3 .go{margin-top:auto;font-size:14px;font-weight:700;color:#2b59d9}
.tile{display:flex;flex-direction:column;gap:6px;padding:18px 20px;border-radius:14px;background:#ffffff;border:1px solid #e6e6e6;text-decoration:none;color:#222222}
.tile b{font-size:28px;line-height:30px}
.tile span{font-size:13px;color:#6a6a6a}
.tile .go{font-size:13px;font-weight:600;color:#222222;margin-top:auto}
.lock{opacity:0.6}
.ib{display:grid;grid-template-columns:380px 1fr;border:1px solid #e6e6e6;border-radius:16px;background:#ffffff;overflow:hidden;min-height:680px}
.ibl{border-right:1px solid #ebebeb;display:flex;flex-direction:column}
.ibi{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid #f0f0f0;cursor:pointer}
.ibi.on{background:#f7f7f7}
.ibi .a2{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;flex-shrink:0}
.ibi .ttl{display:flex;justify-content:space-between;gap:8px;font-size:14px}
.ibi .pv{font-size:13px;color:#6a6a6a;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:270px}
.ibi.un .ttl strong::after{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:#ff385c;margin-left:6px;vertical-align:1px}
.ibr{padding:24px 28px;display:flex;flex-direction:column;gap:16px}
.msg{padding:16px 18px;border-radius:14px;background:#f5f5f5;font-size:15px;line-height:23px;max-width:620px}
.slots{display:flex;gap:10px;flex-wrap:wrap}
.slot{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;width:120px;height:62px;border-radius:12px;border:1px solid #dddddd;font-size:13px;font-weight:600;background:#ffffff}
.slot span{font-size:12px;color:#6a6a6a;font-weight:500}
.cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));border-top:1px solid #ebebeb;border-left:1px solid #ebebeb}
.cal .h{padding:8px;font-size:11px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#6a6a6a;border-right:1px solid #ebebeb;border-bottom:1px solid #ebebeb;background:#fafafa}
.cal .c{min-height:96px;padding:6px;border-right:1px solid #ebebeb;border-bottom:1px solid #ebebeb;display:flex;flex-direction:column;gap:4px;box-sizing:border-box}
.cal .c.off{background:#fafafa}
.cal .n{font-size:12px;font-weight:600;color:#6a6a6a}
.ev{display:block;padding:3px 6px;border-radius:5px;font-size:11px;line-height:14px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ev.ap{background:#fff1e0;color:#9a5200;border-left:3px solid #e8740c}
.ev.sc{background:#e3eefc;color:#134a91;border-left:3px solid #2d6fd6}
.ev.gh{background:#ffffff;color:#a0a0a0;border:1px dashed #cfcfcf}
.leg{display:flex;gap:16px;font-size:12px;color:#484848;flex-wrap:wrap}
.leg i{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.path{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.pt{display:flex;flex-direction:column;gap:6px;padding:16px;border-radius:14px;border:1px solid #e6e6e6;background:#ffffff}
.pt.cur{border:2px solid #222222}
.pt.next{border:2px dashed #ff385c;background:#fff8f6}
.pt .top{display:flex;justify-content:space-between;align-items:center}
.pt strong{font-size:15px}
.pt span.d{font-size:12px;line-height:17px;color:#484848}
.tag{display:inline-flex;align-items:center;height:22px;padding:0 9px;border-radius:11px;font-size:11px;font-weight:700}
.apv{display:flex;flex-direction:column;gap:8px;padding:14px 0;border-top:1px solid #f0f0f0}
.apv:first-of-type{border-top:none}
.apv .ty{font-size:11px;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;color:#9a5200}
.apv p{margin:0;font-size:13px;line-height:19px;color:#484848}
.acts{display:flex;gap:6px}
.w2{display:grid;grid-template-columns:1fr 380px;gap:20px;align-items:start}
.vis{display:grid;grid-template-columns:auto 1fr 1fr 1fr auto;gap:28px;align-items:center}
.vis b{font-size:30px;line-height:32px}
.nl2{display:grid;grid-template-columns:360px 1fr;border:1px solid #e6e6e6;border-radius:16px;background:#ffffff;overflow:hidden;min-height:700px}
.nli{display:flex;flex-direction:column;gap:4px;padding:14px 16px;border-bottom:1px solid #f0f0f0;cursor:pointer}
.nli.on{background:#f7f7f7;box-shadow:inset 3px 0 0 #222222}
.nli .ty{font-size:11px;font-weight:700;letter-spacing:0.05em;text-transform:uppercase;color:#6a6a6a}
.nli strong{font-size:14px;line-height:19px}
.st{display:inline-flex;align-items:center;height:20px;padding:0 8px;border-radius:10px;font-size:11px;font-weight:700;align-self:flex-start}
.st.rv{background:#fff1e0;color:#9a5200}.st.ok{background:#e3f4e6;color:#1c5f2a}.st.it{background:#e3eefc;color:#134a91}
.asset{padding:20px 22px;border-radius:14px;border:1px solid #e6e6e6;background:#ffffff;font-size:15px;line-height:24px;white-space:pre-line}
.fb{display:flex;flex-direction:column;gap:8px;padding:16px;border-radius:14px;background:#f7f5f1}
.fb textarea{width:100%;height:76px;border:1px solid #d6d0c4;border-radius:10px;padding:10px 12px;font-family:inherit;font-size:14px;box-sizing:border-box;resize:none;background:#ffffff}
.nt{display:flex;gap:12px;padding:12px 0;border-top:1px solid #f0f0f0}
.nt .q{width:28px;height:28px;border-radius:50%;background:#13203a;color:#ffffff;display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.nt strong{font-size:14px;line-height:20px}
.nt span{font-size:12px;color:#6a6a6a}
.nt.new{background:#fffbe8;margin:0 -12px;padding:12px}
.set{display:grid;grid-template-columns:240px 1fr;gap:28px;align-items:start}
.sidel{display:flex;flex-direction:column;gap:2px;position:sticky;top:20px}
.sidel a{padding:10px 12px;border-radius:10px;font-size:14px;color:#222222;text-decoration:none}
.sidel a.on{background:#f0f0f0;font-weight:600}
.srow{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:14px 0;border-top:1px solid #f0f0f0;font-size:14px}
.srow:first-of-type{border-top:none}
.srow .k{display:flex;flex-direction:column;gap:2px}
.srow .k span{font-size:13px;color:#6a6a6a}
.danger{border-color:#f3c2b8}
.bred{background:#ffffff;color:#c13515;border:1px solid #c13515}
.big3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.hc{display:flex;flex-direction:column;gap:6px;padding:20px;border-radius:14px;border:1px solid #e6e6e6;background:#ffffff}
.hc strong{font-size:16px}
.hc span{font-size:13px;line-height:19px;color:#6a6a6a}
'''
G='<svg width="20" height="20" viewBox="0 0 48 48" aria-hidden="true"><path fill="#EA4335" d="M24 9.5c3.5 0 6.6 1.2 9.1 3.6l6.8-6.8C35.8 2.4 30.3 0 24 0 14.6 0 6.6 5.4 2.7 13.2l7.9 6.2C12.5 13.6 17.8 9.5 24 9.5z"/><path fill="#4285F4" d="M46.1 24.5c0-1.6-.1-3.1-.4-4.5H24v9h12.4c-.5 2.9-2.2 5.3-4.6 6.9l7.4 5.7c4.3-4 6.9-9.9 6.9-17.1z"/><path fill="#FBBC05" d="M10.6 28.6c-.5-1.4-.8-3-.8-4.6s.3-3.2.8-4.6l-7.9-6.2C1 16.6 0 20.2 0 24s1 7.4 2.7 10.8l7.9-6.2z"/><path fill="#34A853" d="M24 48c6.5 0 11.9-2.1 15.9-5.8l-7.4-5.7c-2.1 1.4-4.8 2.2-8.5 2.2-6.2 0-11.5-4.1-13.4-9.9l-7.9 6.2C6.6 42.6 14.6 48 24 48z"/></svg>'
BELL='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"></path><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"></path></svg>'
def nav(cur):
    items=[('home','Dashboard','OwnerHome.dc.html',''),('page','My business','Dashboard.dc.html',''),('inbox','Inbox','OwnerInbox.dc.html','3'),('work','Premium','OwnerPremium.dc.html','{{apN}}')]
    def badge(b):
        if b=='{{apN}}': return '<span class="bdg" style="display: {{apD}};">{{apN}}</span>'
        return f'<span class="bdg">{b}</span>' if b else ''
    IC={'home': '<path d="M4 11 12 4l8 7v9h-5v-6H9v6H4z"/>', 'page': '<path d="M4 9h16l-1.5-4h-13z"/><path d="M5 9v11h14V9"/><path d="M10 20v-6h4v6"/>', 'inbox': '<path d="M3 13h5l2 3h4l2-3h5"/><path d="M5 5h14l2 8v6H3v-6z"/>', 'work': '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/><path d="m9 15 2 2 4-4"/>'}
    h=''.join('<a href="'+u+'" class="oni '+('on' if k==cur else '')+'"><span class="oic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+IC[k]+'</svg>'+badge(b)+'</span>'+t+'</a>' for k,t,u,b in items)
    notif=[('Kody from Local AI Registry sent you a message','2 hours ago','OwnerInbox.dc.html'),('Kelly W. says you are closed Oct 3. Confirm?','3 hours ago','OwnerInbox.dc.html'),('New question: Does Lumen take HSA cards?','Yesterday','Dashboard.dc.html'),('Your AI Score went from 55 to 58','2 days ago','OwnerPremium.dc.html'),('Anna P. requested a booking for Saturday','2 days ago','OwnerInbox.dc.html')]
    nl=''.join(f'<a href="{u}" class="it"><span class="dt"></span><span style="display: flex; flex-direction: column; gap: 2px;"><span>{t}</span><span class="mu" style="font-size: 12px;">{w}</span></span></a>' for t,w,u in notif)
    return f'''<div class="pbar"><span class="l">Prototype</span><span class="l" style="margin-left: 8px; opacity: 0.7;">Plan</span><sc-for list="{{{{tiers}}}}" as="t" hint-placeholder-count="4"><span class="p {{{{t.on}}}}" onClick="{{{{t.pick}}}}">{{{{t.t}}}}</span></sc-for></div><div class="onav"><a href="OwnerHome.dc.html" class="lg">{LOGO}<span style="font-weight: 800; font-size: 16px; letter-spacing: -0.01em; color: #ff385c;">Local AI Registry</span></a><span class="locsw" onClick="{{{{tLoc}}}}"><span class="lav">L</span><span style="display: flex; flex-direction: column; line-height: 16px;"><strong style="font-size: 13px;">Lumen Aesthetics</strong><span class="mu" style="font-size: 11px;">Irvine Spectrum</span></span><span style="font-size: 9px; color: #6a6a6a;">▾</span><sc-if value="{{{{locOpen}}}}" hint-placeholder-val="{{{{ false }}}}"><span class="locm2"><span class="mu" style="font-size: 11px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; padding: 8px 12px 4px;">Your businesses</span><a href="OwnerHome.dc.html"><span class="lav">L</span><span style="display: flex; flex-direction: column;"><strong>Lumen Aesthetics</strong><span class="mu" style="font-size: 12px;">Irvine Spectrum · Tier 3</span></span><span style="margin-left: auto; color: #237233; font-weight: 700;">✓</span></a><span class="sep"></span><a href="AddLocation.dc.html"><span class="lav" style="background: #f1f1f1; color: #222222;">+</span><span style="display: flex; flex-direction: column;"><strong>Add a location</strong><span class="mu" style="font-size: 12px;">Another Lumen address</span></span></a><a href="Home.dc.html"><span class="lav" style="background: #f1f1f1; color: #222222;">⌕</span><span style="display: flex; flex-direction: column;"><strong>Claim another business</strong><span class="mu" style="font-size: 12px;">Search for it by name</span></span></a></span></sc-if></span>{h}
<span style="margin-left: auto; display: flex; align-items: center; gap: 10px;"><sc-if value="{{{{showUp}}}}" hint-placeholder-val="{{{{ true }}}}"><a href="Upgrade.dc.html" class="btn b-sm b-coral">{{{{upLbl}}}}</a></sc-if><span class="bell" onClick="{{{{tBell}}}}">{BELL}<span class="bdg">5</span></span><span class="me" onClick="{{{{tMe}}}}"><span class="av">PN</span><span style="font-size: 9px; color: #6a6a6a;">▾</span><sc-if value="{{{{meOpen}}}}" hint-placeholder-val="{{{{ false }}}}"><span class="menu"><span class="mm-h"><span class="av" style="width: 40px; height: 40px;">PN</span><span style="display: flex; flex-direction: column; line-height: 18px;"><strong style="font-size: 15px;">Dr. Priya Nair</strong><span class="mu" style="font-size: 12px;">Owner · Lumen Aesthetics</span></span></span><a href="Main.dc.html" class="mm-i">View my public page<span class="mu">↗</span></a><a href="OwnerReferral.dc.html" class="mm-ref"><strong>Refer a business, pay less</strong><span>15% off your plan for each one, forever. Stack them until it's free.</span></a><span class="mm-g">Account</span><a href="OwnerTeam.dc.html" class="mm-i">Team<span class="mu">Yours and ours</span></a><a href="Billing.dc.html" class="mm-i">Plan and billing</a><a href="OwnerNotes.dc.html" class="mm-i">AI notes</a><a href="OwnerSettings.dc.html" class="mm-i">Settings</a><a href="OwnerHelp.dc.html" class="mm-i">Help center</a><span class="sep"></span><a href="Home.dc.html" class="mm-i" style="color: #667085;">Sign out</a></span></sc-if></span></span>
<sc-if value="{{{{bellOpen}}}}" hint-placeholder-val="{{{{ false }}}}"><div class="dropn"><span style="display: flex; justify-content: space-between; padding: 8px 10px;"><strong>Notifications</strong><a href="OwnerSettings.dc.html" style="font-size: 12px;">Settings</a></span>{nl}</div></sc-if></div>
'''
BASEJS='''    const S = this.state || {};
    const tier = S.tier === undefined ? TIER0 : S.tier;
    const TN = ['Free', 'Fix', 'Trust', 'Authority'];
    const tiers = TN.map((t, i) => ({ t: i === 0 ? 'Free plan' : 'Tier ' + (i + 1) + ' · ' + t, on: i === tier ? 'on' : '', pick: () => this.setState({ tier: i }) }));
    const base = { tiers, showUp: true, upLbl: 'See plans', meOpen: !!S.me, bellOpen: !!S.bell, locOpen: !!S.loc, tLoc: () => this.setState({ loc: !S.loc, me: false, bell: false }), tMe: () => this.setState({ me: !S.me, bell: false, loc: false }), tBell: () => this.setState({ bell: !S.bell, me: false, loc: false }), apN: tier === 0 ? '' : String(3 + tier), apD: tier === 0 ? 'none' : 'inline-flex', tierName: TN[tier], isFree: tier === 0, isPaid: tier > 0 };
'''
def build(fname,cur,title,body,js,tier0=2):
    B=nav(cur)+f'<div class="main">{body}</div>'
    J=BASEJS.replace('TIER0',str(tier0))+js
    open(P+fname,'w').write(page(title,CSS,B,J)); print(fname)
# ---------- HOME ----------
home=f'''<div style="display: flex; justify-content: space-between; align-items: flex-end;"><div style="display: flex; flex-direction: column; gap: 4px;"><h1 class="ttl1">Welcome, Dr. Nair</h1><span class="mu" style="font-size: 15px;">Lumen Aesthetics · Irvine Spectrum</span></div><span style="display: flex; gap: 12px; align-items: center;"><span class="mu" style="font-size: 12px; cursor: pointer;" onClick="{{{{tVer}}}}">Prototype: {{{{verLbl}}}}</span><a href="Main.dc.html" class="btn b-sm">View my page</a></span></div>
<sc-if value="{{{{notVer}}}}" hint-placeholder-val="{{{{ true }}}}"><div class="vhero"><div style="display: flex; flex-direction: column; gap: 12px;"><svg viewBox="0 0 140 110" width="140" height="110" aria-hidden="true" fill="none" stroke="#13203a" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="22" y="36" width="84" height="62" fill="#fbf4ea"/><path d="M16 36h96l-6-14H22z" fill="#e5482d" fill-opacity="0.18" stroke="#e5482d"/><rect x="54" y="66" width="20" height="32" fill="#dfe8f5"/><rect x="30" y="50" width="16" height="14"/><rect x="82" y="50" width="16" height="14"/><path d="M8 98h124" stroke-width="1"/><circle cx="108" cy="30" r="14" fill="#237233" stroke="#237233"/><path d="M101 30l5 5 9-10" stroke="#fff" stroke-width="2.2"/></svg><span class="eyb2">Last step · 3 of 4 done</span><h2 class="vh">Verify that you own Lumen</h2><p>Connect the Google account that manages Lumen's Business Profile. Until you verify, your answers do not rank first and someone else could dispute the page.</p><span style="display: flex; gap: 14px; align-items: center; flex-wrap: wrap;"><a href="Verify.dc.html" class="btn b-dark" style="height: 52px; padding: 0 26px; font-size: 15px;">Connect Google Business Profile ⟶</a><a href="ClaimIssue.dc.html" style="font-size: 14px; font-weight: 600;">Other ways to verify</a></span></div><div class="vsafe"><strong style="font-size: 16px;">We won't touch your Google profile.</strong><span>✓ Connecting only confirms you're the owner.</span><span>✓ Nothing changes on Google until you pick a plan and approve each change.</span><span>✓ Disconnect anytime in Settings.</span></div></div></sc-if>
<sc-if value="{{{{isVer}}}}" hint-placeholder-val="{{{{ false }}}}"><div style="display: flex; align-items: center; gap: 10px; font-size: 14px; color: #1c5f2a; font-weight: 700;"><span style="width: 22px; height: 22px; border-radius: 50%; background: #237233; color: #fff; display: inline-flex; align-items: center; justify-content: center; font-size: 12px;">✓</span>Verified owner · connected to Google Business Profile</div></sc-if>
<span class="sech">Needs you today</span>
<div class="g3d"><a href="OwnerInbox.dc.html" class="dt3"><span class="k">Customers</span><b>5</b><span class="l">people waiting on you</span><span class="s">2 booking requests · 2 questions · 1 heads-up to confirm</span><span class="go">Open inbox ›</span></a>
<a href="OwnerPremium.dc.html" class="dt3"><span class="k">Approvals</span><b>{{{{apHome}}}}</b><span class="l">{{{{apHomeL}}}}</span><span class="s">{{{{apUpS}}}}</span><span class="go">{{{{apGo}}}}</span></a>
<a href="Dashboard.dc.html" class="dt3"><span class="k">My business</span><b>9</b><span class="l">facts need you to confirm</span><span class="s">6 AI guesses and 3 visitor suggestions. Confirmed facts are what AI repeats.</span><span class="go">Review them ›</span></a></div>
<div class="kody"><svg viewBox="0 0 64 64" width="56" height="56" aria-hidden="true" fill="none" stroke="#13203a" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="32" cy="32" r="28" fill="#dfe8f5" stroke="none"/><circle cx="32" cy="26" r="9" fill="#fbf4ea"/><path d="M16 52c3-9 9-13 16-13s13 4 16 13" fill="#fbf4ea"/><path d="M48 14l4-4M51 20h5M44 10V5" stroke="#e5482d"/></svg><span style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1;"><strong style="font-size: 16px;">Not sure where to start? Kody is here.</strong><span class="mu" style="font-size: 14px;">Kody Muffoletto, your rep, can walk you through all of this in 15 minutes.</span></span><a href="#" class="btn b-dark">Book with Kody</a><a href="mailto:support@localairegistry.com" style="font-size: 13px; font-weight: 600; white-space: nowrap;">Or contact support</a></div>
<span class="sech">Finish setting up Lumen</span>
<div class="chk"><sc-for list="{{{{todo}}}}" as="x" hint-placeholder-count="5"><div class="chr"><span class="cst {{{{x.c}}}}">{{{{x.ic}}}}</span><span style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1;"><strong style="font-size: 15px;">{{{{x.t}}}}</strong><span class="mu" style="font-size: 13px;">{{{{x.d}}}}</span></span><a href="{{{{x.h}}}}" class="btn b-sm" onClick="{{{{x.pick}}}}">{{{{x.b}}}}</a></div></sc-for>
<sc-if value="{{{{vOpen}}}}" hint-placeholder-val="{{{{ false }}}}">'''
exec(open('/tmp/gen/verified.py').read())
home += VER + '</sc-if></div>'
build('OwnerHome.dc.html','home','Owner home',home,'''    const apH = [69, 12, 18, 21][tier], more = [69, 38, 12, 0][tier];
'''+VJS+'''    const ver = !!S.ver, vOpen = !!S.vOpen;
    const TD = [['Verify ownership', ver ? 'Done. Your answers rank first.' : 'Connect Google Business Profile. About 30 seconds.', ver, ver ? 'Done' : 'Verify', 'Verify.dc.html', null],
      ['Add the Verified badge to your website', 'Points AI to your verified record. Without it, AI keeps pulling old info from other sites.', !!(S.chk || S.md), vOpen ? 'Hide code' : 'Get the code', '#verified', () => this.setState({ vOpen: !vOpen })],
      ['Add the schema code to your homepage', 'Tells ChatGPT, Gemini and Claude which facts are the right ones: yours, verified.', !!S.chk, vOpen ? 'Hide code' : 'Get the code', '#verified', () => this.setState({ vOpen: !vOpen })],
      ['Invite your marketing person', 'They get the approvals, so work never waits on you.', false, 'Invite', 'OwnerSettings.dc.html#team', null],
      ['Get your free AI audit', 'What ChatGPT, Gemini and Claude say about Lumen. Kody reviews it with you.', false, 'Run it free', 'Next.dc.html', null]];
    const todo = TD.map((x, i) => ({ t: x[0], d: x[1], c: x[2] ? 'done' : (i === 0 && !ver ? 'now' : ''), ic: x[2] ? '✓' : String(i + 1), b: x[3], h: x[4], pick: x[5] }));
    return Object.assign(base, vs, { todo, vOpen, notVer: !ver, isVer: ver, verLbl: ver ? 'verified' : 'not verified', tVer: () => this.setState({ ver: !ver }), apHome: String(apH), apHomeL: tier ? 'pieces waiting for your approval' : 'pieces of work could be done this month', apUpS: tier === 0 ? 'On Free, none of it goes out. Fix unlocks 31, Authority unlocks all 69.' : more ? more + ' more pieces we could do this month on ' + (tier === 0 ? 'Fix, Trust or Authority' : TN[Math.min(3, tier + 1)]) + '. Upgrade to unlock them.' : 'You have everything. Approve and it goes out.', apGo: tier ? 'Review and approve ›' : 'See what we would do ›' });''')
# ---------- INBOX ----------
inbox='''<h1 class="ttl1">Inbox</h1><div class="ib"><div class="ibl"><div style="display: flex; gap: 6px; padding: 12px 16px; border-bottom: 1px solid #ebebeb;"><span class="tag" style="background: #222222; color: #ffffff; height: 28px; padding: 0 12px; border-radius: 14px;">All</span><span class="tag" style="background: #f1f1f1; color: #484848; height: 28px; padding: 0 12px; border-radius: 14px;">Bookings</span><span class="tag" style="background: #f1f1f1; color: #484848; height: 28px; padding: 0 12px; border-radius: 14px;">Locals</span><span class="tag" style="background: #f1f1f1; color: #484848; height: 28px; padding: 0 12px; border-radius: 14px;">Local AI Registry</span></div>
<sc-for list="{{msgs}}" as="m" hint-placeholder-count="5"><div class="ibi {{m.cls}}" onClick="{{m.pick}}"><span class="a2" style="background: {{m.bg}};">{{m.i}}</span><span style="display: flex; flex-direction: column; gap: 2px; min-width: 0; flex-grow: 1;"><span class="ttl"><strong>{{m.n}}</strong><span class="mu" style="font-size: 12px; white-space: nowrap;">{{m.w}}</span></span><span class="pv">{{m.p}}</span></span></div></sc-for></div>
<div class="ibr"><span style="display: flex; align-items: center; gap: 12px;"><span class="av" style="width: 44px; height: 44px; background: {{cur.bg}};">{{cur.i}}</span><span style="display: flex; flex-direction: column;"><strong style="font-size: 16px;">{{cur.n}}</strong><span class="mu" style="font-size: 13px;">{{cur.sub}}</span></span></span>
<div style="display: flex; flex-wrap: wrap; gap: 8px 18px; padding: 12px 14px; border-radius: 12px; background: #f7f7f7; font-size: 13px; max-width: 620px;"><span><span class="mu">Name </span><strong>{{ct.n}}</strong></span><span><span class="mu">Email </span><a href="#">{{ct.e}}</a></span><span><span class="mu">Phone </span>{{ct.p}}</span><span class="mu" style="flex-basis: 100%;">{{ct.s}}</span></div>
<div class="msg" style="white-space: pre-line;">{{cur.body}}</div>
<sc-if value="{{isKody}}" hint-placeholder-val="{{ true }}"><div style="display: flex; flex-direction: column; gap: 10px; padding: 16px 18px; border: 1px solid #e6e6e6; border-radius: 14px; max-width: 620px;"><span style="display: flex; justify-content: space-between; align-items: center;"><strong style="font-size: 15px;">30 minutes with Kody</strong><span class="mu" style="font-size: 12px;">calendly.com/kody-lair/30min</span></span><span class="slots"><span class="slot">Mon, Sep 28<span>10:00 AM</span></span><span class="slot">Mon, Sep 28<span>2:30 PM</span></span><span class="slot">Tue, Sep 29<span>11:00 AM</span></span><span class="slot">Wed, Sep 30<span>9:30 AM</span></span></span><a href="#" class="btn b-sm b-dark" style="align-self: flex-start;">Open Calendly to pick a time</a></div></sc-if>
<sc-if value="{{isHU}}" hint-placeholder-val="{{ false }}"><span style="display: flex; gap: 8px;"><a href="Edit.dc.html" class="btn b-sm b-dark">Yes, we're closed Oct 3</a><span class="btn b-sm">No, we're open</span></span></sc-if>
<sc-if value="{{isBook}}" hint-placeholder-val="{{ false }}"><span style="display: flex; gap: 8px;"><span class="btn b-sm b-dark">Accept and reply</span><span class="btn b-sm">Suggest another time</span><span class="btn b-sm">Decline</span></span></sc-if>
<div style="margin-top: auto; display: flex; gap: 10px; align-items: center; padding-top: 16px; border-top: 1px solid #ebebeb;"><span style="flex-grow: 1; height: 46px; border: 1px solid #dddddd; border-radius: 23px; display: flex; align-items: center; padding: 0 16px; font-size: 14px; color: #8a8a8a;">Write a reply</span><span class="btn b-sm b-dark">Send</span></div></div></div>'''
injs='''    const KICK = ['SL', '#fde6e6', 'Steve Lee, Local AI Registry', 'Today', 'Lumen Aesthetics: official kickoff, your team and what is next', 'Welcome email · sent when your plan starts', 'Dr. Nair,\\n\\nFirst, thank you for your trust. We are officially kicking things off, and this email lays out the whole plan in one place.\\n\\nYour team from day one:\\n· Kody Muffoletto, your guide. Your first call for anything.\\n· Caron Cooper, SVP Web Development and Semantic SEO. Your website and content.\\n· Clinton Adeleke, CPO. Installs our AI code on your site and photos.\\n· Eric Sim, COO. Billing.\\n· Bridgette DeBrino, VP Sales and Marketing. Trade shows and press.\\n\\nWhat happens first:\\n1. Everything we make shows up in Premium. Nothing goes out until you approve it.\\n2. Your first month of work is already on the calendar.\\n3. Your AI Score is 58 today. Your monthly report shows where it goes from here.\\n\\nThe faster we get your feedback, the faster AI gets Lumen right. Here we go.\\n\\nSteve', 'x'];
    const M = [
      ['KM', '#dfe8f5', 'Kody from Local AI Registry', '2 hours ago', 'Hey Dr. Nair, want to set up a time?', 'Your Local AI Registry guide', 'Hey Dr. Nair, congrats on claiming Lumen! I\\'m Kody, your guide at Local AI Registry. Want to grab 30 minutes this week? I\\'ll walk you through what ChatGPT and Gemini say about Lumen right now, the 3 things they get wrong, and what I\\'d fix first. No pressure to buy anything. Pick any time that works below.', 'k'],
      ['KW', '#fff1e0', 'kellyw_irvine · Heads-up', '3 hours ago', 'Says you are closed Saturday, Oct 3. Confirm?', 'Posted on your page under Locals', 'Kelly posted a heads-up: "Closed Saturday, Oct 3 for staff training. Google still shows them open." Confirming turns it into a solid fact on your page.', 'h'],
      ['AP', '#fde6ee', 'anna_irvine_22 · Booking request', '2 days ago', 'Lip filler, Saturday morning if possible', 'Requested through your page', 'Hi! I\\'d like to book lip filler, ideally a half syringe, Saturday morning. First time. Is Dr. Nair available?', 'b'],
      ['CW', '#eef2fb', 'curious_in_woodbridge · Question', 'Yesterday', 'Does Lumen take HSA cards?', 'Posted on your page under Locals', 'Priya S. asked: "Does Lumen take HSA cards?" Two locals said yes. An owner answer ranks first and is what AI will repeat.', 'q'],
      ['LA', '#ffe6ea', 'Local AI Registry', 'Sep 26', 'Welcome to Local AI Registry', 'Account', 'Your page is claimed. Verify ownership by connecting Google Business Profile to finish setup.', 'w']
    ];
    const CT = { 'Steve Lee, Local AI Registry': ['Steve Lee', 'steve@localairegistry.com', '(347) 292-9294', 'Your account team'], 'Kody from Local AI Registry': ['Kody Muffoletto', 'kody@localairegistry.com', '(949) 555-0110', 'Your Local AI Registry guide'], 'kellyw_irvine · Heads-up': ['Kelly W.', 'kelly.w.irvine@gmail.com', 'Not shared', 'Posted a heads-up on your page · 14 posts'], 'anna_irvine_22 · Booking request': ['Anna Park', 'anna.park22@gmail.com', '(714) 555-0132', 'Booked through your page · first visit · found you on ChatGPT'], 'curious_in_woodbridge · Question': ['Priya S.', 'priya.s.oc@gmail.com', '(949) 555-0187', 'Asked on your page · 2 people agreed'], 'Local AI Registry': ['Local AI Registry', 'hello@localairegistry.com', '', 'Account'] };
    if (base.isPaid) M.unshift(KICK);
    const ib = S.ib || 0;
    const msgs = M.map((m, i) => ({ i: m[0], bg: m[1], n: m[2], w: m[3], p: m[4], cls: (i === ib ? 'on ' : '') + (i < (base.isPaid ? 4 : 3) ? 'un' : ''), pick: () => this.setState({ ib: i }) }));
    const c = M[ib];
    const ct = CT[c[2]] || ['', '', '', ''];
    return Object.assign(base, { msgs, ct: { n: ct[0], e: ct[1], p: ct[2] || 'Not shared', s: ct[3] }, cur: { i: c[0], bg: c[1], n: c[2], sub: c[5], body: c[6] }, isKody: c[7] === 'k', isHU: c[7] === 'h', isBook: c[7] === 'b' });'''
build('OwnerInbox.dc.html','inbox','Inbox',inbox,injs)
exec(open('/tmp/gen/premium.py').read())
# ---------- SETTINGS ----------
sett=f'''<h1 class="ttl1">Settings</h1><div class="set"><div class="sidel"><a href="#acct" class="on">Account</a><a href="#conn">Connected accounts</a><a href="#bill">Plan and billing</a><a href="OwnerTeam.dc.html">Team</a><a href="#notif">Notifications</a><a href="#data">Your data</a><a href="OwnerHelp.dc.html">Help center</a></div>
<div style="display: flex; flex-direction: column; gap: 20px;">
<div class="card" id="acct"><h2 class="sh">Account</h2><div><div class="srow"><span class="k"><strong>Name</strong><span>Dr. Priya Nair</span></span><a href="#">Edit</a></div><div class="srow"><span class="k"><strong>Email</strong><span>priya@lumenirvine.com</span></span><a href="#">Edit</a></div><div class="srow"><span class="k"><strong>Phone</strong><span>(949) 555-0148 · used to sign in</span></span><a href="#">Edit</a></div></div></div>
<div class="card" id="conn"><h2 class="sh">Connected accounts</h2><div><div class="srow"><span class="k" style="flex-direction: row; align-items: center; gap: 12px;">{G}<span style="display: flex; flex-direction: column;"><strong>Google Business Profile</strong><span>Connected Sep 26 · read-only until you approve work on a plan</span></span></span><span class="btn b-sm bred">Disconnect</span></div><div class="srow"><span class="k"><strong>Instagram</strong><span>Turn your posts into updates on your page</span></span><span class="btn b-sm">Connect</span></div><div class="srow"><span class="k"><strong>Facebook</strong><span>Not connected</span></span><span class="btn b-sm">Connect</span></div><div class="srow"><span class="k"><strong>Your website</strong><span>lumenirvine.com · verified by DNS</span></span><span class="btn b-sm">Manage</span></div></div></div>
<div class="card" id="bill"><h2 class="sh">Plan and billing</h2><div><div class="srow"><span class="k"><strong>{{{{tierLbl}}}}</strong><span>No contract. Cancel anytime.</span></span><a href="Upgrade.dc.html" class="btn b-sm">Change plan</a></div><div class="srow"><span class="k"><strong>Payment method</strong><span>Visa ending in 4417</span></span><a href="#">Update</a></div><div class="srow"><span class="k"><strong>Invoices</strong><span>Download past invoices</span></span><a href="#">View</a></div></div></div>
<div class="card" id="team" style="flex-direction: row; align-items: center; justify-content: space-between;"><span style="display: flex; flex-direction: column; gap: 3px;"><h2 class="sh">Team</h2><span class="mu" style="font-size: 13px;">Your team at Lumen, what each person can do, and your Local AI Registry team.</span></span><a href="OwnerTeam.dc.html" class="btn b-sm">Open Team ›</a></div>
<div class="card" id="notif"><h2 class="sh">Notifications</h2><div><div class="srow"><span class="k"><strong>New questions and heads-ups</strong><span>Text and email</span></span><a href="#">Edit</a></div><div class="srow"><span class="k"><strong>Booking requests</strong><span>Text, right away</span></span><a href="#">Edit</a></div><div class="srow"><span class="k"><strong>Weekly AI report</strong><span>Email, Mondays</span></span><a href="#">Edit</a></div></div></div>
<div class="card danger" id="data"><h2 class="sh">Your data</h2><div><div class="srow"><span class="k"><strong>Download all your data</strong><span>Your page, edits, answers, messages and AI notes, as a ZIP file</span></span><span class="btn b-sm">Request download</span></div><div class="srow"><span class="k"><strong>Delete your account</strong><span>Removes your login, messages and AI notes. Your public page stays live and goes back to unclaimed, so anyone can claim it again.</span></span><span class="btn b-sm bred">Delete account</span></div></div></div>
</div></div>'''
sjs='''    const TB = ['Free plan', 'Tier 2 · Fix', 'Tier 3 · Trust', 'Tier 4 · Authority'];
    return Object.assign(base, { tierLbl: TB[tier] });'''
build('OwnerSettings.dc.html','','Settings',sett,sjs)
# ---------- REFERRAL + CASHBACK ----------
ref='''<div class="rfw"><div style="display: flex; flex-direction: column; gap: 16px;"><span class="eyb2">Referral program</span><h1 class="ttl1" style="font-size: 52px; line-height: 56px;">Refer a business.<br>Pay <em style="color: #e5482d;">less</em>, forever.</h1><p style="margin: 0; font-size: 17px; line-height: 27px; color: #3d4658; max-width: 560px;">Every business you refer that starts a plan takes 15% off your bill, for as long as they stay. It stacks. Refer enough of them and your plan is free.</p>
<div style="display: flex; gap: 12px; align-items: center; margin-top: 8px;"><a href="#" class="btn b-dark" style="height: 52px; padding: 0 26px; font-size: 15px;">Book a call to refer someone ⟶</a><span class="mu" style="font-size: 14px;">Or send them your link below.</span></div>
<div style="display: flex; align-items: center; gap: 10px; margin-top: 6px;"><span style="height: 46px; flex: 1; max-width: 460px; border: 1px solid #dcd5c7; border-radius: 6px; background: #ffffff; display: flex; align-items: center; padding: 0 14px; font-size: 14px;"><a href="RefLanding.dc.html">localairegistry.com/r/lumen-priya</a></span><span class="btn b-sm">Copy link</span></div></div>
<div class="rfv"><svg viewBox="0 0 260 170" width="260" height="170" aria-hidden="true" fill="none" stroke="#13203a" stroke-width="1.4"><rect x="16" y="70" width="70" height="80" fill="#fbf4ea"/><path d="M10 70h82l-6-14H16z" fill="#e5482d" fill-opacity="0.2" stroke="#e5482d"/><rect x="40" y="110" width="22" height="40" fill="#dfe8f5"/><rect x="174" y="70" width="70" height="80" fill="#fbf4ea"/><path d="M168 70h82l-6-14h-70z" fill="#e5482d" fill-opacity="0.2" stroke="#e5482d"/><rect x="198" y="110" width="22" height="40" fill="#dfe8f5"/><path d="M96 100c24-30 44-30 68 0" stroke-dasharray="4 4"/><path d="M158 94l6 6-8 3" /><circle cx="130" cy="62" r="18" fill="#f5e3cc"/><text x="130" y="67" font-size="13" text-anchor="middle" fill="#13203a" stroke="none" font-family="Figtree,sans-serif" font-weight="700">15%</text><path d="M4 150h252" stroke-width="1"/></svg><div class="rfs"><span><b>1 referral</b> 15% off</span><span><b>3 referrals</b> 45% off</span><span><b>7 referrals</b> free</span></div></div></div>
<div class="card" style="flex-direction: row; align-items: center; gap: 18px; padding: 18px 22px;"><span style="display: flex; flex-direction: column; gap: 3px; flex-grow: 1;"><strong style="font-size: 15px;">Want to offer your customers cashback?</strong><span class="mu" style="font-size: 14px;">Our partner OrbitBack runs cashback programs for local businesses. It is a separate company.</span></span><a href="#" class="btn b-sm">Book a call with OrbitBack</a></div>'''
build('OwnerReferral.dc.html','','Referral program',ref,'    return base;')

OURS=[('KM','Your rep','Kody Muffoletto','Account Executive','kody@localairegistry.com','Your first call for anything. Book time, ask questions, get unstuck.'),('C','Onboarding and setup','Caron','AI Onboarding and Readiness Specialist','caron@localairegistry.com','Setup, getting your record right, and making sure you see results.'),('ES','Customer support','Eric Sim','COO','eric@localairegistry.com','Billing, invoices, account changes, and anything that needs an answer today.'),('CA','Technical','Clinton Adeleke','CPO','clinton@localairegistry.com','Bugs and technical issues. If something here is broken, tell Clinton.'),('BD','Partnerships','Bridgette DeBrino','VP of Marketing and Sales','bridgette@localairegistry.com','Multi-location deals, co-branding and referrals.'),('SL','Strategy','Steve Lee','Founder and CEO','steve.lee@localairegistry.com','How your business shows up inside AI answers, and the method behind your AI Score.')]
oc=''.join(f'<div class="tmc"><span class="tav">{i}</span><span style="display: flex; flex-direction: column; gap: 2px;"><span class="tro">{r}</span><strong style="font-size: 16px;">{n}</strong><span class="mu" style="font-size: 13px;">{ti}</span><a href="mailto:{e}" style="font-size: 13px; font-weight: 600;">{e}</a><span style="font-size: 13px; line-height: 19px; color: #3d4658; margin-top: 4px;">{d}</span></span></div>' for i,r,n,ti,e,d in OURS)
THEIRS=[('PN','Dr. Priya Nair','priya@lumenirvine.com','Owner','Everything, including billing and removing people',[1,1,1,1]),('MO','Maya Ortiz','maya@lumenirvine.com','Front desk','Answers locals and replies in the inbox',[0,0,1,0]),('NR','Nadia Rahimi, RN','Invite pending, sent Sep 26','Team member','Shows on the page as a nurse injector',[0,0,0,0]),('JL','Jordan Lee, NP','No email yet','Team member','Shows on the page as a nurse injector',[0,0,0,0])]
tr=''
for i,n,e,role,can,tg in THEIRS:
    tgs=''.join(f'<span class="tg2 {"on" if v else ""}"><i></i>{lab}</span>' for v,lab in zip(tg,['Approvals','Monthly report','Weekly summary','Billing']))
    tr+=f'<div class="tmr"><span class="tav" style="background: #e4ded2; color: #13203a;">{i}</span><span style="display: flex; flex-direction: column; gap: 2px; min-width: 0;"><strong style="font-size: 15px;">{n}</strong><span class="mu" style="font-size: 12px;">{e}</span></span><span style="display: flex; flex-direction: column; gap: 2px;"><span class="rsel">{role} ▾</span><span class="mu" style="font-size: 12px;">{can}</span></span><span class="tgs">{tgs}</span></div>'
team=f'''<div style="display: flex; flex-direction: column; gap: 6px;"><h1 class="ttl1" style="font-size: 48px; line-height: 52px;">Team</h1><span class="mu" style="font-size: 15px;">Who works on Lumen, what each person can do, and who to reach at Local AI Registry.</span></div>
<span class="sech">Your team at Lumen</span>
<div class="chk">{tr}</div>
<div class="apv"><span style="display: flex; flex-direction: column; gap: 6px; flex-grow: 1;"><strong style="font-family: 'Cormorant Garamond', Georgia, serif; font-size: 30px; line-height: 34px; font-weight: 500;">Add someone who can approve when you cannot.</strong><span style="font-size: 14px; line-height: 21px; color: #d8dde8;">Most of what we draft waits for a sign-off. Whoever you add gets the same approval requests and can approve, decline or ask for a change.</span></span><span style="display: flex; gap: 8px;"><span style="height: 46px; width: 260px; border-radius: 6px; background: #ffffff; display: flex; align-items: center; padding: 0 14px; font-size: 14px; color: #8a8a8a;">name@lumenirvine.com</span><span style="height: 46px; padding: 0 20px; border-radius: 9999px; background: #ffffff; color: #13203a; display: inline-flex; align-items: center; font-size: 14px; font-weight: 700;">Send invite</span></span></div>
<div class="card" style="gap: 8px;"><strong style="font-size: 15px;">What each role can do</strong><div class="rls"><span><b>Owner</b>Everything, including billing and removing people</span><span><b>Admin</b>Everything except transferring ownership</span><span><b>Marketing</b>Approve work, edit the page, see reports</span><span><b>Front desk</b>Answer locals and reply in the inbox</span></div></div>
<span class="sech">Your Local AI Registry team</span>
<div class="tmg">{oc}</div>'''
build('OwnerTeam.dc.html','','Team',team,'    return base;')
# ---------- HELP ----------
helpb='''<div style="display: flex; flex-direction: column; align-items: center; gap: 14px; padding: 30px 0 10px; text-align: center;"><h1 class="ttl1" style="font-size: 36px;">How can we help?</h1><span style="width: 640px; height: 54px; border: 1px solid #dddddd; border-radius: 27px; display: flex; align-items: center; padding: 0 20px; font-size: 15px; color: #8a8a8a; background: #ffffff; box-shadow: 0 4px 14px rgba(0,0,0,0.06);">Search the help center</span></div>
<div class="big3"><div class="hc"><strong>Getting started</strong><span>Claiming, confirming your info, verifying ownership</span></div><div class="hc"><strong>Editing your page</strong><span>Pencils, tracked changes, pushing changes to AI</span></div><div class="hc"><strong>Locals and questions</strong><span>Answering, heads-ups, reporting a post</span></div><div class="hc"><strong>Plans and billing</strong><span>What each tier includes, upgrading, canceling</span></div><div class="hc"><strong>Approvals and AI notes</strong><span>How feedback teaches AI your voice</span></div><div class="hc"><strong>Ownership disputes</strong><span>When someone else claimed your business</span></div></div>
<div class="card" style="flex-direction: row; align-items: center; gap: 20px;"><span style="display: flex; flex-direction: column; gap: 4px; flex-grow: 1;"><strong style="font-size: 16px;">Still stuck?</strong><span class="mu" style="font-size: 14px;">Message support, or book time with Kody, your Local AI Registry guide.</span></span><a href="OwnerInbox.dc.html" class="btn b-sm b-dark">Message support</a><a href="OwnerInbox.dc.html" class="btn b-sm">Book with Kody</a></div>'''
build('OwnerHelp.dc.html','','Help center',helpb,'    return base;')
