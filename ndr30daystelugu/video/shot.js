const puppeteer=require('puppeteer-core');const {pathToFileURL}=require('url');const path=require('path');
(async()=>{const ts=process.argv.slice(2).map(Number);
const b=await puppeteer.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:'new',args:['--allow-file-access-from-files','--force-device-scale-factor=1']});
const p=await b.newPage();await p.setViewport({width:1080,height:1920,deviceScaleFactor:1});
p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>console.log('LOG',m.text()));
await p.goto(pathToFileURL(path.resolve(__dirname,'index.html')).href);await p.evaluate(()=>window.ready);
for(const t of ts){await p.evaluate(t=>window.renderFrame(t),t);await p.screenshot({path:path.join(__dirname,'out','s_'+t+'.png')});}
await b.close()})();
