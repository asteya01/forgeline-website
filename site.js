/* Forgeline site: shared behaviour for every page. */
{
  // The founder's contact number. Put the real number here, e.g. '+1 555 123 4567'.
  // Until it's set, the button points people to GitHub instead.
  const CONTACT_NUMBER = '(279) 267-6299';
  const CONTACT_EMAIL = 'tangriasteya@gmail.com';
  const GITHUB = 'https://github.com/asteya01';

  // Mobile menu
  const mb = document.querySelector('.menu-btn');
  const links = document.querySelector('.links');
  if (mb && links) {
    mb.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      mb.setAttribute('aria-expanded', String(open));
      mb.textContent = open ? 'Close' : 'Menu';
    });
  }

  // Contact number: one button shows it with a rolling animation, and hides it again.
  const split = (t) => [...t].map((c, i) => `<span class="${/\d/.test(c) ? '' : 'sep'}" style="--i:${i}">${c}</span>`).join('');
  document.querySelectorAll('[data-reveal]').forEach((b) => {
    const out = document.getElementById(b.dataset.reveal);
    if (!out) return;
    const label = b.textContent.trim();
    b.innerHTML = `<span class="swap"><span class="s-show">${label}</span><span class="s-hide" aria-hidden="true">Hide number</span></span>`;
    b.setAttribute('aria-expanded', 'false');
    b.setAttribute('aria-controls', out.id);
    out.classList.add('reveal-out');
    out.inert = true;
    let built = false;
    const build = () => {
      built = true;
      if (CONTACT_NUMBER) {
        const tel = CONTACT_NUMBER.replace(/[^+\d]/g, '');
        out.innerHTML = `<div class="rv-clip"><div class="numcard"><div><span class="nc-label">Founder's number</span><a class="digits" href="tel:${tel}" aria-label="${CONTACT_NUMBER}">${split(CONTACT_NUMBER)}</a></div><div><span class="nc-label">Email</span><a class="nc-mail" href="mailto:${CONTACT_EMAIL}">${CONTACT_EMAIL}</a></div><button class="mini-btn" type="button" data-copynum>Copy number</button></div></div>`;
        out.querySelector('[data-copynum]').addEventListener('click', async (e) => {
          const c = e.currentTarget;
          try { await navigator.clipboard.writeText(CONTACT_NUMBER); c.textContent = 'Copied'; } catch (_) { c.textContent = 'Select and copy'; }
          c.classList.add('done');
          setTimeout(() => { c.textContent = 'Copy number'; c.classList.remove('done'); }, 1800);
        });
      } else {
        out.innerHTML = `<div class="rv-clip"><div class="numcard"><p class="nc-msg">The contact number isn't listed yet. Email <a href="mailto:${CONTACT_EMAIL}">${CONTACT_EMAIL}</a> or find the founder on <a href="${GITHUB}">GitHub</a>.</p></div></div>`;
      }
    };
    const set = (open) => {
      if (open && !built) build();
      out.inert = !open;
      out.classList.toggle('open', open);
      b.setAttribute('aria-expanded', String(open));
      b.querySelector('.s-show').setAttribute('aria-hidden', String(open));
      b.querySelector('.s-hide').setAttribute('aria-hidden', String(!open));
    };
    b.addEventListener('click', () => set(!out.classList.contains('open')));
    out.addEventListener('keydown', (e) => { if (e.key === 'Escape') { set(false); b.focus(); } });
  });

  // Press ripple on every button
  document.addEventListener('pointerdown', (e) => {
    const b = e.target.closest('.btn,.copy,.mini-btn,.menu-btn,.ctrl button,.cmdchip:not(.static),.theme-btn');
    if (!b || b.disabled || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const r = b.getBoundingClientRect();
    const d = Math.max(r.width, r.height) * 2.2;
    const s = document.createElement('span');
    s.className = 'ripple';
    s.style.cssText = `width:${d}px;height:${d}px;left:${e.clientX - r.left - d / 2}px;top:${e.clientY - r.top - d / 2}px`;
    b.appendChild(s);
    s.addEventListener('animationend', () => s.remove());
  });

  // Copy buttons sit right before a <pre>; comment lines are left out of the copy.
  document.addEventListener('click', async (e) => {
    const b = e.target.closest('.copy');
    if (!b) return;
    const pre = b.nextElementSibling;
    if (!pre) return;
    const txt = pre.innerText.split('\n').filter((l) => !l.trim().startsWith('#')).join('\n');
    try {
      await navigator.clipboard.writeText(txt);
      b.textContent = 'Copied';
      b.classList.add('done');
    } catch (_) {
      b.textContent = 'Select and copy';
    }
    setTimeout(() => { b.textContent = 'Copy'; b.classList.remove('done'); }, 1800);
  });

  // Click a command to copy it.
  document.addEventListener('click', async (e) => {
    const c = e.target.closest('[data-copy]');
    if (!c) return;
    const orig = c.dataset.label || (c.dataset.label = c.textContent);
    try {
      await navigator.clipboard.writeText(c.dataset.copy);
      c.textContent = 'Copied';
      c.classList.add('done');
    } catch (_) {
      c.textContent = 'Select and copy';
    }
    setTimeout(() => { c.textContent = orig; c.classList.remove('done'); }, 1600);
  });
}

