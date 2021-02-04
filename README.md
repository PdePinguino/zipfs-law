# ¿Cuáles son las palabras más frecuentes en "Hijo de Ladrón"?

El siguiente código tiene por objetivo ilustrar la frecuencia de palabras que componen esta novela.

Puede utilizarse el mismo código para otros textos. Solo se requiere el archivo en formato txt.

Para utilizar este repositorio:
```
git clone https://github.com/PdePinguino/zipfs-law.git
cd zipfs-law
./zipf_law.py -t hijo_de_ladron.txt
```
Si se quiere analizar otro texto, entonces
```
./zipf_law.py -t [mi_texto.txt]
```

Los argumentos disponibles son:\
`-t TEXT, --text TEXT` archivo que será analizado.\
`-r, --remove_stop_words` remover o no stop words dadas por `nltk.corpus` para español.\
`-p, --plot` plotear o no los resultados.\
`-v, --verbose` imprimir en consola detalles del proceso.

## Libraries
numpy==1.16.4
nltk==3.4.4
matplotlib==3.1.0

## Pre-procesamiento

Antes de calcular la frecuencia de palabras, es necesario leer el archivo en formato txt y eliminar aquello que no se analizará.
El código de `preprocessing.py` se encarga de:
- convertir mayúsculas en minúsculas.
- eliminar puntuación y caracteres que no sean letras.
- (opcional) remover stop words del español ('de', 'a', 'tu'...).
- (opcional) lematizar (reducir palabras a su forma base). TODO
- (opcional) radicalizar (stemming) (reducir palabras a su raíz). TODO

## Frecuencias

Una vez obtenida la lista de palabras a considerar, se genera un diccionario que cuenta las instancias de cada palabra.\
Para esto, se cuenta cuántas veces la misma palabra está contenida en la lista.\\
En este análisis, las decisiones del pre-procesamiento son importantes ya que nuestros resultados serán distintos según qué estamos contando.\\
La pregunta que está en cuestión es qué estamos contando (¿contamos palabras?) y cómo las contamos. ¿Debemos considerar los siguientes pares de palabras como correspondientes a una misma palabra?\\
"hijo" - "hijos" (singular - plural)\
"corrimos" - "correremos" (distintos tiempos verbales y/o modos)\
"tierra" - "tierra" (distinto significado pero igual escritura: la "tierra" entendida como "planeta" y entendida como "suelo")\

## Análisis: Frecuencia de palabras con y sin stop words

Cuando nos fijamos en la frecuencia de las palabras, vemos que muy pocas palabras aparecen gran cantidad de veces, y muchas palabras aparecen muy pocas veces. Es decir, si graficamos cada palabra del texto en el eje x y su frecuencia en el eje y, entonces obtenemos lo siguiente:

