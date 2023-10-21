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
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/6d65bb66-31da-4bdf-b6b6-8b945b607d95"  width="400" height="200"> </p>
  <em><p align="center">Comparación de tipos de filtros en el dominio de tiempo y frecuencia [1]</p></em> 

**Filtros IIR**
<p align="justify"> El filtro digital IIR es un filtro importante. Puede lograr una selectividad de frecuencia precisa con un orden inferior. Por lo general, para diseñar un filtro digital IIR es necesario diseñar primero el filtro analógico y luego transformarlo en un filtro digital. Este método tiene desventajas como el costo de la banda de transición amplia, por lo que el rendimiento del filtro no es lo suficientemente ideal. Algunos académicos también han aplicado algoritmos de enjambre de partículas al diseño de filtros IIR, pero estos algoritmos pueden tener deficiencias de convergencia óptima o lenta local [2] </p>

<p align="center">
  <img src="https://ineurocienciaslima.com.pe/img/electroencefalografia.jpg"  width="400" height="200"> </p>
<em><p align="center">Respuesta en frecuencia de los filtros IIR [3]</p></em> 

**Wavelet**

<p align="justify"> La técnica más común y exitosa para eliminar ruido de señales con señales no estacionarias, como el electroencefalograma (EEG) y el electrocardiograma (ECG), es la transformada wavelet (WT). El éxito de WT depende de la configuración óptima de sus parámetros de control, que a menudo se establecen experimentalmente [4]. Es difícil detectar diferencias sutiles y vitales en las señales del electroencefalograma (EEG) simplemente mediante inspección visual. Se ha descubierto que el rendimiento de las bases wavelet es eficaz para analizar el comportamiento transitorio y abrupto de las señales de EEG [8]. Los resultados preliminares de varios proyectos muestran que las wavelet se pueden utilizar como herramientas de detección automática de artefactos y potenciales relacionados con eventos y en aplicaciones que requieren procesamiento en tiempo real de señales EEG. El mayor beneficio de la transformada wavelet es que se localiza tanto en tiempo como en frecuencia. La transformada wavelet se utiliza para convertir la señal EEG en una serie de wavelet que son una versión desplazada y escalada de la wavelet madre. Por lo tanto, Wavelet puede ser adecuado con eventos ocultos que pueden ayudar a detectar la frecuencia exacta y la ubicación del evento en una escala de tiempo.


<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/6d65bb66-31da-4bdf-b6b6-8b945b607d95"  width="400" height="200"> </p>
  <em><p align="center">Transformada de Wavelet [5]></em> 


## **Objetivos** <a name="obj"></a>
---
- Diseñar 1 filtro IIR (elegir entre  Bessel, Butterworth, Chebyshev o Eliptico)
- Diseñar 1 filtro FIR, elegir 2 métodos de ventana pueden ser: Hanning, Hamming,Bartlett, rectangular o Blackman
- Diseñar un filtro Wavelet

## **Resultados** <a name="resul"></a>
---
### **Señal EEG** <a name="conex"></a>

<p align="justify">Para obtener las señales se usó la conexión en la placa BiTalino con un sensor de EEG de 3 electrodos. En la configuración bipolar, se utilizan dos electrodos de medición (IN+/-) que se colocan sobre la posición del electrodo. El electrodo negro se coloca en la región derecha de la frente, mientras que el electrodo rojo se coloca en la región izquierda de la frente. El electrodo de referencia (blanco) se coloca en una región neutral, el hueso detrás de la oreja [8]. 

<p align="justify">En este informe se mantiene la identidad anónima y datos personales de las personas involucradas en los experimentos siguiendo así la Ley N.° 29733:Ley de Protección de Datos Personales, la presente Ley tiene el objeto de garantizar el derecho fundamental a la protección de los datos personales, previsto en el artículo 2 numeral 6 de la Constitución Política del Perú, a través de su adecuado tratamiento, en un marco de respeto de los demás derechos fundamentales que en ella se reconocen [10].
     
<div align="center">
     
| | | |
|:-------------:|:-------------:|:-------------:|
|<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/conexion_usada.jpg?raw=true" width="400" height="300"></p> |<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/conexion_carlos.png?raw=true" width="400" height="300"></p>| <p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/colocacion_ultracortex.jpg?raw=true" width="400" height="300"></p>|
</div>

<p align="justify">
Se procedió a tomar señales de un miembro del equipo siguiendo el protocolo de BITalino ®evolution Lab Guide, experimental guides to meet & learn your biosignals.

