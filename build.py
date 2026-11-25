"""Builds the Forgeline website: shared header and footer around each page's content."""
import re
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "dist"
OUT.mkdir(exist_ok=True)

# Set to the live address (for example "https://forgeline.dev/") so share previews use a full link. Leave empty until the domain is chosen.
SITE_URL = ""

LOGO = ('<svg width="28" height="28" viewBox="0 0 32 32" aria-hidden="true"><path d="M4 9h24l-3 6H14v3l-4 3v-6H7z" fill="currentColor"/>'
        '<path d="M11 24h10l2 4H9z" fill="currentColor"/><path d="M19 4c2 2 1 3 3 4" stroke="#ff4d12" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg>')

COMPANY_NAV = [("newton.html", "Newton"), ("freezeframe.html", "Freezeframe"), ("about.html", "About"),
               ("founders.html", "Founders"), ("invest.html", "Invest"), ("donate.html", "Donate")]


THEME_JS = r"""(function(){
var R=document.documentElement,K="fl-theme";
var V={light:{bg:"#ffffff",bg2:"#f3f2f0",ink:"#1b1a19",mute:"#5d6670",line:"#dcdad6",band:"#1d1c1b",cardline:"#34312e",codebg:"#e6e3de"},
dark:{bg:"#141312",bg2:"#1c1b19",ink:"#f2f0ec",mute:"#a3abb3",line:"#34322f",band:"#0a0908",cardline:"#3a3632",codebg:"#2a2826"}};
function get(){var t=null;
try{t=localStorage.getItem(K)}catch(e){}
if(!t){try{t=sessionStorage.getItem(K)}catch(e){}}
if(!t){var m=/(?:^|;)fl-theme=(light|dark)/.exec(window.name||"");t=m&&m[1]}
return t==="light"||t==="dark"?t:null}
function save(t){
try{localStorage.setItem(K,t)}catch(e){}
try{sessionStorage.setItem(K,t)}catch(e){}
try{window.name=(window.name||"").replace(/(?:^|;)fl-theme=\w+/,"")+";fl-theme="+t}catch(e){}}
function sys(){try{return matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"}catch(e){return"light"}}
function eff(){return R.getAttribute("data-theme")||sys()}
function paint(){var dark=eff()==="dark",bs=document.querySelectorAll(".theme-btn");
for(var i=0;i<bs.length;i++){var b=bs[i];
if(dark)b.classList.add("is-dark");else b.classList.remove("is-dark");
var l=dark?"Switch to light mode":"Switch to dark mode";b.setAttribute("aria-label",l);b.title=l}}
function apply(t){R.setAttribute("data-theme",t);R.style.colorScheme=t;
var v=V[t];for(var k in v)R.style.setProperty("--"+k,v[k]);paint()}
var saved=get();if(saved)apply(saved);
document.addEventListener("click",function(e){
var b=e.target&&e.target.closest?e.target.closest(".theme-btn"):null;if(!b)return;
var next=eff()==="dark"?"light":"dark";
try{if(!matchMedia("(prefers-reduced-motion: reduce)").matches){R.classList.add("theme-anim");setTimeout(function(){R.classList.remove("theme-anim")},600)}}catch(x){}
apply(next);save(next)});
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",paint);else paint();
try{matchMedia("(prefers-color-scheme: dark)").addEventListener("change",paint)}catch(e){}
})();"""


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<script>{THEME_JS}</script>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141312" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Forgeline">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE_URL}{'' if SITE_URL else '/'}og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Forgeline. Forge ahead. Coding tools for every level.">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@112,700;112,800;100,500;100,600&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
</head>
<body>
"""


def header(page, product=None, anchors=None, cta=("index.html#products", "Get the tools")):
    if product:
        brand = (f'<a class="brand morph" href="index.html" aria-label="{product} by Forgeline, go to the Forgeline home page">{LOGO}'
                 f'<span class="prod">{product}</span> <span class="by">by Forgeline</span></a>')
    else:
        brand = f'<a class="brand" href="index.html" aria-label="Forgeline home">{LOGO}Forgeline</a>'
    items = anchors or COMPANY_NAV
    links = "".join(
        f'<a href="{h}"{" aria-current=page" if h == page else ""}>{t}</a>' for h, t in items
    )
    return f"""<header><nav aria-label="Main">
  {brand}
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="links">Menu</button>
  <div class="links" id="links">{links}</div>
  <button class="theme-btn" type="button" aria-label="Switch to dark mode"><svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3 17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4a8.2 8.2 0 1 0 10.2 10.2Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></button>
  <a class="btn hot" href="{cta[0]}">{cta[1]}</a>
