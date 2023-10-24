# Laboratorio 6: Procesamiento de EMG 

1. [Introducción](#intro)
2. [Metodología](#met)
3. [Resultados](#resul)\
     3.1 [Señal EEG](#EEG)\
     3.1 [Señal EMG](#EMG)\
     3.1 [Señal ECG](#ECG)\
     3.2 [Archivos](#arch)
6. [Conclusiones](#conclu)
7. [Referencias](#ref)


## **Introducción** <a name="intro"></a>
---
**Extracción de características de un EMG**

<p align="justify">En general el proceso se rige por las etapas de adquisición de datos, procesamiento de señal, extracción y clasificación de características de señal y funciones de predicción. Cada una de las etapas varía dependiendo los parámetros de diseño, como costo de elaboración y porcentaje de asertividad [1].

## **Metodología EMG** <a name="met"></a>
--- 
1. **Adquisición** 
<p align="justify"> Dado su sencillo diseño, los filtros FIR de fase lineal encuentran una amplia variedad de aplicaciones en los campos de procesamiento de señales de voz y biomédicas. Esto se debe a su estabilidad asegurada, una distorsión de fase mínima y una baja sensibilidad a los coeficientes. Dependiendo de si el número de coeficientes (N) es par o impar y de si la respuesta al impulso h(n) es simétrica o asimétrica, los filtros FIR de fase lineal pueden clasificarse en cuatro tipos, todos con la característica de tener una fase lineal. Diversos métodos están disponibles para derivar h(n), incluyendo los filtros de fase lineal que emplean el método de la ventana, los que se basan en el muestreo de frecuencia (FSM) y la ampliamente utilizada técnica de filtro FIR óptimo [2].

<p align="center">
  <img src="Img\tabla.png"  width="400" height="200"> </p>
  <em><p align="center">Tabla 1: Características de sEMG y EMG invasiva [2]</p></em> 

2. **Filtrado**
<p align="justify">La señal proveniente de la etapa de pre-amplificación contiene una mezcla de señales biológicas y ruido del ambiente, es por esta razón que se requiere depurar o filtrar la información.  Para descartae interferencias originadas por fuentes electromagnéticas de 50Hz, generalmente se utiliza un filtro Butterworth de orden 2 con frecuencia de bloqueo entre 49 y 51 Hz. Adicionalmente, la señal debe ser filtrada con un paso de banda de 20 a 400 Hz para eliminar los artefactos de movimiento o frecuencias inusuales.

3. **Rectificación**
<p align="justify">Consiste en obtener el valor ansoluto de la señal cruda. La rectificación puede ser de dos tipos: de media onda, donde se excluyen los valores negativos y únicamente se consideran los valores positivos; o de onda completa, en la que se obtiene el valor absoluto de todos los valores, incluyendo los negativos.

<p align="center">
  <img src="Img\rectificación.png"  width="400" height="200"> </p>
  <em><p align="center">Influencia de la rectificación en la señal en función del nivel de excitación</p></em> 

4. **Suavización**
<p align="justify">Este procedimiento es útil cuando se requiere realizar estudios de amplitud. El suavizado elimina o reduce significativamente los picos indeseados y extrae la tendencia de la señal. Uno de los métodos más utilizados es el Root mean-squared (RMS), el cual es la raíz cuadrada de la potencia promedio de una señal EMG en un intervalo de tiempo específico. Se denomina "variable en el dominio del tiempo" porque muestra cómo cambia la amplitud de la señal a lo largo del tiempo. El tamaño del segmento suele situarse entre 50-100 ms dependiendo del tipo de movimiento.

5. **Extracción de características**
<p align="justify">La extracción de características consiste en obtener información relevante de la  señal de sEMG mediante una transformación de los datos originales, de esta transformación se obtiene el vector de características o Feature Vector (FV). Existen tres tipos de características para la señal de EMG: las características en el dominio del tiempo, en el dominio de la frecuencia y en el dominio de tiempo frecuencia.

<p align="center">
  <img src="Img\procedimiento.png"  width="400" height="200"> </p>
  <em><p align="center">Fig. X: Sistema de control mioeléctrico basados en reconocimiento de patrones</p></em> 

6. **Análisis**
<p align="justify">
**Filtros IIR**
<p align="justify"> El filtro digital IIR es un filtro importante. Puede lograr una selectividad de frecuencia precisa con un orden inferior. Por lo general, para diseñar un filtro digital IIR es necesario diseñar primero el filtro analógico y luego transformarlo en un filtro digital. Este método tiene desventajas como el costo de la banda de transición amplia, por lo que el rendimiento del filtro no es lo suficientemente ideal. Algunos académicos también han aplicado algoritmos de enjambre de partículas al diseño de filtros IIR, pero estos algoritmos pueden tener deficiencias de convergencia óptima o lenta local [3] </p>

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/IIR%20filters.png?raw=true"  width="400" height="200"> </p>
<em><p align="center">Influencia de la rectificación en la señal en función del nivel de excitación.</p></em> 

**Wavelet**

<p align="justify"> La técnica más común y exitosa para eliminar ruido de señales con señales no estacionarias, como el electroencefalograma (EEG) y el electrocardiograma (ECG), es la transformada wavelet (WT). El éxito de WT depende de la configuración óptima de sus parámetros de control, que a menudo se establecen experimentalmente [5]. Es difícil detectar diferencias sutiles y vitales en las señales del electroencefalograma (EEG) simplemente mediante inspección visual. Se ha descubierto que el rendimiento de las bases wavelet es eficaz para analizar el comportamiento transitorio y abrupto de las señales de EEG. Los resultados preliminares de varios proyectos muestran que las wavelet se pueden utilizar como herramientas de detección automática de artefactos y potenciales relacionados con eventos y en aplicaciones que requieren procesamiento en tiempo real de señales EEG. El mayor beneficio de la transformada wavelet es que se localiza tanto en tiempo como en frecuencia [6].


<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/wavelet.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Transformada de Wavelet [7]</em> 


## **Objetivos** <a name="obj"></a>
---
- Diseñar 1 filtro IIR (elegir entre  Bessel, Butterworth, Chebyshev o Eliptico)
- Diseñar 1 filtro FIR, elegir 2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman
- Diseñar un filtro Wavelet

## **Resultados y Discusiones** <a name="resul"></a>
---
### **Señal EEG** <a name="EEG"></a>

<p align="justify">El electroencefalograma (EEG) es un método no invasivo para recopilar señales cerebrales del cuero cabelludo humano. Las señales de EEG se encuentran en un rango de frecuencia baja y relativamente pequeñas. La amplitud de estas señales es de aproximadamente 50 μ V y la amplitud máxima es de aproximadamente 100 μ V. Por lo tanto, hay varias fuentes, como la línea eléctrica, el EOG o el ECG, que pueden interferir extremadamente con las señales de EEG. La detección y eliminación de artefactos juega un papel importante para adquirir señales EEG limpias para analizar y detectar actividades cerebrales [8]. El análisis de las señales del electroencefalograma (EEG) es fundamental porque es un método eficaz para diagnosticar trastornos neurológicos cerebrales [9].

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg.png?raw=true"  width="500" height="250"> </p>
  <em><p align="center">Señal cruda</em> 

     
<div align="center">

|  | Filtro FIR | Filtro IIR | Wavelet |
|--------------|--------------|--------------|--------------|
| Señal filtrada |<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg_fir.png?raw=true" width="400" height="200"></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg_iir.png?raw=true" width="400" height="200"></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg_wv.png?raw=true" width="400" height="200" ></p>|
| Descripción    | <p align="justify">En este análisis se pretende estructurar un filtro FIR avanzado basado en Field Programmable Gate Array (FPGA) para obtener señales biomédicas más rápidas, especialmente señales EEG. A este respecto, se introduce un filtro FIR simple y rentable para hacer que la señal de EEG esté libre de ruido, sea menos costosa, consuma menos energía y sea simple. Requiere menos espacio para la implementación del chip que otros filtros digitales y evita la mezcla de otras señales biomédicas [10] | <p align="justify">Usamos un filtro butterworth un método de filtrado de prototipos analógicos en el que se utilizan los polos y ceros de un prototipo de filtro paso bajo clásico en el dominio continuo (Laplace), obtenga un filtro digital mediante transformación de frecuencia y discretización del filtro [11] | <p align="justify">La transformada wavelet se utiliza para convertir la señal EEG en una serie de wavelet que son una versión desplazada y escalada de la wavelet madre. Por lo tanto, Wavelet puede ser adecuado con eventos ocultos que pueden ayudar a detectar la frecuencia exacta y la ubicación del evento en una escala de tiempo. La transformada Wavelet utiliza diferentes tamaños de ventana para cada rango de frecuencias. Ventana más larga para el rango de frecuencias más bajas y ventana más corta para el rango de frecuencias más altas [8].|
| Parámetros    | <p align="justify">- Ventana: Hanning <p align="justify">- Frecuencia de corte 1: 0.5 Hz <p align="justify">- Frecuencia de corte 2: 50 Hz <p align="justify">- Tipo de filtro: filtro notch <p align="justify">- Orden del filtro: 2<p align="justify">- Frecuencia de muestreo: 1 Hz   | <p align="justify">-	Frecuencia de muestreo: 1000 Hz<p align="justify">-	Frecuencia de corte inferior: 0.5 Hz<p align="justify">-	Frecuencia de corte inferior: 50 Hz<p align="justify">-	Tipo de filtro: Butterworth<p align="justify">-	Orden: 4| <p align="justify">-	Nivel: 8 <p align="justify">-	Familia: Symlet (sym) 3<p align="justify">-	Coeficientes de aproximación: se eliminan de la tabla D1, D8 y A8 (ruidos)|
| Discusiones  | <p align="justify">Al utilizar la ventana Hamming, usamos una ventana específica para la respuesta de frecuencia, lo que afectará la forma en que se ven y se analizan las oscilaciones en la señal EEG, se debería poder identificar las ondas alfa, delta, beta y gamma, pero podemos observar que no se tiene una señal muy buena y tampoco se puede diferenciar bien cuál banda de frecuencia muestra una mayor amplitud en un momento específico. | <p align="justify">En la señal EEG filtrada con Butterworth podemos identificar las amplitudes de las oscilaciones en diferentes bandas de frecuencia, como delta, theta, alpha, beta y gamma. El gráfico nos permite cuantificar la amplitud en microvoltios(uV) o unidades relativas.| <p align="justify">Podemos observar que después de aplicar el filtro Wavelet Sym3 de nivel 8, la señal tiene la semejanza esperada de acuerdo a la referencia del paper estudiado. Además, en la señal filtrada podemos buscar patrones específicos, como los picos de onda, ritmos específicos (como el ritmo alfa o delta) y eventos relacionados con la actividad cerebral.|

</div>

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/tabal_de.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Descomposición y adquisición de señales EEG después de la SWT nivel 8 de la Transformada de Wavelet[8]</em> 

<p align="justify">
Para eliminar los componentes de parpadeo, implementamos Stationary Wavelet Transform (SWT) de 8 niveles de transformada wavelet discreta no diezmada. Se propone utilizar Wavelet Sym3 que tiene una alta correlación con los artefactos de parpadeo para el algoritmo de cancelación de ruido. Los coeficientes de detalle D1, D8 y A8 son componentes de artefactos que luego se eliminan de las señales [8].
Las wavelets de la familia de los symlets se conocen por symN (N es el orden). Estas wavelets son casi simétricas, ortogonales y biortogonales, Daubechies también las sugiere como una modificación de la familia db [12].

### **Señal EMG** <a name="EMG"></a>

<p align="justify">Las señales de sEMG se obtienen utilizando electrodos colocados en la piel para capturar las señales eléctricas generadas por la actividad muscular. Estas señales son relativamente débiles, con amplitudes de alrededor de 0.1 a 5.0 mV. Esto significa que se necesita un sistema de medición muy sensible, pero esta sensibilidad puede hacer que las señales sean más susceptibles a interferencias. Aunque la mayor parte de la energía de la señal sEMG se encuentra en un rango de frecuencias de 0 a 1000 Hz, las señales de EMG suelen filtrarse en un rango de 20 a 500 Hz, con atenuación de 40 dB/década, a fin de  eliminar el ruido eléctrico por debajo de 20 Hz y por encima de 500 Hz. La interferencia de la línea de alimentación eléctrica se puede reducir con un filtro notch centrado en 50 o 60 Hz. Se debe tomar en cuenta que cuando se realiza el filtrado es necesario reducir la frecuencia de muestreo de la señal EMG (downsampling) para evitar la distorsión de la señal [13]. 

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/emg.png?raw=true"  width="500" height="250"> </p>
  <em><p align="center">Señal cruda</em> 

<div align="center">

|  | Filtro FIR | Filtro IIR | Wavelet |
|--------------|--------------|--------------|--------------|
| Señal filtrada |<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/emg_fir.png?raw=true" width="400" height=70%></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/emg_iir.png?raw=true" width="400" height=70%></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/emg_wv.png?raw=true" width="400" height=90%></p>|
| Descripción    |<p align="justify">El diseño de un filtro FIR Hanning implica la multiplicación de la respuesta de un filtro ideal (como un filtro paso bajo) con la función de ventana de Hanning en el dominio del tiempo. Esto se hace para suavizar la transición entre las frecuencias de paso y de paro del filtro, reduciendo así las oscilaciones no deseadas en la respuesta en frecuencia[13]. | <p align="justify">Filtro IIR logra una buena atenuación en la banda de paso y en la banda de parada, también obtiene frecuencias de borde precisas en la banda de paso y banda de parada, y los requisitos computacionales son pequeños, lo que reduce en gran medida los requisitos de costos de hardware. El filtro IIR Butterworth requiere solo 14 pasos para lograr una atenuación máxima de -100 dB a 50 H [14]| <p align="justify">Se realizaron descomposiciones sucesivas similares hasta que el componente de alta frecuencia presentó cambios en el voltaje promedio y/o picos. Para estimar el ruido, los últimos componentes de la descomposición se filtraron para eliminar la mayor parte de las señales musculares de la interferencia de ruido. Para atenuar la interferencia de ruido de 60 Hz fue la WT de Daubechies de cuarto orden [15].|
| Parámetros    | <p align="justify">- Ventana: Hanning <p align="justify">- Frecuencia de corte 1: 70 Hz <p align="justify">- Frecuencia de corte 2: 108 Hz <p align="justify">- Tipo de filtro: filtro notch <p align="justify">- Orden del filtro: 2<p align="justify">- Frecuencia de muestreo: 2K Hz   | <p align="justify">-	Frecuencia de muestreo: 10000 Hz<p align="justify">-	Frecuencia de trampa: 50 Hz<p align="justify">-	Rango de frecuencia: 20 Hz - 500Hz<p align="justify">-	Tipo de filtro: Butterworth<p align="justify">-	Orden: 2| <p align="justify">-	Nivel: 4 <p align="justify">-	Familia: Daucbechies<p align="justify">-	Coeficientes de aproximación en el árbol de descomposición|
| Discusiones  | <p align="justify">Para el caso de esta señal de EMG, el filtrado atenuó pequeñas frecuencias, por ello aún se conservó el ruido de la señal| <p align="justify">Nuevamente, el filtrado no resultó como se deseaba, ya que los parámetros del filtro que seleccionamos atenuaban demasiado la señal, y se le atribuye el posible error a la Frecuencia de Muestreo utilizado en el bitalino al adquirir la señal.| <p align="justify">Con este filtro se pueden obtener características específicas de la señal EMG, como por ejemplo RMS, la amplitud, la frecuencia, entre otros, y como se puede ver en la imagen de la señal  filtrada hay un contraste significativo con la imagen de la señal no filtrada, ambos se encuentran en las mismas escalas, pero en la señal filtrada se pueden extraer con mayor facilidad las características mencionadas. Además, se pueden identificar las frecuencias dominantes dentro de la señal y cómo varían en el tiempo.|

</div>

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/arbol.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Árbol de descomposición</em> 

<p align="justify">Dado que la frecuenSSScia de muestreo es de 1 KHz, el coeficiente (0,0) contiene componentes de frecuencia que van desde 0 hasta 500 Hz; el coeficiente (1,0) de 0 a 250 Hz, el coeficiente (1,1) de 250 a 500 Hz y así sucesivamente[15]. 

### **Señal ECG** <a name="ECG"></a>

<p align="justify">Una señal ECG es una serie temporal cuasiperiódica no lineal y no estacionaria, que representa la función cardiaca, tanto musculares como eléctricas. Es una bioseñal variable en el tiempo que refleja el flujo de corriente iónica, que provoca contracciones y posteriores relajaciones en las fibras cardíacas y proporciona una visión indirecta del flujo sanguíneo al músculo cardíaco. Proporciona información sobre la frecuencia cardíaca, el ritmo cardíaco y la actividad eléctrica. El ECG se registra midiendo la diferencia de potencial entre dos electrodos colocados en la piel del paciente.  [16] La mayoría de las patologías cardíacas se pueden entender observando la señal del ECG. Las señales de frecuencia cardíaca y ECG se utilizan para evaluar un corazón sano e identificar diversas patologías.[17] Sin embargo, el ECG es susceptible a diferentes tipos de ruidos, que pueden distorsionar las características morfológicas y los aspectos de intervalo del ECG.
 
 <p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/ecg.png?raw=true"  width="500" height="250"> </p>
  <em><p align="center">Señal cruda de ECG</em> 

<div align="center">

|  | Filtro FIR | Filtro IIR | Wavelet |
|--------------|--------------|--------------|--------------|
| Señal filtrada |<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/ecg_fir.png?raw=true" width="400" height="200" ></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/ecg_iir.png?raw=true" width="400" height="200"></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/ecg_wv.png?raw=true" width="400" height="200"></p>|
| Descripción    |<p align="justify"> Los filtros FIR (Finite Impulse Response) son caracterizados por no tener una retroalimentación, lo que les permite ser estables y tener fases lineales [18]. Se conocen cinco métodos de diseño de este filtro, mediante ventanas, multibanda con bandas de transición, mínimos cuadrados restringidos, respuesta arbitraria y coseno alzado  [19]. La técnica más fácil es ventanas debido a que estas se basan entre la elección entre funciones de transición ya conocidas, existen múltiples ventanas como rectangular que representa una respuesta ideal y entre las que tienen respuestas al coseno más compleja son la Hanning, Hamming y Blackman  [20]. Hanning es la ventana comúnmente usada para este propósito. Para el diseño del filtro se considera los siguientes parámetros:[21]| <p align="justify">Un filtro IIR (Infinite Impulse Response) es uno que responde a una ecuación recursiva, está ampliamente relacionado a los filtros analógicos por su respuesta infinita [22,23]. Dentro de los filtros IIR clásicos se tiene Butterworth, Chebyshev I y II, elíptico y Besel [24]. El primero está basado en un aproximación en base a las series de Taylor a un filtro ideal [25]. Se ha evidenciado que Butterworth tiene una mejor respuesta de atenuación frente a Chebyshev [26].|<p align="justify"> La transformada wavelet descompone la señal ECG en una serie de coeficientes de wavelet en diferentes escalas y ubicaciones temporales. Estos coeficientes se pueden procesar y analizar para identificar patrones característicos en la señal, como picos, ondas y segmentos. Se propone usar un propone usar la transformada de wavelet Daubechies9 (Db9)para filtrar el ruido relacionado con los artefactos de movimiento.se puede usar un orden entre el 1 y el 10, experimentalmente se obtuvo un orden de nivel 7 como el nivel óptimo de trabajo; y experimentalmente también se halló el coeficiente de aproximación óptimo, el cual es 𝑐𝐴7 [27] |
| Parámetros    | <p align="justify">- Ventana: Hanning <p align="justify">- Frecuencia de corte 1: 0.5 Hz <p align="justify">- Frecuencia de corte 2: 108 Hz <p align="justify">- Tipo de filtro: filtro notch <p align="justify">- Orden del filtro: 56<p align="justify">- Frecuencia de muestreo: 200 Hz   | <p align="justify">-	Frecuencia de muestreo: 500 Hz<p align="justify">-	Frecuencia de corte: 150 Hz<p align="justify">-	Tipo de filtro: Butterworth<p align="justify">-	Orden: 100| <p align="justify">-	Nivel: 7 <p align="justify">-	Familia: Daucbechies9<p align="justify">-	Coeficientes de aproximación: cA7|
| Discusiones  | <p align="justify">Tenemos una señal filtrada buena, en la que se puede reconocer la cantidad de complejos QRS en un tiempo dado, por lo tanto, se podría calcular la frecuencia cardíaca. Además, se puede llegar a medir el intervalo RR y el intervalo QT y obtener valores aproximados. Todos estos datos son importantes para evaluar la función cardíaca.| <p align="justify">Idealmente el filtro nos permitiría identificar  los complejos cardíacos, como las ondas P, el complejo QRS y la onda T para poder evaluar su duración, amplitud y detectar posibles anomalías; sin embargo, no se obtiene una señal tan buena como lo obtenido con el filtro Wavelet, por lo que al menos en este caso no se llega a tener un buen filtrado. | <p align="justify">Gracias al filtrado Wavelet en la señal ECG podemos analizar cómo las frecuencias de la señal se distribuyen en escalas, también gracias a la imagen de la señal filtrada podemos identificar y analizar la amplitud y  la duración del complejo QRS y la onda P, gracias a todo ello se pueden detectar arritmias  cardíacas y la identificación de patrones anómalos en la señal de la persona.|

</div>

### **Archivos** <a name="arch"></a>


- [Código para plotear señales en Python](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/f969f36d273772d218a80eb36dafb51be4d3568c/ISB/Laboratorios/Laboratorio%2006%20-%20Filtros%20digitales/Archivos)


## **Conclusiones** <a name="conclu"></a>
---
Tras observar el filtrado en cada respectiva señal (EEG, EMG y ECG), llegamos a la conclusión de que el filtrado Wavelet es el que mejor ha resultado debido a que no realizan una atenuación muy grande a la señal, por ello, se pueden realizar las distintas mediciones y extracciones de características necesarias para el análisis estadístico u otros y poder analizarlos mejor para un diagnóstico más pertinente de la salud del paciente.



## **Referencias** <a name="ref"></a>
---
[1] J. G. Proakis and D. G. Manolakis, "Digital Signal Processing," 4th ed., Prentice Hall, Madrid, 1998.

[2] Niyan Marchon, “Efficient FIR Filters for Biomedical Signals,” Oct. 2019, doi: https://doi.org/10.1109/tencon.2019.8929397. Available: https://ieeexplore.ieee.org/document/8929397. [Accessed: Oct. 21, 2023]
[3] D. Yue and H. Liu, “The Design Of Intelligent Filter For EEG,” MATEC Web of Conferences, vol. 232, p. 04023, 2018, doi: https://doi.org/10.1051/matecconf/201823204023

[4] C. J. Kikkert, “A Phasor Measurement Unit Algorithm Using IIR Filters for FPGA Implementation,” Electronics, vol. 8, no. 12, pp. 1523–1523, Dec. 2019, doi: https://doi.org/10.3390/electronics8121523. Available: https://www.mdpi.com/2079-9292/8/12/1523. [Accessed: Oct. 21, 2023]

[5] “IEEE Xplore Full-Text PDF”:, Ieee.org, 2023. Available: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8944069. [Accessed: Oct. 21, 2023]


[6] M. Sharma, Abhinav Dhere, Ram Bilas Pachori, and U. Rajendra Acharya, “An automatic detection of focal EEG signals using new class of time–frequency localized orthogonal wavelet filter banks,” Knowledge Based Systems, vol. 118, pp. 217–227, Feb. 2017, doi: https://doi.org/10.1016/j.knosys.2016.11.024. Available: https://www.sciencedirect.com/science/article/abs/pii/S0950705116304816. [Accessed: Oct. 21, 2023]


[7] Novel Applications of Wavelet Transforms based Side-Channel Analysis - Scientific Figure on ResearchGate. Available from: https://www.researchgate.net/figure/Wavelet-transform-illustration_fig1_265359018 [accessed 21 Oct, 2023]

[8] Pham Phuc Ngoc, Vu Duy Hai, Nguyen Chi Bach, and Pham Van Binh, “EEG Signal Analysis and Artifact Removal by Wavelet Transform,” IFMBE proceedings, pp. 179–183, Jan. 2015, doi: https://doi.org/10.1007/978-3-319-11776-8_44. Available: https://link.springer.com/chapter/10.1007/978-3-319-11776-8_44. [Accessed: Oct. 21, 2023]


[9] F. A. Alturki, Khalil AlSharabi, A. M. Abdurraqeeb, and Majid Aljalal, “EEG Signal Analysis for Diagnosing Neurological Disorders Using Discrete Wavelet Transform and Intelligent Techniques,” Sensors, vol. 20, no. 9, pp. 2505–2505, Apr. 2020, doi: https://doi.org/10.3390/s20092505. Available: https://www.mdpi.com/1424-8220/20/9/2505. [Accessed: Oct. 21, 2023]


[10] A. Mahabub, “Design and implementation of cost-effective IIR filter for EEG signal on FPGA,” Australian Journal of Electrical and Electronics Engineering, vol. 17, no. 2, pp. 83–91, Apr. 2020, doi: https://doi.org/10.1080/1448837x.2020.1771662


[11] “VisibleBreadcrumbs,” Mathworks.com, 2023. Available: https://www.mathworks.com/help/signal/ug/iir-filter-design.html. [Accessed: Oct. 21, 2023]

[12] M. Felja, A. Bencheqroune, M. Karim, and G. B. Limas, “Removing Artifacts From EEG Signal Using Wavelet Transform and Conventional Filters,” WSEAS TRANSACTIONS ON INFORMATION SCIENCE AND APPLICATIONS, vol. 17, pp. 177–183, Feb. 2021, doi: https://doi.org/10.37394/23209.2020.17.22

[13] Different types of filters that can be used to shape...,” ResearchGate, 2020. Available: https://www.researchgate.net/figure/A-Different-types-of-filters-that-can-be-used-to-shape-the-EMG-spectrum-to-keep_fig14_344666810. [Accessed: Oct. 21, 2023]

[14]  Z. Xiao, J. Ye, H. Shen, S. Deng, H. Zhu, and X. Han, “Analysis of Digital Filtering Design Based on Surface EMG Signals,” Apr. 2023, doi: https://doi.org/10.1109/iceib57887.2023.10170168. Available: https://ieeexplore.ieee.org/abstract/document/10170168?casa_token=Epyu1ipDXccAAAAA:7rlxsFaoju_vAGk2qw3lHHTWjA4M3CqbL4Zv8GCiZkDgcqpy-HZK7CE1PP_oC7WmdW1RyvUV. [Accessed: Oct. 21, 2023]

[15] Rodrigo Lício Ortolan, R. Mori, R. Pereira, C. Maria, José Carlos Pereira, and A. Cliquet, “Evaluation of adaptive/nonadaptive filtering and wavelet transform techniques for noise reduction in EMG mobile acquisition equipment,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 11, no. 1, pp. 60–69, Mar. 2003, doi: https://doi.org/10.1109/tnsre.2003.810432. Available: https://ieeexplore.ieee.org/abstract/document/1200908?casa_token=EQtC1icvSZ8AAAAA:ALAVecBpqkWB45PHzRZa67EUAgCX_0tw3rL67tK0OeG_8t-3ARPz2vo5UE_2YrksVrg7tC2v. [Accessed: Oct. 21, 2023]

[16]   	S. Chatterjee, R. S. Thakur, R. N. Yadav, L. Gupta, and D. K. Raghuvanshi, “Review of noise removal techniques in ECG signals,” IET Signal Processing, vol. 14, no. 9, pp. 569–590, Dec. 2020, doi: 10.1049/IET-SPR.2020.0104.

[17]   	N. Manjula, N. P. Singh, and P. A. Babu, “An Efficient Designing of IIR Filter for ECG Signal Classification Using MATLAB,” Engineering Proceedings 2023, Vol. 34, Page 24, vol. 34, no. 1, p. 24, Mar. 2023, doi: 10.3390/HMAM2-14154.

[18] 	R. Oshana, “Overview of DSP Algorithms,” DSP for Embedded and Real-Time Systems, pp. 113–131, Jan. 2012, doi: 10.1016/B978-0-12-386535-9.00007-X.

[19] 	“Diseño de filtros FIR - MATLAB & Simulink - MathWorks América Latina.” Accessed: Oct. 19, 2023. [Online]. Available: https://la.mathworks.com/help/signal/ug/fir-filter-design.html

[20] 	S. Gopal, A. P. Gawande, K. B. Khanchandani, and T. P. Marode, “PERFORMANCE ANALYSIS OF FIR DIGITAL FILTER DESIGN TECHNIQUES,” vol. 2, 2012, Accessed: Oct. 19, 2023. [Online]. Available: http://www.ijccr.com

[21]   	I. Jahan and O. Sarker, “A Lower Transition Width FIR Filter & its Noise Removal Performance on an ECG Signal,” Oct. 2017.

[22]   	J. D. Broesch, “Digital Filters,” Digit Signal Process, pp. 101–123, 2009, doi: 10.1016/B978-0-7506-8976-2.00006-7.

[23]   	S. M. Alessio, “IIR Filter Design,” pp. 263–367, 2016, doi: 10.1007/978-3-319-25468-5_8.

[24]   	“Diseño de filtros IIR - MATLAB & Simulink - MathWorks América Latina.” Accessed: Oct. 19, 2023. [Online]. Available: https://la.mathworks.com/help/signal/ug/iir-filter-design.html?s_tid=mwa_osa_a

[25]   	Dr. R. Mehra, “Analysis of Different IIR Filter based on Implementation Cost Performance,” International Journal of Engineering and Advance Technology, vol. 3, pp. 267–270, Oct. 2014.

[26]   	G. Gupta and R. Mehra, “Design Analysis of IIR Filter for Power Line Interference Reduction in ECG Signals,” 2013.

[27]   	U. Seljuq, F. Himayun, and H. Rasheed, “Selection of an optimal mother wavelet basis function for ECG signal denoising,” 17th IEEE International Multi Topic Conference: Collaborative and Sustainable Development of Technologies, IEEE INMIC 2014 - Proceedings, pp. 26–30, 2014, doi: 10.1109/INMIC.2014.7096905.