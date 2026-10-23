# Guion propuesto de 15 minutos

Cota asintótica 0,6934 para siete clusters próximos a cuatro fases. Eje elegido por el usuario el 22/10/2026. Tiempos objetivos que suman 900 segundos, sin ensayo medido. No acreditan revisión del equipo.

## 1. Kuramoto: una cota asintótica

Tiempo objetivo: 30 segundos.

Presentamos una cota superior para una clase asintótica de siete clusters cerca de cuatro fases. La conectividad límite superior es menor que 0,6934 bajo las hipótesis que precisaremos. El resultado no determina el umbral general. La construcción de referencia y mu0 se atribuyen a O’Keeffe. El equipo eligió este resultado como foco de defensa. La elección no acredita revisión matemática, novedad ni un ensayo medido. La portada es una ilustración conceptual y no representa una red certificada.

Fuentes:
- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md
- exposicion/visual_asset.md

## 2. El modelo de Kuramoto

Tiempo objetivo: 55 segundos.

Comenzamos con osciladores idénticos en un grafo simple no dirigido. Al quitar la frecuencia común, su dinámica es el flujo negativo de esta energía. Cada arista aparece una vez. En sincronía las fases son iguales, pero pueden existir otros mínimos locales. La pregunta es cuánta conectividad permite esos estados. La propuesta usa el grado mínimo más uno dividido por n. Otras fuentes usan delta dividido por n menos uno. A orden finito convertimos las expresiones. En sucesiones de orden creciente, sus diferencias con delta sobre n se anulan. No se sustituye grado mínimo por grado promedio.

Fuentes:
- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- Bullo, Lectures on Network Systems, ed. 1.6, capítulo 17.1–17.2.
- Propuesta local: modelo y normalización.

## 3. Equilibrio y estabilidad

Tiempo objetivo: 55 segundos.

El residuo debe anularse antes de clasificar estabilidad. En un equilibrio, el Hessiano es un Laplaciano con pesos que incluyen el coseno de diferencias de fase. La rotación global conserva la energía y da un cero inevitable. Un autovalor transversal negativo implica inestabilidad. Positividad estricta en el complemento de esa rotación da un mínimo estricto módulo rotación. Si quedan ceros adicionales, la semidefinitud sola no decide estabilidad. No exigimos un margen uniforme: en las sucesiones que estudiaremos, el margen puede tender a cero. Por eso los límites degenerados necesitan un tratamiento distinto de los datos finitos.

Fuentes:
- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- Bullo, capítulo 17, Lema 17.2.

## 4. Cuatro fases y siete clusters

Tiempo objetivo: 50 segundos.

Las cuatro hojas tienen fases separadas por un cuarto de vuelta. Tres hojas se dividen en dos clusters y la última permanece entera. Así aparecen siete masas positivas. El dibujo muestra las cuatro fases límite y no las proporciones de masas. Los estados finitos se acercan a ellas, con separaciones que pueden tener escalas distintas. El estado exactamente C4 tiene conectividad tres cuartos, pero es degenerado. No satisface nuestra hipótesis de Hessiano finito estricto. Por tanto, no constituye una excepción a la cota que presentaremos. La degeneración explica por qué normalizamos la separación antes de tomar límites.

Fuentes:
- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md

## 5. La construcción conocida

Tiempo objetivo: 60 segundos.

La constante inferior procede del preprint de O’Keeffe, no de esta investigación. Su familia de estados estrictos se aproxima a mu0 al reducir el desdoblamiento. La fuente analiza un patrón simétrico y prueba la existencia de los estados. En IV.3 aclara que las observaciones de optimalidad de su modelo no son una prueba del umbral general. Nuestra pregunta es distinta: acotar todos los valores límite dentro de una clase de siete clusters que se acercan a cuatro fases, liberando asimetrías y densidades principales. No afirmamos aumentar la constante inferior ni resolver el problema para todos los grafos.

Fuentes:
- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- optimalidad_global.md

## 6. La clase asintótica

Tiempo objetivo: 65 segundos.

Pasamos explícitamente del grafo a plantillas ponderadas. Las masas suman uno y las densidades son simétricas y están entre cero y uno. La conectividad de plantilla es el mínimo de sus grados ponderados. En cada elemento finito exigimos equilibrio exacto y Hessiano positivo fuera de la rotación. Las siete masas convergen a límites positivos y las fases a j por pi medios, con j igual al vector mostrado. Permitimos mitades desiguales, internos incompletos, densidades límite cero y distintas escalas. No cubrimos masas límite nulas u otras geometrías. En grafos, el corolario requiere siete grupos de fase y orden creciente.

Fuentes:
- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md

## 7. La cota de esta clase

