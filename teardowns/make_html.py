"""
CRED Product Teardown — HTML Presentation (v2, quality rebuild)
Best practices applied:
  - Font sizes: titles clamp(40px,5vw,56px), body clamp(14px,1.6vw,17px)
  - 8px grid spacing throughout
  - Content fills 100% slide height via flex
  - Viewport-relative units so everything scales with screen size
  - Max content density: 60/40 content-to-space ratio
"""

import base64, os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

ASSETS = "/tmp/cred_v2"
os.makedirs(ASSETS, exist_ok=True)

# ── Image helpers ───────────────────────────────────────────────

def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

def logo_badge(text, bg, fg, W=160, H=160, r=24):
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    d = ImageDraw.Draw(img)
    fill = tuple(int(bg[i:i+2],16) for i in (0,2,4)) + (255,)
    d.rounded_rectangle([0,0,W-1,H-1], radius=r, fill=fill)
    try:    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", W//3)
    except: font = ImageFont.load_default()
    bb = d.textbbox((0,0), text, font=font)
    tw, th = bb[2]-bb[0], bb[3]-bb[1]
    d.text(((W-tw)//2, (H-th)//2-2), text, font=font,
           fill=tuple(int(fg[i:i+2],16) for i in (0,2,4))+(255,))
    buf = BytesIO(); img.save(buf,"PNG"); buf.seek(0)
    return "data:image/png;base64," + base64.b64encode(buf.read()).decode()

def wordmark(W=360, H=120):
    img = Image.new("RGBA",(W,H),(0,0,0,0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0,0,W-1,H-1],radius=18,fill=(18,18,18,255))
    d.rectangle([0,0,W-1,7],fill=(201,168,76,255))
    try:    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
    except: font = ImageFont.load_default()
    bb = d.textbbox((0,0),"CRED",font=font)
    tw,th = bb[2]-bb[0], bb[3]-bb[1]
    d.text(((W-tw)//2,(H-th)//2+4),"CRED",font=font,fill=(201,168,76,255))
    buf=BytesIO(); img.save(buf,"PNG"); buf.seek(0)
    return "data:image/png;base64,"+base64.b64encode(buf.read()).decode()

def phone(title, rows, accent="C9A84C", W=300, H=560):
    img = Image.new("RGBA",(W,H),(0,0,0,0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([2,2,W-3,H-3],radius=36,fill=(20,20,20,255),
                         outline=(55,55,55,255),width=2)
    ac = tuple(int(accent[i:i+2],16) for i in (0,2,4))+(255,)
    d.ellipse([W//2-12,14,W//2+12,30],fill=(10,10,10,255))
    d.rectangle([20,36,W-20,90],fill=ac)
    try:
        fL = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
        fM = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 15)
        fS = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 12)
    except:
        fL=fM=fS=ImageFont.load_default()
    d.text((32,50),title,font=fL,fill=(20,20,20,255))
    y=100
    for i,(lbl,val) in enumerate(rows):
        bg=(28,28,28,255) if i%2==0 else (33,33,33,255)
        d.rectangle([20,y,W-20,y+46],fill=bg)
        d.text((32,y+7),lbl,font=fS,fill=(140,140,140,255))
        d.text((32,y+24),val,font=fM,fill=(240,240,240,255))
        y+=50
    d.rounded_rectangle([W//2-28,H-20,W//2+28,H-12],radius=3,fill=(60,60,60,255))
    buf=BytesIO(); img.save(buf,"PNG"); buf.seek(0)
    return "data:image/png;base64,"+base64.b64encode(buf.read()).decode()

def bar_chart(W=700,H=260):
    img=Image.new("RGBA",(W,H),(20,20,20,255))
    d=ImageDraw.Draw(img)
    try:
        fH=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",20)
        fM=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",16)
    except: fH=fM=ImageFont.load_default()
    d.text((20,12),"Operating Revenue (₹ Crore)",font=fH,fill=(201,168,76,255))
    data=[("FY 2022","₹394 Cr",0.159,(70,70,70)),
          ("FY 2023","₹1,400 Cr",0.566,(130,110,50)),
          ("FY 2024","₹2,473 Cr",1.0,(201,168,76))]
    bx=130; mw=W-bx-130; bh=48; gap=16; y=50
    for lbl,val,ratio,col in data:
        d.rectangle([bx,y,bx+int(mw*ratio),y+bh],fill=col+(255,))
        d.text((10,y+14),lbl,font=fM,fill=(200,200,200,255))
        d.text((bx+int(mw*ratio)+10,y+14),val,font=fM,fill=(201,168,76,255))
        y+=bh+gap
    buf=BytesIO(); img.save(buf,"PNG"); buf.seek(0)
    return "data:image/png;base64,"+base64.b64encode(buf.read()).decode()

def funnel(W=480,H=340):
    img=Image.new("RGBA",(W,H),(20,20,20,255))
    d=ImageDraw.Draw(img)
    try:
        fL=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",28)
        fM=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",16)
        fS=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",13)
    except: fL=fM=fS=ImageFont.load_default()
    cx,cy=W//2,H//2+10
    # rings
    d.ellipse([cx-195,cy-145,cx+195,cy+145],outline=(45,45,45,255),width=2)
    d.ellipse([cx-130,cy-97,cx+130,cy+97],outline=(70,70,70,255),width=2)
    d.ellipse([cx-68,cy-52,cx+68,cy+52],fill=(38,32,12,255),outline=(201,168,76,255),width=2)
    d.text((cx-24,cy-18),"13M",font=fL,fill=(201,168,76,255))
    d.text((cx-30,cy+12),"CRED",font=fS,fill=(150,150,150,255))
    d.text((10,40),"100M+",font=fM,fill=(100,100,100,255))
    d.text((10,62),"CC Holders",font=fS,fill=(80,80,80,255))
    d.text((W-95,40),"35–40M",font=fM,fill=(140,140,140,255))
    d.text((W-95,62),"Premium",font=fS,fill=(100,100,100,255))
    buf=BytesIO(); img.save(buf,"PNG"); buf.seek(0)
    return "data:image/png;base64,"+base64.b64encode(buf.read()).decode()

print("Generating images...")
WM      = wordmark()
OC      = logo_badge("OC",    "1A1A2E","C9A84C")
SL      = logo_badge("SFB",   "CC3333","FFFFFF")
UN      = logo_badge("uni",   "1E5C3A","FFFFFF")
JU      = logo_badge("JM",    "5B2D8E","FFFFFF")
FI      = logo_badge("fi",    "009970","FFFFFF")
SC      = logo_badge("SC",    "005F8A","FFFFFF")
PH_B    = phone("My Bills",   [("HDFC Regalia","₹18,450 due"),("ICICI Sapphiro","₹6,220 due"),("Axis Magnus","₹32,100 due"),("Coins Earned","2,847 ◆"),("Next Due","Mar 5")])
PH_C    = phone("CRED Cash",  [("Pre-approved","₹4,00,000"),("Rate","1.5% / month"),("Fee","Zero"),("Disbursal","< 2 min"),("CIBIL","Soft pull")],accent="3EC97A")
PH_G    = phone("CRED Garage",[("Honda City","MH02-AX-4521"),("FASTag","₹420 Recharge"),("Insurance","Renew Apr 3"),("Service","42 days ago"),("Fuel saved","₹340")],accent="4A90D9")
CHART   = bar_chart()
FUNNEL  = funnel()
print("Done.")

# ── CSS ─────────────────────────────────────────────────────────

CSS = """
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }

:root {
  --black:  #0E0E0E;
  --dark:   #161616;
  --card:   #1F1F1F;
  --card2:  #1A1A1A;
  --border: #2A2A2A;
  --gold:   #C9A84C;
  --gold2:  #E8C96A;
  --white:  #F0F0F0;
  --gray:   #9A9A9A;
  --lgray:  #555;
  --red:    #E04040;
  --green:  #3DC97A;
  --amber:  #F0A020;
  --blue:   #4A8FD4;

  /* 8-point grid */
  --s1: 8px;  --s2: 16px; --s3: 24px; --s4: 32px;
  --s5: 40px; --s6: 48px; --s7: 56px; --s8: 64px;
}

html, body {
  width: 100vw; height: 100vh;
  overflow: hidden;
  background: var(--black);
  font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif;
  color: var(--white);
  -webkit-font-smoothing: antialiased;
}

/* ── SLIDE SHELL ─────────────────────────────────────── */
#deck { width:100%; height:100%; position:relative; }

.slide {
  display: none;
  position: absolute; inset: 0;
  background: var(--dark);
  flex-direction: column;
  padding: clamp(24px,3.2vh,40px) clamp(40px,4.5vw,64px) clamp(20px,2.6vh,32px);
  overflow: hidden;
}
.slide.active { display: flex; }

/* gold bars top + bottom */
.slide::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 4px;
  background: var(--gold);
}
.slide::after {
  content: '';
  position: absolute; bottom: 0; left: 0; right: 0; height: 4px;
  background: var(--gold);
}
.slide.no-bars::before, .slide.no-bars::after { display: none; }

/* ── SLIDE HEADER ────────────────────────────────────── */
.slide-hd {
  display: flex; align-items: baseline; gap: var(--s2);
  margin-bottom: clamp(12px,1.6vh,20px);
  flex-shrink: 0;
}
.slide-tag {
  font-size: clamp(9px,1vw,11px);
  font-weight: 700; letter-spacing: 2.5px;
  text-transform: uppercase; color: var(--gold);
  white-space: nowrap;
}
.slide-tag::after { content: ' ·'; color: var(--border); margin-left: 6px; }
.slide-sub {
  font-size: clamp(9px,1vw,11px);
  color: var(--lgray); letter-spacing: 1px;
}

/* ── TYPOGRAPHY ──────────────────────────────────────── */
h1 {
  font-size: clamp(32px,4.2vw,52px);
  font-weight: 700; line-height: 1.1;
  color: var(--white);
  margin-bottom: clamp(12px,1.5vh,20px);
  flex-shrink: 0;
  letter-spacing: -0.5px;
}
h2 { font-size: clamp(20px,2.4vw,28px); font-weight:700; color: var(--white); }
h3 { font-size: clamp(13px,1.5vw,17px); font-weight:700; color: var(--gold); line-height:1.3; }

p, li, td, .body {
  font-size: clamp(13px,1.4vw,16px);
  line-height: 1.6;
  color: var(--gray);
}
.lg { font-size: clamp(15px,1.6vw,18px) !important; }
.sm { font-size: clamp(11px,1.1vw,13px) !important; }
.xs { font-size: clamp(9px,0.9vw,11px) !important; }

strong, b { color: var(--white); font-weight: 700; }
.gold  { color: var(--gold)  !important; }
.white { color: var(--white) !important; }
.gray  { color: var(--gray)  !important; }
.red   { color: var(--red)   !important; }
.green { color: var(--green) !important; }
.amber { color: var(--amber) !important; }

/* ── LAYOUT ──────────────────────────────────────────── */
.body-area { flex: 1; display: flex; flex-direction: column; min-height: 0; }
.row  { display: flex; gap: clamp(12px,1.5vw,20px); flex: 1; min-height: 0; }
.col  { display: flex; flex-direction: column; flex: 1; min-height: 0; }
.col2 { flex: 2; }
.col3 { flex: 3; }

.g2 { display: grid; grid-template-columns: 1fr 1fr;         gap: clamp(10px,1.3vw,18px); }
.g3 { display: grid; grid-template-columns: 1fr 1fr 1fr;     gap: clamp(10px,1.3vw,18px); }
.g4 { display: grid; grid-template-columns: repeat(4, 1fr);  gap: clamp(8px,1vw,14px); }
.g6 { display: grid; grid-template-columns: repeat(6, 1fr);  gap: clamp(6px,0.8vw,12px); }
.g23 { display: grid; grid-template-columns: 2fr 3fr;         gap: clamp(10px,1.3vw,18px); }
.g32 { display: grid; grid-template-columns: 3fr 2fr;         gap: clamp(10px,1.3vw,18px); }

/* ── CARD ────────────────────────────────────────────── */
.card {
  background: var(--card);
  border-radius: 8px;
  padding: clamp(14px,1.8vh,22px) clamp(14px,1.6vw,20px);
  position: relative;
  display: flex; flex-direction: column;
  border-top: 3px solid var(--gold);
}
.card.red-top   { border-top-color: var(--red);   }
.card.green-top { border-top-color: var(--green); }
.card.amber-top { border-top-color: var(--amber); }
.card.blue-top  { border-top-color: var(--blue);  }
.card.rec       { background: #1E1A08; border: 1.5px solid var(--gold); border-top: 3px solid var(--gold); }
.card.flat      { border-top: none; border: 1px solid var(--border); }

.card-num   { font-size: clamp(26px,3vw,36px); font-weight:700; color:var(--gold); line-height:1; margin-bottom:var(--s1); }
.card-title { font-size: clamp(13px,1.5vw,17px); font-weight:700; color:var(--white); margin-bottom:var(--s1); line-height:1.3; }
.card-body  { font-size: clamp(12px,1.3vw,15px); color:var(--gray); line-height:1.55; flex:1; }

/* ── QUOTE ───────────────────────────────────────────── */
.quote {
  background: #1E1A08;
  border-left: 4px solid var(--gold);
  padding: clamp(10px,1.3vh,16px) clamp(14px,1.6vw,20px);
  border-radius: 0 6px 6px 0;
  font-size: clamp(13px,1.4vw,16px);
  font-style: italic; color: var(--gold);
  line-height: 1.5;
}
.info {
  background: var(--card2);
  border-left: 4px solid var(--gold);
  padding: clamp(8px,1vh,14px) clamp(12px,1.4vw,18px);
  border-radius: 0 5px 5px 0;
  font-size: clamp(12px,1.3vw,14px);
  color: var(--gold); line-height: 1.5;
  flex-shrink: 0;
}

/* ── BULLET LIST ─────────────────────────────────────── */
ul.bl { list-style: none; padding: 0; margin: 0; }
ul.bl li {
  padding: clamp(5px,0.7vh,8px) 0 clamp(5px,0.7vh,8px) var(--s3);
  position: relative;
  font-size: clamp(13px,1.4vw,16px);
  color: var(--white); line-height: 1.5;
  border-bottom: 1px solid var(--border);
}
ul.bl li:last-child { border-bottom: none; }
ul.bl li::before { content:'▸'; position:absolute; left:0; color:var(--gold); }

/* ── STAT TILES ──────────────────────────────────────── */
.stat {
  background: var(--card);
  border-radius: 8px;
  border-top: 3px solid var(--gold);
  padding: clamp(14px,1.8vh,20px) clamp(12px,1.4vw,18px);
  display: flex; flex-direction: column; justify-content: center;
}
.stat-n { font-size: clamp(22px,2.8vw,36px); font-weight:700; color:var(--gold); line-height:1; margin-bottom:6px; }
.stat-l { font-size: clamp(11px,1.2vw,14px); font-weight:700; color:var(--white); margin-bottom:4px; line-height:1.3; }
.stat-s { font-size: clamp(10px,1vw,12px); color:var(--gray); line-height:1.4; }

/* ── TABLE ───────────────────────────────────────────── */
table { width:100%; border-collapse:collapse; }
th {
  background: var(--gold);
  color: #111; font-weight:700;
  padding: clamp(8px,1vh,12px) clamp(10px,1.2vw,16px);
  font-size: clamp(11px,1.2vw,14px);
  text-align: left;
}
td {
  padding: clamp(7px,0.9vh,11px) clamp(10px,1.2vw,16px);
  font-size: clamp(11px,1.2vw,14px);
  border-bottom: 1px solid var(--border);
  vertical-align: middle;
  color: var(--white);
}
tr:nth-child(even) td { background: #1C1C1C; }
.hl { color: var(--gold) !important; font-weight:700; }

/* ── TIMELINE ────────────────────────────────────────── */
.tl { display:flex; position:relative; flex:1; align-items:stretch; gap:0; }
.tl::before {
  content:''; position:absolute;
  top: clamp(26px,3.5vh,36px); left:4%; right:4%; height:3px;
  background: var(--gold);
}
.tl-step { flex:1; text-align:center; position:relative; display:flex; flex-direction:column; }
.tl-dot {
  width: clamp(14px,1.6vw,18px); height: clamp(14px,1.6vh,18px);
  border-radius:50%; background:var(--gold);
  margin: clamp(18px,2.4vh,30px) auto clamp(8px,1vh,12px);
  position:relative; z-index:1; flex-shrink:0;
}
.tl-yr  { font-size:clamp(11px,1.2vw,14px); font-weight:700; color:var(--gold); }
.tl-lbl { font-size:clamp(9px,1vw,12px); color:var(--gray); margin-bottom:var(--s1); }
.tl-box {
  background:var(--card); border-radius:5px;
  padding: clamp(8px,1vh,12px) clamp(6px,0.8vw,10px);
  font-size:clamp(10px,1.1vw,13px); color:var(--white); flex:1;
  margin: 0 2px; line-height:1.4;
}

/* ── FLOW DIAGRAM ────────────────────────────────────── */
.flow { display:flex; position:relative; flex:1; gap:0; align-items:stretch; }
.flow::before {
  content:''; position:absolute;
  top: clamp(36px,5vh,52px); left:3%; right:3%; height:3px;
  background: linear-gradient(90deg, var(--gold) 60%, var(--red) 60%);
}
.fl-step { flex:1; display:flex; flex-direction:column; align-items:center; position:relative; z-index:1; }
.fl-dot {
  width:clamp(16px,2vw,22px); height:clamp(16px,2vh,22px);
  border-radius:50%; background:var(--gold); flex-shrink:0;
  margin-top:clamp(28px,3.8vh,44px);
}
.fl-dot.crit { background:var(--red); box-shadow:0 0 12px rgba(224,64,64,0.5); }
.fl-top {
  text-align:center; flex-shrink:0;
  padding:0 4px;
}
.fl-name { font-size:clamp(10px,1.1vw,13px); font-weight:700; line-height:1.3; }
.fl-sub  { font-size:clamp(9px,0.9vw,11px); color:var(--gray); margin-top:3px; line-height:1.3; }
.fl-bottom { flex:1; display:flex; flex-direction:column; gap:var(--s1); padding:0 2px; margin-top:var(--s1); }
.fl-good { font-size:clamp(9px,0.9vw,11px); color:var(--green); line-height:1.4; text-align:center; }
.fl-bad  { font-size:clamp(9px,0.9vw,11px); color:var(--amber); line-height:1.4; text-align:center; }
.fl-bad.crit { color:var(--red); }

/* ── SECTION DIVIDER ─────────────────────────────────── */
.divider {
  background: #0A0A0A !important;
  border-left: 8px solid var(--gold) !important;
  justify-content: center;
}
.divider::before, .divider::after { display:none !important; }
.div-sec  { font-size:clamp(9px,1vw,11px); letter-spacing:3px; color:var(--gold); font-weight:700; text-transform:uppercase; margin-bottom:var(--s2); }
.div-h1   { font-size:clamp(52px,7.5vw,96px); font-weight:700; line-height:1; margin-bottom:var(--s1); letter-spacing:-1px; }
.div-sub  { font-size:clamp(14px,1.7vw,20px); color:var(--gold); margin-bottom:var(--s6); }
.div-foot { font-size:clamp(10px,1vw,12px); color:var(--lgray); }

/* ── TITLE SLIDE ─────────────────────────────────────── */
.title-slide { background:#0A0A0A !important; }
.title-slide::before, .title-slide::after { height:6px !important; }

/* ── PHONE ───────────────────────────────────────────── */
.phones { display:flex; gap:clamp(16px,2.5vw,36px); justify-content:center; align-items:flex-start; flex:1; }
.ph-wrap { text-align:center; display:flex; flex-direction:column; align-items:center; }
.ph-wrap img { height:clamp(200px,32vh,320px); width:auto; border-radius:clamp(18px,2vw,28px); }
.ph-label { margin-top:var(--s1); font-size:clamp(13px,1.4vw,16px); font-weight:700; color:var(--gold); }
.ph-desc  { font-size:clamp(10px,1.1vw,13px); color:var(--gray); margin-top:4px; line-height:1.4; }

/* ── COMP LOGO ───────────────────────────────────────── */
.comp-logo { width:clamp(28px,2.8vw,40px); height:clamp(28px,2.8vw,40px); border-radius:8px; }

/* ── NAV ─────────────────────────────────────────────── */
#nav {
  position:fixed; bottom:var(--s3); right:var(--s4);
  display:flex; align-items:center; gap:var(--s2); z-index:100;
}
.nb {
  background:rgba(201,168,76,.12); border:1.5px solid var(--gold);
  color:var(--gold); padding:6px 18px; border-radius:20px; cursor:pointer;
  font-size:13px; font-weight:600; transition:all .15s;
}
.nb:hover { background:var(--gold); color:#111; }
#cnt { font-size:12px; color:var(--gray); min-width:56px; text-align:center; }
#prg {
  position:fixed; bottom:0; left:0; height:3px;
  background:var(--gold); transition:width .25s; z-index:100;
}
"""

JS = """
const slides = document.querySelectorAll('.slide');
let cur = 0;
function go(n) {
  slides[cur].classList.remove('active');
  cur = ((n % slides.length) + slides.length) % slides.length;
  slides[cur].classList.add('active');
  document.getElementById('cnt').textContent = (cur+1) + ' / ' + slides.length;
  document.getElementById('prg').style.width = ((cur+1)/slides.length*100) + '%';
}
document.getElementById('prev').onclick = () => go(cur-1);
document.getElementById('next').onclick = () => go(cur+1);
document.addEventListener('keydown', e => {
  if ([' ','ArrowRight','ArrowDown'].includes(e.key))  { e.preventDefault(); go(cur+1); }
  if (['ArrowLeft','ArrowUp'].includes(e.key))          { e.preventDefault(); go(cur-1); }
});
go(0);
"""

# ── Slide builder helpers ────────────────────────────────────────

def S(body, tag="", sub="", cls=""):
    hd = f'<div class="slide-hd"><span class="slide-tag">{tag}</span><span class="slide-sub">{sub}</span></div>' if tag else ""
    return f'<div class="slide {cls}">{hd}{body}</div>\n'

def DIV(num, title, sub):
    return S(f'''
<div class="div-sec">Section {num}</div>
<div class="div-h1">{title}</div>
<div class="div-sub">{sub}</div>
<div class="div-foot">CRED · Product Teardown · Shraddha Singh · Feb 2026</div>
''', cls="divider no-bars")

def CARD(num, title, body, cls=""):
    return f'<div class="card {cls}"><div class="card-num">{num}</div><div class="card-title">{title}</div><div class="card-body">{body}</div></div>'

def STAT(n, l, s):
    return f'<div class="stat"><div class="stat-n">{n}</div><div class="stat-l">{l}</div><div class="stat-s">{s}</div></div>'

# ════════════════════════════════════════════════════════════════
# SLIDES
# ════════════════════════════════════════════════════════════════

# pre-build asset_rows (avoids f-string nesting issues)
asset_rows = "".join(
    f'<div style="display:flex;align-items:center;background:var(--card);'
    f'border-radius:6px;padding:clamp(10px,1.3vh,16px) clamp(14px,1.5vw,20px);gap:clamp(12px,1.5vw,20px);">'
    f'<div style="font-size:clamp(13px,1.4vw,16px);font-weight:700;color:var(--gold);min-width:190px;">{a}</div>'
    f'<div style="font-size:clamp(12px,1.3vw,15px);color:var(--gray);">{b}</div></div>'
    for a,b in [
        ("Low credit risk","→ Safe to build a lending book from day one"),
        ("High purchasing power","→ Valuable to premium brands & advertisers"),
        ("Multi-card holder","→ Rich cross-category spend data"),
        ("Aspirational mindset","→ Responds to status-driven product design"),
    ]
)

slides = []

# 1 — TITLE
slides.append(S(f'''
<div class="row" style="align-items:center;gap:clamp(32px,5vw,64px);">
  <div style="flex:1.3;display:flex;flex-direction:column;gap:clamp(12px,1.5vh,20px);">
    <div style="font-size:clamp(80px,12vw,140px);font-weight:700;line-height:0.95;
         color:var(--white);letter-spacing:-3px;">CRED</div>
    <div style="font-size:clamp(22px,3vw,38px);color:var(--gold);font-weight:600;">
      Product Teardown</div>
    <div style="font-size:clamp(13px,1.5vw,17px);color:var(--gray);line-height:1.6;max-width:480px;">
      An inside-out analysis of India's most opinionated fintech product</div>
    <div style="width:64px;height:3px;background:var(--gold);margin:4px 0;"></div>
    <div>
      <div style="font-size:clamp(16px,1.8vw,22px);font-weight:700;color:var(--white);">Shraddha Singh</div>
      <div style="font-size:clamp(13px,1.4vw,16px);color:var(--gray);margin-top:5px;">
        Product Manager · Fintech & Enterprise SaaS · Feb 2026</div>
    </div>
  </div>
  <div style="flex:0.7;display:flex;flex-direction:column;align-items:center;gap:clamp(16px,2vh,28px);">
    <img src="{WM}" style="width:clamp(180px,22vw,280px);border-radius:16px;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;width:100%;">
      {STAT("13M","MAU","Flat since 2022")}
      {STAT("₹2,473Cr","FY24 Revenue","66% YoY growth")}
      {STAT("1.1%","NPA","vs 2.7% industry")}
      {STAT("$942M","Raised","11 rounds")}
    </div>
  </div>
</div>
''', cls="title-slide no-bars"))

# 2 — AGENDA
slides.append(S(f'''
<h1>Agenda</h1>
<div class="body-area g3" style="grid-template-rows:1fr 1fr;align-items:stretch;">
  {CARD("01","Context","What is CRED · Target user · Core problem")}
  {CARD("02","The Product","Product evolution · Feature analysis · App UI showcase")}
  {CARD("03","The Business","Business model · Revenue data · Market opportunity")}
  {CARD("04","The Competition","4-player landscape · 6-way fintech threat analysis")}
  {CARD("05","Product Thinking","Opportunities · Pain points · Onboarding · North Star")}
  <div class="card" style="justify-content:center;align-items:center;gap:12px;">
    <img src="{WM}" style="width:clamp(100px,14vw,180px);border-radius:10px;">
    <div style="font-size:clamp(10px,1.1vw,13px);color:var(--gray);text-align:center;line-height:1.6;">
      25 slides · Feb 2026<br>Navigate with ← → keys</div>
  </div>
</div>
''', tag="AGENDA", sub="What this deck covers"))

# 3 — WHAT IS CRED
slides.append(S(f'''
<h1>What is CRED?</h1>
<div class="body-area row">
  <div class="col col2" style="gap:clamp(12px,1.5vh,18px);">
    <div class="quote lg">
      Pay your credit card bills. Get rewarded. Be part of an exclusive club.
    </div>
    <ul class="bl">
      <li>Founded 2018 by Kunal Shah (FreeCharge)</li>
      <li>Invite-only: only users with CIBIL 750+ can join</li>
      <li>Core utility: aggregate all credit cards, pay bills in one tap</li>
      <li>Earn CRED coins for every rupee paid on time</li>
      <li>Now expanding into lending, travel, investments, UPI & vehicles</li>
    </ul>
    <div class="info" style="margin-top:auto;">
      <strong>The master insight:</strong> The credit card bill was never the product. <em>The user was.</em>
    </div>
  </div>
  <div class="col" style="align-items:center;gap:clamp(12px,1.5vh,20px);">
    <img src="{WM}" style="width:clamp(160px,20vw,240px);border-radius:14px;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;width:100%;">
      {STAT("₹2,473 Cr","FY24 Revenue","Up 66% YoY")}
      {STAT("13M","Monthly Active","750+ CIBIL")}
      {STAT("₹19,000 Cr","Lending AUM","Dec 2024")}
      {STAT("FY2024","Contribution+","9 qtrs running")}
    </div>
  </div>
</div>
''', tag="WHAT IS CRED", sub="Overview"))

# 4 — THE USER
slides.append(S(f'''
<h1>The Target User</h1>
<div class="body-area row">
  <div class="col card" style="gap:0;">
    <h3 style="margin-bottom:clamp(10px,1.2vh,16px);">Persona — Aspirational Aryan</h3>
    <ul class="bl" style="flex:1;">
      <li>Age: 26–40, urban professional</li>
      <li>Income: ₹10L+ per annum</li>
      <li>Owns 2–4 credit cards</li>
      <li>Values exclusivity, design, and his time</li>
      <li>Pays bills but gets nothing back from his bank</li>
      <li>Trusts brands that treat him as premium</li>
    </ul>
  </div>
  <div class="col col2" style="gap:clamp(8px,1vh,12px);">
    <h3>Why this user = CRED's product asset</h3>
    {asset_rows}
  </div>
</div>
''', tag="THE USER", sub="Who CRED is built for"))

# 5 — CORE PROBLEM
slides.append(S(f'''
<h1>The Problem CRED Solves</h1>
<div class="body-area g3">
  {CARD("01","Bill payment is boring & unrewarded",
    "Banks give nothing back for on-time payments. Netbanking UX is a 2/10 — unchanged for 15 years.")}
  {CARD("02","Premium buyers are expensive to reach",
    "Brands cannot efficiently target creditworthy, high-income users through generic digital ad channels.")}
  {CARD("03","Good credit behaviour is unrecognised",
    "No social or economic reward for financial discipline in India. The CIBIL score goes up — silently.")}
</div>
<div class="info" style="margin-top:clamp(10px,1.3vh,16px);">
  <strong>Delta 4 Theory (Kunal Shah):</strong>
  Users switch only when new experience is 4× better. Bank netbanking = 2/10. CRED = 6/10. The switch happens.
</div>
''', tag="CORE PROBLEM", sub="The insight behind CRED"))

# DIVIDER
slides.append(DIV("02","The Product","Evolution · Features · App UI"))

# 7 — PRODUCT EVOLUTION
tl_data = [
    ("2018","Launch",     "Credit card bill payment\n+ CRED Coins"),
    ("2019","Rewards",    "CRED Store:\ncoins → brand offers"),
    ("2020","Lending",    "CRED Cash (credit line)\n+ CRED Stash"),
    ("2021","Expansion",  "Travel · RentPay\n· Mint (FD)"),
    ("2022","Payments",   "CRED Pay (UPI)\n+ Flash (BNPL)"),
    ("2023–24","Super-app","Garage · Money\nvehicles & unified finance"),
]
tl_html = "".join(f'''<div class="tl-step">
  <div class="tl-yr">{yr}</div>
  <div class="tl-lbl">{lbl}</div>
  <div class="tl-dot"></div>
  <div class="tl-box">{desc.replace(chr(10),"<br>")}</div>
</div>''' for yr,lbl,desc in tl_data)

slides.append(S(f'''
<h1>How the Product Evolved</h1>
<div class="body-area" style="gap:clamp(12px,1.5vh,20px);">
  <div class="tl">{tl_html}</div>
  <div class="g2">
    <div class="info">
      <strong>Pattern:</strong> Each new feature either deepens engagement with the existing user base,
      or monetises their trust in a new category. CRED is not chasing users — it's extracting
      more value from the same premium cohort.
    </div>
    <div class="info">
      <strong>Today:</strong> CRED has morphed from a bill payment app into a financial OS
      for premium Indians — covering payments, lending, investing, travel, and vehicle management.
    </div>
  </div>
</div>
''', tag="PRODUCT EVOLUTION", sub="From bill payment to financial super-app"))

# 8 — FEATURE ANALYSIS
feat_data = [
    ("Bill Payment",  "✅ Strong",    "Solves real pain. Builds monthly habit.", "Commoditised — GPay/PhonePe offer the same.", "white"),
    ("CRED Coins",    "⚠️ Mixed",     "Pavlovian loop; drives retention.",       "Devaluation erodes trust with power users.",  "amber"),
    ("CRED Store",    "✅ Strong",    "Brands pay premium CPMs; high conversion.","Store noisy; curation quality dropped.",      "white"),
    ("CRED Cash",     "✅ Strong",    "Low-risk lending, high margins.",          "RBI BNPL crackdown forced restructuring.",    "white"),
    ("CRED Garage",   "✅ Underrated","Vehicle data → insurance → recurring rev.","Low awareness; undermarketed.",               "green"),
    ("CRED Travel",   "⚠️ Weak",      "Coin redemption play; retention lever.",  "No edge vs MMT/Ixigo/Goibibo.",               "amber"),
]
ft = "".join(f'<tr><td style="font-weight:700;">{f}</td><td class="{c}">{s}</td><td>{w}</td><td style="color:var(--gray);">{r}</td></tr>'
             for f,s,w,r,c in feat_data)
slides.append(S(f'''
<h1>Feature Analysis</h1>
<div class="body-area">
  <table>
    <tr><th>Feature</th><th>Signal</th><th>What Works</th><th>Risk / Gap</th></tr>
    {ft}
  </table>
</div>
''', tag="FEATURE ANALYSIS", sub="What each feature does and where it struggles"))

# 9 — APP UI
slides.append(S(f'''
<h1>App UI — Key Screens</h1>
<div class="body-area phones">
  <div class="ph-wrap">
    <img src="{PH_B}">
    <div class="ph-label">My Bills</div>
    <div class="ph-desc">Monthly bill aggregation<br>& one-tap payment</div>
  </div>
  <div class="ph-wrap">
    <img src="{PH_C}">
    <div class="ph-label">CRED Cash</div>
    <div class="ph-desc">Pre-approved instant<br>credit line</div>
  </div>
  <div class="ph-wrap">
    <img src="{PH_G}">
    <div class="ph-label">CRED Garage</div>
    <div class="ph-desc">Vehicle management,<br>FASTag & insurance</div>
  </div>
</div>
<div class="info" style="margin-top:clamp(8px,1vh,14px);">
  <strong>PM Note:</strong> Bill screen is high-trust and clean. CRED Cash converts because the pre-approved limit
  shows upfront — no application anxiety. Garage is the most undervalued screen; vehicle data compounds into insurance upsell.
</div>
''', tag="APP UI SHOWCASE", sub="Bills · Lending · Garage"))

# DIVIDER
slides.append(DIV("03","The Business","Model · Revenue · Market"))

# 11 — BUSINESS MODEL
slides.append(S(f'''
<h1>Business Model</h1>
<div class="body-area g3">
  {CARD("01","Advertising & Commerce",
    "Brands pay premium CPMs for CRED Store placement and targeted campaigns. "
    "Higher conversion than generic ads — verified CIBIL-filtered audience.<br><br>"
    "<span class='gold'>→ High margin</span>")}
  {CARD("02","Lending",
    "CRED Cash, Flash, Stash — instant credit lines and BNPL. "
    "Low NPA risk (750+ CIBIL). Interest income + processing fees. "
    "₹19,000 Cr AUM as of Dec 2024.<br><br>"
    "<span class='gold'>→ Very High margin</span>")}
  {CARD("03","Transactional Commissions",
    "Travel bookings, RentPay, Garage services — CRED earns a cut "
    "on every completed transaction.<br><br>"
    "<span class='gold'>→ Medium margin</span>")}
</div>
<div class="info" style="margin-top:clamp(10px,1.3vh,16px);">
  <strong>Master play:</strong> Bill payment is a <em>free acquisition tool</em> →
  build trust + data → monetise through lending and commerce.
  Contribution margin positive for 9 consecutive quarters by FY24.
</div>
''', tag="BUSINESS MODEL", sub="How CRED actually makes money"))

# 12 — BY THE NUMBERS
slides.append(S(f'''
<h1>By the Numbers</h1>
<div class="body-area row">
  <div class="col col2" style="justify-content:center;">
    <img src="{CHART}" style="width:100%;border-radius:8px;max-height:clamp(180px,28vh,260px);object-fit:contain;">
    <div style="font-size:clamp(9px,1vw,11px);color:var(--lgray);margin-top:6px;">
      Sources: Inc42 · Entrackr · TechCrunch (public filings)</div>
  </div>
  <div class="col" style="display:grid;grid-template-columns:1fr 1fr;
       grid-template-rows:repeat(3,1fr);gap:clamp(8px,1vw,14px);">
    {STAT("13M","Monthly Active Users","Flat since Nov 2022 — intentional")}
    {STAT("1.1%","NPA on CRED Cash","vs 2.7% industry avg")}
    {STAT("₹19,000 Cr","Lending AUM","As of Dec 2024")}
    {STAT("9 Qtrs","Contribution Margin +ve","Path to EBITDA break-even")}
    {STAT("−41%","Operating Loss Drop","FY23→FY24: ₹1,024Cr→₹609Cr")}
    {STAT("$942M","Total Raised","11 rounds · $6.4B peak val.")}
  </div>
</div>
''', tag="BY THE NUMBERS", sub="Public financial data FY22–FY24"))

# 13 — HONEST ASSESSMENT
_row_style = 'style="padding:clamp(7px,0.9vh,10px) 0;border-bottom:1px solid var(--border);font-size:clamp(12px,1.3vw,15px);"'
working = ["Trust moat — 750+ CIBIL creates self-selecting quality users",
           "Lending business — low NPAs, high margins, zero extra CAC",
           "Design & brand — India's best-designed consumer fintech app",
           "CRED Garage — vehicle data = insurance goldmine",
           "Core retention — bill reminders = reliable monthly re-engagement"]
working_rows = "".join(f'<div style="padding:clamp(7px,0.9vh,10px) 0;border-bottom:1px solid var(--border);font-size:clamp(12px,1.3vw,15px);color:var(--white);">✓ &nbsp;{w}</div>' for w in working)
risks = ["CRED Coins devaluation — heavy users feel cheated",
         "Feature sprawl — too many tabs, weak discoverability",
         "Travel & Commerce — no edge vs dedicated players",
         "High CAC — brand campaigns expensive to sustain",
         "RBI regulatory risk — lending & BNPL under scrutiny"]
risk_rows = "".join(f'<div style="padding:clamp(7px,0.9vh,10px) 0;border-bottom:1px solid var(--border);font-size:clamp(12px,1.3vw,15px);color:var(--gray);">✗ &nbsp;{r}</div>' for r in risks)

slides.append(S(f'''
<h1>Honest Assessment</h1>
<div class="body-area row">
  <div class="col">
    <div style="background:var(--green);padding:clamp(8px,1vh,12px) clamp(14px,1.5vw,18px);
         border-radius:6px 6px 0 0;font-size:clamp(13px,1.4vw,15px);font-weight:700;">
      ✓ What's Working</div>
    <div style="background:var(--card);border-radius:0 0 6px 6px;flex:1;padding:clamp(10px,1.3vh,16px);">
      {working_rows}
    </div>
  </div>
  <div class="col">
    <div style="background:var(--red);padding:clamp(8px,1vh,12px) clamp(14px,1.5vw,18px);
         border-radius:6px 6px 0 0;font-size:clamp(13px,1.4vw,15px);font-weight:700;">
      ✗ What's Not Working</div>
    <div style="background:var(--card);border-radius:0 0 6px 6px;flex:1;padding:clamp(10px,1.3vh,16px);">
      {risk_rows}
    </div>
  </div>
</div>
''', tag="HONEST ASSESSMENT", sub="What's working and what isn't"))

# 14 — MARKET OPPORTUNITY
mkt_rows = [
    ("100M+",    "Credit card holders in India (growing ~20% YoY)"),
    ("35–40M",   "Premium holders (750+ CIBIL) — CRED's actual TAM"),
    ("13M",      "CRED MAU — ~33% TAM penetration"),
    ("₹8–10T",   "Annual credit card spend in India (FY24)"),
    ("₹190/yr",  "CRED revenue per MAU — severely undermonetised"),
    ("10×",      "Revenue/user headroom vs global fintech benchmarks"),
]
mkt_rows_html = "".join(f'<tr><td class="hl">{n}</td><td style="color:var(--gray);">{l}</td></tr>' for n,l in mkt_rows)

slides.append(S(f'''
<h1>India Market Opportunity</h1>
<div class="body-area row">
  <div class="col" style="justify-content:center;align-items:center;">
    <img src="{FUNNEL}" style="width:100%;max-height:clamp(200px,38vh,340px);object-fit:contain;border-radius:8px;">
  </div>
  <div class="col col2" style="gap:clamp(8px,1vh,12px);">
    <table>
      <tr><th>Number</th><th>What it means</th></tr>
      {mkt_rows_html}
    </table>
    <div class="info" style="margin-top:auto;">
      <strong>Opportunity:</strong> CRED's path is revenue depth per user, not user growth.
      At ₹190/user/yr it's massively undermonetised vs Amex (₹8,000+/user/yr).
      Lending at scale is the unlock.
    </div>
  </div>
</div>
''', tag="MARKET OPPORTUNITY", sub="India's premium credit card market"))

# DIVIDER
slides.append(DIV("04","The Competition","Who's threatening CRED's moat in 2025–26"))

# 16 — CLASSIC 4-PLAYER
rows4 = [
    ("Primary Utility","CC Bills + Rewards","UPI Payments","Payments + Lend.","UPI Payments"),
    ("Target User","Premium 750+ CIBIL","Mass market","Mass market","Mass market"),
    ("Rewards","Strong (coins)","Cashback","Cashback","Minimal"),
    ("Lending","Yes (premium)","Yes","Yes (aggressive)","No"),
    ("Brand","Premium / exclusive","Utility","Declining","Google-backed"),
    ("Design","Best-in-class","Good","Average","Clean"),
]
rows4_html = "".join(f"<tr><td style='font-weight:600;'>{r[0]}</td><td class='hl'>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td></tr>" for r in rows4)
slides.append(S(f'''
<h1>CRED vs Mass Market</h1>
<div class="body-area">
  <table>
    <tr><th>Dimension</th><th>CRED</th><th>PhonePe</th><th>Paytm</th><th>GPay</th></tr>
    {rows4_html}
  </table>
  <div class="info" style="margin-top:clamp(10px,1.3vh,16px);">
    CRED's defensible position: the only platform that earned the trust of
    India's creditworthy, high-income segment at scale.
    Mass-market players compete on volume; CRED competes on value density.
  </div>
</div>
''', tag="COMPETITION", sub="Mass-market players vs CRED"))

# 17 — THREAT LANDSCAPE
threat = [
    (OC,"OneCard",  "Urban prof 21–35",     "Own issuer (SBM/BoB)",    "5× pts on top 2 categories",    "HIGH",    "var(--red)",   "Same demo, owns card relationship"),
    (SL,"Slice SFB","18–30, credit newcomers","Full bank (NESFB merger Oct 2024)","Cashback + savings account","MEDIUM","var(--amber)","Captures users before CRED eligibility"),
    (UN,"Uni Cards","Premium high spenders", "Co-branded partner banks","Pay 1/3 monthly (split)",       "LOW",     "var(--green)", "₹95 Cr revenue — struggling to scale"),
    (JU,"Jupiter",  "Digital-first millennials","Neobank, Federal Bank","Smart pots + UPI RuPay card",   "HIGH",    "var(--red)",   "Full financial OS for the same user"),
    (FI,"Fi Money", "Tech professionals",    "Neobank, Federal Bank",   "Smart deposits + credit line",  "HIGH",    "var(--red)",   "Lifestyle + credit direct competitor"),
    (SC,"Scapia",   "Travel lovers",         "Co-branded Federal Bank", "20% coins travel, zero forex",  "MED-HIGH","var(--amber)","Steals CRED Travel segment users"),
]
trows = "".join(f'''<tr>
  <td><img src="{lg}" class="comp-logo"></td>
  <td style="font-weight:700;">{nm}</td>
  <td style="color:var(--gray);">{usr}</td>
  <td style="color:var(--gray);">{card}</td>
  <td style="color:var(--gray);">{rew}</td>
  <td style="color:{tc};font-weight:700;">{thr}</td>
  <td style="color:var(--gray);" class="xs">{why}</td></tr>'''
  for lg,nm,usr,card,rew,thr,tc,why in threat)

slides.append(S(f'''
<h1>Fintech Threat Landscape 2025–26</h1>
<div class="body-area" style="gap:clamp(10px,1.2vh,16px);">
  <table>
    <tr><th></th><th>Company</th><th>Target User</th><th>Card Model</th>
        <th>Rewards</th><th>Threat</th><th>Why It Matters</th></tr>
    {trows}
  </table>
  <div class="g2" style="margin-top:auto;">
    <div class="info" style="border-color:var(--red);">
      <strong style="color:var(--red);">Watch:</strong>
      Slice is now a full Small Finance Bank (merged Oct 2024).
      OneCard at ₹1,910 Cr (FY25) is closing fast on CRED's ₹2,473 Cr.
    </div>
    <div class="info" style="border-color:var(--red);">
      <strong style="color:var(--red);">Biggest structural threat:</strong>
      Jupiter + Fi want to be where premium users <em>bank</em>.
      If they win the primary account, CRED loses relevance.
    </div>
  </div>
</div>
''', tag="COMPETITIVE THREAT LANDSCAPE 2025–26", sub="The real challengers to CRED's moat"))

# DIVIDER
slides.append(DIV("05","Product Thinking","Opportunities · Pain Points · Onboarding · North Star"))

# 19 — WHAT I'D BUILD NEXT
slides.append(S(f'''
<h1>What I Would Build Next</h1>
<div class="body-area g3">
  {CARD("01","CRED Score Dashboard",
    "<strong>Problem:</strong> Users open CRED once/month and leave. No daily reason to return.<br><br>"
    "<strong>Build:</strong> Proprietary health index — bill behaviour, utilisation, spend patterns, debt-to-income.<br><br>"
    "<span class='gold'>Why: Daily open reason · new data asset · natural CRED Cash upsell.</span>")}
  {CARD("02","CRED for Business",
    "<strong>Problem:</strong> Self-employed & founders can't separate personal vs business card spend.<br><br>"
    "<strong>Build:</strong> 'Business Mode' — tag transactions, generate reports, export to accounting tools.<br><br>"
    "<span class='gold'>Why: Low build cost · high perceived value · opens B2B lane.</span>")}
  {CARD("03","Proactive Spend Intelligence",
    "<strong>Problem:</strong> Users know their balance, not their behaviour.<br><br>"
    "<strong>Build:</strong> Monthly AI 'Spend Story' — anomalies + one recommended action.<br><br>"
    "<span class='gold'>Why: Increases DAU · deepens trust · upsells CRED Cash or Mint.</span>")}
</div>
''', tag="PRODUCT OPPORTUNITIES", sub="What I would build next"))

# 20 — PRODUCT BRIEF
mvp_items = [
    ("M","CRED Health Score (proprietary index)","var(--green)"),
    ("M","Credit utilisation trend (30/60/90 days)","var(--green)"),
    ("S","Spend category breakdown + benchmarks","var(--amber)"),
    ("S","Bill payment streak & on-time history","var(--amber)"),
    ("C","'Improve your score' action cards","var(--gray)"),
    ("W","Competitor card comparison engine","var(--lgray)"),
]
mvp_html = "".join(f'<div style="display:flex;gap:10px;padding:5px 0;border-bottom:1px solid var(--border);font-size:clamp(12px,1.3vw,15px);"><span style="font-weight:700;color:{c};min-width:16px;">{m}</span><span>{txt}</span></div>' for m,txt,c in mvp_items)
slides.append(S(f'''
<h1>Product Brief: CRED Score Dashboard</h1>
<div class="body-area g2">
  <div style="display:flex;flex-direction:column;gap:clamp(8px,1vh,14px);">
    <div class="card">
      <h3 style="margin-bottom:8px;">Problem Statement</h3>
      <p class="lg" style="color:var(--white);">Users open CRED once/month to pay bills then leave.
      CIBIL alone is a lagging indicator. No competitor offers a proactive financial health OS for premium users.</p>
    </div>
    <div class="card" style="flex-shrink:0;">
      <h3 style="margin-bottom:8px;">Target User</h3>
      <p>Existing CRED members who pay bills regularly but haven't activated CRED Cash — the pre-lending conversion cohort.</p>
    </div>
    <div class="card" style="flex:1;">
      <h3 style="margin-bottom:8px;">MVP Features (MoSCoW)</h3>
      {mvp_html}
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:clamp(8px,1vh,14px);">
    <div class="card">
      <h3 style="margin-bottom:8px;">Success Metrics</h3>
      <div style="font-size:clamp(12px,1.3vw,15px);line-height:2;">
        <div class="gold" style="font-weight:700;font-size:clamp(10px,1.1vw,13px);">PRIMARY</div>
        <div>• DAU/MAU ratio — target <strong>+8pp in 90 days</strong></div>
        <div>• CRED Cash activation rate among dashboard users</div>
        <div class="gold" style="font-weight:700;font-size:clamp(10px,1.1vw,13px);margin-top:6px;">GUARDRAIL</div>
        <div>• Session length ≤ 10% increase (no fatigue)</div>
        <div>• CIBIL pull consent rate ≥ 80%</div>
      </div>
    </div>
    <div class="card rec">
      <h3 style="margin-bottom:8px;">RICE Score</h3>
      <div style="font-size:clamp(12px,1.3vw,15px);line-height:1.9;">
        <div>Reach: <strong>13M MAU</strong> (100% eligible)</div>
        <div>Impact: <strong>HIGH</strong> — lending funnel entry</div>
        <div>Confidence: <strong>80%</strong> · Effort: <strong>M</strong> (8–12 weeks)</div>
        <div class="gold" style="font-weight:700;font-size:clamp(14px,1.5vw,17px);margin-top:8px;">→ RICE ~520 · HIGH PRIORITY</div>
      </div>
    </div>
    <div class="card red-top" style="flex:1;">
      <h3 style="margin-bottom:8px;">Top 3 Risks</h3>
      <div style="font-size:clamp(12px,1.3vw,15px);line-height:1.9;">
        <div>1. RBI data rules may restrict real-time CIBIL pulls</div>
        <div>2. Users may distrust proprietary score vs official CIBIL</div>
        <div>3. Score gamification → wrong financial behaviours</div>
      </div>
    </div>
  </div>
</div>
''', tag="PRODUCT OPPORTUNITY BRIEF", sub="CRED Score Dashboard"))

# 21 — USER PAIN POINTS
pains = [
    ("01","CRED Coins Devaluation","HIGH","Coins worth less each cycle. Power users with large balances feel cheated.",'"50,000 coins and nothing worth more than ₹50"',"Transparent tier system with locked-in redemption rates"),
    ("02","No Support / Slow Resolution","HIGH","No phone number. Bot fails on complex issues. Email takes 5–10 days.",'"Multiple emails, no response. Money stuck 3 weeks"',"Live chat for payments; 4-hr SLA on transaction failures"),
    ("03","Payment Failures & Refund Delays","HIGH","Transactions marked successful but not credited. Refunds take 7–21 days.",'"Refund initiated after 45 days of follow-up"',"Real-time bank confirmation + auto-refund SLA of 3 days"),
    ("04","Notification Spam & Clutter","MEDIUM","5+ daily promo notifications. Bill payment (core utility) buried in tabs.",'"5 notifications a day about Store deals I never asked for"',"Opt-in notifications by category; surface bill CTA prominently"),
    ("05","Store MRP Mismatch","MEDIUM","Products delivered with MRP higher than advertised price.",'"MRP on box higher than price I paid — not a real discount"',"Verified MRP display; buyer protection policy"),
]
pain_rows = "".join(f'''<tr style="border-left:4px solid {'var(--red)' if f=='HIGH' else 'var(--gold)'};">
  <td style="font-weight:700;color:{'var(--red)' if f=='HIGH' else 'var(--gold)'};">{n}</td>
  <td style="font-weight:700;color:var(--white);">{t}</td>
  <td style="font-weight:700;color:{'var(--red)' if f=='HIGH' else 'var(--gold)'};">{f}</td>
  <td style="color:var(--gray);">{b}</td>
  <td style="font-style:italic;color:var(--gold);" class="sm">{q}</td>
  <td class="sm">{fix}</td></tr>'''
  for n,t,f,b,q,fix in pains)

slides.append(S(f'''
<h1>Top 5 User Pain Points</h1>
<div class="body-area" style="gap:clamp(8px,1vh,12px);">
  <div style="font-size:clamp(10px,1.1vw,12px);color:var(--lgray);">
    Source: 1★ & 2★ Google Play · Trustpilot · MouthShut (2024–25)</div>
  <table>
    <tr><th>#</th><th>Pain Point</th><th>Freq</th><th>Description</th><th>User Quote</th><th>PM Fix</th></tr>
    {pain_rows}
  </table>
</div>
''', tag="USER PAIN POINTS", sub="Synthesised from low-rating app reviews"))

# 22 — ONBOARDING FLOW
fl_data = [
    ("App Discovery",   "Invite or IPL ad",       False,"✅ Exclusivity\ncreates aspiration","⚠️ Invite gate\nblocks organic growth"),
    ("Download & Open", "Play Store install",      False,"✅ Premium first\nimpression on open","⚠️ No value\npreview upfront"),
    ("OTP Verify",      "Mobile → OTP",            False,"✅ Frictionless;\nunder 30 seconds","⚠️ None — this\nstep is clean"),
    ("CIBIL Check",     "PAN + DOB; auto-fetch",   True, "✅ Instant score\nreveal for free","🔴 HIGH DROP-OFF\nfear of hard inquiry"),
    ("Card Linking",    "Manual or auto-detect",   False,"✅ All major\nnetworks supported","⚠️ Manual entry\ntedious; auto fails"),
    ("First Payment",   "Dashboard + one-tap",     False,"✅ Clean UI;\ninstant coins","⚠️ Coin value\nopaque upfront"),
]
fl_steps = "".join(f'''<div class="fl-step">
  <div class="fl-top" style="height:clamp(40px,5.5vh,64px);">
    <div class="fl-name {'red' if crit else 'gold'}">{n}</div>
    <div class="fl-sub">{d}</div>
  </div>
  <div class="fl-dot {'crit' if crit else ''}"></div>
  <div class="fl-bottom">
    <div class="fl-good">{g.replace(chr(10),'<br>')}</div>
    <div class="fl-bad {'crit' if crit else ''}">{b.replace(chr(10),'<br>')}</div>
  </div>
</div>''' for n,d,crit,g,b in fl_data)

slides.append(S(f'''
<h1>Onboarding Flow Analysis</h1>
<div class="body-area" style="gap:clamp(10px,1.3vh,16px);">
  <div class="flow">{fl_steps}</div>
  <div class="info">
    <strong>PM Fix:</strong>
    Add "soft check — your score won't change" at CIBIL step (biggest drop-off point).
    Partner with CAMS/CVL for one-click card import to remove manual entry friction.
    Show coin value <em>before</em> first payment to set user expectations upfront.
  </div>
</div>
''', tag="ONBOARDING FLOW", sub="From app download to first bill payment"))

# 23 — NORTH STAR METRIC
nsm = [
    ("Candidate 1","Monthly Bill\nPayment GMV",
     "Measures core utility. Easy to track. Grows with India's card adoption.",
     "Doesn't capture monetisation. GMV can grow while business stagnates.",
     False,"✗ Reject"),
    ("Candidate 2","Revenue Per\nActive User (RPAU)",
     "Captures monetisation efficiency. Forces product to deepen value for existing fixed user base. Aligns with lending + commerce strategy.",
     "Could incentivise short-term squeezing. Needs NPA and churn guardrails.",
     True,"✓ Recommended"),
    ("Candidate 3","Lending AUM Per\nEligible User",
     "Directly tracks highest-margin business. The metric CRED's investors care most about.",
     "Too narrow — ignores 80%+ of users not on CRED Cash. Neglects trust-building.",
     False,"✗ Reject"),
]
nsm_cards = "".join(f'''<div class="card {'rec' if r else ''}">
  <div class="xs gray" style="margin-bottom:6px;">{lbl}</div>
  <h3 style="font-size:clamp(16px,1.9vw,22px);color:{'var(--gold)' if r else 'var(--white)'};
     margin-bottom:12px;">{t.replace(chr(10),"<br>")}</h3>
  <div style="height:2px;background:var(--green);border-radius:1px;margin-bottom:8px;"></div>
  <p class="sm" style="color:var(--white);margin-bottom:10px;">{p}</p>
  <div style="height:2px;background:var(--red);border-radius:1px;margin-bottom:8px;"></div>
  <p class="sm">{c}</p>
  <div style="margin-top:auto;padding-top:10px;font-size:clamp(12px,1.3vw,15px);
     font-weight:700;color:{'var(--gold)' if r else 'var(--gray)'};">{v}</div>
</div>''' for lbl,t,p,c,r,v in nsm)

slides.append(S(f'''
<h1>North Star Metric</h1>
<div class="body-area g3">{nsm_cards}</div>
<div class="info" style="margin-top:clamp(8px,1vh,14px);">
  <strong>Supporting metrics laddering up to RPAU:</strong>
  ① Monthly Bill GMV (core health) &nbsp;·&nbsp;
  ② Lending AUM Growth (monetisation depth) &nbsp;·&nbsp;
  ③ CRED Store GMV per Active User (commerce engagement)
</div>
''', tag="NORTH STAR METRIC", sub="What CRED should optimise for"))

# 24 — PM TAKEAWAYS
tks = [
    ("Constraint as strategy",
     "The 750+ CIBIL rule is a product decision, not just marketing. "
     "It sets NPA rates, brand perception, and ad CPMs. Constraints can be moats."),
    ("Nail the core loop first",
     "Bill payment → coins → store is tight and validated. CRED earned the right "
     "to expand only after this worked. Premature expansion dilutes trust."),
    ("Monetisation follows trust",
     "CRED didn't launch lending on day one. It waited until users trusted the brand "
     "enough to borrow from it. Sequence of trust-building before monetisation is deliberate."),
    ("Design is a product feature",
     "In a world of functional parity, CRED's UI and brand voice are genuine retention drivers. "
     "Premium design is not vanity — it's a moat."),
]
tks_html = "".join(f'<div style="background:var(--card);border-radius:8px;padding:clamp(16px,2vh,24px) clamp(16px,1.8vw,22px);border-left:5px solid var(--gold);display:flex;flex-direction:column;gap:clamp(8px,1vh,12px);"><h3 style="font-size:clamp(15px,1.7vw,19px);">{t}</h3><p class="lg">{b}</p></div>' for t,b in tks)
slides.append(S(f'''
<h1>PM Takeaways</h1>
<div class="body-area g2">
  {tks_html}
</div>
''', tag="PM TAKEAWAYS", sub="Lessons for product builders"))

# 25 — END CARD
slides.append(S(f'''
<div style="display:flex;align-items:center;height:100%;gap:clamp(32px,5vw,72px);">
  <div style="width:8px;height:clamp(80px,14vh,140px);background:var(--gold);border-radius:4px;flex-shrink:0;"></div>
  <div style="flex:1;display:flex;flex-direction:column;gap:clamp(10px,1.4vh,18px);">
    <div style="font-size:clamp(40px,5.5vw,68px);font-weight:700;line-height:1;letter-spacing:-1px;">Shraddha Singh</div>
    <div style="font-size:clamp(16px,2vw,24px);color:var(--gold);font-weight:600;">
      Product Manager · Fintech & Enterprise SaaS</div>
    <div style="width:72px;height:3px;background:var(--gold);"></div>
    <div style="font-size:clamp(13px,1.5vw,17px);color:var(--gray);line-height:2.0;">
      shraddhasingh8968@gmail.com<br>
      linkedin.com/in/shraddha-singh-9149a4172
    </div>
  </div>
  <div style="flex:0;display:flex;flex-direction:column;align-items:center;gap:clamp(12px,1.5vh,20px);">
    <img src="{WM}" style="width:clamp(160px,20vw,240px);border-radius:14px;">
    <div style="font-size:clamp(10px,1.1vw,13px);color:var(--lgray);text-align:center;">
      PM Portfolio · Feb 2026</div>
  </div>
</div>
''', cls="title-slide no-bars"))

# ── Assemble & write ─────────────────────────────────────────────

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CRED — Product Teardown · Shraddha Singh</title>
<style>{CSS}</style>
</head>
<body>
<div id="deck">
{"".join(slides)}
</div>
<div id="nav">
  <button class="nb" id="prev">← Prev</button>
  <span id="cnt">1 / {len(slides)}</span>
  <button class="nb" id="next">Next →</button>
</div>
<div id="prg"></div>
<script>{JS}</script>
</body>
</html>"""

OUT = "/Users/utkarshsingh/Downloads/workspace/second-brain/portfolio/teardowns/CRED-Teardown-Shraddha-Singh.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

size_kb = os.path.getsize(OUT) // 1024
print(f"✅  {OUT}")
print(f"   Slides: {len(slides)}  ·  Size: {size_kb} KB")
