<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>To-Do List — Uday Anand</title>
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
body{background:var(--black);color:var(--white);font-family:var(--sans);min-height:100vh;display:flex;flex-direction:column;overflow-x:hidden;cursor:none}

.cursor{position:fixed;width:8px;height:8px;background:var(--white);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);mix-blend-mode:difference;transition:transform .15s}
.cursor-ring{position:fixed;width:36px;height:36px;border:1px solid rgba(255,255,255,0.25);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);transition:all .1s ease}

.grid{position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.03}
.grid::before{content:'';position:absolute;top:0;left:25%;width:1px;height:100%;background:var(--white)}
.grid::after{content:'';position:absolute;top:0;right:25%;width:1px;height:100%;background:var(--white)}

nav{position:fixed;top:0;left:0;right:0;z-index:200;padding:1.8rem 4rem;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid transparent;transition:border-color .3s}
nav.scrolled{border-color:var(--border);background:rgba(5,5,5,0.92);backdrop-filter:blur(12px)}
.nav-logo{font-family:var(--serif);font-size:1rem;font-weight:300;letter-spacing:.25em;color:var(--white);text-transform:uppercase;text-decoration:none}
.nav-tag{font-family:var(--mono);font-size:.6rem;letter-spacing:.2em;color:var(--gold);text-transform:uppercase}

main{flex:1;display:flex;flex-direction:column;align-items:center;padding:9rem 2rem 4rem;position:relative;z-index:1}

.page-tag{font-family:var(--mono);font-size:.65rem;letter-spacing:.4em;color:var(--gold);text-transform:uppercase;margin-bottom:1.5rem;opacity:0;animation:fadeUp .6s ease .2s forwards}
.page-title{font-family:var(--serif);font-size:clamp(3.5rem,8vw,6.5rem);font-weight:300;line-height:.92;letter-spacing:-.02em;text-align:center;margin-bottom:1rem;opacity:0;animation:fadeUp .8s ease .4s forwards}
.page-title em{font-style:italic;color:var(--gold)}
.page-sub{font-size:.78rem;color:rgba(255,255,255,.35);font-weight:300;letter-spacing:.05em;margin-bottom:3.5rem;text-align:center;opacity:0;animation:fadeUp .6s ease .6s forwards}

/* APP WRAP */
.app{width:100%;max-width:640px;opacity:0;animation:fadeUp .7s ease .8s forwards}

/* STATS */
.stats-row{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--border);margin-bottom:2.5rem}
.stat-box{background:var(--black);padding:1.4rem 1rem;text-align:center}
.stat-label{font-family:var(--mono);font-size:.55rem;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);margin-bottom:.5rem}
.stat-val{font-family:var(--serif);font-size:2.2rem;font-weight:300;color:var(--white)}
.stat-val.gold{color:var(--gold)}

