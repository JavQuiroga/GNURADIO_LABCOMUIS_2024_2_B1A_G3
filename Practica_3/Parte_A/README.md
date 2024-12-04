## Descripción General
En esta actividad se trabajó con la construcción y análisis de un modulador de amplitud (AM) en GNU Radio, enfocándose en medir y evaluar las características de señales moduladas. Se realizaron mediciones en el dominio del tiempo y de la frecuencia para diferentes índices de modulación, y se analizaron sus efectos en las señales generadas.

### Actividades Realizadas
#### Construcción del Modulador AM

 - Se diseñó un modulador AM utilizando GNU Radio y se conectó la salida del USRP al bloque modulador.
 - Se generaron señales moduladas AM y se analizaron tanto en el dominio del tiempo de la señal s(t) (con un osciloscopio) como en el dominio de la frecuencia (con un analizador de espectro).

#### Análisis de Casos de Modulación
Se consideraron tres casos de índices de modulación:

  - Índice de modulación igual a 1 (modulación balanceada).
  - Índice de modulación igual a 1 más 0.1 multiplicado por el último dígito de un código identificador (sobreexcitación).
  - Índice de modulación igual a 1 menos 0.1 multiplicado por el último dígito de un código identificador (subexcitada).

Para cada caso:

  - Se analizaron las características de la señal envolvente compleja mediante el bloque QT GUI Time Sink.
  - Se midieron las amplitudes de la señal en el osciloscopio.
  - Se evaluaron las bandas laterales y la portadora en el espectro para determinar su potencia relativa.
  - Se calculó la profundidad de modulación en forma de porcentaje utilizando los cursores del osciloscopio.

#### Medición y Comparación
  - Se midió la potencia de las señales moduladas, incluyendo la portadora y las bandas laterales, para validar los índices de modulación configurados.
  - Se compararon los resultados experimentales con los valores obtenidos previamente en cálculos teóricos.

### Resultados Observados
  - Dominio del Tiempo: Las señales moduladas presentaron envolventes claras que variaron en amplitud y forma según el índice de modulación configurado.
  - Dominio de la Frecuencia: En todos los casos, se identificaron claramente la portadora y las dos bandas laterales, cuyos niveles de potencia se midieron con precisión.
  - Profundidad de Modulación: Los índices de modulación fueron consistentes con los resultados esperados, confirmados tanto en el dominio del tiempo como en el de la frecuencia.

### Conclusión
La actividad permitió explorar cómo varían las características de las señales moduladas AM en función del índice de modulación. El uso de herramientas como el osciloscopio y el analizador de espectro facilitó la medición y análisis de las señales, reforzando los conceptos teóricos de modulación AM.
