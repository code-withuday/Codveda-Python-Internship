<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>File Encryption Tool — Uday Anand</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --black:#050505;
  --white:#f0ede8;
  --gold:#c9a96e;
  --muted:#666;
  --border:#1a1a1a;
  --serif:'Cormorant Garamond',serif;
  --sans:'Inter',sans-serif;
  --mono:'JetBrains Mono',monospace;
}
html{scroll-behavior:smooth}
body{background:var(--black);color:var(--white);font-family:var(--sans);overflow-x:hidden;min-height:100vh}

.grid{position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.035}
.grid::before{content:'';position:absolute;top:0;left:25%;width:1px;height:100%;background:var(--white)}
.grid::after{content:'';position:absolute;top:0;right:25%;width:1px;height:100%;background:var(--white)}

nav{position:relative;z-index:10;padding:1.8rem 5rem;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--border)}
.nav-logo{font-family:var(--serif);font-size:1rem;font-weight:300;letter-spacing:.25em;color:var(--white);text-transform:uppercase;text-decoration:none}
.nav-back{font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.45);text-decoration:none;transition:color .3s;display:flex;align-items:center;gap:.5rem}
.nav-back:hover{color:var(--gold)}

main{position:relative;z-index:1;max-width:1000px;margin:0 auto;padding:5rem 5rem 6rem}

.page-tag{font-family:var(--mono);font-size:.65rem;letter-spacing:.3em;color:var(--gold);text-transform:uppercase;margin-bottom:1.5rem}
.page-title{font-family:var(--serif);font-size:clamp(3rem,7vw,5.5rem);font-weight:300;line-height:.95;letter-spacing:-.02em;margin-bottom:1rem}
.page-title em{font-style:italic;color:var(--gold)}
.page-sub{font-size:.85rem;color:rgba(255,255,255,.4);font-weight:300;max-width:480px;line-height:1.8;margin-bottom:3.5rem}

.tracker-layout{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start}

.panel-label{font-size:.62rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin-bottom:1.8rem;display:block}

.field{margin-bottom:1.8rem}
.field-label{font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:.8rem;display:block}
input, textarea{
  width:100%;
  background:transparent;
  border:none;
  border-bottom:1px solid var(--border);
  color:var(--white);
  font-family:var(--serif);
  font-size:1.4rem;
  font-weight:300;
  padding:.6rem 0;
  outline:none;
  transition:border-color .3s;
  resize:none;
}
input:focus, textarea:focus{border-color:var(--gold)}
input::placeholder, textarea::placeholder{color:rgba(255,255,255,.18)}

.mode-toggle{display:flex;gap:1px;background:var(--border);margin-bottom:2rem}
.mode-btn{flex:1;background:var(--black);border:none;color:rgba(255,255,255,.4);font-family:var(--mono);font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;padding:.9rem 0;cursor:pointer;transition:all .3s}
.mode-btn.active{color:var(--gold);background:#0a0a0a}

.shift-row{display:flex;align-items:center;gap:1.2rem;margin-bottom:1.8rem}
.shift-row input[type=range]{flex:1;-webkit-appearance:none;height:1px;background:var(--border);outline:none}
.shift-row input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;border-radius:50%;background:var(--gold);cursor:pointer}
.shift-val{font-family:var(--serif);font-size:1.3rem;color:var(--gold);min-width:30px;text-align:center}

.btn-calc{
  width:100%;
  background:transparent;
  border:1px solid var(--gold);
  color:var(--gold);
  font-family:var(--mono);
  font-size:.72rem;
  letter-spacing:.25em;
  text-transform:uppercase;
  padding:1.1rem 0;
  cursor:pointer;
  transition:all .35s;
  margin-top:1rem;
}
.btn-calc:hover{background:var(--gold);color:var(--black)}

.result-panel{
  border:1px solid var(--border);
  padding:3rem 2.5rem;
  min-height:280px;
  display:flex;
  flex-direction:column;
  justify-content:center;
  transition:border-color .4s;
  word-break:break-all;
}
.result-panel.active{border-color:var(--gold)}
.result-empty{font-size:.8rem;color:rgba(255,255,255,.25);font-weight:300;text-align:center;line-height:1.8}

.result-total-label{font-size:.62rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin-bottom:1rem;display:block}
.result-total{font-family:var(--mono);font-size:1.3rem;font-weight:400;line-height:1.6;color:var(--white)}

.copy-btn{margin-top:1.5rem;font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.35);background:none;border:none;cursor:pointer;transition:color .3s;padding:0;align-self:flex-start}
.copy-btn:hover{color:var(--gold)}

