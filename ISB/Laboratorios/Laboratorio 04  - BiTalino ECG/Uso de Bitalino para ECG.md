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

Las enfermedades cardiovasculares (ECV) son la principal causa de muerte a nivel mundial y se calcula que cobran 17,9 millones de vidas cada año. Las ECV son un grupo de trastornos del corazón y los vasos sanguíneos e incluyen enfermedades coronarias, enfermedades cerebrovasculares, enfermedades cardíacas reumáticas y otras afecciones. Más de cuatro de cada cinco muertes por ECV se deben a ataques cardíacos y accidentes cerebrovasculares, y un tercio de estas muertes ocurren prematuramente en personas menores de 70 años. Las enfermedades cardiovasculares afectan en mucha mayor medida a los países de ingresos bajos y medianos: más del 80% de las defunciones por esta causa se producen en esos países. [1] Según MINSA, en el Perú, mueren más de 4 mil personas al año por infarto al miocardio y el principal factor de riesgo se encuentra en individuos mayores de 30, especialmente en hipertensos. Lima como región presenta más decesos por infarto, con más de dos mil casos por año. (3) Esencialmente el ECG se indica para confirmar o descartar la sospecha de una enfermedad cardíaca. sea esta una cardiopatía coronaría o principalmente arritmias. En algunos casos el ECG, es el primer indicador de enfermedades cardíacas cuando dentro de los exámenes de rutina, preventiva, inicio de actividad física programada u otro, se pesquisa de anomalía. (4)

<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/caa51a04-b9cb-4601-8867-50f76c7e409d"  width="200" height="200"> </p>

## **Marco teórico** <a name="obj"></a>
---


## **Objetivos** <a name="obj"></a>
---
● Adquirir señales biomédicas de EMG y ECG.

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

</div>

## **Resultados** <a name="resul"></a>
---
### **Conexión usada** <a name="conex"></a>

Para obtener las señales se usó la conexión en la placa BiTalino con un sensor de ECG de 3 electrodos. Se procedió a tomar señales de dos integrantes del equipo siguiendo el protocolo de BITalino ®evolution Lab Guide, experimental guides to meet & learn your biosignals. El electrodo positivo (rojo) se coloca en la clavícula izquierda (LA), mientras que el electrodo negativo (negro) se coloca en la clavícula derecha (RA). El electrodo de referencia (REF) en color blanco se coloca en la cresta ilíaca.

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
| Reposo| <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_carlos.jpg?raw=true" width="50%" height="50%"> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_stephany.jpg?raw=true" width="50%" height="50%"> |
| Agitado |<img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_agirtado_carlos.jpg?raw=true" width="50%" height="50%"> | <div align="center"> <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_04/se%C3%B1al_agitado_stephany.jpg?raw=true" width="50%" height="50%"> |

</div>
