import re,json,os,sys,shutil
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
OUT=sys.argv[1]; os.makedirs(OUT,exist_ok=True)
c=json.load(open(P+'canvas.json'))
shutil.copy('/tmp/lair-rt.js',os.path.join(OUT,'lair-rt.js'))
keep=[k for k in c['order'] if not re.search(r'_p\d\.dc\.html$',k) and 'Unused' not in c['boards'][k].get('title','')]
def links(h):
    h=re.sub(r'href="([A-Za-z0-9_]+)\.dc\.html',r'href="\1.html',h)
    return re.sub(r'href="([A-Za-z0-9]+)_p\d\.html','href="\\1.html',h)
for f in keep:
    s=open(P+f).read()
    js=s[s.index('class Component extends DCLogic'):s.rindex('</script>')]
    head=s[s.index('<helmet>')+8:s.index('</helmet>')]
    body=links(s[s.index('</helmet>')+9:s.index('</x-dc>')]).replace('</script','<\\/script')
    w=c['boards'][f].get('w',1440); t=c['boards'][f].get('title',f)
    html=(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width={w}"><title>{t} · Local AI Registry prototype</title>'+head+
          '</head><body style="margin:0"><div id="dc-root"></div><script type="text/x-dc-tpl" id="dc-tpl">'+body+'</script><script src="lair-rt.js"></script><script>'+js+
          '\n__dcStart(Component);</script></body></html>')
    open(os.path.join(OUT,f.replace('.dc.html','.html')),'w').write(html)
shutil.copy(os.path.join(OUT,'Flow.html'),os.path.join(OUT,'index.html'))
open(os.path.join(OUT,'.nojekyll'),'w').write('')
print(len(keep),'pages')
