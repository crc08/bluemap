# Bluemap
Feed de triggers curados para BBVA relacionados a edges culturales actualizados en tiempo real.

# Estructura de la herramienta
ETL

# Extract

En la primera etapa se usará la API de Crimson Hexagon para hacer la extracción de datos de Twitter, foros, reddit y blogs.
En una etapa posterior se plantea agregar valor haciendo uso de Scrappers y otras API de noticias o institucionales como feedly, Reddit, Banxico, Inegi entre otros.

Se plantean originalmente 3 monitores de streaming entrenados: Marca, Cultura y Benchmark.

En la primera etapa funcionará exclusivamente con un monitor que analice el sector bancario.


# Transform

Se dividirán el feed entre notas de largo y corto plazo.
Se exportará a un json limpio y enriquecido.
Se analizará el contenido para clasificarlo en edges con una algoritmo de bosques aleatorios.
Se calificarán los contenidos por medio de otro algoritmo de bosques aleatorios o regresión logística para determinar su relevancia.

# Load

En la primera etapa se realizarán las visualizaciones en powerBI
En una etapa posterior se recomienda simular el entorno Honeycomb para facilitar la navegación
Se mostrará el top 10 de temas relevantes al momento.



