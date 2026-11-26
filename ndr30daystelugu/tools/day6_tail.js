/* ---------- SCENE 9 : recap (75.0 - 82.6) ---------- */
function scene9(v,u){
  kin([['CLOUD STORAGE',C.bl]],540,340,76,v,.3);kin([['STORE DATA IN THE CLOUD',C.tx]],540,425,38,v,.9,{ls:0});
  const ca=ebo(P(v,.5,1.3));ctx.save();ctx.translate(540,760);ctx.scale(clamp(ca),clamp(ca));ctx.translate(-540,-760);infraCloud(540,760,600,u,1,3);ctx.restore();
  [['AWS S3',200,0],['AZURE BLOB STORAGE',540,1],['GOOGLE CLOUD STORAGE',880,2]].forEach(([s,x,k])=>{const t0=[2.1,3.6,4.8][k],a=ebo(P(v,t0,t0+.7));if(a<=0)return;ctx.save();ctx.globalAlpha*=clamp(a);
    const pts=[[x,1020],[x,960],[540,960],[540,880]];line(pts,rgba(C.bl,.4),4);flow(pts,u+k*.3,3,.5,C.rd,7);
    card(x-155,1030,310,300,26);if(k===0)bucketIcon(x,1150,.5,.6,u,'S3');else if(k===1)azureIcon(x,1150,.55,.7,u);else hexIcon(x,1150,.5,.7,u);
    txt(s,x,1280,s.length>12?19:30,C.bl,{f:HF,ls:0});ctx.restore()});
  sec(v,6.0,20,()=>pill(540,1450,'POPULAR CLOUD STORAGE SERVICES',26,C.rd,C.tx,null,{ls:3,glow:rgba(C.rd,.4)}),{f:.3,out:false});
}
/* ---------- SCENE 9b : series card + coming next (82.6 - 91.6) ---------- */
function scene9b(v,u){
  sec(u,0,3.8,uu=>{txt('30 DAYS OF SNOWFLAKE',540,800,60,C.bl,{f:HF,ls:4,a:eo(P(uu,.1,.7))});
    const p=ebo(P(uu,.3,1));ctx.save();ctx.translate(540,940);ctx.scale(p,p);ctx.globalAlpha*=clamp(p);rr(-200,-72,400,144,72);ctx.fillStyle=C.rd;ctx.shadowColor=rgba(C.rd,.5);ctx.shadowBlur=30;ctx.fill();ctx.shadowBlur=0;ctx.shadowOffsetY=0;txt('DAY 06',0,6,100,C.tx,{ls:4});ctx.restore();
    kin([['CLOUD',C.tx]],540,1130,86,uu,.9);kin([['STORAGE',C.bl]],540,1230,86,uu,1.3)},{f:.35});
  sec(u,3.5,20,uu=>{pill(540,330,'COMING NEXT',36,C.rd,C.tx,null,{ls:8,glow:rgba(C.rd,.5)});kin([['SNOWFLAKE',C.tx]],540,480,86,uu,.9);kin([['EDITIONS',C.bl]],540,580,86,uu,1.3);
    [['STANDARD',0,2.4],['ENTERPRISE',1,3.1],['BUSINESS CRITICAL',2,3.8]].forEach(([s,i,t0])=>{const a=ebo(P(uu,t0,t0+.6));if(a<=0)return;ctx.save();ctx.globalAlpha*=clamp(a);ctx.translate((1-a)*-40,0);
      const y=860+i*170;slab3(250+i*60,y+30,200+i*50,100+i*16,40+i*26,.3,C.bl,{paint:paintStorage(u,i===2),top:.25});
      rr(470,y-40,500,100,24);ctx.fillStyle=i===2?C.rd:'#fff';ctx.fill();ctx.strokeStyle=C.bl;ctx.lineWidth=4;ctx.stroke();txt(s,720,y+10,i==2?30:36,i==2?C.tx:C.bl,{f:HF,ls:2});ctx.restore()})},{f:.35,out:false});
}

