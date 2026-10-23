# Guion de tres minutos para el checkpoint

Borrador para el equipo, cuya formación confirmó el usuario el 18/10/2026. Los tiempos son objetivos, no un ensayo realizado. Usar después de revisar el enunciado y poder explicar las desigualdades. No se presupone comprensión ni aprobación del resultado por parte del equipo.

## 0:00–0:35 — La pregunta

«Partimos de la construcción reciente de O'Keeffe para Kuramoto homogéneo. Con asistencia de IA obtuvimos una separación certificada entre patrones a fases fijas, que también se traslada a grafos simples, y una optimalidad límite restringida como complemento. No mejoramos la constante general conocida. Queremos revisar corrección, antecedentes e interés antes de elegir el eje de la entrega.»

## 0:35–1:30 — El resultado finito

«Fijamos exactamente las masas y los puntos del círculo de una plantilla de siete clusters. Si obligamos a que todos los enlaces entre hojas opuestas estén vacíos, incluso optimizando libremente los adyacentes, la conectividad es menor que 0,68877337417. Esa es una cota superior certificada, no el mejor punto que devolvió una búsqueda.

»Con las mismas masas y fases encontramos un equilibrio estrictamente estable que supera 0,68877357363. Mantiene completos los enlaces internos y solo agrega un enlace opuesto de densidad aproximada 0,000001585. Se reajustan también los adyacentes. Así queda una separación estricta mayor que 0,000000199 entre el testigo y toda la primera clase.»

## 1:30–2:35 — Certificado y grafos simples

«Comprobamos primero equilibrio exacto y después fuerzas internas y positividad fuera de la rotación. La cota superior usa multiplicadores racionales y dualidad débil; cubre todas las densidades adyacentes y se verifica con Python estándar.

»La separación también vale en grafos simples del mismo orden: se aplica el lema de realización citado y se completan los grupos de fase igual. La cota para la clase contraria se obtiene promediando residuos y restringiendo el Hessiano, sin exigir bloques regulares. El orden tiene 113 cifras; es existencia, no una lista de aristas. Un enlace de plantilla representa muchas aristas entre dos clusters.»

## 2:35–3:00 — Lo que pedimos revisar

«El diseño de pesos para imponer fases y la dualidad ya tienen antecedentes. No reivindicamos esas ideas generales. Quisiéramos revisar la separación concreta: si el enunciado y el certificado son correctos, qué antecedentes conviene contrastar y si vale la pena centrar la investigación en cuándo ayudan los enlaces opuestos pequeños.»

## Para llevar a la discusión

- [Enunciado, prueba y alcance](obstruccion_patron_finito.md).
- [Paquete de verificación](kit-patron-finito-kuramoto.zip), con las dos órdenes de reproducción en su README.
- [Traslado a grafos simples y normalizaciones](separacion_grafos_simples.md), incluido en el [paquete actual de revisión](paquete-revision-grafos-equipo-v1.zip).
- [Optimalidad en la familia límite](optimalidad_global.md), como segundo resultado candidato.

La pregunta para el mentor es si alguno de estos resultados aporta algo que merezca desarrollarse y defenderse en el evento. La elección sigue pendiente del equipo. No se enviaron mensajes ni archivos a terceros.

## Antes de defenderlo

Cada integrante que vaya a explicarlo necesita poder justificar: por qué se comprueba equilibrio antes de estabilidad; por qué el gauge equivale al complemento de la rotación; por qué los pivotes no son autovalores; por qué un testigo mejor que una cota superior prueba una separación; y por qué esto no aumenta la constante crítica general. Son puntos para revisar, no tareas declaradas como realizadas.

**Uso de IA:** texto y preparación por Codex (OpenAI), pendiente de lectura, revisión y ensayo del equipo. Conservar esta atribución y los historiales que contribuyeron al trabajo para la entrega correspondiente.

## Complemento para discutir, agregado el 19/10

El usuario confirmó que todavía no hubo devolución del mentor; no se registra asistencia ni resultados de una reunión. La [obstrucción asintótica nueva](enlaces_opuestos_limite.md) permite una respuesta más precisa si se propone reducir $h$: dentro de la familia explícita, los opuestos no elevan la conectividad límite sobre $\mu_0$, aunque sí mejoren un caso finito. En el constructor compacto, reducir hasta $h=10^{-6}$ produce un equilibrio inestable comprobado exactamente. El resultado y sus hipótesis requieren revisión antes de incorporarlos al discurso del equipo. Los tiempos de tres minutos anteriores no incluyen este complemento.
