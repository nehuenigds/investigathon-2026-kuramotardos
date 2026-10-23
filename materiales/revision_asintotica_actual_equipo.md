# Los Kuramotardos: materiales actuales para revisar

23/10/2026. Esta selección reúne el informe ampliado, la fuente de la charla actual y el póster ampliado, junto con las pruebas, los datos y los mensajes visibles ya autorizados. Es un paquete local para revisión del equipo. No acredita revisión humana de la prueba, novedad, ensayo ni entrega al evento.

## Por dónde empezar

1. Seguir la ruta de Bullo 17.1 y 17.2 de `primera-lectura-cota-06934.md`; esa introducción conserva el caso estricto original.
2. Leer `informe/output/pdf/informe-minimos-locales-v2.pdf`, de cinco páginas. El enunciado exige mínimos locales reales, posiblemente degenerados, siete masas límite positivas y las fases límite con reparto `(2,2,2,1)`. Equilibrio y semidefinitud solos no bastan.
3. Contrastar la reducción con `cota_minimos_locales_06934.md`, `cota_flujos_06934.md`, `cota_perfil_general.md`, `cota_capacidades_agregadas.md` y las dos auditorías de flujos y del paso variacional.
4. Revisar el póster de una hoja A1: `exposicion/poster/output/pdf/poster-minimos-locales-v2.pdf`. Expone las mismas hipótesis y distingue la prueba escrita de los controles informáticos.
5. Preparar la explicación con `exposicion/guion-15-minutos-minimos-locales-v2.md` y `exposicion/notas_defensa.md`. Los 900 segundos son un objetivo sin ensayo medido; la cantidad de expositores sigue pendiente y no se asignaron roles.

El foco 0,6934 es el elegido por el usuario. La cota es para esa clase asintótica, no para todos los grafos de Kuramoto. La construcción inferior conocida corresponde a O'Keeffe v1 y el descenso cúbico para cuatro fases exactas adapta el Lema 11 de Lepsveridze–Zhang. El intervalo del supremo de la clase queda en [mu0; 0,6934]; no se prueba que alcance su extremo superior ni que coincida con mu0. El punto 0,6932 pertenece solo a una relajación y no mejora el récord inferior.

## Charla actual y formatos

La charla editable de este chat es `artifact_HY7aNlQL_1n7Hw_dMGGdRWEk0oBJmy84`, revisión 6, con quince diapositivas. Su contenido está en `exposicion/charla-minimos-locales-v2.json`; `populate_local_minima_deck.mjs` conserva las operaciones de creación o actualización y `validate_local_minima_talk.mjs` compara el documento con sus fuentes. Estas operaciones requieren el editor de presentaciones y su entorno de ejecución.

`exposicion/charla-minimos-locales-estado6.zip` conserva un único archivo `charla-minimos-locales-estado6.json`: la fuente nativa completa de la revisión actual, con sus objetos, imágenes, tablas, gráfico y notas. No contiene mensajes del chat o registros de herramientas. Su compresión se comprobó byte a byte. Es una fuente del editor de presentaciones; **no es un PPTX ni un PDF y no se abre directamente en PowerPoint**.

La preferencia de formato para usar la charla fuera del chat quedó consultada al usuario, todavía sin respuesta al congelar esta selección. No se exportó una nueva presentación a PowerPoint o PDF. La revisión visual realizada corresponde al editor del chat; no acredita funcionamiento en otras aplicaciones.

La revisión estricta anterior queda representada por `charla-asintotica.json`, su guion y procedimiento originales, y la fuente nativa completa `charla-asintotica-estado4.zip`. Las cuatro tablas están en las diapositivas 3, 6, 10 y 12 y el gráfico nativo de fases en la 4. Ambas fuentes nativas son contenido necesario para conservar y comparar las revisiones; las capturas y las copias de comprobación no se incluyen.

## Integridad y alcance de la reproducción

Extraer una copia fuera del baúl y de Drive, en una subcarpeta propia del temporal local del sistema. No ejecutar con `-O`. Antes y después de usar o reproducir los materiales:

```text
python -B -S verify_review_package.py --folder .
```

