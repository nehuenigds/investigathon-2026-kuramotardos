# Guion propuesto de 15 minutos: mínimos locales

Versión ampliada para revisión de Los Kuramotardos. Tiempos objetivos: 900 segundos, sin ensayo medido. La cantidad de expositores sigue pendiente de respuesta; no se asignaron roles.

## 1. Kuramoto: una cota asintótica

Tiempo objetivo: 30 segundos.

Presentamos una cota superior para mínimos locales de una clase asintótica de siete clusters próximos a cuatro fases. La conectividad límite superior es menor que 0,6934. El argumento permite mínimos degenerados, bajo las hipótesis que precisaremos. La construcción inferior corresponde a O’Keeffe y el descenso que descarta las cuatro fases exactas se atribuye a Lepsveridze y Zhang. La portada es una ilustración conceptual. La reducción analítica y la novedad requieren revisión independiente.

Fuentes:

- cota_minimos_locales_06934.md
- cota_flujos_06934.md
- Lepsveridze y Zhang, arXiv:2608.20010v1, Lema 11, https://arxiv.org/html/2608.20010v1
- O’Keeffe v1, https://arxiv.org/html/2610.21271v1
- exposicion/visual_asset.md

## 2. El modelo de Kuramoto

Tiempo objetivo: 55 segundos.

Comenzamos con osciladores idénticos en un grafo simple no dirigido. Al quitar la frecuencia común, su dinámica es el flujo negativo de esta energía. Cada arista aparece una vez. En sincronía las fases son iguales, pero pueden existir otros mínimos locales. La pregunta es cuánta conectividad permite esos estados. La propuesta usa el grado mínimo más uno dividido por n. Otras fuentes usan delta dividido por n menos uno. A orden finito convertimos las expresiones. En sucesiones de orden creciente, sus diferencias con delta sobre n se anulan. No se sustituye grado mínimo por grado promedio.

Fuentes:

- Bullo, Lectures on Network Systems, ed. 1.6, capítulo 17.1-17.2.
- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- Bullo, Lectures on Network Systems, ed. 1.6, capítulo 17.1–17.2.
- Propuesta local: modelo y normalización.

## 3. Equilibrio y estabilidad

Tiempo objetivo: 55 segundos.

Primero comprobamos que el residuo de equilibrio sea cero. El Hessiano tiene el cero inevitable de la rotación global. Un autovalor transversal negativo implica inestabilidad. Si todos son estrictamente positivos, tenemos un mínimo estricto módulo rotación. Los ceros adicionales requieren analizar órdenes superiores de la energía. Nuestro teorema ampliado supone directamente un mínimo local real, que proporciona equilibrio y semidefinitud. Estas dos condiciones necesarias por sí solas no certifican minimalidad. El caso de cuatro fases exactas mostrará por qué necesitamos esa distinción.

Fuentes:

- Bullo, Lectures on Network Systems, ed. 1.6, capítulo 17.1-17.2.
- cota_minimos_locales_06934.md

## 4. Cuatro fases y siete clusters

Tiempo objetivo: 45 segundos.

Las hojas A, B y C se dividen en dos clusters y W permanece entera. Así aparecen siete masas positivas. El gráfico muestra las cuatro fases límite y no las proporciones de masas. Permitimos distintas escalas de separación y asimetrías en los datos que se acercan a ellas. El C4 exacto puede tener conectividad tres cuartos y Hessiano semidefinido. Un giro de hojas reduce su energía cuando hay enlaces adyacentes. Después usaremos esa perturbación para excluir la separación exactamente cero en una sucesión de grado alto.

Fuentes:

- cota_minimos_locales_06934.md
- auditoria_flujos_centros.md
- O’Keeffe v1, https://arxiv.org/html/2610.21271v1

## 5. La construcción conocida

Tiempo objetivo: 50 segundos.

La constante inferior procede del preprint de O’Keeffe, no de esta investigación. Su familia de estados estrictos se aproxima a mu0 al reducir el desdoblamiento. La fuente analiza un patrón simétrico y prueba la existencia de los estados. En IV.3 aclara que las observaciones de optimalidad de su modelo no son una prueba del umbral general. Nuestra pregunta es distinta: acotar todos los valores límite dentro de una clase de siete clusters que se acercan a cuatro fases, liberando asimetrías y densidades principales. No afirmamos aumentar la constante inferior ni resolver el problema para todos los grafos.

