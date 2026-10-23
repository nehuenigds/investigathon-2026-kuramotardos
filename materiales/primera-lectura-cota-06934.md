# Primera lectura de la cota 0,6934

Para **Los Kuramotardos**. Preparada el 22/10/2026 después de que el usuario indicara que el equipo todavía no revisó la prueba. Esta guía explica el argumento; no registra una revisión o un ensayo realizado y no sustituye la demostración completa.

La exposición siguiente conserva la versión con Hessiano finito estricto, igual que los medios y el paquete congelados. Una [ampliación posterior](cota_minimos_locales_06934.md) sustituye esa hipótesis por minimalidad local real y explica con una cuenta cúbica por qué semidefinitud sola no basta. Requiere revisión antes de incorporarla a la defensa.

## 1. Empezar por Bullo: equilibrio, energía y rotación

Seguir la ruta solicitada: **17.1 y 17.2 de Bullo primero**. En la copia del proyecto son las páginas 271–277 del PDF; la rotación común aparece en la página 272 y la energía en la 276. La [[99 Sistema/Fichas/rec-465902e4-85fe-4e4f-a8f9-c65d690e81c8|guía del libro]] conserva los prerrequisitos puntuales a consultar si hacen falta. No es necesario recorrer primero todos los capítulos anteriores.

Tomemos un grafo simple no dirigido, con matriz de adyacencia $A$. Las frecuencias idénticas se eliminan mediante un marco que gira con ellas. Con una escala positiva de tiempo fijada, queda

$$\dot\theta_i=-\sum_j A_{ij}\sin(\theta_i-\theta_j).$$

Un **equilibrio** tiene todas esas sumas iguales a cero. La energía es

$$E(\theta)=\sum_{i<j}A_{ij}[1-\cos(\theta_i-\theta_j)],\qquad\dot\theta=-\nabla E.$$

La sincronía tiene todas las fases iguales. El problema permite otros equilibrios: que las fuerzas se cancelen no obliga por sí solo a que coincidan las fases.

Para estudiar un equilibrio calculamos el Hessiano $H=\nabla^2E$. Su forma cuadrática es

$$v^THv=\sum_{i<j}A_{ij}\cos(\theta_i-\theta_j)(v_i-v_j)^2.$$

Mover todas las fases por el mismo ángulo no cambia la energía. Por eso $H\mathbf1=0$ siempre. Exigimos positividad estricta en $\mathbf1^\perp$: cualquier variación pequeña que no sea una rotación común aumenta la energía a segundo orden. En un equilibrio esto da un mínimo estricto y estabilidad local módulo rotación. Un autovalor transversal negativo implica inestabilidad; ceros adicionales dejan inconcluso este criterio.

**La primera distinción que hay que poder explicar:** se comprueba equilibrio antes de clasificar estabilidad. Un Hessiano positivo calculado fuera de un equilibrio no certifica un estado estacionario estable.

Un ejemplo pequeño ayuda a fijar el orden. Para dos vértices unidos por una arista, escribir $\Delta=\theta_1-\theta_2$. El primer residuo es $\sin\Delta$ y el autovalor transversal del Hessiano es $2\cos\Delta$:

| Diferencia de fases | Primer residuo | Autovalor transversal | Conclusión |
| --- | ---: | ---: | --- |
| $0$ | $0$ | $2$ | Equilibrio sincronizado estricto módulo rotación |
| $\pi$ | $0$ | $-2$ | Equilibrio inestable |
| $\pi/2$ | $1$ | $0$ | No es equilibrio; no se clasifica como estado estacionario |

Esta cuenta solo explica el criterio local; no es una construcción densa ni un ejemplo de la clase de siete clusters.

## 2. Qué cambia al pasar a siete clusters

Una plantilla resume grupos de vértices que comparten fase. Cada cluster tiene masa $x_i>0$, las masas suman uno y las densidades satisfacen $P_{ij}=P_{ji}\in[0,1]$. Es un modelo ponderado: no se está enumerando un grafo simple.

El equilibrio de plantilla y su grado mínimo ponderado se escriben

$$F_i=\sum_jx_jP_{ij}\sin(\theta_i-\theta_j)=0,\qquad
\mu(T)=\min_i\sum_jx_jP_{ij}.$$

