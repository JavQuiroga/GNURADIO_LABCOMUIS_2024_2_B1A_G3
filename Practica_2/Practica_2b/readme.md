## Descripción General
En esta actividad se trabajó con señales de diversas formas, como cuadradas, triangulares, seno y coseno, generadas mediante GNU Radio. A estas señales se les aplicó un nivel controlado de ruido y se realizaron análisis detallados para medir su potencia de ruido, potencia de armónicos y relación señal a ruido pico (PSNR). Para este propósito, las señales fueron analizadas utilizando un analizador de espectro.

### Actividades Realizadas
  #### 1. Generación de Señales
  Se diseñaron y generaron las siguientes señales con GNU Radio:

  - Señal cuadrada.
  - Señal triangular.
  - Señal senoidal.
  - Señal cosenoidal.
  
  A cada una de estas señales se les añadió un nivel de ruido, controlando su amplitud y tipo (por ejemplo, ruido blanco).

  #### 2. Análisis de Espectro
  Se utilizaron herramientas como el analizador de espectro para:

  - Identificar la distribución de la potencia en el dominio de la frecuencia.
  - Medir la potencia de los armónicos presentes en cada tipo de señal.
  - Determinar la potencia de ruido añadida a las señales.
    
  #### 3. Cálculo de PSNR
  Se calculó la relación señal a ruido pico (PSNR) de las señales analizadas. Este indicador permitió evaluar:

  - La calidad de las señales afectadas por ruido.
  - El impacto del ruido en diferentes formas de onda.
    
  #### 4. Comparación de Resultados
  Se compararon los resultados de las mediciones entre los distintos tipos de señales, observando:

  - Cómo la forma de la señal influye en la distribución de potencia en el espectro.
  - La relación entre la potencia de los armónicos y el nivel de ruido añadido.
  - Variaciones en el PSNR según el tipo de señal.

### Resultados Observados
Potencia de Ruido: La potencia de ruido aumentó de manera proporcional al nivel de ruido añadido, afectando especialmente las señales con componentes armónicos significativos.
Potencia de Armónicos: Las señales cuadradas y triangulares presentaron mayores niveles de armónicos, mientras que las señales senoidales y cosenoidales mostraron espectros más limpios.
PSNR: El PSNR fue más alto en señales senoidales y cosenoidales, indicando una mayor resistencia al ruido en comparación con señales cuadradas y triangulares.

### Conclusión
El laboratorio permitió analizar cómo el ruido afecta la calidad y las propiedades espectrales de diferentes tipos de señales. La combinación de generación de señales con GNU Radio y su análisis en un analizador de espectro ofreció una visión práctica de los efectos del ruido en sistemas de comunicación.