También se puede comprobar el ZIP sin extraerlo con `--archive RUTA_DEL_ZIP`. La selección es la revisión 3; el manifiesto conserva la versión 2 de su esquema, compatible con ese verificador. El manifiesto comprueba miembros, tamaños y huellas. No es una firma de autor ni una revisión matemática.

`revision_asintotica_ampliada_equipo.md` conserva las doce órdenes matemáticas y las instrucciones de dependencias de la selección anterior. Se pueden ejecutar desde esta copia. La cobertura y los controles racionales usan Python estándar; cinco órdenes científicas necesitan SymPy y mpmath, con versiones en `requirements-verificacion.txt`. Las bibliotecas se instalan fuera del baúl y no se redistribuyen aquí. El complemento finito y el traslado existencial a grafos conservan sus datos y verificadores.

El paquete v2 superó dieciséis órdenes en una copia aislada: integridad, doce matemáticas y tres de historiales. Su recibo `expanded_team_package_validation.json` se incluye como evidencia de esa ejecución anterior. Esta revisión comprueba que todos los archivos matemáticos reproducidos conservan exactamente los mismos bytes del v2; las diferencias del contenido anterior se limitan a checkpoint, notas de defensa y la bitácora posterior. **No se vuelven a ejecutar las doce órdenes ni se presenta su reproducción previa como una nueva ejecución.** Tampoco se reconstruye el árbol, se relanzan búsquedas o se recompilan medios durante este empaquetado.

El constructor `build_current_team_package.py` comprueba fuentes, las dos fuentes nativas, los PDF y sus recibos, forma el manifiesto y verifica una copia aislada. Su recibo externo `current_team_package_validation.json` registra lo que efectivamente se comprobó después. La bitácora incluida termina antes de esa comprobación y no se reescribe retrospectivamente. El constructor depende de la selección v2 conservada para comparar bytes y no puede reconstruir por sí solo ese archivo desde esta selección extraída.

## Versiones preservadas

El póster ampliado usa `exposicion/poster/main-minimos-locales-v2.tex` y su recibo correspondiente. La fuente estricta original, su PDF `poster-kuramoto.pdf` y su recibo siguen incluidos. El informe original de cuatro páginas también se conserva. Los documentos anteriores se interpretan con su hipótesis estricta y su fecha, aunque mencionen entonces una charla o un póster como actuales.

Los procedimientos de compilación necesitan XeLaTeX, Arial, PGFPlots, pypdf y Poppler y reciben una carpeta temporal para los auxiliares. No reemplazan automáticamente un PDF revisado. Los guiones de exposición son propuestas sin ensayo medido. Esta selección no incluye el cuaderno completo ni todos los recursos históricos enlazados desde sus notas.

## Mensajes visibles autorizados

Se incluyen las mismas dos exportaciones de 159 y 20 mensajes, en `trazabilidad/chat-visible-20261022-v1` y `trazabilidad/preparacion-visible-20261022-v1`. Sus cortes siguen siendo el 22/10 a las 22:43:46.836 UTC y el 18/10 a las 04:02:45.503 UTC. No incluyen estas continuaciones posteriores. Cada carpeta conserva `mensajes.jsonl`, `transcripcion.md`, `cobertura.json` y `MANIFEST.json`.

El usuario autorizó copiar e incluir únicamente mensajes conversacionales visibles, considerando que el baúl puede sincronizarse con Drive. No se amplían chats o cortes y no se incluyen razonamiento, configuración, contexto automático, herramientas o sesiones privadas. Las fuentes nativas de presentación son documentos editables, no registros de conversación. Los programas de integridad y los ocho controles sintéticos del filtro siguen disponibles según la guía v2.

## Revisión pendiente y uso de IA

Antes de usar el resultado como aporte propio, el equipo debe revisar la reducción continua, sus hipótesis, los casos degenerados y el interés bibliográfico. Los verificadores no comprueban por máquina toda la demostración escrita. El usuario confirmó el 22/10 que el equipo todavía no había revisado la prueba; no se recibió una confirmación posterior de revisión.

Codex (OpenAI) produjo derivaciones, código, comprobaciones, texto, medios y esta selección, sin subagentes. Constructor y verificadores proceden del mismo agente. La portada conserva la atribución a image_gen. No se acredita revisión matemática independiente, ensayo medido, publicación, comunicaciones a terceros, entrega al evento ni haber ganado.
