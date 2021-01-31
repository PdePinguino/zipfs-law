# ¿Cuáles son las palabras más frecuentes en "Hijo de Ladrón"?

El siguiente código tiene por objetivo ilustrar la frecuencia de palabras que componen esta novela.

Puede utilizarse el mismo código para otros textos. Solo se requiere el archivo en formato txt.

Para utilizar este repositorio:
```
git clone https://github.com/PdePinguino/zipfs-law.git
cd zipfs-law
./zipf_law.py hijo_de_ladron.txt
```

## Pre-procesamiento
Antes de calcular la frecuencia de palabras, es necesario leer el archivo en formato txt y eliminar aquello que no se analizará.
Este código se encarga de:
- convertir mayúsculas en minúsculas.
- eliminar puntuación y caracteres que no sean letras.
- (opcional) remover stop-words ('de', 'a', 'tu'...).
- (opcional) lematizar (reducir palabras a su forma base). TODO
- (opcional) radicalizar (stemming) (reducir palabras a su raíz). TODO

## Frecuencias
Una vez obtenida la lista de palabras a considerar, se genera un diccionario que cuenta las instancias de cada palabra.\
Para esto, se cuenta cuántas veces la misma palabra está contenida en la lista.\
En este análisis, las decisiones del pre-procesamiento son importantes ya que nuestros resultados serán distintos según qué estamos contando.\
Por ejemplo, cuando analizamos todas las palabras del texto, es decir, no removemos stop-words, la frecuencia es la siguiente:

![freq_allwords_30](https://user-images.githubusercontent.com/76110750/106389944-ced90100-63c4-11eb-9ab6-bc9a24a2ef93.png)

Pero si removes stop-words, entonces vemos que la frecuencia cae considerablemente (cerca de 9.000 a menos de 1.000) y las palabras pueden generar más sentido según el texto que estamos analizando.

<!-- ![freq_wsw](https://user-images.githubusercontent.com/76110750/106389950-d13b5b00-63c4-11eb-8325-67fd3ccfc0b4.png) -->
![freq_wsw_30](https://user-images.githubusercontent.com/76110750/106389952-d26c8800-63c4-11eb-81d7-8b55bcf27cf4.png)

De manera similar, si hemos lematizado o radicalizado las palabras, obtendremos diferentes frecuencias.

## Análisis
Cuando revisamos el comportamiento de frecuencias, podemos notar la siguiente tendencia: un grupo reducido de palabras aparece muchas veces, y el resto de palabras aparece muy pocas veces. Si graficamos la frecuencia de todas las palabras, vemos cómo van disminuyendo rápidamente las frecuencias:
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
'los'| 2761

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


## Resultados

