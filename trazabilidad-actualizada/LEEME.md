# Adenda de mensajes visibles del 23/10/2026

Esta adenda acompaña a `paquete-revision-asintotica-actual-equipo-v3.zip`. Actualiza la trazabilidad de los dos chats autorizados sin modificar ese paquete, sus pruebas o sus medios. No es una entrega al evento ni acredita cumplimiento íntegro de sus bases.

## Qué contiene

| Chat | Carpeta | Corte UTC de turno completo | Mensajes |
| --- | --- | --- | ---: |
| Ganar el Investigathon | `trazabilidad/chat-visible-20261023-v1` | 23/10/2026 15:03:53.970 | 217: 8 humanos, 169 actualizaciones y 40 finales |
| Preparar proyecto de Investigathon | `trazabilidad/preparacion-visible-20261022-v1` | 18/10/2026 04:02:45.503 | 20: 4 humanos, 13 actualizaciones y 3 finales |

El chat principal conserva como prefijo exactamente los 159 mensajes de su corte anterior y añade 58. El otro chat no tuvo actividad nueva y sus cuatro archivos se conservan sin cambios. Son 237 mensajes en total. Cada carpeta tiene `mensajes.jsonl`, `transcripcion.md`, `cobertura.json` y `MANIFEST.json`.

El nuevo corte alcanza la preparación del paquete actual v3: incluye los mensajes visibles posteriores al corte anterior sobre la ampliación, las auditorías, los informes y los medios. No incluye este turno de preparación de la adenda ni conversaciones de otras personas o herramientas. No se presenta como historial bruto completo.

## Autorización y exclusiones

El usuario autorizó guardar e incluir en el paquete local los mensajes visibles de estos dos chats, conociendo que el baúl puede sincronizarse con Drive. Esa autorización se mantiene para esta actualización; no se amplía a otros chats ni contenidos.

Se incluyen solo textos conversacionales visibles completados y sus metadatos de ubicación. Las respuestas de formulario conservan pregunta y respuesta legibles. Se excluyen razonamiento, configuración, contexto automático y del proyecto, entradas, resultados e índices de herramientas, sesiones privadas y medios incrustados. No se copian registros brutos. Los archivos de fuentes y código son evidencia separada de las transcripciones.

## Comprobar una copia

Extraer en una carpeta temporal local fuera del baúl y de Drive, o comprobar directamente el ZIP. Python estándar, sin `-O`:

```text
python -B -S adenda_historial_visible.py --verify-archive RUTA_DE_LA_ADENDA
python -B -S verificar_historial_visible_v3.py --folder trazabilidad/chat-visible-20261023-v1
python -B -S verificar_historial_visible_v3.py --folder trazabilidad/preparacion-visible-20261022-v1
```

Los ocho controles sintéticos del filtro se ejecutan con:

```text
python -B -S test_historial_visible_v3.py --temp-parent RUTA_TEMPORAL_LOCAL
```

En la instalación original, `--local-sources` en el verificador de cada carpeta reconstruye exactamente el texto desde su prefijo local de solo lectura. Esa fuente privada no se redistribuye. Los manifiestos comprueban bytes, tamaños y miembros; no son firmas de autor ni revisión matemática.

## Relación con la entrega

La propuesta de Kuramoto, páginas 4 y 5, pide que el repositorio reúna informe, código y experimentos producidos, historiales de IA que contribuyeron, póster y presentación. Prioriza corrección y claridad, profundidad, reproducibilidad y originalidad, y evalúa la comprensión demostrada por el equipo. La autorización de exportación conserva aquí su límite de mensajes visibles; no se afirma que cubra cualquier exigencia adicional del jurado.

La consulta del cronograma oficial del 23/10 mantuvo el checkpoint del 26/10 de 15 a 17 h, simulacro de pósters del 29/10 de 18 a 20 h y final del 30/10 de 14 a 21 h, horario de Buenos Aires: [página oficial](https://somosyhat.com/investigathon). Se conserva Kuramoto como tema confirmado por el usuario, aunque la web describe otro problema en el track.

El enlace del repositorio de entrega y el formato externo de la charla están consultados, todavía sin respuesta al preparar esta adenda. El equipo confirmó el 22/10 que aún no había revisado la prueba; no se recibió una confirmación posterior. Siguen pendientes revisión matemática humana, contraste de novedad y ensayo. No se acreditan inscripción, envío, publicación o haber ganado a partir de estos archivos.

Codex (OpenAI) preparó la actualización, su filtro y las comprobaciones, sin subagentes. El recibo de la adenda registra las verificaciones efectivamente realizadas. El paquete v3 y las exportaciones anteriores permanecen intactos.
