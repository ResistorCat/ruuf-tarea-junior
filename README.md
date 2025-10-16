# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

- Python: 3.12
- Youtube: https://youtu.be/bfVTqvk95N8

---

## 💰 Bonus Implementado y explicación
Implementé el bonus de la opción 2, ya que me pareció más directo teniendo la solución base del problema. Como hice la solución usando POO con clases, era más sencillo reemplazar la matriz que definí para la clase Roof con una hardcodeada que representara el techo con rectángulos superpuestos. Este fue el resultado:
```
Bonus 2: techo de 9x4 con esquinas de 1x4 ocupadas
-1 -1 -1 -1  0  0  0  0  0
 0  0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0  0
 0  0  0  0  0 -1 -1 -1 -1
Colocando paneles de 1x2
-1 -1 -1 -1 15 16 17 18 19
20 21 22 23 15 16 17 18 19
20 21 22 23 24 25 25 26 26
27 27 28 28 24 -1 -1 -1 -1
Se colocaron 14 paneles
```

> Los `-1` representan las áreas ocupadas del techo.

---

## 🤔 Supuestos y Decisiones

- Supuse que los paneles siempre tienen anchos y alturas enteras, para simplificar la lógica del código (use matrices binarias con ceros representando espacios libres, y un id entero para cada panel colocado).
- Supuse que las rotaciones solo pueden ser de 90 grados (no diagonales o ángulos raros).

> PD: Me tardé aproximadamente 19 minutos en la solución base, 7 minutos en el bonus y unos 12 minutos en documentar y hacer el video.