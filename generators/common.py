import re
P='/mnt/user-data/outputs/artifacts/01ea5720-d0c8-4528-b8cc-76eb1693feae/project/'
claim=open(P+'Claim.dc.html').read()
HEAD=open('/tmp/gen/HEAD_base.txt').read()
LOGO='<svg width="30" height="30" viewBox="0 0 30 30" fill="none" aria-hidden="true"><rect x="2" y="2" width="26" height="26" rx="7" fill="#ff385c"></rect><path d="M8.5 21V9h2.6v9.7h5.6V21H8.5Z" fill="#ffffff"></path><path d="M18.2 21l2.9-8.2h.1l2.9 8.2h-5.9Z" fill="#ffffff" opacity="0.7"></path></svg>'
def header(right):
    return f'''<header style="height: 68px; flex-shrink: 0; padding: 0 40px; display: flex; align-items: center; justify-content: space-between; gap: 24px; border-bottom: 1px solid #ebebeb; background: #ffffff;">
<a href="Home.dc.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">{LOGO}<span style="font-weight: 800; font-size: 16px; letter-spacing: -0.01em; color: #ff385c;">Local AI Registry</span></a>
<div style="display: flex; align-items: center; gap: 8px;">{right}</div>
</header>'''
def page(title, css, body, js, w=1440, h=None):
    t=HEAD.replace('<title>Lumen Aesthetics on Local AI Registry</title>',f'<title>{title}</title>')
    box=f'width: {w}px; min-height: {h}px;' if h else f'width: {w}px;'
    return t+'\n'+css+'\n</style>\n</helmet>\n'+f'<div style="{box} box-sizing: border-box; display: flex; flex-direction: column; background: #ffffff; position: relative;">\n'+body+'\n</div>\n</x-dc>\n<script type="text/x-dc" data-dc-script>\nclass Component extends DCLogic {\n  renderVals() {\n'+js+'\n  }\n}\n</script>\n</body>\n</html>\n'

PUB_R='<a href="Explore.dc.html" class="hnl">Explore</a><a href="Business.dc.html" class="hnl">For business</a><a href="#" class="hnl">Sign in</a><a href="Explore.dc.html" class="btn b-sm b-dark" style="margin-left: 6px;">Join your city</a>'
HNL_CSS='.hnl{font-size:14px;font-weight:600;color:#222222;text-decoration:none;padding:0 12px;white-space:nowrap}\n'

_pg=page
def page(*a,**k):
    import palette
    return palette.apply(_pg(*a,**k))
