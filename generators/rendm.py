import sys,re,json,subprocess
from playwright.sync_api import sync_playwright
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
f,out,h=sys.argv[1],sys.argv[2],int(sys.argv[3]); st=sys.argv[4] if len(sys.argv)>4 else '{}'
s=open(P+f).read()
js=s[s.index('class Component extends DCLogic'):s.rindex('</script>')]
open('/tmp/t2.js','w').write('class DCLogic{constructor(){this.props={};this.state='+st+'} setState(){}}\n'+js+'\nconst r=new Component().renderVals();console.log(JSON.stringify(r,(k,v)=>typeof v==="function"?null:v))')
V=json.loads(subprocess.run(['node','/tmp/t2.js'],capture_output=True,text=True).stdout)
def get(ctx,expr):
    expr=expr.strip()
    if expr in ('true','false'): return expr=='true'
    cur=None
    parts=expr.split('.')
    for c in reversed(ctx):
        if parts[0] in c: cur=c[parts[0]]; break
    for p in parts[1:]:
        cur=cur.get(p) if isinstance(cur,dict) else None
    return cur
def find_close(t,i,tag):
    depth=0
    for m in re.finditer(r'<(/?)'+tag+r'\b[^>]*>',t[i:]):
        depth+= -1 if m.group(1) else 1
        if depth==0: return i+m.start(), i+m.end()
def expand(t,ctx):
    out=''; i=0
    while True:
        m=re.search(r'<sc-(for|if)\b([^>]*)>',t[i:])
        if not m: out+=t[i:]; break
        a=i+m.start(); out+=t[i:a]
        tag='sc-'+m.group(1); cs,ce=find_close(t,a,tag)
        inner=t[a+len(m.group(0)):cs]; attrs=m.group(2)
        if m.group(1)=='for':
            lst=get(ctx,re.search(r'list="\{\{([^}]*)\}\}"',attrs).group(1)) or []
            nm=re.search(r'as="(\w+)"',attrs).group(1)
            for it in lst: out+=expand(inner,ctx+[{nm:it}])
        else:
            v=get(ctx,re.search(r'value="\{\{([^}]*)\}\}"',attrs).group(1))
            if v: out+=expand(inner,ctx)
        i=ce
    return re.sub(r'\{\{([^}]*)\}\}',lambda mm:'' if get(ctx,mm.group(1)) is None else str(get(ctx,mm.group(1))),out)
head=s[s.index('<helmet>')+8:s.index('</helmet>')]
body=s[s.index('</helmet>')+9:s.index('</x-dc>')]
html='<html><head><meta charset="utf-8">'+head+'</head><body style="margin:0">'+expand(body,[V])+'</body></html>'
open('/tmp/r2.html','w').write(html)
clip=sys.argv[5] if len(sys.argv)>5 else None
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':int(__import__("os").environ.get("VW","1440")),'height':h}); pg.goto('file:///tmp/r2.html'); pg.wait_for_timeout(300)
    if clip:
        el=pg.query_selector(clip); el.scroll_into_view_if_needed(); bb=el.bounding_box(); pad=int(sys.argv[6]) if len(sys.argv)>6 else 0; pg.screenshot(path=out,clip={'x':0,'y':max(0,bb['y']-pad),'width':int(__import__("os").environ.get("VW","1440")),'height':min(bb['height']+2*pad,1400)},full_page=True)
    else: pg.screenshot(path=out)
    b.close()
