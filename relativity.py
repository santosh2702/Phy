<!DOCTYPE html>
<html>
<head>
  <title>Pendulum Simulator</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.2/p5.min.js"></script>
  <style>
    body { display: flex; flex-direction: column; align-items: center; font-family: Arial; }
    canvas { border: 1px solid black; }
    .slider-container { margin: 10px; }
  </style>
</head>
<body>
  <h3>Cosmic Pendulum: Hack the Math</h3>
  <div class="slider-container">
    <label>Length (m): <input type="range" id="length" min="0.5" max="2" step="0.1" value="1"></label>
    <span id="length-value">1</span>
  </div>
  <div class="slider-container">
    <label>Angle (deg): <input type="range" id="angle" min="5" max="45" step="1" value="20"></label>
    <span id="angle-value">20</span>
  </div>
  <div class="slider-container">
    <label>Gravity (m/s²): <input type="range" id="gravity" min="5" max="15" step="0.1" value="9.81"></label>
    <span id="gravity-value">9.81</span>
  </div>
  <div class="slider-container">
    <label>Shadow Force (μN): <input type="range" id="shadow" min="0" max="0.001" step="0.0001" value="0"></label>
    <span id="shadow-value">0</span>
  </div>
  <p id="hint">Swinging... but is a cosmic glitch nudging the code?</p>
<script>
let length, angle, gravity, shadowForce;
let theta, omega = 0;

function setup() {
  createCanvas(400, 400);
  lengthSlider = document.getElementById('length');
  angleSlider = document.getElementById('angle');
  gravitySlider = document.getElementById('gravity');
  shadowSlider = document.getElementById('shadow');
  updateValues();
}

function updateValues() {
  length = parseFloat(lengthSlider.value);
  angle = parseFloat(angleSlider.value) * PI / 180;
  gravity = parseFloat(gravitySlider.value);
  shadowForce = parseFloat(shadowSlider.value);
  document.getElementById('length-value').textContent = length;
  document.getElementById('angle-value').textContent = angleSlider.value;
  document.getElementById('gravity-value').textContent = gravity;
  document.getElementById('shadow-value').textContent = shadowForce;
  theta = angle;
  omega = 0;
  if (shadowForce > 0) {
    document.getElementById('hint').textContent = "A shadow force stirs... is reality's math bending?";
  } else {
    document.getElementById('hint').textContent = "Swinging... but is a cosmic glitch nudging the code?";
  }
}

function draw() {
  background(255);
  translate(width / 2, 50);
  let dt = 0.02;
  let alpha = -gravity / length * sin(theta) + shadowForce * cos(theta);
  omega += alpha * dt;
  theta += omega * dt;
  let x = length * 100 * sin(theta);
  let y = length * 100 * cos(theta);
  stroke(0);
  line(0, 0, x, y);
  fill(255, 0, 0);
  ellipse(x, y, 20, 20);
  lengthSlider.oninput = updateValues;
  angleSlider.oninput = updateValues;
  gravitySlider.oninput = updateValues;
  shadowSlider.oninput = updateValues;
}
</script>
</body>
</html>
