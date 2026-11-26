import os, shutil
os.chdir(r"D:\ndr edtech\ndr30daystelugu\day5")
for f in ('scenes_a.html', 'scenes_b.html'):
    if not os.path.exists(f + '.bak'):
        shutil.copy(f, f + '.bak')
a = open('scenes_a.html.bak', encoding='utf-8').read()
b = open('scenes_b.html.bak', encoding='utf-8').read()

def rep(s, x, y):
    assert s.count(x) >= 1, ("MISSING", x)
    return s.replace(x, y)

# ---------- scene1: bubble text matches "No, boss!"
a = rep(a, "txt('GODOWN?!',0,6,92,C.tx,{f:HF,ls:2})", "txt('NO, BOSS!',0,6,88,C.tx,{f:HF,ls:2})")
# ---------- scene2 (18.7 - 38.8)
a = rep(a, "const act=u>10.0;", "const act=u>10.8;")
a = rep(a, "bus(700,1380,u>10.9,u,P(u,10,11));", "bus(700,1380,u>11.5,u,P(u,10.8,11.8));")
a = rep(a, "const hl=bell(u,17.4,20.4)>0?1:0;", "const hl=u>17.9?1:0;")
a = rep(a, "sec(u,0,17.4,uu=>{kin([['WHAT IS A',C.tx]]", "sec(u,0,14.2,uu=>{kin([['WHAT IS A',C.tx]]")
a = rep(a, "const t0=5.8+i*1.5,px=[360,545,740][i];", "const t0=[7.7,8.2,8.8][i],px=[360,545,740][i];")
a = rep(a, "(u>11?.5:1)", "(u>11.8?.5:1)")
a = rep(a, "sec(u,10.0,20.4,uu=>{if(Math.floor(uu*2)%2==0)", "sec(u,10.8,25,uu=>{if(Math.floor(uu*2)%2==0)")
a = rep(a, "sec(u,11.0,15.6,uu=>pill(540,1115,'DATA ACCESSED FROM STORAGE'", "sec(u,11.6,16.2,uu=>pill(540,1115,'DATA ACCESSED FROM STORAGE'")
a = rep(a, "sec(u,15.3,20.6,uu=>{card(300,895", "sec(u,13.0,25,uu=>{card(300,895")
a = rep(a, "sec(u,17.4,20.6,uu=>{kin([['VIRTUAL WAREHOUSE = COMPUTE RESOURCE',C.tx]],540,325,30,uu,.1,{ls:0});kin([['NOT DATA STORAGE',C.rd]],540,400,74,uu,.7);\n    pill(900,640,'NO DATA STORED',20,C.rd,C.tx,null,{ls:2});pill(900,1380,'DATA LIVES HERE',20,C.bl,C.wh,null,{ls:2})},{f:.4,out:false});",
          "sec(u,14.0,25,uu=>{kin([['VIRTUAL WAREHOUSE = COMPUTE RESOURCE',C.tx]],540,325,30,uu,.1,{ls:0});kin([['NOT DATA STORAGE',C.rd]],540,400,74,uu,.7);\n    pill(900,640,'NO DATA STORED',20,C.rd,C.tx,null,{ls:2})},{f:.4,out:false});\n  sec(u,17.9,25,uu=>pill(900,1380,'DATA LIVES HERE',20,C.bl,C.wh,null,{ls:2}),{f:.3,out:false});")