### **Explicación del protocolo seguido** <a name="senal"></a>

| **Pasos** | **Bitalino** | 
|:-------------:|:-------------:|
|<p align="justify"> **1. Conectar el BITalino (r)evolution Core BT** </p> <p align="justify">**2. Prueba de la configuración** </p> <p align="justify">**3. Conectar el sensor de EEG de 3 electrodos al participante:** Como se menciona en la guía. Además, se procuró que el participante no cuente con objetos metálicos ni electrónicos cerca, para evitar el ruido producido por estos; y, de igual manera, se procuró que el participante se mantenga sentado en una silla en un estado de reposo y calma. Posterior a esto se inició la grabación de la toma de datos. | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/conexion_usada.jpg?raw=true" width="50%" height="50%"> | 
|<p align="justify">**4. Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal).** Para esto se le solicitó al participante que se mantenga en calma por 10 segundos para establecer la línea base, la cual será el punto de partida para la toma de datos. <p align="justify">**5.Sin movimientos oculares/ojos cerrados durante 30 segundos.** Una vez pasados los 10 segundos, se le solicitó al paciente que cierre los ojos durante 30 segundos mientras se mantenía en una posición de calma</p> | <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/b49b3a1a-012c-4920-a10f-29f06f2c0569" width="50%" height="50%"></video>| 
|<p align="justify">**6. Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces** Culminados los 30 segundos, se le solicitó al participante realizar un ciclo de abrir y cerrar los ojos con un intervalo de tiempo de 5 seg, y repetir este ciclo 5 veces, mientras mantenía la misma posición y miraba un punto fijo.<p align="justify"> **7. Registre otra fase de referencia de 30 segundos (paso 5)** Finalizadas las 5 repeticiones de apertura y cierre de ojos, se le solicitó al paciente volver a cerrar los ojos por 30 segundos mientras se mantenía en un estado de calma.| <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/7d3688bc-70c6-4dd7-a6d3-b16b7c402c21" width="50%" height="50%"></video> | 
|<p align="justify"> **6. Leer en voz alta una serie de ejercicios matemáticos** Finalizados los 30 segundos, otro participante leyó en voz alta una serie de ejercicios matemáticos (*), los cuales fueron resolvidos por el participante mientras fijaba su mirada en un punto específico; no se asignó un tiempo límite para cada pregunta. <p align="justify">**7. Detener la grabación y guardar los datos.**|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/cb2f8bb4-ba15-4911-b9cd-6b597a817790" width="50%" height="50%"></video> | 

**(*)Preguntas utilizadas [11]**
| Categoría           | Ejemplo                                                                                                                                                       |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ejemplo Sencillo    | - Hay 3 pájaros en un árbol; Llegan 7 más. ¿Cuántas aves hay ahora?                                                                                           |
|                     | - Jonas tiene 5 manzanas y Mary tiene 4. ¿Cuántas manzanas tienen en total?                                                                                   |
|                     | - Hanna tiene 9 dólares pero gastó 4. ¿Cuántos dólares le quedan?                                                                                              |
| Ejemplo Complejo    | - John anotó 45 puntos para su equipo; 10 más que José. Marie anotó 13 puntos más que John y Joseph juntos. ¿Cuántos puntos obtuvieron en total?              |
|                     | - El Grupo A tiene 24 estudiantes; 13 menos que el grupo B. El grupo C tiene 12 estudiantes más que los grupos A y B combinados. ¿Cuál es el número total de estudiantes? |
|                     | - Una tienda vendía 21 refrescos por la mañana y 13 más que por la tarde. Por la noche vendió 10 más que por la mañana y por la tarde juntas. ¿Cuántos refrescos se vendieron en total?               |

### Ploteo de la señal en OpenBCI GUI <a name="plot"></a>
Para evitar interferencias es importante no tener objetos metálicos como aretes, anillos, cadenas, etc.

**Observación** No se completó la toma de datos durante la ronda de preguntas matemáticas, pues por las disposiciones de tiempo no se puedo llegar a realizar.</p> 

<div align="center">

| **Etapa** | **OpenBCI GUI** | 
|:-------------:|:-------------:|
| Inicial (30 segundos)| <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/se%C3%B1al_ultracortex.jpg?raw=true" width="50%" height="50%"> | 
| Abrir y cerrar ojos |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/uc_30secon.png?raw=true" width="50%" height="50%">| 
---

