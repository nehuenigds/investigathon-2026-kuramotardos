# Flujos positivos y vector límite no nulo

22/10/2026. Auditoría de otro paso de la [reducción 0,6934](cota_flujos_06934.md), preparada por Codex. Explicita por qué se puede normalizar el flujo y conservar una dirección no nula cuando las separaciones tienen distintas escalas. No cambia la cota ni el certificado y no acredita revisión humana o novedad.

La [auditoría variacional](auditoria_paso_variacional.md) justifica las cancelaciones principales sin derivar los datos. Aquí se parte de esas cancelaciones, del equilibrio principal y de una cota de grado en el límite. Son hipótesis distintas; comprobar solo una de ellas no basta.

## 1. Primero tomar el límite, después normalizar el flujo

Tras extraer subsucesión, sean $x_i>0$, $\sum_i x_i=1$, las masas límite y $s_i$ los offsets límite normalizados por la desviación angular máxima. Fijar W y conservar

$$s_6=0,\qquad\max_i|s_i|=1.$$

La igualdad del máximo pasa al límite por continuidad en dimensión siete. No exige que las tres diferencias dentro de parejas tengan la misma escala.

Las hojas son A={0,1}, B={2,3}, C={4,5}, W={6}, con masas $y_A,y_B,y_C,y_W$. Las conductancias adyacentes límite son $a_{ij}=x_i x_jP_{ij}$, orientadas A→B→C→W→A y acotadas por $x_i x_j$. Se han probado opuestos límite nulos.

Tomar el límite en los residuos de equilibrio exactos da, en cada cluster,

$$f_i^{\rm out}:=\sum_{i\to j}a_{ij}=\sum_{j\to i}a_{ji}=:f_i^{\rm in}=:f_i\geq0.\tag{1}$$

En efecto, los senos internos tienden a cero, los opuestos desaparecen y los senos adyacentes orientados tienden a −1. No se afirma que los flujos adyacentes de cada dato finito ya estén balanceados por separado. Eso se usa después de pasar al límite.

Sumar (1) por hojas iguala los cuatro flujos totales de corte a un mismo $T\geq0$. Hasta aquí no se divide por $T$ ni por un flujo individual.

## 2. El grado excluye todos los flujos cero

Completar internos en el límite a densidad uno, como relajación, aumenta grados. Supongamos que el grado mínimo completado es al menos $u>1/2$; la aplicación 0,6934 tiene esta propiedad bajo su hipótesis de contradicción. Usar la conectividad de plantilla $\mu=\min_i(Px)_i$.

Un cluster de la hoja opuesta a L tiene grado a lo sumo $1-y_L$, porque faltan todos los enlaces con L. Cada hoja opuesta es no vacía. Por tanto,

$$y_L\leq1-u\qquad(L=A,B,C,W).\tag{2}$$

Por equilibrio principal, el grado completado de cada cluster es exactamente

$$d_i=y_{L(i)}+\frac{2f_i}{x_i}.\tag{3}$$

El primer término incluye la diagonal de plantilla, completada a uno, y las conexiones con la otra mitad de su hoja. No se confunde con el grado finito de un grafo simple. De $d_i\geq u$ y (2), antes de normalizar flujos,

$$\boxed{f_i\geq\frac{x_i}{2}(u-y_{L(i)})\geq c_u x_i>0,\qquad c_u=\frac{2u-1}{2}.}\tag{4}$$

Así se excluyen a la vez el flujo total cero y una mitad con flujo cero. La positividad usa las masas límite positivas; no se divide por cantidades cuyo límite pudiera ser cero.

Además $T=\sum_{i\in L}f_i\geq c_u y_L$ para cada hoja, y alguna $y_L\geq1/4$. Las capacidades de los cortes A–B y C–W dan $T^2\leq y_Ay_By_Cy_W\leq1/256$. Queda el intervalo uniforme, deliberadamente conservador,

$$\frac{2u-1}{8}\leq T\leq\frac1{16}.\tag{5}$$

Para $u=3467/5000$, (4)–(5) dan $c_u=967/5000$ y $967/20000\leq T\leq1/16$. Estas cotas son consecuencias de las condiciones ya utilizadas, no un nuevo certificado o una mejora del umbral.

## 3. Cada corte iguala dos centros

Definir el momento por flujo de una hoja

$$D_L=\sum_{i\in L}f_i s_i.$$

Para un corte L→M, la cancelación principal de la auditoría anterior es

