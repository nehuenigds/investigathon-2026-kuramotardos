# Cota asintótica 0,6935 mediante capacidades agregadas

19/10/2026. Deducción asistida por Codex, con cobertura racional reproducida. **Modelo:** Kuramoto homogéneo; plantillas de siete clusters y corolario para grafos simples no dirigidos. Novedad bibliográfica y revisión humana independiente pendientes.

Esta nota refuerza la [cota 0,70](cota_perfil_general.md) conservando las capacidades totales de los cuatro cortes entre hojas. Mantiene su clase asintótica, sin imponer el patrón simétrico del artículo. Se releyó [O'Keeffe v1, IV.3](https://arxiv.org/html/2610.21271v1) antes de formular la ampliación. La construcción y el valor inferior conocido $\mu_0\approx0.69290770637$ se atribuyen a esa fuente.

## Resultado

Sean plantillas homogéneas de siete clusters en equilibrio exacto, con densidades simétricas en [0,1] y Hessiano finito positivo fuera de la rotación global. Suponer masas que convergen a valores positivos y fases que, tras rotación, convergen a

$$j_i\pi/2,\qquad j=(0,0,1,1,2,2,3).$$

Entonces

$$\boxed{\limsup_\ell\mu(T_\ell)<\frac{1387}{2000}=0.6935},\qquad
\mu(T)=\min_i\sum_jx_jp_{ij}.$$

Se admiten mitades desiguales, internos incompletos, densidades límite cero y separaciones en distintas escalas. No se cubren masas límite nulas, otras reparticiones de siete clusters, más fases o configuraciones alejadas de cuatro cuartos de vuelta. La hipótesis estricta es finita; no se clasifica un límite semidefinido como estrictamente estable.

La construcción conocida y esta cota dejan el supremo de valores límite de esta clase en $[\mu_0,0.6935]$. El ancho es menor que 0,000593. No se prueba que el supremo sea $\mu_0$ ni se determina la conectividad crítica general.

## 1. Reducción de equilibrio y estabilidad

Se usa la reducción analítica de la nota 0,70, con un umbral genérico $2/3<u<3/4$. Para explicitar el orden lógico, primero se plantea la contradicción de grado límite al menos $u$ y se completan los internos **solo como relajación**. El equilibrio principal y los cortes no cambian, aumentan los grados y se relajan las pruebas variacionales del Hessiano. No se afirma que completar internos conserve un equilibrio finito.

Los casos de flujo total cero o de una mitad con flujo cero se descartan por grado antes de tomar centros ponderados por flujo. En el caso restante todos esos flujos son positivos. Los cortes obligan a que los centros de offsets por flujo coincidan con W, fijada a cero. Normalizar por la máxima desviación angular asegura un offset principal no nulo; si las tres separaciones internas fueran nulas todos los offsets serían cero. Por tanto, el vector de pruebas variacionales $z$ no es nulo, aunque alguna de sus coordenadas pueda ser cero.

La versión vigente de la nota 0,70 aclara esta dependencia de positividad de flujos. Se conserva su texto previo en `cota_perfil_general-070-v1.md` y en el kit antiguo. No se cambió el certificado 0,70 ni se presenta esta aclaración como una nueva comprobación de sus datos.

Normalizar el flujo común a uno. Sean $M_A,M_B,M_C,g$ las masas brutas de las hojas y $N$ su suma. Poner $y_i=M_i/N$, con $M_W=g$, y $\chi_A,\chi_B,\chi_C$ los cocientes de varianzas definidos en la nota base. Las covarianzas normalizadas satisfacen

$$|\kappa|+\sqrt{\chi_A\chi_B}\leq1,\qquad
|\lambda|+\sqrt{\chi_B\chi_C}\leq1.$$

Las dos pruebas necesarias de estabilidad son

$$\begin{aligned}
\|z\|^2&\geq\kappa^2z_B^2+(2\chi_Bz_B-\kappa z_A-\lambda z_C)^2+\lambda^2z_B^2,\\
\|z\|^2&\geq(2\chi_Az_A-\kappa z_B)^2+(\kappa z_A-\lambda z_C)^2+(2\chi_Cz_C-\lambda z_B)^2.
\end{aligned}\tag{1}$$

Los argumentos de grado y capacidades dan, como antes,

$$\chi_i\in[\eta,\eta^{-1}],\quad\eta=\frac{2u-1}{2(1-u)},\qquad
y_i\geq\ell_i:=\frac{u}{1+2\chi_i},\qquad y_i\leq1-u.$$

Para $u=1387/2000$, el cubo exacto es $[387/613,613/387]^3$.

## 2. Cotas inferiores de masas y escala común

Las capacidades hacia W implican que los grados completados de A y C no superan $M_A+2g$ y $M_C+2g$. Las capacidades agregadas $1\leq gM_A,gM_C$ también dan que el grado de W, $g+2/g$, no supera $g+2M_A$ ni $g+2M_C$. Como todas las masas proporcionales son a lo sumo $1-u$,

$$y_A,y_C,y_W\geq u-\tfrac12.$$

Definir cuatro cotas inferiores

$$L_A=\max(\ell_A,u-\tfrac12),\quad L_B=\ell_B,\quad
L_C=\max(\ell_C,u-\tfrac12),\quad L_W=u-\tfrac12.$$

Se tiene $0<L_i\leq y_i\leq1-u<u/2$, así que $\sum L_i\leq1$. En cada hoja el grado mínimo es menor o igual que el promedio $M_i+2/M_i$; para W ese es el grado exacto. Luego

$$N^2\leq\frac{2}{y_i(u-y_i)}\quad(i=A,B,C,W).$$

La función $t(u-t)$ es creciente en [0,1−u]. Por tanto, si

$$D=\max_{i=A,B,C,W}L_i(u-L_i),$$

se obtiene $N^2\leq2/D$. No se iguala grado mínimo con promedio.

Poniendo $s=1-L_A-L_B-L_C$, las capacidades individuales con W dan otra condición necesaria:

$$\max(\chi_A,\chi_C)D\leq2s^2.\tag{2}$$

## 3. Capacidades totales de los cuatro cortes

El flujo de cada corte adyacente es uno. Sus densidades no superan uno, de modo que

$$1\leq M_pM_q=N^2y_py_q\qquad(pq=AB,BC,CW,WA).$$

Si $r,s$ son las otras dos hojas, definir $R_{pq}=1-L_r-L_s$. Como $y_p+y_q\leq R_{pq}$, la desigualdad elemental de producto a suma fija da

$$y_py_q\leq R_{pq}^2/4,\qquad N^2\geq4/R_{pq}^2.$$

Combinar ambas cotas de $N^2$ produce las cuatro restricciones nuevas

$$\boxed{R_{pq}^2\geq2D\quad(pq=AB,BC,CW,WA).}\tag{3}$$

Las capacidades parciales de cada enlace ya estaban presentes en las cotas de covarianzas. Aquí se retiene además su capacidad **total**, ligada a la misma escala $N^2$ que los grados de las cuatro hojas. Omitir esa ligadura deja una relajación más amplia.

El código exploró también $2\chi_BD\leq(1-L_B-L_W)^2$ y $\chi_iR_{\min}^2\geq(u-U_i)^2$, con $U_i=\min(1-u,1-\sum_{j\ne i}L_j)$. La primera sigue de $\chi_B\leq N^2\min(y_A,y_C)^2$ y la segunda de $\chi_i\geq N^2(u-y_i)^2/4$. El certificado final no tiene hojas de esos dos tipos; no son necesarias para su conclusión.

## 4. Verificar el continuo

`profile_upper_certificate_06935-v1.json` cubre el cubo completo mediante 11.469 nodos, 5.734 bisecciones y 5.735 hojas, con profundidad máxima 36:

| Exclusión exacta | Hojas |
| --- | ---: |
| Capacidad de covarianzas | 102 |
| Suma de cotas inferiores de masas | 9 |
| Condición (2) | 1.148 |
| Capacidad total de un corte, (3) | 1.567 |
| Matriz de comparación racional | 2.125 |
| Menores de Sylvester por Bernstein racional | 784 |

En una caja de los tres cocientes, las funciones $L_i$ se acotan inferiormente usando los extremos superiores de $\chi_i$. Eso acota $D$ inferiormente y los $R_{pq}$ y $s$ superiormente. Todas las exclusiones se hacen con desigualdad estricta en la dirección que descarta la caja completa. Los bordes no se omiten.

Las hojas matriciales combinan (1) con un coeficiente racional $\alpha\in[0,1]$ y prueban que $M_\alpha-I$ es definido positivo para todas las covarianzas admitidas. La matriz y sus menores son los de la nota base. Se comprueban todos los signos de covarianzas mediante congruencias de signos y, en las cotas, matrices de comparación. Las raíces se acotan con raíces enteras y denominador $10^8$; las operaciones aceptadas son racionales.

`verify_profile_upper_capacity.py` no importa constructor, predicados, NumPy ni un solucionador espectral. Reimplementa las cotas y reconstruye cada caja desde la raíz. La cobertura y las desigualdades pasaron con Python estándar. Los números flotantes del constructor solo proponen parámetros; no aceptan hojas. La construcción tardó unos 129 segundos. El número de nodos describe el comprobador, no sustituye la prueba analítica que lo reduce a este dominio.

## 5. Controles y reproducción

```text
python -S verify_profile_upper_capacity.py
python -S profile_upper_capacity_checks.py
python verify_covariance_reduction.py
python verify_global_optimum.py
```

Las dos primeras órdenes usan Python estándar; las otras necesitan SymPy. El último teorema conserva el intervalo algebraico de referencia para $\mu_0$ y no se usa para probar la cota superior nueva. Sí permite comprobar exactamente que $0.000592<0.6935-\mu_0<0.000593$.

Los controles rechazan cinco corrupciones de dominio, cobertura y desigualdades. También conservan tres perfiles racionales de proporción de masas diferente, que pasan el verificador de equilibrio exacto y LDL del gauge completo en realizaciones finitas. Son controles físicos de la proyección, inferiores al valor conocido; no se presentan como récords. El conjunto finito de controles no prueba el cuantificador continuo.

La búsqueda `capacity_projection_20261019-capacity-v1.json` conserva 24 arranques con semilla 190071, límites y todas las terminaciones. Varias no convergieron o violaron restricciones; ninguna se aceptó como equilibrio finito. La búsqueda orientó el intento de cota, pero la demostración depende de la cobertura racional y de (1)–(3).

El corolario de grafos simples de la nota base conserva su alcance: equilibrios constantes en siete grupos con proporciones límite positivas y Hessiano completo positivo fuera de la rotación. Se tiene $\limsup\delta/n<0.6935$; las otras dos normalizaciones comparten la cota solo para orden tendiendo a infinito. No se obtiene una cota para todas las geometrías o todos los grafos.

**Uso de IA:** Codex (OpenAI) realizó consulta, deducción, código, cálculos, controles y texto. Constructor y verificador proceden del mismo agente y no constituyen revisión humana independiente. No hubo subagentes, publicación, comunicaciones ni entrega al evento. Los medios anteriores no incluyen esta ampliación.
