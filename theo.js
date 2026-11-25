/* Theo: a scripted helper. Ready-made answers only, no live AI. */
{
  const INTRO =
    "Hi, I'm Theo, the helper for Forgeline's tools. I answer common questions about Newton and Freezeframe. My answers are ready-made, not a live AI, so for anything else please email <a href=\"mailto:tangriasteya@gmail.com\">tangriasteya@gmail.com</a> or <a href=\"founders.html\">contact the founder</a>. Pick a question below to start.";

  const GROUPS = [
    {
      name: 'Newton',
      items: [
        ['What is Newton?', 'Newton turns plain English into shell commands. Type what you want, press <b>Tab</b>, and the command replaces your words on the prompt. You read it, edit it if you like, and press Enter. Nothing runs until you do.'],
        ['How do I install Newton?', 'Download <code>newton.zip</code>, unzip it, then run <code>sh install.sh</code> inside the folder. You need Python 3.9 or newer, and on Windows you use WSL. The <a href="newton.html#install">install steps</a> cover each system.'],
        ['Does it run commands for me?', 'No. Newton only writes the command on your line, and you press Enter to run it. In plan mode you approve every step, and local safety rules flag dangerous commands whatever the AI suggests.'],
        ['What commands does Newton have?', 'Tab does most of the work. Beyond that there are <code>newton plan</code>, <code>newton agent</code>, <code>newton ask</code>, <code>newton fix</code>, <code>newton commit</code> and more. The <a href="newton.html#commands">commands section</a> lists them all.'],
        ['What is Iris?', 'Iris is Newton\'s chat agent. Run <code>newton agent</code> and it opens in a browser window on your own computer, working in your current folder. It runs read-only steps by itself and asks before it changes anything.'],
        ['Is Newton free?', 'Yes. Newton Free costs $0 and is MIT licensed. You bring your own AI: Ollama is free and runs on your computer, or you can use your own API key.'],
        ['What does Newton Max cost?', 'Newton Max is planned at $7 a month, with hosted models, priority email support and early access. It isn\'t billing yet, but you can reserve a spot in the <a href="newton.html#pricing">pricing section</a>.'],
        ['What does Newton send to the AI?', 'For Tab, your request plus a short description of your setup: OS, shell, current folder, project type, installed tool names and top-level file names. You can turn that off. File contents, environment variables and shell history are never sent. Plan mode, ask, fix and commit send more, such as a failed step\'s output or your staged diff, only when you use them, and secrets are redacted first.'],
        ['Can I use it offline?', 'Yes. Run <code>ollama pull llama3.1</code>, then <code>newton config provider ollama</code> and <code>newton config model llama3.1</code>. With Ollama nothing leaves your computer, and there\'s no telemetry.'],
        ['Which systems does it support?', 'macOS, Linux, Chromebook, and Windows through WSL, in zsh, bash 4+ or fish. Native PowerShell isn\'t supported. Newton is one file and needs Python 3.9 or newer.'],
        ['How do I contact you?', 'I can\'t take messages, but the founder can. Email <a href="mailto:tangriasteya@gmail.com">tangriasteya@gmail.com</a>, or open the <a href="founders.html">Founders page</a> for GitHub and the contact number.'],
      ],
    },
    {
      name: 'Freezeframe',
      items: [
        ['What is Freezeframe?', 'A Chrome extension that copies code out of coding videos. Freeze the video, drag a box around the code, and get real text with the indentation intact. See the <a href="freezeframe.html">Freezeframe page</a>.'],
        ['How do I install Freezeframe?', 'It isn\'t in the Chrome Web Store yet. Unzip the download, open <code>chrome://extensions</code>, turn on Developer mode, click Load unpacked and pick the folder. <a href="freezeframe.html#install">Full steps are here</a>.'],
        ['Does Freezeframe upload my screen?', 'No. The code is read on your computer. Only if you turn on AI assist and press an AI button does the code text go to the AI you chose, and with Ollama it stays on your computer.'],
        ['Which browsers does it work in?', 'Chrome, Edge, Brave, Arc and other Chromium browsers on Windows, Mac, Linux and Chromebook. It doesn\'t work in Firefox, Safari or phone browsers.'],
      ],
    },
  ];

  const reduced = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  const opts = GROUPS.map(
    (g, gi) => `<optgroup label="${g.name}">${g.items.map((it, ii) => `<option value="${gi}-${ii}">${it[0]}</option>`).join('')}</optgroup>`
  ).join('');

  const wrap = document.createElement('div');
  wrap.innerHTML = `
    <button class="theo-fab" type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="theo-panel"><span class="theo-av" aria-hidden="true">T</span>Ask Theo</button>
    <section class="theo" id="theo-panel" role="dialog" aria-label="Chat with Theo" tabindex="-1" inert>
      <header class="theo-head"><span class="theo-av" aria-hidden="true">T</span><div><b>Theo</b><small>Forgeline's helper</small></div>
        <button class="theo-x" type="button" aria-label="Close chat"><svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="m4 4 8 8M12 4l-8 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button></header>
      <div class="theo-log" role="log" aria-live="off"></div>
      <div class="sr" aria-live="polite"></div>
      <footer class="theo-foot"><label class="sr" for="theo-q">Choose a question</label>
        <select id="theo-q" disabled><option value="">Choose a question…</option>${opts}</select></footer>
    </section>`;
  document.body.append(...wrap.children);

  const fab = document.querySelector('.theo-fab');
  const panel = document.getElementById('theo-panel');
  const log = panel.querySelector('.theo-log');
  const live = panel.querySelector('.sr');
  const sel = document.getElementById('theo-q');
  let run = 0;

  const toEnd = () => { log.scrollTop = log.scrollHeight; };
  const add = (cls, html = '') => {
    const m = document.createElement('div');
    m.className = `tmsg ${cls}`;
    m.innerHTML = html;
    log.appendChild(m);
    toEnd();
    return m;
  };

  /* Reveal the text of a message gradually, keeping links and code intact. */
  function typeInto(el, html, tok) {
    return new Promise((done) => {
      el.innerHTML = html;
      const nodes = [];
      const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      let n;
      while ((n = w.nextNode())) nodes.push([n, n.nodeValue]);
      const total = nodes.reduce((a, [, t]) => a + t.length, 0);
      if (reduced() || !total) return done();
      nodes.forEach(([node]) => (node.nodeValue = ''));
      el.classList.add('typing');
      const dur = Math.min(2600, Math.max(700, total * 14));
      const t0 = performance.now();
      const step = (now) => {
        if (tok !== run) return done();
        const k = Math.min(total, Math.floor(((now - t0) / dur) * total));
        let left = k;
        for (const [node, t] of nodes) {
          const c = Math.min(left, t.length);
          node.nodeValue = t.slice(0, c);
          left -= c;
        }
        toEnd();
        if (k < total) requestAnimationFrame(step);
        else { el.classList.remove('typing'); done(); }
      };
      requestAnimationFrame(step);
    });
  }

  async function say(html, tok) {
    if (!reduced()) {
      const d = add('bot dots', '<i></i><i></i><i></i>');
      await sleep(650);
      d.remove();
      if (tok !== run) return;
    }
    const m = add('bot');
    await typeInto(m, html, tok);
    if (tok === run) { m.classList.remove('typing'); live.textContent = m.textContent; }
  }

  async function open() {
    const tok = ++run;
    log.innerHTML = '';
    live.textContent = '';
    sel.disabled = true;
    sel.value = '';
    panel.inert = false;
    panel.classList.add('open');
    fab.classList.add('hide');
    fab.setAttribute('aria-expanded', 'true');
    panel.focus();
    await say(INTRO, tok);
    if (tok === run) { sel.disabled = false; }
  }

  function close(returnFocus = true) {
    run++;
    panel.classList.remove('open');
    panel.inert = true;
    fab.classList.remove('hide');
    fab.setAttribute('aria-expanded', 'false');
    if (returnFocus) fab.focus();
  }

  fab.addEventListener('click', open);
  panel.querySelector('.theo-x').addEventListener('click', () => close());
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && panel.classList.contains('open')) close();
  });
  // Following a link inside the chat closes it, so the page behind is visible.
  log.addEventListener('click', (e) => { if (e.target.closest('a')) close(false); });

  sel.addEventListener('change', async () => {
    if (!sel.value) return;
    const [gi, ii] = sel.value.split('-').map(Number);
    const [q, a] = GROUPS[gi].items[ii];
    const tok = run;
    sel.disabled = true;
    add('me', q);
    sel.value = '';
    await say(a, tok);
    if (tok === run) { sel.disabled = false; sel.focus(); }
  });
}
