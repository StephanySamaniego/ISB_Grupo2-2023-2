# Laboratorio 6: Filtros 

1. [Marco teórico](#marco)
2. [Objetivos](#obj)
3. [Resultados](#resul)\
     3.1 [Archivos](#arch)\
     3.2 [Ploteo de la señal en Python](#plote)
6. [Conclusiones](#conclu)
7. [Referencias](#ref)


## **Marco Teórico** <a name="marco"></a>
---
**Filtros Digitales**

<p align="justify">Los filtros tienen como propósito mejorar la relación señal-ruido (SNR), separar componentes de frecuencia y extraer información relevante de señales utilizadas en el procesamiento de señales biomédicas. El diseño de filtros digitales es el proceso de derivar la función de transferencia del filtro H(z) que cumple con las especificaciones dadas. Los filtros selectivos de frecuencia lineales e invariantes en el tiempo se pueden clasificar en dos categorías: filtros de respuesta al impulso infinito (IIR) y filtros de respuesta al impulso finito (FIR), a su vez los filtros pueden ser de varios tipos, como filtros pasa bajos, filtros pasa altos, filtros pasa banda y filtros rechaza banda [1].

**Filtros FIR**

<p align="justify"> Dado su sencillo diseño, los filtros FIR de fase lineal encuentran una amplia variedad de aplicaciones en los campos de procesamiento de señales de voz y biomédicas. Esto se debe a su estabilidad asegurada, una distorsión de fase mínima y una baja sensibilidad a los coeficientes. Dependiendo de si el número de coeficientes (N) es par o impar y de si la respuesta al impulso h(n) es simétrica o asimétrica, los filtros FIR de fase lineal pueden clasificarse en cuatro tipos, todos con la característica de tener una fase lineal. Diversos métodos están disponibles para derivar h(n), incluyendo los filtros de fase lineal que emplean el método de la ventana, los que se basan en el muestreo de frecuencia (FSM) y la ampliamente utilizada técnica de filtro FIR óptimo [1].


<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/fir_filtros.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Comparación de tipos de filtros en el dominio de tiempo y frecuencia [1]</p></em> 

**Filtros IIR**
<p align="justify"> El filtro digital IIR es un filtro importante. Puede lograr una selectividad de frecuencia precisa con un orden inferior. Por lo general, para diseñar un filtro digital IIR es necesario diseñar primero el filtro analógico y luego transformarlo en un filtro digital. Este método tiene desventajas como el costo de la banda de transición amplia, por lo que el rendimiento del filtro no es lo suficientemente ideal. Algunos académicos también han aplicado algoritmos de enjambre de partículas al diseño de filtros IIR, pero estos algoritmos pueden tener deficiencias de convergencia óptima o lenta local [2] </p>

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/IIR%20filters.png?raw=true"  width="400" height="200"> </p>
<em><p align="center">Respuesta en frecuencia de los filtros IIR [3]</p></em> 

**Wavelet**

<p align="justify"> La técnica más común y exitosa para eliminar ruido de señales con señales no estacionarias, como el electroencefalograma (EEG) y el electrocardiograma (ECG), es la transformada wavelet (WT). El éxito de WT depende de la configuración óptima de sus parámetros de control, que a menudo se establecen experimentalmente [4]. Es difícil detectar diferencias sutiles y vitales en las señales del electroencefalograma (EEG) simplemente mediante inspección visual. Se ha descubierto que el rendimiento de las bases wavelet es eficaz para analizar el comportamiento transitorio y abrupto de las señales de EEG [8]. Los resultados preliminares de varios proyectos muestran que las wavelet se pueden utilizar como herramientas de detección automática de artefactos y potenciales relacionados con eventos y en aplicaciones que requieren procesamiento en tiempo real de señales EEG. El mayor beneficio de la transformada wavelet es que se localiza tanto en tiempo como en frecuencia [5].


<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/wavelet.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Transformada de Wavelet [5]</em> 


## **Objetivos** <a name="obj"></a>
---
- Diseñar 1 filtro IIR (elegir entre  Bessel, Butterworth, Chebyshev o Eliptico)
- Diseñar 1 filtro FIR, elegir 2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman
- Diseñar un filtro Wavelet

## **Resultados y Discusiones** <a name="resul"></a>
---
### **Señal EEG** <a name="conex"></a>

<p align="justify">El electroencefalograma (EEG) es un método no invasivo para recopilar señales cerebrales del cuero cabelludo humano. Las señales de EEG se encuentran en un rango de frecuencia baja y relativamente pequeñas. La amplitud de estas señales es de aproximadamente 50 μ V y la amplitud máxima es de aproximadamente 100 μ V. Por lo tanto, hay varias fuentes, como la línea eléctrica, el EOG o el ECG, que pueden interferir extremadamente con las señales de EEG. La detección y eliminación de artefactos juega un papel importante para adquirir señales EEG limpias para analizar y detectar actividades cerebrales [5]. El análisis de las señales del electroencefalograma (EEG) es fundamental porque es un método eficaz para diagnosticar trastornos neurológicos cerebrales [6].

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Señal cruda</em> 



     
<div align="center">

|  | Filtro FIR | Filtro IIR | Wavelet |
|--------------|--------------|--------------|--------------|
| Señal filtrada |<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg_fir.png?raw=true" width="400" height=70%></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg_iir.png?raw=true" width="400" height=100%></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg_wv.png?raw=true" width="400" height=80% ></p>|
| Descripción    | <p align="justify">En este análisis se pretende estructurar un filtro FIR avanzado basado en Field Programmable Gate Array (FPGA) para obtener señales biomédicas más rápidas, especialmente señales EEG. A este respecto, se introduce un filtro FIR simple y rentable para hacer que la señal de EEG esté libre de ruido, sea menos costosa, consuma menos energía y sea simple. Requiere menos espacio para la implementación del chip que otros filtros digitales y evita la mezcla de otras señales biomédicas [4] | <p align="justify">Usamos un filtro butterworth un método de filtrado de prototipos analógicos en el que se utilizan los polos y ceros de un prototipo de filtro paso bajo clásico en el dominio continuo (Laplace), obtenga un filtro digital mediante transformación de frecuencia y discretización del filtro [6] | <p align="justify">La transformada wavelet se utiliza para convertir la señal EEG en una serie de wavelet que son una versión desplazada y escalada de la wavelet madre. Por lo tanto, Wavelet puede ser adecuado con eventos ocultos que pueden ayudar a detectar la frecuencia exacta y la ubicación del evento en una escala de tiempo. La transformada Wavelet utiliza diferentes tamaños de ventana para cada rango de frecuencias. Ventana más larga para el rango de frecuencias más bajas y ventana más corta para el rango de frecuencias más altas [2].|
| Parámetros    | <p align="justify">- Ventana: Hanning <p align="justify">- Frecuencia de corte 1: 0.5 Hz <p align="justify">- Frecuencia de corte 2: 50 Hz <p align="justify">- Tipo de filtro: filtro notch <p align="justify">- Orden del filtro: 2<p align="justify">- Frecuencia de muestreo: 1 Hz   | <p align="justify">-	Frecuencia de muestreo: 1000 Hz<p align="justify">-	Frecuencia de corte inferior: 0.5 Hz<p align="justify">-	Frecuencia de corte inferior: 50 Hz<p align="justify">-	Tipo de filtro: Butterworth<p align="justify">-	Orden: 4| <p align="justify">-	Nivel: 8 <p align="justify">-	Familia: Symlet (sym) 3<p align="justify">-	Coeficientes de aproximación: se eliminan de la tabla D1, D8 y A8 (ruidos)|
| Discusiones  | <p align="justify">Al utilizar la ventana Hamming, usamos una ventana específica para la respuesta de frecuencia, lo que afectará la forma en que se ven y se analizan las oscilaciones en la señal EEG, se debería poder identificar las ondas alfa, delta, beta y gamma, pero podemos observar que no se tiene una señal muy buena y tampoco se puede diferenciar bien cuál banda de frecuencia muestra una mayor amplitud en un momento específico. | <p align="justify">En la señal EEG filtrada con Butterworth podemos identificar las amplitudes de las oscilaciones en diferentes bandas de frecuencia, como delta, theta, alpha, beta y gamma. El gráfico nos permite cuantificar la amplitud en microvoltios(uV) o unidades relativas.| <p align="justify">Podemos observar que después de aplicar el filtro Wavelet Sym3 de nivel 8, la señal tiene la semejanza esperada de acuerdo a la referencia del paper estudiado. Además, en la señal filtrada podemos buscar patrones específicos, como los picos de onda, ritmos específicos (como el ritmo alfa o delta) y eventos relacionados con la actividad cerebral.|

</div>

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/tabal_de.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Descomposición y adquisición de señales EEG después de la SWT nivel 8 de la Transformada de Wavelet</em> 

<p align="justify">
Para eliminar los componentes de parpadeo, implementamos Stationary Wavelet Transform (SWT) de 8 niveles de transformada wavelet discreta no diezmada. Se propone utilizar Wavelet Sym3 que tiene una alta correlación con los artefactos de parpadeo para el algoritmo de cancelación de ruido. Los coeficientes de detalle D1, D8 y A8 son componentes de artefactos que luego se eliminan de las señales [2].
Las wavelets de la familia de los symlets se conocen por symN (N es el orden). Estas wavelets son casi simétricas, ortogonales y biortogonales, Daubechies también las sugiere como una modificación de la familia db [9].

### **Señal EMG** <a name="conex"></a>

<p align="justify">Las señales de sEMG se obtienen utilizando electrodos colocados en la piel para capturar las señales eléctricas generadas por la actividad muscular. Estas señales son relativamente débiles, con amplitudes de alrededor de 0.1 a 5.0 mV. Esto significa que se necesita un sistema de medición muy sensible, pero esta sensibilidad puede hacer que las señales sean más susceptibles a interferencias. Aunque la mayor parte de la energía de la señal sEMG se encuentra en un rango de frecuencias de 0 a 1000 Hz, las señales de EMG suelen filtrarse en un rango de 20 a 500 Hz, con atenuación de 40 dB/década, a fin de  eliminar el ruido eléctrico por debajo de 20 Hz y por encima de 500 Hz. La interferencia de la línea de alimentación eléctrica se puede reducir con un filtro notch centrado en 50 o 60 Hz. Se debe tomar en cuenta que cuando se realiza el filtrado es necesario reducir la frecuencia de muestreo de la señal EMG (downsampling) para evitar la distorsión de la señal. 

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/emg.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Señal cruda</em> 

<div align="center">

|  | Filtro FIR | Filtro IIR | Wavelet |
|--------------|--------------|--------------|--------------|
| Señal filtrada |<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/emg_fir.png?raw=true" width="400" height=70%></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/emg_iir.png?raw=true" width="400" height=70%></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/emg_wv.png?raw=true" width="400" height=90%></p>|
| Descripción    |<p align="justify">El diseño de un filtro FIR Hanning implica la multiplicación de la respuesta de un filtro ideal (como un filtro paso bajo) con la función de ventana de Hanning en el dominio del tiempo. Esto se hace para suavizar la transición entre las frecuencias de paso y de paro del filtro, reduciendo así las oscilaciones no deseadas en la respuesta en frecuencia. | <p align="justify">Filtro IIR logra una buena atenuación en la banda de paso y en la banda de parada, también obtiene frecuencias de borde precisas en la banda de paso y banda de parada, y los requisitos computacionales son pequeños, lo que reduce en gran medida los requisitos de costos de hardware. El filtro IIR Butterworth requiere solo 14 pasos para lograr una atenuación máxima de -100 dB a 50 H| <p align="justify">Se realizaron descomposiciones sucesivas similares hasta que el componente de alta frecuencia presentó cambios en el voltaje promedio y/o picos. Para estimar el ruido, los últimos componentes de la descomposición se filtraron para eliminar la mayor parte de las señales musculares de la interferencia de ruido. Para atenuar la interferencia de ruido de 60 Hz fue la WT de Daubechies de cuarto orden.|
| Parámetros    | <p align="justify">- Ventana: Hanning <p align="justify">- Frecuencia de corte 1: 70 Hz <p align="justify">- Frecuencia de corte 2: 108 Hz <p align="justify">- Tipo de filtro: filtro notch <p align="justify">- Orden del filtro: 2<p align="justify">- Frecuencia de muestreo: 2K Hz   | <p align="justify">-	Frecuencia de muestreo: 10000 Hz<p align="justify">-	Frecuencia de trampa: 50 Hz<p align="justify">-	Rango de frecuencia: 20 Hz - 500Hz<p align="justify">-	Tipo de filtro: Butterworth<p align="justify">-	Orden: 2| <p align="justify">-	Nivel: 4 <p align="justify">-	Familia: Daucbechies<p align="justify">-	Coeficientes de aproximación en el árbol de descomposición|
| Discusiones  | <p align="justify">Para el caso de esta señal de EMG, el filtrado atenuó pequeñas frecuencias, por ello aún se conservó el ruido de la señal| <p align="justify">Nuevamente, el filtrado no resultó como se deseaba, ya que los parámetros del filtro que seleccionamos atenuaban demasiado la señal, y se le atribuye el posible error a la Frecuencia de Muestreo utilizado en el bitalino al adquirir la señal.| <p align="justify">Con este filtro se pueden obtener características específicas de la señal EMG, como por ejemplo RMS, la amplitud, la frecuencia, entre otros, y como se puede ver en la imagen de la señal  filtrada hay un contraste significativo con la imagen de la señal no filtrada, ambos se encuentran en las mismas escalas, pero en la señal filtrada se pueden extraer con mayor facilidad las características mencionadas. Además, se pueden identificar las frecuencias dominantes dentro de la señal y cómo varían en el tiempo.|

</div>

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/arbol.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Árbol de descomposición</em> 

<p align="justify">Dado que la frecuenSSScia de muestreo es de 1 KHz, el coeficiente (0,0) contiene componentes de frecuencia que van desde 0 hasta 500 Hz; el coeficiente (1,0) de 0 a 250 Hz, el coeficiente (1,1) de 250 a 500 Hz y así sucesivamente. 

### **Señal ECG** <a name="conex"></a>

<p align="justify">Una señal ECG es una serie temporal cuasiperiódica no lineal y no estacionaria, que representa la función cardiaca, tanto musculares como eléctricas. Es una bioseñal variable en el tiempo que refleja el flujo de corriente iónica, que provoca contracciones y posteriores relajaciones en las fibras cardíacas y proporciona una visión indirecta del flujo sanguíneo al músculo cardíaco. Proporciona información sobre la frecuencia cardíaca, el ritmo cardíaco y la actividad eléctrica. El ECG se registra midiendo la diferencia de potencial entre dos electrodos colocados en la piel del paciente.  [C1] La mayoría de las patologías cardíacas se pueden entender observando la señal del ECG. Las señales de frecuencia cardíaca y ECG se utilizan para evaluar un corazón sano e identificar diversas patologías.[C2] Sin embargo, el ECG es susceptible a diferentes tipos de ruidos, que pueden distorsionar las características morfológicas y los aspectos de intervalo del ECG.
 
 <p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/ecg.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Señal cruda de ECG</em> 

<div align="center">

|  | Filtro FIR | Filtro IIR | Wavelet |
|--------------|--------------|--------------|--------------|
| Señal filtrada |<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/ecg_fir.png?raw=true" width="400" height=70%></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/ecg_iir.png?raw=true" width="400" height=70%></p> | <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/ecg_wv.png?raw=true" width="400" height=70%></p>|
| Descripción    |<p align="justify"> Los filtros FIR (Finite Impulse Response) son caracterizados por no tener una retroalimentación, lo que les permite ser estables y tener fases lineales [3]. Se conocen cinco métodos de diseño de este filtro, mediante ventanas, multibanda con bandas de transición, mínimos cuadrados restringidos, respuesta arbitraria y coseno alzado  [4]. La técnica más fácil es ventanas debido a que estas se basan entre la elección entre funciones de transición ya conocidas, existen múltiples ventanas como rectangular que representa una respuesta ideal y entre las que tienen respuestas al coseno más compleja son la Hanning, Hamming y Blackman  [5]. Hanning es la ventana comúnmente usada para este propósito. Para el diseño del filtro se considera los siguientes parámetros:[6]| <p align="justify">Un filtro IIR (Infinite Impulse Response) es uno que responde a una ecuación recursiva, está ampliamente relacionado a los filtros analógicos por su respuesta infinita [C5,C8]. Dentro de los filtros IIR clásicos se tiene Butterworth, Chebyshev I y II, elíptico y Besel [C6]. El primero está basado en un aproximación en base a las series de Taylor a un filtro ideal [C7]. Se ha evidenciado que Butterworth tiene una mejor respuesta de atenuación frente a Chebyshev [C9].|<p align="justify"> La transformada wavelet descompone la señal ECG en una serie de coeficientes de wavelet en diferentes escalas y ubicaciones temporales. Estos coeficientes se pueden procesar y analizar para identificar patrones característicos en la señal, como picos, ondas y segmentos. Además, la transformada wavelet es capaz de separar el contenido de alta y baja frecuencia de la señal, lo que facilita la eliminación de ruido y la mejora de la detección de eventos cardíacos. |
| Parámetros    | <p align="justify">- Ventana: Hanning <p align="justify">- Frecuencia de corte 1: 0.5 Hz <p align="justify">- Frecuencia de corte 2: 108 Hz <p align="justify">- Tipo de filtro: filtro notch <p align="justify">- Orden del filtro: 56<p align="justify">- Frecuencia de muestreo: 200 Hz   | <p align="justify">-	Frecuencia de muestreo: 500 Hz<p align="justify">-	Frecuencia de corte: 150 Hz<p align="justify">-	Tipo de filtro: Butterworth<p align="justify">-	Orden: 100| <p align="justify">-	Nivel: 7 <p align="justify">-	Familia: Daucbechies9<p align="justify">-	Coeficientes de aproximación: cA7|
| Discusiones  | <p align="justify">Tenemos una señal filtrada buena, en la que se puede reconocer la cantidad de complejos QRS en un tiempo dado, por lo tanto, se podría calcular la frecuencia cardíaca. Además, se puede llegar a medir el intervalo RR y el intervalo QT y obtener valores aproximados. Todos estos datos son importantes para evaluar la función cardíaca.| <p align="justify">Idealmente el filtro nos permitiría identificar  los complejos cardíacos, como las ondas P, el complejo QRS y la onda T para poder evaluar su duración, amplitud y detectar posibles anomalías; sin embargo, no se obtiene una señal tan buena como lo obtenido con el filtro Wavelet, por lo que al menos en este caso no se llega a tener un buen filtrado. | <p align="justify">Gracias al filtrado Wavelet en la señal ECG podemos analizar cómo las frecuencias de la señal se distribuyen en escalas, también gracias a la imagen de la señal filtrada podemos identificar y analizar la amplitud y  la duración del complejo QRS y la onda P, gracias a todo ello se pueden detectar arritmias  cardíacas y la identificación de patrones anómalos en la señal de la persona.|

</div>


## **Conclusiones** <a name="conclu"></a>
---
Tras observar el filtrado en cada respectiva señal (EEG, EMG y ECG), llegamos a la conclusión de que el filtrado Wavelet es el que mejor ha resultado debido a que no realizan una atenuación muy grande a la señal, por ello, se pueden realizar las distintas mediciones y extracciones de características necesarias para el análisis estadístico u otros y poder analizarlos mejor para un diagnóstico más pertinente de la salud del paciente.



## **Referencias** <a name="ref"></a>
---
[1] J. G. Proakis and D. G. Manolakis, "Digital Signal Processing," 4th ed., Prentice Hall, Madrid, 1998.

[2] T. K. Bera, "A Review on the Medical Applications of Electroencephalography (EEG)," *Proceedings of 2021 IEEE 7th International Conference on Bio Signals, Images and Instrumentation, ICBSII 2021*, Mar. 2021, doi: [10.1109/ICBSII51839.2021.9445153](https://doi.org/10.1109/ICBSII51839.2021.9445153).

[3] "Electroencefalograma," *Centro Medico Helguera*, Jul. 18, 2016. Available: [https://www.centrohelguera.com.ar/el-centro-medico-helguera/especialidades/neurologia/electroencefalograma/](https://www.centrohelguera.com.ar/el-centro-medico-helguera/especialidades/neurologia/electroencefalograma/). [Accessed: Oct. 02, 2023]

[4] T. Thompson, T. Steffert, T. Ros, J. Leach, and J. Gruzelier, "EEG applications for sport and performance," *Methods*, vol. 45, no. 4, pp. 279–288, Aug. 2008, doi: [10.1016/J.YMETH.2008.07.006](https://doi.org/10.1016/J.YMETH.2008.07.006).

[5] B. Giesbrecht and J. Garrett, "Electroencephalography," *Reference Module in Neuroscience and Biobehavioral Psychology*, Jan. 2024, doi: [10.1016/B978-0-12-820480-1.00007-3](https://doi.org/10.1016/B978-0-12-820480-1.00007-3).

[6] "Electroencefalografía - Instituto de Neurociencias de Lima," *Instituto Neurociencias de Lima*. Accessed: Sep. 30, 2023. [Online]. Available: [https://ineurocienciaslima.com.pe/electroencefalografia](https://ineurocienciaslima.com.pe/electroencefalografia)

[7] S. Beniczky and D. L. Schomer, "Electroencephalography: basic biophysical and technological aspects important for clinical applications," *Epileptic Disorders*, vol. 22, no. 6, pp. 697–715, Dec. 2020, doi: [10.1684/EPD.2020.1217](https://doi.org/10.1684/EPD.2020.1217).

[8] "BITalino (r)evolution Lab Guide," 2020, Accessed: Sep. 30, 2023. [Online]. Available: [http://BITalino.com/](http://BITalino.com/)

[9] R. Srinivasan and P. L. Nunez, "Electroencephalography," *Encyclopedia of Human Behavior: Second Edition*, pp. 15–23, Jan. 2012, doi: [10.1016/B978-0-12-375000-6.00395-5](https://doi.org/10.1016/B978-0-12-375000-6.00395-5).

[10] "Ley N.° 29733," *Www.gob.pe*, 2023. [https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733](https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733).

[11] J. Molina del Río, M. A. Guevara, M. Hernández González, R. M. Hidalgo Aguirre, and M. A. Cruz Aguilar, "EEG correlation during the solving of simple and complex logical–mathematical problems," *Cognitive, Affective, & Behavioral Neuroscience*, vol. 19, no. 4, pp. 1036–1046, 2019. doi: [10.3758/s13415-019-00703-5](https://doi.org/10.3758/s13415-019-00703-5).

[12] V. Peterson, C. Galván, H. Hernández, and R. Spies, "A feasibility study of a complete low-cost consumer-grade brain-computer interface system," *Heliyon*, vol. 6, p. 3425, 2020, doi: [10.1016/j.heliyon.2020.e03425](https://doi.org/10.1016/j.heliyon.2020.e03425).

[13] T. Uktveris and Vacius Jusas, "Development of a Modular Board for EEG Signal Acquisition," *Sensors*, vol. 18, no. 7, pp. 2140–2140, Jul. 2018, doi: [10.3390/s18072140](https://doi.org/10.3390/s18072140). Available: [https://www.mdpi.com/1424-8220/18/7/2140](https://www.mdpi.com/1424-8220/18/7/2140). [Accessed: Oct. 02, 2023]

[14] R. Álvarez Encinoso, "Montaje, prueba y calibración de sistemas de encefalografía EEG OPEN-BCI," 2020, Accessed: Oct. 01, 2023. [Online]. Available: [https://riull.ull.es/xmlui/handle/915/19811](https://riull.ull.es/xmlui/handle/915/19811)

[15] S. I. Dimitriadis, Y. Sun, N. V. Thakor, and A. Bezerianos, "Causal interactions between Frontalθ – parieto-occipitalα2 predict performance on a mental arithmetic task," *Frontiers in Human Neuroscience*, vol. 10, 2016. doi: [10.3389/fnhum.2016.00454](https://doi.org/10.3389/fnhum.2016.00454)

[16] R. K. Almajidy, K. S. Le, and U. G. Hofmann, "Novel near infrared sensors for hybrid BCI applications," *SPIE Proceedings*, 2015. doi: [10.1117/12.2182066](https://doi.org/10.1117/12.2182066)