<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/1d2203f7-a0ef-4a80-94b1-e483379ad579" width="50%" height="50%"></video> 
<em><p align="center"> Visualización de la señal EEG </p></em> 
</div>


### Discusión
**Apertura y cierre de ojos**

En adultos despiertos, el EEG revela principalmente la presencia de ondas alfa y beta, como se muestra en la Imagen 11 del paper [13].

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/imagen1.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Imagen 11: Detección de ondas alfa a partir de una señal EEG registrada [13]</p></em> 

La Imagen 12 muestra las diferencias entre un participante con los ojos abiertos (parte superior) y un participante con los ojos cerrados (parte inferior) [14].

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/imagen3.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Imagen 12. Gráfica superior, participante con ojos abiertos. Gráfica inferior, participante con ojos cerrados. [14]</p></em> 

**Complejidad de problemas matemáticos**

En problemas matemáticos de alta complejidad, se registra una mayor actividad en las bandas de frecuencia theta y alfa en las áreas frontales y parietales izquierdas, que están vinculadas al razonamiento matemático y el cálculo. Estos resultados respaldan investigaciones previas que indican una mayor activación de estas áreas cerebrales en situaciones de mayor dificultad. Además, se ha notado una disminución en la actividad de las regiones temporales durante la resolución de estos problemas[15].

La siguiente imagen ilustra la interacción entre las áreas cerebrales encargadas de almacenar y manipular la información visual, destacando las oscilaciones en las bandas de frecuencia theta y alfa2[15].

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/imagen4.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Interacción entre áreas cerebrales [15]
</p></em> 

En otro estudio, tanto las concentraciones de hemoglobina oxigenada (HbO) como las señales de EEG mostraron un aumento durante la tarea mental, pero el inicio, el período y la cantidad de ese aumento depende de las características de cada modalidad [16].

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/imagen5.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Comparación de señales [16]
</p></em> 

### **Archivos** <a name="arch"></a>

- [Documentos.txt](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/972ce8758b55bbeff94d1fea3cc9e4206d2c9f3b/ISB/Laboratorios/Laboratorio%2005%20-%20Registro%20de%20EEG/Documentaci%C3%B3n/Archivos%20.txt)
- [Código para plotear señales en Python](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/972ce8758b55bbeff94d1fea3cc9e4206d2c9f3b/ISB/Laboratorios/Laboratorio%2005%20-%20Registro%20de%20EEG/Documentaci%C3%B3n/C%C3%B3digos)

### **Ploteo de la señal en Python** <a name="plote"></a>

**SEÑAL OBTENIDA CON EL BITALINO**
<div align="center">

| **Etapa** | **Señal Bitalino** |  
|:-------------:|:-------------:|
| **Reposo (30 segundos)**| <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg1.png?raw=true"  width="50%" height="50%"> <p align="justify">| 
| **Abrir y cerrar ojos** |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg2.png?raw=true"  width="50%" height="50%"><p align="justify"> | 
| **Reposo** |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg3.png?raw=true"  width="50%" height="50%"><p align="justify"> | 
| **Preguntas matemáticas** |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg4.png?raw=true"  width="50%" height="50%" ><p align="justify"> | 
</div>

**SEÑAL OBTENIDA CON EL ULTRACORTEX**

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg1_uc.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Ploteo de la señal obtenida</p></em> 

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg_fft_psd_uc.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">PSD para FFT de la señal</p></em> 




## **Conclusiones** <a name="conclu"></a>
---
- Se pudo observar variaciones en las mediciones de las gráficas de ojos cerrados y abiertos, Se observa el aumento de amplitud sobre los 10 Hz y la aparición de las ondas alfa en los electrodos occipitales O1 y O2. Sin embargo, el ruido generado puede deberse a la mala posición de los electrodos.
- El cerebro realiza mayor esfuerzo cuando el sujeto se encuentra bajo presión procesando las preguntas matemáticas.
- Se pudieron comparar entre las señales del ultracortex y el bitalino, que el primero posee una mejor muestra de las señales ya que no adquiere tanto ruido a diferencia del bitalino, esto se puede deber al nivel de filtrado que posee cada uno y la calidad de sus componentes.
- La presencia de artefactos cerca del sujeto y que este esté conectado eléctricamente a otros dispositivos pueden generar altas impedancias en los electrodos de EEG y alterar los rangos normales.



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