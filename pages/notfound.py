import re as _re
page("404.html", "Page not found · Forgeline", "That page isn't here. Head back to Forgeline, Newton or Freezeframe.", """
<main id="top">
<section class="band hero nf"><div class="wrap">
  <p class="nf-code">Error 404</p>
  <h1>That page isn't here.</h1>
  <p class="lede">The link may have a typo, or the page may have moved. These will get you back on track.</p>
  <div class="cta"><a class="btn hot" href="index.html">Go to the home page</a><a class="btn ghost" href="newton.html">See Newton</a><a class="btn ghost" href="freezeframe.html">See Freezeframe</a></div>

  <div class="term nf-term" aria-hidden="true">
    <div class="dim"><span class="ps">~/forgeline ❯</span> cd that-page</div>
    <div class="err">zsh: no such file or directory: that-page</div>
    <div class="dim" style="margin-top:10px"><span class="ps">~/forgeline ❯</span> show me the pages that exist</div>
    <div class="dim" style="margin:4px 0">press Tab</div>
    <div><span class="ps">~/forgeline ❯</span> <span class="hotline">ls</span></div>
    <div class="ls">about  donate  founders  freezeframe  invest  newton  privacy  terms</div>
  </div>
</div></section>
</main>
""")
_p = OUT / "404.html"
_h = _p.read_text()
# Preview copy keeps relative links so it renders in the artifact viewer.
(HERE / "preview-404.html").write_text(_h)
# The live 404 page is served at whatever address was missing (even /a/b/c), so every link must start from the site root.
_h = _re.sub(r'(href|src)="(?!https?:|#|/|mailto:|tel:)([^"]+)"', r'\1="/\2"', _h)
_p.write_text(_h)
