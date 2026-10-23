# Optimalidad global del modelo reducido con masas desiguales

18/10/2026. Deducción asistida por Codex. **Alcance:** modelo límite de siete clusters con reflexión A/C, mitades iguales en cada hoja, masas proporcionales a $(r,r,1,1,r,r,1+q)$ y el patrón fijo descrito en [conclusiones](conclusiones.md). No incluye todos los tamaños, fases, patrones ni correcciones a orden superior con separación finita.

El [preprint de O'Keeffe, v1](https://arxiv.org/html/2610.21271v1), sección IV.3, obtiene la constante de referencia por dos condiciones de neutralidad. Allí se presenta como observación numérica una optimalidad local en un modelo más amplio. El resultado de esta nota es una demostración de **optimalidad global en la subfamilia reducida especificada**, condicionada a la reducción algebraica previamente derivada. No se afirma novedad bibliográfica ni revisión humana independiente.

## Teorema

Sean $r>0$, $0<q<1$, $w>0$, $K=1+2q-q^2$, y

$$
\begin{aligned}
D&=r^2[-2(1+q)^2w^2+4(1-q^2)w+2K]+Kw^2,\\
R&=4r^2+Kw^2+4(1-q^2)w-4(1+q)^2.
\end{aligned}
$$

Definimos

$$
\mu(r,q)=\min\left\{
\frac{2r+2+2q}{4r+3+q},\quad
\frac{2+2r(1+q)}{4r+3+q},\quad
\frac{4r+1+q}{4r+3+q}
\right\}.
$$

Sea $a$ la única raíz en $(0,1)$ del polinomio

$$
p(a)=9a^8+72a^7+288a^6+448a^5+470a^4+88a^3-208a^2-128a-15.
$$

Si $D\geq0$ y $R\geq0$, entonces

$$
\boxed{\mu(r,q)\leq c:=\frac{4+2a}{7+a}=0.692907706369586\ldots.}
$$

La igualdad ocurre únicamente en

$$
r=1,\qquad q=a,\qquad w=w_*:=\sqrt{\frac{a^2+6a+1}{(a+1)^2}}.
$$

En el conjunto $D>0$, $R>0$, $c$ es el supremo y no se alcanza. Estas condiciones corresponden a la forma límite, no constituyen por sí solas un certificado para una plantilla a separación finita ni para un grafo simple finito. Tampoco dan una cota superior para la conectividad crítica general.

## Prueba

Escribimos $g_1,g_2,g_W$ para las tres fracciones de la definición de $\mu$.

### 1. La conectividad obliga a entrar en una región pequeña

Supongamos $\mu\geq c$. En particular $g_1,g_2\geq c$. Como $c>2/3$, la desigualdad $g_2\geq c$ implica

$$
2r(1+q-2c)\geq c(3+q)-2>0,
$$

de modo que $q>2c-1>1/3$. En este rango $g_2$ crece estrictamente con $r$, mientras que $g_1$ decrece estrictamente con $r$. Por tanto

$$
\min(g_1,g_2)\leq g_1(1,q)=g_2(1,q)=\frac{4+2q}{7+q}.
$$

La última fracción crece con $q$, por lo que $q\geq a$.

Resolviendo las dos desigualdades de grado se obtiene

$$
L(q)\leq r\leq U(q),\qquad
U(q)=\frac{-2a+5q+1}{3a+1},\qquad
L(q)=\frac{(a+2)q+2a-1}{(a+7)q-3a-1}.
$$

El denominador de $L$ es positivo para $a\leq q\leq1$. Además $U$ crece, $L$ decrece y $L(a)=U(a)=1$. En particular

$$
\frac{31}{50}<r_{\min}:=L(1)\leq r\leq U(1)=:r_{\max}<\frac85,
\qquad r_{\min}r_{\max}=1.
$$

Los extremos racionales son cotas amplias verificadas exactamente; no redondeos usados como hipótesis.

### 2. Todo candidato factible cumple $1<w<2$

Se verifican, uniformemente en $a\leq q\leq1$,

$$
R(U(q),q,1)<0,\qquad D(L(q),q,2)<0. \tag{A}
$$

Para verificar estos signos, multiplicar por los denominadores cuadrados positivos, sustituir $q=a+(1-a)t$ y expresar los numeradores en la base de Bernstein de $0\leq t\leq1$. Todos los coeficientes son estrictamente negativos: hay tres para $R$ y cinco para $D$. El verificador adjunto encierra cada coeficiente mediante fracciones exactas en un intervalo aislante de $a$.

Como $R$ crece con $r$ y con $w>0$, la primera desigualdad de (A) obliga a $w>1$ si $R\geq0$.

Para $w=2$,

$$
D(r,q,2)=r^2(2-12q-18q^2)+4K
$$

decrece con $r$ cuando $q\geq a$. La segunda desigualdad de (A) da $D(r,q,2)<0$. Como cuadrática en $w$, $D$ tiene término independiente positivo y término lineal no negativo. Su coeficiente principal debe ser negativo; tiene una única raíz positiva y esa raíz es menor que 2. Así $D\geq0$ exige $w<2$.

### 3. Se puede bajar $q$ hasta la frontera de conectividad

En la caja $r\geq31/50$, $q\geq13/20$, $1\leq w\leq2$, las dos funciones decrecen estrictamente con $q$.

Para $D_q$, el coeficiente de $w^2$ es $-4r^2(1+q)+2(1-q)<0$. El término lineal también es negativo, de modo que su máximo para $w\geq1$ ocurre en $w=1$, donde

$$
D_q\leq-16r^2q+2(1-q)<0.
$$

Por otro lado,

$$
R_q=2(1-q)w^2-8qw-8(1+q)\leq-24q<0.
$$

Para un $r$ fijo en el intervalo anterior, la menor $q$ que satisface ambas desigualdades $g_1,g_2\geq c$ es

$$
q_b(r)=
\begin{cases}
\displaystyle\frac{(1+3a)r+2a-1}{(7+a)r-2-a},&r\leq1,\\[6pt]
\displaystyle\frac{(1+3a)r+2a-1}{5},&r\geq1.
\end{cases}
$$

Es la igualdad de $g_2$ con $c$ en la primera rama y de $g_1$ con $c$ en la segunda. En ambas ramas $a\leq q_b\leq1$, con $q_b(1)=a$ y $q_b(r_{\min})=q_b(r_{\max})=1$.

Si existiera un candidato factible con $\mu\geq c$, mantener $r,w$ y sustituir $q$ por $q_b(r)\leq q$ preservaría $D,R\geq0$. Basta, por tanto, estudiar estas dos curvas de frontera.

### 4. No hay factibilidad en las dos curvas salvo en $r=1$

Sea

$$
\mathcal P(r,q)=\frac14\operatorname{Res}_w(D,R).
$$

Es un polinomio exacto con $\mathcal P(1,q)=p(q)$. En cada rama sustituimos $q_b(r)$ y multiplicamos por el denominador a la octava potencia, que es positivo. Después usamos $p(a)=0$ para reducir las potencias de $a$.

En la rama $r\geq1$, ponemos $r=1+z$. El numerador reducido tiene un factor $z$ y el cociente es un polinomio de grado 11. Sus **12 coeficientes de Bernstein en $0\leq z\leq3/5$ son estrictamente positivos**.

En la rama $r\leq1$, ponemos $r=1-z$. El numerador reducido vuelve a tener un factor $z$ y el cociente tiene grado 15. Sus **16 coeficientes de Bernstein en $0\leq z\leq19/50$ son estrictamente positivos**.

Estos intervalos cubren las ramas completas por las cotas de $r_{\min},r_{\max}$. Los signos se verifican con aritmética racional; los polinomios y los intervalos de cada coeficiente quedan en `global_optimum_certificate.json`. En consecuencia, para $r\ne1$ en las curvas,

$$
\operatorname{Res}_w(D(r,q_b(r),w),R(r,q_b(r),w))>0.
$$

En particular, las dos cuadráticas no comparten ninguna raíz.

Por el paso 2, en cada curva $D$ tiene una única raíz positiva $w_D<2$ y $R$ una única raíz positiva $w_R>1$. Ambas raíces varían continuamente con $r$. La factibilidad equivale a $w_R\leq w_D$. El orden de las raíces no puede cambiar en ninguna de las ramas abiertas $r>1$ y $r<1$, pues un cambio exigiría una raíz común.

En los extremos de las ramas $q_b=1$. Escribiendo $s=r^2$, las dos desigualdades allí exigirían

$$
8-2s\leq w^2\leq\frac{2s}{4s-1},
$$

y por tanto $s^2-4s+1\geq0$. Sin embargo este polinomio es negativo en todo

$$
\left[(31/50)^2,(8/5)^2\right]:
$$

es convexo y sus valores en ambos extremos son negativos. Los extremos de las dos ramas son, pues, infactibles. Por continuidad y ausencia de raíces comunes, las ramas completas con $r\ne1$ son infactibles.

### 5. Igualdad y supremo estricto

En $r=1,q=a$, las dos cuadráticas tienen la misma raíz positiva $w_*$, y únicamente allí pueden ser simultáneamente no negativas. Las identidades $D(1,a,w_*)=R(1,a,w_*)=0$ se comprueban reduciendo los numeradores módulo $p(a)$, escogiendo la raíz positiva. Además

$$
g_W(1,a)-c=\frac{1-a}{7+a}>0.
$$

Si $r=1$ y $q>a$, bajar $q$ hasta $a$ aumentaría estrictamente tanto $D$ como $R$, exigiendo que ambas fuesen estrictamente positivas allí, imposible. Por el paso 4, todo candidato con $\mu\geq c$ queda reducido a $(1,a,w_*)$, donde $\mu=c$. Esto prueba la cota y la unicidad.

Finalmente, fijar $r=1$, $w=w_*$ y tomar $q<a$ suficientemente próximo hace estrictamente positivas ambas desigualdades, por los signos de las derivadas del paso 3. La conectividad tiende a $c$. Queda probado el supremo en el conjunto estricto. $\square$

## Verificación y uso

`verify_global_optimum.py` comprueba el conteo de raíces, las identidades, los signos de (A), la monotonía usada, las cotas del dominio y los 28 coeficientes positivos de las dos resultantes. Usa SymPy y fracciones racionales, con las dependencias locales de `bootstrap.py`. Su salida es `global_optimum_certificate.json`; el verificador guarda su propia huella SHA-256. `run_checks.py` lo integra con las comprobaciones previas.

La demostración combina esos cálculos exactos finitos con el argumento explícito de continuidad. No es una formalización en un asistente de pruebas. Falta revisión humana independiente y una búsqueda bibliográfica más amplia antes de presentar el resultado como novedoso.

La consecuencia para el proyecto es concreta: buscar una mejora cambiando solo $r$ en este modelo límite no puede funcionar. Permanecen abiertas otras masas, otros desdoblamientos, otros patrones y las correcciones a separación finita. La conectividad aquí es el límite de plantilla; para un grafo finito se debe especificar $(\delta+1)/n$ o $\delta/(n-1)$ y convertir antes de comparar.

**Uso de IA:** Codex (OpenAI) propuso la prueba, derivó las sustituciones, programó las verificaciones y redactó esta nota a partir del objetivo del usuario «gana el invetigathon». La reducción inicial pertenece al trabajo previo de la misma carpeta y el patrón inicial procede del preprint citado. No se produjo una revisión independiente por otro agente ni por una persona.
