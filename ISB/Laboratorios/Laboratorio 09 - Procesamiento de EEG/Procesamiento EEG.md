Laboratorio 9: Procesamiento de EEG 

1. [Introducción](#intro)
2. [Metodología](#met)
3. [Resultados](#resul)
6. [Archivos](#arch)
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
<p align="justify"> La señal fue obtenida con el Ultracortex Mark IV. Herramienta de investigación científicamente validada que le permite adquirir hasta 16 canales de datos EEG y es capaz de muestrear hasta 16 canales de EEG desde hasta 35 ubicaciones diferentes de 10-20. 

2. **Filtrado**
<p align="justify">Durante la adquisición de señales se puede observar la interferencia de diversos artefactos fisiológicos, como los movimientos oculares involuntarios, el parpadeo, la actividad cardíaca y los movimientos musculares, se encuentran presentes en las señales de EEG, comprometiendo así la calidad de las señales obtenidas . Por ello, para eliminar los componentes de parpadeo, implementamos Stationary Wavelet Transform (SWT) de 8 niveles de transformada wavelet discreta no diezmada. Se propone utilizar Wavelet Sym3 que tiene una alta correlación con los artefactos de parpadeo para el algoritmo de cancelación de ruido. Los coeficientes de detalle D1, D8 y A8 son componentes de artefactos que luego se eliminan de las señales [2].

**Nivel: 8** 
-	Familia: Symlet (sym) 3
-	Coeficientes de aproximación: se eliminan de la tabla D1, D8 y A8 (ruidos)


3. **Extracción de características**
<p align="justify">La extracción de características es un proceso mediante el cual se extrae la información o características relevantes de la señal para que las características puedan interpretarse fácilmente. Por lo tanto, es un proceso sustancial en la interpretación de una señal de entrada. El extracto de información refleja la fisiología y anatomía de la actividad que ocurre dentro del cerebro. Implica una serie de variables en un gran conjunto de datos, que requieren una gran cantidad de memoria o un algoritmo potente para analizar los datos. En este contexto, se necesita un método de extracción de características para resolver estas variables o información a interpretar de una manera simple y precisa [3].

**Transformada wavelet**
<p align="justify">La transformada wavelet (WT) puede analizar diversos eventos transitorios en el campo biomédico. Se ha descrito que la WT es adecuada para señales no estacionarias y tiene ventajas sobre el análisis espectral, también es un método eficaz para la representación de la frecuencia temporal de una señal. La característica importante de WT es que proporciona información precisa de frecuencia en las frecuencias bajas e información precisa de tiempo en las frecuencias altas. Esta propiedad es importante en aplicaciones biomédicas, ya que la mayoría de estas señales siempre contienen componentes de alta frecuencia con un periodo de tiempo corto y componentes de baja frecuencia con un periodo de tiempo largo, es por ello que la WT proporciona un análisis multirresolución de señales no estacionarias [4].


<p align="justify">Los métodos temporales usan como características las variaciones temporales de las señales; estos son adaptados particularmente para describir las señales neurofisiológicas con un compás de tiempo preciso y específico. Diversas técnicas estadísticas permiten caracterizar la señal EEG, entre las cuales se encuentran el valor absoluto medio, longitud de onda, cambios en la pendiente de la señal, la integral cuadrada simple, la amplitud de Willison, Kurtosis. Otras técnicas estadísticas como cruce por cero, Varianza, Desviación Estándar, coeficiente de correlación y parámetros de Hjorth son empleadas para extraer características relevantes en la señal de EEG, con el objeto de alcanzar menos complejidad computacional [5].

- Media
- Varianza
- Simetría
- Kurtosis


<p align="center">
  <img src="img\tabla.png"  width="400" height="200"> </p>
  <em><p align="center">Tabla 1: Conjunto de mediciones caracterizando cada latido. Extraído de [9]
</p></em> 






## **Referencias** <a name="ref"></a>
---

[1] A. Chaddad, Y. Wu, R. Kateb, and A. Bouridane, “Electroencephalography Signal Processing: A comprehensive review and analysis of methods and Techniques,” Sensors, vol. 23, no. 14, p. 6434, 2023. doi:10.3390/s23146434 

[2] Pham Phuc Ngoc, Vu Duy Hai, Nguyen Chi Bach, and Pham Van Binh, “EEG Signal Analysis and Artifact Removal by Wavelet Transform,” IFMBE proceedings, pp. 179–183, Jan. 2015, doi: https://doi.org/10.1007/978-3-319-11776-8_44. Available: https://link.springer.com/chapter/10.1007/978-3-319-11776-8_44.

[3] W. Amirah and Yin Fen Low, “Feature extraction of electroencephalogram (EEG) signal - A review,” Dec. 2014, doi: https://doi.org/10.1109/iecbes.2014.7047620.


[4]

[5] B. Medina, J. Sierra, and A. Ulloa, “Técnicas de extracción de características de señales EEG en la imaginación de movimiento para sistemas BCI Extraction techniques of EEG signals characteristics in motion imagination for BCI systems Contenido,” No22), vol. 39, 2018, Available: https://www.revistaespacios.com/a18v39n22/a18v39n22p36.pdf
