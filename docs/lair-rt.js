/* Local AI Registry static prototype runtime: renders the board template with its Component and re-renders on setState. */
(function(){
  var tplEl=document.getElementById('dc-tpl'), root=document.getElementById('dc-root');
  var TPL=tplEl.textContent, H=[];
  function get(ctx,expr){
    expr=expr.trim(); if(expr==='true')return true; if(expr==='false')return false;
    var p=expr.split('.'),cur;
    for(var i=ctx.length-1;i>=0;i--){ if(ctx[i]&&Object.prototype.hasOwnProperty.call(ctx[i],p[0])){cur=ctx[i][p[0]];break;} }
    for(var j=1;j<p.length;j++){ cur=(cur!=null&&typeof cur==='object')?cur[p[j]]:undefined; }
    return cur;
  }
  function findClose(t,i,tag){
    var re=new RegExp('<(/?)'+tag+'\\b[^>]*>','g'); re.lastIndex=i; var d=0,m;
    while((m=re.exec(t))){ d+= m[1]?-1:1; if(d===0) return [m.index, m.index+m[0].length]; }
    return [t.length,t.length];
  }
  function esc(v){ return String(v).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;'); }
  function expand(t,ctx){
    var out='',i=0,re=/<sc-(for|if)\b([^>]*)>/g,m;
    while(true){
      re.lastIndex=i; m=re.exec(t);
      if(!m){ out+=t.slice(i); break; }
      out+=t.slice(i,m.index);
      var tag='sc-'+m[1], c=findClose(t,m.index,tag), inner=t.slice(m.index+m[0].length,c[0]), at=m[2];
      if(m[1]==='for'){
        var lm=/list="\{\{([^}]*)\}\}"/.exec(at), nm=(/as="(\w+)"/.exec(at)||[])[1];
        var lst=lm?get(ctx,lm[1]):[]; lst=lst||[];
        for(var k=0;k<lst.length;k++){ var o={}; o[nm]=lst[k]; out+=expand(inner,ctx.concat([o])); }
      } else {
        var vm=/value="\{\{([^}]*)\}\}"/.exec(at); if(vm&&get(ctx,vm[1])) out+=expand(inner,ctx);
      }
      i=c[1];
    }
    out=out.replace(/\son([A-Z][a-zA-Z]*)="\{\{([^}]*)\}\}"/g,function(_,ev,ex){
      var f=get(ctx,ex); if(typeof f!=='function') return '';
      H.push(f); return ' data-h-'+ev.toLowerCase()+'="'+(H.length-1)+'"';
    });
    return out.replace(/\{\{([^}]*)\}\}/g,function(_,ex){ var v=get(ctx,ex); return (v==null||typeof v==='function')?'':(typeof v==='object'?esc(JSON.stringify(v)):String(v)); });
  }
  window.DCLogic=function(){ this.props={}; this.state={}; };
  window.DCLogic.prototype.setState=function(p){
    var n=typeof p==='function'?p(this.state):p; this.state=Object.assign({},this.state,n); schedule();
  };
  var comp=null, pending=false;
  function schedule(){ if(pending)return; pending=true; requestAnimationFrame(function(){pending=false; render();}); }
  function render(){
    var a=document.activeElement, keep=null;
    if(a&&root.contains(a)&&(a.tagName==='INPUT'||a.tagName==='TEXTAREA')){
      var all=root.querySelectorAll('input,textarea'); keep={i:Array.prototype.indexOf.call(all,a),s:a.selectionStart,e:a.selectionEnd,v:a.value};
    }
    H=[]; var v={}; try{ v=comp.renderVals()||{}; }catch(err){ console.error(err); }
    root.innerHTML=expand(TPL,[v]);
    root.querySelectorAll('*').forEach(function(el){
      for(var x=0;x<el.attributes.length;x++){
        var at=el.attributes[x]; if(at.name.indexOf('data-h-')!==0) continue;
        var ev=at.name.slice(7), f=H[+at.value];
        if(ev==='change'&&(el.tagName==='INPUT'&&!/checkbox|radio/.test(el.type)||el.tagName==='TEXTAREA')) ev='input';
        (function(fn){ el.addEventListener(ev,function(e){ fn(e); }); })(f);
      }
    });
    if(keep&&keep.i>=0){ var nw=root.querySelectorAll('input,textarea')[keep.i]; if(nw){ if(nw.value!==keep.v&&nw.getAttribute('value')===null) nw.value=keep.v; nw.focus(); try{nw.setSelectionRange(keep.s,keep.e);}catch(e){} } }
  }
  document.addEventListener('keydown',function(e){
    var el=e.target; if(e.key!=='Enter'||!el||el.tagName!=='INPUT'||!el.closest('.sbox,.s3-q,.srch'))return;
    var v=el.value.trim(); if(!v)return; e.preventDefault(); location.href=/\s/.test(v)?'QResults.html':'ExploreSearch.html';
  });
  window.__dcStart=function(C){ comp=new C(); render(); };
})();
