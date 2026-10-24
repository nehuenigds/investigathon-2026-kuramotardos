# Los Kuramotardos: Kuramoto y conectividad

Borrador local para revisión del equipo. El foco elegido es la cota asintótica
0,6934 para mínimos locales de siete clusters próximos a cuatro fases, con
masas límite positivas y reparto (2,2,2,1). La revisión matemática humana y la
comprobación de novedad siguen pendientes. No determina el umbral universal.

## Leer y revisar

- [Informe ampliado de cinco páginas](materiales/informe/output/pdf/informe-minimos-locales-v2.pdf).
- [Póster ampliado A1](materiales/exposicion/poster/output/pdf/poster-minimos-locales-v2.pdf).
- [Guion de quince minutos](materiales/exposicion/guion-15-minutos-minimos-locales-v2.md): duración objetivo, sin ensayo medido.
- [Ruta de lectura y prueba completa](materiales/revision_asintotica_actual_equipo.md), empezando por Bullo 17.
- [Notas para la defensa](materiales/exposicion/notas_defensa.md).
- [Mensajes visibles actualizados y su alcance](trazabilidad-actualizada/LEEME.md).

La charla editable actual es la revisión 6 del artefacto
`artifact_HY7aNlQL_1n7Hw_dMGGdRWEk0oBJmy84` en el chat. Su fuente nativa completa
está conservada en `materiales/exposicion/charla-minimos-locales-estado6.zip`.
Necesita el editor de presentaciones; no es un PPTX ni un PDF. El formato externo
sigue consultado. No se acredita funcionamiento en PowerPoint.

## Comprobar integridad

Con Python estándar, desde esta carpeta y sin `-O`:

```text
python -B -S verificar_entrega.py
```

Ese procedimiento comprueba las huellas de esta selección y los manifiestos de
ambas carpetas. Para repetir las matemáticas, seguir la guía de `materiales` en
una copia de trabajo fuera del baúl y de Drive. Algunas órdenes necesitan SymPy
y mpmath; no se incluyen bibliotecas. La reproducción previa de doce órdenes
matemáticas y sus límites están registrados en los recibos conservados. Preparar
este repositorio no constituye una nueva ejecución de esas doce órdenes.

GitHub ejecuta esta misma comprobación automáticamente en cada subida y
solicitud de cambio; también puede iniciarse desde la pestaña Actions. El control
se llama «Integridad de la entrega». Tras comprobar archivos y manifiestos,
reproduce el árbol racional de 0,6934, sus seis controles de corrupción, los tres
testigos finitos conservados y las 24 desigualdades del lema de flujos. Esas tres
órdenes usan Python estándar y escriben sus salidas en una copia temporal.
No ejecuta las otras nueve órdenes matemáticas ni acredita por sí solo la
reducción analítica, revisión humana, novedad o entrega al jurado. La configuración
conserva los bytes de los archivos entre sistemas.

Las carpetas preservan los materiales congelados y sus manifiestos. Si se editan,
la comprobación detectará esas diferencias hasta actualizar la selección. Los
temporales, vistas, cachés y auxiliares deben quedar fuera del baúl y de Drive;
añadirlos a `.gitignore` no evita su sincronización.

## Trazabilidad y estado de entrega

La adenda contiene 217 mensajes visibles del chat principal hasta el 23/10/2026
a las 15:03:53.970 UTC y 20 de preparación hasta el 18/10 a las 04:02:45.503 UTC.
El paquete de materiales conserva el corte principal anterior de 159 mensajes
como versión histórica. No deben sumarse ambos cortes como mensajes distintos:
el total actualizado es 237. No se cubren los turnos posteriores u otros chats.
Se excluyen razonamiento, configuración, contexto automático y herramientas.

Codex (OpenAI) produjo deducciones, código, controles y medios; el informe
detalla ese uso. Constructor y verificadores proceden del mismo agente. El equipo
confirmó el 22/10 que aún no había revisado la prueba; no se recibió confirmación
posterior. La comprensión y el ensayo siguen pendientes.

Repositorio privado creado y copia subida el 23/10/2026:
[nehuenigds/investigathon-2026-kuramotardos](https://github.com/nehuenigds/investigathon-2026-kuramotardos).
El usuario autorizó expresamente este destino privado y la transferencia de los
materiales preparados, incluidos los mensajes visibles seleccionados. El corte de
las transcripciones y sus exclusiones permanecen sin cambios. No se invitó a otras
personas ni se hizo público el contenido. La subida del repositorio no acredita
inscripción, envío al jurado, revisión matemática, ensayo ni haber ganado.
