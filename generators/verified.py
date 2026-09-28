import html,urllib.parse
PROF='https://localairegistry.com/irvine/lumen-aesthetics'
BADGE=f'''<a href="{PROF}" rel="noopener" title="Verified business information for Lumen Aesthetics on Local AI Registry">
  <img src="https://localairegistry.com/badge/lumen-aesthetics.svg" alt="Lumen Aesthetics is verified on Local AI Registry" width="190" height="44">
  <span>Our verified hours, services and prices are kept up to date on Local AI Registry</span>
</a>'''
SCHEMA='''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "@id": "https://lumenaesthetics.com/#business",
  "name": "Lumen Aesthetics",
  "url": "https://lumenaesthetics.com",
  "telephone": "+1-949-555-0148",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "9891 Irvine Center Dr, Suite 210",
    "addressLocality": "Irvine",
    "addressRegion": "CA",
    "postalCode": "92618",
    "addressCountry": "US"
  },
  "sameAs": [
    "'''+PROF+'''",
    "[GOOGLE MAPS LINK]",
    "[INSTAGRAM LINK]"
  ],
  "subjectOf": {
    "@type": "WebPage",
    "name": "Verified business record for Lumen Aesthetics",
    "url": "'''+PROF+'''",
    "publisher": {
      "@type": "Organization",
      "name": "Local AI Registry",
      "url": "https://localairegistry.com"
    }
  }
}
</script>'''
MAILBODY=f'''Hi,

Could you add two small snippets to our website? They help AI tools like ChatGPT show our correct business info by pointing them to our verified Local AI Registry profile.

1. Badge (visible). Please paste this in the site footer, near our address and phone number:

{BADGE}

2. Schema code (invisible). Please add this to the homepage, inside the <head> or anywhere in the page body:

{SCHEMA}

Neither one changes how the site looks, other than the small badge in the footer. Thank you!

Dr. Priya Nair
Lumen Aesthetics'''
MAILTO='mailto:?subject='+urllib.parse.quote('Two snippets to add to our website')+'&body='+urllib.parse.quote(MAILBODY)
E=lambda x: html.escape(x).replace('{','&#123;').replace('}','&#125;')
BADGEVIS='<span style="display: inline-flex; align-items: center; gap: 10px; height: 44px; padding: 0 14px 0 10px; border: 1px solid #dcd5c7; border-radius: 22px; background: #ffffff;"><svg width="22" height="22" viewBox="0 0 30 30" aria-hidden="true"><path d="M15 3 27.5 27h-8.2L15 18.6 10.7 27H2.5L15 3Z" fill="#2b59d9"></path><path d="M15 18.6 19.3 27h-8.6L15 18.6Z" fill="#e5482d"></path></svg><span style="display: flex; flex-direction: column; line-height: 14px;"><span style="font-size: 10px; color: #667085; font-weight: 600;">✓ Verified on</span><strong style="font-size: 13px; color: #13203a;">Local AI Registry</strong></span></span>'
PLAT=[('WordPress',['Badge: go to Appearance, then Widgets or the Site Editor, and add a Custom HTML block to the footer. Paste the badge code.','Schema: install a header and footer plugin (like WPCode), open Header, and paste the schema code.']),
 ('Wix',['Badge: in the Editor, add Embed Code, then Embed HTML, to your footer. Paste the badge code.','Schema: go to Settings, then Custom Code, add code to the Head of the homepage, and paste the schema code.']),
 ('Squarespace',['Badge: edit the footer, add a Code block, and paste the badge code.','Schema: go to Settings, then Advanced, then Code Injection. Paste the schema code in Header.']),
 ('Shopify',['Badge: go to Online Store, then Themes, then Customize. Add a Custom Liquid section to the footer and paste the badge code.','Schema: in Themes, choose Edit code, open theme.liquid, and paste the schema code just before </head>.'])]
