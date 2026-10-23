# La separación entre patrones también ocurre en grafos simples

18/10/2026. Deducción y comprobación asistidas por Codex. **Modelo:** Kuramoto homogéneo sobre grafos simples no dirigidos, sin lazos. Esta nota conecta la [separación de plantillas a geometría fija](obstruccion_patron_finito.md) con el modelo original. La existencia de los grafos se obtiene mediante un lema publicado; no se enumeran sus aristas ni se seleccionan conjuntos de desplazamientos. No hay mejora de la cota general conocida ni novedad bibliográfica confirmada.

## Enunciado

Con las siete fases especificadas por sus coordenadas racionales y las proporciones $x=(20,20,20,20,20,20,33)/153$ del caso finito, existen **dos grafos simples del mismo orden $n$**, cada uno con un equilibrio no sincronizado estrictamente estable, tales que:

- Los cuatro conjuntos de hojas $A=V_0\cup V_1$, $B=V_2\cup V_3$, $C=V_4\cup V_5$ y $W=V_6$ son cliques en ambos grafos.
- Uno tiene todos los enlaces entre hojas opuestas ausentes.
- El otro solo tiene un par de clusters opuestos enlazado, $V_1$ con $V_4$.
- La conectividad $(\delta+1)/n$ del segundo supera en más de $1.99\times10^{-7}$ la de **cualquier** grafo de ese orden con esas proporciones y fases, hojas completas y opuestos vacíos, que esté en equilibrio y tenga Hessiano semidefinido positivo.

Los bloques adyacentes de la clase competidora son arbitrarios: no hace falta que la partición sea equitativa ni que todos los vértices de un cluster tengan el mismo número de vecinos en otro. La comparación se refiere siempre al mismo $n$ y a las mismas masas y fases.

El certificado da $n=D^2$, con

$$D=160491671956874583744960806572727970000000000000000000000.$$

El orden tiene 113 cifras. La afirmación es de existencia y no representa una construcción pequeña o una lista explícita de aristas. Se pueden obtener órdenes mayores mediante el mismo lema.

## 1. De un grafo arbitrario de la clase restringida a una plantilla

Sea $G$ un grafo simple con una partición $V_0,\ldots,V_6$, $n_i=|V_i|=x_i n$, y la fase constante $\varphi_i$ en $V_i$. Cada hoja induce un clique y no hay enlaces entre hojas opuestas. Para $i\ne j$, definir

$$P_{ij}=\frac{e(V_i,V_j)}{n_i n_j},\qquad P_{ii}=1.$$

La diagonal uno es una convención de la plantilla, no un lazo del grafo. Esta matriz está en la clase restringida de la cota dual: entre las dos mitades de una hoja $P_{ij}=1$, entre opuestos $P_{ij}=0$ y las doce entradas adyacentes pertenecen a $[0,1]$.

### Equilibrio por promedio

Sea $R_v=\sum_{w\sim v}\sin(\theta_v-\theta_w)$ el residuo del grafo. Al sumar sobre $V_i$,

$$F_i(P)=\sum_jx_jP_{ij}\sin(\varphi_i-\varphi_j)
=\frac{1}{n n_i}\sum_{v\in V_i}R_v.$$

Si todos los vértices están en equilibrio, la plantilla lo está. No se necesita igualdad de los grados entre bloques.

### Hessiano por restricción

Sea $J:\mathbb R^7\to\mathbb R^n$ la inclusión que asigna el valor $y_i$ a todos los vértices de $V_i$. Para el Hessiano $H_G$ del grafo y el Hessiano ponderado $H_T$ de la plantilla,

$$J^TH_GJ=n^2H_T.$$

Las aristas internas de un cluster no contribuyen a la forma restringida, porque la diferencia de sus valores es cero. Si $H_G\succeq0$, entonces $H_T\succeq0$. Esta implicación solo se usa para la cota superior; no se invierte para certificar un grafo concreto.

