import re
TRI='<svg width="30" height="30" viewBox="0 0 30 30" fill="none" aria-hidden="true"><path d="M15 3 27.5 27h-8.2L15 18.6 10.7 27H2.5L15 3Z" fill="#2b59d9"></path><path d="M15 18.6 19.3 27h-8.6L15 18.6Z" fill="#e5482d"></path></svg>'
FONT='<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&display=swap" rel="stylesheet">'
EXTRA='\n/*palette:lair*/body{background:#f3efe7 !important}\nh1,.ttl1,h2.h2{font-family:"Cormorant Garamond",Georgia,serif !important;font-weight:500 !important;letter-spacing:0 !important}\n'
MAP=[('#ff385c','#e5482d'),('#e61e4d','#e5482d'),('#d70466','#c93b22'),('#bd1e59','#c93b22'),('#fff0f3','#fcebe6'),('#ffe8ed','#fcebe6'),
 ('#222222','#13203a'),('#484848','#3d4658'),('#6a6a6a','#667085'),('#717171','#667085'),
 ('#ebebeb','#e4ded2'),('#e6e6e6','#e4ded2'),('#e3e3e3','#e4ded2'),('#dddddd','#dcd5c7'),
 ('#f7f7f7','#f3efe7'),('#fafafa','#f7f4ee'),('#fbfbfa','#f7f4ee'),('#f3f3f3','#efeae0'),('#f5f5f5','#efeae0'),('#efefef','#ebe5d9'),('#f0f0f0','#ece6da')]
def apply(s):
    s=re.sub(r'<svg width="30" height="30" viewBox="0 0 30 30" fill="none" aria-hidden="true"><rect x="2" y="2" width="26" height="26" rx="7" fill="#ff385c"></rect>.*?</svg>',TRI,s,flags=re.S)
    s=re.sub(r'(<rect[^>]*rx="\d+"[^>]*fill="#ff385c"[^>]*>\s*</rect>)(<path d="M8\.5 21V9[^"]*"[^>]*></path><path[^>]*></path>)',lambda m:'',s)
    s=re.sub(r'color: #ff385c;">Local AI Registry','color: #13203a; font-weight: 600;">Local AI Registry',s)
    s=re.sub(r'(<header[^>]*?)background: #ffffff',r'\1background: #f3efe7',s)
    s=re.sub(r'(\.(?:onav|top|nav|hdr|bar0)\{[^}]*?)background:#ffffff',r'\1background:#f3efe7',s)
    s=s.replace('background: #ffffff; position: relative;">','background: #f3efe7; position: relative;">')
    for a,b in MAP: s=s.replace(a,b).replace(a.upper(),b)
    if 'Cormorant+Garamond' not in s and '</helmet>' in s: s=s.replace('</helmet>',FONT+'</helmet>',1)
    if '/*palette:lair*/' not in s: s=s.replace('</style>',EXTRA+'</style>',1)
    if '/*wrap*/' not in s: s=s.replace('</style>','\n/*wrap*/h1,h2,h3,.ttl1,.T,.T2,.sh{text-wrap:balance}p,.v4-sub,.sub,.lead{text-wrap:pretty}\n</style>',1)
    return s
if __name__=='__main__':
    import glob,os
    os.chdir('/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project')
    for f in glob.glob('*.dc.html'):
        s=open(f).read(); n=apply(s); open(f,'w').write(n)
    print('done')
