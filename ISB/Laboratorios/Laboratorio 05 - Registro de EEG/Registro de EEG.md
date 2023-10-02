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
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/oscilaciones.png?raw=true"400" height="200"> </p>
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

<p align="justify">Para obtener las señales se usó la conexión en la placa BiTalino con un sensor de EEG de 3 electrodos. En la configuración bipolar, se utilizan dos electrodos de medición (IN+/-) que se colocan sobre la posición del electrodo. El electrodo negro se coloca en la región derecha de la frente, mientras que el electrodo rojo se coloca en la región izquierda de la frente. El electrodo de referencia (blanco) se coloca en una región neutral, el hueso detrás de la oreja [10]. 

<p align="justify">En este informe se mantiene la identidad anónima y datos personales de las personas involucradas en los experimentos siguiendo así la Ley N.° 29733:Ley de Protección de Datos Personales, la presente Ley tiene el objeto de garantizar el derecho fundamental a la protección de los datos personales, previsto en el artículo 2 numeral 6 de la Constitución Política del Perú, a través de su adecuado tratamiento, en un marco de respeto de los demás derechos fundamentales que en ella se reconocen [11].
     
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
|<p align="justify"> 1. Conectar el BITalino (r)evolution Core BT </p> <p align="justify">2. Prueba de la configuración </p> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_05/conexion_usada.jpg?raw=true" width="50%" height="50%"> | 
|<p align="justify">3. Luego de colocar los electrodos en las ubicaciones mencionadas, registrar una línea base de señal con poco ruido y sin movimientos (respiración normal, sin movimientos oculares/ojos cerrados) durante 30 segundos. </p> | <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/b49b3a1a-012c-4920-a10f-29f06f2c0569" width="50%" height="50%"></video>| 
|<p align="justify"> 4. Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambas fases durante cinco segundos. <p align="justify"> 5. Registre otra fase de referencia de 30 segundos (paso 3)| <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/7d3688bc-70c6-4dd7-a6d3-b16b7c402c21" width="50%" height="50%"></video> | 
|<p align="justify"> 6. Leer en voz alta una serie de ejercicios matemáticos (verindicaciones abajo) y el participante deberá resolverlos cada uno de ellos mentalmente enfocando tu mirada en unpunto específico (llavero) para evitar artefactos. <p align="justify"> 7. Detener la grabación y guardar los datos.|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/cb2f8bb4-ba15-4911-b9cd-6b597a817790" width="50%" height="50%"></video> | 

### Ploteo de la señal en OpenBCI GUI <a name="plot"></a>
Para evitar interferencias es importante no tener objetos metálicos como aretes, anillos, cadenas, etc.

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
1. **Frecuencia Cardíaca:**
<p align="justify">
Es la medida del número de contracciones por minuto que ejecuta el corazón para bombear sangre, permitiendo el flujo de esta por el sistema circulatorio. Es una de las variables más estudiadas en el ejercicio, observando su relación con la reducción o el aumento de la frecuencia cardiaca en reposo y en diferentes intensidades del ejercicio. Esta variable puede indicar el grado de adaptación de una persona al entrenamiento, así como su condición física y la monitorización de la intensidad del ejercicio, entre otros. Para evaluar la frecuencia cardiaca existen diferentes factores que la afectan tanto en reposo como durante la actividad física, siendo estas [10]:

- Variaciones diarias: la frecuencia cardiaca presenta variaciones día a día, observando variaciones alrededor de dos o cuatro latidos por minuto al medir la frecuencia en condiciones controladas en una persona, durante días sucesivos.
- Hora del día: la frecuencia presenta variaciones durante el día, siendo menor por la mañana y mayor por la tarde.
Hidratación: cuando una persona está deshidratada presenta una frecuencia cardiaca más alta, el incremento de la frecuencia está relacionado positivamente con el nivel de deshidratación.
- Altitud: la frecuencia cardiaca incrementa cuando se realiza ejercicio en altura.
- Medicación: las variaciones de la frecuencia dependen del tipo de medicamento y la dosis suministrada
- Ejercicio continuo
- Caminatas

</div>

### **Archivos** <a name="arch"></a>

- [Documentos.txt](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2004%20%20-%20BiTalino%20ECG/Documentaci%C3%B3n/Archivos_txt)
- [Código para plotear señales en Python](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2004%20%20-%20BiTalino%20ECG/Documentaci%C3%B3n/C%C3%B3digos)

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


### **Comparación gráfica del sujeto masculino agitado VS el sujeto femenino agitado**

Existe una diferencia notoria entre ambos gráficos.
1. El número de latidos es mayor en el sujeto masculino en la duración de 2 segundos, lo cual podría deberse a su estilo de vida más físico.
2. Los picos máximos y mínimos son muy similares por lo que probablemente experimenten una amplitud semejante en milivoltios.
3. La variabilidad de la frecuencia cardíaca es mayor en el sujeto masculino, lo cual también se debería a la condición física de este.
4. El intervalo QT es más prolongado en el sujeto femenino, lo cual va acorde a la literatura.

### **Imágenes de ECGs con indicios de alguna enfermedad**