### Grado mínimo frente al promedio de grados

Si $\bar\delta_i$ es el promedio de los grados de los vértices de $V_i$, el hecho de que $V_i$ sea completo da

$$d_i(T)=\sum_jx_jP_{ij}=\frac{\bar\delta_i+1}{n}.$$

Por tanto,

$$\frac{\delta(G)+1}{n}\leq\min_i\frac{\bar\delta_i+1}{n}
=\mu(T)\leq U,$$

donde $U$ es la fracción exacta de la cota dual restringida y $U<0.68877337417$. La primera desigualdad puede ser estricta: identificar grado mínimo con grado promedio exigiría una condición adicional que aquí no se supone.

Como $\delta(G)$ es entero, también se obtiene la cota finita

$$\delta(G)\leq\delta_U:=\lfloor nU-1\rfloor.$$

Esto cubre cualquier grafo de la clase, incluidos bloques adyacentes no regulares.

## 2. De los dos testigos estrictos a grafos del mismo orden

Los dos datos de entrada son el testigo restringido de `fixed_geometry_005_tight_data.json` y el testigo de un opuesto de `one_opposite_link_data.json`. Sus matrices originales, denotadas $P^-$ y $P^+$, tienen internos completos, las mismas masas y puntos del círculo, equilibrio exacto, fuerzas internas positivas y Hessiano de clusters estrictamente positivo fuera de la rotación. Las siete fases son distintas.

Se elige el mismo denominador par $D$ para las masas y las dos matrices. Para cada testigo, sustituir únicamente la diagonal por

$$\widetilde P_{ii}=1-\frac1D,$$

manteniendo las entradas fuera de ella. Esto conserva equilibrio y Hessiano de clusters; la fuerza interna del cluster $i$ disminuye en $x_i/D$ y sigue siendo positiva, comprobado exactamente.

