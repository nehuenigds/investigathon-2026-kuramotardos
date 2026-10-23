# Perfil general de cuatro hojas y mitades desiguales

19/10/2026. Deducción asistida por Codex. **Modelo:** plantillas ponderadas del Kuramoto homogéneo, con hojas de tamaños `(2,2,2,1)` cerca de cuatro fases separadas por cuartos de vuelta. No es una cota para todos los grafos ni para todas las configuraciones de siete fases. Novedad bibliográfica y revisión humana independiente pendientes.

Se releyeron III, IV.3 y A.2–A.4 de [O'Keeffe v1](https://arxiv.org/html/2610.21271v1). El artículo estudia el perfil simétrico, usa eliminación de modos internos y registra numéricamente una familia de mitades desiguales que parece alcanzar el mismo valor. Aquí se da un criterio para perfiles más generales y una prueba de esa propiedad en una deformación explícita. La construcción original, la constante y los métodos de ajuste y realización conservan su atribución. No se obtuvo un récord nuevo.

## 1. Datos y criterio

Las hojas son A={0,1}, B={2,3}, C={4,5}, W={6}. Fijar masas brutas $m_i>0$, $N=\sum_i m_i$, y desplazamientos $s_i$, con $s_6=0$ tras rotación. Exigir las tres separaciones $k_A=s_1-s_0$, $k_B=s_3-s_2$, $k_C=s_5-s_4$ distintas de cero. Las fases principales son $j_i\pi/2$, con $j=(0,0,1,1,2,2,3)$.

Orientar las doce adyacencias según A→B→C→W→A, en el orden

$$\mathcal E=((0,2),(0,3),(1,2),(1,3),(2,4),(2,5),(3,4),(3,5),(4,6),(5,6),(6,0),(6,1)).$$

Asignar conductancias principales $a_{ij}$ con $0<a_{ij}\leq m_im_j$. La densidad principal es $p_{ij}=a_{ij}/(m_im_j)$. Los enlaces dentro de cada hoja, incluidas las diagonales de plantilla, tienen límite uno. No fijamos inicialmente la escala de los opuestos en las sucesiones que se van a acotar.

Sea $B$ la incidencia orientada, con +1 en la cola y −1 en la cabeza. Definir las condiciones lineales

$$Ba=0,\qquad c_\nu:=\sum_{(i,j)\in\mathcal E:\,j_i=\nu}a_{ij}(s_i-s_j)=0\quad(\nu=0,1,2,3).\tag{1}$$

Sean $U$ y $Z$ las siguientes matrices de siete filas y tres columnas. Las filas de $U$ son constantes por hoja, con valores

$$U_A=(1,1,1),\quad U_B=(0,2,0),\quad U_C=(-1,1,1),\quad U_W=(0,0,0),$$

y las columnas de $Z$ valen $(-1/2,1/2)$ en las dos mitades de su hoja y cero en las demás. Escribir

$$J=\operatorname{diag}(m_0m_1,m_2m_3,m_4m_5),\qquad E=\sum_{\nu=A,B,C}J_{\nu\nu}k_\nu^2,$$
$$C=\sum_{(i,j)\in\mathcal E}a_{ij}(s_i-s_j)(U_i-U_j)^T(Z_i-Z_j),\qquad P=CJ^{-1}C^T.$$

La letra $P$ en esta fórmula designa una matriz modal de 3×3; las densidades se escriben $p_{ij}$ para evitar confundirlas. Las tres pruebas escalares son

$$\Delta_\alpha=E-P_{\alpha\alpha}\geq0,\qquad\alpha=1,2,3.\tag{2}$$

**Teorema.** Bajo las condiciones de positividad y separaciones anteriores, (1) y (2) son equivalentes a la existencia de una sucesión de plantillas en equilibrio exacto y con Hessiano de clusters semidefinido positivo, tal que

$$h_\ell\to0,\quad x_i^{(\ell)}\to m_i/N,\quad
\theta_i^{(\ell)}=j_i\pi/2+h_\ell u_i^{(\ell)},\quad u_i^{(\ell)}\to s_i,$$

las adyacencias convergen a $p_{ij}$ y los enlaces de cada hoja convergen a uno. No se exigen derivadas ni tasas de convergencia. Además, cuando las condiciones se cumplen, se puede elegir la sucesión con masas exactamente $m/N$, internos completos, **todos los opuestos cero**, fuerzas internas positivas y Hessiano estrictamente positivo módulo rotación en cada elemento finito.

La equivalencia caracteriza perfiles en esta clase; no demuestra que su conectividad máxima general sea $\mu_0$. Tampoco afirma estabilidad estricta de una matriz límite semidefinida.

## 2. Necesidad sin derivadas

Usar la identidad exacta y las cotas trigonométricas de [patron_principal_limite.md](patron_principal_limite.md), ahora con masas y desplazamientos principales arbitrarios. Poner $a_{ij}^{(\ell)}=N^2x_i^{(\ell)}x_j^{(\ell)}p_{ij}^{(\ell)}$. La suma $S_h$ de los pesos adyacentes del Hessiano bruto satisface

$$S_h=h^2\left(\sum_{\mathrm{internos}}a_{ij}^{(h)}(u_i-u_j)^2-
                    \sum_{\mathrm{opuestos}}a_{ij}^{(h)}(u_i-u_j)^2\right)+O(h^3).$$

Los datos reescalados están acotados. Las rotaciones de hojas (1,0,−1,0) y (1,2,1,0) tienen diferencias de cuadrado uno en todas las adyacencias, y de cuadrado cuatro respectivamente en A–C y B–W. Semidefinitud obliga a que todos los opuestos sean $O(h^2)$. Por tanto,

$$S_h/h^2\longrightarrow E.\tag{3}$$

El límite de equilibrio de orden cero da $Ba=0$. Para las condiciones de corte hay que justificar algo más que la suma de los cuatro cortes. Restringir el Hessiano a los cuatro indicadores de hojas produce una matriz semidefinida positiva de traza

$$2S_h-2\sum_{\mathrm{opuestos}}a_{ij}^{(h)}\cos(h(u_i-u_j))=O(h^2).$$

Su norma de operador está acotada por esa traza, así que cada entrada es $O(h^2)$. La entrada de dos hojas adyacentes es el negativo de la suma de sus pesos de Hessiano. Dividirla por $h$ y pasar al límite da cada $c_\nu=0$. No se supuso una expansión diferenciable de esos pesos.

Los bloques $Z^T(N^2H)Z$ y $h^{-1}U^T(N^2H)Z$ convergen a $J$ y $C$. Para cada columna $U_\alpha$ usar la variación

$$U_\alpha-hZJ^{-1}C^Te_\alpha.$$

Su energía dividida por $h^2$, junto con (3), da

$$\begin{aligned}
0&\leq\Delta_1-4\sum_{A-C}m_im_jp_{ij}^{(h)}/h^2+o(1),\\
0&\leq\Delta_2-4\sum_{B-W}m_im_jp_{ij}^{(h)}/h^2+o(1),\\
0&\leq\Delta_3+o(1).
\end{aligned}$$

Los opuestos no aportan a la tercera rotación, que toma el mismo valor en cada pareja de hojas opuestas. Se deduce (2) y, adicionalmente, las dos cotas de límite superior ponderadas por $\Delta_1/4$ y $\Delta_2/4$. Las sustituciones de masas límite son válidas porque las razones opuestas por $h^2$ ya están acotadas.

## 3. Completar el bloque agregado equivale a tres escalares

Sean $b_0,b_1,b_2,b_3$ los pesos agregados de Hessiano a orden $h^2$ en A–B, B–C, C–W y W–A. Pueden tener ambos signos. En la base modal $U$, la matriz del Laplaciano del ciclo tiene las tres diagonales iguales a $b_0+b_1+b_2+b_3$. La identidad de equilibrio fija esa suma en $E$.

Para cualquier matriz simétrica $P$ hay una elección única de pesos con suma $E$ y entradas fuera de la diagonal iguales a las de $P$:

$$\begin{aligned}
b_0&=(E-P_{12}+P_{13}-P_{23})/4,\\
b_1&=(E+P_{12}-P_{13}-P_{23})/4,\\
b_2&=(E-P_{12}-P_{13}+P_{23})/4,\\
b_3&=(E+P_{12}+P_{13}+P_{23})/4.
\end{aligned}\tag{4}$$

Entonces el complemento de Schur es exactamente $\operatorname{diag}(\Delta_1,\Delta_2,\Delta_3)$. Recíprocamente, cualquier complemento positivo exige las tres diagonales no negativas. Esto prueba la equivalencia para el bloque agregado; aún hay que realizar los pesos mediante densidades compatibles con equilibrio.

## 4. Realizar la completación y levantar a datos finitos

Supongamos primero $0<p_{ij}<1$ y $\Delta_\alpha>0$. Sea $L_I$ el Laplaciano de las tres parejas internas, de pesos $m_0m_1,m_2m_3,m_4m_5$. Para un predictor de conductancias $a+hy$, el equilibrio a primer orden requiere

$$By=L_Is.\tag{5}$$

Se resuelve sobre cualquier árbol adyacente porque el segundo miembro suma cero. Si $\widetilde b_\nu=\sum_{\mathcal E_\nu}y_{ij}(s_i-s_j)$, entonces

$$\sum_\nu\widetilde b_\nu=s^TBy=s^TL_Is=E.$$

Tres circulaciones conservan (5): sustituir la mitad menos por la mitad más de A, B o C en el ciclo A–B–C–W. Sus efectos sobre los cuatro pesos agregados son las columnas de

$$\begin{pmatrix}
k_A&-k_B&0\\0&k_B&-k_C\\0&0&k_C\\-k_A&0&0
\end{pmatrix}.$$

Las primeras tres filas tienen determinante $k_Ak_Bk_C\neq0$. Se puede por tanto modificar el predictor para obtener exactamente los cuatro valores (4), sin cambiar equilibrio a primer orden. Esta libertad es esencial; completar una matriz sin comprobarla no bastaría.

Elegir fases $j_i\pi/2+hs_i$ o, para datos racionales, $j_i\pi/2+2\arctan(hs_i/2)$. La segunda elección cambia las fases solo en $O(h^3)$ y da coordenadas racionales del círculo. El predictor deja residuo de equilibrio $O(h^2)$. Corregirlo sobre un árbol de adyacencias usa senos que tienden a ±1, por lo que cambia las densidades en $O(h^2)$, conserva simetría y mantiene los opuestos cero. Como las densidades principales son interiores, para $h$ pequeño siguen dentro de (0,1).

La corrección cambia el bloque de Hessiano reescalado solo en $O(h)$: las adyacencias tienen coseno $O(h)$. En las coordenadas $U\eta+hZ\zeta$, la energía dividida por $h^2$ converge a una matriz con bloque interno $J\succ0$ y complemento de Schur $\operatorname{diag}(\Delta_1,\Delta_2,\Delta_3)\succ0$. La transformación es invertible en el gauge W=0 para $h>0$, así que el Hessiano finito es positivo módulo rotación. Las fuerzas internas tienden a la masa total de la propia hoja dividida por $N$, positiva. Esto demuestra la existencia estricta, no solo una completación formal.

Para admitir $p_{ij}=1$ y ceros en (2), sustituir primero $a$ por $\rho a$ con $0<\rho<1$. Se conservan (1), $E$ y $J$, mientras $C$ se multiplica por $\rho$. Luego

$$\Delta_\alpha(\rho)=E-\rho^2P_{\alpha\alpha}>0.$$

Todas las adyacencias quedan interiores. Para cada $\rho_\ell\uparrow1$ aplicar el argumento estricto y escoger $h_\ell<1/\ell$ suficientemente pequeño. Esta elección diagonal produce la sucesión del teorema para el perfil original. No proporciona aquí una cota uniforme explícita de $h$ para todos los perfiles.

## 5. Una familia exacta de mitades desiguales

Fijar $r>0$, $0<q<1$, $w>0$ y

$$\frac{1-q}{2}<t<\frac{1+q}{2}.$$

Definir $q_t=1-(1-q)/(2t)$, $q_{1-t}=1-(1-q)/(2(1-t))$ y

$$m=(2rt,2r(1-t),2(1-t),2t,2rt,2r(1-t),1+q),\quad N=4r+3+q,$$
$$s=(-(1-t),t,-tw,(1-t)w,-(1-t),t,0).$$

Las cuatro adyacencias cruzadas (0,3),(1,2),(2,5),(3,4) tienen densidades $q_t,q_{1-t},q_{1-t},q_t$; las otras ocho son uno. Con $a_{ij}=m_im_jp_{ij}$ se cumplen (1). La asimetría está ligada por estas fórmulas; no se permite escoger independientemente todas las masas o densidades en este corolario.

Con $K=1+2q-q^2$ y los polinomios $D,R$ de [optimalidad_global.md](optimalidad_global.md), el cálculo exacto da

$$\Delta_1=2t(1-t)D,\quad\Delta_2=2t(1-t)R,\quad
\Delta_3=2t(1-t)(4r^2+Kw^2)>0.\tag{6}$$

Los grados tampoco dependen de $t$. La conectividad límite es

$$\mu_\infty=\frac{\min\{2r+2+2q,\,2+2r(1+q),\,4r+1+q\}}{4r+3+q}.$$

**Corolario.** Esta familia de perfiles de mitades desiguales es aproximable por equilibrios estrictos si y solo si $D,R\geq0$. Su máximo global es $\mu_0$, por el teorema algebraico anterior. La igualdad exige $r=1,q=a,w=w_*$, pero permite todo $t$ del intervalo indicado. Para $t=1/2$ se recupera el perfil simétrico mediante un cambio común de escala de $h$.

La suficiencia usa la elección diagonal del apartado 4. Esto demuestra una familia exacta que confirma la observación numérica citada de IV.3, sin atribuirse su descubrimiento. No demuestra que todos los perfiles del apartado 1 tengan máximo $\mu_0$.

## 6. Evidencia y reproducción

`verify_general_quarter_profile.py` comprueba con SymPy la completación (4), las tres circulaciones, su rango, la recuperación de los dos polinomios anteriores y (6), además de la independencia de los grados respecto de $t$. El determinante se comparó inicialmente por igualdad estructural entre formas factorizadas distintas; se corrigió a comprobar diferencia polinómica nula.

`general_quarter_profile_checks.py` usa solo Python estándar. Cuatro ejemplos pasan el verificador de equilibrio exacto, fuerzas internas y LDL del gauge completo de dimensión seis. Tres tienen $t=1/5,1/2,4/5$, masas desiguales, $\rho=999999/10^6$ y $h=10^{-10}$; sus conectividades son aproximadamente 0.69290724633, por debajo de $\mu_0$ y del testigo simétrico mejor del cuaderno. El cuarto usa masas y adyacencias fuera de la subfamilia ligada y tiene conectividad menor. Se rechazan cinco alteraciones de equilibrio principal, corte, prueba escalar, caja de densidades y equilibrio finito. Los pivotes LDL no se interpretan como autovalores. Estos casos no prueban los cuantificadores del teorema: lo hace el argumento anterior.

La búsqueda `general_profile_search_20261019-general-v1` ensayó 24 arranques de SLSQP, semilla 76193, hasta 400 iteraciones por arranque. Permitió siete masas, tres fracciones de flujo, dos transportes y dos razones de anchura libres, con límites guardados. Todos terminaron numéricamente cerca de $\mu_0$; las pequeñas diferencias de unas $10^{-15}$ no se presentan como mejoras. Los residuos numéricos y salidas completas se conservan. No es una búsqueda exhaustiva ni una prueba de cota para el perfil general.

```text
python -S general_quarter_profile_checks.py
python verify_general_quarter_profile.py
python verify_global_optimum.py
```

La primera orden no usa bibliotecas externas; las otras necesitan SymPy. Constructor y verificadores proceden del mismo agente. No equivalen a revisión independiente.

**Uso de IA:** Codex (OpenAI) realizó relectura, deducción, programación, controles, búsqueda y texto. No hubo subagentes, revisión humana independiente, publicación ni comunicaciones. Los medios y paquetes congelados anteriormente no se modificaron para incluir esta ampliación.
