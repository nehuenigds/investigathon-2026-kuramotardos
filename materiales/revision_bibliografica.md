# Revisión bibliográfica acotada

18/10/2026. Lectura asistida por Codex. Esta nota documenta lo consultado; no certifica novedad ni reemplaza una revisión especializada.

| Fuente primaria | Partes contrastadas | Relación con el trabajo |
| --- | --- | --- |
| [O'Keeffe, arXiv:2610.21271v1](https://arxiv.org/html/2610.21271v1) | IV.3, A.1-A.5 y lema de realización | Proporciona el patrón, predictor, constante y realización. En IV.3 presenta la optimalidad local de su modelo como observación numérica. El teorema del cuaderno prueba un máximo global en una subfamilia con masas $(r,r,1,1,r,r,1+q)$ y simetrías fijadas; no cubre todo aquel modelo. |
| [Canale, arXiv:2209.06362v3](https://arxiv.org/html/2209.06362v3) | III-V | Construye grafos simples a partir de grafos con pesos enteros y estudia una familia de ocho vértices. Es un antecedente directo para el paso de ponderado a no ponderado. No se identificó en las secciones consultadas el mismo argumento general de racionalización por bosque y coordenadas racionales del círculo. |
| Bullo, *Lectures on Network Systems*, edición 1.6 | 17.1-17.2 | Base para equilibrio, simetría de rotación y estabilidad transversal. La lectura directa consta en la bitácora anterior. |
| [Lepsveridze y Zhang, arXiv:2608.20010v1](https://arxiv.org/abs/2608.20010) | Resumen consultado directamente | Declara una cota estricta por debajo de $3/4$ para la versión de mínimos locales. Se usa como contexto; en esta continuación no se reprodujo su prueba. |
| [Menara, Baggio, Bassett y Pasqualetti, *Functional control of oscillator networks* (2022)](https://www.nature.com/articles/s41467-022-31733-2) | Resultados, ecuaciones 4, 5, 9 y 11; sección de métodos sobre caminos | Expresa la asignación de fases como un problema lineal en los pesos, describe soluciones mediante el espacio de ciclos y formula intervenciones convexas. Es un antecedente directo: corregir pesos para imponer fases no se presenta como una idea nueva. |
| [Boyd y Vandenberghe, diapositivas de *Convex Optimization*, capítulo 5](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf) | Dualidad débil, diapositiva 5.11 | La cota dual de la nueva nota aplica un principio estándar. No se reivindica novedad para dualidad, SDP ni la certificación mediante multiplicadores factibles. |

Las búsquedas breves por racionalización, puntos racionales del círculo y equilibrio de Kuramoto no alcanzaron para resolver la cuestión bibliográfica. El uso de flujos en árboles y la parametrización racional del círculo son herramientas elementales conocidas; se presenta como deducción de esta sesión la combinación y su aplicación, con novedad pendiente.

Para exponer, atribuir siempre a O'Keeffe la construcción y la constante. Describir con las hipótesis completas el teorema de optimalidad del cuaderno y distinguir el argumento de racionalización de un nuevo récord de conectividad.

La continuación posterior obtuvo una [separación exacta entre dos clases de densidades a geometría finita fija](obstruccion_patron_finito.md): un enlace opuesto permite superar la cota superior de toda la clase que los prohíbe. La prueba global del modelo límite mantiene otro alcance. La consulta de O'Keeffe, Menara y las referencias ya registradas no identificó esta separación concreta, pero no confirma su novedad bibliográfica. El libro completo de Boyd no se pudo recuperar mediante la herramienta; se consultaron las diapositivas oficiales, sin atribuirle una lectura del libro.

## Relectura para delimitar la contribución

Se volvió a consultar directamente el preprint v1, en especial A.4: ya impone equilibrio exacto mediante una corrección sobre un camino de enlaces adyacentes. A.5 racionaliza masas y densidades resolviendo fases por el teorema de la función implícita. Por ello no se debe presentar corregir el equilibrio con un camino como una invención del cuaderno. La variante de coordenadas racionales conserva un alcance distinto, con novedad sin resolver.

| Afirmación posible | Qué puede defenderse con lo consultado |
| --- | --- |
| Usar linealidad en pesos, flujos o SDP es un método nuevo para Kuramoto | No: atribuir los antecedentes de diseño de pesos y las herramientas estándar. |
| La subfamilia límite tiene un máximo global en $r,q,w$ | Hay una prueba propia para ese dominio preciso; no sustituye la observación del modelo más amplio del preprint. Novedad pendiente. |
| Un enlace opuesto supera toda la clase sin opuestos a esta geometría | Hay una separación exacta concreta; no se confirmó si existe antes en la literatura. |
| Esa separación persiste al perturbar masas y puntos | Se añadió una [prueba cuantitativa en una caja de radio $10^{-17}$](separacion_abierta.md). Apertura de condiciones estrictas y convexidad son principios conocidos; no se reivindican como nuevos. |

Se hicieron búsquedas dirigidas sobre fases fijas, pesos, semidefinitud, conectividad crítica y coordenadas racionales. No proporcionan una prueba de ausencia de antecedentes. La extensión abierta refuerza el alcance matemático del ejemplo concreto; por sí sola no resuelve su interés ni su novedad para el evento.

**Uso de IA:** Codex realizó las lecturas, el contraste y esta síntesis. No se consultó a autores ni a mentores.

Se volvió a consultar directamente el Lema 2 y su demostración en el Apéndice B del preprint. El nuevo [traslado a grafos simples](separacion_grafos_simples.md) aplica ese lema, completa los grupos de fase igual y usa promedios para acotar grafos sin regularidad entre bloques. La realización no se presenta como un lema nuevo ni como una enumeración de aristas. La novedad de la separación concreta continúa pendiente. El usuario confirmó que el equipo todavía no recibió devolución de un mentor.

## Contraste y deducción del 19/10/2026

Se releyeron III, IV.3, VI y A.1–A.5 de [O'Keeffe v1](https://arxiv.org/html/2610.21271v1). El problema convexo con fases fijas y el paso por agrupación ya están formulados allí; tampoco se presentan como invenciones del cuaderno. A.4 identifica el efecto de orden principal de opuestos de tamaño $h^2$. La observación de optimalidad de IV.3 sigue sin ser una demostración global de todas las geometrías.

La [deducción nueva del cuaderno](enlaces_opuestos_limite.md) convierte esa observación de escala en dos cotas necesarias: $\limsup\sum_{A-C}P_{ij}/h^2\leq D/(2r^2)$ y $\limsup\sum_{B-W}P_{ij}/h^2\leq R/[2(1+q)]$. Usa doce coeficientes adyacentes independientes y la prueba restringida anterior. Concluye una cota para la conectividad límite y rigidez de opuestos en el caso de igualdad. Son consecuencias matemáticas aquí demostradas bajo sus hipótesis; no se acredita que sean nuevas en la literatura.

Se buscaron términos sobre fases fijas, grado mínimo, conectividad crítica, enlaces opuestos y diseño de pesos. El resultado primario pertinente volvió a ser [Menara y colaboradores (2022)](https://www.nature.com/articles/s41467-022-31733-2); los resultados ajenos a osciladores no se usaron como antecedentes técnicos. La búsqueda no prueba ausencia de trabajos previos. El usuario confirmó nuevamente que no hubo devolución de mentor. La separación finita permanece como candidata para discutir, sin convertir esta recomendación en una elección del equipo.

La [ficha de arXiv consultada el 19/10](https://arxiv.org/abs/2610.21271) muestra solo v1, del 15/10. Se volvió a leer A.2–A.4 antes de deducir la [obstrucción para el perfil principal sin suavidad](patron_principal_limite.md). Esa deducción usa una identidad exacta de equilibrio para evitar derivadas y traslada la cota a sucesiones del perfil especificado; se atribuye al preprint la existencia de sucesiones estrictas que alcanzan el valor como límite. No se identificó allí una demostración del mismo enunciado superior, pero esta consulta no acredita novedad ni cubre toda la literatura.

## Perfiles generales y mitades desiguales

Se volvió a consultar la ficha y III, IV.3 y A.2–A.4 de v1 antes de la [ampliación a cuatro hojas](perfil_general_cuatro_hojas.md). IV.3 menciona como observación numérica una familia de un parámetro con mitades desiguales que parece alcanzar el mismo valor; esa mención no proporciona su parametrización. La nota construye una deformación explícita que cumple esa propiedad y prueba su máximo dentro de esa subfamilia. No se afirma haber identificado la misma parametrización del autor ni descubierto el fenómeno.

El criterio general usa equilibrio, complementos de Schur, circulaciones y positividad; son herramientas estándar. La prueba realiza la completación mediante densidades y una sucesión de equilibrios estrictos, con hipótesis explícitas. La consulta no acredita novedad de ese criterio en la literatura ni permite concluir que todos los perfiles generales tengan máximo $\mu_0$. No hubo consulta a autores o mentores.

## Cota asintótica 7/10

Se volvió a consultar la ficha de arXiv y la sección IV.3 antes de la [cota para siete clusters próximos a cuatro fases](cota_perfil_general.md); la ficha seguía mostrando v1. La nueva deducción permite masas y adyacencias asimétricas y demuestra una cota de 0,70 para la clase asintótica indicada mediante reducción y cobertura racional. No sustituye la cota inferior conocida ni determina el umbral general. Covarianzas, comparación de matrices, Sylvester y Bernstein son herramientas estándar; su uso no se reivindica como nuevo. Esta lectura no acredita novedad bibliográfica de la cota concreta y no constituye revisión independiente del argumento.

Se volvió a consultar el preprint antes de la [mejora a 0,6935 por capacidades totales](cota_capacidades_agregadas.md). La construcción de la fuente sigue proporcionando el extremo inferior del intervalo para esta clase; la cota nueva conserva hipótesis sobre siete masas límite positivas, cuatro fases y Hessiano finito estricto. No se atribuye novedad a la desigualdad de producto a suma fija, a las capacidades agregadas ni a los métodos de certificación. El interés y la novedad del resultado concreto requieren revisión independiente; no se hizo una búsqueda exhaustiva de toda la literatura.

El 20/10 se releyó IV.3 de [v1](https://arxiv.org/html/2610.21271v1) antes del [refuerzo por flujos por masa](cota_flujos_por_masa.md). La desigualdad elemental de capacidades no se presenta como una herramienta nueva. El testigo racional posterior solo pertenece a una relajación de condiciones necesarias; no contradice la construcción del artículo, no mejora su cota inferior y no acredita novedad matemática. No se comprobó que el autor utilizara o descartara la misma proyección. La consulta de esta fuente no constituye una búsqueda exhaustiva ni revisión humana independiente.

## Cota 0,6934 y foco de defensa

La ficha de arXiv seguía mostrando solo v1 al volver a consultar la fuente para la [cota 0,6934](cota_flujos_06934.md). IV.3 estudia el patrón simétrico y atribuye carácter numérico a sus observaciones de optimalidad y de mitades desiguales. La nueva cota mantiene una clase concreta de siete masas límite positivas y cuatro fases, sin afirmar un umbral universal ni haber descubierto la construcción inferior. La cobertura exacta demuestra el resultado junto con su reducción analítica; no demuestra novedad bibliográfica.

El usuario eligió ese resultado como foco de la defensa el 22/10. La elección editorial no sustituye la revisión del argumento ni el contraste de antecedentes. Informe y charla atribuyen la constante inferior a O'Keeffe, declaran la asistencia de Codex y distinguen las herramientas estándar de la deducción concreta. No hubo consulta a autores o mentores ni se acredita una búsqueda exhaustiva de toda la literatura.

## Contraste focalizado del 22/10 y ampliación a mínimos locales

Se consultaron de nuevo las fichas de arXiv y se contrastaron las partes indicadas abajo. O'Keeffe seguía mostrando solo v1. Las búsquedas incluyeron `Kuramoto "0.6934"`, `Kuramoto "0.693" bound`, siete clusters, desdoblamiento y cuatro fases, con consultas dirigidas a arXiv. No se identificó el mismo enunciado en las fuentes contrastadas. La indexación limitada y esta selección no prueban ausencia de antecedentes.

| Fuente primaria y parte leída | Distinción relevante |
| --- | --- |
| [O'Keeffe v1, IV.3 y Teorema 1](https://arxiv.org/html/2610.21271v1) | La construcción da el extremo inferior. El modelo límite analizado fija el patrón simétrico; la observación de máximo local y la familia de mitades desiguales se señalan como numéricas. No presenta allí la cota superior 0,6934 para toda nuestra clase. |
| [Lepsveridze–Zhang v1, Teorema 1 y Lema 11](https://arxiv.org/html/2608.20010v1) | Prueban una cota universal con eta positivo sin fijarlo; el lema elimina las cuatro fases exactas mediante un descenso cúbico. |
| [Kassabov–Strogatz–Townsend, resumen](https://arxiv.org/abs/2105.11406) | La cota 3/4 y su barrera para el análisis puramente lineal son antecedentes, no aportes del cuaderno. |
| [Canale v3, resumen y ficha](https://arxiv.org/abs/2209.06362) | El paso de grafos ponderados a no ponderados tiene un antecedente directo. |

**Consecuencia para la defensa, inferida de ese contraste:** no puede presentarse 0,6934 como una mejora de la cota universal `3/4 - eta`, cuyo valor de eta no se fija en el texto consultado. La comparación defendible es una constante explícita en una clase declarada; no se afirma prioridad bibliográfica ni que no pueda deducirse cuantitativamente de otros trabajos.

La nueva [ampliación a mínimos locales](cota_minimos_locales_06934.md) sustituye la positividad estricta del Hessiano finito por minimalidad local real, incluso con degeneración. La auditoría del argumento superior identificó que la hipótesis estricta se usaba para descartar separación angular exactamente cero. Una adaptación ponderada del descenso conocido permite descartarla por minimalidad y grado. El resto usa equilibrio y semidefinitud, y llega al mismo dominio certificado. Es una deducción del cuaderno con revisión y novedad pendientes; no se atribuye novedad al descenso cúbico ni se clasifica estabilidad a partir de ceros espectrales.

El informe, la charla, el póster y el paquete del equipo ya congelados mantienen el enunciado de la subclase estricta. Esta ampliación no se incorporó retrospectivamente a ellos. No hubo consulta a autores o mentores.