/* INPUT */
.input-wrap{display:flex;border:1px solid #2a2a2a;background:#0a0a0a;margin-bottom:2.5rem;transition:border-color .3s}
.input-wrap:focus-within{border-color:var(--gold)}
.task-input{flex:1;background:transparent;border:none;outline:none;padding:1.2rem 1.6rem;font-family:var(--mono);font-size:.82rem;color:var(--white);letter-spacing:.05em}
.task-input::placeholder{color:rgba(255,255,255,.2)}
.add-btn{background:transparent;border:none;border-left:1px solid #2a2a2a;padding:1.2rem 1.8rem;cursor:pointer;color:var(--gold);font-family:var(--mono);font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;transition:background .3s,color .3s;white-space:nowrap}
.add-btn:hover{background:var(--gold);color:var(--black)}

/* FILTER */
.filter-row{display:flex;gap:0;margin-bottom:1.5rem;border:1px solid var(--border)}
.filter-btn{flex:1;background:transparent;border:none;padding:.7rem;font-family:var(--mono);font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);cursor:pointer;transition:all .2s;border-right:1px solid var(--border)}
.filter-btn:last-child{border-right:none}
.filter-btn.active{background:#0f0f0f;color:var(--gold)}

/* TASK LIST */
.task-list{display:flex;flex-direction:column;gap:1px;background:var(--border);margin-bottom:2rem}

.task-item{background:var(--black);padding:1.4rem 1.6rem;display:flex;align-items:center;gap:1.2rem;transition:background .3s;animation:slideIn .35s ease}
.task-item:hover{background:#080808}

.task-check{width:18px;height:18px;border:1px solid #333;cursor:pointer;flex-shrink:0;position:relative;transition:border-color .3s}
.task-check:hover{border-color:var(--gold)}
.task-check.done{border-color:var(--gold);background:rgba(201,169,110,.12)}
.task-check.done::after{content:'';position:absolute;top:3px;left:6px;width:4px;height:8px;border-right:1px solid var(--gold);border-bottom:1px solid var(--gold);transform:rotate(45deg)}

.task-num{font-family:var(--mono);font-size:.58rem;color:var(--muted);min-width:24px}
.task-text{flex:1;font-size:.85rem;font-weight:300;color:rgba(255,255,255,.75);transition:all .3s;line-height:1.5}
.task-text.done{color:var(--muted);text-decoration:line-through;text-decoration-color:#333}

.task-del{background:transparent;border:none;color:#333;cursor:pointer;font-size:1rem;padding:.2rem .4rem;transition:color .2s;font-family:var(--mono);line-height:1}
.task-del:hover{color:#e07070}

/* EMPTY */
.empty{text-align:center;padding:3.5rem 2rem;border:1px solid var(--border)}
.empty-title{font-family:var(--serif);font-size:2rem;font-weight:300;color:rgba(255,255,255,.08);font-style:italic;margin-bottom:.8rem}
.empty-sub{font-family:var(--mono);font-size:.58rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}

/* CLEAR BTN */
.clear-btn{width:100%;padding:1rem;border:1px solid #1a1a1a;background:transparent;color:rgba(255,255,255,.25);font-family:var(--mono);font-size:.62rem;letter-spacing:.18em;text-transform:uppercase;cursor:pointer;transition:all .3s}
.clear-btn:hover{border-color:#e07070;color:#e07070}

footer{padding:2rem 4rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;position:relative;z-index:1}
footer p{font-family:var(--mono);font-size:.58rem;color:var(--muted);letter-spacing:.08em}
footer a{color:var(--gold);text-decoration:none}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideIn{from{opacity:0;transform:translateX(-12px)}to{opacity:1;transform:translateX(0)}}

@media(max-width:600px){
  nav{padding:1.4rem 1.6rem}
  body{cursor:auto}
  .cursor,.cursor-ring{display:none}
  main{padding:7rem 1.2rem 3rem}
  footer{flex-direction:column;gap:.6rem;text-align:center;padding:1.5rem}
}
</style>
</head>
<body>

<div class="cursor" id="cur"></div>
<div class="cursor-ring" id="ring"></div>
<div class="grid"></div>

<nav id="nav">
  <a class="nav-logo" href="https://code-withuday.github.io/portfolio">Uday Anand</a>
  <span class="nav-tag">To-Do List</span>
</nav>

<main>
  <p class="page-tag">Python Project — Task Manager</p>
  <h1 class="page-title">Your <em>Tasks.</em></h1>
  <p class="page-sub">Add, manage and track your daily tasks efficiently.</p>

  <div class="app">

    <!-- STATS -->
    <div class="stats-row">
      <div class="stat-box">
        <div class="stat-label">Total</div>
        <div class="stat-val" id="statTotal">0</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Done</div>
        <div class="stat-val gold" id="statDone">0</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Pending</div>
        <div class="stat-val" id="statPending">0</div>
      </div>
    </div>

    <!-- INPUT -->
    <div class="input-wrap">
      <input class="task-input" id="taskInput" type="text" placeholder="Add a new task..." autocomplete="off"/>
      <button class="add-btn" onclick="addTask()">Add Task</button>
    </div>

    <!-- FILTER -->
    <div class="filter-row">
      <button class="filter-btn active" onclick="setFilter('all',this)">All</button>
      <button class="filter-btn" onclick="setFilter('pending',this)">Pending</button>
      <button class="filter-btn" onclick="setFilter('done',this)">Done</button>
    </div>

    <!-- LIST -->
    <div class="task-list" id="taskList"></div>

    <!-- CLEAR -->
    <button class="clear-btn" onclick="clearDone()">Clear Completed Tasks</button>

  </div>
</main>

<footer>
  <p>Built by <a href="https://code-withuday.github.io/portfolio">Uday Anand</a> · Python Developer</p>
  <p>To-Do List — Python Logic Project</p>
</footer>

<script>
// CURSOR
const cur=document.getElementById('cur'),ring=document.getElementById('ring');
let mx=0,my=0,rx=0,ry=0;
document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;cur.style.left=mx+'px';cur.style.top=my+'px'});
(function follow(){rx+=(mx-rx)*.12;ry+=(my-ry)*.12;ring.style.left=rx+'px';ring.style.top=ry+'px';requestAnimationFrame(follow)})();

// NAV SCROLL
window.addEventListener('scroll',()=>{
  document.getElementById('nav').classList.toggle('scrolled',window.scrollY>20)
});

let tasks = [];
let filter = 'all';
let idCounter = 0;

function addTask(){
  const input = document.getElementById('taskInput');
  const text = input.value.trim();
  if(!text) return;
  tasks.push({id: ++idCounter, text, done: false});
  input.value = '';
  render();
}

function toggleTask(id){
  const t = tasks.find(t => t.id === id);
  if(t) t.done = !t.done;
  render();
}

function deleteTask(id){
  tasks = tasks.filter(t => t.id !== id);
  render();
}

function clearDone(){
  tasks = tasks.filter(t => !t.done);
  render();
}

function setFilter(f, btn){
  filter = f;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  render();
}

function render(){
  const total = tasks.length;
  const done = tasks.filter(t => t.done).length;
  document.getElementById('statTotal').textContent = total;
  document.getElementById('statDone').textContent = done;
  document.getElementById('statPending').textContent = total - done;

  const filtered = tasks.filter(t => {
    if(filter === 'done') return t.done;
    if(filter === 'pending') return !t.done;
    return true;
  });

  const list = document.getElementById('taskList');

  if(filtered.length === 0){
    list.innerHTML = `
      <div class="empty">
        <div class="empty-title">${filter === 'done' ? 'Nothing done yet.' : filter === 'pending' ? 'All caught up.' : 'No tasks yet.'}</div>
        <div class="empty-sub">${filter === 'all' ? 'Add your first task above' : ''}</div>
      </div>`;
    return;
  }

  list.innerHTML = filtered.map((t, i) => `
    <div class="task-item">
      <div class="task-check ${t.done?'done':''}" onclick="toggleTask(${t.id})"></div>
      <span class="task-num">${String(i+1).padStart(2,'0')}</span>
      <span class="task-text ${t.done?'done':''}">${t.text}</span>
      <button class="task-del" onclick="deleteTask(${t.id})">×</button>
    </div>
  `).join('');

  // Cursor effect on new elements
  document.querySelectorAll('.task-item,.task-del,.task-check').forEach(el=>{
    el.addEventListener('mouseenter',()=>{ring.style.transform='translate(-50%,-50%) scale(2)';ring.style.borderColor='rgba(201,169,110,0.45)'});
    el.addEventListener('mouseleave',()=>{ring.style.transform='translate(-50%,-50%) scale(1)';ring.style.borderColor='rgba(255,255,255,0.25)'});
  });
}

// Enter key
document.getElementById('taskInput').addEventListener('keydown', e => {
  if(e.key === 'Enter') addTask();
});

render();
</script>
</body>
</html>