Fuentes:

- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- optimalidad_global.md

## 6. La clase asintótica

Tiempo objetivo: 65 segundos.

Pasamos explícitamente del grafo a una plantilla ponderada. Las masas son positivas y suman uno, y las densidades son simétricas y están entre cero y uno. La energía suma x_i x_j P_ij por uno menos el coseno de la diferencia de fase. Exigimos que cada configuración finita sea un mínimo local real de esa energía, permitiendo degeneración. La conectividad es el mínimo de los grados ponderados. Las masas tienen límites positivos y las fases convergen al vector mostrado. Se admiten internos incompletos y distintas escalas. Las masas límite nulas y otras geometrías quedan fuera del enunciado.

Fuentes:

- cota_minimos_locales_06934.md
- cota_flujos_06934.md

## 7. La cota de esta clase

Tiempo objetivo: 55 segundos.

Cada sucesión con las hipótesis anteriores tiene límite superior de conectividad menor que 3467 sobre 5000. Para el supremo entre sucesiones informamos el intervalo cerrado mostrado, sin afirmar un margen uniforme adicional o que se alcance el extremo superior. O’Keeffe aporta el extremo inferior conocido. En grafos simples, restringir un mínimo local a movimientos constantes por siete grupos conserva minimalidad. La energía de plantilla es la energía restringida dividida por n al cuadrado. La conectividad de plantilla domina delta sobre n por promedios de grupos. Así obtenemos el corolario, con las normalizaciones equivalentes solo en el límite.

Fuentes:

- cota_minimos_locales_06934.md
- cota_flujos_06934.md
- global_optimum_certificate.json
- O’Keeffe v1, https://arxiv.org/html/2610.21271v1

## 8. El caso de cuatro fases exactas

Tiempo objetivo: 85 segundos.

Este es el argumento atribuido al Lema 11 de Lepsveridze y Zhang, adaptado a conductancias de plantilla. En cuatro fases exactas, dos pruebas del Hessiano vacían los pares opuestos. El equilibrio iguala las cuatro conductancias adyacentes a T. Rotamos A por menos t y B por t, dejando C y W fijas. La diferencia exacta de energía es T por seno de dos t menos dos senos de t. Para T positivo desciende con giros positivos arbitrariamente pequeños. Un mínimo local exige entonces T cero. Cada hoja queda aislada y el menor grado no supera un cuarto. Bajo la contradicción de grado límite al menos 0,6934, la separación h es por tanto positiva en una cola de la sucesión.

Fuentes:

- Lepsveridze y Zhang, arXiv:2608.20010v1, Lema 11, https://arxiv.org/html/2608.20010v1
- cota_minimos_locales_06934.md
- verify_quarter_turn_local_minima.py

## 9. La reducción a cinco parámetros

Tiempo objetivo: 80 segundos.

Con h positivo normalizamos por la máxima desviación angular y extraemos offsets de máximo uno. La identidad de equilibrio controla la suma adyacente del Hessiano. Dos pruebas de semidefinitud fuerzan opuestos de orden h al cuadrado y la traza sobre hojas cancela cada corte principal. Antes de dividir por el flujo, el grado alto excluye todos sus ceros. Los centros por flujo coinciden con W y quedan en cero. Alguna anchura principal tiene módulo al menos uno, de modo que z no se anula aunque otras dos anchuras sean cero. Completamos internos solo como relajación e invertimos su bloque completado, positivo por las masas. J_i es el producto de las dos masas brutas de la pareja i. Tras normalizar cada corte a uno, tres productos y dos covarianzas dan las desigualdades necesarias mostradas. Las auditorías detallan los límites sin derivadas.

Fuentes:

- cota_minimos_locales_06934.md
- cota_flujos_06934.md
- auditoria_paso_variacional.md
- auditoria_flujos_centros.md
- verify_covariance_reduction.py

## 10. Los flujos ligan masas vecinas

Tiempo objetivo: 65 segundos.

La mejora clave conserva una relación entre masas vecinas. En una hoja dividida, los dos flujos suman uno. Dividir cada flujo por su masa da tau. El equilibrio principal iguala flujo entrante y saliente, y la capacidad de cada hoja vecina acota ambos tau por su masa B. La identidad escrita es una suma de términos no negativos y da chi por la masa propia menor o igual que la masa vecina. Se obtienen seis restricciones lineales sobre las cuatro masas relativas. No se suponen mitades iguales. Propagarlas estrecha las cotas inferiores de masas utilizadas por los siguientes argumentos de escala.

