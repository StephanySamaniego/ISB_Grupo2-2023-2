# Laboratorio 4: Procedimiento de registro EEG

1. [Contexto](#context)
2. [Marco teórico](#marco)
3. [Objetivos](#obj)
4. [Materiales y equipos](#mat)
5. [Resultados](#resul)\
     5.1 [Fotos de la conexión usada](#conex)\
     5.2 [Explicación del protocolo seguido](#senal)\
     5.3 [Ploteo de la señal en OpenBCI GUI](#plot)\
     5.4 [Archivos](#arch)\
     5.5 [Ploteo de la señal en Python](#plote)
6. [Conclusiones](#conclu)
7. [Referencias](#ref)

## **Contexto** <a name="context"></a>
---

<p align="justify">La electroencefalografía ha desempeñado un papel fundamental en el estudio de la actividad cerebral. Los orígenes de esta técnica se remontan a la década de 1920, cuando el médico alemán Hans Berger registró señales que mostraban ritmos marcados cuando los sujetos tenían los ojos cerrados, pero que se volvían menos rítmicas y con amplitudes generalmente menores cuando los ojos estaban abiertos[1].</p>

<p align="justify">Diversas enfermedades cerebrales, trastornos cerebrales y lesiones cerebrales pueden ser diagnosticadas mediante el análisis de la información obtenida de las señales del EEG. La aplicación del EEG en el campo de la ciencia proporciona una visión general del estado actual y las perspectivas futuras de la tecnología EEG en los campos de la neurociencia y la neuroingeniería. También, tiene aplicaciones en el diagnóstico y estudio de trastornos cerebrales significativos, como la enfermedad de Parkinson, la epilepsia, la enfermedad de Alzheimer, los tumores cerebrales y los accidentes cerebrovasculares[2].</p>

<p align="center">
  <img src="https://www.centrohelguera.com.ar/wp-content/uploads/2016/07/electro.jpg"  width="300" height="200"> </p>
<em><p align="center">Señales del EEG [3]</p></em> 


## **Marco teórico** <a name="marco"></a>
---
**¿Qué es el EEG?**
<p align="justify"> La actividad eléctrica de las neuronas en el cerebro produce corrientes que llegan a la superficie del cuero cabelludo [4]. El EEG, o electroencefalografía, representa una técnica no invasiva que mide los campos eléctricos del cerebro. Al posicionar electrodos en el cuero cabelludo, se logra el registro de potenciales de voltaje generados por el flujo de corriente circulante en y alrededor de las neuronas.  Cada electrodo  registra la actividad eléctrica a gran escala, midiendo corrientes eléctricas (o potenciales) generadas en el tejido cortical que contiene aproximadamente de 30 millones a 500 millones de neuronas. Las oscilaciones del voltaje cuentan una parte limitada pero importante de la historia del funcionamiento del cerebro. Por ejemplo, estados de sueño profundo, coma o anestesia están en su mayoría asociados con oscilaciones muy lentas del EEG y amplitudes más grandes [5].  </p>

<p align="center">
  <img src="https://ineurocienciaslima.com.pe/img/electroencefalografia.jpg"  width="400" height="200"> </p>
<em><p align="center">Registro electroencefalográfico (EEG) [6]</p></em> 

**Activación neural**

<p align="justify"> Las señales de EEG son generadas por las corrientes iónicas transmembrana en las neuronas piramidales ya que se puede medir desde el exterior. Las células piramidales se encuentran en todas las áreas de la corteza cerebral, como la occipital, temporal, parietal y frontal, y siempre están orientadas perpendicularmente a la superficie cortical, es decir, el cuerpo celular de estas células se dirige hacia el interior del cerebro y sus dendritas apuntan hacia la superficie cortical. En lla siguiente imagen se observa elipsoides negros que simbolizan la conducción de volumen de las corrientes de retorno en el tejido entre el generador (flecha roja) y el electrodo de EEG de grabación (taza que contiene pasta conductora) en el cuero cabelludo [7].


<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/6d65bb66-31da-4bdf-b6b6-8b945b607d95"  width="400" height="200"> </p>
  <em><p align="center">Origen de la señal EEG [7]</p></em> 

**Oscilaciones del EEG**
<p align="justify"> La señal es siempre una mezcla de varias frecuencias base subyacentes que se consideran reflejo de ciertos estados cognitivos, afectivos o de atención. Estas frecuencias varían ligeramente según factores individuales, propiedades de los estímulos y estados internos, y se clasifican en bandas de frecuencia específicas [8]:


| Tipo de Banda        | Frecuencia (Hz) | Descripción                                                                                                     |
|----------------------|------------------|-----------------------------------------------------------------------------------------------------------------|
| Banda delta          | 1-4 Hz           | Estas oscilaciones son las más lentas y tienen una amplitud más alta. Solo están presentes durante el sueño profundo de ondas lentas y juegan un papel en la consolidación de la memoria y el aprendizaje. |
| Banda theta          | 4-8 Hz           | Se asocian con la atención y el procesamiento de la memoria de trabajo. Aumentan con la dificultad de las tareas mentales. |
| Banda alfa           | 8-12 Hz          | Descubierta por Hans Berger, la banda alfa se relaciona con la relajación y la inhibición sensorial. Aumenta cuando la persona está relajada y con los ojos cerrados, pero disminuye cuando está activa y con los ojos abiertos. |
| Banda beta           | 12-25 Hz         | Están asociadas con el pensamiento activo, la concentración y la planificación de movimientos. También se activan al observar los movimientos de otras personas. |
| Banda gamma          | > 25 Hz          | Su papel aún no está claro, pero se sugiere que pueden estar involucradas en la unificación de impresiones sensoriales y la atención. |
<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/oscilacionesss.png?raw=true"400" height="200"> </p>
<em><p align="center"> Ondas del EEG [8]</p></em> 

**Artefactos**
<p align="justify"> Las señales registradas en el cuero cabelludo se originan en fuentes cerebrales, ruido ambiental y ruido del sistema, así como en artefactos biológicos que pueden deberse a movimientos corporales, el ritmo cardíaco, la actividad muscular, los movimientos oculares y el parpadeo. La eliminación de los artefactos con frecuencias superiores a 20 Hz es desafiante ya que el artefacto eléctrico generado se registra junto con el EEG [9].</p>

## **Objetivos** <a name="obj"></a>
---
- Adquirir señales biomédicas de EEG.
- Hacer una correcta configuración de BiTalino y Ultracortex Mark IV.
- Extraer la información de las señales EEG del software OpenBCI GUI y Open Signal


## **Materiales y equipos** <a name="mat"></a>
---
<div align="center">

| **Modelo** | **Descripción** | **Imagen Referencial** |
|:-------------:|:-------------:|:-------------:|
| (R)evolution | <p align="justify">**Kit BITalino:** Plataforma de adquisición de bioseñales viene con diferentes sensores, como EMG ,ECG o EEG. Envía como una placa todo en uno, con todos los bloques electrónicos necesarios para la adquisición de bioseñales preconectados.</p> | <div align="center"> <img src="https://cdn.sparkfun.com//assets/parts/1/1/8/2/8/14022-01a.jpg" width="50%" height="50%"> |
| - | <p align="justify">**Ultracortex Mark IV EEG:** Casco EEG de código abierto, imprimible en 3D, diseñado para trabajar con cualquier placa OpenBCI. El Ultracortex Mark IV, la última versión, puede muestrear hasta 16 canales de EEG desde 35 ubicaciones diferentes según el sistema 10-20.  </p> | <div align="center"> <img src="https://shop.openbci.com/cdn/shop/products/DSC02861.jpg?v=1652731236&width=900" width="50%" height="50%">  |
| - |<p align="justify"> **Cable de 3 derivaciones :** Registra la actividad eléctrica del cerebro desde tres ubicaciones diferentes (frente y punto de referencia) en el cuerpo del paciente. </p>  |<div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/electrodos.jpg?raw=true" width="50%" height="50%"> |
| - |<p align="justify">**Electrodos:** Los electrodos son utilizados para capturar la actividad eléctrica del cerebro al registrar la diferencia de potencial.</p> | <div align="center"> <img src="https://beurer.pe/assets/sources/ELECTRODOS%20X8%201.jpg" width="50%" height="50%">  |
| - |<p align="justify"> **Software OpenSignals:** Software e diseñado para la adquisición, procesamiento y análisis de datos biomédicos, incluyendo señales fisiológicas y de movimiento.</p>  | <div align="center"> <img src="https://cdn.shopify.com/s/files/1/0595/1068/5887/t/6/assets/ezgif5b55a161ca2-1-1-1649945010655.png?v=1649945012" width="50%" height="50%">  |
| - |<p align="justify"> **Software OpenBCI GUI:** Herramienta de software de OpenBCI para visualizar, grabar y transmitir datos desde las placas OpenBCI. Los datos pueden mostrarse en tiempo real, reproducirse, guardarse en la computadora en formato .txt</p>  | <div align="center"> <img src="https://docs.openbci.com/assets/images/GUI-V4-Screenshot-6d16898fb8d30a8f48e2f748ff0c2d51.jpg" width="50%" height="50%">  |
| - | <p align="justify">**Laptop o PC:** Descargar las plataformas mencionadas en una Laptop para observar y procesar las señales.</p> | <div align="center"> <img src="https://www.lenovo.com/medias/lenovo-laptops-thinkbook-16-gen-4-intel-hero.png?context=bWFzdGVyfHJvb3R8MzQ1OTM2fGltYWdlL3BuZ3xoMjEvaGZkLzEzMjU1MTI1OTkxNDU0LnBuZ3xlMGJjMDAyZjIzYzczYmY0YTY3NTlmODcwMDJjZTBhMzg5M2VlMjFlNTNlZWJkZDMyNDA3MTdlNjc3NjhhZWY5" width="50%" height="50%">  |

</div>

## **Resultados** <a name="resul"></a>
---
### **Conexión usada** <a name="conex"></a>

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

En adultos despiertos, el EEG revela principalmente la presencia de ondas alfa y beta, como se muestra en la imagen del paper [13].

![Imagen 11](enlace_a_la_imagen_11)

La Imagen 12 muestra las diferencias entre un participante con los ojos abiertos (parte superior) y un participante con los ojos cerrados (parte inferior) [14].

![Imagen 12](enlace_a_la_imagen_12)

**Complejidad de problemas matemáticos**

En problemas matemáticos de alta complejidad, se registra una mayor actividad en las bandas de frecuencia theta y alfa en las áreas frontales y parietales izquierdas, que están vinculadas al razonamiento matemático y el cálculo. Estos resultados respaldan investigaciones previas que indican una mayor activación de estas áreas cerebrales en situaciones de mayor dificultad. Además, se ha notado una disminución en la actividad de las regiones temporales durante la resolución de estos problemas[15].

La siguiente imagen ilustra la interacción entre las áreas cerebrales encargadas de almacenar y manipular la información visual, destacando las oscilaciones en las bandas de frecuencia theta y alfa2[15].

![Imagen](enlace_a_la_imagen)

En otro estudio, tanto las concentraciones de hemoglobina oxigenada (HbO) como las señales de EEG mostraron un aumento durante la tarea mental, pero el inicio, el período y la cantidad de ese aumento dependieron de las características de cada modalidad [16].


### **Archivos** <a name="arch"></a>

- [Documentos.txt](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/972ce8758b55bbeff94d1fea3cc9e4206d2c9f3b/ISB/Laboratorios/Laboratorio%2005%20-%20Registro%20de%20EEG/Documentaci%C3%B3n/Archivos%20.txt)
- [Código para plotear señales en Python](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/972ce8758b55bbeff94d1fea3cc9e4206d2c9f3b/ISB/Laboratorios/Laboratorio%2005%20-%20Registro%20de%20EEG/Documentaci%C3%B3n/C%C3%B3digos)

### **Ploteo de la señal en Python** <a name="plote"></a>

**SEÑAL OBTENIDA CON EL BITALINO**
<div align="center">

| **Etapa** | **Señal Bitalino** |  
|:-------------:|:-------------:|
| **Reposo (30 segundos)**| <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg1.png?raw=true"  width="50%" height="50%"> <p align="justify">Según la gráfica, se muestra en la imagen del sujeto masculino en reposo un promedio de 2 latidos en los 2 segundos, lo cual tiene sentido según la bibliografía consultada. Además, se tiene un pico máximo del complejo QRS de algo más de 800 en amplitud, y un pico mínimo de aproximadamente 320 de amplitud. Existe una variabilidad de la frecuencia cardíaca de 0.75 segundos (0.85 - 0.10) aproximadamente entre cada latido, lo cual indica que la persona se encuentra en un estado de reposo. El intervalo QT es de aproximadamente 0.18 segundos.| 
| **Abrir y cerrar ojos** |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg2.png?raw=true"  width="50%" height="50%"><p align="justify"> Según la gráfica, se muestra en la imagen del sujeto masculino agitado un total de 4 latidos en los 2 segundos,contando el primer complejo QRS como el número 0. Se puede notar un aumento de la frecuencia cardíaca a comparación del gráfico en reposo. A comparación de la gráfica en reposo, se tiene un pico máximo del complejo QRS de un poco más de 700 en amplitud, y un pico mínimo de aproximadamente 290 de amplitud. Existe una variabilidad de la frecuencia cardíaca de 0.45 segundos (0.70 - 0.25) aproximadamente entre cada latido, lo cual es menor al obtenido en el gráfico de reposo, lo cual indicaría que efectivamente la persona se encuentra en un estado de agitación. El intervalo QT es de aproximadamente 0.15 segundos.| 
| **Reposo** |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg3.png?raw=true"  width="50%" height="50%"><p align="justify"> Según la gráfica, se muestra en la imagen del sujeto masculino agitado un total de 4 latidos en los 2 segundos,contando el primer complejo QRS como el número 0. Se puede notar un aumento de la frecuencia cardíaca a comparación del gráfico en reposo. A comparación de la gráfica en reposo, se tiene un pico máximo del complejo QRS de un poco más de 700 en amplitud, y un pico mínimo de aproximadamente 290 de amplitud. Existe una variabilidad de la frecuencia cardíaca de 0.45 segundos (0.70 - 0.25) aproximadamente entre cada latido, lo cual es menor al obtenido en el gráfico de reposo, lo cual indicaría que efectivamente la persona se encuentra en un estado de agitación. El intervalo QT es de aproximadamente 0.15 segundos.| 
| **Preguntas matemáticas** |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg4.png?raw=true"  width="50%" height="50%" ><p align="justify"> Según la gráfica, se muestra en la imagen del sujeto masculino agitado un total de 4 latidos en los 2 segundos,contando el primer complejo QRS como el número 0. Se puede notar un aumento de la frecuencia cardíaca a comparación del gráfico en reposo. A comparación de la gráfica en reposo, se tiene un pico máximo del complejo QRS de un poco más de 700 en amplitud, y un pico mínimo de aproximadamente 290 de amplitud. Existe una variabilidad de la frecuencia cardíaca de 0.45 segundos (0.70 - 0.25) aproximadamente entre cada latido, lo cual es menor al obtenido en el gráfico de reposo, lo cual indicaría que efectivamente la persona se encuentra en un estado de agitación. El intervalo QT es de aproximadamente 0.15 segundos.| 
</div>

**SEÑAL OBTENIDA CON EL ULTRACORTEX**

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg1_uc.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Ploteo de la señal obtenida</p></em> 

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/eeg_fft_psd_uc.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">PSD para FFT de la señal</p></em> 




## **Conclusiones** <a name="conclu"></a>
---
- El ruido proveniente de la respiración y contracción muscular puede afectar a la adquisición del ECG, por lo tanto, también afectaría a la eficiencia del algoritmo. Adicionar filtros digitales podría servir para reducir el ruido bajo severas condiciones, sin embargo, esto podría no remover por completo el ruido.
- Se lograron encontrar diferencias entre ambos sujetos y compararlos exitosamente.
- La sujeto femenino posee una variabilidad de frecuencia cardíaca menor que el del sujeto masculino, lo cual evidenciaría las diferencias entre ambos en los aspectos de su vida cotidiana.
- Ninguno de ellos posee una gráfica de reposo ni de agitación parecida al de alguna enfermedad cardíaca, por lo que se descarta ello.
- Se logró con éxito plotear las señales en Python y así lograr un análisis de estas.
- Se cumplió con la protección de la identidad de ambos sujetos, ya que es vital en este tipo de pruebas, por lo que se tuvo extremado cuidado en proteger el rostro y datos personales.



## **Referencias** <a name="ref"></a>
---
[1] A. Biasiucci, B. Franceschiello, and M. M. Murray, "Electroencephalography," *Current Biology*, vol. 29, no. 3, pp. R80–R85, Feb. 2019, doi: [10.1016/J.CUB.2018.11.052](https://doi.org/10.1016/J.CUB.2018.11.052).

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
