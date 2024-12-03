# Práctica de Laboratorio: Análisis de Señales FM

## Parte A: Uso de SDR y GNU Radio

En esta parte, se empleó GNU Radio y un SDR para analizar señales FM (88-108 MHz). Se configuró un flujo de bloques para:

- Capturar señales con USRP.
- Filtrar el ancho de banda y demodular con WBFM.
- Aplicar preénfasis FM para mejorar la calidad de audio.

Se listaron las emisoras disponibles y se identificaron características clave de la señal demodulada, incluyendo servicios adicionales. Además, se verificó el cumplimiento del ancho de banda permitido. Los datos y resultados se documentaron en una tabla Excel disponible en el repositorio.

Se analizaron las emisoras *106.7, 99.2, 98.5, 92.3, 99.7, 95.7, 100.7, 105.1, 93.4 Y 96.2 MHz*

## Parte B: Uso de Analizador de Espectro

Se analizaron las emisoras *99.7, 95.7, 100.7, 105.1 y 93.4 MHz*:

- Se midió el ancho de banda con criterio de -20 dB y nivel de ruido de piso.
- Los anchos oscilaron entre 140 y 200 kHz, mostrando variaciones mínimas y buena calidad de señal.

### Comparación SDR vs. Analizador

- *SDR*: Flexible para análisis y demodulación en tiempo real.
- *Analizador*: Preciso para medir ancho de banda, potencia y ruido.

Ambos enfoques son complementarios: el SDR es ideal para procesamiento digital, mientras que el analizador ofrece mayor exactitud para estudios detallados en frecuencia.
