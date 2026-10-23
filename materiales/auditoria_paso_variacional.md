# Del Hessiano finito a las dos pruebas variacionales

22/10/2026. Auditoría de un paso de la [reducción base](cota_perfil_general.md), preparada por Codex para revisar la cota 0,6934. Explicita estimaciones que antes se escribían con O(h²); no propone otra cota ni acredita revisión humana o novedad. El modelo es la plantilla homogénea ponderada, con energía y normalización de las notas anteriores.

## Datos y convenciones

Sean $x_i>0$, suma uno, $P$ simétrica con entradas en $[0,1]$ y $a_{ij}=x_i x_j P_{ij}$ para $i<j$. Escribir

$$\theta_i=j_i\pi/2+h u_i,\qquad j=(0,0,1,1,2,2,3),\quad u_6=0,\quad |u_i|\leq1,\quad0<h\leq1/4.$$

Se supone **equilibrio exacto** y Hessiano H semidefinido. Esto último equivale a semidefinitud en el complemento de la rotación, pues H1=0. El caso h=0 no se divide por h: su exclusión se justifica aparte por estricta positividad, o por el [lema de mínimos locales](cota_minimos_locales_06934.md).

En los pasos de límite se considera una sucesión con $h\to0$, masas que convergen a valores positivos y, tras extraer subsucesión, conductancias y offsets reescalados convergentes. Las estimaciones finitas siguientes son uniformes sobre los datos indicados; no presuponen tasas de convergencia.

Las tres aristas internas son 01, 23 y 45. Los seis pares opuestos son A–C y B–W. Las doce adyacencias se orientan A→B→C→W→A; en esa orientación la fase base de cola menos cabeza tiene seno −1 y coseno cero. Poner d_ij=u_i−u_j, con la misma orientación en cada sumando. La simetría permite elegir esa orientación al agregar pares no dirigidos. Se tiene |d_ij|≤2 y Σ_(i<j) a_ij≤1/2.

Definir

$$S_h=\sum_{\rm adj}a_{ij}\sin(hd_{ij}),\quad
R_{AC}=\sum_{A-C}a_{ij}\cos(hd_{ij}),\quad
R_{BW}=\sum_{B-W}a_{ij}\cos(hd_{ij}).$$

R_AC y R_BW son no negativos: |hd|≤1/2 y cos(hd)≥7/8. S_h puede tener sumandos de ambos signos.

## 1. Identidad exacta y opuestos pequeños

Escribir F_i=Σ_j a_ij sin(θ_i−θ_j), es decir, el residuo ponderado. Al sumar u_i F_i por vértices, cada par aparece una vez. Para **cualquier** dato, sin suponer todavía F=0, resulta

$$S_h=h\sum_{\rm int}a_{ij}d_{ij}\sin(hd_{ij})
-h\sum_{\rm op}a_{ij}d_{ij}\sin(hd_{ij})
+\sum_{\rm adj}a_{ij}[\sin(hd_{ij})-hd_{ij}\cos(hd_{ij})]
-h\sum_i u_iF_i.\tag{1}$$

El último término desaparece por equilibrio exacto. Esta es una dependencia real: comprobar solo un residuo flotante pequeño no autoriza suprimirlo al dividir por h².

Para |t|≤1/2 se usan |sin t|≤|t|, |sin t−t|≤|t|³/6, |sin t−t cos t|≤|t|³/3 y 0≤1−cos t≤t²/2. Las dos cotas cúbicas se obtienen integrando cos t−1 y t sin t, respectivamente. Además t sin t≥0. Por (1),

$$S_h\leq2h^2+\frac43h^3\leq\frac73h^2.\tag{2}$$

Sean q_1=(1,0,−1,0) y q_2=(1,2,1,0), repetidos por hojas. Sus diferencias al cuadrado valen uno en cada adyacencia y cuatro solo en A–C y B–W, respectivamente. Por semidefinitud,

$$0\leq q_1^THq_1=S_h-4R_{AC},\qquad
0\leq q_2^THq_2=S_h-4R_{BW}.\tag{3}$$

En particular S_h≥0, R_AC+R_BW≤S_h/2 y

