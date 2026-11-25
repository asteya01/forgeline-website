page("privacy.html", "Privacy Policy · Forgeline", "What Forgeline's website, Newton and Freezeframe collect, what they send, and the choices you have.", """
<main id="top">
<section class="band phero"><div class="wrap">
  <h1>Privacy Policy</h1>
  <p class="lede">Forgeline's tools are built to keep your code and commands on your computer. This page explains what the website, Newton and Freezeframe do with your information.</p>
  <p class="fine">Last updated November 22, 2026</p>
</div></section>

<section class="band alt"><div class="wrap doc">
  <h2>The short version</h2>
  <ul>
    <li>Forgeline has no accounts, no analytics and no telemetry in Newton or Freezeframe.</li>
    <li>Nothing is sent to an AI service unless you set one up and use it. With Ollama, which runs on your own computer, nothing leaves your machine.</li>
    <li>We don't sell your information, and we don't have much of it to sell.</li>
  </ul>

  <h2>Newton</h2>
  <p>Newton runs in your terminal. When you press Tab, it sends your request plus a short description of your setup to the AI model you chose. That description covers your operating system, shell, current folder, project type, the names of installed tools and top-level file names. You can turn it off.</p>
  <p>Newton never sends file contents, environment variables or shell history. Commands such as <code>newton plan</code>, <code>newton ask</code>, <code>newton fix</code> and <code>newton commit</code> send more, for example the output of a failed step or your staged changes, but only when you run them. Secrets such as API keys are removed first.</p>
  <p>If you use Ollama, the model runs on your computer and nothing is sent anywhere. If you connect a cloud AI service with your own key, what Newton sends goes to that service, and its privacy policy applies. Newton keeps its settings and saved plans in files on your own computer.</p>

  <h2>Freezeframe</h2>
  <p>Freezeframe is a Chrome extension. The text reader (OCR) is built in and runs on your computer, so video frames are never uploaded. Freezeframe has no servers.</p>
  <ul>
    <li><b>AI assist</b> is off by default. When you turn it on and press an AI button, the code text in that panel and its language are sent to the service you picked: Ollama on your own computer, or an OpenAI-compatible service at the address you entered. Nothing is sent until you press an AI button.</li>
    <li><b>Your API key</b> is stored only in this browser's local extension storage. It is not synced and is sent only to the address you entered.</li>
    <li><b>What is stored on your device:</b> your captures (the code, a small thumbnail, the page address, the video title and the timestamp) and your settings. You can delete the captures from Settings → Clear library, or by removing the extension.</li>
    <li><b>Permissions:</b> access to all sites lets the freeze button appear on videos wherever they are and lets Freezeframe reach the AI address you chose. It does not read or send your browsing.</li>
  </ul>

  <h2>This website</h2>
  <p>The site has no accounts, cookies or analytics. It remembers your light or dark choice in your browser so the page doesn't flash on the next visit, and it stays on your device.</p>
  <p>The site loads its fonts from Google Fonts, so Google receives your IP address and browser details when a page loads, as with any site that uses them. When you press a "Click to see contact number" button, the number is shown on your screen; nothing is recorded. Theo, the helper chat, answers from a fixed set of answers inside the page and does not send what you click to anyone.</p>

  <h2>When you contact us</h2>
  <p>If you email us or call or message the number on the Founders page, we see your email address or number and anything you tell us. We use it to reply, and we don't add you to a list or share it.</p>

  <h2>Sharing</h2>
  <p>We don't sell or rent personal information. The only services that receive anything from our tools are the AI services you choose to connect. We may disclose information if the law requires it.</p>

  <h2>Children</h2>
  <p>Our tools are meant for people learning and working in code and don't ask for personal information. If you believe a child has given us personal information, tell us and we'll delete it.</p>

  <h2>Your choices</h2>
  <p>You control your data on your own device: delete Freezeframe captures, remove your API key, turn AI assist off, or uninstall either tool. For anything we hold from contact with you, ask and we'll delete it.</p>

  <h2>Changes</h2>
  <p>If we change this policy, we'll update the date at the top. If a change affects what Newton or Freezeframe send, we'll say so in the release notes.</p>

  <h2>Contact</h2>
  <p>Questions about this policy? Email <a href="mailto:tangriasteya@gmail.com">tangriasteya@gmail.com</a>, reach the founder on the <a href="founders.html">Founders page</a>, or:</p>
  <p><button class="btn hot" type="button" data-reveal="num1">Click to see contact number</button></p>
  <div class="reveal-out" id="num1" aria-live="polite"></div>
</div></section>
</main>
""")