Tiempo objetivo: 60 segundos.

Bajo las hipótesis anteriores, el límite superior de conectividades de cada sucesión es estrictamente menor que 3467 sobre 5000. Al hablar del supremo entre todas las sucesiones dejamos el extremo superior cerrado: no afirmamos un margen uniforme adicional ni que se alcance ese extremo. La construcción conocida aporta el extremo inferior mu0. El ancho es menor que 0,000493, comprobado con el intervalo algebraico de referencia. Para grafos de orden creciente, la agregación por promedios da delta sobre n menor o igual que la conectividad de plantilla. Las otras normalizaciones comparten esta cota solo en el límite.

Fuentes:
- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md
- global_optimum_certificate.json

## 8. El equilibrio controla los opuestos

Tiempo objetivo: 75 segundos.

Fijamos W y medimos h como la mayor desviación angular respecto de las fases límite. La hipótesis estricta descarta h exactamente cero. Tomamos una subsucesión de los desplazamientos reescalados acotados. Multiplicar el equilibrio por esos desplazamientos produce la identidad exacta de la pantalla. Los restos trigonométricos están acotados y dan S_h de orden h al cuadrado. Al probar positividad con las rotaciones de hojas uno, cero, menos uno, cero y uno, dos, uno, cero, todos los enlaces opuestos quedan del mismo orden. La traza del Hessiano restringido a hojas controla cada corte. No se derivan los datos ni se impone una tasa de convergencia. Aquí a_ij=x_i x_j P_ij, d_ij es la diferencia de offsets reescalados y sigma_ij es el seno de la diferencia de fases base. S_h es la suma adyacente a_ij cos(theta_i−theta_j).

Fuentes:
- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md

## 9. Tres productos y dos covarianzas

Tiempo objetivo: 70 segundos.

Para una contradicción de grado al menos u, con u mayor que dos tercios, los casos de flujo cero se excluyen primero por grado. Solo entonces usamos centros ponderados por flujo para demostrar que el vector variacional z no es nulo. Completar internos se usa como relajación de grado y de pruebas necesarias, sin conservar necesariamente un equilibrio finito. Normalizamos el flujo común a uno. Cada pareja aporta el producto chi y cada transporte entre parejas aporta una covarianza normalizada. Dos formas cuadráticas necesarias de estabilidad quedan descritas por a, b, c, kappa y lambda. Las capacidades de transportes y los grados confinan los tres productos a un cubo compacto. Kappa es el determinante del transporte A–B dividido por la raíz de J_A J_B; lambda se define análogamente para B–C. Las dos desigualdades de la pantalla son las pruebas variacionales necesarias que luego combinamos.

Fuentes:
- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md
- verify_covariance_reduction.py

## 10. Los flujos ligan masas vecinas

Tiempo objetivo: 60 segundos.

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

El verificador separado reconstruye el cubo, cada bisección y cada hoja. Usa solo Python estándar y no importa el constructor, sus predicados, NumPy ni un solucionador espectral. Los controles rechazan cambios de dominio, ramas o justificaciones. Conservan también testigos finitos válidos y comprueban equilibrio antes de estabilidad. Los ejemplos controlan errores, pero no sustituyen el argumento continuo. Las identidades simbólicas y el intervalo de mu0 se verifican aparte. El paquete pasó cinco órdenes en una copia aislada, manteniendo las huellas. La separación de programas no equivale a revisión humana independiente: ambos proceden de Codex.

Fuentes:
- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md
- profile_upper_mass_flow_checks.json
- mass_flow_lemma_checks.json
- profile_upper_mass_flow_kit_validation.json

## 14. Lo que la relajación aún permite

Tiempo objetivo: 65 segundos.

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

El resultado central es una cota superior asintótica para la clase indicada y un certificado exacto que cualquiera puede reproducir. La construcción inferior conocida mantiene su atribución. La principal revisión pendiente es comprobar la cadena analítica que conecta equilibrios y estabilidad con el dominio certificado, además de contrastar la novedad. No se ha determinado la conectividad crítica general. Codex realizó deducciones, búsquedas, código y redacción, incluidos constructor y verificadores. No hubo subagentes ni revisión humana independiente acreditada. Los textos visibles de IA conservan cortes declarados y no son historiales completos. Estos quince minutos son un objetivo de guion, todavía sin ensayo medido.

Fuentes:
- cota_flujos_06934.md
- cota_perfil_general.md
- cota_capacidades_agregadas.md
- cota_flujos_por_masa.md
- O'Keeffe, Beyond 11/16, arXiv:2610.21271v1, https://arxiv.org/html/2610.21271v1
- Bitácora.md
- trazabilidad/README.md