$$A_{\rm op}:=\sum_{\rm op}a_{ij}\leq\frac87(R_{AC}+R_{BW})\leq\frac43h^2.\tag{4}$$

Esto acota conductancias. Para concluir P_ij=O(h²) a lo largo de una sucesión se usan además las masas límite estrictamente positivas. No se obtiene esa conclusión si se permite que x_i x_j desaparezca.

## 2. Cada corte se cancela por separado

Sea B la matriz 7×4 de indicadores de hojas. La matriz R=B^T H B es semidefinida y

$$0\leq\operatorname{tr}R=2S_h-2R_{AC}-2R_{BW}\leq\frac{14}{3}h^2.\tag{5}$$

Para una matriz semidefinida, cada entrada tiene valor absoluto a lo sumo la norma de operador, que no supera la traza. Si K_ν=Σ_(adj del corte ν) a_ij sin(hd_ij), la entrada correspondiente de R es −K_ν. Por tanto, **cada** |K_ν|≤14h²/3. No se deduce la cancelación de los cuatro cortes únicamente de su suma.

Poniendo c_ν^h=Σ_(corte ν) a_ij d_ij y usando la cota del resto de seno,

$$|c_\nu^h|\leq\frac{14}{3}h+\frac23h^2.\tag{6}$$

Así, si a^h y u^h convergen, cada corte principal tiene límite cero. No hace falta que los datos tengan derivadas respecto de h.

También, con E_h=Σ_int a_ij d_ij², (1) y (4) dan una estimación explícita:

$$\left|\frac{S_h}{h^2}-E_h\right|\leq\frac43h+\frac{20}{3}h^2.\tag{7}$$

Los tres errores son, respectivamente, el resto adyacente ≤4h/3, el error interno ≤4h²/3 y el término opuesto ≤4 A_op≤16h²/3. Por ello S_h/h²→E_o, donde E_o usa los internos originales, que pueden ser incompletos.

## 3. El bloque cruzado y los internos originales

Usar U con filas constantes por hoja

$$U_A=(1,1,1),\ U_B=(0,2,0),\ U_C=(-1,1,1),\ U_W=(0,0,0),$$

y Z con la columna de cada pareja igual a (−1/2,1/2), cero en el resto. La diferencia entre sus dos entradas es uno; de ahí la normalización del bloque interno, sin un factor dos extra.

Definir

$$C_h=h^{-1}U^THZ,\quad J_h=Z^THZ,\quad
\widetilde C_h=\sum_{\rm adj}a_{ij}d_{ij}(U_i-U_j)^T(Z_i-Z_j),$$

$$J_o^h=\operatorname{diag}(a_{01},a_{23},a_{45}).$$

Para cada entrada se tiene

$$|(C_h-\widetilde C_h)_{\alpha\beta}|\leq\frac43h+\frac13h^2,\qquad
|(J_h-J_o^h)_{\alpha\beta}|\leq\frac14h+\frac56h^2.\tag{8}$$

En la primera cota, los internos no contribuyen porque U es constante por hoja. En adyacencias, |ΔU|=1 y |ΔZ|≤1/2; el resto sin(hd)/h−d aporta a lo sumo h²/3. En opuestos, |ΔU ΔZ|≤1 y (4) aporta 4h/3.

En la segunda cota, las adyacencias aportan a lo sumo (2h)(1/4)(1/2)=h/4; los opuestos, A_op/4≤h²/3. En una entrada diagonal, el error de su única arista interna es a_ij(1−cos hd)≤h²/2, porque a_ij≤x_i x_j≤1/4. No hay internos en las entradas fuera de la diagonal. Esto justifica la cota uniforme escrita.

Extraer una subsucesión convergente de a^h y u^h es suficiente. Entonces C_h→C, J_h→J_o y E_h→E_o. No se exige que J_o sea invertible ni que las tres separaciones internas tengan límites no nulos.

## 4. La variación que da las desigualdades necesarias

Para α=1,2, sea U_α la columna correspondiente y ζ cualquier vector fijo de tres componentes. En cada dato finito, semidefinitud da

