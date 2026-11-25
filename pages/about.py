page("about.html", "About Forgeline", "Why Forgeline exists, how we build our tools, and what we believe about learning to code.", """
<main id="top">
<section class="band phero"><div class="wrap">
  <h1>Built for people who learn and work in code</h1>
  <p class="lede">Forgeline makes coding easier to learn and faster to do. Our tools write the command or read the code, and you stay in control of what happens next.</p>
  <div class="cta"><a class="btn hot" href="index.html#products">See the tools</a><a class="btn ghost" href="founders.html">Meet the founder</a></div>
</div></section>

<section class="band alt"><div class="wrap">
  <h2>Why Forgeline exists</h2>
  <div class="ledger">
    <div><h3>You know the task, not the flags</h3><p>The right <code>tar</code> options, the <code>find</code> flag for “bigger than”, how to use <code>lsof</code> for a port. The usual fix is a browser search, a forum thread, then copy, paste and edit. <a href="newton.html">Newton</a> turns that whole loop into one key: type a sentence, press Tab, and the command appears in your prompt.</p></div>
    <div><h3>The code is on screen, but you can't select it</h3><p>Millions of people learn from coding videos, and every one of them pauses, squints and retypes. That's slow, and one indentation mistake breaks Python. <a href="freezeframe.html">Freezeframe</a> turns the code in the video into real text you can paste.</p></div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <h2>How we build</h2>
  <ol class="steps two">
    <li><h3>Our tools write. You decide.</h3><p>Newton never runs a command until you press Enter, and local safety rules flag dangerous commands whatever the AI says. Freezeframe shows AI changes before they replace anything.</p></li>
    <li><h3>Private by default</h3><p>No telemetry and no accounts. Newton removes secrets before anything is sent. Freezeframe reads code on your computer. With Ollama, nothing leaves your machine.</p></li>
    <li><h3>Tested for real</h3><p>Newton's tests open real zsh, bash and fish sessions, type a sentence and press Tab. Freezeframe's tests run real Chrome on rendered tutorial videos and check every character.</p></li>
    <li><h3>Works where you work</h3><p>Newton is one file that needs Python 3.9 or newer and no admin rights, on macOS, Linux, Chromebook and Windows through WSL. Freezeframe runs in Chrome and other Chromium browsers.</p></li>
  </ol>
</div></section>

<section class="band cta-band"><div class="wrap">
  <h2>Free and open</h2>
  <p class="sub">Newton and Freezeframe are released under the MIT license. Use your own AI: Ollama on your computer for free, or any OpenAI-compatible service with your own key. Newton also works with Claude.</p>
  <div class="cta" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:26px"><a class="btn hot" href="newton.html#install">Install Newton</a><a class="btn ghost" href="freezeframe.html#install">Install Freezeframe</a></div>
</div></section>
</main>
""")