Su energía usa $x_ix_jP_{ij}$ en lugar de $A_{ij}$. Aquí $\partial_iE=x_iF_i$: la dinámica $\dot\theta=-F$ es un flujo gradiente con pesos de masa. No se debe copiar literalmente la identidad $\dot\theta=-\nabla E$ del grafo sin ese factor. Como las masas son positivas, la positividad del Hessiano módulo rotación sigue dando el criterio estricto que usamos.

El teorema estudia **sucesiones** de estas plantillas. Cada elemento finito está en equilibrio exacto y tiene Hessiano estricto fuera de la rotación. Sus siete masas convergen a valores positivos. Sus fases convergen, tras una rotación común, a

$$\left(0,0,\frac\pi2,\frac\pi2,\pi,\pi,\frac{3\pi}2\right).$$

Llamamos A, B, C y W a esas cuatro hojas de fase. A, B y C se dividen en dos clusters; W tiene uno. «Próximos a cuatro fases» no exige mitades iguales ni una única escala de separación.

## 3. Qué afirma 0,6934

Para cada sucesión que satisface las hipótesis anteriores,

$$\limsup_\ell\mu(T_\ell)<\frac{3467}{5000}=0{,}6934.$$

La construcción conocida de O'Keeffe aporta valores límite que llegan a $\mu_0\approx0{,}69290770637$. Por eso el supremo de valores límite de **esta clase** queda en $[\mu_0,0{,}6934]$, un intervalo de ancho menor que $0{,}000493$.

No se prueba que el supremo sea $\mu_0$. No se cubren masas límite nulas, otros repartos de clusters ni otras geometrías. Tampoco es una cota superior para todos los grafos o para la conectividad crítica general. La construcción inferior se atribuye a O'Keeffe; la novedad concreta de la cota superior sigue pendiente de contraste.

El patrón exactamente a cuartos de vuelta puede tener ceros adicionales en el Hessiano. Esa degeneración impide usarlo como ejemplo estricto que contradiga el teorema. La hipótesis estricta se exige antes de tomar el límite.

## 4. La prueba como una cadena de condiciones necesarias

Se razona por contradicción: suponer que el límite superior del grado alcanza al menos $u=3467/5000$. Se extrae una subsucesión que realiza ese límite y se deducen condiciones que todo candidato real tendría que satisfacer.

1. **Normalizar la separación.** Fijar W y dividir los desvíos angulares por su máximo $h$. Los offsets quedan acotados y alguno tiene límite de valor absoluto uno. Así se admiten distintas escalas; algunas separaciones principales pueden desaparecer, pero no todos los offsets.
2. **Usar equilibrio y Hessiano.** Una identidad exacta, con restos trigonométricos acotados, fuerza enlaces opuestos de orden $O(h^2)$. La semidefinitud del Hessiano de las cuatro hojas da cuatro cancelaciones principales. No se derivan masas o densidades respecto de $h$.
3. **Relajar internos y descartar flujos cero.** Completar internos aumenta grados y relaja pruebas necesarias de estabilidad. No se afirma que conserve un equilibrio finito. Bajo el grado supuesto, los casos de flujo cero son imposibles. Solo después se toman centros por flujo y se demuestra que el vector variacional $z$ es no nulo.
4. **Normalizar el flujo y conservar las masas.** Cada corte adyacente lleva el mismo flujo total; se reescala a uno. Los productos de flujo por masa de A, B y C son $a,b,c$. Dos transportes aportan covarianzas $\kappa,\lambda$. Capacidades y grados imponen cotas sobre esos parámetros y sobre las masas vecinas.
5. **Excluir el dominio resultante.** Bajo el grado hipotético, $(a,b,c)$ está en el cubo $[967/1533,1533/967]^3$. El certificado cubre todo ese cubo. En cada caja contradice una capacidad o demuestra que ningún $z\ne0$ puede satisfacer las dos pruebas necesarias de estabilidad.

Si se pierde una posibilidad real en cualquiera de los primeros pasos, el certificado del último paso no la recupera. Por eso la revisión de la reducción analítica es indispensable.

## 5. Una cuenta que conviene hacer a mano

