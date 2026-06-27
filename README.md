# optical-trap-stiffness-vs-height
Gráfica experimental de la rigidez (kx, ky) de una trampa óptica en función de la altura de la partícula, con datos en pN/µm y escala logarítmica.
# Optical trap stiffness vs. height – Experimental plot

Representación gráfica de las constantes de rigidez \(k_x\) y \(k_y\) de una trampa óptica medidas experimentalmente a diferentes alturas de la partícula sobre el cubreobjetos. Los datos originales en N/m se convierten a pN/µm y se muestran en escala logarítmica para facilitar la comparación.

---

## 📘 Contexto físico

En una trampa óptica, una partícula dieléctrica es atrapada cerca del foco de un láser fuertemente enfocado. La fuerza de restauración es aproximadamente armónica para pequeños desplazamientos, y se caracteriza por las constantes de rigidez \(k_x\) y \(k_y\) (en el plano transversal a la dirección de propagación). Estas constantes dependen de la potencia del láser, la geometría del haz y, crucialmente, de la distancia entre la partícula y la interfase vidrio‑agua (la altura).

Conocer \(k\) en función de la altura es esencial para:
- Calibrar la trampa.
- Corregir efectos de aberración esférica.
- Realizar experimentos de fuerza con precisión.

Este repositorio contiene un script mínimo que lee un conjunto concreto de datos experimentales y genera la curva **\(k\) vs altura** con las unidades prácticas **pN/µm**.

---

## 🧪 Datos experimentales incluidos

Los datos están directamente escritos en el script y provienen de un experimento de calibración. Se muestran en la tabla siguiente:

| Altura (µm) | \(k_x\) (N/m) | \(k_y\) (N/m) |
|-------------|---------------|---------------|
| 4.002       | 6.76×10⁻¹¹    | 9.04×10⁻⁹     |
| 5.0025      | 3.27×10⁻¹¹    | 8.15×10⁻¹⁰    |
| 6.003       | 2.73×10⁻¹¹    | 1.92×10⁻⁹     |
| 7.0035      | 9.45×10⁻¹¹    | 2.07×10⁻⁹     |
| 8.004       | 3.23×10⁻⁷     | 7.40×10⁻⁷     |

*Atención*: Se observa un salto considerable en los valores a la altura de 8.004 µm. Esto puede deberse a una recalibración, un cambio de potencia del láser o una condición experimental distinta. El script lo representa tal cual.

Los valores se almacenan en dos arreglos (`kx_Npm`, `ky_Npm`) y luego se convierten a pN/µm con el factor \(1\,\text{N/m} = 10^6\,\text{pN/µm}\).

---

## 📊 Descripción del gráfico

- **Eje X**: altura (µm).
- **Eje Y**: constante de rigidez \(k\) en **pN/µm**, escala logarítmica.
- **Curva kx**: línea continua con marcadores circulares (`o-`), etiquetada como `kx (PSD)`.
- **Curva ky**: línea discontinua con marcadores cuadrados (`s--`), etiquetada como `ky (PSD)`.
- Se añade una rejilla fina (lineas punteadas) tanto para los ejes lineales como logarítmicos.
- El título del gráfico es “Constante de la trampa óptica vs altura”.

La escala logarítmica permite visualizar simultáneamente valores que difieren en varios órdenes de magnitud, como los puntos a 8 µm (≈10⁻¹ pN/µm) y los de alturas menores (≈10⁻⁵ – 10⁻⁴ pN/µm).

---

## 🚀 Uso

1. Asegúrate de tener instaladas las dependencias:
   ```bash
   pip install numpy matplotlib