$$0=c_{LM}:=\sum_{i\in L,j\in M}a_{ij}(s_i-s_j)
=D_L-D_M.\tag{6}$$

La última igualdad usa **ambas** identidades de (1): las sumas por filas son los flujos salientes y las sumas por columnas son los entrantes de los clusters de M. Así $D_A=D_B=D_C=D_W$. Como W tiene un único cluster y $s_6=0$, se obtiene $D_W=Ts_6=0$ y todos los momentos son cero.

Los centros $D_L/T$ están definidos porque ya se probó $T>0$. No se divide aquí por cada $f_i$; su positividad individual es necesaria también para que los productos de flujo por masa usados después sean estrictamente positivos.

## 4. Por qué no desaparece la dirección variacional

Numerar las hojas divididas A, B, C por $L=0,1,2$. Escribir $\pi_L=f_{2L}/T\in(0,1)$ y $k_L=s_{2L+1}-s_{2L}$. La igualdad $D_L=0$ equivale a

$$s_{2L}=-(1-\pi_L)k_L,\qquad s_{2L+1}=\pi_L k_L.\tag{7}$$

Las tres parejas y W representan todos los offsets. Por (7),

$$1=\|s\|_\infty\leq\|k\|_\infty\leq2.\tag{8}$$

La primera desigualdad usa $0\leq\pi_L\leq1$ y la segunda, $|s_i|\leq1$. En particular, alguna diferencia principal es no nula. No hace falta que lo sean las tres.

Con $J_L=x_{2L}x_{2L+1}>0$ y $z_L=\sqrt{J_L}k_L$, se conserva una cota explícita por sucesión:

$$\|z\|^2=\sum_LJ_L k_L^2\geq\min_LJ_L>0.\tag{9}$$

Si todas las masas de esa sucesión están acotadas inferiormente en el límite por $\varepsilon>0$, el último miembro es al menos $\varepsilon^2$. No se anuncia un $\varepsilon$ común a todas las sucesiones de la clase.

La normalización posterior $m_i=x_i/\sqrt T$, $a'_{ij}=a_{ij}/T$ da flujo uno y masas brutas de suma $N=1/\sqrt T$. Conserva las densidades, los offsets y las fracciones de flujo. Ahora $J'_L=J_L/T$ y $\|z'\|^2=\|z\|^2/T>0$; no se pierde la dirección al cambiar escala. Los productos $\chi_L=\pi_L(1-\pi_L)/J'_L$ también son estrictamente positivos.

## 5. Qué valida el control algebraico

`verify_flow_centers.py` verifica por símbolos que un transporte de cuatro cortes con márgenes balanceados da (6), sin exigir que todas las entradas de cada transporte sean positivas. Comprueba la reconstrucción (7), el factor de escala y las constantes racionales de (4)–(5).

Con fracciones, vuelve a leer cuatro perfiles conservados y sus testigos finitos. El residuo exacto de cada testigo se comprueba antes del Hessiano; esos testigos no se modifican. La auditoría de flujos se ejecuta sobre los **perfiles principales**, no anunciando como equilibrio finito una lista de offsets.

Otros controles algebraicos cubren una, dos o tres diferencias internas no nulas y transportes con entradas cero. Solo comprueban equilibrio principal, cortes, capacidades y la conservación del vector. **No se afirma que estos controles sintéticos realicen equilibrios finitos estables ni satisfagan las dos formas variacionales.** Las condiciones que aquí se usan son necesarias y parciales. Se rechazan por separado un balance alterado, un corte alterado, una normalización nula y casos de flujo cero que no alcanzan el grado supuesto.

```text
python -B verify_flow_centers.py
```

Necesita SymPy de la caché externa existente. El JSON `flow_centers_verification.json` separa identidades universales, controles racionales y alcance. La demostración continua, incluida la extracción de subsucesiones, sigue siendo el argumento escrito. El comprobador no reejecuta el árbol, no acredita la novedad ni una revisión humana independiente.

Las masas límite nulas, la falta de anclaje, la ausencia de cancelaciones individuales o una normalización angular distinta requieren otro argumento. Por ejemplo, con hojas desconectadas pueden tenerse $h>0$ y las tres diferencias internas nulas; ese caso no cumple el grado alto usado en (4).

**Uso de IA:** deducción explícita, código y texto por Codex (OpenAI), sin subagentes. No cambia el enunciado ni los medios y paquetes congelados. Revisión humana independiente pendiente.
