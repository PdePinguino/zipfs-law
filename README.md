# ¿Cuáles son las palabras más frecuentes en "Hijo de Ladrón"?

El siguiente código tiene por objetivo ilustrar la frecuencia de palabras que componen esta novela.

Puede utilizarse el mismo código para otros textos. Solo se requiere el archivo en formato txt.

Para utilizar este repositorio:
```
git clone https://github.com/PdePinguino/zipfs-law.git
cd zipfs-law
./zipf_law.py hijo_de_ladron.txt
```
Si se quiere analizar otro texto, entonces
```
./zipf_law.py [mi_texto.txt]
```

Los argumentos disponibles son:\
`-t TEXT, --text TEXT` archivo que será analizado.\
`-r, --remove_stop_words` remover o no stop words dadas por `nltk.corpus` para español.\
`-p, --plot` plotear o no los resultados.\
`-v, --verbose` imprimir en consola detalles del proceso.


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
Para esto, se cuenta cuántas veces la misma palabra está contenida en la lista.\
En este análisis, las decisiones del pre-procesamiento son importantes ya que nuestros resultados serán distintos según qué estamos contando.\
La pregunta que está en cuestión es qué estamos contando (¿contamos palabras?) y cómo las contamos. ¿Debemos considerar los siguientes pares de palabras como correspondientes a una misma palabra?\
"hijo" - "hijos" (singular - plural)\
"corrimos" - "correremos" (distintos tiempos verbales y/o modos)\
"tierra" - "tierra" (distinto significado pero igual escritura: la "tierra" entendida como "planeta" y entendida como "suelo")\

## Análisis
Cuando nos fijamos en la frecuencia de las palabras, vemos que muy pocas palabras aparecen gran cantidad de veces, y muchas palabras aparecen muy pocas veces. Es decir, si graficamos cada palabra del texto en el eje x y su frecuencia en el eje y, entonces obtenemos lo siguiente:

![freq_allwords_30](https://user-images.githubusercontent.com/76110750/106389944-ced90100-63c4-11eb-9ab6-bc9a24a2ef93.png)

La frecuencia detallada de las 10 palabras más frecuentes está mostrada en la siguiente tabla. Podemos ver cómo 'de' es la palabra más utilizada con 9.050 apariciones.\

| Palabra | Frecuencia |
| --- | --- |
'de'| 9050
'y'| 8413 
'que'| 6294
'la'| 5321 
'el'| 4849 
'a'| 4358 
'en'| 4042 
'no'| 4014 
'un'| 3124 
'se'| 2797 

Cuando nos percatamos de las palabras, no hay mucho de característico en ellas que remita al texto que estamos analizando. Si comparamos las 10 palabras más frecuentes con la novela "Cien años de soledad" de García Márquez, obtenemos el siguiente resultado (en negrita están las palabras repetidas en ambas novelas).


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


Pero si removes stop-words, entonces vemos que la frecuencia cae considerablemente (cerca de 9.000 a menos de 1.000) y las palabras pueden generar más sentido según el texto que estamos analizando.

<!-- ![freq_wsw](https://user-images.githubusercontent.com/76110750/106389950-d13b5b00-63c4-11eb-8325-67fd3ccfc0b4.png) -->
![freq_wsw_30](https://user-images.githubusercontent.com/76110750/106389952-d26c8800-63c4-11eb-81d7-8b55bcf27cf4.png)

De manera similar, si hemos lematizado o radicalizado las palabras, obtendremos diferentes frecuencias.

## Análisis


![freq_allwords](https://user-images.githubusercontent.com/76110750/106389937-ca144d00-63c4-11eb-9d4f-2912267fd272.png)

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

Considerando que hemos removido stop words, entonces hay 4 palabras que aparecen más de 5 mil veces cada una. Para ser exactos, 
Según estos resultados, menos de 10 palabras (de 11.907) ocurren casi 10.000 veces en el texto, y si el texto tiene un total de 98.307 tokens, entonces menos del 1% de las palabras abarca el 12% de las palabras de todo el texto.

## Créditos
El texto "Hijo de ladrón" de Manuel Rojas ha sido extraído de 