![freq_allwords_30](https://user-images.githubusercontent.com/76110750/106389944-ced90100-63c4-11eb-9ab6-bc9a24a2ef93.png)

La frecuencia detallada de las 10 palabras más frecuentes está mostrada en la columna izquierda de la siguiente tabla. Podemos ver cómo 'de' es la palabra más utilizada con 9.050 apariciones. Cuando nos percatamos de las palabras, no hay mucho de característico en ellas que remita al texto que estamos analizando. Si comparamos las 10 palabras más frecuentes con la novela "Cien años de soledad" de Gabriel García Márquez (columna derecha), obtenemos el siguiente resultado (en negrita están las palabras repetidas en ambas novelas: 8 palabras son las mismas con más alta frecuencia).

| Palabra | Frecuencia | Palabra | Frecuencia |
| --- | --- | --- | --- |
**'de'**| 9050 | 'de' | 8859
**'y'**| 8413 | 'la' | 6115
**'que'**| 6294 | 'que' | 4683
**'la'**| 5321 | 'y' | 4149
**'el'**| 4849 | 'el' | 4057
**'a'**| 4358 | 'en' | 3885
**'en'**| 4042 | 'a' | 3166
'no'| 4014 | 'los' | 2377
'un'| 3124 | 'se' | 2155
**'se'**| 2797 | 'con' | 1985

Y si vemos el gráfico para "Cien años de soledad", la curvatura sigue una tendencia similar.

![ggm_freqallwords_30](https://user-images.githubusercontent.com/76110750/106954366-6ebec380-6712-11eb-890b-40e055488fa3.png)

Pero si removemos stop-words, entonces vemos que la frecuencia cae considerablemente (cerca de 9.000 a menos de 1.000) y las palabras pueden generar más sentido según el texto que estamos analizando. Esta vez, ninguna palabra está repetida en ambos textos. El ávido lector podrá distinguir qué columna corresponde a qué novela.

| Palabra | Frecuencia | Palabra | Frecuencia |
| --- | --- | --- | --- |
si | 789 | aureliano | 796
hombre | 656 | úrsula | 512
hacia | 526 | arcadio | 480
allí | 420 | casa | 463
dos | 412 | josé | 438
vez | 384 | buendía | 411
ser | 328 | años | 357
después | 322 | coronel | 312
podía | 314 | amaranta | 310
hombres | 300 | segundo | 309

## Análisis: Frecuencia de la frecuencia de palabras

Hasta aquí hemos visto lo que ocurre con las primeras 30 palabras, pero si graficamos qué ocurre con todas las palabras, obtenemos la siguiente curva de frecuencias. Si removemos stop words, entonces la curva se ve levemente menos pronunciada, pero característicamente bajo el mismo fenómeno: pocas palabras aparecen muchas veces, muchas palabras aparecen pocas veces.

![freq_allwords](https://user-images.githubusercontent.com/76110750/106389937-ca144d00-63c4-11eb-9d4f-2912267fd272.png)

![freq_allwords_wsw](https://user-images.githubusercontent.com/76110750/106955660-49cb5000-6714-11eb-9fe0-e8e06109ba6f.png)

Puedes revisar si lo mismo ocurre para la novela "Cien años de soledad": `./zipfs_law.py -t cien_años_de_soledad.txt -p`

Si contamos la frecuencia de la frecuencia, es decir, cuántas palabras ocurren más de 1.000 veces, cuántas ocurren entre 999 y 500, entre 499 y 200, entre 199 y 100, entre 99 y 50, entre 49 y 10, y menos de 10, obtenemos el siguiente resultado.

| Palabras que ocurren... | Frecuencia |
| --- | --- | 
|más de 5000 | 4| 
|entre 5000 y 1000| 21|
|entre 1000 y 500 | 15|
|entre 500 y 200| 72|
|entre 200 y 100| 103|
|entre 100 y 50| 221|
|entre 50 y 10| 1721|
|menos de 10| 9974|

![freq_of_freq](https://user-images.githubusercontent.com/76110750/106397292-65201d80-63eb-11eb-800b-b86f8ab3968f.png)

## Ley de Zipf

¿Y dónde entra la ley de Zipf? La ley de Zipf describe la frecuencia de aparición de las palabras en una lengua. Las palabras aparecen proporcionalmente según el ranking de frecuencia. Esto quiere decir que, suponiendo que la primera palabra aparece 1.000 veces, la primera aprecerá 1/1 * 1.000, la segunda aparecerá 1/2 * 1.000, la tercera 1/3 * 1.000, la cuarta 1/4 * 1.000, y así sucesivamente.

Si graficamos la distribución actual de palabras junto a la distribución de Zipf, vemos que ambas coinciden, si bien no son exactas.

![text_zipfs_distribution](https://user-images.githubusercontent.com/76110750/106959336-4a1a1a00-6719-11eb-8ab4-85f694fb7b10.png)

## Créditos
El texto "Hijo de ladrón" de Manuel Rojas ha sido extraído desde https://www.escritores.cl/libros_gratis/hijo%20de%20ladron.pdf\
El texto "Cien años de soledad" de Gabriel García Márquez ha sido extraído desde https://www.fundacionarteficial.com/post/2016/02/21/descarga-12-libros-de-gabriel-garc%C3%ADa-m%C3%A1rquez-en-pdf
