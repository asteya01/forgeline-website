FF_ANCHORS = [("#how", "How it works"), ("#ai", "AI assist"), ("#accuracy", "Accuracy"), ("#privacy", "Privacy"), ("#install", "Install"), ("#faq", "FAQ")]
page("freezeframe.html", "Freezeframe by Forgeline", "Freezeframe: pause a coding tutorial, drag around the code, get real text with the indentation intact. Optional AI to fix, explain or improve it.", """
<main id="top">
<section class="band hero"><div class="wrap">
  <h1>Pause the tutorial.<br>Copy the code.</h1>
  <p class="lede">Freezeframe is a Chrome extension that turns code inside any video into real, correctly indented text in about three seconds. No more pausing, squinting and retyping by hand.</p>
  <div class="cta"><a class="btn hot" href="#install">Add Freezeframe to Chrome</a><a class="btn ghost" href="#how">See how it works</a></div>
  <ul class="facts"><li>Works on YouTube and any site with video</li><li>Reads the code on your computer</li><li>Optional AI: fix, explain, improve</li><li>Free, MIT licensed</li></ul>
  <div class="forge">
    <figure class="frame" style="position:relative;z-index:1">
      <div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span>youtube.com · Build a GitHub CLI in Python</span></div>
      <img src="img/ff-result.webp" alt="A paused Python tutorial with the Freezeframe panel showing the 21 lines of code it read, highlighted as Python, with Copy code, Edit, download, Sharpen and AI buttons" width="1140" height="720">
    </figure>
  </div>
  <p class="note">A real capture from Freezeframe's automated test, which runs in real Chrome on a rendered tutorial video.</p>
</div></section>

<section class="band" id="video"><div class="wrap">
  <h2>See Freezeframe in about a minute</h2>
  <p class="sub">Freeze a video, drag around the code, and copy real text. Then see what AI assist can do. Captions are on the CC button.</p>
  <figure class="vidwrap">
    <video controls preload="metadata" playsinline poster="freezeframe-intro-poster.webp" width="1920" height="1080" aria-describedby="vid-note"><source src="freezeframe-intro.mp4" type="video/mp4"><track kind="captions" src="freezeframe-intro.vtt" srclang="en" label="English">Your browser can't play this video. <a href="freezeframe-intro.mp4">Download it instead</a>.</video>
    <figcaption id="vid-note">About 1 minute, with sound and captions. The AI answer shown is a sample from a test model.</figcaption>
  </figure>
</div></section>

<section class="band alt" id="how"><div class="wrap">
  <h2>Three steps, about three seconds</h2>
  <p class="sub">Code in videos is right there on screen, but you can't select it. Freezeframe fixes that.</p>
  <ol class="shots3">
    <li><figure class="frame"><img src="img/ff-frozen.webp" alt="The video frozen, with a hint to drag around the code" loading="lazy" width="1100" height="695"></figure>
      <h3>Freeze</h3><p>Click the freeze button in the YouTube player, or press <kbd style="color:var(--ink);background:var(--bg2);border-color:var(--line)">Alt</kbd>+<kbd style="color:var(--ink);background:var(--bg2);border-color:var(--line)">Shift</kbd>+<kbd style="color:var(--ink);background:var(--bg2);border-color:var(--line)">F</kbd>. The video pauses.</p></li>
    <li><figure class="frame"><img src="img/ff-select.webp" alt="A selection box being dragged around the code" loading="lazy" width="1100" height="695"></figure>
      <h3>Drag</h3><p>Draw a box around the code. Press Enter instead to grab the whole frame, and Freezeframe drops the file tree for you.</p></li>
    <li><figure class="frame"><img src="img/ff-result.webp" alt="The code panel with the result" loading="lazy" width="1140" height="720"></figure>
      <h3>Paste</h3><p>Get highlighted, editable code. Copy it, download it as a file, or find it later in your library.</p></li>
  </ol>
</div></section>

<section class="band" id="ai"><div class="wrap">
  <div class="split" style="align-items:center">
    <div>
      <h2>AI that fixes, explains and improves</h2>
      <p class="sub">Press the AI button in the code panel and choose what you need. It's optional and stays off until you turn it on.</p>
      <ul class="ticks">
        <li><b>Fix misreads</b> repairs characters the reader got wrong, like 1 for l or a missing underscore</li>
        <li><b>Explain</b> describes the code in plain words, with a heads-up about likely bugs</li>
        <li><b>Make it better</b> fixes bugs and adds error handling, keeping it close to the video</li>
        <li>You see the suggestion first, then choose <b>Use this</b> or <b>Keep original</b></li>
        <li>Free and offline with Ollama, or use your own API key</li>
      </ul>
    </div>
    <div class="aigrid">
      <figure class="frame"><img src="img/ff-ai-fix.webp" alt="AI suggestion card with Use this, Copy and Keep original buttons" loading="lazy" width="570" height="690"></figure>
      <figure class="frame"><img src="img/ff-ai-explain.webp" alt="AI explanation in bullet points with a watch-out line" loading="lazy" width="570" height="445"></figure>
    </div>
  </div>
  <p class="note" style="text-align:left">Screenshots from the automated test, which uses a stand-in AI server, so the AI's answers shown here are sample text.</p>
</div></section>

<section class="band alt"><div class="wrap">
  <h2>Everything a learner needs</h2>
  <div class="ledger">
    <div><h3>Indentation that's actually right</h3><p>Code in videos uses a fixed-width font, so Freezeframe measures the characters and rebuilds every indent and blank line. That matters a lot for Python.</p></div>
    <div><h3>Line numbers removed</h3><p>Editor line numbers, tab titles and status bars are cleaned out, so you only get the code.</p></div>
    <div><h3>21 languages</h3><p>The language is detected automatically, highlighted, and used for the file type when you download.</p></div>
    <div><h3>Honest about doubts</h3><p>Words it isn't sure about are highlighted, so you know exactly what to double-check. Sharpen re-reads with stronger cleanup.</p></div>
    <div><h3>A library of every capture</h3><p>Search everything you've captured. <b>Watch at 3:42</b> jumps back to that exact moment in the video.</p></div>
    <div><h3>Works beyond YouTube</h3><p>A freeze button appears when you hover over a video on Udemy, Coursera, course sites and docs.</p></div>
  </div>
</div></section>

<section class="band" id="accuracy"><div class="wrap">
  <h2>Measured, not promised</h2>
  <p class="sub">Freezeframe's automated test renders tutorial videos, compresses them like YouTube does, and checks every character in real Chrome.</p>
  <div class="scroll"><table class="stack">
    <thead><tr><th>Test video</th><th class="n">Characters</th><th class="n">Lines exact</th><th class="n">Indentation</th></tr></thead>
    <tbody>
      <tr><td>1080p, dark theme Python, drag-select with line numbers</td><td class="n">100%</td><td class="n">21 / 21</td><td class="n">21 / 21</td></tr>
      <tr><td>1080p, dark theme Python, whole frame with sidebar</td><td class="n">99.8%</td><td class="n">20 / 21</td><td class="n">21 / 21</td></tr>
      <tr><td>720p, light theme JavaScript, video from another site</td><td class="n">99.7%</td><td class="n">12 / 13</td><td class="n">13 / 13</td></tr>
    </tbody>
  </table></div>
  <p class="fine">Results from Freezeframe 1.1.0's test run. Real videos vary with resolution, font size and blur, so check highlighted spots.</p>
</div></section>

<section class="band safe" id="privacy"><div class="wrap">
  <h2>Your code stays yours</h2>
  <p class="sub">Freezeframe has no servers, no accounts and no analytics.</p>
  <div class="guard">
    <div><h3>Read on your computer</h3><p>The text reader is built into the extension. Frames are never uploaded.</p></div>
    <div><h3>AI only when you ask</h3><p>Code goes to an AI only after you turn AI assist on and press an AI button.</p></div>
    <div><h3>Offline with Ollama</h3><p>Use a free local model and nothing leaves your computer at all.</p></div>
    <div><h3>Your key stays local</h3><p>An API key is saved on this device only. It's never synced.</p></div>
  </div>
</div></section>

<section class="band" id="install"><div class="wrap">
  <h2>Install in under a minute</h2>
  <p class="sub">Freezeframe isn't in the Chrome Web Store yet, so you load it yourself. It works in Chrome, Edge, Brave, Arc and other Chromium browsers.</p>
  <div class="cta" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:22px"><a class="btn hot" href="freezeframe-extension-v1.1.0.zip">Download Freezeframe 1.1.0</a></div>
  <ol class="steps">
    <li><h3>Unzip it</h3><p>Unzip <code>freezeframe-extension-v1.1.0.zip</code> somewhere you'll keep it, like your Documents folder.</p></li>
    <li><h3>Load it</h3><p>Open <code>chrome://extensions</code>, turn on <b>Developer mode</b>, click <b>Load unpacked</b>, and pick the unzipped folder.</p></li>
    <li><h3>Pin it and try it</h3><p>Pin Freezeframe from the puzzle-piece menu, open any coding tutorial, and press <b>Alt+Shift+F</b>.</p></li>
  </ol>
  <h3 style="margin-top:48px">Turn on free AI with Ollama</h3>
  <p class="sub">Install <a href="https://ollama.com">Ollama</a> and get a model, then turn on <b>AI assist</b> in Freezeframe's Settings and press <b>Test connection</b>:</p>
  <div class="code"><button class="copy" type="button">Copy</button><pre>ollama pull llama3.1</pre></div>
  <p class="sub">If the test says Ollama blocked the request, allow Chrome extensions and then restart Ollama:</p>
  <div class="code"><button class="copy" type="button">Copy</button><pre>launchctl setenv OLLAMA_ORIGINS "chrome-extension://*"</pre></div>
</div></section>

<section class="band alt" id="faq"><div class="wrap">
  <h2>Questions</h2>
  <div class="faq">
    <details><summary>Is Freezeframe free?</summary><p>Yes. It's free and open source under the MIT license. The AI features are free too with Ollama. If you use your own API key, that service may charge you.</p></details>
    <details><summary>Do I have to use the AI?</summary><p>No. AI assist is off until you turn it on. Reading the code, copying, editing and the library all work without it.</p></details>
    <details><summary>Does it upload my screen?</summary><p>No. The code is read on your own computer and frames are never uploaded. Only the code text goes to an AI, and only when you press an AI button.</p></details>
    <details><summary>Which sites does it work on?</summary><p>YouTube gets a button in the player. On other sites, like Udemy and Coursera, a freeze button appears when you hover over the video. The shortcut works on any video.</p></details>
    <details><summary>What if it misreads something?</summary><p>Spots it isn't sure about are highlighted. You can edit the code, press Sharpen to re-read it with stronger cleanup, or use AI's Fix misreads.</p></details>
    <details><summary>Why isn't it in the Chrome Web Store?</summary><p>It's coming. For now, you load it with Developer mode, which takes about a minute.</p></details>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="snap">
    <div><h2 style="font-size:clamp(26px,3vw,36px)">Also from Forgeline: Newton</h2>
    <p class="sub">AI in your terminal. Describe a task in plain English, press Tab, and get the command. Nothing runs until you press Enter.</p></div>
    <a class="btn ghost" href="newton.html">See Newton</a>
  </div>
</div></section>
</main>
""", product="Freezeframe", anchors=FF_ANCHORS, cta=("#install", "Add to Chrome"))