a = rep(a, "[10.0,'COMPUTE RESOURCES'],[15.3,'RESULTS']],1595);", "[10.8,'COMPUTE RESOURCES'],[13.0,'RESULTS'],[18.0,'STORAGE LAYER']],1595);")
# ---------- scene3 (38.8 - 58.3)
a = rep(a, "ST=[3.55,4.3,5.05,5.8,6.8];", "ST=[4.1,4.9,5.7,6.4,7.2];")
a = rep(a, "const cur=ST.filter(t=>u>=t).length-1,all=u>7.3;", "const cur=ST.filter(t=>u>=t).length-1,all=u>8.4;")
a = rep(a, "for(let i=0;i<5;i++){if(u<ST[i])continue;const a=ebo(P(u,ST[i],ST[i]+.7));", "for(let i=0;i<5;i++){if(u<ST[i]){if(u>1.5){ctx.save();ctx.globalAlpha*=.16*P(u,1.5,2.2);slab3(cx[i],base,SW[i],SD[i],SH[i],th,C.bl,{shadow:false});ctx.restore()}continue}const a=ebo(P(u,ST[i],ST[i]+.7));")
a = rep(a, "[['COMPUTE RESOURCES',1130,3.6],['CREDIT CONSUMPTION',1260,3.9]]", "[['COMPUTE RESOURCES',1130,4.2],['CREDIT CONSUMPTION',1260,14.4]]")
a = rep(a, "function lvlAt(u,mi){const d=mi?.35:0;let n=0;for(let i=0;i<5;i++)n+=P(u-d,ST[i]+.2,ST[i]+1.0);return n/5*(i5(u))}", "function lvlAt(u,mi){if(mi===1)return .06+.94*P(u,14.6,17.8);let n=0;for(let i=0;i<5;i++)n+=P(u,ST[i]+.2,ST[i]+1.0);return n/5}")
a = rep(a, "sec(u,7.2,15,uu=>{txt('More compute → can improve performance'", "sec(u,15.6,30,uu=>{txt('More compute → can improve performance'")
a = rep(a, "sec(u,10.9,15,uu=>{txt('More credits consumed while running'", "sec(u,17.2,30,uu=>{txt('More credits consumed while running'")
a = rep(a, "keyword(u,[[.6,'VIRTUAL WAREHOUSE SIZES'],[7.0,'COMPUTE RESOURCES ↑'],[10.9,'CREDIT CONSUMPTION ↑']],1595);", "keyword(u,[[.5,'VIRTUAL WAREHOUSE SIZES'],[11.4,'COMPUTE RESOURCES ↑'],[14.6,'CREDIT CONSUMPTION ↑']],1595);")
# ---------- scene4 (58.3 - 71.9)
a = rep(a, "const v1=u>7.0&&u<10.9,v2=u>10.9&&u<15.2,both=u>=15.2;", "const v1=u>2.6&&u<6.4,v2=u>6.4&&u<10.7,both=u>=10.7;")
a = rep(a, "const ba=ebo(P(u,.4,1.1));", "const ba=ebo(P(u,.1,.8));")
a = rep(a, "sec(u,2.3,6.5,uu=>txt('Millions of customer & transaction records'", "sec(u,.8,5.0,uu=>txt('Millions of customer & transaction records'")
a = rep(a, "const sa=ebo(P(u,2.4,3.2));", "const sa=ebo(P(u,.3,1.0));")
a = rep(a, "if(u>3.2)for(let i=0;i<3;i++){const q=polyAt", "if(u>1.0)for(let i=0;i<3;i++){const q=polyAt")
a = rep(a, "paint:paintStorage(u,u>3.2)", "paint:paintStorage(u,u>1.0)")
a = rep(a, "const W1=ebo(P(u,4.9,5.7)),W2=ebo(P(u,5.9,6.7));", "const W1=ebo(P(u,2.5,3.2)),W2=ebo(P(u,6.2,6.9));")
a = rep(a, "sec(u,7.0,15.2,uu=>{// ETL mini", "sec(u,2.8,25,uu=>{// ETL mini")
a = rep(a, "Math.floor(u*1.2)%3===i&&u<11;", "Math.floor(u*1.2)%3===i&&u<6.5;")
a = rep(a, "ctx.globalAlpha*=u<10.9?1:.35;pill(xs[i]", "ctx.globalAlpha*=u<6.5?1:.35;pill(xs[i]")
a = rep(a, "if(u<10.9){txt('Daily batch loading'", "if(u<6.5){txt('Daily batch loading'")
a = rep(a, "sec(u,10.9,15.2,uu=>{[.5,.8,.62,.95,.7]", "sec(u,6.4,10.7,uu=>{[.5,.8,.62,.95,.7]")
a = rep(a, "[['SEPARATE COMPUTE RESOURCES',15.3],['SHARED UNDERLYING DATA',16.5],['INDEPENDENT WORKLOADS',17.6]]", "[['SEPARATE COMPUTE RESOURCES',10.7],['SHARED UNDERLYING DATA',11.7],['INDEPENDENT WORKLOADS',12.7]]")
open('scenes_a.html', 'w', encoding='utf-8').write(a)

