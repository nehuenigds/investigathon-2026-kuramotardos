# Los Kuramotardos: revisión de la cota 0,6934, versión ampliada

22/10/2026. Paquete local de revisión preparado con Codex. El usuario eligió la cota asintótica como eje y confirmó que el equipo aún no revisó la prueba. Esta versión incorpora el informe ampliado y los controles posteriores; no acredita revisión humana, comprensión, ensayo, novedad o entrega al evento.

## Lectura del resultado

1. Empezar por Bullo 17.1 y 17.2, siguiendo `primera-lectura-cota-06934.md`. Esa guía conserva la exposición de la versión estricta original.
2. Leer `informe/output/pdf/informe-minimos-locales-v2.pdf`: cinco páginas con el enunciado ampliado, su caso degenerado, el corolario para grafos y el complemento finito.
3. Revisar `cota_minimos_locales_06934.md`, `cota_flujos_06934.md`, `cota_perfil_general.md` y `cota_capacidades_agregadas.md` para la prueba completa.
4. Revisar `auditoria_paso_variacional.md` y `auditoria_flujos_centros.md` para el tratamiento de internos singulares, distintas escalas, flujos cero y vector no nulo.

El enunciado ampliado exige **mínimos locales reales** de la energía de plantilla, siete masas límite positivas y fases que convergen a los cuatro cuartos de vuelta con reparto `(2,2,2,1)`. Bajo esas hipótesis, `limsup mu < 3467/5000`. Equilibrio exacto y Hessiano semidefinido solos no bastan. El descenso cúbico se atribuye al Lema 11 de Lepsveridze–Zhang; la construcción inferior y mu0 ≈ 0,69290770637 se atribuyen a O'Keeffe v1.

El supremo de valores límite queda en [mu0; 0,6934], de ancho menor que 0,000493. No se determina el umbral universal, no se mejora el récord inferior y no se incluyen masas límite nulas u otras geometrías. Los programas comprueban identidades y certificados; la reducción continua escrita sigue requiriendo revisión.

## Verificar integridad y reproducir

Extraer una copia fuera del baúl y de Drive, en una subcarpeta propia de la carpeta temporal local del sistema. Ejecutar desde esa copia, con Python 3.11 o posterior, sin `-O`. `-B` evita cachés junto a las fuentes. Antes y después de las comprobaciones:

```text
python -B -S verify_review_package.py --folder .
```

También se puede comprobar el ZIP sin extraerlo, con `--archive RUTA_DEL_ZIP`. El manifiesto verifica tamaños, huellas y miembros; no es una firma de autor ni una revisión matemática.

La cobertura 0,6934 y los controles racionales usan Python estándar:

```text
python -B -S verify_profile_upper_mass_flow.py
python -B -S profile_upper_mass_flow_checks.py
python -B -S mass_flow_lemma_checks.py
```

La cobertura tiene 15.511 nodos y 7.756 hojas, incluidos los bordes. Los controles rechazan seis alteraciones y conservan tres testigos estrictos; el lema de masas conserva otros cuatro y sus 24 desigualdades. No hace falta reconstruir el árbol o relanzar búsquedas.

Estas cinco órdenes necesitan SymPy y mpmath, con versiones en `requirements-verificacion.txt`:

```text
python -B verify_covariance_reduction.py
python -B verify_global_optimum.py
python -B verify_quarter_turn_local_minima.py
python -B verify_variational_bridge.py
python -B verify_flow_centers.py
```

La segunda reproduce el intervalo algebraico de referencia de mu0. Las tres últimas comprueban el caso degenerado, los factores del paso variacional y la conservación de la dirección. El control variacional distingue las identidades exactas de once evaluaciones a 120 dígitos. Los controles sintéticos de flujos son condiciones parciales; no se anuncian como equilibrios finitos estables. Ninguna de estas órdenes verifica por máquina la prueba continua completa.

En esta instalación se usó la caché externa existente, localizada por `bootstrap.py`; se puede indicar otra con `CODEX_W_KURAMOTO_DEPS`. En otra máquina, instalar las dependencias en un entorno local fuera del baúl. No se redistribuyen bibliotecas ni se acredita una instalación nueva.

## Complemento finito y traslado a grafos

Se incluyen los datos y verificadores necesarios para las órdenes del informe, además de las pruebas `obstruccion_patron_finito.md` y `separacion_grafos_simples.md`. Se conservan los cuatro juegos de datos de geometría fija que usa la suite, incluido el enlace opuesto único.

```text
python -B -S fixed_geometry_checks.py
python -B -S verify_pattern_obstruction.py
python -B -S verify_simple_graph_separation.py
python -B -S simple_graph_separation_checks.py
```

