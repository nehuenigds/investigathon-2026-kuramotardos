# Cota asintótica 0,6934 por flujos y masas vecinas

21/10/2026. Deducción y comprobaciones asistidas por Codex. Modelo: Kuramoto homogéneo, plantillas ponderadas de siete clusters y corolario para grafos simples no dirigidos. Novedad bibliográfica y revisión humana independientes pendientes.

Se volvió a consultar [O'Keeffe v1, IV.3](https://arxiv.org/html/2610.21271v1) antes de formular el resultado. La ficha seguía mostrando solo v1. La construcción y el extremo inferior conocido $\mu_0\approx0.69290770637$ se atribuyen a esa fuente. Esta nota refuerza la [cota 0,6935](cota_capacidades_agregadas.md), usando la [desigualdad adicional de flujos por masa](cota_flujos_por_masa.md).

## Teorema y alcance

Sean plantillas homogéneas de siete clusters en equilibrio exacto, con masas positivas que suman uno, densidades simétricas en [0,1] y Hessiano positivo fuera de la rotación global en cada elemento finito. Suponer, tras una rotación común, que

$$x_i^{(\ell)}\longrightarrow\bar x_i>0,\qquad \theta_i^{(\ell)}\longrightarrow j_i\pi/2,\qquad j=(0,0,1,1,2,2,3).$$

Entonces, para $\mu(T)=\min_i\sum_jx_jP_{ij}$,

$$\boxed{\limsup_\ell\mu(T_\ell)<\frac{3467}{5000}=0.6934.}\tag{T}$$

Se admiten mitades desiguales, falta de reflexión, internos incompletos, adyacencias límite cero y separaciones en distintas escalas. La estricta hipótesis es finita; una matriz límite semidefinida no se clasifica como estrictamente estable. No se cubren masas límite nulas, otros repartos de clusters, más fases ni geometrías alejadas de los cuatro cuartos de vuelta. No es una cota superior universal para la conectividad crítica de Kuramoto.

La construcción conocida y (T) sitúan el supremo de valores límite de esta clase en $[\mu_0,0.6934]$. El intervalo tiene ancho menor que 0,000493. No se demuestra que el supremo sea $\mu_0$ ni que se alcance el extremo superior.

## 1. Reducción analítica utilizada

Se emplea íntegramente la reducción de [cota_perfil_general.md](cota_perfil_general.md), con umbral genérico $2/3<u<3/4$. La identidad exacta de equilibrio y la positividad del Hessiano fuerzan opuestos $O(h^2)$, cuatro cancelaciones principales y un vector variacional $z\ne0$. Los casos de flujo cero se excluyen por grado **antes** de tomar centros por flujo. Completar internos se usa solo como relajación de grado y estabilidad; no se afirma que esa operación preserve un equilibrio finito.

Normalizar el flujo común a uno. Para las hojas A, B, C y W sean $M_A,M_B,M_C,g$ las masas brutas, $N$ su suma, $y_i=M_i/N$ y $a,b,c$ los tres productos de flujo por masa. Las covarianzas normalizadas $\kappa,\lambda$ satisfacen

$$|\kappa|+\sqrt{ab}\leq1,\quad |\kappa|\leq\sqrt{ab},\qquad |\lambda|+\sqrt{bc}\leq1,\quad |\lambda|\leq\sqrt{bc}.$$

Las dos formas de estabilidad, su matriz convexa y sus menores son exactamente los de la nota base. Para el hipotético grado mínimo al menos $u$ se tiene

$$a,b,c\in[\eta,\eta^{-1}],\qquad \eta=\frac{2u-1}{2(1-u)},\qquad \frac{u}{1+2\chi_i}\leq y_i\leq1-u.$$

Las capacidades hacia W dan también $y_A,y_C,y_W\geq u-1/2$. Se mantienen las cuatro capacidades agregadas de cortes y la misma escala $N^2$ que limita los grados. No se iguala grado mínimo con promedio.

## 2. Refuerzo que permite bajar la cota

Para cualquier hoja dividida, con flujos $f_0+f_1=1$, masas $m_0,m_1$ y $\tau_i=f_i/m_i$, una hoja vecina de masa $B$ impone $\tau_i\leq B$. La identidad

$$B-\tau_0\tau_1(m_0+m_1)=m_0\tau_0(B-\tau_1)+m_1\tau_1(B-\tau_0)\geq0$$

produce las seis condiciones necesarias

$$a y_A\leq y_B,y_W,\qquad b y_B\leq y_A,y_C,\qquad c y_C\leq y_B,y_W.\tag{1}$$

En una caja $[a_0,a_1]\times[b_0,b_1]\times[c_0,c_1]$, iniciar

$$A_0=\max\left(\frac{u}{1+2a_1},u-\frac12\right),\quad B_0=\frac{u}{1+2b_1},\quad C_0=\max\left(\frac{u}{1+2c_1},u-\frac12\right)$$

y propagar

$$L_B=\max(B_0,a_0A_0,c_0C_0),\quad L_A=\max(A_0,b_0L_B),\quad L_C=\max(C_0,b_0L_B),\quad L_W=\max(u-\tfrac12,a_0L_A,c_0L_C).\tag{2}$$

Cada paso conserva $L_i\leq y_i$. Se excluye la caja si $\max L_i>1-u$ o $\sum L_i>1$. Solo en el caso restante se usa la monotonía de $t(u-t)$ en $[0,1-u]$. Poniendo

$$D=\max_i L_i(u-L_i),\quad s=1-L_A-L_B-L_C,\quad R_{pq}=1-L_r-L_s,$$

con $r,s$ las otras hojas de cada corte adyacente $pq$, siguen siendo necesarias

$$\max(a,c)D\leq2s^2,\qquad R_{pq}^2\geq2D.$$

Sus deducciones, a partir de $N^2\leq2/D$, $N^2\geq4/R_{pq}^2$ y las capacidades hacia W, son las de la nota 0,6935. El cambio consiste en conservar las masas vecinas en (2). Los otros dos predicados de escala implementados no aparecen en ninguna hoja del certificado y no se necesitan para su conclusión.

## 3. Cobertura racional completa

Para $u=3467/5000$, se cubrió el cubo exacto $[967/1533,1533/967]^3$ con 15.511 nodos, 7.755 bisecciones y 7.756 hojas, profundidad máxima 42:

| Exclusión | Hojas |
| --- | ---: |
| Capacidades de covarianzas | 88 |
| Suma de masas tras propagación (2) | 57 |
| Cota ligada a W | 1.858 |
| Capacidad total de un corte | 1.739 |
| Matriz de comparación con vector racional positivo | 2.362 |
| Menores de Sylvester por Bernstein racional | 1.652 |

Todas las hojas de Bernstein usan una subdivisión en dos de cada intervalo de covarianzas al cuadrado. El constructor ensayó refinamientos mayores en cajas que aún no podía cerrar, pero ninguno fue necesario en hojas aceptadas. Las cotas de raíces usan raíces enteras con denominador $10^8$ y amplían el dominio. Toda aceptación es racional y estricta; los autovalores flotantes solo proponen coeficientes y vectores. Los bordes de cajas y todos los signos de covarianzas quedan cubiertos.

`verify_profile_upper_mass_flow.py` reprodujo la raíz, la partición y todas las hojas con Python estándar. No importa constructor, predicados, NumPy ni un solucionador espectral. El archivo completo es `profile_upper_certificate_06934-v1.json`, SHA-256 `2e0beb78e67adec883d4a5bb9e5feab063958976b3b1253f7c7739db851e84f3`. La construcción terminó el 20/10 y tardó unos 1.212 segundos; la reproducción separada se realizó el 21/10. No queda ninguna caja sin resolver.

La cobertura excluye grado límite al menos $u$ bajo las condiciones necesarias anteriores y las dos formas de estabilidad, lo que concluye (T). La reducción analítica es parte de la prueba; contar nodos o no hallar contraejemplos no la sustituye.

## 4. Reproducción, controles y barrera restante

```text
python -B -S verify_profile_upper_mass_flow.py
python -B -S profile_upper_mass_flow_checks.py
python -B -S mass_flow_lemma_checks.py
python -B verify_covariance_reduction.py
python -B verify_global_optimum.py
```

Las tres primeras órdenes usan Python estándar; las dos simbólicas requieren SymPy. El último teorema reproduce el intervalo de referencia anterior para $\mu_0$, sin usarlo para excluir 0,6934. Ese intervalo da exactamente $0.000492<0.6934-\mu_0<0.000493$.

Los controles del árbol comprueban cobertura y desigualdades, rechazan seis alteraciones de dominio, ramas o justificaciones y conservan tres perfiles racionales finitos estrictos. Los controles del lema conservan otros cuatro testigos previos y sus 24 desigualdades, revalidando equilibrio exacto antes de estabilidad. Los ejemplos no sustituyen el cuantificador continuo.

El punto racional de [la nota de flujos](cota_flujos_por_masa.md) sigue mostrando una limitación de esta relajación: satisface sus desigualdades a 0,6932 y a 0,69291. No es una plantilla de Kuramoto ni un nuevo récord. Por ello el certificado 0,6934 no sugiere que baste subdividir más para obtener $\mu_0$; hacen falta restricciones adicionales para alcanzar esos umbrales.

## Corolario para grafos simples

Para grafos de orden creciente con equilibrio constante en siete grupos, proporciones límite positivas, fases límite indicadas y Hessiano completo positivo fuera de la rotación, agregar por promedios con $P_{ii}=2e(V_i)/n_i^2$. El grado de plantilla es el promedio del grupo dividido por $n$ y $\delta/n\leq\mu(T)$. Por (T), $\limsup\delta/n<0.6934$. Las normalizaciones $(\delta+1)/n$ y $\delta/(n-1)$ tienen la misma cota solo al tender $n$ a infinito. No se exigen bloques regulares ni se acotan todos los grafos.

**Uso de IA:** Codex (OpenAI) realizó consulta, deducción, código, cálculos, controles y texto. Constructor y verificadores proceden del mismo agente y no equivalen a revisión humana independiente. No hubo subagentes, comunicaciones, publicación ni entrega al evento. La novedad y la revisión del argumento analítico siguen pendientes. Los paquetes anteriores se conservan congelados.