# ---------- scene5 (71.9 - 85.4)
b = rep(b, "const run=u<5.0?1:u<6.3?1-P(u,5,6.3):u<9.3?0:P(u,9.3,10.5);", "const run=u<6.2?1:u<7.4?1-P(u,6.2,7.4):u<11.1?0:P(u,11.1,12.3);")
b = rep(b, "const T=Math.min(u,5.0)+Math.max(0,u-9.3);const state=u<5.1?0:u<9.4?1:2;", "const T=Math.min(u,6.2)+Math.max(0,u-11.1);const state=u<6.3?0:u<11.2?1:2;")
b = rep(b, "const sa=ebo(P(u,state==0?.3:state==1?5.2:9.4,(state==0?.3:state==1?5.2:9.4)+.4));", "const sa=ebo(P(u,state==0?.3:state==1?6.4:11.3,(state==0?.3:state==1?6.4:11.3)+.4));")
b = rep(b, "P(u,6.2,6.8);txt('z z z'", "P(u,6.6,7.2);txt('z z z'")
b = rep(b, "const ps=bell(u,4.7,5.4),pr=bell(u,8.7,9.5);", "const ps=bell(u,6.0,6.8),pr=bell(u,10.9,11.7);")
b = rep(b, "btn(300,1215,370,'SUSPEND',u>4.8&&u<9.0,ps,'pause');btn(780,1215,370,'RESUME',u>9.0,pr,'play');", "btn(300,1215,370,'SUSPEND',u>6.2&&u<11.0,ps,'pause');btn(780,1215,370,'RESUME',u>11.0,pr,'play');")
b = rep(b, "if(u>3.5&&u<10.2){const e1=eio(P(u,3.5,4.7)),e2=eio(P(u,6.5,8.6));const px=u<4.7?540+(300-540)*e1:(u<6.5?300:300+(780-300)*e2),py=u<4.7?1120+95*e1:1215;", "if(u>4.7&&u<12.4){const e1=eio(P(u,4.8,6.0)),e2=eio(P(u,8.4,10.6));const px=u<6.0?540+(300-540)*e1:(u<8.4?300:300+(780-300)*e2),py=u<6.0?1120+95*e1:1215;")
b = rep(b, "ctx.globalAlpha*=1-P(u,9.7,10.2);cursor(px+26,py+10,1);const cl=Math.max(bell(u,4.75,5.3),bell(u,8.8,9.4));", "ctx.globalAlpha*=1-P(u,11.7,12.2);cursor(px+26,py+10,1);const cl=Math.max(bell(u,6.05,6.6),bell(u,11.0,11.6));")
# ---------- scene6 recap (85.4 - 91.2)
b = rep(b, "sec(u,0,6.0,uu=>{\n    kin([['VIRTUAL WAREHOUSE',C.bl]]", "sec(u,0,6.4,uu=>{\n    kin([['VIRTUAL WAREHOUSE',C.bl]]")
b = rep(b, "kin([['EXECUTES SQL QUERIES',C.tx]],540,1420,44,uu,2.2,{ls:0});kin([['DOES NOT STORE DATA',C.rd]],540,1500,56,uu,3.4,{ls:0})", "kin([['EXECUTES SQL QUERIES',C.tx]],540,1420,44,uu,2.1,{ls:0});kin([['DOES NOT STORE DATA',C.rd]],540,1500,56,uu,4.0,{ls:0})")
# split coming-next into scene6c, add scene6b
b = rep(b, "  sec(u,5.5,9.5,uu=>{pill(540,330,'COMING NEXT'", """}
function scene6b(u){
  txt('30 DAYS OF SNOWFLAKE',540,800,60,C.bl,{f:HF,ls:4,a:eo(P(u,.1,.7))});
  const p=ebo(P(u,.3,1));ctx.save();ctx.translate(540,940);ctx.scale(p,p);ctx.globalAlpha*=clamp(p);rr(-200,-72,400,144,72);ctx.fillStyle=C.rd;ctx.shadowColor=rgba(C.rd,.5);ctx.shadowBlur=30;ctx.fill();ctx.shadowBlur=0;ctx.shadowOffsetY=0;txt('DAY 05',0,6,100,C.tx,{ls:4});ctx.restore();
  kin([['VIRTUAL',C.tx]],540,1130,86,u,.9);kin([['WAREHOUSE',C.bl]],540,1230,86,u,1.3);
}
function scene6c(u){
  sec(u,0,30,uu=>{pill(540,330,'COMING NEXT'""")
