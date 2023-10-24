# Laboratorio 6: Procesamiento de EMG 

1. [Introducción](#intro)
2. [Metodología](#met)
3. [Resultados](#resul)
6. [Conclusiones](#conclu)
7. [Referencias](#ref)


## **Introducción** <a name="intro"></a>
---
**Extracción de características de un EMG**
<p align="justify">La señal de electromiografía (EMG) es una indicación eléctrica de la actuación neuromuscular relacionada con un músculo en contracción. Es un signo extremadamente complicado que está influenciado por las propiedades anatómicas y fisiológicas de los músculos, el sistema de control del sistema sensorial marginal y también las características de la instrumentación que se utiliza para identificarlo y observarlo. La mayoría de las conexiones entre la señal EMG y las propiedades de un músculo en contracción que se utilizará rápidamente se han desarrollado de forma fortuita. La ausencia de una representación adecuada de la señal EMG es probablemente la variable más notable que ha obstaculizado el desarrollo de la EMG hasta convertirla en un campo específico [1].

<p align="justify">En general el proceso se rige por las etapas de adquisición de datos, procesamiento de señal, extracción y clasificación de características de señal y funciones de predicción. Cada una de las etapas varía dependiendo los parámetros de diseño, como costo de elaboración y porcentaje de asertividad [2]

## **Metodología EMG** <a name="met"></a>
--- 
1. **Adquisición** 
<p align="justify"> La adquisición de señales biomédicas es una herramienta fundamental en la evaluación de pacientes con patologías, e incluso, en la evaluación del rendimiento deportivo. En el mismo contexto, el uso de la electromiografía de superficie (EMGs) ha permitido fortalecer los esquemas de tratamiento convencionales, pesquisando posibles modificaciones musculoesqueléticas vinculadas al tiempo de activación, coactivación, patrones de activación, entre otros [3].
En la adquisición de las señales de sEMG es posible distinguir las siguientes etapas: pre-amplificación, filtrado y la etapa de conversión de analógico a digital [4].

<p align="center">
  <img src="Img\tabla.png"  width="400" height="200"> </p>
  <em><p align="center">Tabla 1: Características de sEMG y EMG invasiva [4]</p></em> 

2. **Filtrado**
<p align="justify">La señal proveniente de la etapa de pre-amplificación contiene una mezcla de señales biológicas y ruido del ambiente, es por esta razón que se requiere depurar o filtrar la información.  Para descartar interferencias originadas por fuentes electromagnéticas de 50Hz, generalmente se utiliza un filtro Butterworth de orden 2 con frecuencia de bloqueo entre 49 y 51 Hz [5]. Adicionalmente, la señal debe ser filtrada con un paso de banda de 20 a 400 Hz para eliminar los artefactos producidos por los movimientos del electrodo y la piel del paciente [6]. Los parámetros que utilizaremos son los siguientes:

- Filtro paso alto con frecuencia de corte entre 10 – 20 Hz.
- Filtro paso bajo con frecuencia de corte entre 400 – 450 Hz.


3. **Rectificación**
<p align="justify">La técnica más común de detección de la amplitud de EMG es la rectificación seguida de una etapa de suavizado. Consiste en obtener el valor absoluto de la señal cruda. La rectificación puede ser de dos tipos: de media onda, donde se excluyen los valores negativos y únicamente se consideran los valores positivos; o de onda completa, en la que se obtiene el valor absoluto de todos los valores, incluyendo los negativos [5]. 

<p align="center">
  <img src="Img\rectificación3.png"  width="400" height="200"> </p>
  <em><p align="center">Figura 1: Rectificación y filtrado de una señal EMG en el dominio de la frecuencia [7]</p></em> 

4. **Suavización**
<p align="justify">Este procedimiento es útil cuando se requiere realizar estudios de amplitud. El suavizado elimina o reduce significativamente los picos indeseados y extrae la tendencia de la señal. Uno de los métodos más utilizados es el Root mean-squared (RMS), el cual es la raíz cuadrada de la potencia promedio de una señal EMG en un intervalo de tiempo específico. Se denomina "variable en el dominio del tiempo" porque muestra cómo cambia la amplitud de la señal a lo largo del tiempo. El tamaño del segmento suele situarse entre 50-100 ms dependiendo del tipo de movimiento [5].

5. **Extracción de características**
<p align="justify">La extracción de características consiste en obtener información relevante de la  señal de sEMG mediante una transformación de los datos originales, de esta transformación se obtiene el vector de características o Feature Vector (FV). Existen tres tipos de características para la señal de EMG: las características en el dominio del tiempo, en el dominio de la frecuencia y en el dominio de tiempo frecuencia [4].
Esta característica de la señal puede brindarnos información de la actividad muscular, el nivel de fatiga muscular, detección de patrones anormales, así como una evaluación de coordinación muscular [8].

- **Dominio del tiempo**
<p align="justify">Para ello se pueden usar diversas funciones como IEMG, MAV, RMS, VAR y ZC. Ante esto, se eligió la técnica  RMS por su reducción de la variabilidad, respuesta ponderada alta y sencillez, en comparación con los otros métodos.

- **Dominio de la frecuencia**
<p align="justify">Para esta característica se suele usar las funciones MNF, MDF y PSD. Estas ayudan a identificar patrones específicos e identificar la activación y coordinación de diversas tareas y obtener información sobre la modulación de la fuerza y velocidad de contracción muscular.

- **Dominio de tiempo frecuencia**
<p align="justify">Las herramientas de análisis en tiempo-frecuencia son capaces de darnos la información temporal de la cual se carece en el análisis espectral. Además, permite una mejor lectura e interpretación de las contracciones musculares.


<p align="center">
  <img src="Img\procedimiento.png"  width="400" height="200"> </p>
  <em><p align="center">Fig. 2: Sistema de control mioeléctrico basados en reconocimiento de patrones</p></em> 

## **Resultados y Discusiones** <a name="met"></a>
--- 
<p align="justify">Para obtener los resultados, primero se utilizó un filtro Notch de 60Hz para eliminar el ruido, luego se pasó la señal por un filtro pasabanda de 20 a 400 Hz, así mismo, se adjuntan las imágenes de los espectros de cada paso de la señal. Luego, se hace una detección de eventos y una comparación con la señal filtrada.

1. **Filtrado**

|Señal Cruda | Espectro de frecuencia|
|-------------|-------------|
| <img src="Img\ssin_filtrar.jpg"  width="300" height="300">  | <img src="Img\fft_cruda.jpg"  width="300" height="300">  |

- **Filtro Notch**

|Señal filtrada  | Espectro de frecuencia | Espectro de frecuencia |
|-------------|-------------|-------------|
| <img src="Img\senal_filtrada.jpg"  width="300" height="300">   |<img src="Img\filtro_notch.jpg"  width="300" height="300"> |<img src="Img\filtro_notch_2.jpg"  width="300" height="300"> |

- **Filtro pasabanda**

|Señal filtrada  | Espectro de frecuencia |
|-------------|-------------|
| <img src="Img\sfiltrada_pasab.jpg"  width="300" height="300">  |<img src="Img\fft_pasabanda.jpg"  width="300" height="300">  |

2. **Extracción de características**

- **Detección de eventos - Contracciones musculares**
<img src="Img\emg_deteccion_eventos.png"  width="300" height="300"> 

- **Detección de señales de activación**
<img src="Img\emg_deteccion_señal_activación.png"  width="300" height="300"> 

- **RMS**
<img src="Img\emg_RMS.png"  width="300" height="300"> 

- **Valores obtenidos**
    - Maximum EMG (mV): 1.274705
    - Minimum EMG (mV): -1.02152
    - Average EMG (mV): -1.58645
    - Standard Deviation EMG : 0.085814
    - RMS EMG: 0.0003960

<p align="justify">Tomando en cuenta que se usó la señal de contracción, tenemos la gráfica de RMS que nos muestra la relación a la fuerza aplicada bajo condiciones de no fatiga, entonces sabemos que en un evento de contracción puede haber fatiga muscular. Un aumento del RMS en la señal suele estar relacionado con una mayor actividad muscular, como la que ocurre durante una contracción muscular más intensa, también, generalmente indica una mayor amplitud de la actividad muscular.


## **Referencias** <a name="ref"></a>
---
[1] Bita Mokhlesabadifarahani and Vinit Kumar Gunjan, “Introduction to EMG Technique and Feature Extraction,” SpringerBriefs in applied sciences and technology, pp. 1–9, Jan. 2015, doi: https://doi.org/10.1007/978-981-287-320-0_1. Available: https://link.springer.com/chapter/10.1007/978-981-287-320-0_1. [Accessed: Oct. 24, 2023]
‌

[2] L. Sanabria and O. Avilez, “Extracción de características y métodos de clasificación para reconocimiento de movimientos de mano a partir de señales de EMG y EEG: Revisión.” Available: https://repository.udistrital.edu.co/bitstream/handle/11349/25505/SanabriaHernandezLauraViviana2020.pdf?sequence=1&isAllowed=y


[3] O. Valencia, C. De La Fuente, R. Guzmán-Venegas, R. Salas, and A. Weinstein, “Propuesta de Flujo de Procesamiento utilizando Python para ajustar la Señal Electromiográfica Funcional a la Contracción Voluntaria Máxima,” vol. 40, no. 3, pp. 171–175, 2021, Available: https://repositoriobibliotecas.uv.cl/bitstream/handle/uvscl/7565/Valencia_Pro2021.pdf?sequence=1&isAllowed=y. [Accessed: Oct. 24, 2023]

‌[4] “Item 1009/743 | Repositorio INAOE,” Repositorioinstitucional.mx, 2023, doi: http://inaoe.repositorioinstitucional.mx/jspui/handle/1009/743. Available: https://inaoe.repositorioinstitucional.mx/jspui/handle/1009/743. [Accessed: Oct. 24, 2023]


[5]A. Moreno Sanz, “Procesado Avanzado de señal EMG,” thesis, Universidad Carlos III de Madrid, Escuela politécnica superior, Madrid, 2017 


‌[6] C. Alva Coras, “Procesamiento de señales de electromiografía superficial para la detección de movimiento de dos dedos de la mano,” thesis, Universidad Ricardo Palma, Peru, 2012


[7] J. Avila Lapo and F. Fajardo Taday, “Análisis entre señales electromiográficas en los mússculos cervicales y el ángulo de inclinación de la cabeza en niños con PCI entre 5 y 10 años aplicada a terapia cervical,” thesis, Universidad Politécnica Salesiana Sede Cuenca, Cuenca, 2019 


[8] Nizam Uddin Ahamed, Tasriva Sikandar, Mohammad Fazle Rabbi, and Kamarul Hawari Ghazali, “Time and frequency domain features of EMG signal during Islamic prayer (Salat),” Mar. 2017, doi: https://doi.org/10.1109/cspa.2017.8064939. Available: https://ieeexplore.ieee.org/abstract/document/8064939. [Accessed: Oct. 24, 2023]
‌
