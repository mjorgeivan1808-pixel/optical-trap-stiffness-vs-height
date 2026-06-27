# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:49:45 2026

@author: mjorg
"""

import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales (altura en µm)
altura = np.array([4.002, 5.0025, 6.003, 7.0035, 8.004])  # micras

# Constantes originales en N/m
kx_Npm = np.array([6.76e-11, 3.27e-11, 2.73e-11, 9.45e-11, 3.23e-07])
ky_Npm = np.array([9.04e-09, 8.15e-10, 1.92e-09, 2.07e-09, 7.40e-07])

# Conversión a pN/µm (1 N/m = 1e6 pN/µm)
kx = kx_Npm * 1e6
ky = ky_Npm * 1e6

# Crear figura
plt.figure(figsize=(8,6))

# Graficar
plt.plot(altura, kx, 'o-', label='kx (PSD)')
plt.plot(altura, ky, 's--', label='ky (PSD)')

# Escala logarítmica en eje y
plt.yscale('log')

# Etiquetas (ahora en pN/µm)
plt.xlabel('Altura (µm)')
plt.ylabel('k (pN/µm)')
plt.title('Constante de la trampa óptica vs altura')

# Leyenda y grid
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()