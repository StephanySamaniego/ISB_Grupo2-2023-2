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

<p align="justify"> La interfaz es muy amigable y es bastante intuitiva. Según la página oficial puedes implementar tu proyecto en minutos (dejando de lado la etapa de aprendizaje). Para implementar tu proyecto solo tienes que crear tu cuenta, indicar que tipo de proyecto quieres hacer (detección de objetos, reconocimiento de voz, o procesar gestos de un acelerómetro) y hacer la adquisición de datos. Cuando tengas tu dataset puedes crear un Impulse, que es la herramienta que procesará y entrenará el modelo con los datos, para finalmente cargar el modelo a tu microcontrolador.

<p align="center">
  <img src="img\sensors.webp"  width="400" height="200"> </p>
  <em><p align="center">Fig. 1: Flujograma del procesamiento de señales EEG [1].</p></em> 

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

- Nivel: 9
-	Familia: Symlet (sym) 3


<p align="center">
  <img src="img\parametros.png"  width="400" height="300"> </p>
  <em><p align="center"> Parámetros utilizados</p></em> 

4. **Edge Impulse - Entrenamiento**

  <p align="center">
  <img src="img\split.png"  width="400" height="300"> </p>
  <em><p align="center">Señal cortada</p></em> 

<p align="center">
  <img src="img\create_imp.png"  width="400" height="200"> </p>
  <em><p align="center">Creación del impulso</p></em> 

5. **Obtención del modelo**

<p align="center">
  <img src="img\resultado.png"  width="400" height="200"> </p>
  <em><p align="center">Resultado obtenido después del entrenamiento </p></em>

## **Discusión y conclusiones** <a name="disc"></a>
---

<p align="justify">Al finalizar el entrenamiento, obtuvimos un porcentaje de exactitud del 77%, esto se puede deber a que previamente tuvimos datos cargados en el Edge Impulse que no borramos antes de darle a “split”. La 
Por otro lado, la falta de data de entrenamiento afecta a la precisión del modelo, por lo que se podría desarrollar data sintética, a partir de la data obtenida, o ampliar la data de muestreo, para lo cual se deberían obtener más data de los participantes; esto mejoraría la precisión del modelo.
 


## **Archivos** <a name="arch"></a>
---
- [Archivos de csv](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2009%20-%20Procesamiento%20de%20EEG/Archivo)

## **Conclusiones** <a name="conc"></a>
---
- Seguir adecuadamente el proceso de adquisición, filtrado, pre y procesamiento nos permitió extraer las características deseadas.
- El análisis previo de los coeficientes de detalle fue fundamental para la extracción de características.
- Se logró la extracción de las ondas alfa, beta, theta y delta y poder compararlas con la información brindada en la literatura, por ejemplo, el caso de la mayor amplitud.
- Las características de medio, desviación estándar, varianza, valor máximo y mínimo sí van acorde a lo obtenido en las bandas alfa, theta, beta y delta.

## **Referencias** <a name="ref"></a>
---

[1] A. Chaddad, Y. Wu, R. Kateb, and A. Bouridane, “Electroencephalography Signal Processing: A comprehensive review and analysis of methods and Techniques,” Sensors, vol. 23, no. 14, p. 6434, 2023. doi:10.3390/s23146434 

[2] Pham Phuc Ngoc, Vu Duy Hai, Nguyen Chi Bach, and Pham Van Binh, “EEG Signal Analysis and Artifact Removal by Wavelet Transform,” IFMBE proceedings, pp. 179–183, Jan. 2015, doi: https://doi.org/10.1007/978-3-319-11776-8_44. Available: https://link.springer.com/chapter/10.1007/978-3-319-11776-8_44.

[3] W. Amirah and Yin Fen Low, “Feature extraction of electroencephalogram (EEG) signal - A review,” Dec. 2014, doi: https://doi.org/10.1109/iecbes.2014.7047620.

[4] A. R. Mane, S. D. Biradar, and R. K. Shastri, "Review Paper on Feature Extraction Methods for EEG Signal Analysis," International Journal of Emerging Trend in Engineering and Basic Sciences (IJEEBS), vol. 2, no. 1, pp. 545-552, Jan-Feb 2015. . Available: https://www.researchgate.net/profile/Shashank-Biradar/publication/337831914_Review_paper_on_Feature_Extraction_Methods_for_EEG_Signal_Analysis/links/5dee1825299bf10bc34cac5e/Review-paper-on-Feature-Extraction-Methods-for-EEG-Signal-Analysis.pdf . ISSN  2349-6967.

[5] B. Medina, J. Sierra, and A. Ulloa, “Técnicas de extracción de características de señales EEG en la imaginación de movimiento para sistemas BCI Extraction techniques of EEG signals characteristics in motion imagination for BCI systems Contenido,” No22), vol. 39, 2018, Available: https://www.revistaespacios.com/a18v39n22/a18v39n22p36.pdf

[6] L. Cabañero-Gomez, R. Hervas, I. Gonzalez, and L. Rodriguez-Benitez, “eeglib: A Python module for EEG feature extraction,” SoftwareX, vol. 15, p. 100745, Jul. 2021, doi: 10.1016/J.SOFTX.2021.100745.

[7] “Revista Ingeniería,” Udistrital.edu.co, 2023. https://revistas.udistrital.edu.co/index.php/reving/article/view/10968/12577 (accessed Nov. 13, 2023).

[8] J. Satheesh Kumar and P. T. V. Bhuvaneswari, “Analysis of Electroencephalography (EEG) Signals and Its Categorization–A Study,” Procedia Engineering, vol. 38, pp. 2525–2536, Jan. 2012, doi: https://doi.org/10.1016/j.proeng.2012.06.298.