El [Lema 2 de O'Keeffe v1](https://arxiv.org/html/2610.21271v1) realiza una plantilla racional estricta mediante grafos simples si su denominador par y sus fuerzas internas satisfacen una condición explícita. Aquí esa condición se verifica para ambos testigos con el mismo $D$ y $\ell=1$. Los grafos resultantes tienen orden $n=D^2$ y cada vértice de $V_i$ tiene exactamente $\widetilde P_{ij}n_j$ vecinos en $V_j$. El lema garantiza estabilidad estricta del estado de clusters; no se usa solo la estabilidad del Hessiano de siete dimensiones para inferir la del grafo completo.

La condición comprobada es

$$c_{\min}D>2\sqrt{2D\log(8DN_s)}+3,\qquad N_s=7(7+3)/2=35.$$

Para evitar evaluar el logaritmo en punto flotante, se usan $k=\operatorname{bitlength}(D)$ y $b=\operatorname{bitlength}(8N_s)$. Entonces $\log(8DN_s)<k+b$. Basta verificar por fracciones

$$c_{\min}D-3>0,\qquad (c_{\min}D-3)^2>8D(k+b).$$

Son condiciones suficientes del lema, no una selección explícita de sus conjuntos aleatorios de desplazamientos.

## 3. Completar clusters de fase igual preserva estabilidad

En cada grafo realizado, agregar las aristas que falten dentro de cada $V_i$. Un enlace nuevo une fases idénticas, así que aporta cero al residuo y añade al Hessiano

$$ (e_v-e_w)(e_v-e_w)^T\succeq0.$$

El equilibrio sigue siendo exacto y la positividad estricta en el complemento de la rotación se conserva. Las aristas entre mitades de la misma hoja ya eran completas, porque sus densidades eran uno. Por ello, después de completar los $V_i$, cada hoja es un clique. No se agrega ningún enlace entre clusters distintos ni cambia el soporte opuesto.

El lema proporciona grados regulares dentro de los bloques realizados. Antes de completar, cada vértice de $V_i$ tiene $\widetilde P_{ii}n_i$ vecinos en su mismo cluster. Para convertirlo en clique se agregan exactamente

$$n_i-1-\widetilde P_{ii}n_i=\frac{n_i}{D}-1=x_iD-1$$

vecinos por vértice. Esta cantidad es un entero no negativo. Si $d_i=\sum_jx_jP_{ij}$ es el grado de la **plantilla original con diagonal uno**, el grado final de cada vértice de $V_i$ es

$$n\left(d_i-\frac{x_i}{D}\right)+(x_iD-1)=nd_i-1.$$

En consecuencia,

$$\boxed{\delta(G^{\pm})=n\mu(P^{\pm})-1,\qquad
\frac{\delta(G^{\pm})+1}{n}=\mu(P^{\pm}).}$$

La identidad explica el $+1$ de la normalización y evita confundir un lazo ficticio con una arista del grafo. Ambas conectividades corresponden a grafos del mismo tamaño, con las mismas masas y fases.

## 4. Comparación exacta de las tres normalizaciones

El testigo de un opuesto satisface

$$\mu(P^+)>0.68877357363,\qquad
\mu(P^+)-U>1.99\times10^{-7}.$$

El primer grafo existe y pertenece a la clase restringida; por ello la clase competidora no es vacía a este orden. La existencia del segundo, junto con el apartado 1, prueba la separación frente a toda esa clase.

Para un grafo realizado y completado, con $\mu=\mu(P^{\pm})$,

| Normalización | Valor exacto después de completar |
| --- | --- |
| $\delta/n$ | $\mu-1/n$ |
| $(\delta+1)/n$ de la propuesta | $\mu$ |
| $\delta/(n-1)$ del artículo | $(n\mu-1)/(n-1)$ |

Con el mismo $n$, el cambio de normalización es una función afín creciente. Si $\delta_+$ es el grado mínimo del grafo de un opuesto y $\delta_U=\lfloor nU-1\rfloor$, la ventaja frente a toda la clase es al menos

$$\frac{\delta_+-\delta_U}{n}>1.99\times10^{-7}$$

para las dos primeras normalizaciones, y

$$\frac{\delta_+-\delta_U}{n-1}>1.99\times10^{-7}$$

para la tercera. Son fracciones verificadas: no se comparan números finitos de convenciones distintas.

## Reproducción, controles y alcance

Con Python estándar, sin optimizador:

```text
python -S verify_simple_graph_separation.py
python -S simple_graph_separation_checks.py
```

El primer comprobador reconstruye el denominador común, verifica los dos testigos adelgazados y la condición suficiente del lema, comprueba los conteos enteros de grados tras completar y compara las tres normalizaciones con la cota universal. Produce `simple_graph_separation_plan.json` y `simple_graph_separation_certificate.json`. El plan especifica masas, fases y densidades, **no** todos los enlaces de un grafo seleccionado.

El segundo incluye dos controles algebraicos en un grafo de 14 vértices. Uno comprueba la agregación con bloques no regulares y muestra una desigualdad estricta entre grado mínimo y promedio; ese grafo de control no es un equilibrio y no es uno de los grafos de la proposición. El otro comprueba que añadir aristas entre fases iguales no altera el gradiente y añade exactamente una suma de Laplacianos positivos. Los controles negativos rechazan errores en grado mínimo, normalización, orden, holgura diagonal y soporte fijo.

El resultado traslada una limitación local de patrones al modelo de grafos simples. No da un grafo pequeño, no enumera aristas, no identifica la conectividad crítica general y no mejora $\mu_0$. La realización se atribuye al lema citado; la agregación y la completación son argumentos elementales. La novedad de la comparación concreta sigue pendiente de comprobación.

**Uso de IA:** Codex (OpenAI) hizo la consulta, deducción, código, controles y redacción. Constructor y verificadores proceden del mismo agente. No hubo subagentes, revisión humana independiente, publicaciones, comunicaciones ni entrega al evento.
