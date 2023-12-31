# Laboratorio 9: Procesamiento de EEG 

1. [Introducción](#intro)
2. [Metodología](#met)
3. [Resultados](#resul)
4. [Discusiones](#disc)
5. [Archivos](#arch)
6. [Conclusiones](#conc)
7. [Referencias](#ref)


## **Introducción** <a name="intro"></a>
---
**Electroenceralograma**
<p align="justify"> El EEG es una técnica neurofisiológica utilizada para medir y cuantificar la actividad neuronal en diversas regiones del cerebro, el cual está compuesto por numerosas neuronas cuyas actividades generan distintos potenciales en el cuero cabelludo, se producen señales en distintos estados, como alerta, respuesta a estímulos externos y otros factores únicos de cada individuo[1]. 

<p align="center">
  <img src="img\sensors.webp"  width="400" height="200"> </p>
  <em><p align="center">Fig. 1: Flujograma del procesamiento de señales EEG [1].</p></em> 

## **Objetivos** 
---
- Analizar la señal EEG después del procesamiento
- Extraer las características de una señal EEG


## **Metodología EEG** <a name="met"></a>
--- 
1. **Adquisición** 
<p align="justify"> La señal fue obtenida con el Bitalino.En el protocolo, se conectaron tres electrodos de EEG al participante, asegurando un entorno sin interferencias. Se registró una línea base de 10 segundos y fases de ojos abiertos/cerrados. Se repitió el ciclo y se añadió la resolución de ejercicios matemáticos mientras se grababan los datos. Finalmente, se detuvo la grabación para analizar los resultados obtenidos. 

2. **Filtrado**
<p align="justify">Durante la adquisición de señales se puede observar la interferencia de diversos artefactos fisiológicos, como los movimientos oculares involuntarios, el parpadeo, la actividad cardíaca y los movimientos musculares, se encuentran presentes en las señales de EEG, comprometiendo así la calidad de las señales obtenidas . Por ello, para eliminar los componentes de parpadeo, implementamos Stationary Wavelet Transform (SWT) de 8 niveles de transformada wavelet discreta no diezmada. Se propone utilizar Wavelet Sym3 que tiene una alta correlación con los artefactos de parpadeo para el algoritmo de cancelación de ruido. Los coeficientes de detalle D1, D8 y A8 son componentes de artefactos que luego se eliminan de las señales [2].

**Caraceterísticas del filtro**
- Nivel: 8
-	Familia: Symlet (sym) 3
-	Coeficientes de aproximación: se eliminan de la tabla D1, D8 y A8 (ruidos)

<p align="center">
  <img src="img\tabla.png"  width="400" height="200"> </p>
  <em><p align="center">Tabla 1: Descomposición y adquisición de señales EEG después de la SWT nivel 8 de la Transformada de Wavelet </p></em> 



3. **Extracción de características**
<p align="justify">La extracción de características es un proceso mediante el cual se extrae la información o características relevantes de la señal para que las características puedan interpretarse fácilmente. Por lo tanto, es un proceso sustancial en la interpretación de una señal de entrada. El extracto de información refleja la fisiología y anatomía de la actividad que ocurre dentro del cerebro. Implica una serie de variables en un gran conjunto de datos, que requieren una gran cantidad de memoria o un algoritmo potente para analizar los datos. En este contexto, se necesita un método de extracción de características para resolver estas variables o información a interpretar de una manera simple y precisa [3].

**Transformada wavelet**
<p align="justify">La transformada wavelet (WT) puede analizar diversos eventos transitorios en el campo biomédico. Se ha descrito que la WT es adecuada para señales no estacionarias y tiene ventajas sobre el análisis espectral, también es un método eficaz para la representación de la frecuencia temporal de una señal. La característica importante de WT es que proporciona información precisa de frecuencia en las frecuencias bajas e información precisa de tiempo en las frecuencias altas. Esta propiedad es importante en aplicaciones biomédicas, ya que la mayoría de estas señales siempre contienen componentes de alta frecuencia con un periodo de tiempo corto y componentes de baja frecuencia con un periodo de tiempo largo, es por ello que la WT proporciona un análisis multirresolución de señales no estacionarias [4].


<p align="justify">Los métodos temporales usan como características las variaciones temporales de las señales; estos son adaptados particularmente para describir las señales neurofisiológicas con un compás de tiempo preciso y específico. Diversas técnicas estadísticas permiten caracterizar la señal EEG, entre las cuales se encuentran el valor absoluto medio, longitud de onda, cambios en la pendiente de la señal, la integral cuadrada simple, la amplitud de Willison, Kurtosis. Otras técnicas estadísticas como cruce por cero, Varianza, Desviación Estándar, coeficiente de correlación y parámetros de Hjorth son empleadas para extraer características relevantes en la señal de EEG, con el objeto de alcanzar menos complejidad computacional [5].

- Extracción de la banda Theta
- Extracción de la banda Delta
- Extracción de la banda Alfa
- Extracción de la banda Beta
- Valor máximo
- Valor mínimo
- Amplitud
- Valor medio
- Media
- Varianza
- Desviación Estándar


## **Resultados** <a name="resul"></a>
--- 
**Procesamiento y obtención de características de EEG**
Se tendrá en cuenta los siguientes parámetros para la obtención de las características deseadas:
Filtros generados para la adquisición de las características, usaando un filtro de pasa alta y un filtro pasabaja, lo que nos da un rango de 0.5 a 50 Hz
Tiempo de muestreo 20 seg
Para la extracción de características se identificarán las bandas theta (1-4 Hz), delta (4-7 Hz), alfa (8-12 Hz) y beta (12-30 Hz) [6]

Al realizar la extracción de los valores de los valores máximos y mínimos, así como la amplitud, media, valor medio, desviación estándar y variación se usa la librería numpy para obtener los valores [7]. Donde la media, varianza y desviación estándar están dadas por las siguientes expresiones matemáticas, siendo Cj,ki.los coeficientes de Wavelet.

<p align="center">
  <img src="img\formulas.png" width="500" height="100"> </p>


-   **Señal original**
<p align="center">
  <img src="https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/Dise%C3%B1o/Laboratorio_07/eeg.png?raw=true"  width="500" height="250"> </p>

- **Señal filtrada**

<p align="center"><img src="img\EEG_filtrado.png" width="600" height="300"  ></p>

<p align="justify">Podemos observar patrones específicos de la señal filtrada , como los picos de onda, ritmos específicos (como el ritmo alfa o delta) y eventos relacionados con la actividad cerebral.

<p align="center"><img src="img\EEG_Wavelet_1.png" width="600" height="300"  ></p>
<p align="center"><img src="img\EEG_Wavelet_2.png" width="600" height="300"  ></p>

- **Características generales**
<p align="center"><img src="img\valores_extracción_características.png" width="500" height="200" ></p>

- **Extracción de bandas**
<div align='center'>

|Banda Theta|Banda Delta|
|-----------|------------|
|<p align="center"><img src="img\Banda_teta.png" width="400" height="200" ></p>|<p align="center"><img src="img\Banda_delta.png" width="400" height="200" ></p>|

|Banda Alfa|Banda Beta|
|-----------|------------|
|<p align="center"><img src="img\Banda_alfa.png" width="400" height="200" ></p>|<p align="center"><img src="img\Banda_beta.png" width="400" height="200" ></p>|

</div>

## **Discusiones** <a name="disc"></a>
---
- **Banda theta**

<div align='center'>

|||
|-----------|------------|
|<p align="center"><img src="img\Banda_teta.png" width="400" height="200" ></p>|<p align="center"><img src="img\theta.png" width="400" height="200" ></p><em><p align="center">Banda Theta extraído de[8] </p></em> |
<p align="justify">Este tipo de onda se observa cuando la persona se encuentra en un estado de relajación o meditación, lo cual podría ser equivalente al estado de reposo antes del cierre y abrir de ojos, aún así no es tan común en los adultos. Se puede ver una diferencia notable entre ambas imágenes, la del sujeto a prueba presenta una línea creciente, mentiras que el otro presenta fluctuaciones.

</div>

- **Banda delta**

<div align='center'>

|||
|-----------|------------|
|<p align="center"><img src="img\Banda_delta.png" width="400" height="200" ></p>|<p align="center"><img src="img\delta.png" width="400" height="200" ></p></p><em><p align="center">Banda Delta extraído de[8] </p></em>|
<p align="justify">La onda delta es la más grande en amplitud y a la vez la más lenta, son raras cuando los adultos están despiertos, en este caso con los ojos abiertos. En la imagen del sujeto se puede observar que el pico máximo de la onda es más de 450 uV, lo cual coincide con la literatura de que tiene la amplitud más alta.
</div>

- **Banda alfa**

<div align='center'>

|||
|-----------|------------|
|<p align="center"><img src="img\Banda_alfa.png" width="400" height="200" ></p>|<p align="center"><img src="img\alfa.png" width="400" height="200" ></p></p><em><p align="center">Banda Alfa extraído de[8] </p></em>|
<p align="justify">La onda alfa se encuentra en todos los casos, también cuando la persona está despierta, pero se encuentra con los ojos cerrados. Es el puente entre lo consciente y lo subconsciente. Ocurre en ambos lados de la cabeza, pero tiene una amplitud ligeramente mayor en el lado dominante y se registra en las regiones occipital y parietal del cerebro.
</div>

- **Banda beta**

<div align='center'>

|||
|-----------|------------|
|<p align="center"><img src="img\Banda_beta.png" width="400" height="200" ></p>|<p align="center"><img src="img\beta.png" width="400" height="200" ></p></p><em><p align="center">Banda Beta extraído de[8] </p></em>|
<p align="justify">Las ondas betas están bastante relacionadas con lo que la persona mira, siente, toca, oye, huele y prueba, lo cual podría estar relacionado a cuando el sujeto mira fijamente a un punto de concentración mientras escucha, analiza y responde las preguntas realizadas por otra persona. Además, estas ondas se producen en estado consciente como hablar, resolver problemas o tomar decisiones, lo cual está bastante relacionado al caso del sujeto. Comparando las imágenes, se puede observar que las ondas siguen ciertos patrones con fluctuaciones muy notorias en ambas. 
</div>

## **Archivos** <a name="arch"></a>
---
- [Códigos para procesar la señal en Python](https://github.com/StephanySamaniego/ISB_Grupo2-2023-2/tree/main/ISB/Laboratorios/Laboratorio%2009%20-%20Procesamiento%20de%20EEG/Archivo)

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