Fuentes:

- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md
- mass_flow_lemma_checks.py

## 11. Grados y cortes comparten escala

Tiempo objetivo: 70 segundos.

Las cotas inferiores L de masas deben ser compatibles entre sí y con que cada masa sea a lo sumo uno menos u. Excluimos primero las que incumplen eso. En el caso restante, la función t por u menos t es creciente en el intervalo usado. Los promedios de grado de las cuatro hojas dan una cota superior para N al cuadrado, donde N es la suma de masas brutas. No igualamos promedio con mínimo. Un corte de flujo uno necesita suficiente capacidad total y da una cota inferior para la misma escala. Combinar ambas produce R al cuadrado mayor o igual que dos D. Las capacidades hacia W añaden otra restricción necesaria.

Fuentes:

- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md

## 12. La cobertura racional completa

Tiempo objetivo: 80 segundos.

El dominio de tres productos es compacto bajo la hipotética conectividad 0,6934. El certificado lo biseca de forma racional hasta justificar todas sus hojas. Algunas contradicen restricciones de masas o capacidades. Otras combinan las dos formas necesarias de estabilidad con un coeficiente racional y prueban que la matriz menos la identidad es definida positiva. Eso contradice que el vector z no nulo satisfaga ambas formas. La comparación usa un vector racional positivo. El otro método verifica los menores de Sylvester con coeficientes de Bernstein racionales en todo el rectángulo de covarianzas. Las cotas de raíces se calculan con raíces enteras y amplían el dominio. Ninguna hoja se acepta por un autovalor flotante.

Fuentes:

- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md
- profile_upper_certificate_06934-v1.json
- verify_profile_upper_mass_flow.py

## 13. Qué comprueba el certificado

Tiempo objetivo: 60 segundos.

El verificador reconstruye el cubo, las bisecciones y todas las hojas con Python estándar. No importa el constructor, sus predicados, NumPy ni un solucionador espectral. Los controles conservan testigos y rechazan seis alteraciones. La ampliación añade identidades simbólicas del descenso y auditorías de factores, flujos y centros. El control a 120 dígitos verifica ejemplos, mientras las desigualdades continuas dependen de la demostración escrita. El paquete ampliado pasó dieciséis órdenes: doce matemáticas, una de integridad y tres de historiales autorizados. Sus 106 archivos conservaron sus huellas en una copia aislada. La construcción y las verificaciones proceden del mismo agente de IA. Falta revisión matemática independiente.

Fuentes:

- expanded_team_package_validation.json
- profile_upper_certificate_06934-v1_verification.json
- variational_bridge_verification.json
- flow_centers_verification.json

## 14. Lo que la relajación aún permite

Tiempo objetivo: 60 segundos.

La cobertura no sugiere que baste subdividir indefinidamente las mismas cajas hasta alcanzar mu0. Construimos un punto racional que satisface estrictamente las dos formas de estabilidad y todas las condiciones proyectadas usadas, incluso a 0,6932. Esto demuestra una barrera de esa relajación concreta. El punto no contiene masas realizadas, matrices de transporte, fases ni un Hessiano de Kuramoto. No es una nueva cota inferior o un contraejemplo al óptimo de una clase mayor. Para acercar esta vía al valor conocido hacen falta restricciones adicionales. La posibilidad de otras geometrías o masas límite nulas tampoco se resuelve con nuestro teorema.

Fuentes:

- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md
- verify_mass_flow_relaxation.py
- mass_flow_relaxation_witness.json

## 15. Resultado y revisión pendiente

Tiempo objetivo: 45 segundos.

La cota vale para la clase indicada de mínimos locales, incluyendo degeneración. La construcción conocida y el certificado sitúan el supremo en el intervalo mostrado, de ancho menor que 0,000493. Quedan fuera otras geometrías y masas límite nulas. El siguiente paso del equipo es revisar la reducción y contrastar el interés bibliográfico antes de ensayar la defensa. Codex realizó deducciones, código y redacción. La reproducción informática no acredita una revisión independiente, ni se presenta aquí una mejora del umbral universal.

Fuentes:

- cota_minimos_locales_06934.md
- cota_flujos_06934.md
- auditoria_paso_variacional.md
- auditoria_flujos_centros.md
- revision_bibliografica.md
