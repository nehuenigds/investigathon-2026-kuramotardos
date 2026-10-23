# Perfil principal de S7: obstrucción sin hipótesis de suavidad

19/10/2026. Deducción asistida por Codex. **Modelo:** plantillas del Kuramoto homogéneo; el corolario final vuelve a grafos simples no dirigidos. Se atribuyen el perfil inicial y la construcción que se aproxima a $\mu_0$ a [O'Keeffe v1, Tabla 2 y Teorema 1](https://arxiv.org/html/2610.21271v1). El teorema algebraico de apoyo es [optimalidad_global.md](optimalidad_global.md). Novedad y revisión independiente no acreditadas.

Esta nota amplía la [obstrucción anterior](enlaces_opuestos_limite.md): **no exige masas fijas, expansión de densidades, términos de fase de segundo orden ni derivabilidad**. El perfil límite de masas y fases sigue estando especificado; no es una cota general para todos los grafos.

## Teorema

Sean $h_\ell>0$, $h_\ell\to0$, y plantillas $(x^{(\ell)},\theta^{(\ell)},P^{(\ell)})$ en equilibrio exacto, con densidades simétricas en $[0,1]$ y Hessiano de clusters semidefinido positivo. Fijar $r>0$, $0<q<1$, $w>0$, y definir

$$M=(r,r,1,1,r,r,1+q),\quad N=4r+3+q,\quad
j=(0,0,1,1,2,2,3),\quad s=(-1,1,-w,w,-1,1,0).$$

Suponer, tras escoger un representante de rotación, que

$$x_i^{(\ell)}\longrightarrow M_i/N,\qquad
\theta_i^{(\ell)}=j_i\pi/2+h_\ell u_i^{(\ell)},\qquad u_i^{(\ell)}\longrightarrow s_i.$$

Las hojas son A $=\{0,1\}$, B $=\{2,3\}$, C $=\{4,5\}$, W $=\{6\}$. Las densidades dentro de cada hoja, incluidas las diagonales, tienden a uno. Las doce densidades adyacentes tienden al patrón $p(q)$: valor $q$ en $(0,3),(1,2),(2,5),(3,4)$ y uno en las otras ocho parejas. No se impone tasa de convergencia, reflexión en los datos finitos ni una hipótesis inicial de tamaño sobre las seis densidades opuestas.

Entonces, con $K=1+2q-q^2$,

$$D=r^2[-2(1+q)^2w^2+4(1-q^2)w+2K]+Kw^2,$$
$$R=4r^2+Kw^2+4(1-q^2)w-4(1+q)^2,$$

se cumplen:

1. Todos los opuestos son $O(h_\ell^2)$ y
   $$\limsup_\ell\sum_{A-C}\frac{P_{ij}^{(\ell)}}{h_\ell^2}\leq\frac{D}{2r^2},\qquad
   \limsup_\ell\sum_{B-W}\frac{P_{ij}^{(\ell)}}{h_\ell^2}\leq\frac{R}{2(1+q)}.$$
2. $D,R\geq0$ y el límite de conectividades de plantilla satisface
   $$\mu_\infty=\min\left\{\frac{2r+2+2q}{N},\frac{2+2r(1+q)}{N},\frac{4r+1+q}{N}\right\}\leq\mu_0.$$
3. Si $\mu_\infty=\mu_0$, necesariamente $r=1,q=a,w=w_*$ y cada opuesto es $o(h_\ell^2)$. Aquí $a,w_*$ y $\mu_0=(4+2a)/(7+a)$ son los del teorema algebraico citado.

No se concluye estabilidad estricta de una forma límite semidefinida. La cota es necesaria para cualquier sucesión de equilibrios estables con este perfil.

## 1. Una identidad exacta reemplaza las derivadas

Omitir el índice $\ell$. Poner $m_i=Nx_i$, $a_{ij}=m_im_jP_{ij}\geq0$ y $d_{ij}=u_i-u_j$. Para las parejas adyacentes escribir $\sigma_{ij}=\sin((j_i-j_j)\pi/2)\in\{-1,1\}$. Denotar por I las tres parejas entre mitades de una misma hoja, por E las doce adyacentes y por O las seis opuestas.

Multiplicar los residuos ponderados por $u_i$ y sumar. El equilibrio exacto da

$$0=\sum_I a_{ij}d_{ij}\sin(hd_{ij})
  +\sum_E a_{ij}\sigma_{ij}d_{ij}\cos(hd_{ij})
  -\sum_O a_{ij}d_{ij}\sin(hd_{ij}).$$

La suma de los pesos de Hessiano adyacentes es

$$S_h=\sum_Ea_{ij}\cos(\theta_i-\theta_j)
    =-\sum_Ea_{ij}\sigma_{ij}\sin(hd_{ij}).$$

Sumar $h$ veces la identidad de equilibrio produce **exactamente**

$$S_h=h\sum_Ia_{ij}d_{ij}\sin(hd_{ij})
      -h\sum_Oa_{ij}d_{ij}\sin(hd_{ij})
      +\sum_Ea_{ij}\sigma_{ij}\,[hd_{ij}\cos(hd_{ij})-\sin(hd_{ij})].$$

Como las masas y $u$ convergen, existen constantes $A,L$ con $a_{ij}\leq A$ y $|u_i|\leq L$. Las desigualdades elementales

$$|\sin t-t|\leq|t|^3/6,\qquad|t\cos t-\sin t|\leq|t|^3/3$$

dan

$$S_h=h^2\left(\sum_Ia_{ij}d_{ij}^2-\sum_Oa_{ij}d_{ij}^2\right)+\mathcal R_h,$$
$$|\mathcal R_h|\leq32AL^3h^3+24AL^4h^4.$$

La segunda desigualdad elemental se obtiene integrando $(t\cos t-\sin t)'=-t\sin t$. Los coeficientes cuentan doce parejas adyacentes y nueve internas u opuestas. En particular, $S_h=O(h^2)$ sin derivar masas, fases ni densidades.

## 2. La semidefinitud fuerza pequeños los opuestos

Sea $\Pi$ la matriz de indicadores de A,B,C, con W anclada, y usar $v_A=(1,0,-1)^T$, $v_B=(1,2,1)^T$. Las diferencias de $\Pi v_A$ y $\Pi v_B$ tienen cuadrado uno en todas las adyacencias. Sus cuadrados son cuatro, respectivamente, en A–C y B–W, y cero en el otro tipo opuesto. Así,

$$0\leq(\Pi v_A)^T\bar H(\Pi v_A)=S_h-4\sum_{A-C}a_{ij}\cos(hd_{ij}),$$
$$0\leq(\Pi v_B)^T\bar H(\Pi v_B)=S_h-4\sum_{B-W}a_{ij}\cos(hd_{ij}),$$

donde $\bar H=N^2H$. Para $h$ pequeño, $\cos(hd_{ij})\geq1/2$. Las masas están acotadas inferiormente por una constante positiva. Por tanto, las seis densidades opuestas son $O(h^2)$. No se supuso esa escala ni que ya tendieran a cero.

Volviendo a la identidad anterior, la suma opuesta allí es ahora $O(h^2)$ y

$$S_h/h^2\longrightarrow E:=\sum_I M_iM_j(s_i-s_j)^2=8r^2+4w^2.$$

## 3. Dos variaciones internas dan $D$ y $R$

Sea $Z$ la matriz que vale $(-1/2,1/2)$ en cada hoja dividida. Los enlaces internos anulan $\Pi$ exactamente, cualquiera que sea su densidad. Por los límites de datos y la escala opuesta ya probada,

$$Z^T\bar H Z\longrightarrow J=\operatorname{diag}(r^2,1,r^2),\qquad
h^{-1}\Pi^T\bar H Z\longrightarrow C.$$

$C$ se obtiene solo de $M,p,s$: cada adyacencia aporta $-M_iM_jp_{ij}\sigma_{ij}(s_i-s_j)(\Pi_i-\Pi_j)^T(Z_i-Z_j)$. No se necesita que el bloque superior completo dividido por $h^2$ converja.

Tomar las dos correcciones explícitas

$$\zeta_A=\left(\frac{w(1-q)}r,-2r[(q+1)w+q-1],\frac{w(1-q)}r\right)^T,$$
$$\zeta_B=\left(\frac{(q-1)w+2(q+1)}r,0,-\frac{(q-1)w+2(q+1)}r\right)^T.$$

Se verifican $C^Tv_A=-J\zeta_A$, $C^Tv_B=-J\zeta_B$ y

$$E-\zeta_A^TJ\zeta_A=2D,\qquad E-\zeta_B^TJ\zeta_B=2R.$$

Aplicar la semidefinitud a $\Pi v_A+hZ\zeta_A$ y $\Pi v_B+hZ\zeta_B$ y dividir por $h^2$. Como $P_{ij}/h^2$ está acotado, los errores de masas y cosenos son $o(1)$, aun sin tasa prescrita. Se obtiene

$$0\leq2D-4r^2\sum_{A-C}P_{ij}/h^2+o(1),$$
$$0\leq2R-4(1+q)\sum_{B-W}P_{ij}/h^2+o(1).$$

Esto prueba las cotas de límite superior y $D,R\geq0$. `verify_leading_pattern.py` comprueba las identidades por pares, los bloques $J,C$ y los dos valores polinómicos con SymPy exacto.

## 4. Conectividad, igualdad y alcance de la cota

Todos los datos de densidad tienen ya los límites especificados, incluidos los opuestos cero. Los grados y su mínimo convergen a las tres fracciones del enunciado. El teorema algebraico para $D,R\geq0$ da la cota $\mu_0$ y sus únicos parámetros de igualdad. En ese punto $D=R=0$; no negatividad y las dos cotas fuerzan $P_{ij}/h^2\to0$ en cada opuesto.

La cota es ajustada como límite: la construcción estricta conocida de O'Keeffe permite elegir primero $q\uparrow a$ y después $h$ suficientemente pequeño. Elegir una sucesión diagonal da exactamente este perfil y conectividad tendiendo a $\mu_0$. Se atribuye esa existencia al resultado publicado; no se afirma que un dato finito alcance el valor límite ni que se haya construido un récord nuevo.

## Corolario para sucesiones de grafos simples

Sean grafos simples de orden $n_\ell\to\infty$, con un equilibrio constante en cada uno de siete grupos y Hessiano completo semidefinido. Suponer las mismas hipótesis sobre proporciones, fases y densidades entre grupos. Dentro de un grupo de $n_i$ vértices usar la convención

$$P_{ii}=2e(V_i)/n_i^2,$$

y fuera de él $P_{ij}=e(V_i,V_j)/(n_in_j)$. Exigir que los bloques dentro de cada hoja sean asintóticamente completos, sin pedir completitud exacta ni regularidad entre bloques.

La agregación por promedios conserva equilibrio y semidefinitud. Con esta **convención diagonal particular**, $d_i=\bar\delta_i/n$, por lo que $\delta/n\leq\mu(T)$. El teorema implica

$$\limsup_\ell\frac{\delta(G_\ell)}{n_\ell}\leq\mu_0.$$

Como $n_\ell\to\infty$, la misma cota vale para $(\delta+1)/n$ y $\delta/(n-1)$, cuyas diferencias tienden a cero. No se igualan estas normalizaciones a orden finito. No se necesita una partición equitativa ni grados de bloque constantes. El corolario sigue dependiendo del perfil de siete fases y densidades; no acota todos los grafos simples.

## Controles y límites de la comprobación

`moving_geometry_limit.py` registró primero la cancelación de siete pendientes de masa y siete términos de fase de segundo orden. Eso motivó la identidad exacta; ese cálculo exploratorio no prueba el teorema sin suavidad.

`leading_pattern_checks.py` conserva tres controles racionales con $h=\varepsilon^2$, masas modificadas en $\varepsilon=\sqrt h$, anchura $w+\sqrt h$ y densidades que se acercan al patrón a velocidad $\sqrt h$. También se adelgazan enlaces internos. Son casos fuera de las hipótesis anteriores. Reescalar los productos $x_ix_jP_{ij}$ por un factor común conserva equilibrio y Hessiano hasta escala positiva. Las tres plantillas pasan el verificador estricto exacto y los valores de las dos pruebas se acercan a los límites calculados. Cambiar las masas sin corregir los productos rompe el equilibrio y se rechaza.

```text
python -S leading_pattern_checks.py
python verify_leading_pattern.py
python verify_global_optimum.py
```

La primera orden usa Python estándar; las otras requieren SymPy. Los controles finitos no prueban el cuantificador sobre sucesiones: lo hacen la identidad, las cotas y los límites escritos. El primer control simbólico comparaba formas factorizadas y expandidas por igualdad estructural; se corrigió a comprobar que su diferencia polinómica es cero. El certificado final pasó.

Se conservan las restricciones de **perfil límite**: masas principales con mitades iguales y reflexión A/C, anchuras A y C iguales a primer orden, y los doce límites adyacentes especificados. No se cubren otras distribuciones principales, anchuras distintas, más clusters ni todos los patrones. El informe, las diapositivas, el póster y los paquetes congelados anteriores no incluyen esta ampliación. Novedad y revisión humana siguen pendientes.

**Uso de IA:** Codex (OpenAI) realizó relectura, deducción, código, controles y redacción. No hubo subagentes, revisión independiente de otra persona, ensayos, publicación ni comunicaciones.
