# Cota 7/10 para siete clusters que se acercan a cuatro fases

19/10/2026. Deducción asistida por Codex, con certificado racional reproducido. **Modelo:** plantillas del Kuramoto homogéneo y grafos simples no dirigidos en el corolario. Novedad bibliográfica y revisión humana independiente pendientes.

La [caracterización anterior](perfil_general_cuatro_hojas.md) no daba una cota máxima para todos sus perfiles. Aquí se obtiene una cota superior de 0,70 para una clase asintótica más amplia. No exige mitades iguales, reflexión A/C, anchuras comparables, adyacencias principales positivas ni internos asintóticamente completos. Mantiene siete clusters de masas límite positivas que se agrupan en cuatro hojas de tamaños `(2,2,2,1)`.

Se volvió a consultar [O'Keeffe v1, III, IV.3 y A.2–A.4](https://arxiv.org/html/2610.21271v1) antes de formular el resultado. Se atribuyen a esa fuente la construcción S7 y la constante inferior $\mu_0\approx0.69290770637$. La prueba de esta nota combina una reducción analítica con una cobertura exacta de un dominio compacto. No determina la conectividad crítica general ni la mejor cota de esta clase.

## Teorema y alcance

Sean plantillas $(x^{(\ell)},\theta^{(\ell)},p^{(\ell)})$ de siete clusters, con masas positivas que suman uno, densidades simétricas en [0,1], equilibrio exacto y Hessiano de clusters positivo módulo rotación en cada elemento finito. Suponer, tras rotación, que

$$x_i^{(\ell)}\longrightarrow\bar x_i>0,\qquad
\theta_i^{(\ell)}\longrightarrow j_i\pi/2,\qquad j=(0,0,1,1,2,2,3).$$

Entonces

$$\limsup_\ell\mu(T_\ell)<\frac7{10},\qquad
\mu(T)=\min_i\sum_jx_jp_{ij}.\tag{T}$$

La positividad estricta se supone para los datos finitos; no se infiere de una matriz límite semidefinida. No se exige un margen uniforme ni una velocidad de convergencia. Las densidades pueden tener límites cero. No se cubren masas límite nulas, otras reparticiones de siete clusters, más fases o configuraciones alejadas de cuatro cuartos de vuelta.

Para el supremo de valores límite en esta clase, la construcción conocida y (T) dan el intervalo $[\mu_0,0.70]$. No se demuestra que ese supremo sea $\mu_0$.

## 1. Normalizar la separación y completar solo como relajación

Fijar W en $3\pi/2$ y poner $h_\ell=\max_i|\theta_i^{(\ell)}-j_i\pi/2|$. Este número es positivo: si todas las fases son exactamente las de C4, la semidefinitud obliga a vaciar los opuestos y quedan tres rotaciones adicionales de hojas con energía cero, contradiciendo positividad módulo rotación.

Tomar una subsucesión que realice el límite superior de grados, con densidades convergentes y desplazamientos reescalados $u_i=(\theta_i-j_i\pi/2)/h$ convergentes a $s_i$. La compacidad da $s_6=0$ y $\max_i|s_i|=1$.

La identidad exacta de equilibrio usada en [patron_principal_limite.md](patron_principal_limite.md) sigue valiendo con internos incompletos. Para hacer explícita la reducción, poner $a_{ij}^h=N^2x_ix_jp_{ij}$, $d_{ij}=u_i-u_j$ y $\sigma_{ij}=\sin((j_i-j_j)\pi/2)$ en las adyacencias. Multiplicar los residuos ponderados por $u_i$ y sumar da exactamente

$$\begin{aligned}
S_h&:=\sum_{\rm adj}a_{ij}^h\cos(\theta_i-\theta_j)\\
&=h\sum_{\rm int}a_{ij}^h d_{ij}\sin(hd_{ij})-h\sum_{\rm op}a_{ij}^h d_{ij}\sin(hd_{ij})\\
&\quad+\sum_{\rm adj}a_{ij}^h\sigma_{ij}[hd_{ij}\cos(hd_{ij})-\sin(hd_{ij})].
\end{aligned}$$

Las estimaciones $|\sin t-t|\leq|t|^3/6$ y $|t\cos t-\sin t|\leq|t|^3/3$ dan $S_h=O(h^2)$, porque los coeficientes y desplazamientos están acotados. Las rotaciones de hojas (1,0,−1,0) y (1,2,1,0) tienen diferencias de cuadrado uno en todas las adyacencias y de cuadrado cuatro, respectivamente, en A–C y B–W. Sus energías no negativas son $S_h-4\sum_{A-C}a_{ij}^h\cos(hd_{ij})$ y $S_h-4\sum_{B-W}a_{ij}^h\cos(hd_{ij})$. Los cosenos tienden a uno y las masas están acotadas inferiormente: todos los opuestos son $O(h^2)$.

Si $J_o$ es la diagonal de conductancias internas límite de las tres parejas, volver a la identidad da $S_h/h^2\to E_o=\sum (J_o)_{ii}k_i^2$, con $k_i$ las diferencias de offsets de cada pareja. El Hessiano restringido a los cuatro indicadores de hojas es semidefinido positivo y tiene traza $O(h^2)$. Su norma está acotada por la traza, por lo que cada entrada adyacente es $O(h^2)$; dividirla por $h$ da por separado los cuatro cortes principales nulos. El equilibrio a orden cero iguala los flujos entrantes y salientes.

Para una relajación de cota superior, **completar las densidades internas límite a uno**, incluidas las diagonales de plantilla. Esto aumenta los grados. No se afirma que esa modificación conserve un equilibrio finito. El equilibrio de orden cero y los cortes principales no cambian. Sean $J=\operatorname{diag}(m_0m_1,m_2m_3,m_4m_5)$ y $E=\sum J_{ii}k_i^2$, con masas brutas $m_i=N\bar x_i$.

El bloque cruzado $C$ solo depende de adyacencias principales. Para cada test modal escoger la corrección $\zeta=-J^{-1}C^Te_i$. Semidefinitud del dato original implica

$$0\leq E_o+2(C\zeta)_i+\zeta^TJ_o\zeta\leq E+2(C\zeta)_i+\zeta^TJ\zeta
=E-(CJ^{-1}C^T)_{ii}.$$

Se omitió un término opuesto no positivo, lo que solo relaja la condición. Si $J_o=\operatorname{diag}(\beta_iJ_i)$, la diferencia entre las dos expresiones es $\sum_i(1-\beta_i)J_i(k_i^2+\zeta_i^2)\geq0$. No se invierte $J_o$, que puede ser singular. Por tanto, las pruebas escalares del modelo completado son necesarias también para internos incompletos.

En el caso relevante para la contradicción, el flujo común y los flujos de cada mitad son positivos, como se justifica al comienzo del apartado 2. Entonces los cortes y el equilibrio implican que los centros ponderados por flujo de las cuatro hojas coinciden. W tiene offset cero. Si las tres diferencias internas fueran cero, todos los $s_i$ serían cero, imposible por la normalización. Así $E>0$, aunque una o dos de las separaciones principales sean nulas. Los casos de flujo cero se descartan por grado antes de usar este argumento.

## 2. Flujos y covarianzas

Para probar (T) por contradicción, suponer que el límite de grados originales es al menos $u=7/10$. El grado mínimo del perfil completado también lo es. En este apartado $N=\sum_i m_i$ y $M_A,M_B,M_C,g$ son las masas brutas de las cuatro hojas.

Orientar las adyacencias A→B→C→W→A. El equilibrio principal iguala, en cada nodo, sus flujos entrante y saliente; el flujo total de cada corte es un mismo $T$. Si $T=0$, el grado completado de cada nodo es solo la masa de su hoja y su mínimo no supera $N/4$. Si una mitad tiene flujo cero, su grado es la masa de su hoja, a lo sumo $(1-u)N$ por ausencia de opuestos. Ambos casos contradicen el grado mínimo supuesto. Luego $T>0$ y todas las mitades tienen flujo positivo.

Reescalar $m\mapsto m/\sqrt T$ y las conductancias $a\mapsto a/T$. Esto preserva densidades, grados normalizados y desigualdades de estabilidad; el flujo de cada corte pasa a uno. En la hoja $i$ sean $\pi_i,1-\pi_i$ sus fracciones de flujo, y $J_i$ el producto de sus masas. Definir

$$\chi_i=\frac{\pi_i(1-\pi_i)}{J_i}>0.$$

Los centros por flujo nulos fijan los offsets como $(-(1-\pi_i)k_i,\pi_i k_i)$. Para las dos matrices de transporte A–B y B–C, definir sus determinantes $d_{AB},d_{BC}$ y

$$\kappa=\frac{d_{AB}}{\sqrt{J_AJ_B}},\qquad
\lambda=\frac{d_{BC}}{\sqrt{J_BJ_C}},\qquad z_i=\sqrt{J_i}k_i.$$

Los dos tests necesarios de estabilidad se vuelven

$$\begin{aligned}
\|z\|^2&\geq \kappa^2z_B^2+(2\chi_Bz_B-\kappa z_A-\lambda z_C)^2+\lambda^2z_B^2,\\
\|z\|^2&\geq (2\chi_Az_A-\kappa z_B)^2+(\kappa z_A-\lambda z_C)^2+(2\chi_Cz_C-\lambda z_B)^2.
\end{aligned}\tag{1}$$

Aquí $z\neq0$; no se exige que sus tres coordenadas sean distintas de cero. Las identidades por pares y la transformación se comprueban simbólicamente en `verify_covariance_reduction.py`.

**Cota por capacidades.** Para una matriz de transporte de total uno, de entradas $a,b,c,d\geq0$, poner $D=ad-bc$ y $V=(a+b)(c+d)(a+c)(b+d)$. Si $D\geq0$,

$$V=(a-D)(d-D),\qquad
(\sqrt{ad}-D)^2-V=D(a+d-2\sqrt{ad})\geq0.$$

Como $\sqrt{ad}-D\geq0$, se obtiene $D+\sqrt V\leq\sqrt{ad}$. Las capacidades de las dos entradas diagonales dan $ad\leq J_{\rm izquierda}J_{\rm derecha}$. Para $D<0$ intercambiar las dos columnas. Además $V-D^2=ad(b+c)+bc(a+d)\geq0$. Dividir por los productos de masas prueba

$$|\kappa|+\sqrt{\chi_A\chi_B}\leq1,\quad |\kappa|\leq\sqrt{\chi_A\chi_B},\qquad
|\lambda|+\sqrt{\chi_B\chi_C}\leq1,\quad |\lambda|\leq\sqrt{\chi_B\chi_C}.\tag{2}$$

## 3. Reducir las masas a un cubo compacto

Sea $y_i=M_i/N$ la proporción de una hoja. Sin opuestos, cada grado completado es a lo sumo $N-M_{\rm opuesta}$, así que $y_i\leq1-u$. En una hoja dividida, escribir $\tau_0,\tau_1$ para flujo por masa de sus dos mitades. Su promedio ponderado por masas es $1/M_i$. Por tanto,

$$\min\tau\geq(uN-M_i)/2,\qquad \max\tau\geq1/M_i,$$
$$\chi_i=\tau_0\tau_1\geq\frac{uN-M_i}{2M_i}=\frac{u}{2y_i}-\frac12.$$

Para $u=7/10$, esto y (2) dan

$$\frac23\leq\chi_A,\chi_B,\chi_C\leq\frac32.\tag{3}$$

Definir las cotas inferiores de masas $\ell_i=u/(1+2\chi_i)$ y $s=1-\ell_A-\ell_B-\ell_C$. Se tiene $y_i\geq\ell_i$ y $0<y_W\leq s$.

Las adyacencias con W dan $\tau_0,\tau_1\leq g$, luego $\chi_A,\chi_C\leq g^2=N^2y_W^2$. Por otra parte, el grado mínimo no supera el promedio de grados en **cada** hoja dividida:

$$uN\leq M_i+2/M_i,\qquad N^2\leq\frac{2}{y_i(u-y_i)}.$$

Como $\ell_i\leq y_i\leq1-u<u/2$, la función $t(u-t)$ es creciente en ese intervalo. Se obtiene para las tres hojas

$$\max(\chi_A,\chi_C)\,\ell_i(u-\ell_i)\leq2s^2.
$$

Equivale a la condición necesaria

$$s\geq0,\qquad \max(\chi_A,\chi_C)\,\ell_{\max}(u-\ell_{\max})\leq2s^2,
\quad\ell_{\max}=\max(\ell_A,\ell_B,\ell_C).\tag{4}$$

No se identifica grado mínimo con promedio. Conservar solo el promedio de B deja una relajación demasiado amplia; el certificado final usa las tres restricciones.

## 4. Certificado de exclusión de (1)–(4)

Poner $a=\chi_A,b=\chi_B,c=\chi_C$ y $k=|\kappa|,l=|\lambda|$. Al combinar las dos desigualdades (1) con $0\leq\alpha\leq1$ aparece una matriz $M_\alpha$ tal que $z^TM_\alpha z\leq\|z\|^2$. Para covarianzas no negativas,

$$M_\alpha=\begin{pmatrix}
4(1-\alpha)a^2+k^2&-2k[\alpha b+(1-\alpha)a]&(2\alpha-1)kl\\
-2k[\alpha b+(1-\alpha)a]&4\alpha b^2+k^2+l^2&-2l[\alpha b+(1-\alpha)c]\\
(2\alpha-1)kl&-2l[\alpha b+(1-\alpha)c]&4(1-\alpha)c^2+l^2
\end{pmatrix}.$$

Los otros signos de covarianzas son congruentes mediante una diagonal de signos, así que tienen los mismos criterios de positividad.

El árbol de `profile_upper_certificate_070-v4.json` cubre el cubo (3) por bisecciones racionales. Contiene 9.971 nodos, 4.985 bisecciones y 4.986 hojas, con profundidad máxima 33. Cada hoja tiene una de estas justificaciones exactas:

- 148 contradicen una capacidad: $ab>1$ o $bc>1$.
- 2.580 contradicen (4), usando cotas racionales exteriores de las masas.
- 1.170 prueban $M_\alpha-I\succ0$ mediante una matriz de comparación y un vector racional positivo.
- 1.088 prueban $M_\alpha-I\succ0$ mediante los tres menores de Sylvester y coeficientes de Bernstein estrictamente positivos en cajas de $k^2,l^2$.

Para una caja $a\in[a_0,a_1]$, etc., (2) permite $0\leq k\leq1-\sqrt{a_0b_0}$ y $0\leq l\leq1-\sqrt{b_0c_0}$. Las raíces se acotan inferiormente por raíces enteras con denominador $10^8$, lo que **amplía** los intervalos de covarianzas. No hay redondeo flotante en la aceptación.

En las hojas de comparación se reemplazan las entradas fuera de la diagonal por el negativo de su valor absoluto. Las tres cotas de filas contra un vector racional positivo son estrictas; completar cuadrados demuestra positividad de la matriz de comparación y, por tanto, de la matriz original para cualquier signo. Los mínimos en $k,l$ de los términos cuadráticos se calculan exactamente, incluyendo posibles mínimos interiores.

En las otras hojas se conservan los signos de la matriz completa. Sus menores son polinomios de grado a lo sumo dos en cada variable $k^2,l^2$. Se subdivide cada intervalo en dos y se comprueban los nueve coeficientes tensoriales de Bernstein en cada subrectángulo. Son positivos por intervalos racionales; las bases de Bernstein son no negativas y suman uno, lo que prueba positividad en el continuo. Las fórmulas de los menores se verifican simbólicamente.

En ambos casos $M_\alpha-I\succ0$ contradice (1) porque $z\neq0$. La cobertura incluye los bordes de todas las cajas y todos los signos de covarianza. Excluir el cubo completo bajo (2) y (4) demuestra (T); no basta con no encontrar un candidato en una búsqueda.

## 5. Reproducción, controles y límites

```text
python -S verify_profile_upper_certificate.py
python verify_covariance_reduction.py
python -S profile_upper_certificate_checks.py
```

La primera y la tercera orden usan solo Python estándar. El verificador del árbol no importa el constructor, sus predicados, NumPy ni un solucionador espectral. Reconstruye cada caja desde la raíz y comprueba todas las hojas por fracciones, raíces enteras y coeficientes racionales. La segunda orden requiere SymPy y comprueba las identidades de transporte, normalización, combinación de formas y menores.

Los datos flotantes solo proponen $\alpha$ y vectores; nunca aceptan una hoja. El certificado de 0,71 anterior también pasó, pero fue reemplazado como cota principal por el de 0,70. Tres intentos incompletos de 0,70 agotaron profundidad; se conservaron sus registros y no se interpretaron como pruebas. Se corrigió primero la propuesta de vectores casi desacoplados y después se añadió el test de Bernstein para conservar el término entre A y C. No se ocultaron cajas sin resolver.

La suite de controles rechaza alteraciones del dominio, cobertura y desigualdades. Incluye el caso exactamente C4, de conectividad 3/4 y con ceros adicionales: no satisface la hipótesis estricta. No se clasifica su estabilidad no lineal a partir de esa semidefinitud.

Las exploraciones numéricas previas —60 arranques con escala, 16 sin ella y 20 en una proyección más débil— son registros separados de propuestas, no el certificado. Algunas terminaron sin converger o con restricciones violadas. Se conservan todos los resultados, límites y semillas. El teorema no depende de afirmar optimalidad de esos cálculos.

## Corolario para grafos simples

Sean grafos de orden creciente con un equilibrio constante en siete grupos y Hessiano positivo fuera de la rotación global. Suponer proporciones de grupos que tienden a valores positivos y fases que se acercan a los cuatro cuartos de vuelta con reparto `(2,2,2,1)`. Promediar por bloques, con $p_{ii}=2e(V_i)/n_i^2$, conserva equilibrio y positividad del Hessiano de clusters. No se necesitan bloques regulares ni hojas completas.

El grado de plantilla es el promedio de grados del grupo dividido por $n$, y $\delta/n\leq\mu(T)$. Por (T), $\limsup\delta/n<0.70$. Al tender $n$ a infinito, las diferencias de $(\delta+1)/n$ y $\delta/(n-1)$ con $\delta/n$ se anulan. No se identifica ninguna de esas normalizaciones a orden finito ni se acotan todos los grafos.

**Uso de IA:** Codex (OpenAI) realizó consulta, reducción, código, controles y texto. Constructor y verificadores proceden del mismo agente; su separación no constituye revisión humana independiente. No hubo subagentes, publicación, comunicaciones ni entrega al evento. Los medios y paquetes anteriores permanecen congelados y no incluyen este resultado.