La desigualdad de masas vecinas es una parte accesible de la mejora de la cota. En una hoja dividida, sean $m_0,m_1$ sus masas brutas y $f_0,f_1$ los flujos de las mitades. Se normalizó $f_0+f_1=1$. Definir $\tau_i=f_i/m_i$.

Si una hoja vecina tiene masa $B$, sus capacidades imponen $\tau_0,\tau_1\leq B$. Entonces

$$B-\tau_0\tau_1(m_0+m_1)
=m_0\tau_0(B-\tau_1)+m_1\tau_1(B-\tau_0)\geq0.$$

Con $\chi=\tau_0\tau_1$ y $M=m_0+m_1$, obtenemos **$\chi M\leq B$**. La misma cuenta sirve para ambas hojas vecinas. Estas relaciones permiten propagar cotas entre masas en vez de acotarlas por separado.

Ejemplo exacto de un solo corte: $m_0=1$, $m_1=2$, $f_0=f_1=1/2$ y $B=3/4$. Entonces $\tau_0=1/2$, $\tau_1=1/4$, $\chi=1/8$ y $\chi M=3/8\leq3/4$. La diferencia es $3/8=1/4+1/8$, justamente la suma de los dos términos no negativos. Estos datos ilustran el lema; no especifican una plantilla completa de Kuramoto ni una nueva cota inferior.

## 6. Qué aporta el programa y qué revisar al leer

El árbol tiene 15.511 nodos y 7.756 hojas. No es una grilla de puntos: cada hoja justifica una desigualdad uniforme sobre una caja, incluidos sus bordes. En las hojas matriciales se usan dos condiciones necesarias

$$\|L_1z\|^2\leq\|z\|^2,\qquad \|L_2z\|^2\leq\|z\|^2.$$

Si para algún $\alpha\in[0,1]$ se certifica

$$\alpha L_1^TL_1+(1-\alpha)L_2^TL_2-I\succ0,$$

se obtiene una contradicción, porque $z\ne0$. Las [notas de defensa](exposicion/notas_defensa.md) escriben las matrices y las cuentas de escala completas. No hace falta entender primero cada detalle de Bernstein para entender esta contradicción.

| Parte | Evidencia disponible | Qué requiere lectura humana |
| --- | --- | --- |
| Equilibrio, límites y flujos | Demostración analítica | Que cubra todas las sucesiones de la clase declarada |
| Identidades y cambio de variables | Texto e identidades simbólicas | Que las variables representen los datos originales con las hipótesis necesarias |
| Cajas e inecuaciones | Verificador racional y controles de alteraciones | Que las condiciones verificadas sean las deducidas en la reducción |
| Interés y antecedentes | Fuentes y revisión acotada | La novedad y el valor del resultado para el evento |

Constructor y verificadores proceden de Codex. Un comprobador separado reduce ciertos errores de código, pero no constituye revisión humana independiente.

Para comprobar comprensión, intentar explicar sin leer: qué hipótesis excluye el C4 degenerado; por qué completar internos no exige construir otro equilibrio; por qué $z\ne0$ es esencial; y qué paso de la prueba no puede validar por sí solo el programa. Las respuestas están desarrolladas en las notas de defensa. Este documento no registra que el equipo haya respondido esas preguntas.

## Fuentes y siguiente lectura

La base del modelo procede de Bullo, *Lectures on Network Systems*, edición 1.6, capítulo 17. La construcción inferior se atribuye a O'Keeffe, *Beyond 11/16*, arXiv:2610.21271v1, IV.3; el estado bibliográfico está en [la revisión acotada](revision_bibliografica.md).

Leer después el [enunciado y prueba de 0,6934](cota_flujos_06934.md), que enlaza la [reducción base](cota_perfil_general.md) y las [capacidades agregadas](cota_capacidades_agregadas.md). El [paquete matemático](kit-cota-flujos-06934-v1.zip) y su [guía](kit_cota_flujos_06934.md) permiten reproducir el certificado. El [guion breve](guion-checkpoint-equipo.md) sirve para preparar la exposición una vez revisado el argumento.

**Uso de IA:** explicación, ejemplo y redacción por Codex (OpenAI), a partir de las fuentes y pruebas del cuaderno. No hubo subagentes ni se realizó una revisión humana, un ensayo o una entrega al evento mediante esta preparación.