b = rep(b, "kin([['SNOWFLAKE',C.tx]],540,470,88,uu,.4);kin([['CLOUD STORAGE',C.bl]],540,575,76,uu,.8);", "kin([['SNOWFLAKE',C.tx]],540,470,88,uu,.8);kin([['CLOUD STORAGE',C.bl]],540,575,76,uu,1.2);")
b = rep(b, "const a=ebo(P(uu,.9+i*.35,1.6+i*.35));if(a<=0)return;", "const t0=[2.5,3.4,4.0][i],a=ebo(P(uu,t0,t0+.7));if(a<=0)return;")
b = rep(b, "{ls:2,a:P(uu,2.2,2.8)})},{f:.4,out:false});", "{ls:2,a:P(uu,4.2,4.8)})},{f:.4,out:false});")
# ---------- scene7 outro (99.2 - end)
b = rep(b, "sec(u,0,6.2,uu=>{const p=ebo(P(uu,.1,.9));ctx.save();ctx.translate(540,700)", "sec(u,0,6.6,uu=>{const p=ebo(P(uu,.1,.9));ctx.save();ctx.translate(540,700)")
b = rep(b, "kin([['FOLLOW ',C.tx],['NDR EDTECH',C.bl]],540,1270,64,uu,2.2);kin([['LET\\'S LEARN AND GROW TOGETHER!',C.rd]],540,1360,40,uu,3.0,{ls:0})},{f:.4});", "kin([['FOLLOW ',C.tx],['NDR EDTECH',C.bl]],540,1270,64,uu,3.6);kin([['ON INSTAGRAM',C.rd]],540,1360,44,uu,4.3,{ls:2})},{f:.4});")
b = rep(b, "sec(u,5.8,20,uu=>{\n    const lp=", "sec(u,6.3,20,uu=>{\n    const lp=")
b = rep(b, "hi:uu>t0+.3&&uu<t0+5.5", "hi:uu>t0+.3&&uu<t0+1.8")
b = rep(b, "row(990,250,5.9,'mail'", "row(990,250,1.3,'mail'")
b = rep(b, "row(1270,190,9.2,'web','WEBSITE',['www.ndredtech.com'],58)},{f:.4,out:false});", """row(1270,190,2.2,'web','WEBSITE',['www.ndredtech.com'],58);
    sec(uu,1.6,30,()=>pill(540,1530,'FULL COURSE DETAILS',24,C.rd,C.tx,null,{ls:4}),{f:.3,out:false})},{f:.4,out:false});
  sec(u,9.6,30,uu=>{ctx.fillStyle=rgba('#FFFFFF',.95*P(uu,0,.4));ctx.fillRect(0,0,W,H);const p=ebo(P(uu,.2,.9));ctx.save();ctx.translate(540,780);ctx.scale(.7+.3*p,.7+.3*p);ctx.globalAlpha*=clamp(p);
    for(let r=0;r<3;r++){const rp=((uu*.7+r/3)%1);ctx.strokeStyle=rgba(C.rd,(1-rp)*.8);ctx.lineWidth=5;ctx.beginPath();ctx.arc(0,0,240+rp*300,0,7);ctx.stroke()}
    ctx.translate(-540,-780);logoCard(540,780,480,P(uu,.5,1.3));ctx.restore();
    kin([['LET\\'S LEARN AND',C.tx]],540,1130,60,uu,.5);kin([['GROW TOGETHER!',C.rd]],540,1230,80,uu,.9);txt('NDR EdTech  ·  DAY 05',540,1340,28,tg(.6),{f:SF,ls:5,a:P(uu,1.6,2.2)})},{f:.2,out:false});""")
b = rep(b, "const SC=[[0,19.16,scene1],[19.16,39.46,scene2],[39.46,53.92,scene3],[53.92,72.45,scene4],[72.45,85.91,scene5],[85.91,94.4,scene6],[94.4,DUR+1,scene7]];", "const SC=[[0,18.7,scene1],[18.7,38.8,scene2],[38.8,58.3,scene3],[58.3,71.9,scene4],[71.9,85.4,scene5],[85.4,91.2,scene6],[91.2,94.3,scene6b],[94.3,99.2,scene6c],[99.2,DUR+1,scene7]];")
b = rep(b, "const a=P(t,19.2,19.9)*(1-P(t,93.6,94.3));", "const a=P(t,18.9,19.6)*(1-P(t,98.6,99.3));")
open('scenes_b.html', 'w', encoding='utf-8').write(b)
print("ok")
