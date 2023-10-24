# Laboratorio 6: Procesamiento de EMG 

1. [Introducción](#intro)
2. [Metodología](#met)
3. [Resultados](#resul)
6. [Conclusiones](#conclu)
7. [Referencias](#ref)


## **Introducción** <a name="intro"></a>
---
**Extracción de características de un EMG**
<p align="justify">La señal de electromiografía (EMG) es una indicación eléctrica de la actuación neuromuscular relacionada con un músculo en contracción. Es un signo extremadamente complicado que está influenciado por las propiedades anatómicas y fisiológicas de los músculos, el sistema de control del sistema sensorial marginal y también las características de la instrumentación que se utiliza para identificarlo y observarlo. La mayoría de las conexiones entre la señal EMG y las propiedades de un músculo en contracción que se utilizará rápidamente se han desarrollado de forma fortuita. La ausencia de una representación adecuada de la señal EMG es probablemente la variable más notable que ha obstaculizado el desarrollo de la EMG hasta convertirla en un campo específico [1].

<p align="justify">En general el proceso se rige por las etapas de adquisición de datos, procesamiento de señal, extracción y clasificación de características de señal y funciones de predicción. Cada una de las etapas varía dependiendo los parámetros de diseño, como costo de elaboración y porcentaje de asertividad [2]

## **Metodología EMG** <a name="met"></a>
--- 
1. **Adquisición** 
<p align="justify"> La adquisición de señales biomédicas es una herramienta fundamental en la evaluación de pacientes con patologías, e incluso, en la evaluación del rendimiento deportivo. En el mismo contexto, el uso de la electromiografía de superficie (EMGs) ha permitido fortalecer los esquemas de tratamiento convencionales, pesquisando posibles modificaciones musculoesqueléticas vinculadas al tiempo de activación, coactivación, patrones de activación, entre otros [3].
En la adquisición de las señales de sEMG es posible distinguir las siguientes etapas: pre-amplificación, filtrado y la etapa de conversión de analógico a digital [4].

<p align="center">
  <img src="Img\tabla.png"  width="400" height="200"> </p>
  <em><p align="center">Tabla 1: Características de sEMG y EMG invasiva [4]</p></em> 

2. **Filtrado**
<p align="justify">La señal proveniente de la etapa de pre-amplificación contiene una mezcla de señales biológicas y ruido del ambiente, es por esta razón que se requiere depurar o filtrar la información.  Para descartar interferencias originadas por fuentes electromagnéticas de 50Hz, generalmente se utiliza un filtro Butterworth de orden 2 con frecuencia de bloqueo entre 49 y 51 Hz [5]. Adicionalmente, la señal debe ser filtrada con un paso de banda de 20 a 400 Hz para eliminar los artefactos producidos por los movimientos del electrodo y la piel del paciente [6]. Los parámetros que utilizaremos son los siguientes:

- Filtro paso alto con frecuencia de corte entre 10 – 20 Hz.
- Filtro paso bajo con frecuencia de corte entre 400 – 450 Hz.


3. **Rectificación**
<p align="justify">La técnica más común de detección de la amplitud de EMG es la rectificación seguida de una etapa de suavizado. Consiste en obtener el valor absoluto de la señal cruda. La rectificación puede ser de dos tipos: de media onda, donde se excluyen los valores negativos y únicamente se consideran los valores positivos; o de onda completa, en la que se obtiene el valor absoluto de todos los valores, incluyendo los negativos [5]. 

<p align="center">
  <img src="Img\rectificación3.png"  width="400" height="200"> </p>
  <em><p align="center">Figura 1: Rectificación y filtrado de una señal EMG en el dominio de la frecuencia [7]</p></em> 

4. **Suavización**
<p align="justify">Este procedimiento es útil cuando se requiere realizar estudios de amplitud. El suavizado elimina o reduce significativamente los picos indeseados y extrae la tendencia de la señal. Uno de los métodos más utilizados es el Root mean-squared (RMS), el cual es la raíz cuadrada de la potencia promedio de una señal EMG en un intervalo de tiempo específico. Se denomina "variable en el dominio del tiempo" porque muestra cómo cambia la amplitud de la señal a lo largo del tiempo. El tamaño del segmento suele situarse entre 50-100 ms dependiendo del tipo de movimiento [5].

5. **Extracción de características**
<p align="justify">La extracción de características consiste en obtener información relevante de la  señal de sEMG mediante una transformación de los datos originales, de esta transformación se obtiene el vector de características o Feature Vector (FV). Existen tres tipos de características para la señal de EMG: las características en el dominio del tiempo, en el dominio de la frecuencia y en el dominio de tiempo frecuencia [4].
Esta característica de la señal puede brindarnos información de la actividad muscular, el nivel de fatiga muscular, detección de patrones anormales, así como una evaluación de coordinación muscular [8].

- 

<p align="center">
  <img src="Img\procedimiento.png"  width="400" height="200"> </p>
  <em><p align="center">Fig. 2: Sistema de control mioeléctrico basados en reconocimiento de patrones</p></em> 

## **Resultados** <a name="met"></a>
--- 

1. **Filtrado**

|Señal Cruda | Espectro de frecuencia|
|-------------|-------------|
| <img src="Img\ssin_filtrar.jpg"  width="300" height="300">  | <img src="Img\fft_cruda.jpg"  width="300" height="300">  |

- **Filtro Notch**

|Señal filtrada  | Espectro de frecuencia | Espectro de frecuencia |
|-------------|-------------|-------------|
| <img src="Img\senal_filtrada.jpg"  width="300" height="300">   |<img src="Img\filtro_notch.jpg"  width="300" height="300"> |<img src="Img\filtro_notch_2.jpg"  width="300" height="300"> |

- **Filtro pasabanda**

|Señal filtrada  | Espectro de frecuencia |
|-------------|-------------|
| <img src="Img\sfiltrada_pasab.jpg"  width="300" height="300">  |<img src="Img\fft_pasabanda.jpg"  width="300" height="300">  |






## **Conclusiones** <a name="conclu"></a>
---
Tras observar el filtrado en cada respectiva señal (EEG, EMG y ECG), llegamos a la conclusión de que el filtrado Wavelet es el que mejor ha resultado debido a que no realizan una atenuación muy grande a la señal, por ello, se pueden realizar las distintas mediciones y extracciones de características necesarias para el análisis estadístico u otros y poder analizarlos mejor para un diagnóstico más pertinente de la salud del paciente.



## **Referencias** <a name="ref"></a>
---
[1] J. G. Proakis and D. G. Manolakis, "Digital Signal Processing," 4th ed., Prentice Hall, Madrid, 1998.

[2] Niyan Marchon, “Efficient FIR Filters for Biomedical Signals,” Oct. 2019, doi: https://doi.org/10.1109/tencon.2019.8929397. Available: https://ieeexplore.ieee.org/document/8929397. [Accessed: Oct. 21, 2023]
[3] D. Yue and H. Liu, “The Design Of Intelligent Filter For EEG,” MATEC Web of Conferences, vol. 232, p. 04023, 2018, doi: https://doi.org/10.1051/matecconf/201823204023

[4] C. J. Kikkert, “A Phasor Measurement Unit Algorithm Using IIR Filters for FPGA Implementation,” Electronics, vol. 8, no. 12, pp. 1523–1523, Dec. 2019, doi: https://doi.org/10.3390/electronics8121523. Available: https://www.mdpi.com/2079-9292/8/12/1523. [Accessed: Oct. 21, 2023]

[5] “IEEE Xplore Full-Text PDF”:, Ieee.org, 2023. Available: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8944069. [Accessed: Oct. 21, 2023]


[6] M. Sharma, Abhinav Dhere, Ram Bilas Pachori, and U. Rajendra Acharya, “An automatic detection of focal EEG signals using new class of time–frequency localized orthogonal wavelet filter banks,” Knowledge Based Systems, vol. 118, pp. 217–227, Feb. 2017, doi: https://doi.org/10.1016/j.knosys.2016.11.024. Available: https://www.sciencedirect.com/science/article/abs/pii/S0950705116304816. [Accessed: Oct. 21, 2023]


[7] Novel Applications of Wavelet Transforms based Side-Channel Analysis - Scientific Figure on ResearchGate. Available from: https://www.researchgate.net/figure/Wavelet-transform-illustration_fig1_265359018 [accessed 21 Oct, 2023]

[8] Pham Phuc Ngoc, Vu Duy Hai, Nguyen Chi Bach, and Pham Van Binh, “EEG Signal Analysis and Artifact Removal by Wavelet Transform,” IFMBE proceedings, pp. 179–183, Jan. 2015, doi: https://doi.org/10.1007/978-3-319-11776-8_44. Available: https://link.springer.com/chapter/10.1007/978-3-319-11776-8_44. [Accessed: Oct. 21, 2023]


[9] F. A. Alturki, Khalil AlSharabi, A. M. Abdurraqeeb, and Majid Aljalal, “EEG Signal Analysis for Diagnosing Neurological Disorders Using Discrete Wavelet Transform and Intelligent Techniques,” Sensors, vol. 20, no. 9, pp. 2505–2505, Apr. 2020, doi: https://doi.org/10.3390/s20092505. Available: https://www.mdpi.com/1424-8220/20/9/2505. [Accessed: Oct. 21, 2023]


[10] A. Mahabub, “Design and implementation of cost-effective IIR filter for EEG signal on FPGA,” Australian Journal of Electrical and Electronics Engineering, vol. 17, no. 2, pp. 83–91, Apr. 2020, doi: https://doi.org/10.1080/1448837x.2020.1771662


[11] “VisibleBreadcrumbs,” Mathworks.com, 2023. Available: https://www.mathworks.com/help/signal/ug/iir-filter-design.html. [Accessed: Oct. 21, 2023]

[12] M. Felja, A. Bencheqroune, M. Karim, and G. B. Limas, “Removing Artifacts From EEG Signal Using Wavelet Transform and Conventional Filters,” WSEAS TRANSACTIONS ON INFORMATION SCIENCE AND APPLICATIONS, vol. 17, pp. 177–183, Feb. 2021, doi: https://doi.org/10.37394/23209.2020.17.22

[13] Different types of filters that can be used to shape...,” ResearchGate, 2020. Available: https://www.researchgate.net/figure/A-Different-types-of-filters-that-can-be-used-to-shape-the-EMG-spectrum-to-keep_fig14_344666810. [Accessed: Oct. 21, 2023]

[14]  Z. Xiao, J. Ye, H. Shen, S. Deng, H. Zhu, and X. Han, “Analysis of Digital Filtering Design Based on Surface EMG Signals,” Apr. 2023, doi: https://doi.org/10.1109/iceib57887.2023.10170168. Available: https://ieeexplore.ieee.org/abstract/document/10170168?casa_token=Epyu1ipDXccAAAAA:7rlxsFaoju_vAGk2qw3lHHTWjA4M3CqbL4Zv8GCiZkDgcqpy-HZK7CE1PP_oC7WmdW1RyvUV. [Accessed: Oct. 21, 2023]

[15] Rodrigo Lício Ortolan, R. Mori, R. Pereira, C. Maria, José Carlos Pereira, and A. Cliquet, “Evaluation of adaptive/nonadaptive filtering and wavelet transform techniques for noise reduction in EMG mobile acquisition equipment,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 11, no. 1, pp. 60–69, Mar. 2003, doi: https://doi.org/10.1109/tnsre.2003.810432. Available: https://ieeexplore.ieee.org/abstract/document/1200908?casa_token=EQtC1icvSZ8AAAAA:ALAVecBpqkWB45PHzRZa67EUAgCX_0tw3rL67tK0OeG_8t-3ARPz2vo5UE_2YrksVrg7tC2v. [Accessed: Oct. 21, 2023]

[16]   	S. Chatterjee, R. S. Thakur, R. N. Yadav, L. Gupta, and D. K. Raghuvanshi, “Review of noise removal techniques in ECG signals,” IET Signal Processing, vol. 14, no. 9, pp. 569–590, Dec. 2020, doi: 10.1049/IET-SPR.2020.0104.

[17]   	N. Manjula, N. P. Singh, and P. A. Babu, “An Efficient Designing of IIR Filter for ECG Signal Classification Using MATLAB,” Engineering Proceedings 2023, Vol. 34, Page 24, vol. 34, no. 1, p. 24, Mar. 2023, doi: 10.3390/HMAM2-14154.

[18] 	R. Oshana, “Overview of DSP Algorithms,” DSP for Embedded and Real-Time Systems, pp. 113–131, Jan. 2012, doi: 10.1016/B978-0-12-386535-9.00007-X.

[19] 	“Diseño de filtros FIR - MATLAB & Simulink - MathWorks América Latina.” Accessed: Oct. 19, 2023. [Online]. Available: https://la.mathworks.com/help/signal/ug/fir-filter-design.html

[20] 	S. Gopal, A. P. Gawande, K. B. Khanchandani, and T. P. Marode, “PERFORMANCE ANALYSIS OF FIR DIGITAL FILTER DESIGN TECHNIQUES,” vol. 2, 2012, Accessed: Oct. 19, 2023. [Online]. Available: http://www.ijccr.com

[21]   	I. Jahan and O. Sarker, “A Lower Transition Width FIR Filter & its Noise Removal Performance on an ECG Signal,” Oct. 2017.

[22]   	J. D. Broesch, “Digital Filters,” Digit Signal Process, pp. 101–123, 2009, doi: 10.1016/B978-0-7506-8976-2.00006-7.

[23]   	S. M. Alessio, “IIR Filter Design,” pp. 263–367, 2016, doi: 10.1007/978-3-319-25468-5_8.

[24]   	“Diseño de filtros IIR - MATLAB & Simulink - MathWorks América Latina.” Accessed: Oct. 19, 2023. [Online]. Available: https://la.mathworks.com/help/signal/ug/iir-filter-design.html?s_tid=mwa_osa_a

[25]   	Dr. R. Mehra, “Analysis of Different IIR Filter based on Implementation Cost Performance,” International Journal of Engineering and Advance Technology, vol. 3, pp. 267–270, Oct. 2014.

[26]   	G. Gupta and R. Mehra, “Design Analysis of IIR Filter for Power Line Interference Reduction in ECG Signals,” 2013.

[27]   	U. Seljuq, F. Himayun, and H. Rasheed, “Selection of an optimal mother wavelet basis function for ECG signal denoising,” 17th IEEE International Multi Topic Conference: Collaborative and Sustainable Development of Technologies, IEEE INMIC 2014 - Proceedings, pp. 26–30, 2014, doi: 10.1109/INMIC.2014.7096905.