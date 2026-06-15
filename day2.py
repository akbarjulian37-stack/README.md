<!DOCTYPE html>
<html>
<head>
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #000;
  margin: 0;
}

.container {
  position: relative;
  width: 200px;
  height: 200px;
  animation: ubah 6s ease-in-out infinite;
}

.petal {
  position: absolute;
  width: 40px;
  height: 80px;
  background: pink;
  border-radius: 50% 50% 0 0;
  top: 50%;
  left: 50%;
  transform-origin: 0 0;
  animation: mekar 3s ease-out forwards;
}

/* 8 kelopak melingkar */
.petal:nth-child(1) { transform: rotate(0deg) translateY(-60px); animation-delay: 0s; }
.petal:nth-child(2) { transform: rotate(45deg) translateY(-60px); animation-delay: 0.2s; }
.petal:nth-child(3) { transform: rotate(90deg) translateY(-60px); animation-delay: 0.4s; }
.petal:nth-child(4) { transform: rotate(135deg) translateY(-60px); animation-delay: 0.6s; }
.petal:nth-child(5) { transform: rotate(180deg) translateY(-60px); animation-delay: 0.8s; }
.petal:nth-child(6) { transform: rotate(225deg) translateY(-60px); animation-delay: 1s; }
.petal:nth-child(7) { transform: rotate(270deg) translateY(-60px); animation-delay: 1.2s; }
.petal:nth-child(8) { transform: rotate(315deg) translateY(-60px); animation-delay: 1.4s; }

@keyframes mekar {
 0% { opacity: 0; transform: rotate(var(--r)) translateY(0) scale(0); }
 100% { opacity: 1; transform: rotate(var(--r)) translateY(-60px) scale(1); }
}

/* Pas detik ke 3-6, kelopaknya nyatu jadi love */
@keyframes ubah {
 0%, 45% { filter: hue-rotate(0deg); }
 50% { filter: hue-rotate(180deg) brightness(1.3); }
 51%, 100% { 
    /* Bentuk love pake clip-path */
    clip-path: path('M100 180 C50 140, 0 100, 50 40 C100 0, 150 40, 100 100 C50 40, 0 0, 50 140 Z');
    background: red;
  }
}

.center {
  position: absolute;
  width: 30px;
  height: 30px;
  background: yellow;
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 10;
  animation: hilang 6s forwards;
}

@keyframes hilang {
 0%, 48% { opacity: 1; }
 50%, 100% { opacity: 0; }
}
</style>
</head>
<body>
<div class="container">
  <div class="petal" style="--r: 0deg"></div>
  <div class="petal" style="--r: 45deg"></div>
  <div class="petal" style="--r: 90deg"></div>
  <div class="petal" style="--r: 135deg"></div>
  <div class="petal" style="--r: 180deg"></div>
  <div class="petal" style="--r: 225deg"></div>
  <div class="petal" style="--r: 270deg"></div>
  <div class="petal" style="--r: 315deg"></div>
  <div class="center"></div>
</div>
</body>
</html>