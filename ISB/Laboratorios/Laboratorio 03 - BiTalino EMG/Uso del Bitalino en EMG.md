# Laboratorio 3: Uso del Bitalino para EMG

1. [Objetivos](#obj)
2. [Materiales y equipos](#mat)
3. [Resultados](#resul)\
     3.1 [Fotos de la conexión usada](#conex)\
     3.2 [Video de la señal](#senal)\
     3.3 [Ploteo de la señal en OpenSignal](#plot)\
     3.4 [Archivos](#arch)\
     3.5 [Ploteo de la señal en Python](#plote)
4. [Referencias](#ref)

## **Objetivos** <a name="obj"></a>
---
● Adquirir señales biomédicas de EMG y ECG.

● Hacer una correcta configuración de BiTalino.

● Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution

## **Materiales y equipos** <a name="mat"></a>
---
<div align="center">

| Modelo | Descripción | Cantidad |
|:-------------:|:-------------:|:-------------:|
| (R)evolution | Kit Bitalino | 1 |
| - | Laptop o PC | 1 |
| - | Cable EMG de 3 derivaciones | 1 |
| - | Electrodos | 3 |
| - | Software OpenSignals | 1 |

</div>

## **Resultados** <a name="resul"></a>
---
### **Conexión usada** <a name="conex"></a>

Para obtener las señales se usó la conexión en la placa BiTalino con un sensor de EMG de 3 electrodos.

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Posicion%20_electrodos.jpg?raw=true" width="400" height="266"></p>
</p>

<p align="justify">
Se procedió a tomar señales de cada miembro del equipo siguiendo el protocolo de BITalino ®evolution Lab Guide, experimental guides to meet & learn your biosignals.

<p align="justify">
Para iniciar el experimento es necesario conectar el sensor a la placa y, a continuación, identificar el canal al que está conectado el sensor y asegurarse de que está seleccionado para la adquisición en el software, en la parte posterior del núcleo ensamblado BITalino (r)evolution Assembled Core encontrará la caja etiquetada como AX (X=1, ..., 6) donde X corresponde al número de canal. A continuación se puede realizar el siguiente procedimiento.

### Explicación del protocolo seguido

1. Conectar su BITalino (r)evolution Core BT
2. Prueba de la configuración
3. Colocar los dos electrodos (positivo y negativo) en el músculo bíceps braquial izquierdo separados aproximadamente 2cm
4. Colocar el tercer electrodo, el de referencia, en una zona de baja actividad muscular, en este caso, en el codo.
5. Empezar a registrar una línea de base de señal con poco ruido y sin activación muscular durante 30 segundos.
6. Comenzar a registrar los datos en OpenSignals (r)evolution
7. Repetir un ciclo de Contracción-Liberación-Descanso cinco veces, manteniendo la contracción dos segundos y descansando dos segundos, intenta comenzar con una contracción de baja intensidad y aumente gradualmente el nivel en cada repetición, de tal forma que la última corresponda a tu máxima capacidad de contracción voluntaria.
8. Detener  la grabación y guardar los datos [1].

### Conexiones en cada integrante

| ![Imagen 1](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Conexion_Carlos.jpg?raw=true) | ![Imagen 2](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Conexion_Marcelo.jpg?raw=true) |
|--------------------------|--------------------------|
| ![Imagen 3](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Conexion_Sara.jpg?raw=true) | ![Imagen 4](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Conexion_Steph.jpg?raw=true) |

### Ploteo de la señal en OpenSignal <a name="plot"></a>
Para empezar a tomar la señal en reposo o silencio eléctrico es importante no tener objetos metálicos como aretes, anillos, cadenas, etc; ya que generan interferencias.


|<video src=" https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/f83ecbe1-9d87-483c-9fca-0acb900327c7">|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/f83ecbe1-9d87-483c-9fca-0acb900327c7">|
|--------------------------|--------------------------|
|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/ab7bdc4d-9740-4748-a667-f6e4897306f6 ">|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/16f3f9ee-0a9f-429c-9950-d94414c28468">|

|<video src=" https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/f83ecbe1-9d87-483c-9fca-0acb900327c7">|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/ab7bdc4d-9740-4748-a667-f6e4897306f6">|
|--------------------------|--------------------------|
|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/ab7bdc4d-9740-4748-a667-f6e4897306f6 ">|<video src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/assets/99302662/2f495126-186e-4d6d-9352-d40d366348fd">|



### Comentarios sobre las señales obtenidas

El estado de reposo varía según la presencia de actividades espontáneas propias de la fisiología de cada participante, de interferencia o ruidos propios del ambiente de trabajo y posibles errores en la medición, ya sea por desgaste del gel de los electrodos o por la falta de adherencia en la piel. [2]
Por otro lado, la contracción voluntaria máxima que se produce al realizar la flexión del brazo para vencer una fuerza de agarre, esta se verá afectada por las interferencias, pero a su vez por el estímulo del participantes, pues la diferencia de potencial puede variar según el esfuerzo y anatomía del participante. [3]

### **Archivos** <a name="arch"></a>

- [Documentos.txt](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/Documentacion/Laboratorio%2003%20-%20BiTalino/Documentos)
- [Código para plotear señales en Python](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/Documentacion/Laboratorio%2003%20-%20BiTalino/C%C3%B3digo)

### **Ploteo de la señal en Python** <a name="plote"></a>

Señal EMG Carlos
| ![Imagen 1](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/Se%C3%B1al_Carlos.JPG?raw=true) | ![Imagen 2](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/FFT_Carlos.JPG?raw=true) | ![Imagen 3](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/Segmentos_Carlos.JPG?raw=true)|
|--------------------------|--------------------------|--------------------------|

Señal EMG Marcelo
| ![Imagen 1](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/Se%C3%B1al_Marcelo.JPG?raw=true) | ![Imagen 2](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/FFT_Marcelo.JPG?raw=true) | ![Imagen 3](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/Segmentos_Marcelo.JPG?raw=true)|
|--------------------------|--------------------------|--------------------------|

Señal EMG Sara
| ![Imagen 1](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/Se%C3%B1al_Sara.JPG?raw=true) | ![Imagen 2](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/FFT_Sara.JPG?raw=true) | ![Imagen 3](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/Segmentos_Sara.JPG?raw=true)|
|--------------------------|--------------------------|--------------------------|

Señal EMG Stephany

| ![Imagen 1](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/Se%C3%B1al_Stephany.JPG?raw=true) | ![Imagen 2](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/FFT_Stephany.JPG?raw=true) | ![Imagen 3](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_03/Segmentos_Stephany.JPG?raw=true)|
|--------------------------|--------------------------|--------------------------|

## Referencias <a name="ref"></a>
---

[1] “BITalino Lab Guides (Home Guides) – Support PLUX Biosignals official,” Pluxbiosignals.com, Apr. 2022. Available: https://support.pluxbiosignals.com/knowledge-base/bitalino-lab-guides/. [Accessed: Sep. 09, 2023]

[2] L. Gila, A. Malanda, I. Rodríguez Carreño, J. Rodríguez Falces, and J. Navallas, “Métodos de procesamiento y análisis de señales electromiográficas,” An Sist Sanit Navar, vol. 32, pp. 27–43, 2009, Accessed: Sep. 08, 2023. [Online]. Available: https://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S1137-66272009000600003&lng=es&nrm=iso&tlng=es 

[3] J. Antonio Domínguez Jiménez and S. H. Contreras Ortiz, “Análisis de las señales EMG de superficie del bíceps durante la ejecución de ejercicios con pesas,” 2015.
‌