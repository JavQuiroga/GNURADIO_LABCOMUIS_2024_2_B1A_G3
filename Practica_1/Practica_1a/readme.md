
# Práctica 1a

## Descripción General

En esta primera práctica del laboratorio de comunicaciones, se exploraron la generación y manipulación de señales en GNU Radio. Se trabajó con señales sinusoidales y se aplicó el **Teorema de Muestreo de Nyquist**, ajustando parámetros como amplitud, frecuencia y frecuencia de muestreo.

## Actividades Realizadas

### 1. Generación de Señales Sinusoidales
Se inició generando una señal sinusoidal básica, explorando cómo afectan los parámetros de **amplitud** y **frecuencia** a la forma de onda. 
- La **amplitud** fue variada para observar el impacto en la escala vertical de la señal.
- La **frecuencia** fue ajustada para analizar cómo los ciclos por segundo afectan el periodo de la onda.

Resultados:
- La señal generada mostraba variaciones en la amplitud y frecuencia en tiempo real, permitiendo visualizar estos efectos.

### 2. Visualización del Teorema de Muestreo de Nyquist
En esta sección, se trabajó con la representación del **Teorema de Nyquist**, ajustando la frecuencia de muestreo para demostrar sus principios. 
- Se observaron aliasing y reconstrucción de señales al cambiar la frecuencia de muestreo en relación con la frecuencia de la señal original.

Pasos:
1. Ajustar la **frecuencia de muestreo** para valores mayores al doble de la frecuencia de la señal (cumpliendo Nyquist).
2. Reducir la frecuencia de muestreo por debajo de este límite para visualizar aliasing.
3. Analizar el espectro de la señal en el dominio de la frecuencia.

Resultados:
- En las gráficas se mostró cómo una adecuada frecuencia de muestreo evita la superposición espectral y cómo aliasing distorsiona la señal original.

## Objetivos Alcanzados
- Comprender cómo los parámetros básicos afectan las señales sinusoidales.
- Visualizar el impacto del Teorema de Nyquist en el dominio del tiempo y la frecuencia.
- Experimentar con herramientas de GNU Radio para el análisis de señales.

## Conclusión
La práctica proporcionó una introducción práctica a los conceptos fundamentales del procesamiento de señales, preparando a los estudiantes para abordar problemas más complejos en sesiones futuras.