VER=r'''
<div id="verified" style="display: flex; flex-direction: column; gap: 18px; padding: 22px 24px; border-top: 1px solid #e4ded2; background: #fbf8f3;"><div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;"><div style="display: flex; flex-direction: column; gap: 6px; max-width: 760px;"><strong style="font-size: 17px;">Make sure AI shows your correct info</strong><span style="font-size: 14px; line-height: 22px; color: #3d4658;">AI tools like ChatGPT and Gemini sometimes show outdated business info. Adding these two snippets to your website points them to your verified Local AI Registry profile. It takes about 5 minutes.</span></div><span class="mu" style="font-size: 12px; cursor: pointer; white-space: nowrap;" onClick="{{tSite}}">Prototype: {{siteLbl}}</span></div>
<sc-if value="{{hasSite}}" hint-placeholder-val="{{ true }}">
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 10px 22px; padding: 12px 16px; border-radius: 12px; background: #f7f4ee; font-size: 14px;"><span style="color: {{bC}}; font-weight: 700;">{{bIc}} Badge {{bSt}}</span><span style="color: {{sC}}; font-weight: 700;">{{sIc}} Schema {{sSt}}</span><span class="mu" style="font-size: 13px;">We checked lumenaesthetics.com {{chkWhen}}.</span><span class="btn b-sm" onClick="{{recheck}}" style="margin-left: auto;">Check again</span></div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
<div style="display: flex; flex-direction: column; gap: 10px; padding: 18px; border: 1px solid #e4ded2; border-radius: 14px; background: #ffffff; min-width: 0;"><span style="display: flex; justify-content: space-between; align-items: baseline;"><strong style="font-size: 16px;">1. Badge</strong><span class="mu" style="font-size: 12px;">Visible on your site</span></span><span class="mu" style="font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;">Preview</span><div style="padding: 16px; border-radius: 10px; background: #13203a0a; border: 1px dashed #dcd5c7;">'''+BADGEVIS+'''</div><pre style="margin: 0; padding: 12px; border-radius: 10px; background: #13203a; color: #e6ebf5; font-size: 11px; line-height: 16px; white-space: pre-wrap; word-break: break-all;">'''+E(BADGE)+'''</pre><span style="display: flex; align-items: center; gap: 10px;"><span class="btn b-sm b-dark" onClick="{{copy1}}">{{c1}}</span><span class="mu" style="font-size: 13px;">Paste this in your website footer, near your address and phone number.</span></span><span class="mu" style="font-size: 12px;">The badge image is hosted on localairegistry.com, so it stays up to date without you changing anything.</span></div>
<div style="display: flex; flex-direction: column; gap: 10px; padding: 18px; border: 1px solid #e4ded2; border-radius: 14px; background: #ffffff; min-width: 0;"><span style="display: flex; justify-content: space-between; align-items: baseline;"><strong style="font-size: 16px;">2. Schema code</strong><span class="mu" style="font-size: 12px;">Invisible on your site</span></span><pre style="margin: 0; padding: 12px; border-radius: 10px; background: #13203a; color: #e6ebf5; font-size: 11px; line-height: 16px; white-space: pre-wrap; word-break: break-all; max-height: 246px; overflow: auto;">'''+E(SCHEMA)+'''</pre><span style="display: flex; align-items: center; gap: 10px;"><span class="btn b-sm b-dark" onClick="{{copy2}}">{{c2}}</span><span class="mu" style="font-size: 13px;">This code is invisible on your site. Send it to whoever manages your website and ask them to add it to the homepage.</span></span></div></div>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 12px;"><a href="'''+html.escape(MAILTO)+'''" class="btn b-coral">Send to my web person</a><span class="mu" style="font-size: 13px;">Opens an email with both snippets and simple steps, ready to send.</span><label style="margin-left: auto; display: flex; align-items: center; gap: 8px; font-size: 13px; cursor: pointer;" onClick="{{markDone}}"><span style="width: 16px; height: 16px; border-radius: 4px; border: 1.5px solid #3d4658; background: {{mdBg}};"></span>I added both myself</label></div>
<div style="display: flex; flex-direction: column; border-top: 1px solid #ece6da;"><strong style="font-size: 14px; padding: 14px 0 6px;">Where to paste it</strong><sc-for list="{{plats}}" as="p" hint-placeholder-count="4"><div style="border-bottom: 1px solid #ece6da;"><span onClick="{{p.pick}}" style="display: flex; justify-content: space-between; padding: 12px 0; font-size: 14px; font-weight: 600; cursor: pointer;">{{p.n}}<span class="mu">{{p.car}}</span></span><sc-if value="{{p.open}}" hint-placeholder-val="{{ false }}"><ol style="margin: 0 0 12px; padding-left: 20px; font-size: 13px; line-height: 20px; color: #3d4658;"><sc-for list="{{p.steps}}" as="x" hint-placeholder-count="2"><li>{{x}}</li></sc-for></ol></sc-if></div></sc-for></div>
<span class="mu" style="font-size: 12px; line-height: 18px;">This helps AI tools show the correct info. It does not guarantee what they say, and updates can take days to weeks.</span>
</sc-if>
<sc-if value="{{noSite}}" hint-placeholder-val="{{ false }}"><div style="display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 18px 20px; border-radius: 14px; background: #f7f4ee;"><span style="display: flex; flex-direction: column; gap: 4px;"><strong style="font-size: 16px;">No website? Let's talk.</strong><span style="font-size: 14px; color: #3d4658;">We can help you get set up.</span></span><a href="[CALENDLY LINK]" class="btn b-dark">Book a time</a></div></sc-if></div>'''
VJS=r'''    const PL = '''+repr([[n,st] for n,st in PLAT])+r''';
    const vs = { hasSite: !S.noSite, noSite: !!S.noSite, siteLbl: S.noSite ? 'no website' : 'has a website', tSite: () => this.setState({ noSite: !S.noSite }),
      c1: S.cp1 ? 'Copied' : 'Copy code', c2: S.cp2 ? 'Copied' : 'Copy code', copy1: () => this.setState({ cp1: true }), copy2: () => this.setState({ cp2: true }),
      bIc: S.chk || S.md ? '✓' : '○', bSt: S.chk ? 'found on your site' : (S.md ? 'marked as added' : 'not found yet'), bC: S.chk || S.md ? '#237233' : '#667085',
      sIc: S.chk ? '✓' : (S.md ? '✓' : '○'), sSt: S.chk ? 'found on your homepage' : (S.md ? 'marked as added' : 'not found yet'), sC: S.chk || S.md ? '#237233' : '#667085',
      chkWhen: S.chk ? 'just now' : 'today at 9:12 AM', recheck: () => this.setState({ chk: true }), markDone: () => this.setState({ md: !S.md }), mdBg: S.md ? '#13203a' : 'transparent',
      plats: PL.map((p, i) => ({ n: p[0], steps: p[1], open: S.plat === i, car: S.plat === i ? '▲' : '▼', pick: () => this.setState({ plat: S.plat === i ? undefined : i }) })) };
'''
