# Cota asintótica para discutir en el checkpoint

Actualizado el 23/10/2026. El usuario eligió la **cota asintótica 0,6934** como eje de la defensa y confirmó el 22/10 que el equipo **todavía no revisó la prueba**. Esa selección no acredita revisión matemática, comprensión o ensayo. La [primera lectura](primera-lectura-cota-06934.md) parte del modelo y separa la reducción analítica del certificado. La última confirmación de ausencia de devolución fue el 19/10.

El [cronograma oficial](https://somosyhat.com/investigathon), consultado nuevamente el 22/10, mantiene el segundo checkpoint el **26/10, de 15 a 17 h**, en horario de Buenos Aires. Se conserva Kuramoto como tema confirmado por el usuario y los PDFs, pese a la descripción distinta del track en esa web.

## Resultado central

Para sucesiones de plantillas del Kuramoto homogéneo con siete clusters, equilibrio exacto y Hessiano finito positivo fuera de la rotación, suponer masas límite positivas y fases que convergen a los cuatro cuartos de vuelta con reparto **(2,2,2,1)**. Entonces la conectividad límite superior es **menor que 0,6934**.

Se permiten mitades desiguales, falta de reflexión, internos incompletos, densidades límite cero y distintas escalas de separación. No se cubren masas límite nulas, otros repartos o geometrías alejadas de esas cuatro fases. No es una cota superior universal para la conectividad crítica de Kuramoto.

La construcción de O'Keeffe aporta el extremo inferior conocido mu0 ≈ 0,69290770637. Para el supremo de valores límite de esta clase queda el intervalo **[mu0; 0,6934]**, de ancho menor que **0,000493**. No se demuestra que el supremo sea mu0.

[Prueba y alcance](cota_flujos_06934.md) · [Paquete reproducible](kit-cota-flujos-06934-v1.zip) · [Guía de reproducción](kit_cota_flujos_06934.md).

**Ampliación posterior al paquete del equipo:** la [nota de mínimos locales](cota_minimos_locales_06934.md) conserva 0,6934 sin exigir positividad estricta del Hessiano finito. Exige minimalidad local real, que no se infiere de semidefinitud. El caso de cuatro fases exactas se descarta por un descenso cúbico conocido; después funciona la misma reducción y cobertura. El [informe ampliado de cinco páginas](informe/output/pdf/informe-minimos-locales-v2.pdf), preparado para revisión, ya incluye esa ampliación, su atribución y las auditorías del paso variacional y de centros. La prueba y su correspondencia con el argumento anterior requieren revisión humana. El informe original de cuatro páginas, la charla, el póster y el ZIP congelados conservan la subclase estricta.

La revisión 6 de la charla editable, completada el 23/10, ya presenta mínimos locales y el lema atribuido, en quince diapositivas con [guion ampliado](exposicion/guion-15-minutos-minimos-locales-v2.md). Sus tiempos suman 900 segundos como objetivo, sin ensayo medido. Las tablas y el gráfico siguen editables. Las fuentes de charla dentro del ZIP v2 siguen congeladas en la revisión estricta anterior; la fuente nativa de esa revisión está conservada. El [póster ampliado del 23/10](exposicion/poster/output/pdf/poster-minimos-locales-v2.pdf) también presenta mínimos locales y el descenso atribuido, en una hoja A1. El póster estricto original y el ZIP v2 se conservaron sin cambios; el ZIP no contiene las nuevas versiones de exposición.

## Cómo se demuestra

1. El equilibrio exacto y la positividad del Hessiano fuerzan enlaces opuestos de orden O(h²) y cuatro cancelaciones principales, sin derivar los datos.
2. Completar internos solo como relajación permite tratar el caso incompleto. Se excluyen flujos cero por grado antes de usar centros ponderados; queda un vector variacional no nulo.
3. Tres productos de flujo por masa y dos covarianzas describen pruebas necesarias de estabilidad. Capacidades y grados confinan los tres productos a un cubo compacto.
4. La desigualdad chi_i M_i <= M_vecina conserva información entre masas. Al combinar cotas de grado y capacidades totales de cortes se estrecha el dominio.
5. Un árbol racional de **15.511 nodos y 7.756 hojas** cubre todo el cubo, incluidos sus bordes. Cada hoja contradice una capacidad o prueba una matriz definida positiva incompatible con las dos formas necesarias de estabilidad.

El verificador separado usa fracciones, raíces enteras y Bernstein racional, sin importar constructor, predicados, NumPy ni un solucionador espectral. La reducción analítica es parte de la prueba; un árbol por sí solo no prueba que modele Kuramoto correctamente.

## Evidencia disponible

El paquete de 35 archivos pasó cinco órdenes en una copia aislada fuera de W y Drive. Tres usan Python estándar; las dos simbólicas usan SymPy de la caché existente. Los archivos mantuvieron sus huellas después de regenerar resultados. No se probó una instalación nueva ni se reconstruyó el árbol en esa copia.

El [paquete anterior del equipo](paquete-revision-asintotica-equipo-v1.zip), de 78 miembros, conserva el informe original y los mensajes visibles autorizados. Pasaron ocho órdenes en una copia aislada. Se preserva esa versión y su [guía](revision_asintotica_equipo.md).

El [paquete ampliado v2](paquete-revision-asintotica-ampliada-equipo-v2.zip), de 107 miembros, añade el informe de cinco páginas, la ampliación, las dos auditorías y los datos necesarios para reproducir también el complemento finito y su traslado a grafos. Pasaron dieciséis órdenes en otra copia aislada, con 106 archivos de contenido sin cambios. La [guía ampliada](revision_asintotica_ampliada_equipo.md) distingue el informe nuevo de la charla y el póster estrictos y conserva los mismos cortes de los mensajes visibles. No es el cuaderno completo ni una entrega al evento.

Los controles rechazan seis alteraciones del certificado y conservan tres testigos finitos estrictos. Otros cuatro testigos anteriores conservan las 24 desigualdades nuevas; en todos se comprueba equilibrio exacto antes de estabilidad. Constructor y verificadores proceden del mismo agente y no constituyen revisión humana independiente.

Un [punto racional de la relajación](cota_flujos_por_masa.md) satisface sus desigualdades a 0,6932. No realiza transportes ni un equilibrio de Kuramoto y no mejora el récord. Demuestra que acercar esta vía a mu0 requiere restricciones adicionales; no basta subdividir más las mismas cajas.

## Qué conviene revisar con los mentores

- La extracción de una separación principal no nula cuando hay distintas escalas y la exclusión previa de flujos cero.
- La relajación de internos y las dos formas variacionales necesarias.
- La cadena que liga masas, grados y capacidades a la misma escala.
- La correspondencia entre la prueba analítica y las exclusiones del verificador.
- El interés y la novedad de la cota concreta frente al preprint y otros antecedentes.

El corolario para grafos usa promedios por grupos, sin exigir bloques regulares. Las normalizaciones delta/n, (delta+1)/n y delta/(n−1) comparten la cota solo al crecer el orden. No se igualan a orden finito.

## Resultados complementarios y materiales

La [separación finita entre patrones](obstruccion_patron_finito.md) y su [traslado existencial a grafos simples](separacion_grafos_simples.md) siguen disponibles: un único par opuesto permite superar la cota de toda la clase que lo prohíbe a las mismas masas y fases. La ventaja excede 1,99e−7. Los grafos del traslado tienen orden de 113 cifras y no se enumeran aristas; no se presentan como una mejora de mu0.

El [máximo global del modelo restringido](optimalidad_global.md) y la [obstrucción para un perfil principal especificado](patron_principal_limite.md) dan la cota más fuerte mu0 bajo hipótesis adicionales. No se extrapolan a toda la clase de siete clusters.

El informe original tiene cuatro páginas y desarrolla primero el resultado asintótico. El [guion breve del checkpoint](guion-checkpoint-equipo.md) conserva la hipótesis estricta, con tres minutos como objetivo. La charla editable actual tiene quince diapositivas, con [guion ampliado](exposicion/guion-15-minutos-minimos-locales-v2.md) de 900 segundos objetivos y fuentes en notas, sin ensayo medido. Su contenido y maquetación se revisaron en el editor. El [póster A1 ampliado](exposicion/poster/output/pdf/poster-minimos-locales-v2.pdf) presenta mínimos locales posiblemente degenerados, la desigualdad de masas vecinas, el certificado y sus límites; usa el nombre **Los Kuramotardos**, indicado por el usuario el 22/10. Se revisaron su página completa, tres columnas y pie, sin recortes ni superposiciones observados. El [póster estricto](exposicion/poster/output/pdf/poster-kuramoto.pdf), las versiones anteriores y el PPTX v12 se conservan. Los paquetes previos siguen congelados. La revisión visual y de consistencia no es revisión matemática humana.

**Uso de IA:** Codex (OpenAI) realizó consulta, deducción, código, cálculos, controles y redacción. No hubo subagentes, revisión humana independiente, ensayo medido, comunicaciones, publicación ni entrega al evento. La selección del eje ya está confirmada; revisión, novedad y defensa siguen pendientes.