</nav></header>
"""


FOOTER = """<footer>
  <div class="foot">
    <div><a class="brand" href="index.html">""" + LOGO + """Forgeline</a><p><b style="color:var(--ink)">Forge ahead.</b> Tools for coding at every level, from your first command to your thousandth deploy.</p></div>
    <div><h4>Products</h4><a href="newton.html">Newton</a><a href="freezeframe.html">Freezeframe</a><a href="newton.html#install">Install Newton</a><a href="freezeframe.html#install">Install Freezeframe</a></div>
    <div><h4>Company</h4><a href="about.html">About</a><a href="founders.html">Founders</a><a href="invest.html">Invest</a><a href="donate.html">Donate</a></div>
    <div><h4>Open source</h4><a href="https://github.com/asteya01">GitHub</a><a href="newton.html#faq">Newton FAQ</a><a href="freezeframe.html#faq">Freezeframe FAQ</a></div>
    <div><h4>Legal</h4><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></div>
  </div>
  <p class="legal">© 2026 Forgeline. Newton and Freezeframe are open source under the MIT license.</p>
</footer>
<script src="site.js"></script>
<script src="theo.js"></script>
"""


def page(name, title, desc, body, product=None, anchors=None, cta=None, extra_script=""):
    html = head(title, desc) + header(name, product, anchors, cta or ("index.html#products", "Get the tools")) + body + FOOTER + extra_script + "</body>\n</html>\n"
    (OUT / name).write_text(html)
    print("wrote", name, len(html))


# ---------------------------------------------------------------- Newton (from the page built earlier)
src = (HERE.parent / "forgeline" / "index.html").read_text()
main = src.split('<main id="top">', 1)[1].split("</main>", 1)[0]
script = src.split("<script>", 1)[1].split("</script>", 1)[0]
# copy buttons are handled by site.js now
script = re.sub(r"document\.addEventListener\('click',async e=>\{const b=e\.target\.closest\('\.copy'\).*?\}\);\n", "", script, flags=re.S)
COMMANDS = '<section class="band" id="commands"><div class="wrap">\n  <h2>Every command, in one place</h2>\n  <p class="sub">Most of the time Tab is all you need. These commands cover bigger jobs, fixing mistakes and setup. Click a command to copy it.</p>\n<div class="cmdgroup"><h3>Everyday</h3><ul class="cmdlist">\n<li><span class="cmdchip static">Tab</span><p>Type what you want and press Tab. The command replaces your words. Press Tab again for another option, or Shift+Tab to get your words back.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton ask">newton ask</button><p>Answer a question about whatever you pipe in, like <code>npm test 2&gt;&amp;1 | newton ask what broke</code>.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton explain">newton explain</button><p>Break a pasted command down flag by flag. Handy for checking what a local model wrote.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton fix">newton fix</button><p>Re-run your last failed command, read the real error, and offer a fix.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton commit">newton commit</button><p>Read your staged changes, write a commit message, and wait for your approval.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton chat">newton chat</button><p>Have a back-and-forth conversation in your terminal. Newton knows your machine, so its answers fit your setup.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton history">newton history</button><p>See your recent requests and the commands Newton wrote for them. Add <code>-n 30</code> to see more.</p></li>\n</ul></div>\n<div class="cmdgroup"><h3>Bigger jobs</h3><ul class="cmdlist">\n<li><button class="cmdchip" type="button" data-copy="newton plan">newton plan</button><p>Start plan mode. Give it a goal, like “set up a python project”, and approve one step at a time. Add <code>--dry-run</code> to preview the plan without saving or running it.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton resume">newton resume</button><p>Pick a paused plan back up at the same step. You can close the tab at any time.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton plans undo">newton plans undo</button><p>Roll back finished plan steps, newest first.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton plans export -o setup.sh">newton plans export -o setup.sh</button><p>Export a finished plan as a shell script. <code>-o</code> sets the file name.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton status">newton status</button><p>Show your current plan\'s checklist. Add <code>--md</code> to print it as a Markdown checklist.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton plans list">newton plans list</button><p>See your saved plans. Use <code>newton plans show</code> to read one, or <code>newton plans rm</code> to delete one.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton agent">newton agent</button><p>Open Iris, the chat agent, in your browser. It works in your current folder, runs read-only steps by itself, and asks before changing anything. Add <code>--ask</code> to confirm every command, even read-only ones.</p></li>\n</ul></div>\n<div class="cmdgroup"><h3>Setup</h3><ul class="cmdlist">\n<li><button class="cmdchip" type="button" data-copy="newton setup">newton setup</button><p>Run the guided setup again to choose your AI and turn on Tab.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton doctor">newton doctor</button><p>Check your installation. It finds PATH problems and warns you if another copy of Newton is getting in the way.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton config provider ollama">newton config provider ollama</button><p>Choose the AI provider. <code>ollama</code> is the free one that runs on your computer.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton config model llama3.1">newton config model llama3.1</button><p>Choose the AI model.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton config">newton config</button><p>Show your settings. Add a setting name to see its value, or a name and a value to change it. Your API key is shortened when shown.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton init zsh">newton init zsh</button><p>Print the lines that turn on Tab for a shell: <code>zsh</code>, <code>bash</code> or <code>fish</code>. The installer adds them for you.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton prompt">newton prompt</button><p>Print a one-line badge for your current plan, so you can show it in your shell prompt.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton update">newton update</button><p>Update Newton from the newest <code>newton.zip</code> in your Downloads folder. It shows the version change, asks first, and tests the new copy before replacing yours.</p></li>\n<li><button class="cmdchip" type="button" data-copy="newton uninstall">newton uninstall</button><p>Remove Newton and its lines in your shell config. Add <code>--purge</code> to delete your settings, API key, history and saved plans too.</p></li>\n</ul></div>\n<div class="cmdgroup"><h3>Inside plan mode</h3>\n<p class="sub" style="margin:0 0 16px">Each step waits for you. Use these keys to decide what happens.</p>\n<div class="keys"><span><kbd>Enter</kbd> run the step</span><span><kbd>E</kbd> edit it</span><span><kbd>S</kbd> skip it</span><span><kbd>?</kbd> explain it</span><span><kbd>A</kbd> ask a question</span><span><kbd>R</kbd> revise the plan</span></div></div>\n</div></section>\n\n'
LOOPDEMO = '<div class="loopdemo" data-loop>\n    <div class="term" role="group" aria-label="Looping demo with sample commands">\n      <div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="lp-title">~/projects/site — zsh</span>\n        <button class="lp-pause" type="button" aria-pressed="false" aria-label="Pause the demo"><svg class="i-pause" viewBox="0 0 16 16" aria-hidden="true"><rect x="3.5" y="3" width="3" height="10" rx="1"/><rect x="9.5" y="3" width="3" height="10" rx="1"/></svg><svg class="i-play" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3l8 5-8 5z"/></svg></button></div>\n      <div class="screen" aria-hidden="true">\n        <div class="hist">$ git status<br><span class="ok">On branch main · nothing to commit</span></div>\n        <div class="line"><span class="ps">~/site ❯</span><span class="lp-text"></span><span class="lp-caret"></span></div>\n        <div class="hint lp-hint"></div>\n      </div>\n    </div>\n    <p class="sr">Example: you type "find every file over 100MB here", press Tab, and Newton writes find . -type f -size +100M on your line. Other examples turn "undo my last git commit but keep the changes" into git reset --soft HEAD~1, and "what is using port 3000" into lsof -i :3000. Nothing runs until you press Enter.</p>\n    <p class="note">A looping demo with sample commands. The real tool asks your chosen AI.</p>\n  </div>\n'
LOOPVID = '''<section class="band" id="video"><div class="wrap">
  <h2>See Newton in about a minute</h2>
  <p class="sub">Describe the task, press Tab, check the command, then press Enter. Here is the whole idea in one short video.</p>
  <figure class="vidwrap">
    <video controls preload="metadata" playsinline poster="newton-intro-poster.webp" width="1920" height="1080" aria-describedby="vid-note"><source src="newton-intro.mp4" type="video/mp4">Your browser can't play this video. <a href="newton-intro.mp4">Download it instead</a>.</video>
    <figcaption id="vid-note">About 1 minute, with sound.</figcaption>
  </figure>
</div></section>

'''
main = main.replace('<section class="band alt" id="how">', LOOPVID + '<section class="band alt" id="how">', 1)
how = main.index('id="how"')
j = main.index('</ol>', how) + len('</ol>')
main = main[:j] + '\n  ' + LOOPDEMO + main[j:]
main = main.replace('<section class="band safe" id="safety">', COMMANDS + '<section class="band safe" id="safety">', 1)
main = main.replace("Your request and basic context, like your OS and shell. Secrets such as API keys are removed first. With Ollama, nothing leaves your computer. There's no telemetry.", "For Tab, your request plus a short description of your setup: OS, shell, current folder, project type, installed tool names and top-level file names (you can turn this off). File contents, environment variables and shell history are never sent. Plan mode, ask, fix and commit send more, such as a failed step's output or your staged diff, only when you use them, and secrets are redacted first. With Ollama, nothing leaves your computer. There's no telemetry.")
main = re.sub(
    r'<div class="snap">.*?</div>\s*</div>\s*</section>',
    """<div class="snap">
    <div><h2 style="font-size:clamp(26px,3vw,36px)">Also from Forgeline: Freezeframe</h2>
    <p class="sub">A Chrome extension for learning from coding videos. Freeze a tutorial, drag a box around the code, and get real text with the indentation intact. Then copy it, edit it, or have AI fix, explain or improve it.</p></div>
    <a class="btn ghost" href="freezeframe.html">See Freezeframe</a>
  </div>
</div></section>""",
    main,
    flags=re.S,
)
NEWTON_ANCHORS = [("#how", "How it works"), ("#plan", "Plan mode"), ("#features", "Features"), ("#commands", "Commands"), ("#safety", "Safety"), ("#pricing", "Pricing"), ("#faq", "FAQ")]
page("newton.html", "Newton by Forgeline", "Newton: describe a task in plain English, press Tab, get the shell command. Nothing runs until you press Enter.",
     '<main id="top">' + main + "</main>\n", product="Newton", anchors=NEWTON_ANCHORS, cta=("#install", "Install Newton"),
     extra_script="<script>" + script + "</script>\n")

for name in ["index", "freezeframe", "about", "founders", "invest", "donate", "privacy", "terms", "notfound"]:
    exec((HERE / "pages" / f"{name}.py").read_text())