/* ---------- SCENE 10 : outro + contacts (91.6 - end) ---------- */
/*ICO*/
function scene10(v,u){
  ctx.save();ctx.globalAlpha=.5;for(let k=0;k<3;k++){const y=(u*90+k*640)%2100-200;ctx.fillStyle=rgba(k%2?C.rd:C.bl,.06);ctx.fillRect(0,y,W,120)}ctx.restore();
  sec(u,0,5.6,uu=>{const p=ebo(P(uu,.1,.8));ctx.save();ctx.translate(540,650);ctx.scale(.7+.3*p,.7+.3*p);ctx.globalAlpha*=clamp(p);
    for(let r=0;r<2;r++){const rp=P(uu,.2+r*.3,1.8+r*.3);ctx.strokeStyle=rgba(C.rd,(1-rp)*.9);ctx.lineWidth=5;ctx.beginPath();ctx.arc(0,0,230+rp*380,0,7);ctx.stroke()}
    ctx.translate(-540,-650);logoCard(540,650,400,P(uu,.4,1.2));ctx.restore();
    txt('30 DAYS OF SNOWFLAKE',540,930,46,C.bl,{f:HF,ls:3,a:eo(P(uu,.5,1))});
    pill(540,1015,'DAY 06 – CLOUD STORAGE',28,C.rd,C.tx,null,{ls:3,glow:rgba(C.rd,.4)});
    kin([['FOLLOW ',C.tx],['NDR EDTECH',C.bl]],540,1160,60,uu,3.0);kin([['ON INSTAGRAM',C.bl]],540,1245,46,uu,3.6,{ls:2});
    const hp=ebo(P(uu,4.0,4.6));ctx.save();ctx.translate(540,1360);ctx.scale(hp,hp);ctx.globalAlpha*=clamp(hp);rr(-300,-52,600,104,52);ctx.fillStyle=C.rd;ctx.fill();txt('@NDREDTECH',0,4,54,C.tx,{ls:2});ctx.restore()},{f:.3});
  sec(u,5.2,20,uu=>{
    logoCard(540,420,250,null);
    txt('OFFICIAL CONTACT INFORMATION',540,610,28,C.bl,{f:HF,ls:3,a:eo(P(uu,.2,.8))});
    const row=(y,h,t0,kind,title,lines,fs)=>{const a=ebo(P(uu,t0,t0+.6));if(a<=0)return;ctx.save();ctx.globalAlpha*=clamp(a);ctx.translate(0,(1-a)*50);card(60,y,960,h,28,{hi:uu>t0+.3&&uu<t0+1.8});
      icoCircle(150,y+h/2,kind);txt(title,230,y+34,22,C.bl,{al:'left',f:HF,ls:4});lines.forEach((l,i)=>txt(l,230,y+(h>200?105:92)+i*(fs+22),fs,C.tx,{al:'left',f:HF,ls:1}));ctx.restore()};
    row(680,270,.3,'phone','PHONE',['+91 87223 55666','+91 81509 78999'],60);
    row(990,250,1.3,'mail','EMAIL',['ndredtech@gmail.com','info@ndredtech.com'],50);
    row(1270,190,2.3,'web','WEBSITE',['www.ndredtech.com'],58);
    sec(uu,1.6,20,()=>pill(540,1530,'FULL COURSE DETAILS',24,C.rd,C.tx,null,{ls:4}),{f:.3,out:false})},{f:.4});
  sec(u,9.0,20,uu=>{ctx.fillStyle=rgba('#FFFFFF',.95*P(uu,0,.4));ctx.fillRect(0,0,W,H);const p=ebo(P(uu,.2,.9));ctx.save();ctx.translate(540,780);ctx.scale(.7+.3*p,.7+.3*p);ctx.globalAlpha*=clamp(p);
    for(let r=0;r<3;r++){const rp=((uu*.7+r/3)%1);ctx.strokeStyle=rgba(C.rd,(1-rp)*.8);ctx.lineWidth=5;ctx.beginPath();ctx.arc(0,0,240+rp*300,0,7);ctx.stroke()}
    ctx.translate(-540,-780);logoCard(540,780,480,P(uu,.5,1.3));ctx.restore();
    kin([['LET\'S LEARN AND',C.tx]],540,1130,60,uu,.5);kin([['GROW TOGETHER!',C.bl]],540,1230,80,uu,.9);txt('NDR EdTech  ·  DAY 06',540,1340,28,tg(.6),{f:SF,ls:5,a:P(uu,1.6,2.2)})},{f:.2,out:false});
}

