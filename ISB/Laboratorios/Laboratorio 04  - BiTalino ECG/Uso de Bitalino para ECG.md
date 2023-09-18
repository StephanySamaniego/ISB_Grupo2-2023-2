# Laboratorio 4: Uso del Bitalino para ECG

1. [Contexto](#context)
2. [Marco teórico](#marco)
3. [Objetivos](#obj)
4. [Materiales y equipos](#mat)
5. [Resultados](#resul)\
     5.1 [Fotos de la conexión usada](#conex)\
     5.2 [Explicación del protocolo seguido](#senal)\
     5.3 [Ploteo de la señal en OpenSignal](#plot)\
     5.4 [Archivos](#arch)\
     5.5 [Ploteo de la señal en Python](#plote)\
     5.3 [Señal en Prosim4](#prosim)
6. [Referencias](#ref)

## **Contexto** <a name="context"></a>
---

<p align="justify">Las enfermedades cardiovasculares (ECV) son la principal causa de muerte a nivel mundial y se calcula que cobran 17,9 millones de vidas cada año. Las ECV son un grupo de trastornos del corazón y los vasos sanguíneos e incluyen enfermedades coronarias, enfermedades cerebrovasculares, enfermedades cardíacas reumáticas y otras afecciones. Más de cuatro de cada cinco muertes por ECV se deben a ataques cardíacos y accidentes cerebrovasculares, y un tercio de estas muertes ocurren prematuramente en personas menores de 70 años. Las enfermedades cardiovasculares afectan en mucha mayor medida a los países de ingresos bajos y medianos: más del 80% de las defunciones por esta causa se producen en esos países. [1] Según MINSA, en el Perú, mueren más de 4 mil personas al año por infarto al miocardio y el principal factor de riesgo se encuentra en individuos mayores de 30, especialmente en hipertensos. Lima como región presenta más decesos por infarto, con más de dos mil casos por año. (3) Esencialmente el ECG se indica para confirmar o descartar la sospecha de una enfermedad cardíaca. sea esta una cardiopatía coronaría o principalmente arritmias. En algunos casos el ECG, es el primer indicador de enfermedades cardíacas cuando dentro de los exámenes de rutina, preventiva, inicio de actividad física programada u otro, se pesquisa de anomalía. (4) </p>

<p align="center">
  <img src="https://img.freepik.com/vector-premium/cardiologia-cardiologo-examina-corazon-humano-medico-trata-enfermedad-cardiaca-verifica-latidos-cardiacos-pulso-paciente-cardiograma-diagnostico-accidente-cerebrovascular_284092-2682.jpg?w=2000"  width="300" height="200"> </p>

## **Marco teórico** <a name="obj"></a>
---
**Señal ECG**
<p align="justify"> La señal del electrocardiograma (ECG) refleja la actividad eléctrica del corazón observada desde los puntos estratégicos del cuerpo humano. Estas señales se caracterizan por cinco puntos destacados llamados puntos fiduciales: P, Q, R, S y T . El complejo QRS representa la despolarización de los ventrículos cardíacos derecho e izquierdo y se utiliza como referencia clave para el análisis de las señales. La onda P se origina en la despolarización de las aurículas, mientras que los ventrículos causan el resto de los picos. El diagnóstico de la señal se basa en la forma de estas ondas, así como en la duración de cada pico y los segmentos que los componen. En consecuencia, la identificación precisa de cada parte de la señal del ECG es fundamental para los profesionales de la salud en la detección, diagnóstico y seguimiento de diversas enfermedades cardíacas (4). </p>

<p align="center">
  <img src="https://fisiologia.facmed.unam.mx/wp-content/uploads/2021/11/UTII-2B-img-Elementos-del-electro.jpg"  width="300" height="200"> </p>
<em><p align="center">Interpretación del ECG </p></em> 

**Derivaciones**

<p align="justify"> Las primeras seis derivaciones del electrocardiograma (ECG) de 12 derivaciones se originan de cuatro electrodos ubicados en los brazos y las piernas del paciente, siendo el electrodo de la pierna derecha el de referencia. Debido a que utilizan electrodos positivos y negativos separados, se las conoce como derivaciones bipolares o estándar.

<p align="justify"> En la derivación I, el electrodo positivo se coloca en el brazo izquierdo y se encuentra opuesto al electrodo negativo en el brazo derecho en términos de la dirección del flujo de energía eléctrica. El vector promedio se desplaza desde la parte superior derecha hacia la parte inferior izquierda, lo que resulta en un flujo de energía hacia el electrodo positivo de la derivación I, generando así un complejo QRS con una forma ascendente. Sin embargo, debido a que el vector promedio no se dirige directamente hacia la derivación I, sino que se acerca a ella con un cierto ángulo, la altura del complejo QRS es moderada (5). </p>

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/derivaciones.png?raw=true"  width="350" height="200"> </p>
  <em><p align="center">Derivaciones de Einthoven y los ángulos </p></em> 

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

Para obtener las señales se usó la conexión en la placa BiTalino con un sensor de ECG de 3 electrodos. Para obtener la señal ECG, se ubicaron los electrodos positivo y negativo en la muñeca, en la arteria radial, para medir el pulso radial, se eligió esta ubicación, ya que es el más fiable. La zona del cuello palpando la carótida también es muy fiable, pero según en qué personas puede afectar a la disminución de la frecuencia cardíaca [b]. 

En este informe se mantiene la identidad anónima y datos personales de las personas involucradas en los experimentos siguiendo así la Ley N.° 29733:Ley de Protección de Datos Personales, la presente Ley tiene el objeto de garantizar el derecho fundamental a la protección de los datos personales, previsto en el artículo 2 numeral 6 de la Constitución Política del Perú, a través de su adecuado tratamiento, en un marco de respeto de los demás derechos fundamentales que en ella se reconocen [a].



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
|<p align="justify"> 9. Subir las escaleras trotando durante dos minutos y colocarse los electrodos en las posiciones antes mencionadas. <p align="justify"> 10. Grabar la señal después del ejercicio. <p align="justify"> 11. Detener la grabación y guardar los datos | <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/193f9b68-3f72-411b-b94d-aa701767bca1" width="50%" height="50%"></video> Sujeto masculino | <video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/193f9b68-3f72-411b-b94d-aa701767bca1" width="50%" height="50%"></video> Sujeto femenino| 

### Ploteo de la señal en OpenSignal <a name="plot"></a>
Para empezar a tomar la señal en reposo o silencio eléctrico es importante no tener objetos metálicos como aretes, anillos, cadenas, etc; ya que generan interferencias.

<div align="center">

| **Etapa** | **Sujeto masculino** | **Sujeto femenino** |
|:-------------:|:-------------:|:-------------:|
| Reposo| <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_carlos.jpg?raw=true" width="50%" height="50%"> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_stephany.jpg?raw=true" width="50%" height="50%"> |
| Agitado |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_agirtado_carlos.jpg?raw=true" width="50%" height="50%"> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_agitado_stephany.jpg?raw=true" width="50%" height="50%"> |

</div>

### Discusión
El estado de reposo varía según la presencia de actividades espontáneas propias de la fisiología de cada participante, de interferencia o ruidos propios del ambiente de trabajo y posibles errores en la medición, ya sea por desgaste del gel de los electrodos o por la falta de adherencia en la piel. [2]
Por otro lado, la contracción voluntaria máxima que se produce al realizar la flexión del brazo para vencer una fuerza de agarre, esta se verá afectada por las interferencias, pero a su vez por el estímulo del participantes, pues la diferencia de potencial puede variar según el esfuerzo y anatomía del participante. [3]

### **Archivos** <a name="arch"></a>

- [Documentos.txt](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2004%20%20-%20BiTalino%20ECG/Documentaci%C3%B3n/Archivos_txt)
- [Código para plotear señales en Python](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2004%20%20-%20BiTalino%20ECG/Documentaci%C3%B3n/C%C3%B3digos)

### **Ploteo de la señal en Python** <a name="plote"></a>

<div align="center">

| **Etapa** | **Sujeto masculino** | **Sujeto femenino** |
|:-------------:|:-------------:|:-------------:|
| Reposo| <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgMasculino.png?raw=true" width="50%" height="50%"> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgFemenino.png?raw=true" width="50%" height="50%"> |
| Agitado |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgMasculinoAgitado.png?raw=true" width="50%" height="50%"> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgFemeninoAgitado.png?raw=true" width="50%" height="50%"> |
</div>

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
| Fase 1 | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_1.jpg?raw=true" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro1.png?raw=true" width="50%" height="50%"> | 
| Fase 2 |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_2.jpg?raw=true" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro2.png?raw=true" width="50%" height="50%"> | 
| Fase 3 |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_3.jpg?raw=true" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro3.png?raw=true" width="50%" height="50%"> | 
| Fase 4 | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_4.jpg?raw=true" width="50%" height="50%"> |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro4.png?raw=true" width="50%" height="50%"> | 
| Fase 5 |  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/prosim_paro_5.jpg?raw=true" width="50%" height="50%"> | <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/ecgProSim4Paro5.png?raw=true" width="50%" height="50%"> | 

</div>

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
[5] G. Goldich, “El Electrocardiograma de 12 Derivaciones: Parte I: Reconocimiento de los hallazgos normales,” Nursing (Ed. española), vol. 32, no. 2, pp. 28–34, 2015. doi:10.1016/j.nursi.2015.03.010 
