<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Weather — Uday Anand</title>
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
body{background:var(--black);color:var(--white);font-family:var(--sans);min-height:100vh;display:flex;flex-direction:column;overflow-x:hidden}

/* GRID LINES */
.grid{position:fixed;inset:0;pointer-events:none;z-index:0;opacity:.03}
.grid::before{content:'';position:absolute;top:0;left:25%;width:1px;height:100%;background:var(--white)}
.grid::after{content:'';position:absolute;top:0;right:25%;width:1px;height:100%;background:var(--white)}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:100;padding:1.8rem 4rem;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid transparent;transition:border-color .3s}
nav.scrolled{border-color:var(--border);background:rgba(5,5,5,0.92);backdrop-filter:blur(12px)}
.nav-logo{font-family:var(--serif);font-size:1rem;font-weight:300;letter-spacing:.25em;color:var(--white);text-transform:uppercase;text-decoration:none}
.nav-tag{font-family:var(--mono);font-size:.6rem;letter-spacing:.2em;color:var(--gold);text-transform:uppercase}

/* MAIN */
main{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:8rem 2rem 4rem;position:relative;z-index:1}

/* HEADER */
.page-tag{font-family:var(--mono);font-size:.65rem;letter-spacing:.4em;color:var(--gold);text-transform:uppercase;margin-bottom:1.5rem;opacity:0;animation:fadeUp .6s ease .2s forwards}
.page-title{font-family:var(--serif);font-size:clamp(3.5rem,8vw,6.5rem);font-weight:300;line-height:.92;letter-spacing:-.02em;text-align:center;margin-bottom:1rem;opacity:0;animation:fadeUp .8s ease .4s forwards}
.page-title em{font-style:italic;color:var(--gold)}
.page-sub{font-size:.78rem;color:rgba(255,255,255,.35);font-weight:300;letter-spacing:.05em;margin-bottom:4rem;text-align:center;opacity:0;animation:fadeUp .6s ease .6s forwards}

/* SEARCH BOX */
.search-wrap{width:100%;max-width:560px;margin-bottom:3rem;opacity:0;animation:fadeUp .6s ease .8s forwards}
.search-inner{display:flex;border:1px solid #2a2a2a;background:#0a0a0a;transition:border-color .3s}
.search-inner:focus-within{border-color:var(--gold)}
.search-input{flex:1;background:transparent;border:none;outline:none;padding:1.2rem 1.6rem;font-family:var(--mono);font-size:.82rem;color:var(--white);letter-spacing:.05em}
.search-input::placeholder{color:rgba(255,255,255,.2)}
.search-btn{background:transparent;border:none;border-left:1px solid #2a2a2a;padding:1.2rem 1.8rem;cursor:pointer;color:var(--gold);font-family:var(--mono);font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;transition:background .3s,color .3s;white-space:nowrap}
.search-btn:hover{background:var(--gold);color:var(--black)}
.search-btn:disabled{opacity:.4;cursor:not-allowed}

/* RESULT CARD */
.result{width:100%;max-width:560px;opacity:0;transform:translateY(20px);transition:opacity .6s ease,transform .6s ease}
.result.show{opacity:1;transform:translateY(0)}

.city-label{font-family:var(--mono);font-size:.6rem;letter-spacing:.3em;text-transform:uppercase;color:var(--muted);margin-bottom:.6rem}
.city-name{font-family:var(--serif);font-size:clamp(2.2rem,5vw,3.5rem);font-weight:300;line-height:1;margin-bottom:2.5rem;color:var(--white)}
.city-name span{font-style:italic;color:var(--gold)}

.temp-block{border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:2.5rem 0;display:flex;align-items:flex-end;gap:1rem;margin-bottom:2.5rem}
.temp-num{font-family:var(--serif);font-size:clamp(5rem,14vw,9rem);font-weight:300;line-height:1;color:var(--white)}
.temp-unit{font-family:var(--serif);font-size:2.5rem;font-weight:300;color:var(--gold);margin-bottom:.8rem}
.temp-feels{margin-left:auto;text-align:right}
.feels-label{font-family:var(--mono);font-size:.58rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:.4rem}
.feels-val{font-family:var(--serif);font-size:2rem;font-weight:300;color:rgba(255,255,255,.5)}

.meta-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--border)}
.meta-item{background:var(--black);padding:1.4rem 1.2rem}
.meta-label{font-family:var(--mono);font-size:.55rem;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);margin-bottom:.5rem}
.meta-val{font-size:.9rem;color:var(--white);font-weight:300}
.meta-val strong{font-family:var(--serif);font-size:1.4rem;font-weight:300;color:var(--white)}

