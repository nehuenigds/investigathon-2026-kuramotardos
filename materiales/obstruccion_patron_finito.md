# Un enlace opuesto mejora el patrón a geometría fija

18/10/2026. Deducción y comprobación asistidas por Codex. **Modelo:** Kuramoto homogéneo en plantillas ponderadas de siete clusters, con masas y fases fijadas. La contribución propuesta es una separación rigurosa entre dos clases de densidades a separación finita. No es una mejora de la cota general conocida y su novedad bibliográfica no está confirmada.

## Proposición comprobada

Existen masas y fases racionalmente especificadas para las que se cumplen simultáneamente:

1. Toda plantilla en equilibrio, con Hessiano de clusters semidefinido positivo, enlaces completos dentro de cada hoja y enlaces vacíos entre hojas opuestas, satisface
   $$\mu<0.68877337417.$$
   Las doce densidades adyacentes son completamente libres en $[0,1]$.
2. Con **las mismas masas y fases**, hay una plantilla no sincronizada estrictamente estable, que conserva los enlaces internos completos y solo agrega un enlace opuesto, con
   $$\mu>0.68877357363.$$
3. La conectividad del testigo supera la cota superior de la primera clase en más de $1.99\times10^{-7}$.

Los números escritos son extremos racionales, no tolerancias flotantes. Por tanto, a separación finita y a esta geometría fija, imponer todos los enlaces opuestos vacíos **pierde conectividad**, aun después de optimizar sin simetrías las densidades adyacentes. El enunciado no presupone que el primer patrón sea óptimo en el resto de geometrías.

## Geometría exacta

