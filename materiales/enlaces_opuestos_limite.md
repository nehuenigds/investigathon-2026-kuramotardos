# Enlaces opuestos: mejora finita y obstrucción en el límite

19/10/2026. Deducción y controles asistidos por Codex. **Modelo:** plantillas ponderadas del Kuramoto homogéneo. El patrón y las fases de partida se atribuyen a [O'Keeffe v1, Tabla 2 y Apéndice A](https://arxiv.org/html/2610.21271v1). Allí ya se advierte que enlaces opuestos de orden $h^2$ afectan la forma límite. Aquí se deducen dos cotas necesarias concretas y una consecuencia de rigidez, usando la optimalidad restringida del cuaderno. No se confirma novedad bibliográfica ni revisión independiente.

La separación finita previamente certificada sigue siendo válida. El resultado de esta nota explica un límite preciso de intentar mejorarla reduciendo la separación: **con las hipótesis siguientes, permitir opuestos no eleva la mejor conectividad límite sobre $\mu_0$**. No es una cota superior sobre todas las geometrías de Kuramoto.

## Familia y enunciado

Fijar $r>0$, $0<q<1$, $w>0$, independientes de $h$. Escribir $M=(r,r,1,1,r,r,1+q)$, $N=4r+3+q$ y $x_i=M_i/N$. Las hojas son A $=\{0,1\}$, B $=\{2,3\}$, C $=\{4,5\}$, W $=\{6\}$. Las fases satisfacen

$$\theta_i(h)=j_i\pi/2+h s_i+O(h^3),\qquad
j=(0,0,1,1,2,2,3),\quad s=(-1,1,-w,w,-1,1,0).$$

Esto incluye tanto los ángulos lineales como las coordenadas racionales del círculo usadas en el cuaderno. Las masas permanecen exactamente fijas. Los enlaces dentro de cada hoja son completos. En las doce parejas adyacentes se supone

$$P_{ij}(h)=p_{ij}+hY_{ij}+O(h^2),$$

donde $p$ es la matriz inicial de S7: cuatro enlaces cruzados $(0,3),(1,2),(2,5),(3,4)$ tienen densidad $q$ y las otras ocho adyacencias densidad uno. Los doce números $Y_{ij}$ son libres, sujetos a las condiciones que imponga el equilibrio; **no se les exige reflexión**. En las seis parejas opuestas se admite cualquier densidad en $[0,1]$, sin imponer previamente su tasa de decaimiento.

Supóngase que para todo $h>0$ suficientemente pequeño hay equilibrio exacto y Hessiano de clusters semidefinido positivo. Basta esta condición necesaria de estabilidad; no se deduce estabilidad estricta de una semidefinitud. Entonces:

1. Todas las densidades opuestas son $O(h^2)$.
2. Con $K=1+2q-q^2$ y los polinomios del teorema anterior
   $$D=r^2[-2(1+q)^2w^2+4(1-q^2)w+2K]+Kw^2,$$
   $$R=4r^2+Kw^2+4(1-q^2)w-4(1+q)^2,$$
   se cumplen las cotas
   $$\limsup_{h\downarrow0}\sum_{i\in A,j\in C}\frac{P_{ij}(h)}{h^2}\leq\frac{D}{2r^2},\qquad
   \limsup_{h\downarrow0}\sum_{i\in B,j\in W}\frac{P_{ij}(h)}{h^2}\leq\frac{R}{2(1+q)}.$$
   En particular, $D,R\geq0$.
3. La conectividad de plantilla tiene límite
   $$\mu_\infty=\min\left\{\frac{2r+2+2q}{N},\frac{2+2r(1+q)}{N},\frac{4r+1+q}{N}\right\}\leq\mu_0.$$
4. Si $\mu_\infty=\mu_0$, entonces $r=1$, $q=a$, $w=w_*$, con $a,w_*$ definidos en [optimalidad_global.md](optimalidad_global.md), y **cada densidad opuesta es $o(h^2)$**. Es una condición necesaria; no se afirma existencia ni estabilidad de una familia en ese caso límite.

## Prueba

### 1. La estabilidad impone la escala de los opuestos

Multiplicar el Hessiano por $N^2$ no cambia su signo. Para el indicador de la hoja A, su forma cuadrática suma las contribuciones de los enlaces que cruzan el corte A/resto. En los adyacentes,

$$\cos((j_i-j_j)\pi/2+h(s_i-s_j)+O(h^3))
=-h\sin((j_i-j_j)\pi/2)(s_i-s_j)+O(h^3).$$

La suma del término de orden $h$, con las masas y densidades $p$, es cero. Los términos con $hY$ son $O(h^2)$ y el resto no aumenta ese orden. Esta cancelación se comprueba también mediante $\Pi^TL_1\Pi=0$, debajo.

En los enlaces A–C, el coseno tiende a $-1$ y es menor que $-1/2$ para $h$ pequeño. Como las densidades son no negativas, la semidefinitud obliga a

$$\frac12\sum_{i\in A,j\in C}M_iM_jP_{ij}(h)\leq C_Ah^2.$$

Todas las masas son constantes positivas: cada una de esas cuatro densidades es $O(h^2)$. El indicador de B da la misma conclusión para las dos parejas B–W. No se usaron residuos flotantes ni se supuso de antemano esa escala.

### 2. Forma límite y dos pruebas necesarias

Tomar cualquier sucesión $h\downarrow0$. Por la cota anterior, una subsucesión hace converger simultáneamente las seis razones $P_{ij}/h^2$ a números $\rho_{ij}\geq0$. Denotar

$$\alpha=\sum_{A-C}\rho_{ij},\qquad\beta=\sum_{B-W}\rho_{ij}.$$

Sea $L(h)=L_0+hL_1+h^2L_2+O(h^3)$ el Hessiano sin normalizar que contiene los enlaces internos y adyacentes $p+hY$, con fases lineales. Los errores admitidos en adyacencias y fases solo aportan $o(1)$ a la forma reescalada siguiente. Usar las matrices $\Pi,Z\in\mathbb R^{7\times3}$: $\Pi$ contiene los indicadores de A,B,C y vale cero en W; en cada hoja dividida, la columna de $Z$ vale $(-1/2,1/2)$.

Se verifica

$$L_0\Pi=0,\quad\Pi^TL_1\Pi=0,\quad
J:=Z^TL_0Z=\operatorname{diag}(r^2,1,r^2)\succ0.$$

El equilibrio a primer orden no recibe contribución de los opuestos: su densidad es $O(h^2)$ y su seno $O(h)$. Da seis ecuaciones independientes en las doce entradas de $Y$. Escribir $C_1=\Pi^TL_1Z$. En la base $[\Pi,hZ]$, dividir la forma por $h^2$ y pasar a la subsucesión da una matriz semidefinida. Su complemento de Schur sobre $J$ es

$$Q_Y-M_\rho\succeq0,\qquad
Q_Y=\Pi^TL_2\Pi-C_1J^{-1}C_1^T,$$
$$M_\rho=r^2\alpha(e_A-e_C)(e_A-e_C)^T+(1+q)\beta e_Be_B^T\succeq0.$$

La corrección opuesta aparece con signo negativo porque su coseno tiende a $-1$. No modifica los bloques interno o cruzado en este límite. La matriz $Q_Y$ puede no tener reflexión. Sin embargo, para **cualquier** solución de las seis ecuaciones de equilibrio,

$$v_A=(1,0,-1)^T,\quad v_B=(1,2,1)^T,\qquad
v_A^TQ_Yv_A=2D,\quad v_B^TQ_Yv_B=2R.$$

Por tanto,

$$0\leq v_A^T(Q_Y-M_\rho)v_A=2D-4r^2\alpha,$$
$$0\leq v_B^T(Q_Y-M_\rho)v_B=2R-4(1+q)\beta.$$

Las identidades se expanden y comprueban simbólicamente en `verify_opposite_asymptotics.py`. Ese programa asigna doce símbolos independientes a $Y$, resuelve seis entradas sobre un camino y conserva seis libres. No importa la reducción anterior ni impone órbitas de reflexión.

Como toda subsucesión convergente cumple las cotas, se obtienen los dos límites superiores del enunciado. Esto prueba también $D,R\geq0$.

### 3. Conectividad y rigidez

Los grados convergen a los de $p$ porque los cambios adyacentes son $O(h)$ y los opuestos $O(h^2)$. Su mínimo converge a $\mu_\infty$. El [teorema global ya demostrado para $D,R\geq0$](optimalidad_global.md) da $\mu_\infty\leq\mu_0$, con igualdad solo en $r=1,q=a,w=w_*$. Allí $D=R=0$. Las dos cotas de límite superior y la no negatividad de cada densidad fuerzan $P_{ij}/h^2\to0$ en las seis parejas opuestas. Esto concluye la prueba.

## Controles finitos exactos

`opposite_asymptotics_checks.py` usa Python estándar y guarda cuatro plantillas en `opposite_asymptotics_checks.json`. Comprueba puntos del círculo, densidades, equilibrio exacto y fuerzas internas antes de estudiar el Hessiano.

El ejemplo compacto sin opuestos, con $r=1,q=13/20,w=7/5,\kappa=2,u=10/3$, es estricto a $h=1/200$. Pero **$D=-33/10000<0$**. Reducir el mismo constructor a $h=10^{-6}$ produce un equilibrio exacto con una dirección cuadrática negativa. La forma reescalada vale aproximadamente $-0.00653913$; su signo se comprueba con fracciones, y su límite es $2D=-0.0066$. El verificador estricto lo rechaza. Este caso muestra por qué reducir $h$ de un ejemplo finito no preserva automáticamente la estabilidad.

Otros dos controles usan $q=3/5,w=7/5$, una circulación que rompe reflexión y dos densidades opuestas $h^2/100$. Corrigen equilibrio por flujos exactos y son estrictos para los dos valores guardados de $h$. Sus formas reescaladas se acercan a $2(D-2\alpha)$ y $2(R-2(1+q)\beta)$. Cambiar el signo de la contribución opuesta falla esos controles. Los cuatro puntos no prueban el enunciado sobre un continuo: la prueba usa las expansiones, semidefinitud y paso a subsucesiones descritos arriba.

```text
python -S opposite_asymptotics_checks.py
python verify_opposite_asymptotics.py
```

La segunda orden necesita SymPy 1.14.0 mediante las dependencias del cuaderno. El certificado simbólico queda en `opposite_asymptotics_certificate.json`; la prueba global de apoyo se comprueba por separado con `verify_global_optimum.py`. Aserciones activas, sin `-O`.

## Alcance para decidir el aporte

La mejora finita certificada y este resultado asintótico responden a preguntas distintas. La primera compara dos clases a una geometría fija; el segundo limita familias que conservan masas, patrón principal y expansión de fases precisos. No se probó que el testigo finito con un opuesto pertenezca a una familia estable hasta $h=0$.

No se cubren masas variables con $h$, otros patrones principales, cambios de fase de orden $h^2$ arbitrarios, otros números de clusters ni todos los grafos. En grafos simples debe aplicarse además la agregación del cuaderno y controlar la normalización y el orden; no se añade aquí una nueva realización. El informe, charla, póster y ZIP v1 permanecen congelados y no incluyen esta nota. La deducción no sustituye revisión del equipo ni contraste de novedad.

**Uso de IA:** Codex (OpenAI) realizó relectura, deducción, código, controles y redacción. No hubo subagentes, revisión humana independiente, ensayos, publicaciones ni comunicaciones.

**Ampliación posterior del 19/10:** `patron_principal_limite.md` elimina las hipótesis de masas fijas y suavidad usando una identidad exacta de equilibrio. La nota presente y su kit v1 conservan su alcance anterior. La ampliación mantiene hipótesis precisas de perfil límite y tampoco da una cota general para todos los grafos.
