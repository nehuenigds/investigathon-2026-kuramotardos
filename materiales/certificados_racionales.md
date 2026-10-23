# Certificados racionales por flujos de árbol

18/10/2026. Deducción y experimentos asistidos por Codex. El patrón inicial y el predictor de siete clusters proceden de [O'Keeffe, arXiv:2610.21271v1, Tabla 2 y Apéndice A](https://arxiv.org/html/2610.21271v1). La idea que se desarrolla aquí es elegir puntos racionales del círculo y corregir el equilibrio mediante flujos sobre un árbol o bosque. **No se ha comprobado su novedad bibliográfica ni hubo revisión humana independiente.**

## 1. Un lema de racionalización con coordenadas del círculo racionales

Una plantilla tiene masas $x_i>0$, $\sum_i x_i=1$, densidades simétricas $0\leq P_{ij}\leq1$ y puntos $z_i=(c_i,s_i)$ del círculo unidad. Para evitar confundir las coordenadas $c_i$ con la fuerza interna, llamamos $\gamma_i$ a esta última. Definimos

$$
C_{ij}=c_ic_j+s_is_j,\qquad S_{ij}=s_ic_j-c_is_j,
$$

$$
F_i=\sum_jP_{ij}x_jS_{ij},\qquad
\gamma_i=\sum_jP_{ij}x_jC_{ij}.
$$

El Hessiano de clusters tiene pesos $x_ix_jP_{ij}C_{ij}$. Una plantilla es estricta si $F=0$, $\gamma_i>0$ y el Hessiano es positivo fuera de la rotación.

**Proposición.** Toda plantilla estricta puede aproximarse arbitrariamente por plantillas estrictas del mismo número de clusters para las que son racionales las masas, las densidades y **las dos coordenadas de cada punto del círculo**. Se puede conservar todo enlace de densidad cero y todas las relaciones originales de igualdad o antipodalidad entre puntos. La conectividad converge a la original. Si la original no está sincronizada, se pueden escoger las aproximaciones sin sincronización.

Las fases angulares no se afirman racionales: lo racional es su seno y su coseno. Esta proposición fortalece el tipo de datos racionales de la aproximación; no mejora por sí sola ninguna cota de conectividad.

### Demostración

1. Multiplicar todas las densidades por $1-\eta$, con $\eta>0$ pequeño. El equilibrio sigue siendo exacto, el Hessiano y las fuerzas internas se multiplican por el mismo factor positivo, y la conectividad cambia en una cantidad que tiende a cero con $\eta$. Cada densidad originalmente positiva queda estrictamente entre 0 y 1.

2. Construir el grafo auxiliar $\mathcal S$ con aristas $ij$ tales que $P_{ij}>0$ y $S_{ij}\ne0$. En cada componente escoger un árbol generador; para componentes de un solo vértice no hace falta ninguna arista.

3. Aproximar las masas dentro del simplex por masas racionales positivas y las densidades positivas por racionales interiores, respetando simetría y manteniendo las densidades cero. Para las fases, agrupar los puntos originales en clases módulo antipodalidad: en cada clase son iguales o antipodales entre sí. Aproximar un representante por un punto racional del círculo y conservar exactamente los signos de los demás. Los puntos racionales son densos porque

$$
z(t)=\left(\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\right),\qquad t\in\mathbb Q,
$$

recorre un subconjunto denso del círculo. Así se conservan exactamente todas las igualdades $S_{ij}=0$ originales, y los senos de las aristas del bosque permanecen no nulos para aproximaciones suficientemente próximas.

4. Sean $b_i=x_iF_i$ los desequilibrios de estos datos racionales aproximados. En cada componente de $\mathcal S$ se tiene **exactamente** $\sum_i b_i=0$. Los términos internos se cancelan por antisimetría; todo enlace entre componentes tiene densidad cero o seno cero, conservados en el paso anterior.

5. En un árbol orientado, para la arista $e=i\to j$ sea $A_e$ el lado que contiene a $i$ al eliminarla. El flujo

$$
f_e=-\sum_{k\in A_e}b_k
$$

es la solución de las ecuaciones de conservación que elimina los desequilibrios. Corregir únicamente la densidad de esa arista en

$$
\Delta P_{ij}=\Delta P_{ji}=\frac{f_e}{x_ix_jS_{ij}}
$$

da equilibrio exacto en todos los vértices. Todas las operaciones son racionales. Al acercar los datos aproximados a la plantilla escalada, $b\to0$, mientras los denominadores de las aristas del bosque convergen a valores no nulos; por tanto $\Delta P\to0$. Los enlaces corregidos eran interiores, de modo que permanecen en $[0,1]$.

6. Las fuerzas internas estrictamente positivas y el Hessiano positivo en un complemento de la rotación son condiciones abiertas. Se preservan para aproximaciones suficientemente próximas, al igual que la separación de al menos dos fases cuando la plantilla original no está sincronizada. La conectividad es continua. Primero tomar $\eta$ pequeño y luego la aproximación suficientemente cercana completa la prueba. $\square$

Este argumento no necesita resolver las fases mediante un teorema de función implícita. El bosque es importante: no se supuso que el grafo auxiliar de senos no nulos fuera conectado. Tampoco se presupone una cota uniforme para los denominadores necesarios.

## 2. Una plantilla finita con un certificado exacto breve

Se construyó una variante de la familia conocida con

$$
\tau=\frac1{400},\quad q=\frac{13}{20},\quad w=\frac75,\quad
\kappa=2,\quad u=\frac{10}{3},\quad h=2\tau=\frac1{200}.
$$

Los puntos son

$$
z=\big((C,-S),(C,S),(S_B,C_B),(-S_B,C_B),(-C,S),(-C,-S),(0,-1)\big),
$$

donde

$$
C=\frac{159999}{160001},\quad S=\frac{800}{160001},\quad
C_B=\frac{3999951}{4000049},\quad S_B=\frac{28000}{4000049}.
$$

Las masas son $(20,20,20,20,20,20,33)/153$. Los ángulos de desdoblamiento son $2\arctan\tau$ y $2\arctan(w\tau)$: a separación finita la segunda anchura **no es exactamente $w$ por la primera**, aunque su cociente tiende a $w$. Este cambio respecto de la parametrización angular lineal del cuaderno anterior es explícito.

Se usa el patrón de enlaces y el predictor de primer orden de la referencia, ahora con parámetros racionales. La corrección exacta se calcula sobre el camino

$$
0\to2\to4\to6\to5\to3\to1.
$$

En un camino, el flujo de cada arista es simplemente la suma negativa de los desequilibrios anteriores. Los datos finales completos, incluidas las correcciones, ocupan unos 3,3 kB en `rational_template_compact_data.json`.

### Qué certifica el verificador

`verify_rational_template.py` lee únicamente los datos, usando la biblioteca estándar de Python:

- comprueba $c_i^2+s_i^2=1$, masas, simetría y rango de densidades;
- comprueba los siete residuos como fracciones **exactamente iguales a cero**;
- calcula las siete fuerzas internas como racionales positivos;
- elimina la fila y columna de W y realiza una factorización LDL exacta, con seis pivotes positivos;
- obtiene exactamente los grados y la conectividad.

Eliminar una fase es un gauge, no una base ortonormal de $\mathbf1^\perp$. La equivalencia necesaria es: como $H\mathbf1=0$, para cualquier $y$ se puede restar $y_W\mathbf1$ sin cambiar $y^THy$. La positividad de la matriz fijando W certifica entonces positividad en todo vector que no sea una rotación. Los pivotes **no son autovalores**.

La conectividad de la plantilla es el racional

$$
\mu=\frac{13932945142796296156566051657323629409999}
{20259479432917377318694658296968988013250}
=0.6877247359158795\ldots>\frac{11}{16}.
$$

Las comparaciones $\min\gamma_i>21/100$ y que los seis pivotes son mayores que $6/10^8$ se pueden comprobar directamente con las fracciones del certificado; estas últimas cotas describen pivotes, no márgenes espectrales. El valor es inferior a la mejor cota conocida y no es una mejora de ella.

### Relación con grafos simples

Se redujeron las densidades diagonales a $1-1/D$ con denominador común par

$$
D=2648297965087238865188844221826011505000.
$$

Esto no cambia el equilibrio ni el Hessiano de clusters. El certificado verifica además las condiciones del **Lema 2 de realización del preprint citado**, con $\ell=1$, usando una cota racional para el logaritmo de su condición suficiente. Ese lema implica existencia de un grafo simple homogéneo con

$$
n=D^2=7013482111885210243304661606327107041699655732463355490079820216392365025000000
$$

y un equilibrio estrictamente estable no sincronizado. No se enumeraron las aristas ni se seleccionaron explícitamente los conjuntos de desplazamientos de esa realización. La afirmación de existencia depende del lema citado.

En esa realización $\delta/n=\mu$. La normalización de la propuesta es $(\delta+1)/n=\mu+1/n$, y la de otros artículos es $\delta/(n-1)=\mu n/(n-1)$. Las tres fracciones exactas constan en el certificado; no se las iguala para un grafo finito.

## 3. Experimentos y controles realizados

Se ejecutaron dos barridos deterministas: 40 combinaciones iniciales de $\tau,q,w$, y 390 combinaciones adicionales variando también $\kappa,u$. Pasaron las condiciones de plantilla estricta las 40 y las 390, respectivamente. Superaron $11/16$ 22 y 157. No son búsquedas exhaustivas de plantillas o grafos. Se conservaron todos los parámetros y resultados en `rational_template_trials.json` y `rational_template_compact_trials.json`. La selección compacta minimiza el denominador común **solo entre los casos ensayados** que superan $11/16$.

Los controles negativos del verificador fueron:

1. Restar $10^{-8}$ a una densidad: se rechaza por residuo de equilibrio no nulo.
2. Dar la plantilla de cuatro fases a cuarto de vuelta, completa entre vecinos: se comprueba equilibrio pero se rechaza el primer pivote cero. Así, un Hessiano semidefinido con modos nulos adicionales no se acepta como certificado estricto.

El certificado registra las huellas SHA-256 de los datos y del verificador. Las comparaciones de aceptación no usan números flotantes, tolerancias, autovalores numéricos ni evaluaciones trascendentes. Las aproximaciones decimales en los resúmenes sirven para lectura.

## 4. Uso para el proyecto

Este resultado da una exposición complementaria a la prueba de optimalidad: se puede explicar cómo elegir una geometría racional, equilibrarla por conservación de flujos y certificarla mediante álgebra exacta. La fuerza del ejemplo está en que el certificado es auditable con Python estándar; su conectividad no establece un nuevo récord.

La proposición general y el ejemplo fueron derivados en esta continuación. El patrón y el predictor no son nuevos; el método de realización en grafos procede del preprint. Una búsqueda bibliográfica breve no alcanzó para confirmar novedad del argumento de racionalización.

**Uso de IA:** Codex (OpenAI) propuso el argumento del bosque, programó el constructor y el verificador, ejecutó los 430 casos y redactó la nota. Constructor y verificador están separados, pero fueron escritos por el mismo agente; esto no constituye revisión independiente. No se enviaron comunicaciones ni se presentó material al evento.