.condition-row{margin-top:2.5rem;display:flex;align-items:center;justify-content:space-between}
.condition-text{font-family:var(--serif);font-size:1.5rem;font-weight:300;font-style:italic;color:rgba(255,255,255,.5)}
.condition-icon{font-size:2rem}

/* ERROR */
.error-msg{font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;color:#e07070;padding:1rem 1.4rem;border:1px solid rgba(224,112,112,.2);background:rgba(224,112,112,.04);display:none}
.error-msg.show{display:block}

/* LOADING */
.loading{display:none;flex-direction:column;align-items:center;gap:1rem;padding:3rem 0}
.loading.show{display:flex}
.load-bar{width:120px;height:1px;background:var(--border);position:relative;overflow:hidden}
.load-bar::after{content:'';position:absolute;top:0;left:-40%;width:40%;height:100%;background:var(--gold);animation:loading 1.2s ease-in-out infinite}
.load-text{font-family:var(--mono);font-size:.6rem;letter-spacing:.25em;text-transform:uppercase;color:var(--muted)}
@keyframes loading{0%{left:-40%}100%{left:100%}}

/* FOOTER */
footer{padding:2rem 4rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;position:relative;z-index:1}
footer p{font-family:var(--mono);font-size:.58rem;color:var(--muted);letter-spacing:.08em}
footer a{color:var(--gold);text-decoration:none}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

@media(max-width:600px){
  nav{padding:1.4rem 1.6rem}
  main{padding:7rem 1.4rem 3rem}
  .meta-grid{grid-template-columns:1fr 1fr}
  .meta-item:last-child{grid-column:span 2}
  footer{flex-direction:column;gap:.6rem;text-align:center;padding:1.5rem}
}
</style>
</head>
<body>
<div class="grid"></div>

<nav id="nav">
  <a class="nav-logo" href="#">Uday Anand</a>
  <span class="nav-tag">Weather App</span>
</nav>

<main>
  <p class="page-tag">Live Weather Data</p>
  <h1 class="page-title">Check the<br><em>Weather.</em></h1>
  <p class="page-sub">Real-time temperature & conditions via wttr.in API</p>

  <div class="search-wrap">
    <div class="search-inner">
      <input class="search-input" id="cityInput" type="text" placeholder="Enter city name..." autocomplete="off" spellcheck="false"/>
      <button class="search-btn" id="searchBtn" onclick="fetchWeather()">Search</button>
    </div>
  </div>

  <div class="error-msg" id="errorMsg">City not found — check spelling and try again.</div>

  <div class="loading" id="loading">
    <div class="load-bar"></div>
    <p class="load-text">Fetching data</p>
  </div>

  <div class="result" id="result">
    <div class="city-label">Location</div>
    <div class="city-name" id="cityDisplay">—</div>

    <div class="temp-block">
      <div class="temp-num" id="tempC">—</div>
      <div class="temp-unit">°C</div>
      <div class="temp-feels">
        <div class="feels-label">Feels like</div>
        <div class="feels-val" id="feelsLike">—°</div>
      </div>
    </div>

    <div class="meta-grid">
      <div class="meta-item">
        <div class="meta-label">Humidity</div>
        <div class="meta-val"><strong id="humidity">—</strong>%</div>
      </div>
      <div class="meta-item">
        <div class="meta-label">Wind</div>
        <div class="meta-val"><strong id="wind">—</strong> km/h</div>
      </div>
      <div class="meta-item">
        <div class="meta-label">Visibility</div>
        <div class="meta-val"><strong id="visibility">—</strong> km</div>
      </div>
    </div>

    <div class="condition-row">
      <div class="condition-text" id="conditionText">—</div>
      <div class="condition-icon" id="conditionIcon"></div>
    </div>
  </div>
</main>

<footer>
  <p>Built by <a href="https://code-withuday.github.io/portfolio">Uday Anand</a> · Python Developer</p>
  <p>Data via wttr.in API</p>
</footer>

<script>
// Nav scroll
window.addEventListener('scroll',()=>{
  document.getElementById('nav').classList.toggle('scrolled',window.scrollY>20)
});

// Enter key
document.getElementById('cityInput').addEventListener('keydown',e=>{
  if(e.key==='Enter') fetchWeather()
});

function weatherCodeDesc(code){
  if(code===0) return {text:'Clear Sky',icon:'☀️'};
  if(code<=2) return {text:'Partly Cloudy',icon:'⛅'};
  if(code===3) return {text:'Overcast',icon:'☁️'};
  if(code<=49) return {text:'Foggy',icon:'🌫️'};
  if(code<=59) return {text:'Drizzle',icon:'🌦️'};
  if(code<=69) return {text:'Rainy',icon:'🌧️'};
  if(code<=79) return {text:'Snowy',icon:'❄️'};
  if(code<=82) return {text:'Rain Showers',icon:'🌧️'};
  if(code<=86) return {text:'Snow Showers',icon:'🌨️'};
  if(code<=99) return {text:'Thunderstorm',icon:'⛈️'};
  return {text:'Unknown',icon:'🌡️'};
}

async function fetchWeather(){
  const city = document.getElementById('cityInput').value.trim();
  if(!city) return;

  const btn = document.getElementById('searchBtn');
  const loading = document.getElementById('loading');
  const result = document.getElementById('result');
  const errorMsg = document.getElementById('errorMsg');

  // Reset
  result.classList.remove('show');
  errorMsg.classList.remove('show');
  loading.classList.add('show');
  btn.disabled = true;
  btn.textContent = '...';

  try {
    // Step 1: Geocoding — city name → lat/lon
    const geoRes = await fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(city)}&count=1&language=en&format=json`);
    const geoData = await geoRes.json();
    if(!geoData.results || geoData.results.length === 0) throw new Error('City not found');

    const place = geoData.results[0];
    const { latitude, longitude, name, country } = place;

    // Step 2: Weather — lat/lon → current weather
    const wxRes = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,visibility,weather_code&wind_speed_unit=kmh&timezone=auto`);
    const wxData = await wxRes.json();
    const cur = wxData.current;

    // Weather code → description + icon
    const wDesc = weatherCodeDesc(cur.weather_code);

    document.getElementById('cityDisplay').innerHTML = `${name} <span>${country}</span>`;
    document.getElementById('tempC').textContent = Math.round(cur.temperature_2m);
    document.getElementById('feelsLike').textContent = Math.round(cur.apparent_temperature) + '°';
    document.getElementById('humidity').textContent = cur.relative_humidity_2m;
    document.getElementById('wind').textContent = Math.round(cur.wind_speed_10m);
    document.getElementById('visibility').textContent = cur.visibility ? Math.round(cur.visibility/1000) : '—';
    document.getElementById('conditionText').textContent = wDesc.text;
    document.getElementById('conditionIcon').textContent = wDesc.icon;

    loading.classList.remove('show');
    result.classList.add('show');

  } catch(err) {
    loading.classList.remove('show');
    errorMsg.classList.add('show');
  }

  btn.disabled = false;
  btn.textContent = 'Search';
}
</script>
</body>
</html>