<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/enfermedad_1.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Trazo de ECG con 1000 muestras por segundo. Presenta la onda T invertida, indicador de isquemia miocárdica. Extraído de [14]
</p></em> 

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/enfermedad_2.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Trazo de ECG con 1000 muestras por segundo. Se observa una elevación en el segmento ST, indicador de un ataque al corazón. Extraído de [14]
</p></em> 

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/enfermedad_3.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Trazo de ECG con 1000 muestras por segundo donde se observa una
desincronización en el complejo QRS, esto implica una arritmia. Extraído de [14]</p></em> 

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/enfermedad_3.png?raw=true"  width="400" height="200"> </p> 
<em><p align="center">Trazo de ECG con 1000 muestras por segundo y el segmento ST faltante, infarto agudo al miocardio. Extraído de [14]</p></em> 


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
<p align="justify">
[1] World, “Cardiovascular diseases,” Who.int, Jun. 11, 2019. Available: https://www.who.int/health-topics/cardiovascular-diseases#tab=tab_1. [Accessed: Sep. 14, 2023]
‌<p align="justify">
[2] “Al año más de 4 mil personas mueren por infarto en el Perú,” Www.gob.pe, 2023. Available: https://www.gob.pe/institucion/minsa/noticias/34838-al-ano-mas-de-4-mil-personas-mueren-por-infarto-en-el-peru. [Accessed: Sep. 14, 2023]
<p align="justify">
[3] J. Carlos and R. Beatriz, “Nivel de conocimiento y práctica en la toma del electrocardiograma que realizan los profesionales de enfermería de una Clínica Privada de Miraflores, 2017,” Concytec.gob.pe, 2017. Available: https://alicia.concytec.gob.pe/vufind/Record/UEPU_369add237b65a478cd45d4664220d7d0/Details. [Accessed: Sep. 14, 2023]
<p align="justify">
‌	[4] J. Aspuru et al., “Segmentation of the ECG signal by means of a linear regression algorithm,” Sensors, vol. 19, no. 4, p. 775, 2019. doi:10.3390/s19040775 
<p align="justify">
[5] “Taller de interpretación del electrocardiograma.: Fisiología,” FISIOLOGA, https://fisiologia.facmed.unam.mx/index.php/taller-de-interpretacion-del-electrocardiograma/
<p align="justify">
[6] G. Goldich, “El Electrocardiograma de 12 Derivaciones: Parte I: Reconocimiento de los hallazgos normales,” Nursing (Ed. española), vol. 32, no. 2, pp. 28–34, 2015. doi:10.1016/j.nursi.2015.03.010 
<p align="justify">
[7]Electrocardiography (ECG) Sensor User Manual - Plux Biosignals, https://support.pluxbiosignals.com/wp-content/uploads/2021/10/biosignalsplux-Electrocardiography-ECG-User-Manual.pdf . 
<p align="justify">
[8] JavierFelipe, “Frecuencia cardíaca, todo lo que necesitas saber,” Mundo Entrenamiento, Jul. 24, 2014. https://mundoentrenamiento.com/frecuencia-cardiaca/?= (accessed Sep. 18, 2023).
<p align="justify">
[9] “Ley N.° 29733,” Www.gob.pe, 2023. https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733 (accessed Sep. 18, 2023).
<p align="justify">
[10] Memoria, A. Autor, U. Rojas, M. Paula, and G. Román, “Análisis Electrocardiográfico y del Ritmo Cardíaco durante la Competencia de Maratón de Barcelona 2017.” Accessed: Sep. 18, 2023. [Online]. Available: https://upcommons.upc.edu/bitstream/handle/2117/349759/TFG%20MariaPaulaUsecheRojas.pdf?sequence=1&isAllowed=y
<p align="justify">
‌[11] “Dos maneras fáciles y precisas de medir tu frecuencia cardíaca,” Mayo Clinic, 2022. https://www.mayoclinic.org/es/healthy-lifestyle/fitness/expert-answers/heart-rate/faq-20057979 (accessed Sep. 18, 2023).
<p align="justify">
[12] Suntaxi Suntaxi, T.M. (2019) Repositorio Digital: Variabilidad de la Frecuencia cardiaca (HRV) ) como parámetro para valorar el sobreentrenamiento. Available at: http://www.dspace.uce.edu.ec/handle/25000/18206 (Accessed: 18 September 2023).
<p align="justify">
[13] S. Genovesi, D. Zaccaria, E. Rossi, Maria Grazia Valsecchi, A. Stella, and M. Stramba-Badiale, “Effects of exercise training on heart rate and QT interval in healthy young individuals: are there gender differences?,” Europace, vol. 9, no. 1, pp. 55–60, Jan. 2007, doi: https://doi.org/10.1093/europace/eul145.
<p align="justify">
‌[14] R. Rojas Jiménez, A. Diosdado, and J. Zamora, “Detector de picos de ECG y algoritmo de análisis de forma de onda.” Available: https://www.esfm.ipn.mx/assets/files/esfm/docs/RNAFM/articulos-2020/XXVRNAFM076.pdf

