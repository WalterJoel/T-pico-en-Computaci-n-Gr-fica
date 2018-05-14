
**Etapas Importantes**:
Primero se pre-procesa el texto ingresado, quitando caracteres especiales, números, etc,. Una vez limpio el texto se procede a radicalizar los verbos para conseguir la raíz del verbo utilizando el conocido algoritmo de Porter, luego de esto se aplican las formulas que dicta el algoritmo TF/IDF para calcular la relevancia de cada palabra en el texto, finalmente se genera la matriz TF/IDF para cada palabra.

- Para la visualización de las palabras más relevantes, al final se utiliza el WordCloud que fue obtenido desde la página oficial de D3.js y aplicado para este ejemplo

**Estrategias utilizadas**:

- Librería NLTK de python para Quitar los Stopwords 
- Funcion lower() de python para convertir todo el texto a minuscula
- Expresiones regulares para limpiar texto (quitar números y caracteres extraños)
- Algoritmo de Porter para radicalizar los verbos
- Algoritmo TF/IDF para calcular la relevancia que tiene cada palabra en el texto.

**Código dentro de la carpeta Bag of Words**:
- El archivo *aa.py* es el que contiene todo el código de Bag of Words que genera la matriz TF/IDF.
- Dentro de la carpeta *d3-WordCLoud -> Example* se encuentra  un archivo llamado reducido.py que es lo mismo que el archivo aa.py con la única diferencia que este codigo genera una salida que es el *archivo result.js*, el cual es la entrada que recibe el código de wordcloud para generar la visualización de palabras más relevantes.