$$0\leq h^{-2}(U_\alpha+hZ\zeta)^TH(U_\alpha+hZ\zeta).$$

Por (3), omitir el término opuesto negativo acota esta expresión **por arriba** con

$$\frac{S_h}{h^2}+2(C_h\zeta)_\alpha+\zeta^TJ_h\zeta.$$

Por (7)–(8), su límite existe y es no negativo:

$$0\leq E_o+2(C\zeta)_\alpha+\zeta^TJ_o\zeta.\tag{9}$$

No se necesita que la razón de cada conductancia opuesta a h² converja: esos términos fueron omitidos con el signo correcto antes de pasar al límite.

Sean las masas límite $\bar x_i>0$ y

$$J=\operatorname{diag}(\bar x_0\bar x_1,\bar x_2\bar x_3,\bar x_4\bar x_5)\succ0,\quad
k_i=s_{2i+1}-s_{2i},\quad E=\sum_iJ_i k_i^2.$$

Escribir J_o=diag(β_i J_i), con 0≤β_i≤1. La diferencia entre el miembro derecho completado y el original de (9) es exactamente

$$\sum_i(1-\beta_i)J_i(k_i^2+\zeta_i^2)\geq0.$$

Elegir ahora **$\zeta=-J^{-1}C^T e_\alpha$**, usando $J$, no $J_o$. Se concluye

$$\boxed{E-(CJ^{-1}C^T)_{\alpha\alpha}\geq0,\qquad\alpha=1,2.}\tag{10}$$

La completación es una relajación de una condición necesaria. No se afirma que cambiar los internos conserve el equilibrio finito. Tras excluir flujos nulos por grado y normalizar el flujo, (10) da las dos formas $L_1,L_2$ de la cota; esos pasos siguientes conservan su demostración propia. Al pasar a masas brutas $m_i=\bar x_i/\sqrt T$ y conductancias $a/T$, se multiplican $E,J,C$ y ambos miembros de (10) por el mismo factor positivo $1/T$.

## Qué se comprobó y qué queda fuera

`verify_variational_bridge.py` comprueba signos y factores por cada par de clusters, la identidad con residuo (1), las formas (3), el bloque interno y la identidad de completación. Reutiliza ocho controles estrictos con coordenadas racionales —tres testigos conservados, el testigo con un enlace opuesto y los cuatro con todas sus densidades multiplicadas por 1/2—, verificando exactamente equilibrio antes de LDL. Comprueba además tres controles degenerados con internos nulos o separaciones nulas; su semidefinitud se justifica por bloques y no se anuncia estricta positividad. Una alteración de una adyacencia se rechaza por residuo de equilibrio antes de clasificar estabilidad.

Las cotas (2), (4)–(8) y las expresiones finitas de (9) se evalúan en esos controles con 120 dígitos. Esa evaluación es un control numérico de los factores; **la prueba de las cotas es la cadena de desigualdades escrita aquí**, no el muestreo. El JSON separa ambas clases de evidencia y liga las fuentes por huella. El comprobador no realiza búsquedas ni modifica los testigos originales, no reejecuta el árbol 0,6934 y no verifica automáticamente toda la reducción asintótica.

No se demuestra aquí que h>0, que los flujos sean positivos, que z≠0, que las condiciones sobre masas se propaguen correctamente o que la cobertura racional sea válida. Esos argumentos siguen en sus notas y verificadores. En particular, h>0 por sí solo no obliga a z≠0: las hojas desconectadas pueden rotar sin separarse internamente. La exclusión por grado y los centros por flujo siguen siendo esenciales.

Para reproducir el control desde el cuaderno:

```text
python -B verify_variational_bridge.py
```

Requiere SymPy y mpmath. En esta instalación se usan las bibliotecas de la caché externa localizada por `bootstrap.py`, sin crear un entorno dentro del baúl. El resultado conservado es `variational_bridge_verification.json`.

**Uso de IA:** deducción explícita, código y redacción por Codex (OpenAI), sin subagentes ni revisión humana independiente. Es una auditoría del resultado previo; los medios y paquetes congelados conservan sus bytes.
