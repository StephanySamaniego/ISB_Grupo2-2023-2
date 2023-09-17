# Laboratorio 4: Uso del Bitalino para ECG

1. [Contexto](#context)
2. [Marco teórico](#marco)
3. [Objetivos](#obj)
4. [Materiales y equipos](#mat)
5. [Resultados](#resul)\
     5.1 [Fotos de la conexión usada](#conex)\
     5.2 [Video de la señal](#senal)\
     5.3 [Ploteo de la señal en OpenSignal](#plot)\
     5.4 [Archivos](#arch)\
     5.5 [Ploteo de la señal en Python](#plote)
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

Para obtener las señales se usó la conexión en la placa BiTalino con un sensor de EMG de 3 electrodos.

<p align="center"><img src="" width="400" height="266"></p>
</p>

<p align="justify">
Se procedió a tomar señales de dos miembros del equipo siguiendo el protocolo de BITalino ®evolution Lab Guide, experimental guides to meet & learn your biosignals.

<p align="justify">
Para iniciar el experimento es necesario conectar el sensor a la placa y, a continuación, identificar el canal al que está conectado el sensor y asegurarse de que está seleccionado para la adquisición en el software, en la parte posterior del núcleo ensamblado BITalino (r)evolution Assembled Core encontrará la caja etiquetada como AX (X=1, ..., 6) donde X corresponde al número de canal. A continuación se puede realizar el siguiente procedimiento.
