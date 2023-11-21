# Laboratorio 10: Aplicación de TinyML

1. [Introducción](#intro)
2. [Metodología](#met)
3. [Resultados](#resul)
4. [Discusiones](#disc)
5. [Archivos](#arch)
6. [Conclusiones](#conc)
7. [Referencias](#ref)


## **Introducción** <a name="intro"></a>
---
**TinyML**
<p align="justify"> Creciente campo de de las tecnologías de machine learning y sus aplicaciones, capaces de realizar análisis de datos en dispositivos con un consumo de energía extremadamente bajo, típicamente en el rango de milivatios y menos, permitiendo así una variedad de casos de uso siempre activos y dirigidos a dispositivos alimentados por batería[1].

**Edge Impulse**
<p align="justify"> Edge Impulse es una plataforma para desarrollar algoritmos de aprendizaje máquina enfocados a implementarse en sistemas embebidos como microcontroladores o computadoras con recursos reducidos. Tiene disponibles diversas herramientas que la hacen adecuada tanto para principiantes como usuarios avanzados. La practicidad de esta herramienta es que no necesitas involucrarte demasiado con el código, puedes implementar tu algoritmo con ingresar tu base de datos, ajustas los hiperparámetros y entrenas el programa.

<p align="justify"> La interfaz es muy amigable y es bastante intuitiva. Según la página oficial puedes implementar tu proyecto en minutos (dejando de lado la etapa de aprendizaje). Para implementar tu proyecto solo tienes que crear tu cuenta, indicar que tipo de proyecto quieres hacer (detección de objetos, reconocimiento de voz, o procesar gestos de un acelerómetro) y hacer la adquisición de datos. Cuando tengas tu dataset puedes crear un Impulse, que es la herramienta que procesará y entrenará el modelo con los datos, para finalmente cargar el modelo a tu microcontrolador [2].


## **Materiales** 
---

- Edge Impulse
- Colab
- Archivos CSV



## **Parámetros** <a name="met"></a>
--- 
1. **Adquisición** 
<p align="justify"> La señal fue obtenida con el Bitalino.En el protocolo, se conectaron tres electrodos de ECG al participante, asegurando un entorno sin interferencias. Se registró la señal con los participantes en reposo y luego de realizar actividad física. Finalmente, se detuvo la grabación para analizar los resultados obtenidos. 

2. **Pre-procesamiento de la data**
<p align="justify">Crear un archivo csv de la señal cruda en reposo y después de realizar actividad física.

<p align="center">
  <img src="img\pre.png"  width="400" height="300"> </p>
  <em><p align="center">Señal cortada</p></em> 

3. **Clasificación de la data**

-   Nivel: 9
-	Familia: Symlet (sym) 3


<p align="center">
  <img src="img\parametros.png"  width="400" height="300"> </p>
  <em><p align="center"> Parámetros utilizados</p></em> 

4. **Edge Impulse - Entrenamiento**

  <p align="center">
  <img src="img\split.png"  width="400" height="300"> </p>
  <em><p align="center">Señal cortada</p></em> 



5. **Obtención del modelo**

<p align="center">
  <img src="img\create_imp.png"  width="400" height="300"> </p>
  <em><p align="center">Creación del impulso</p></em> 

## **Discusión y conclusiones** <a name="disc"></a>
---

<p align="justify">Al finalizar el entrenamiento, obtuvimos un porcentaje de exactitud del 77%, esto se puede deber a que previamente tuvimos datos cargados en el Edge Impulse que no borramos antes de darle a “split”. La 
Por otro lado, la falta de data de entrenamiento afecta a la precisión del modelo, por lo que se podría desarrollar data sintética, a partir de la data obtenida, o ampliar la data de muestreo, para lo cual se deberían obtener más data de los participantes; esto mejoraría la precisión del modelo.
 
<p align="center">
  <img src="img\resultado.png"  width="400" height="300"> </p>
  <em><p align="center">Resultado obtenido después del entrenamiento </p></em>

## **Archivos** <a name="arch"></a>
---
- [Archivos de csv](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2009%20-%20Procesamiento%20de%20EEG/Archivo)



## **Referencias** <a name="ref"></a>
---

[1] We are tinyml (no date) About | tinyML Foundation. Available at: https://www.tinyml.org/about/ (Accessed: 21 November 2023). 

[2] 330ohms (2021) ¿Qué es edge impulse?, 330ohms. Available at: https://blog.330ohms.com/2021/05/19/que-es-edge-impulse/ (Accessed: 20 November 2023). 

