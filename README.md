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

## Análisis de frecuencias
Una vez obtenida la lista de palabras a considerar, se genera un diccionario que cuenta las instancias de cada palabra.
Para esto, se cuenta cuántas veces la misma palabra está contenida en la lista.
En este análisis, las decisiones del pre-procesamiento son importantes ya que nuestros resultados serán distintos según qué estamos contando.
Por ejemplo, cuando no removemos stop-words, la frecuencia es la siguiente:

Pero si removes stop-words, entonces vemos que la frecuencia cae considerablemente (cerca de 9.000 a menos de 1.000) y las palabras pueden generar más sentido según el texto que estamos analizando.

De manera similar, si hemos lematizado o radicalizado las palabras, obtendremos diferentes frecuencias.

## Resultados

