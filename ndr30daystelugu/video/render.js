// usage: node render.js <startFrame> <endFrameExclusive> <outfile.mp4>
const puppeteer=require('puppeteer-core');const {pathToFileURL}=require('url');const path=require('path');const {spawn}=require('child_process');
(async()=>{const [s,e,out]=[+process.argv[2],+process.argv[3],process.argv[4]];const FPS=30;
const b=await puppeteer.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:'new',args:['--allow-file-access-from-files','--force-device-scale-factor=1']});
const p=await b.newPage();await p.setViewport({width:1080,height:1920,deviceScaleFactor:1});
p.on('pageerror',x=>console.log('ERR',x.message));
await p.goto(pathToFileURL(path.resolve(__dirname,'index.html')).href);await p.evaluate(()=>window.ready);
const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',String(FPS),'-i','-','-c:v','libx264','-preset','fast','-crf','14','-pix_fmt','yuv420p','-r',String(FPS),out],{stdio:['pipe','inherit','inherit']});
for(let f=s;f<e;f++){await p.evaluate(t=>window.renderFrame(t),f/FPS);
  const buf=await p.screenshot({type:'png'});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();})();