Todo este grupo usa Python estándar. La primera orden pasa nueve controles; la segunda compara las clases a idénticas masas y fases. La ventaja finita supera 1,99e-7 y no mejora mu0. Las dos últimas verifican el traslado existencial y sus controles de agregación, completación y cinco alteraciones. Los grafos de orden de 113 cifras no tienen aristas ni conjuntos de desplazamientos enumerados. Las tres normalizaciones de conectividad se distinguen a orden finito.

## Materiales de exposición y versiones

El informe ampliado es el PDF de cinco páginas indicado arriba, con fuente `informe/main-minimos-locales-v2.tex`, procedimiento `informe/build_local_minima_report.py` y recibo. La fuente y el PDF originales de cuatro páginas siguen incluidos para interpretar las versiones anteriores.

La charla viva `artifact_HY7aNlQL_1n7Hw_dMGGdRWEk0oBJmy84`, estado 4, y el póster A1 conservan la hipótesis finita estricta original. Sus fuentes, guiones, portada y validaciones están incluidos. No se exportó una nueva charla a PPTX o PDF. El programa de población necesita el editor de presentaciones y su runtime; no es una reconstrucción autónoma fuera de ese entorno. El guion de quince diapositivas suma 900 segundos como objetivo, sin ensayo medido. La nueva ampliación requiere revisión antes de trasladarla a la defensa.

Los procedimientos de informe y póster necesitan XeLaTeX y los paquetes de los fuentes; el póster usa Arial y PGFPlots. Los procedimientos Python de compilación usan además pypdf y Poppler. Reciben una carpeta temporal y no reemplazan automáticamente un PDF revisado. Las rutas de herramientas requieren adaptación en otra máquina. La validación de este paquete no recompila medios, no prueba el editor de presentaciones ni instala dependencias.

`kit-cota-flujos-06934-v1.zip` conserva el paquete matemático original intacto; sus fuentes y datos también están sueltos. Los paquetes anteriores no se reemplazan. Esta selección cubre las órdenes matemáticas del informe ampliado; no es el cuaderno completo ni incluye todos los materiales históricos enlazados desde sus notas. No se redistribuyen los PDFs bibliográficos. Los antecedentes se citan mediante enlaces en las pruebas.

## Mensajes visibles autorizados

Se conservan exactamente las dos exportaciones ya autorizadas: 159 mensajes en `trazabilidad/chat-visible-20261022-v1` y 20 en `trazabilidad/preparacion-visible-20261022-v1`. Cada carpeta tiene `mensajes.jsonl`, `transcripcion.md`, `cobertura.json` y `MANIFEST.json`.

Los cortes de turno completo son el 22/10 a las 22:43:46.836 UTC y el 18/10 a las 04:02:45.503 UTC, respectivamente. Incluyen solo mensajes conversacionales visibles; los formularios conservan sus preguntas y respuestas legibles. Excluyen razonamiento, configuración, contexto automático, herramientas y registros brutos. Estas auditorías posteriores, el nuevo informe y este empaquetado están después del corte del chat principal. No se presume cobertura de otros chats ni historiales completos.

```text
python -B -S verificar_historial_visible_v3.py --folder trazabilidad/chat-visible-20261022-v1
python -B -S verificar_historial_visible_v3.py --folder trazabilidad/preparacion-visible-20261022-v1
python -B -S test_historial_visible_v3.py --temp-parent RUTA_TEMPORAL_LOCAL
```

La última orden pasa ocho controles del filtro con mensajes sintéticos y necesita una carpeta temporal existente fuera de W y Drive. No consulta sesiones privadas. La copia e inclusión de estos mensajes fue autorizada expresamente por el usuario considerando la posible sincronización del baúl con Drive; no se amplió el corte de ninguna exportación.

## Evidencia y revisión pendiente

El recibo externo del constructor registra la copia aislada, las dieciséis órdenes, las huellas del contenido antes y después y los paquetes anteriores preservados. La primera orden de integridad, las doce matemáticas y las tres de historiales suman dieciséis. La bitácora incluida tiene corte anterior a este empaquetado; la comprobación posterior se registra fuera del ZIP y no se añade retrospectivamente a su copia.

El equipo debe revisar el enlace entre mínimos locales y dominio certificado, la exclusión de casos degenerados, las escalas, los grados y las capacidades, además del interés bibliográfico. Una reproducción informática correcta no sustituye esa revisión ni acredita novedad.

**Uso de IA:** Codex (OpenAI) realizó deducciones, código, controles, consulta de fuentes, redacción, medios y empaquetado. La portada conserva la atribución a image_gen. Constructor y verificadores provienen del mismo agente. No hubo subagentes, revisión matemática humana independiente acreditada, ensayo medido, comunicaciones a terceros, publicación o entrega al evento. No se verificó haber ganado.
