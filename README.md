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

Este repositorio está preparado localmente, sin remoto ni publicación. El usuario
confirmó el 23/10 que el repositorio de entrega todavía no estaba creado. La
autorización existente para conservar los mensajes cubre el paquete local y su
posible sincronización con Drive. Subirlos a GitHub requiere confirmación aparte.
No se declara inscripción, envío, revisión del jurado ni haber ganado.
