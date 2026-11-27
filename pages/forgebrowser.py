FB_VERSION = "0.4.0"
FB_REL = "https://github.com/asteya01/forge-browser/releases/download/v0.4.0/"
FB_ANCHORS = [("#features", "Features"), ("#download", "Download"), ("#look", "Themes"), ("#privacy", "Privacy"), ("#faq", "FAQ")]
page("forgebrowser.html", "Forge Browser by Forgeline", "Forge Browser: a fast, private browser with a built-in AI side panel that can run offline. Free for Windows, Mac, Linux and ChromeOS.", """
<main id="top">
<section class="band hero"><div class="wrap">
  <h1>A private browser<br>with AI built in.</h1>
  <p class="lede">Forge Browser blocks trackers, upgrades connections to HTTPS and puts an AI assistant in a side panel. The assistant can run fully offline with Ollama, so nothing has to leave your computer.</p>
  <div class="cta"><a class="btn hot" id="dl-hero" href="#download">Download Forge Browser</a><a class="btn ghost" href="#features">See what's inside</a></div>
  <ul class="facts"><li>Windows, Mac, Linux and ChromeOS</li><li>Trackers blocked by default</li><li>Ask AI with no account</li><li>Free, MIT licensed</li></ul>
  <div class="forge">
    <figure class="frame" style="position:relative;z-index:1">
      <img src="img/fb-newtab.webp" alt="Forge Browser's new tab page: the Forge logo, a search box and a row of shortcut tiles on a dark background" width="1280" height="800">
    </figure>
  </div>
  <p class="note">A real screenshot of Forge Browser {v} running on Linux.</p>
</div></section>

<section class="band alt" id="download"><div class="wrap">
  <h2>Download Forge Browser {v}</h2>
  <p class="sub">Free, 64-bit, about 90 to 160 MB. These first builds aren't code-signed yet, so Windows and Mac show a one-time warning on first launch. Each card below says what to click.</p>
  <div class="dlgrid">
    <article class="dlcard" id="windows" data-os="windows">
      <h3>Windows</h3>
      <p class="dlmeta">Windows 10 or 11, 64-bit</p>
      <div class="dlbtns"><a class="btn hot" href="{rel}forge-browser-{v}-windows-x64.zip">Download for Windows</a></div>
      <ol class="dlsteps">
        <li>Right-click the zip and choose <b>Extract All</b>.</li>
        <li>Open the folder and run <code>Forge Browser.exe</code>. No installer needed.</li>
        <li>If SmartScreen appears, choose <b>More info</b>, then <b>Run anyway</b>.</li>
        <li>Right-click its taskbar icon and choose <b>Pin to taskbar</b>.</li>
      </ol>
    </article>
    <article class="dlcard" id="macos" data-os="mac">
      <h3>Mac</h3>
      <p class="dlmeta">macOS 11 or newer. Pick your chip: Apple menu, then About This Mac.</p>
      <div class="dlbtns"><a class="btn hot" href="{rel}forge-browser-{v}-mac-arm64.zip">Apple silicon (M1 or newer)</a><a class="btn ghost" href="{rel}forge-browser-{v}-mac-x64.zip">Intel</a></div>
      <ol class="dlsteps">
        <li>Unzip it and drag <b>Forge Browser</b> into Applications.</li>
        <li>Right-click the app, choose <b>Open</b>, then <b>Open</b> again.</li>
        <li>If macOS says the app is damaged, run the two commands under <a href="#faq">Questions</a> once.</li>
        <li>Right-click its Dock icon and choose <b>Options</b>, then <b>Keep in Dock</b>.</li>
      </ol>
    </article>
    <article class="dlcard" id="linux" data-os="linux">
      <h3>Linux</h3>
      <p class="dlmeta">Debian, Ubuntu and Raspberry Pi OS use the .deb. Other distributions use the zip.</p>
      <div class="dlbtns"><a class="btn hot" href="{rel}forge-browser_{v}_amd64.deb">.deb for Intel or AMD</a><a class="btn ghost" href="{rel}forge-browser_{v}_arm64.deb">.deb for ARM64</a></div>
      <div class="dlbtns"><a class="btn ghost" href="{rel}forge-browser-{v}-linux-x64.zip">Zip, Intel or AMD</a><a class="btn ghost" href="{rel}forge-browser-{v}-linux-arm64.zip">Zip, ARM64</a></div>
      <div class="code"><button class="copy" type="button">Copy</button><pre>sudo apt install ./forge-browser_{v}_amd64.deb</pre></div>
      <p class="dlmeta" style="margin-top:12px">Then open it from your app menu and pin it to the dock. With the zip, unzip it and run <code>./install.sh</code>.</p>
    </article>
    <article class="dlcard" id="chromeos" data-os="chromeos">
      <h3>ChromeOS</h3>
      <p class="dlmeta">Chromebooks that support Linux apps. Forge runs in ChromeOS's Linux environment.</p>
      <div class="dlbtns"><a class="btn hot" href="{rel}forge-browser_{v}_amd64.deb">Intel or AMD Chromebook</a><a class="btn ghost" href="{rel}forge-browser_{v}_arm64.deb">ARM Chromebook</a></div>
      <ol class="dlsteps">
        <li>Turn on Linux: <b>Settings</b>, then <b>Advanced</b>, <b>Developers</b>, <b>Linux development environment</b>.</li>
        <li>Download the .deb that matches your Chromebook. Most are Intel or AMD. MediaTek and Snapdragon models are ARM.</li>
        <li>Open <b>Files</b>, double-click the .deb in Downloads, then choose <b>Install</b>.</li>
        <li>Open Forge Browser from the launcher's <b>Linux apps</b> folder, then right-click its shelf icon and choose <b>Pin</b>.</li>
      </ol>
    </article>
  </div>
  <details class="sums"><summary>Check your download (SHA-256)</summary>
    <p class="dlmeta">Compare the checksum of your file with this list to be sure it downloaded intact. On Windows run <code>certutil -hashfile FILE SHA256</code>. On Mac and Linux run <code>shasum -a 256 FILE</code>. <a href="SHA256SUMS-forge-browser-{v}.txt">Download the list</a>.</p>
    <div class="scroll"><table class="stack"><thead><tr><th>File</th><th>SHA-256</th></tr></thead><tbody>{sums}</tbody></table></div>
  </details>
  <p class="fine">Looking for the source and every release? See <a href="https://github.com/asteya01/forge-browser/releases">all releases on GitHub</a>.</p>
</div></section>

<section class="band" id="features"><div class="wrap">
  <h2>What's inside</h2>
  <p class="sub">The basics done carefully, plus a few things most browsers don't have.</p>
  <div class="ledger">
    <div><h3>Tracker blocking, on by default</h3><p>Blocks requests to 101 known tracking hosts and shows how many it stopped. Third-party cookies are blocked and the Global Privacy Control signal is sent.</p></div>
    <div><h3>HTTPS first</h3><p>Sites are upgraded to a secure connection. If one can't be, you see a clear warning and choose whether to continue.</p></div>
    <div><h3>Ask Forge, a side panel</h3><p>Ask about the page you're on, or anything else. Use Ollama on your own computer with no key, or connect Claude or any OpenAI-compatible service. Page text is sent only when you tick the box.</p></div>
    <div><h3>Ten themes and your own color</h3><p>Pick a theme, choose any accent color and tint the surfaces. Every part of the browser changes at once, including menus and settings.</p></div>
    <div><h3>New tab you can make yours</h3><p>A calm page with your shortcuts, plus 14 backgrounds or your own picture. No clock, no feed, no ads.</p></div>
    <div><h3>The everyday things</h3><p>Tabs you can drag, mute and reopen. Find in page, zoom, downloads, bookmarks, history and private windows.</p></div>
  </div>
</div></section>

<section class="band alt" id="look"><div class="wrap">
  <h2>Looks the way you want</h2>
  <p class="sub">Light or dark, quiet or colorful. Your choice follows you into every Forge page.</p>
  <ul class="shots3 plain">
    <li><figure class="frame"><img src="img/fb-themes.webp" alt="Forge Browser's settings page showing ten theme previews, each a tiny browser in that theme's colors" loading="lazy" width="1280" height="800"></figure>
      <h3>Pick a theme</h3><p>Ten themes, each previewed in its own colors, plus Match system.</p></li>
    <li><figure class="frame"><img src="img/fb-daylight.webp" alt="Forge Browser's new tab page in the light Daylight theme" loading="lazy" width="1280" height="800"></figure>
      <h3>Go light</h3><p>Daylight, Sakura and Meadow are full light themes.</p></li>
    <li><figure class="frame"><img src="img/fb-aurora.webp" alt="Forge Browser's new tab page with a green and violet aurora background" loading="lazy" width="1280" height="800"></figure>
      <h3>Add a background</h3><p>Choose a color, a pattern or your own picture for the new tab.</p></li>
  </ul>
</div></section>

<section class="band safe" id="privacy"><div class="wrap">
  <h2>Private by default</h2>
  <p class="sub">Forge Browser has no accounts, no sync servers and no analytics.</p>
  <div class="guard">
    <div><h3>No telemetry</h3><p>Forge doesn't report what you do. Your history stays on your computer.</p></div>
    <div><h3>AI only when you ask</h3><p>Nothing goes to an AI until you send a message in the Ask panel.</p></div>
    <div><h3>Offline with Ollama</h3><p>Use a free local model and the conversation never leaves your computer.</p></div>
    <div><h3>Keys in your keychain</h3><p>An API key is stored in your system's secure keychain, never in a plain file.</p></div>
  </div>
</div></section>

<section class="band" id="faq"><div class="wrap">
  <h2>Questions</h2>
  <div class="faq">
    <details><summary>Is Forge Browser free?</summary><p>Yes. It's free and open source under the MIT license. If you connect a paid AI service with your own key, that service may charge you. Ollama is free.</p></details>
    <details><summary>Why does Windows or Mac warn me?</summary><p>These first builds aren't code-signed, which costs money and takes time we haven't spent yet. On Windows choose <b>More info</b>, then <b>Run anyway</b>. On Mac, right-click the app and choose <b>Open</b>. Check the SHA-256 list above if you want to be sure the file is the one we published.</p></details>
    <details><summary>The Mac says the app is "damaged"</summary><p>That's how macOS treats unsigned apps on Apple silicon. Run these two commands in Terminal once, after moving the app to Applications:</p>
      <div class="code"><button class="copy" type="button">Copy</button><pre>xattr -dr com.apple.quarantine "/Applications/Forge Browser.app"
codesign --force --deep -s - "/Applications/Forge Browser.app"</pre></div></details>
    <details><summary>Does it work on a Chromebook?</summary><p>Yes, on Chromebooks that support Linux apps, which is most models from 2019 on. ChromeOS runs Forge inside its Linux environment, so Forge opens as its own window next to Chrome. It can't replace Chrome itself, and it isn't a Chrome extension. If animations feel slow, open Settings in Forge and set Motion to Off.</p></details>
    <details><summary>How do I know if my Chromebook is Intel or ARM?</summary><p>Most Chromebooks are Intel or AMD. Models with a MediaTek or Qualcomm Snapdragon chip are ARM. If you're not sure, open the Linux terminal and run <code>uname -m</code>. If it says <code>x86_64</code>, get the Intel or AMD file. If it says <code>aarch64</code>, get the ARM file.</p></details>
    <details><summary>Does it have extensions, sync or a password manager?</summary><p>Not yet. Forge Browser is young. Right now it covers browsing, privacy, the Ask panel, themes, bookmarks, history and downloads. Extensions, sync and restoring your tabs after a restart are on the list.</p></details>
    <details><summary>How do I use the Ask panel without paying for anything?</summary><p>Install <a href="https://ollama.com">Ollama</a> and get a model, then press <b>Ctrl+Shift+A</b> in Forge. It finds Ollama on its own.</p>
      <div class="code"><button class="copy" type="button">Copy</button><pre>ollama pull llama3.2</pre></div></details>
    <details><summary>Does it update itself?</summary><p>Not yet. Come back to this page for new versions. Automatic updates are planned.</p></details>
  </div>
</div></section>

<section class="band alt"><div class="wrap">
  <div class="snap">
    <div><h2 style="font-size:clamp(26px,3vw,36px)">Also from Forgeline</h2>
    <p class="sub">Newton puts AI in your terminal. Freezeframe copies code out of coding videos.</p></div>
    <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn ghost" href="newton.html">See Newton</a><a class="btn ghost" href="freezeframe.html">See Freezeframe</a></div>
  </div>
</div></section>
</main>
""".replace("{v}", FB_VERSION).replace("{rel}", FB_REL).replace("{sums}", "".join(
    f'<tr><td><code>{l.split("  ")[1]}</code></td><td><code style="word-break:break-all">{l.split("  ")[0]}</code></td></tr>'
    for l in (HERE / "assets" / f"SHA256SUMS-forge-browser-{FB_VERSION}.txt").read_text().strip().splitlines())),
    product="Forge Browser", anchors=FB_ANCHORS, cta=("#download", "Download"),
    extra_script="""<script>
(function(){
var ua=navigator.userAgent,os=/CrOS/.test(ua)?'chromeos':/Android/.test(ua)?'':/Windows/.test(ua)?'windows':/Mac/.test(ua)&&!/iPhone|iPad/.test(ua)?'mac':/Linux/.test(ua)?'linux':'';
if(!os)return;
var names={windows:'Windows',mac:'Mac',linux:'Linux',chromeos:'ChromeOS'};
var card=document.querySelector('.dlcard[data-os="'+os+'"]');
if(card){card.setAttribute('data-rec','');var b=document.createElement('span');b.className='badge';b.textContent='Recommended for this device';card.insertBefore(b,card.firstChild);
var grid=card.parentNode;grid.insertBefore(card,grid.firstChild)}
var h=document.getElementById('dl-hero');if(h){h.textContent='Download for '+names[os];h.href='#'+(os==='mac'?'macos':os)}
})();
</script>
""")
