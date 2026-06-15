import random
import time
import os

pemain = {"kamu": 1, "bot": 1}
ular_tangga = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78,
               1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def gambar_papan():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== ULAR TANGGA TERMINAL ===")
    for i in range(100, 0, -10):
        baris = ""
        rentang = range(i, i-10, -1) if (i//10) % 2 == 1 else range(i-9, i+1)
        for j in rentang:
            if pemain["kamu"] == j and pemain["bot"] == j:
                baris += "[KB] "
            elif pemain["kamu"] == j:
                baris += "[K ] "
            elif pemain["bot"] == j:
                baris += "[B ] "
            else:
                baris += f"[{j:2}] "
        print(baris)
    print("\nK = Kamu, B = Bot")

while True:
    gambar_papan()
    input("\nEnter buat lempar dadu kamu...")
    dadu = random.randint(1, 6)
    print(f"Kamu dapat: {dadu}")
    pemain["kamu"] += dadu
    if pemain["kamu"] in ular_tangga:
        tujuan = ular_tangga[pemain["kamu"]]
        print("Ketemu " + ("ular! Turun" if tujuan < pemain["kamu"] else "tangga! Naik"))
        pemain["kamu"] = tujuan
    if pemain["kamu"] > 100:
        pemain["kamu"] = 100
    time.sleep(1)

    if pemain["kamu"] == 100:
        gambar_papan()
        print("Kamu menang! 🎉")
        break

    time.sleep(1)
    dadu_bot = random.randint(1, 6)
    print(f"Bot lempar: {dadu_bot}")
    pemain["bot"] += dadu_bot
    if pemain["bot"] in ular_tangga:
        pemain["bot"] = ular_tangga[pemain["bot"]]
    if pemain["bot"] == 100:
        gambar_papan()
        print("Bot menang! Coba lagi ya")
        break
    time.sleep(1.5)

  # Game Ular Tangga Terminal 🎲
Game ular tangga 2 pemain vs bot. Jalan di Acode/Termux tanpa install apa-apa.

## Cara Main di Acode
1. Buat file baru `ular_tangga.py`
2. Paste kode di atas
3. Run → Enter buat lempar dadu
4. Tujuan: capai kotak 100 duluan

Petak 1,4,9,21,28,36,51,71,80 = tangga naik  
Petak 16,47,49,56,62,64,87,93,95,98 = ular turun