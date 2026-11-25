page("index.html", "Forgeline", "Forgeline makes coding tools for every level: Newton for the terminal and Freezeframe for coding videos.", """
<main id="top">
<section class="band hero"><div class="wrap">
  <h1 style="font-size:clamp(44px,8vw,96px)">Forge ahead.</h1>
  <p class="lede">Forgeline makes coding tools for every level, from the first command you type to your thousandth deploy. Each one works right where you already are, so you spend less time searching and switching tabs, and more time building.</p>
  <div class="cta"><a class="btn hot" href="#products">See the tools</a><a class="btn ghost" href="about.html">Why we build them</a></div>

  <div class="pair" id="products">
    <a class="prodcard" href="newton.html">
      <div class="shot" aria-hidden="true"><div class="mini">
        <div class="dim">$ git status</div>
        <div class="dim">On branch main · nothing to commit</div>
        <div><span class="ps">~/site ❯</span> <span class="dim">find files bigger than 100MB</span></div>
        <div class="dim" style="margin:6px 0">press Tab</div>
        <div><span class="ps">~/site ❯</span> <span class="hotline">find . -type f -size +100M</span></div>
      </div></div>
      <div class="pc-body"><h2 style="font-size:clamp(26px,3vw,34px)">Newton</h2>
        <p>AI in your terminal. Describe a task in plain English, press Tab, and get the exact shell command. Nothing runs until you press Enter.</p>
        <span class="go">Explore Newton</span></div>
    </a>
    <a class="prodcard" href="freezeframe.html">
      <div class="shot"><img src="img/ff-result.webp" alt="Freezeframe showing code it read from a paused Python tutorial, with Copy, Edit, Sharpen and AI buttons" width="1140" height="720"></div>
      <div class="pc-body"><h2 style="font-size:clamp(26px,3vw,34px)">Freezeframe</h2>
        <p>Copy code straight out of coding videos. Freeze the tutorial, drag around the code, and get real text you can paste, edit, or improve with AI.</p>
        <span class="go">Explore Freezeframe</span></div>
    </a>
  </div>
</div></section>

<section class="band alt" style="padding-top:clamp(72px,9vw,128px)"><div class="wrap">
  <h2>How we build every tool</h2>
  <div class="cards3">
    <div><h3>Works where you already are</h3><p>Newton lives in your terminal and Freezeframe lives in your video player. No new app to open, no tab to switch to.</p></div>
    <div><h3>You stay in control</h3><p>Our tools suggest and you decide. Newton never runs a command on its own, and Freezeframe shows AI changes before they replace anything.</p></div>
    <div><h3>Private by default</h3><p>No telemetry and no accounts. Both tools can run fully offline with a free local AI model through Ollama.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap split">
  <div><h2>For beginners, and for everyone after</h2>
  <p class="sub">When you're learning, our tools show you the real command and the real code, so you pick it up as you go. Once you're experienced, they save you the flags you'd otherwise look up and the code you'd otherwise retype.</p></div>
  <div class="cards3" style="grid-template-columns:minmax(0,1fr);margin-top:0">
    <div><h3>Free and open source</h3><p>Both tools are free under the MIT license. Read the code, change it, and share it.</p></div>
    <div><h3>Bring your own AI</h3><p>Use Ollama on your own computer for free, or connect your own API key.</p></div>
  </div>
</div></section>

<section class="band cta-band"><div class="wrap">
  <h2>Built by a founder who codes every day</h2>
  <p class="sub">Forgeline started with one person who was tired of switching tabs to look up flags and pausing videos to retype code.</p>
  <div class="cta" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:26px"><a class="btn hot" href="founders.html">Meet the founder</a><a class="btn ghost" href="invest.html">Invest in Forgeline</a></div>
</div></section>
</main>
""")
