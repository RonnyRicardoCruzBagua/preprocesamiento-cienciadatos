# Universidad Nacional de Chimborazo

- **Nombre:** Ronny Cruz

- **Fecha:** 23 nov 2025

- **Carrera:** Ciencia de Datos e Inteligencia Artificial

- **Periodo:** Periodo 2025 - 2S

- **Semestre:** Tercer Semestre

## 📘 Documentación: Optimizacion de Codigos

## 📖 1. Introducción

El propósito de este proyecto fue analizar y optimizar un programa en Python encargado de encontrar números primos en un rango de 1 a 100,000.
El código original funcionaba correctamente, pero utilizaba un enfoque poco eficiente para verificar si un número era primo, ya que evaluaba todos los posibles divisores desde 2 hasta n−1, lo que elevaba considerablemente el tiempo de ejecución.

**_Problemas detectados_**

- Complejidad O(n) en la verificación de números primos.

- Uso de bucles tradicionales en lugar de list comprehensions.

- No utilizaba bibliotecas eficientes como NumPy.

- Código más lento y difícil de escalar para rangos grandes.

Para mejorar el desempeño, se aplicaron varias técnicas modernas de optimización, cuyo efecto se midió mediante time y cProfile.

## 🚗 2. Código Original

A continuación se muestra el código original implementado:

```yaml
import time

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def buscar_primos(limite):
    primos = []
    for num in range(1, limite + 1):
        if es_primo(num):
            primos.append(num)
    return primos

# Medición de tiempo
inicio = time.time()
resultado = buscar_primos(100000)
fin = time.time()

print(f"Cantidad de primos encontrados: {len(resultado)}")
print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
```

**¿Qué hace el codigo?**

- La función es_primo(n) revisa todos los posibles divisores desde 2 hasta n−1.

- El programa completa muchas divisiones innecesarias, lo que lo hace lento.

- Luego, el programa recorre cada número del 1 al 100,000 verificando si es primo.

- El tiempo de ejecución es alto debido a la gran cantidad de iteraciones.

## 🏎️ 3. Código Optimizado

A continuación se presenta la versión optimizada con mejoras significativas:

```yaml
import time
import numpy as np
import math

def es_primo_opt(n):
    if n < 2:
        return False
    limite = int(math.sqrt(n)) + 1
    for i in range(2, limite):
        if n % i == 0:
            return False
    return True

def buscar_primos_opt(limite):
    numeros = np.arange(1, limite + 1)  # Array más eficiente que range()
    primos = [n for n in numeros if es_primo_opt(n)]  # list comprehension optimizada
    return primos

# Medición de tiempo
inicio = time.time()
resultado = buscar_primos_opt(100000)
fin = time.time()

print(f"Cantidad de primos encontrados: {len(resultado)}")
print(f"Tiempo de ejecución optimizado: {fin - inicio:.4f} segundos")
```

### **¿Que es lo que realiza?**

- es_primo_opt(n) evalúa divisores solo hasta la raíz cuadrada de n, reduciendo la complejidad a O(√n).

- Se usa NumPy para crear el rango numérico más eficientemente.

- Se reemplaza el bucle tradicional por una list comprehension, que es más rápida y legible.

- Estas optimizaciones reducen significativamente el tiempo de ejecución total.

## 👾 4. Optimización aplicada

Las técnicas utilizadas fueron:

☑️ **1. Iteración hasta la raíz cuadrada**

Esto evita evaluar divisores innecesarios, reduciendo la carga del CPU.

☑️ **2. List Comprehensions**

Permiten filtrar números primos en una sola línea optimizada.

☑️ **3. Uso de NumPy**

Arrays más eficientes que listas tradicionales para operaciones numéricas.

☑️ **4. Buenas prácticas (PEP 8)**

Código más legible, mantenible y profesional.

## 🦾 5. Resultados Obtenidos

- **Comparación de tiempos de ejecución**

![Distibucion de Tiempos](<Evidencias/Evidencias doc2/Distribucion.png>)

![Tiempos de Ejecucion](<Evidencias/Evidencias doc2/Tiempos de ejecucion.png>)

### 🚩 Análisis con cProfile

**_Código original_**

Las funciones que más tiempo tomaron fueron:

- es_primo() → debido a su complejidad O(n)

- Llamadas repetitivas al ciclo interno

**_Código optimizado_**

Las funciones con mayor impacto:

- es_primo_opt(), pero con mucho menos tiempo total

- Menor cantidad de iteraciones

- Generación de rangos más rápida gracias a NumPy

Se observó una reducción significativa del tiempo total de ejecución y de la cantidad de llamadas a funciones internas.

## 🏁 6. Conclusiones

- La optimización aplicada permitió una aceleración notable en la búsqueda de números primos.

- El uso de algoritmos eficientes y bibliotecas como NumPy mejora el desempeño sin comprometer la claridad del código.

- Utilizar cProfile ayudó a identificar cuellos de botella y a dirigir la optimización hacia las funciones más costosas.

- Las buenas prácticas de Python no solo ordenan el código, sino que también contribuyen a un mejor rendimiento

## 🕷️ Ejecucion del Git

### Creacion del codigo de optimizacion en Git

![alt text](<Evidencias/Evidencias doc2/1. Creacion del codigo de optimizacion en Git.png>)

### Comit de la optimizacion

![alt text](<Evidencias/Evidencias doc2/2. Commit de la optimizacoin de codigos.png>)

### Git push

![alt text](<Evidencias/Evidencias doc2/3. Git push del codigo.png>)
