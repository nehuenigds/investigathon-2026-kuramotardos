# Flujos por masa: refuerzo y límite de una relajación

20/10/2026. Investigación asistida por Codex. Modelo: plantillas del Kuramoto homogéneo de siete clusters, próximas a cuatro fases con reparto `(2,2,2,1)`. La reducción y sus hipótesis son las de [la cota 0,70](cota_perfil_general.md) y [la cota 0,6935](cota_capacidades_agregadas.md). Revisión humana y novedad bibliográfica pendientes.

Se releyó [O'Keeffe v1, IV.3](https://arxiv.org/html/2610.21271v1) antes de esta ampliación. Se atribuyen al artículo la construcción y la constante inferior conocida $\mu_0\approx0.69290770637$. La familia de mitades desiguales ya se menciona allí como observación numérica. Esta nota no acredita una nueva cota inferior para Kuramoto.

## 1. Una desigualdad que conserva masas vecinas

En la reducción de las notas anteriores el flujo de cada corte adyacente está normalizado a uno. Para una hoja dividida, sean $m_0,m_1>0$ sus masas y $f_0,f_1>0$ los flujos salientes, con $f_0+f_1=1$. El equilibrio principal iguala los flujos entrantes y salientes de cada mitad. Escribir

$$M=m_0+m_1,\qquad \tau_i=f_i/m_i,\qquad \chi=\tau_0\tau_1.$$

Si $B$ es la masa de cualquiera de sus dos hojas vecinas, las capacidades de densidad dan $0<\tau_i\leq B$, usando el corte entrante o el saliente, según corresponda. La identidad

$$B-\chi M=m_0\tau_0(B-\tau_1)+m_1\tau_1(B-\tau_0)\geq0\tag{1}$$

prueba $\chi M\leq B$. No se presupone igualdad de mitades o flujos. Tampoco se identifica grado mínimo con promedio.

Poniendo $a=\chi_A,b=\chi_B,c=\chi_C$ y $y_i=M_i/N$, se obtienen seis restricciones lineales en las masas:

$$a y_A\leq y_B,y_W,\qquad b y_B\leq y_A,y_C,\qquad c y_C\leq y_B,y_W.\tag{2}$$

En la construcción conocida las capacidades hacia W pueden saturar (1). La desigualdad se usa como condición necesaria; no afirma que las condiciones reducidas basten para realizar un transporte.

## 2. Propagación exacta en cajas

Sea $u\in(2/3,3/4)$ un grado mínimo hipotético. Para una caja $a\in[a_0,a_1]$, $b\in[b_0,b_1]$, $c\in[c_0,c_1]$, las cotas anteriores dan

$$A_0=\max\left(\frac{u}{1+2a_1},u-\frac12\right),\quad B_0=\frac{u}{1+2b_1},\quad C_0=\max\left(\frac{u}{1+2c_1},u-\frac12\right).$$

Cada uno de los siguientes pasos conserva una cota inferior válida:

$$\begin{aligned}
L_B&=\max(B_0,a_0A_0,c_0C_0),\\
L_A&=\max(A_0,b_0L_B),\qquad L_C=\max(C_0,b_0L_B),\\
L_W&=\max(u-\tfrac12,a_0L_A,c_0L_C).
\end{aligned}\tag{3}$$

Si $\max L_i>1-u$ o $\sum L_i>1$, toda la caja es imposible. En caso contrario se reutilizan las restricciones de escala y cortes de la nota 0,6935 con estas cotas inferiores más fuertes. En concreto, $D=\max L_i(u-L_i)$ sigue siendo una cota inferior válida porque $L_i\leq y_i\leq1-u<u/2$. No se aplica esa monotonía a una cota que ya excedió $1-u$.

`profile_upper_mass_flow_interval.py` implementa (3) con fracciones. El constructor usa números flotantes para proponer parámetros matriciales, pero solo acepta desigualdades racionales estrictas. El verificador separado reimplementa las exclusiones y no importa el constructor ni sus predicados.

## 3. Por qué estas condiciones no prueban 0,69291

El intento `profile_upper_attempt_069291-v1.json` terminó sin completar la cobertura: alcanzó profundidad 81, por encima del máximo 80, tras visitar 1.094 nodos. No es un certificado ni se infiere una cota del tiempo o de la profundidad agotados.

Hay una obstrucción exacta para esta relajación concreta. Tomar

$$a=c=\frac{8427}{10000},\quad b=\frac{101}{125},\quad k=l=\frac{8739}{50000},\quad z=(1,\frac{28993}{20000},1).$$

El punto satisface estrictamente las dos pruebas de estabilidad de la reducción y todas sus capacidades de covarianza. Las holguras de estabilidad son, respectivamente,

$$\frac{373510048310071}{500000000000000000}>0,\qquad\frac{32144867590071}{500000000000000000}>0.$$

También satisface estrictamente todas las condiciones proyectadas de masas y escala usadas por el predicado nuevo, tanto con $u=0.6932$ como con $u=0.69291$. `verify_mass_flow_relaxation.py`, con Python estándar, comprueba todas esas desigualdades y guarda sus márgenes en `mass_flow_relaxation_witness.json`.

Esto prueba que **esas desigualdades necesarias, por sí solas, no pueden excluir ese punto ni demostrar la cota 0,69291**. Ninguna combinación convexa de las dos formas puede ser definida positiva menos la identidad allí, porque el vector $z\ne0$ satisface ambas formas estrictamente por debajo de su energía.

El punto no contiene masas realizadas, matrices de transporte, fases, equilibrio ni Hessiano de una plantilla. No es un contraejemplo de Kuramoto, no mejora $\mu_0$ y no prueba que la clase asintótica pueda llegar a 0,6932. Señala información que la proyección ha perdido; una cota más cercana requiere restricciones adicionales, no solo subdividir más este mismo dominio.

## 4. Exploración y evidencia

`explore_mass_flow_projection.py` conserva 24 arranques, semilla 200071 y hasta 700 iteraciones en `mass_flow_projection_20261020-flow-v1.json`. Hay terminaciones sin converger y restricciones violadas. Los puntos numéricos solo orientaron la racionalización anterior; no se aceptaron como equilibrios. El testigo racional se comprueba sin ejecutar esa búsqueda.

La cota anterior 0,6935 sigue respaldada por su certificado congelado. El intento de 0,6934 se registra por separado; solo una cobertura completa y su reproducción exacta podrán reforzarla. El informe, la charla v12 y los paquetes anteriores conservan su contenido.

**Uso de IA:** Codex (OpenAI) realizó consulta, deducción, programación, búsqueda, comprobaciones y texto. El constructor y los verificadores proceden del mismo agente. No equivalen a revisión humana independiente. No hubo subagentes, comunicaciones, publicación ni entrega al evento.
