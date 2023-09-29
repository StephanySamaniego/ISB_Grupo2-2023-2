# Laboratorio 4: Procediemietno de registro EEG

1. [Contexto](#context)
2. [Marco teórico](#marco)
3. [Objetivos](#obj)
4. [Materiales y equipos](#mat)
5. [Resultados](#resul)\
     5.1 [Fotos de la conexión usada](#conex)\
     5.2 [Explicación del protocolo seguido](#senal)\
     5.3 [Ploteo de la señal en OpenBCI GUI](#plot)\
     5.4 [Archivos](#arch)\
     5.5 [Ploteo de la señal en Python](#plote)\
6. [Conclusiones](#conclu)
7. [Referencias](#ref)

## **Contexto** <a name="context"></a>
---

<p align="justify">Las enfermedades cardiovasculares (ECV) son la principal causa de muerte a nivel mundial y se calcula que cobran 17,9 millones de vidas cada año. Las ECV son un grupo de trastornos del corazón y los vasos sanguíneos e incluyen enfermedades coronarias, enfermedades cerebrovasculares, enfermedades cardíacas reumáticas y otras afecciones. Más de cuatro de cada cinco muertes por ECV se deben a ataques cardíacos y accidentes cerebrovasculares, y un tercio de estas muertes ocurren prematuramente en personas menores de 70 años. Las enfermedades cardiovasculares afectan en mucha mayor medida a los países de ingresos bajos y medianos: más del 80% de las defunciones por esta causa se producen en esos países. [1] Según MINSA, en el Perú, mueren más de 4 mil personas al año por infarto al miocardio y el principal factor de riesgo se encuentra en individuos mayores de 30, especialmente en hipertensos[2]. Lima como región presenta más decesos por infarto, con más de dos mil casos por año. [3] Esencialmente el ECG se indica para confirmar o descartar la sospecha de una enfermedad cardíaca. sea esta una cardiopatía coronaría o principalmente arritmias. En algunos casos el ECG, es el primer indicador de enfermedades cardíacas cuando dentro de los exámenes de rutina, preventiva, inicio de actividad física programada u otro, se pesquisa de anomalía[4]. </p>

<p align="center">
  <img src="https://img.freepik.com/vector-premium/cardiologia-cardiologo-examina-corazon-humano-medico-trata-enfermedad-cardiaca-verifica-latidos-cardiacos-pulso-paciente-cardiograma-diagnostico-accidente-cerebrovascular_284092-2682.jpg?w=2000"  width="300" height="200"> </p>

## **Marco teórico** <a name="obj"></a>
---
**Señal ECG**
<p align="justify"> La señal del electrocardiograma (ECG) refleja la actividad eléctrica del corazón observada desde los puntos estratégicos del cuerpo humano. Estas señales se caracterizan por cinco puntos destacados llamados puntos fiduciales: P, Q, R, S y T . El complejo QRS representa la despolarización de los ventrículos cardíacos derecho e izquierdo y se utiliza como referencia clave para el análisis de las señales. La onda P se origina en la despolarización de las aurículas, mientras que los ventrículos causan el resto de los picos. El diagnóstico de la señal se basa en la forma de estas ondas, así como en la duración de cada pico y los segmentos que los componen. En consecuencia, la identificación precisa de cada parte de la señal del ECG es fundamental para los profesionales de la salud en la detección, diagnóstico y seguimiento de diversas enfermedades cardíacas [4]. </p>

<p align="center">
  <img src="https://fisiologia.facmed.unam.mx/wp-content/uploads/2021/11/UTII-2B-img-Elementos-del-electro.jpg"  width="400" height="200"> </p>
<em><p align="center">Interpretación del ECG [5]</p></em> 

**Derivaciones**

<p align="justify"> Las primeras seis derivaciones del electrocardiograma (ECG) de 12 derivaciones se originan de cuatro electrodos ubicados en los brazos y las piernas del paciente, siendo el electrodo de la pierna derecha el de referencia. Debido a que utilizan electrodos positivos y negativos separados, se las conoce como derivaciones bipolares o estándar.

<p align="justify"> En la derivación I, el electrodo positivo se coloca en el brazo izquierdo y se encuentra opuesto al electrodo negativo en el brazo derecho en términos de la dirección del flujo de energía eléctrica. El vector promedio se desplaza desde la parte superior derecha hacia la parte inferior izquierda, lo que resulta en un flujo de energía hacia el electrodo positivo de la derivación I, generando así un complejo QRS con una forma ascendente. Sin embargo, debido a que el vector promedio no se dirige directamente hacia la derivación I, sino que se acerca a ella con un cierto ángulo, la altura del complejo QRS es moderada [6]. </p>

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/derivaciones.png?raw=true"  width="400" height="200"> </p>
  <em><p align="center">Derivaciones de Einthoven y los ángulos [7]</p></em> 

## **Objetivos** <a name="obj"></a>
---
● Adquirir señales biomédicas de ECG.

● Hacer una correcta configuración de BiTalino.

● Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution


## **Materiales y equipos** <a name="mat"></a>
---
<div align="center">

| **Modelo** | **Descripción** | **Imagen Referencial** |
|:-------------:|:-------------:|:-------------:|
| (R)evolution | <p align="justify">**Kit BITalino:** Plataforma de adquisición de bioseñales viene con diferentes sensores, como EMG ,ECG o EEG. Envía como una placa todo en uno, con todos los bloques electrónicos necesarios para la adquisición de bioseñales preconectados.</p> | <div align="center"> <img src="https://cdn.sparkfun.com//assets/parts/1/1/8/2/8/14022-01a.jpg" width="50%" height="50%"> |
| - |<p align="justify"> **Cable EMG de 3 derivaciones :** Registra la actividad eléctrica del corazón desde tres ubicaciones diferentes en el cuerpo del paciente. </p>  |<div align="center"> <img src="https://cdn.cloudbf.com/thumb/format/mini_xsize/files/47/img/2022/06/27/202206270945000152799.jpg.webp" width="50%" height="50%"> |
| - |<p align="justify">**Electrodos:** Los electrodos registran la actividad eléctrica de los músculos durante la contracción y el relajamiento muscular</p> | <div align="center"> <img src="https://beurer.pe/assets/sources/ELECTRODOS%20X8%201.jpg" width="50%" height="50%">  |
| - |<p align="justify"> **Software OpenSignals:** Software e diseñado para la adquisición, procesamiento y análisis de datos biomédicos, incluyendo señales fisiológicas y de movimiento.</p>  | <div align="center"> <img src="https://cdn.shopify.com/s/files/1/0595/1068/5887/t/6/assets/ezgif5b55a161ca2-1-1-1649945010655.png?v=1649945012" width="50%" height="50%">  |
| - | <p align="justify">**Laptop o PC:** Descargar el software en una Laptop para procesar las señales.</p> | <div align="center"> <img src="https://www.lenovo.com/medias/lenovo-laptops-thinkbook-16-gen-4-intel-hero.png?context=bWFzdGVyfHJvb3R8MzQ1OTM2fGltYWdlL3BuZ3xoMjEvaGZkLzEzMjU1MTI1OTkxNDU0LnBuZ3xlMGJjMDAyZjIzYzczYmY0YTY3NTlmODcwMDJjZTBhMzg5M2VlMjFlNTNlZWJkZDMyNDA3MTdlNjc3NjhhZWY5" width="50%" height="50%">  |
| HP Multifuncional | <p align="justify">**Caminadora eléctrica:** Se requiere para inducir el ejercicio físico en los participantes y medir su actividad cardíaca después del ejercicio.</p> | <div align="center"> <img src="https://promart.vteximg.com.br/arquivos/ids/5722154-1000-1000/image-460be51623694433a913cef6360e24c2.jpg?v=637872973108530000" width="50%" height="50%">  |
| Fluke | <p align="justify">**Prosim4:** Diseñado para comprobar y verificar el funcionamiento básico de sistemas utilizados para vigilar varios parámetros fisiológicos de un paciente, entre los que se encuentran el ECG, la respiración, la presión arterial invasiva y la presión arterial no invasiva. </p> | <div align="center"> <img src="https://www.flukebiomedical.com/sites/default/files/styles/slideshow_image/public/prosim4front_0.png" width="50%" height="50%">  |

</div>

## **Resultados** <a name="resul"></a>
---
### **Conexión usada** <a name="conex"></a>

Para obtener las señales se usó la conexión en la placa BiTalino con un sensor de ECG de 3 electrodos. Para obtener la señal ECG, se ubicaron los electrodos positivo y negativo en la muñeca, en la arteria radial, para medir el pulso radial, se eligió esta ubicación, ya que es el más fiable. La zona del cuello palpando la carótida también es muy fiable, pero según en qué personas puede afectar a la disminución de la frecuencia cardíaca [8]. 

En este informe se mantiene la identidad anónima y datos personales de las personas involucradas en los experimentos siguiendo así la Ley N.° 29733:Ley de Protección de Datos Personales, la presente Ley tiene el objeto de garantizar el derecho fundamental a la protección de los datos personales, previsto en el artículo 2 numeral 6 de la Constitución Política del Perú, a través de su adecuado tratamiento, en un marco de respeto de los demás derechos fundamentales que en ella se reconocen [9].



<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/imagen.png?raw=true" width="400" height="266"></p>
</p>

<p align="justify">
Se procedió a tomar señales de dos miembros del equipo siguiendo el protocolo de BITalino ®evolution Lab Guide, experimental guides to meet & learn your biosignals.

### **Explicación del protocolo seguido** <a name="senal"></a>

| **Pasos** | **Imagen** | **Imagen** |
|:-------------:|:-------------:|:-------------:|
|<p align="justify"> 1. Conectar el BITalino (r)evolution Core BT </p> <p align="justify">2. Prueba de la configuración </p> | <div align="center"> <img src="https://cdn.sparkfun.com//assets/parts/1/1/8/2/8/14022-01a.jpg" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/conexion.png?raw=true" width="50%" height="50%">| 
|<p align="justify">3. Conectar el Sensor de ECG ensamblado a uno de los canales analógicos disponibles. </p> <p align="justify">4. Colocar los Electrodos con Gel en los broches de los tres sensores de ECG. </p>  <p align="justify">5. Colocar los electrodos en ambas muñecas y el maléolo lateral. </p> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/conexion_masc.jpg?raw=true" width="50%" height="50%">  <p align="center"> Sujeto masculino </p> |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/conexiones_fem.jpg?raw=true" width="50%" height="50%">  <p align="center">Sujeto femenino</p> | 
|<p align="justify"> 6. Iniciar la grabación de datos en OpenSignals (r)evolution. <p align="justify"> 7. Grabar una línea de base de señal con bajo ruido y sin movimientos durante 30 segundos.| <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/1c565ffe-4944-45c2-b2cc-0b917930bd23" width="50%" height="50%"></video> Sujeto masculino | <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/9f5b285e-bee0-4c66-b8b4-50fe8cf17ca8" width="50%" height="50%"></video> Sujeto femenino| 
|<p align="justify"> 8. Retirar los electrodos y realizar actividad física (correr) en la caminadora durante un período de cinco minutos. Se aplica un esfuerzo sostenido que involucra la contracción rítmica de los músculos de las piernas y requiere una adecuada capacidad aeróbica para mantener la actividad a lo largo de la duración especificada.|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/efaca9ab-db45-4a67-80a3-b966748e00dc" width="50%" height="50%"></video> | |
|<p align="justify"> 9. Subir las escaleras trotando durante dos minutos y colocarse los electrodos en las posiciones antes mencionadas. <p align="justify"> 10. Grabar la señal después del ejercicio. <p align="justify"> 11. Detener la grabación y guardar los datos [7]| <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/193f9b68-3f72-411b-b94d-aa701767bca1" width="50%" height="50%"></video> Sujeto masculino | <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/193f9b68-3f72-411b-b94d-aa701767bca1" width="50%" height="50%"></video> Sujeto femenino| 

### Ploteo de la señal en OpenSignal <a name="plot"></a>
Para empezar a tomar la señal en reposo o silencio eléctrico es importante no tener objetos metálicos como aretes, anillos, cadenas, etc; ya que generan interferencias.

<div align="center">

| **Etapa** | **Sujeto masculino** | **Sujeto femenino** |
|:-------------:|:-------------:|:-------------:|
| Reposo| <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_carlos.jpg?raw=true" width="50%" height="50%"> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_stephany.jpg?raw=true" width="50%" height="50%"> |
| Agitado |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_agirtado_carlos.jpg?raw=true" width="50%" height="50%"> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_agitado_stephany.jpg?raw=true" width="50%" height="50%"> |

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


2. **Número de latidos calculado:**
<p align="justify">
En cuanto al número de latidos del corazón en 2 segundos puede variar ampliamente de una persona a otra debido a factores como la frecuencia cardíaca en reposo, la edad y la salud en general. Sin embargo, para obtener una estimación aproximada, puedes considerar la frecuencia cardíaca promedio en reposo, que suele estar entre 60 y 100 latidos por minuto en adultos sanos [11].
Análisis
Si asumimos una frecuencia cardíaca en reposo de alrededor de 70 latidos por minuto (lo que es una estimación promedio), puedes calcular el número de latidos en 2 segundos de la siguiente manera:
<p align="justify">
Si tenemos 70 latidos por minuto / 60 segundos = 1.17 latidos por segundo. Entonces, 1.17 latidos por segundo x 2 segundos ≈ 2.34 latidos en 2 segundos
<p align="justify">
Por lo tanto, en promedio, podría haber alrededor de 2 a 3 latidos del corazón en 2 segundos en una persona con una frecuencia cardíaca en reposo de alrededor de 70 latidos por minuto.

3. **Variabilidad de la frecuencia cardíaca:**
<p align="justify">
La variabilidad de la frecuencia cardíaca se refiere a la variación en intervalos de tiempo entre los latidos del corazón, es decir, al número de latidos en un momento preciso o espacio de tiempo previamente determinado, por lo general esta medida se basa en el cálculo de la diferencia de tiempo entre cada una de las ondas R, que serían los intervalos RR, en un trazo del electrocardiograma en determinados periodos. Si hay una amplia variación en intervalos de tiempo se nota un equilibrio saludable entre el insumo simpático y parasimpático del miocardio, mientras qué poca variación entonces refleja un insumo autónomo disfuncional. La baja variabilidad de la frecuencia cardíaca se relaciona con el riesgo incrementado de insuficiencia cardíaca, infarto al 26 miocardio y muerte súbita cardiaca, mientras que la actividad física regular promueve un incremento de la variabilidad de la frecuencia cardíaca [12]

4. **Diferencia de género:** 

<p align="justify">
Se ha demostrado que existen diferencias de género en la frecuencia cardíaca, la duración del intervalo QT y en la relación entre la repolarización ventricular y la duración del ciclo cardíaco. Las mujeres, en comparación con los hombres, tienen una frecuencia cardíaca más alta y un intervalo QT más largo corregido por la frecuencia cardíaca. Se ha demostrado una mayor prolongación del intervalo QT en ciclos de larga duración y un efecto más significativo de los fármacos que prolongan el QTc en mujeres, en comparación con los hombres. También se ha demostrado una mayor alteración de la duración de la repolarización ventricular en las mujeres en comparación con sus homólogos masculinos en respuesta a cambios importantes en el plasma y los electrolitos intracelulares, como durante la hemodiálisis [13]

5. **Comparación entre sujetos**

Se les realizó una pequeña entrevista a los sujetos involucrados para poder rescatar datos importantes que pueden influenciar en la toma de un ECG.

| **Preguntas**| **Sujeto Femenino** | **Sujeto Masculino** | 
|:-------------:|:-------------:|:-------------:|
|<p align="justify">1. ¿Has padecido o padeces de alguna enfermedad cardíaca?|No|No |
|<p align="justify">2. ¿Cuál es tu actividad principal en la mañana y cuál en la tarde?| En la mañana a veces voy a la universidad caminando y en las tardes usualmente no hago actividad física.|Gimnasio y caminar|
|<p align="justify">3. ¿Cuántos litros de agua sueles tomar al día?|2 litros de agua mínimo |3 litros de agua|
|<p align="justify">4. ¿Consumes algún tipo de medicamento actualmente?|No|No | 
|<p align="justify">5. ¿Cuánto tiempo de caminata diaria sueles hacer|30 minutos|2 horas | 
|<p align="justify">6. ¿Sueles hacer ejercicio durante la semana| Podría decirse que nunca pero sí suelo caminar mucho|Siempre |


</div>

### **Archivos** <a name="arch"></a>

- [Documentos.txt](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2004%20%20-%20BiTalino%20ECG/Documentaci%C3%B3n/Archivos_txt)
- [Código para plotear señales en Python](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2004%20%20-%20BiTalino%20ECG/Documentaci%C3%B3n/C%C3%B3digos)

### **Ploteo de la señal en Python** <a name="plote"></a>

<div align="center">

| **Etapa** | **Sujeto masculino** | **Sujeto femenino** |
|:-------------:|:-------------:|:-------------:|
| Reposo| <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgMasculino.png?raw=true" > <p align="justify">Según la gráfica, se muestra en la imagen del sujeto masculino en reposo un promedio de 2 latidos en los 2 segundos, lo cual tiene sentido según la bibliografía consultada. Además, se tiene un pico máximo del complejo QRS de algo más de 800 en amplitud, y un pico mínimo de aproximadamente 320 de amplitud. Existe una variabilidad de la frecuencia cardíaca de 0.75 segundos (0.85 - 0.10) aproximadamente entre cada latido, lo cual indica que la persona se encuentra en un estado de reposo. El intervalo QT es de aproximadamente 0.18 segundos.| <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgFemenino.png?raw=true"><p align="justify">Según la gráfica, se muestra en la imagen del sujeto femenino en reposo un promedio de 3 latidos en los 2 segundos, lo cual se encuentra cerca de la información según la bibliografía consultada. Además, se tiene un pico máximo del complejo QRS de algo más de 700 en amplitud, y un pico mínimo de aproximadamente 320 de amplitud. Existe una variabilidad de la frecuencia cardíaca (distancia entre R) de 0.60 segundos (0.70 - 0.10) aproximadamente entre cada latido, lo cual indica que la persona se encuentra en un estado de reposo. El intervalo QT es de aproximadamente 0.22 segundos. |
| Agitado |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgMasculinoAgitado.png?raw=true" ><p align="justify"> Según la gráfica, se muestra en la imagen del sujeto masculino agitado un total de 4 latidos en los 2 segundos,contando el primer complejo QRS como el número 0. Se puede notar un aumento de la frecuencia cardíaca a comparación del gráfico en reposo. A comparación de la gráfica en reposo, se tiene un pico máximo del complejo QRS de un poco más de 700 en amplitud, y un pico mínimo de aproximadamente 290 de amplitud. Existe una variabilidad de la frecuencia cardíaca de 0.45 segundos (0.70 - 0.25) aproximadamente entre cada latido, lo cual es menor al obtenido en el gráfico de reposo, lo cual indicaría que efectivamente la persona se encuentra en un estado de agitación. El intervalo QT es de aproximadamente 0.15 segundos.| <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgFemeninoAgitado.png?raw=true" > <p align="justify">Según la gráfica, se muestra en la imagen del sujeto femenino agitada un total de 3 latidos en los 2 segundos, contando el primer complejo QRS como el número 0, lo cual nos indica que no hay una variación destacable. No se puede notar un aumento notorio de la frecuencia cardíaca a comparación del gráfico en reposo. A comparación de la gráfica en reposo, se tiene un pico máximo del complejo QRS de un poco más de 700 en amplitud, y un pico mínimo de aproximadamente 270 de amplitud. Existe una variabilidad de la frecuencia cardíaca de 0.57 segundos (0.76 - 0.19) aproximadamente entre cada latido, el cual es solo un poco menor al obtenido en el gráfico de reposo, lo cual indicaría que la persona se encuentra en un estado de agitación, pero no tanta. El intervalo QT es de aproximadamente 0.20 segundos.|
</div>

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

### **Señal en Prosim4** <a name="prosim"></a>

### Parada cardiaca

Se consideraron los siguientes parámetros:
- ECG 80lpm: 45s
- CVP(VI): 30s
- Taq. vent. 160 lpm: 30s
- Fib. vent severa: 30s
- Asistolia: 30s
- Stop


<div align="center">

| **Etapa** | **Prosim** | **Señal** |
|:-------------:|:-------------:|:-------------:|
| Fase 1 | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_1.jpg?raw=true" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro1.png?raw=true" > | 
| Fase 2 |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_2.jpg?raw=true" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro2.png?raw=true" > | 
| Fase 3 |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_3.jpg?raw=true" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro3.png?raw=true" > | 
| Fase 4 | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_4.jpg?raw=true" width="50%" height="50%"> |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro4.png?raw=true" > | 
| Fase 5 |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_5.jpg?raw=true" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro5.png?raw=true" > | 

</div>

## **Conclusiones** <a name="conclu"></a>
---
- El ruido proveniente de la respiración y contracción muscular puede afectar a la adquisición del ECG, por lo tanto, también afectaría a la eficiencia del algoritmo. Adicionar filtros digitales podría servir para reducir el ruido bajo severas condiciones, sin embargo, esto podría no remover por completo el ruido.
- Se lograron encontrar diferencias entre ambos sujetos y compararlos exitosamente.
- La sujeto femenino posee una variabilidad de frecuencia cardíaca menor que el del sujeto masculino, lo cual evidenciaría las diferencias entre ambos en los aspectos de su vida cotidiana.
- Ninguno de ellos posee una gráfica de reposo ni de agitación parecida al de alguna enfermedad cardíaca, por lo que se descarta ello.
- Se logró con éxito plotear las señales en Python y así lograr un análisis de estas.
- Se cumplió con la protección de la identidad de ambos sujetos, ya que es vital en este tipo de pruebas, por lo que se tuvo extremado cuidado en proteger el rostro y datos personales.



## **Referencias** <a name="context"></a>
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