footer{position:relative;z-index:1;padding:2.5rem 5rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center}
footer p{font-family:var(--mono);font-size:.6rem;color:var(--muted);letter-spacing:.08em}

@media(max-width:768px){
  nav{padding:1.5rem 1.8rem}
  main{padding:3.5rem 1.8rem 4rem}
  .tracker-layout{grid-template-columns:1fr;gap:2.5rem}
  footer{padding:2rem 1.8rem;flex-direction:column;gap:.6rem;text-align:center}
}
</style>
</head>
<body>
<div class="grid"></div>

<nav>
  <a class="nav-logo" href="index.html">Uday Anand</a>
  <a class="nav-back" href="index.html">← Back to portfolio</a>
</nav>

<main>
  <p class="page-tag">Project demo</p>
  <h1 class="page-title">Encryption &amp;<br><em>Decryption.</em></h1>
  <p class="page-sub">A Python project that encrypts text using a Caesar Cipher — shifting each character's ASCII value by a fixed amount. This is a live browser version of the original script.</p>

  <div class="tracker-layout">

    <div>
      <span class="panel-label">01 — Enter message</span>

      <div class="mode-toggle">
        <button class="mode-btn active" id="encryptModeBtn">Encrypt</button>
        <button class="mode-btn" id="decryptModeBtn">Decrypt</button>
      </div>

      <div class="field">
        <label class="field-label" id="inputLabel">Message</label>
        <textarea id="msgInput" rows="2" placeholder="Type your message here..."></textarea>
      </div>

      <div class="field">
        <label class="field-label">Shift value</label>
        <div class="shift-row">
          <input type="range" id="shiftInput" min="1" max="25" value="3"/>
          <span class="shift-val" id="shiftVal">3</span>
        </div>
      </div>

      <button class="btn-calc" id="calcBtn">Run encryption</button>
    </div>

    <div>
      <span class="panel-label">02 — Result</span>
      <div class="result-panel" id="resultPanel">
        <p class="result-empty">Type a message, choose a<br>shift value, then run to see<br>the encrypted output.</p>
      </div>
    </div>

  </div>
</main>

<footer>
  <p>© 2026 Uday Anand</p>
  <p>Python Developer &amp; Graphic Designer · Delhi, India</p>
</footer>

<script>
let mode = 'encrypt';
const encryptBtn = document.getElementById('encryptModeBtn');
const decryptBtn = document.getElementById('decryptModeBtn');
const inputLabel = document.getElementById('inputLabel');
const calcBtn = document.getElementById('calcBtn');
const shiftInput = document.getElementById('shiftInput');
const shiftVal = document.getElementById('shiftVal');

shiftInput.addEventListener('input', () => { shiftVal.textContent = shiftInput.value; });

encryptBtn.addEventListener('click', () => {
  mode = 'encrypt';
  encryptBtn.classList.add('active');
  decryptBtn.classList.remove('active');
  inputLabel.textContent = 'Message';
  calcBtn.textContent = 'Run encryption';
});

decryptBtn.addEventListener('click', () => {
  mode = 'decrypt';
  decryptBtn.classList.add('active');
  encryptBtn.classList.remove('active');
  inputLabel.textContent = 'Encrypted message';
  calcBtn.textContent = 'Run decryption';
});

calcBtn.addEventListener('click', () => {
  const msg = document.getElementById('msgInput').value;
  const shift = parseInt(shiftInput.value) || 0;
  const panel = document.getElementById('resultPanel');

  if (!msg) {
    panel.classList.remove('active');
    panel.innerHTML = `<p class="result-empty" style="color:#d4574e">Please enter a message first.</p>`;
    return;
  }

  let result = '';
  const effectiveShift = mode === 'encrypt' ? shift : -shift;
  for (let i = 0; i < msg.length; i++) {
    result += String.fromCharCode(msg.charCodeAt(i) + effectiveShift);
  }

  panel.classList.add('active');
  panel.innerHTML = `
    <span class="result-total-label">${mode === 'encrypt' ? 'Encrypted message' : 'Decrypted message'}</span>
    <div class="result-total" id="resultText"></div>
    <button class="copy-btn" id="copyBtn">Copy result</button>
  `;
  document.getElementById('resultText').textContent = result;
  document.getElementById('copyBtn').addEventListener('click', () => {
    navigator.clipboard.writeText(result);
    const btn = document.getElementById('copyBtn');
    btn.textContent = 'Copied ✓';
    setTimeout(() => { btn.textContent = 'Copy result'; }, 1500);
  });
});
</script>
</body>
</html>
