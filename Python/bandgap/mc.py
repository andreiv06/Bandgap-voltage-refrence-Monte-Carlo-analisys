import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ Încarcă datele Vref exportate din LTspice
# -----------------------------
# Presupunem că fișierul este 'Vref.txt' și prima coloană este nodul
# Dacă fișierul are header, skiprows=1 îl sărim
data = np.loadtxt('Vref.txt', skiprows=1)

# Dacă fișierul are două coloane: index și Vref, luăm coloana 1
Vref = data[:, 1]

# -----------------------------
# 2️⃣ Calculează medie și deviație standard
# -----------------------------
medie = np.mean(Vref)
deviatie = np.std(Vref)

# -----------------------------
# 3️⃣ Plot distribuție
# -----------------------------
plt.figure()
plt.hist(Vref, bins=100, density=True, alpha=0.7, color='blue', label='Distributie Vref')
plt.axvline(medie, color='red', linestyle='dashed', linewidth=2, label=f'Medie = {medie:.3f} V')
plt.axvline(medie + deviatie, color='green', linestyle='dashed', linewidth=1, label=f'+σ = {medie+deviatie:.3f} V')
plt.axvline(medie - deviatie, color='green', linestyle='dashed', linewidth=1, label=f'-σ = {medie-deviatie:.3f} V')
plt.title('Distributia Vref - Monte Carlo')
plt.xlabel('Vref [V]')
plt.ylabel('Densitate')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(np.arange(len(Vref)), Vref, s=4, c='blue', alpha=0.6)
plt.title('Vref pentru fiecare eșantion')
plt.xlabel('Index eșantion')
plt.ylabel('Vref [V]')
plt.grid(True)
plt.tight_layout()
plt.show()

