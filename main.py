<!DOCTYPE html>
<html lang="ms">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OptiMark AI Pro v3 - Premium</title>
<style>
:root {
    --bg-body: #f4f7f5;
    --bg-card: #ffffff;
    --text-main: #333333;
    --text-muted: #666666;
    --primary: #198754;
    --primary-hover: #146c43;
    --border-color: #dee2e6;
}
[data-theme="dark"] {
    --bg-body: #121212;
    --bg-card: #1e1e1e;
    --text-main: #e0e0e0;
    --text-muted: #a0a0a0;
    --primary: #2ea44f;
    --primary-hover: #2c974b;
    --border-color: #333333;
}
body { font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg-body); margin: 0; color: var(--text-main); transition: all 0.3s ease; }
header { background: var(--primary); color: white; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); position: relative; }
h1, h3 { margin: 5px 0; }
.theme-toggle { position: absolute; top: 20px; right: 20px; background: rgba(255,255,255,0.2); color: white; border: none; padding: 8px 12px; border-radius: 20px; cursor: pointer; font-size: 12px; }
.theme-toggle:hover { background: rgba(255,255,255,0.3); }
.container { padding: 20px; max-width: 1200px; margin: auto; }
.card { background: var(--bg-card); padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,.05); margin-bottom: 15px; transition: background 0.3s; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
.grid-graf { display: grid; grid-template-columns: 2fr 1fr; gap: 15px; }
@media (max-width: 768px) {
    .grid, .grid-graf { grid-template-columns: 1fr; }
    .stats { grid-template-columns: 1fr 1fr !important; }
}
.form-group { display: flex; flex-wrap: wrap; gap: 15px; align-items: center; }
.form-control { display: flex; flex-direction: column; flex: 1; min-width: 180px; }
.form-control label { font-size: 12px; font-weight: bold; margin-bottom: 5px; color: var(--text-muted); text-transform: uppercase; }
input, select, button { padding: 10px; margin: 4px 0; border: 1px solid var(--border-color); border-radius: 6px; font-size: 14px; background: var(--bg-card); color: var(--text-main); }
input:focus, select:focus { border-color: var(--primary); outline: none; }
button { background: var(--primary); color: white; border: none; cursor: pointer; font-weight: bold; transition: background 0.2s, transform 0.1s; }
button:hover { background: var(--primary-hover); }
button:active { transform: scale(0.98); }
button.btn-secondary { background: #6c757d; }
button.btn-secondary:hover { background: #5a6268; }
button.btn-danger { background: #dc3545; }
button.btn-danger:hover { background: #bd2130; }
.jawapan-container { display: grid; grid-template-columns: repeat(auto-fill, minmax(85px, 1fr)); gap: 10px; max-height: 320px; overflow-y: auto; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px; background: rgba(0,0,0,0.02); }
.qrow { display: flex; flex-direction: column; align-items: center; background: var(--bg-card); padding: 8px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); border: 2px solid transparent; transition: all 0.2s; }
.qrow span { font-weight: bold; margin-bottom: 4px; font-size: 12px; color: var(--text-muted); }
.qrow.correct { border-color: #198754; background: rgba(25, 135, 84, 0.1); }
.qrow.wrong { border-color: #dc3545; background: rgba(220, 53, 69, 0.1); }
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 15px; }
.stat { background: var(--bg-card); padding: 15px; border-radius: 8px; text-align: center; border-left: 4px solid var(--primary); box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
.stat b { font-size: 24px; color: var(--primary); }
.search-box { width: 100%; max-width: 300px; margin-bottom: 10px; float: right; }
table { width: 100%; border-collapse: collapse; margin-top: 10px; }
th, td { border: 1px solid var(--border-color); padding: 12px; text-align: center; }
th { background: var(--primary); color: white; font-weight: 600; }
tr:nth-child(even) { background-color: rgba(0,0,0,0.01); }
.actions { display: flex; gap: 10px; margin-top: 10px; flex-wrap: wrap; }
.chart-container { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; min-height: 220px; }
canvas { max-width: 100%; }
.btn-del { background: transparent; color: #dc3545; border: none; cursor: pointer; padding: 2px 8px; font-size: 16px; }
.btn-del:hover { background: rgba(220, 53, 69, 0.1); border-radius: 4px; }
</style>
</head>
<body>

<header>
    <h1>OptiMark AI Pro v3</h1>
    <h3>SK Kampong Tengah</h3>
    <button class="theme-toggle" onclick="toggleTheme()">☀️ / 🌙 Mod Mata</button>
</header>

<div class="container">

    <div class="card">
        <div class="form-group">
            <div class="form-control">
                <label for="nama">Nama Murid</label>
                <input id="nama" placeholder="Contoh: Ahmad Bin Ali">
            </div>
            <div class="form-control">
                <label for="kelas">Kelas</label>
                <input id="kelas" placeholder="Contoh: 5 Gemilang">
            </div>
            <div class="form-control">
                <label for="subjek">Subjek</label>
                <input id="subjek" placeholder="Contoh: Sains">
            </div>
            <div class="form-control">
                <label for="bil">Bil. Soalan</label>
                <select id="bil" onchange="jana()">
                    <option value="10">10</option>
                    <option value="20">20</option>
                    <option value="40">40</option>
                    <option value="50" selected>50</option>
                </select>
            </div>
        </div>
    </div>

    <div class="grid">
        <div class="card">
            <h3>Jawapan Guru (Skema)</h3>
            <div id="guru" class="jawapan-container"></div>
        </div>
        <div class="card">
            <h3>Jawapan Murid</h3>
            <div id="murid" class="jawapan-container"></div>
        </div>
    </div>

    <div class="card">
        <div class="actions">
            <button onclick="semak()">Semak & Simpan</button>
            <button class="btn-secondary" onclick="exportCSV()">Export CSV</button>
            <button class="btn-danger" onclick="padamSemua()" style="margin-left: auto;">Padam Semua Rekod</button>
        </div>
        <h2 id="result" style="color: var(--primary); margin-top: 15px; text-align: center;"></h2>
    </div>

    <div class="grid-graf">
        <div>
            <div class="stats">
                <div class="stat"><b id="jml">0</b><br>Jumlah Murid</div>
                <div class="stat"><b id="tinggi">0%</b><br>Peratus Tertinggi</div>
                <div class="stat"><b id="rendah">0%</b><br>Peratus Terendah</div>
                <div class="stat"><b id="purata">0%</b><br>Purata Peratus</div>
            </div>
        </div>
        <div class="card" style="margin-bottom: 15px; padding: 10px 20px;">
            <h4 style="margin: 0 0 10px 0; text-align: center;">Analisis Graf Gred</h4>
            <div class="chart-container">
                <canvas id="gredChart" width="250" height="150"></canvas>
            </div>
        </div>
    </div>

    <div class="card" style="overflow-x: auto;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <h3>Rekod Murid</h3>
            <input type="text" id="cari" class="search-box" placeholder="🔍 Cari nama/kelas/subjek..." onkeyup="tapisJadual()">
        </div>
        <table id="tbl">
            <thead>
                <tr>
                    <th>Nama</th>
                    <th>Kelas</th>
                    <th>Subjek</th>
                    <th>Markah</th>
                    <th>%</th>
                    <th>Gred</th>
                    <th>Tindakan</th>
                </tr>
            </thead>
            <tbody id="tblBody"></tbody>
        </table>
    </div>

</div>

<script>
let data = JSON.parse(localStorage.getItem("optimark_v3")) || [];

function opt(id) {
    return `<select id="${id}"><option>A</option><option>B</option><option>C</option><option>D</option></select>`;
}

function jana() {
    let n = +document.getElementById('bil').value;
    let guruDiv = document.getElementById('guru');
    let muridDiv = document.getElementById('murid');
    
    guruDiv.innerHTML = '';
    muridDiv.innerHTML = '';
    
    for(let i = 1; i <= n; i++) {
        guruDiv.innerHTML += `<div class='qrow' id='qrow_g${i}'><span>No. ${i}</span>${opt('g'+i)}</div>`;
        muridDiv.innerHTML += `<div class='qrow' id='qrow_m${i}'><span>No. ${i}</span>${opt('m'+i)}</div>`;
    }
}

function grade(p) {
    if(p >= 80) return 'A';
    if(p >= 65) return 'B';
    if(p >= 50) return 'C';
    if(p >= 40) return 'D';
    return 'E';
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const targetTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', targetTheme);
    localStorage.setItem('theme', targetTheme);
}

// Load theme preference
if (localStorage.getItem('theme') === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
}

function semak() {
    let namaInput = document.getElementById('nama');
    let kelasInput = document.getElementById('kelas');
    let subjekInput = document.getElementById('subjek');
    let bilSelect = document.getElementById('bil');
    let resultH2 = document.getElementById('result');

    if(!namaInput.value.trim()){
        alert("Sila masukkan nama murid terlebih dahulu.");
        return;
    }

    let n = +bilSelect.value;
    let m = 0;
    
    for(let i = 1; i <= n; i++) {
        let gVal = document.getElementById('g'+i).value;
        let mVal = document.getElementById('m'+i).value;
        let mRow = document.getElementById('qrow_m'+i);
        
        if(gVal === mVal) {
            m++;
            mRow.className = 'qrow correct';
        } else {
            mRow.className = 'qrow wrong';
        }
    }
    
    let pct = +((m / n) * 100).toFixed(1);
    let g = grade(pct);

    resultH2.innerHTML = `Keputusan: ${m}/${n} Betul | ${pct}% | Gred ${g}`;

    let rec = { id: Date.now(), nama: namaInput.value, kelas: kelasInput.value, subjek: subjekInput.value, markah: `${m}/${n}`, pct, g };
    data.push(rec);
    localStorage.setItem("optimark_v3", JSON.stringify(data));

    paparJadual();
    updateStats();
    lukisGraf();
    
    namaInput.value = '';
}

function updateStats() {
    if(data.length === 0) {
        document.getElementById('jml').innerText = "0";
        document.getElementById('tinggi').innerText = "0%";
        document.getElementById('rendah').innerText = "0%";
        document.getElementById('purata').innerText = "0%";
        return;
    }
    let arrPct = data.map(x => x.pct);
    document.getElementById('jml').innerText = data.length;
    document.getElementById('tinggi').innerText = Math.max(...arrPct) + "%";
    document.getElementById('rendah').innerText = Math.min(...arrPct) + "%";
    document.getElementById('purata').innerText = (arrPct.reduce((a, b) => a + b, 0) / arrPct.length).toFixed(2) + "%";
}

function paparJadual() {
    let tbody = document.getElementById('tblBody');
    tbody.innerHTML = "";
    data.forEach(rec => {
        let r = tbody.insertRow();
        r.insertCell().innerText = rec.nama;
        r.insertCell().innerText = rec.kelas;
        r.insertCell().innerText = rec.subjek;
        r.insertCell().innerText = rec.markah;
        r.insertCell().innerText = rec.pct + "%";
        r.insertCell().innerText = rec.g;
        
        let cellDel = r.insertCell();
        cellDel.innerHTML = `<button class="btn-del" onclick="padamIndividu(${rec.id})" title="Padam Rekod">🗑️</button>`;
    });
}

function tapisJadual() {
    let kanta = document.getElementById('cari').value.toUpperCase();
    let nalar = document.getElementById('tblBody').getElementsByTagName('tr');
    
    for (let i = 0; i < nalar.length; i++) {
        let tdNama = nalar[i].getElementsByTagName('td')[0];
        let tdKelas = nalar[i].getElementsByTagName('td')[1];
        let tdSubjek = nalar[i].getElementsByTagName('td')[2];
        if (tdNama || tdKelas || tdSubjek) {
            let txtNama = tdNama.innerText || tdNama.textContent;
            let txtKelas = tdKelas.innerText || tdKelas.textContent;
            let txtSubjek = tdSubjek.innerText || tdSubjek.textContent;
            if (txtNama.toUpperCase().indexOf(kanta) > -1 || txtKelas.toUpperCase().indexOf(kanta) > -1 || txtSubjek.toUpperCase().indexOf(kanta) > -1) {
                nalar[i].style.display = "";
            } else {
                nalar[i].style.display = "none";
            }
        }
    }
}

function lukisGraf() {
    const canvas = document.getElementById('gredChart');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    let gredCounts = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0 };
    data.forEach(x => { if(gredCounts[x.g] !== undefined) gredCounts[x.g]++; });

    const greds = ['A', 'B', 'C', 'D', 'E'];
    const warnaGred = ['#2ea44f', '#0284c7', '#eab308', '#f97316', '#dc3545'];
    const nilai = greds.map(g => gredCounts[g]);
    const maxNilai = Math.max(...nilai, 1);

    const barWidth = 24;
    const spacing = 16;
    const startX = 30;
    const chartHeight = 110;

    greds.forEach((gred, i) => {
        const h = (nilai[i] / maxNilai) * chartHeight;
        const x = startX + i * (barWidth + spacing);
        const y = canvas.height - h - 25;

        // Draw Rounded Bars
        ctx.fillStyle = warnaGred[i];
        if (h > 0) {
            ctx.beginPath();
            ctx.roundRect(x, y, barWidth, h, [4, 4, 0, 0]);
            ctx.fill();
        }

        // Labels
        ctx.fillStyle = window.getComputedStyle(document.body).getPropertyValue('--text-main');
        ctx.font = 'bold 12px Segoe UI';
        ctx.fillText(gred, x + 6, canvas.height - 8);

        if(nilai[i] > 0) {
            ctx.fillStyle = warnaGred[i];
            ctx.font = 'bold 11px Segoe UI';
            ctx.fillText(nilai[i], x + 7, y - 6);
        }
    });

    ctx.strokeStyle = window.getComputedStyle(document.body).getPropertyValue('--border-color');
    ctx.beginPath();
    ctx.moveTo(15, canvas.height - 23);
    ctx.lineTo(canvas.width - 15, canvas.height - 23);
    ctx.stroke();
}

function exportCSV() {
    if(data.length === 0) {
        alert("Tiada data untuk dieksport.");
        return;
    }
    let csv = "\uFEFFNama,Kelas,Subjek,Markah,Peratus,Gred\n";
    data.forEach(x => {
        csv += `"${x.nama}","${x.kelas}","${x.subjek}","${x.markah}","${x.pct}%","${x.g}"\n`;
    });
    let blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    let a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `OptiMark_Laporan_${document.getElementById('kelas').value || 'SKKT'}.csv`;
    a.click();
}

function padamIndividu(id) {
    if(confirm("Padam rekod murid ini?")) {
        data = data.filter(x => x.id !== id);
        localStorage.setItem("optimark_v3", JSON.stringify(data));
        paparJadual();
        updateStats();
        lukisGraf();
    }
}

function padamAllUIRows() {
    let n = +document.getElementById('bil').value;
    for(let i=1; i<=n; i++) {
        let r = document.getElementById('qrow_m'+i);
        if(r) r.className = 'qrow';
    }
}

function padamAllUIRows() {
    let n = +document.getElementById('bil').value;
    for(let i=1; i<=n; i++) {
        let r = document.getElementById('qrow_m'+i);
        if(r) r.className = 'qrow';
    }
}

function padamSemua() {
    if(confirm("Padam semua rekod? Tindakan ini tidak boleh diundurkan.")) {
        data = [];
        localStorage.removeItem("optimark_v3");
        paparJadual();
        updateStats();
        lukisGraf();
        padamAllUIRows();
        document.getElementById('result').innerHTML = "";
    }
}

jana();
paparJadual();
updateStats();
lukisGraf();
</script>
</body>
</html>def on_forever():
    pass
basic.forever(on_forever)
