# Laboratorio 3: Uso del Bitalino para EMG

1. [Objetivos](#obj)
2. [Materiales y equipos](#mat)
3. [Resultados](#resul)\
     3.1 [Fotos de la conexión usada](#conex)\
     3.2 [Video de la señal](#senal)\
     3.3 [Ploteo de la señal en OpenSignal](#plot)\
     3.4 [Archivos](#arch)\
     3.5 [Ploteo de la señal en Python](#plote)


## Objetivos <a name="obj"></a>

● Adquirir señales biomédicas de EMG y ECG.

● Hacer una correcta configuración de BiTalino.

● Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution

## Materiales y equipos <a name="mat"></a>

| Modelo | Descripción | Cantidad |
|:-------------:|:-------------:|:-------------:|
| (R)evolution | Kit Bitalino | 1 |
| - | Laptop o PC | 1 |
| - | Cable EMG de 3 derivaciones | 1 |
| - | Electrodos | 3 |
| - | Software OpenSignals | 1 |



## Resultados <a name="resul"></a>

### Conexión usada <a name="conex"></a>

Para obtener las señales se usó la conexión en la placa BiTalino con un sensor de EMG de 3 electrodos.

<p align="center"><img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Posicion%20_electrodos.jpg?raw=true" width="400" height="266"></p>
</p>

<p align="justify">
Se procedió a tomar señales de cada miembro del equipo siguiendo el protocolo de BITalino ®evolution Lab Guide, experimental guides to meet & learn your biosignals.

<p align="justify">
Para iniciar el experimento es necesario conectar el sensor a la placa y, a continuación, identificar el canal al que está conectado el sensor y asegurarse de que está seleccionado para la adquisición en el software, en la parte posterior del núcleo ensamblado BITalino (r)evolution Assembled Core encontrará la caja etiquetada como AX (X=1, ..., 6) donde X corresponde al número de canal. A continuación se puede realizar el siguiente procedimiento.

**EXPLICACIÓN DEL PROTOCOLO SEGUIDO**

1. Conectar su BITalino (r)evolution Core BT
2. Prueba de la configuración
3. Colocar los dos electrodos (positivo y negativo) en el músculo bíceps braquial izquierdo separados aproximadamente 2cm
4. Colocar el tercer electrodo, el de referencia, en una zona de baja actividad muscular, en este caso, en el codo.
5. Empezar a registrar una línea de base de señal con poco ruido y sin activación muscular durante 30 segundos.
6. Comenzar a registrar los datos en OpenSignals (r)evolution
7. Repetir un ciclo de Contracción-Liberación-Descanso cinco veces, manteniendo la contracción dos segundos y descansando dos segundos, intenta comenzar con una contracción de baja intensidad y aumente gradualmente el nivel en cada repetición, de tal forma que la última corresponda a tu máxima capacidad de contracción voluntaria.
8. Detener  la grabación y guardar los datos [1].

**CONEXIONES**

| ![Imagen 1](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Conexion_Carlos.jpg?raw=true) | ![Imagen 2](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Conexion_Marcelo.jpg?raw=true) |
|--------------------------|--------------------------|
| ![Imagen 3](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Conexion_Sara.jpg?raw=true) | ![Imagen 4](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Conexion_Steph.jpg?raw=true) |

