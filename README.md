# Development and Comparison of an Algorithm for Blood Pressure Estimation Using the ECG Signal Recorded with a Bitalino (R)EVOLUTION

# Desarrollo y comparación de un Algoritmo para la Estimación de la Presión Arterial Utilizando la Señal ECG Registrada con un Bitalino (R)EVOLUTION


## Tabla de contenidos
1. [Resumen](#Resumen)
2. [Motivación](#Motivación)
3. [Principales hallazgos](#Hallazgos)
4. [Equipo](#Equipo)
5. [Referencias](#Referencias)

## Resumen <a name="Resumen"></a>

<p align="justify">El presente proyecto aborda la necesidad de desarrollar y comparar un algoritmo innovador para la estimación continua y no invasiva de la presión arterial durante procedimientos preoperatorios, utilizando la señal de electrocardiograma (ECG) registrada con el dispositivo BITalino (r)evolution. La monitorización precisa de la presión arterial es fundamental en entornos quirúrgicos y de cuidados intensivos, donde cambios rápidos pueden tener implicaciones críticas para la salud del paciente.

<p align="justify">La investigación comienza con la adquisición de datos de ECG de un grupo diverso de sujetos, buscando representar una amplia variabilidad en términos de presión arterial. Estos datos son sometidos a un proceso de preprocesamiento, que incluye la eliminación de ruido e interferencias, así como la detección y segmentación de las ondas P, QRS y T en la señal ECG. La calidad de la señal es crucial para el éxito del algoritmo, y este paso asegura la fiabilidad de las mediciones. Posteriormente, se extraen características relevantes de la señal ECG, tales como la variabilidad de la frecuencia cardíaca (HRV), la duración de los intervalos RR y la amplitud de las ondas. Estas características son fundamentales para el entrenamiento de un modelo de aprendizaje automático, que busca establecer una relación entre las características del ECG y las mediciones de presión arterial conocidas.

<p align="justify">El modelo se entrena utilizando un conjunto de datos sacados de la base de datos VitalDB, que incluye mediciones de presión arterial correspondientes a las señales de ECG asociadas de pacientes preoperatorios. Se exploran diversos enfoques de aprendizaje automático, como máquinas de soporte vectorial y redes neuronales, evaluando su capacidad para predecir la presión arterial con precisión. 

<p align="justify">La validación del modelo es esencial para evaluar su rendimiento en un conjunto de datos independiente. Se utilizan métricas como el error absoluto medio y el error cuadrático medio para cuantificar la precisión de las predicciones. Los resultados de esta fase son cruciales para ajustar el algoritmo y mejorar su capacidad predictiva.




## Motivación <a name="Motivación"></a>

<p align="justify">La mejoría de la monitorización médica mediante el desarrollo de un algoritmo preciso y comparación de parámetros para la estimación de la presión arterial contribuirá a la detección temprana de cambios en la presión arterial, permitiendo una intervención médica oportuna, especialmente en entornos perioperatorios y de cuidados intensivos. Además, el trabajo podría ser impulsado por el deseo de innovar en el campo de la tecnología médica, explorando nuevas formas de utilizar dispositivos como el Bitalino (r)evolution para mejorar la atención médica y hacerla más accesible. Por otro lado, el reducir la necesidad de métodos invasivos para la medición de la presión arterial, como la canulación arterial, que conlleva riesgos y complicaciones podría mejorar la seguridad y comodidad de los pacientes. 
Es por ello que, como grupo, tuvimos el compromiso de llevar a cabo este proyecto siguiendo todo lo mencionado previamente.

## Principales hallazgos <a name="Hallazgos"></a>


En el año 2020, en el Perú se llevaron a cabo un total de 4,452 cirugías en pacientes menores de 5 años, según datos del MINSA. El grupo más representativo fue el de niños de un año, que constituyó el 19% del total con 846 cirugías, seguido por los niños de dos años con 668 cirugías, representando el 15% [3]. En el Instituto Nacional de Salud del Niño (INSN) de Breña, se realizaron más de 49,816 cirugías en pacientes menores de 18 años entre 2015 y 2019. De estas cirugías, más del 40% se realizaron en niños de 1 a 4 años, lo que destaca este grupo de edad como un área de interés debido a su contribución significativa al total de intervenciones realizadas[4]–[8]. 

## [Conoce al equipo](hhttps://github.com/StephanySamaniego/ISB_Grupo2-2023-2/blob/main/ISB/Proyecto/Entregable%201/presentaci%C3%B3n.md) <a name="Equipo"></a>


## Referencias <a name="Referencias"></a>

‌[1]Africa:, “Cardiovascular Journal of Africa: Vol 32 No 5 (SEPTEMBER/OCTOBER 2021),” Cvja.co.za, 2021. Available: https://cvja.co.za/onlinejournal/vol32/vol32_issue5/46/. 
‌

[2] Santoshi Nerella, Uttam Kumar Sarkar, and Hema Namdeo, “Electrocardiographic and echocardiographic findings in children with dengue infection,” Journal of family medicine and primary care, vol. 11, no. 6, pp. 2334–2334, Jan. 2022, doi: https://doi.org/10.4103/jfmpc.jfmpc_1280_21. Available: https://journals.lww.com/jfmpc/fulltext/2022/06000/electrocardiographic_and_echocardiographic.11.aspx. 

[3] M. de S. del Perú, “DIAGNOSTICOS DE EGRESO DE NIÑOS MENORES DE 5 AÑOS POR
ESPECIALIDAD MEDICA - AÑO 2020”, Ministerio de Salud del Perú, sep. 2020.

[4] O. de Epidemiología y U. de I. Epidemiologica, “Análisis Situacional de los Servicios de Salud
INSN”, Instituto Nacional de Salud del Niño, 2015.

[5] O. de Epidemiología y U. de I. Epidemiologica, “Análisis Situacional de los Servicios de Salud
INSN”, Instituto Nacional de Salud del Niño, 2016.

[6] O. de Epidemiología, U. de I. Epidemiologica, y A. S. de los S. de Salud, “Análisis Situacional de los
Servicios de Salud INSN”, Instituto Nacional de Salud del Niño, 2017.

[7] O. de Epidemiología y U. de I. Epidemiologia, “Análisis Situacional de los Servicios de Salud INSN
Tomo 1”, Instituto Nacional de Salud del Niño, 2019.

[8] O. de Epidemiología y U. de I. Epidemiologica, “Análisis Situacional de los Servicios de Salud INSN
Tomo 1”, Instituto Nacional de Salud del Niño, 2018.