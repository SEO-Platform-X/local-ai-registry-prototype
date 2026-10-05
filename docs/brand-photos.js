
(function(){
  var PH={"[Treatment room]": "https://images.unsplash.com/photo-1761819922656-d1b77eef49c0?fm=jpg&q=70&w=1600&auto=format&fit=crop", "[Dr. Nair, consult]": "https://images.unsplash.com/photo-1785861001619-b263ebd4e615?fm=jpg&q=70&w=1600&auto=format&fit=crop", "[Results wall]": "https://images.unsplash.com/photo-1595871151608-bc7abd1caca3?fm=jpg&q=70&w=1600&auto=format&fit=crop", "[Front desk]": "https://images.unsplash.com/photo-1731514693674-a32211b63996?fm=jpg&q=70&w=1600&auto=format&fit=crop", "[Storefront]": "https://images.unsplash.com/photo-1788781537938-e96aea5838d3?fm=jpg&q=70&w=1600&auto=format&fit=crop"};
  var SIZE={9:12,10:13,11:13,12:13,13:14,14:15,15:16,16:17,17:18};
  function radius(v){var n=parseFloat(v);if(!n||v.indexOf('%')>-1||n>=999)return null;if(n<=4)return null;if(n<=9)return '10px';if(n<=20)return '16px';return '28px';}
  function fix(root){
    root.querySelectorAll('*').forEach(function(e){
      if(e.__fx)return; e.__fx=1;
      var s=getComputedStyle(e), fs=Math.round(parseFloat(s.fontSize)); var inRefs=!!e.closest('.refs');
      var hasText=[].some.call(e.childNodes,function(n){return n.nodeType===3&&n.textContent.trim()});
      if(hasText&&SIZE[fs]&&!inRefs){e.style.setProperty('font-size',SIZE[fs]+'px','important');}
      if(hasText&&fs<=17&&!inRefs){e.style.setProperty('line-height','1.5','important');}
      
      if(+s.fontWeight>=800){e.style.fontWeight='700';}
      if(hasText){var m=s.color.match(/\d+/g);if(m){var R=+m[0],G=+m[1],B=+m[2],mx=Math.max(R,G,B),mn=Math.min(R,G,B),L=(R+G+B)/3;
        if(mx-mn<40&&L>40&&L<200){e.style.setProperty('color',L<110?'#0f1a33':(L<160?'#4a5570':'#7d8599'),'important');}
        else if(R>170&&G<90&&B<80&&fs<22){e.style.setProperty('color','#0f1a33','important');}
        else if(G>110&&R<60&&B<80){e.style.setProperty('color','#2f6b3a','important');}}}
      
    });
    root.querySelectorAll('.aiv-x i,.aiv-x span').forEach(function(x){var bg=getComputedStyle(x).backgroundColor;if(bg==='rgb(228, 222, 210)'||bg==='rgb(220, 213, 199)')x.style.setProperty('background-color','rgba(15,26,51,0.26)','important');});root.querySelectorAll('.hmos > div').forEach(function(t){
      var k=Object.keys(PH).find(function(x){return t.textContent.indexOf(x)>-1});
      if(k){t.style.setProperty('background-image','url("'+PH[k]+'")','important');}
    });
  }
  var root=document.getElementById('dc-root');
  var mo=new MutationObserver(function(){mo.disconnect();fix(root);mo.observe(root,{childList:true,subtree:true});});
  function start(){fix(root);mo.observe(root,{childList:true,subtree:true});}
  if(document.readyState==='complete')start();else window.addEventListener('load',start);
  setTimeout(start,50);
})();