/* Looping demo on the Newton page: type a request, press Tab, get the command. Nothing runs. */
{
  const root = document.querySelector('[data-loop]');
  if (root) {
    const SCENES = [
      { q: 'find every file over 100MB here', cmd: 'find . -type f -size +100M' },
      { q: 'undo my last git commit but keep the changes', cmd: 'git reset --soft HEAD~1' },
      { q: 'what is using port 3000', cmd: 'lsof -i :3000' },
    ];
    const text = root.querySelector('.lp-text');
    const hint = root.querySelector('.lp-hint');
    const caret = root.querySelector('.lp-caret');
    const btn = root.querySelector('.lp-pause');
    const steps = document.querySelectorAll('#how .steps li');
    const stepsBox = document.querySelector('#how .steps');
    const HINTS = [
      '<span>Type what you want in plain words</span>',
      '<span><kbd class="press">Tab</kbd> turns your words into the command</span>',
      '<span><kbd>Enter</kbd> runs it when you are ready. Nothing has run yet.</span>',
    ];
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const mark = (n) => steps.forEach((li, i) => li.classList.toggle('on', i === n));
    let playing = true, visible = true, run = 0, idx = 0;

    if (reduce) {
      // No motion: show one finished example and let people step through the others.
      const show = () => {
        text.textContent = SCENES[idx].cmd;
        hint.innerHTML = HINTS[2];
        caret.hidden = true;
      };
      btn.classList.add('next');
      btn.setAttribute('aria-label', 'Show the next example');
      btn.innerHTML = '<span>Next example</span>';
      btn.addEventListener('click', () => { idx = (idx + 1) % SCENES.length; show(); });
      show();
    } else {
      stepsBox && stepsBox.classList.add('live');
      const can = () => playing && visible && !document.hidden;
      const tick = (ms) => new Promise((r) => setTimeout(r, ms));
      const wait = async (ms, id) => {
        let left = ms;
        while (left > 0) {
          if (id !== run) return false;
          if (!can()) { await tick(150); continue; }
          const s = Math.min(left, 100);
          await tick(s);
          left -= s;
        }
        return id === run;
      };
      const play = async () => {
        const id = ++run;
        while (id === run) {
          const sc = SCENES[idx];
          text.classList.remove('out', 'hot');
          text.textContent = '';
          hint.innerHTML = HINTS[0];
          mark(0);
          if (!(await wait(500, id))) return;
          for (let i = 1; i <= sc.q.length; i++) {
            text.textContent = sc.q.slice(0, i);
            if (!(await wait(34 + Math.random() * 34, id))) return;
          }
          if (!(await wait(700, id))) return;
          mark(1);
          hint.innerHTML = HINTS[1];
          if (!(await wait(450, id))) return;
          text.textContent = sc.cmd;
          text.classList.add('hot');
          if (!(await wait(1400, id))) return;
          mark(2);
          hint.innerHTML = HINTS[2];
          if (!(await wait(3000, id))) return;
          text.classList.add('out');
          if (!(await wait(400, id))) return;
          idx = (idx + 1) % SCENES.length;
        }
      };
      btn.addEventListener('click', () => {
        playing = !playing;
        btn.setAttribute('aria-pressed', String(!playing));
        btn.setAttribute('aria-label', playing ? 'Pause the demo' : 'Play the demo');
        btn.classList.toggle('paused', !playing);
        caret.classList.toggle('still', !playing);
      });
      if ('IntersectionObserver' in window) {
        new IntersectionObserver((e) => { visible = e[0].isIntersecting; }, { threshold: 0.25 }).observe(root);
      }
      play();
    }
  }
}