Se usa la geometría del ejemplo compacto anterior, una variante racional del patrón S7 de [O'Keeffe, Tabla 2 y Apéndice A](https://arxiv.org/html/2610.21271v1). Las masas son

$$x=(20,20,20,20,20,20,33)/153.$$

Las cuatro hojas son $\{0,1\}$, $\{2,3\}$, $\{4,5\}$ y $\{6\}$. Los puntos del círculo son

$$z=((C,-S),(C,S),(S_B,C_B),(-S_B,C_B),(-C,S),(-C,-S),(0,-1)),$$

con

$$C=\frac{159999}{160001},\quad S=\frac{800}{160001},\quad
C_B=\frac{3999951}{4000049},\quad S_B=\frac{28000}{4000049}.$$

Equivalen a parámetros $h=1/200$, $q=13/20$, $w=7/5$ del constructor de coordenadas racionales. Los ángulos son $\pm2\arctan(h/2)$ y $\pm2\arctan(wh/2)$, no exactamente $\pm h,\pm wh$ a separación finita.

El único enlace opuesto del testigo es $(1,4)$, Ap–Cm en la nomenclatura de la fuente, con densidad

$$P_{1,4}=P_{4,1}=\frac{15852476440088611}{10^{22}}\approx1.58525\times10^{-6}.$$

Los demás enlaces opuestos son exactamente cero y todos los internos son exactamente uno. Se reajustan también las densidades adyacentes. Las fracciones completas están en `one_opposite_link_data.json`. El equilibrio es exactamente nulo; las siete fuerzas internas son positivas y el Hessiano en un gauge tiene seis pivotes positivos. El mínimo pivote es aproximadamente $1.50\times10^{-13}$; no es un autovalor.

## Demostración de la cota superior mediante dualidad

Este es un uso de dualidad débil estándar, no un nuevo principio de optimización. La referencia general consultada es [Boyd y Vandenberghe, diapositivas de *Convex Optimization*, capítulo 5](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf). La prueba específica se da aquí para que no dependa del estado de terminación de un SDP.

Escribir $C_{ij}=z_i\cdot z_j$, $S_{ij}=s_ic_j-c_is_j$ y $b_i=x_i\sum_jx_jP_{ij}S_{ij}$. El equilibrio es $b=0$. El Hessiano ponderado es el Laplaciano

$$H=\sum_{i<j}x_ix_jP_{ij}C_{ij}(e_i-e_j)(e_i-e_j)^T.$$

El grado de plantilla es $d_i=\sum_jx_jP_{ij}$ y $\mu=\min_i d_i$. Separar las densidades fijas y las variables $p_e\in[0,1]$:

$$d=d_0+Bp,\qquad b=b_0+Ap,\qquad H=H_0+\sum_e p_eH_e.$$

Elegir racionales $\lambda_i\geq0$ con $\sum_i\lambda_i=1$, un vector racional libre $\eta$ y una matriz racional $W\succeq0$. Para cualquier equilibrio con $H\succeq0$,

$$\mu\leq\lambda^Td\leq\lambda^Td+\operatorname{tr}(WH)+\eta^Tb.$$

La última expresión es $\kappa+\sum_e a_ep_e$, donde

$$\kappa=\lambda^Td_0+\operatorname{tr}(WH_0)+\eta^Tb_0,$$

$$a_{ij}=\lambda_i x_j+\lambda_jx_i+
x_ix_jC_{ij}(W_{ii}+W_{jj}-2W_{ij})+
(\eta_i-\eta_j)x_ix_jS_{ij}.$$

Por la caja de densidades,

$$\boxed{\mu\leq U:=\kappa+\sum_e\max(0,a_e).}$$

No hace falta que los multiplicadores satisfagan exactamente estacionariedad, complementariedad o condiciones de Slater. Cualquier elección con $\lambda\geq0$, suma uno y $W\succeq0$ da una cota válida. Esto permite redondear la salida numérica y verificar el certificado con fracciones.

En los datos, $W=TQT^T$, con $T=[\Pi/h,Z]$: $\Pi$ son tres indicadores de hojas con la cuarta anclada y $Z$ son diferencias internas. Se comprueba por LDL racional que $Q\succ0$; entonces $W\succeq0$. Para esta desigualdad no es necesario identificar los autovalores de la congruencia con los de $H$.

`verify_fixed_geometry.py` reconstruye $W$ desde los datos y evalúa directamente las fórmulas de aristas; no importa el constructor, CVXPY ni las matrices flotantes del SDP. Para la clase con opuestos vacíos obtiene una fracción $U$ que satisface

$$U<0.68877337417.$$

El mismo archivo verifica un testigo estricto de esa clase con conectividad $L>0.68877337398$ y $U-L<2\times10^{-10}$. Por ello se encierra su supremo estricto en un intervalo muy pequeño, sin afirmar que el supremo sea alcanzado.

Para la clase con **todas** las densidades fuera de la diagonal libres, otro certificado da

$$\mu\leq U_{\rm todo}<0.688773576.$$

El testigo con un solo enlace opuesto es estricto y supera $0.68877357363$. En consecuencia la mejora respecto de la primera clase está separada por fracciones exactas. `verify_pattern_obstruction.py` verifica que se usan las mismas masas y coordenadas, el soporte opuesto especificado y la desigualdad estricta $L_{\rm opuesto}-U>1.99\times10^{-7}$. Esto prueba la proposición.

## Un entorno donde sigue habiendo exclusión

Los multiplicadores se pueden mantener fijos al variar masas y puntos. Esto permite extender la cota superior a una caja, sin resolver de nuevo el SDP.

Para masas nuevas positivas que sumen uno y puntos nuevos del círculo, supóngase $|x_i'-x_i|\leq\varepsilon_x$ y que cada una de las dos coordenadas de $z_i'-z_i$ está acotada por $\varepsilon_z$. Entonces

$$|C_{ij}'-C_{ij}|,|S_{ij}'-S_{ij}|\leq4\varepsilon_z,\qquad
|x_i'x_j'-x_ix_j|\leq2\varepsilon_x.$$

Así, con $E_{ij}=W_{ii}+W_{jj}-2W_{ij}$ y $M_{ij}=|E_{ij}|+|\eta_i-\eta_j|$, cada término de traza y equilibrio cambia a lo sumo

$$M_{ij}(2\varepsilon_x+4x_ix_j\varepsilon_z).$$

El grado cambia linealmente y $a\mapsto\max(0,a)$ es 1-Lipschitz. Al sumar se obtiene $U'\leq U+B_x\varepsilon_x+B_z\varepsilon_z$, con los dos coeficientes racionales escritos en el certificado. En el patrón restringido se suman pares internos y adyacentes; en el modelo de todas las densidades se suman todos los pares. Las diagonales tienen seno nulo, no entran en $H$ y se tratan en el término de grado.

Con $\varepsilon_x=\varepsilon_z=10^{-8}$, las cotas resultantes son menores que $0.6929$ en ambos modelos. Esta exclusión permite variaciones sin reflexión ni centrado de las fases, siempre dentro de la caja y con el patrón correspondiente. **No afirma** que el testigo mejorado sea óptimo en ese entorno ni que la ventaja persista uniformemente al mover la geometría: esas serían comparaciones distintas.

## Experimentos, controles y reproducibilidad

Se ejecutaron tres SDP: patrón restringido con márgenes de congruencia $10^{-6}$ y $10^{-10}$, y todas las densidades con margen $10^{-9}$. Los estados numéricos fueron `optimal_inaccurate`, `optimal` y `optimal_inaccurate`. No se aceptaron por esos estados: se corrigieron los equilibrios con flujos racionales y se verificaron tanto las plantillas como las cotas duales con fracciones. El testigo de un solo enlace opuesto se obtuvo completando los internos, anulando los otros opuestos y corrigiendo nuevamente el equilibrio exacto; no requirió un cuarto SDP.

Se preservan las salidas numéricas originales y las huellas en `fixed_geometry_005_data.json`, `fixed_geometry_005_tight_data.json` y `all_density_005_data.json`. El dato simplificado y el certificado de separación son `one_opposite_link_data.json` y `pattern_obstruction_certificate.json`.

La reproducción necesita solo Python estándar:

```text
python fixed_geometry_checks.py
python verify_pattern_obstruction.py
```

Los controles rechazan una matriz dual no positiva, pesos de grado negativos, una cota superior declarada menor que la reconstruida y una densidad que destruye el equilibrio del testigo. La aceptación exacta no importa los constructores numéricos. El verificador y el constructor fueron escritos por el mismo agente; esta separación técnica no equivale a revisión independiente.

## Atribución y estado del aporte

La constante $\mu_0$, S7 y la realización de plantillas proceden del preprint. Esta proposición trata una geometría finita y no contradice una optimalidad del modelo límite con el patrón fijado. No aumenta $\mu_0$ ni da una cota superior para todos los grafos simples. Su conectividad es la de plantilla; no se está comparando $(\delta+1)/n$ con $\delta/(n-1)$ de un grafo finito.

El diseño lineal de pesos con fases prescritas tiene antecedentes explícitos en [Menara, Baggio, Bassett y Pasqualetti (2022), ecuaciones 4, 5 y 11](https://www.nature.com/articles/s41467-022-31733-2). La aportación que se propone revisar es la separación concreta certificada y su aplicación al patrón a separación finita, junto con el verificador racional. No se ha encontrado una demostración idéntica en las fuentes revisadas, pero esa consulta no alcanza para confirmar novedad.

**Uso de IA:** Codex (OpenAI) realizó la derivación, búsquedas, construcción de los certificados, comprobaciones y texto. No hubo subagentes, revisión humana, publicación ni comunicaciones. Los materiales de exposición y el informe previo todavía no incluyen esta proposición.

**Actualización del 19/10/2026:** el informe de cinco páginas, la charla v10 y el póster de grafos sí incorporan esta separación y su traslado existencial. La frase anterior corresponde a la versión inicial de esta nota. La nueva [obstrucción asintótica](enlaces_opuestos_limite.md) explica un límite de reducir $h$; no está incluida en esos medios congelados y no altera los certificados finitos.
