# Guion de tres minutos: cota asintótica 0,6934

22/10/2026. Borrador para **Los Kuramotardos**, con el foco elegido por el usuario. Los tiempos suman 180 segundos como objetivo; no se hizo un ensayo medido. Leer y revisar antes de usarlo. El guion anterior se conserva en [su versión sobre la separación finita](guion-checkpoint-equipo-separacion-v1.md).

## 0:00–0:30 — La pregunta

«Somos Los Kuramotardos. Estudiamos Kuramoto homogéneo: osciladores idénticos sobre una red. La pregunta es cuánta conectividad puede conservar un equilibrio no sincronizado que siga siendo un mínimo estricto de energía, salvo la rotación común. Con asistencia de IA se desarrolló una cota superior para una clase asintótica concreta, que elegimos como eje de la defensa.»

## 0:30–1:20 — El resultado y sus hipótesis

«Pasamos a plantillas ponderadas de siete clusters. En cada elemento exigimos equilibrio exacto y Hessiano positivo fuera de la rotación. Las siete masas convergen a límites positivos. Las fases convergen a cero, pi medios, pi y tres pi medios, con dos, dos, dos y un cluster.

»Bajo esas hipótesis, el límite superior de las conectividades es menor que cero coma seis nueve tres cuatro. Se permiten mitades desiguales, internos incompletos y distintas escalas de separación. La construcción de O'Keeffe aporta el extremo inferior conocido. El intervalo del supremo de esta clase tiene ancho menor que cero coma cero cero cero cuatro nueve tres. No determinamos el umbral general.»

## 1:20–2:20 — Por qué es una prueba y qué se comprobó

«La reducción usa equilibrio exacto y pruebas variacionales del Hessiano. Primero controla los enlaces opuestos y excluye flujos nulos por grado. Solo después normaliza los flujos. Una desigualdad conserva relaciones entre masas vecinas; los grados y las capacidades de los cortes comparten la misma escala.

»Estas condiciones llevan a un dominio compacto de tres parámetros. El certificado cubre todo ese dominio con siete mil setecientas cincuenta y seis hojas. Cada hoja contradice una capacidad o prueba una matriz definida positiva incompatible con la estabilidad necesaria. La aceptación usa fracciones exactas, no autovalores flotantes.

»Un verificador separado reconstruye la cobertura. El paquete pasó cinco órdenes en una copia aislada y rechazó seis alteraciones. Constructor y verificadores proceden del mismo agente de IA: no equivalen a revisión humana independiente.»

## 2:20–3:00 — La revisión que necesitamos

«Queremos revisar tres pasos delicados: que la reducción no pierda perfiles con distintas escalas; que completar internos sea una relajación válida; y que las exclusiones del programa correspondan a las desigualdades escritas. También necesitamos contrastar antecedentes de la cota específica.

»La fuente aporta la construcción inferior; no afirmamos mejorar ese récord. Tampoco cubrimos masas límite nulas u otras geometrías. La cota, su alcance y el uso de IA están declarados en el informe y el póster.»

## Apoyo para la discusión

- [Enunciado y prueba central](cota_flujos_06934.md), con la reducción de equilibrio y estabilidad en [la nota base](cota_perfil_general.md).
- [Paquete matemático](kit-cota-flujos-06934-v1.zip) y [cinco órdenes de reproducción](kit_cota_flujos_06934.md). No es necesario reconstruir la búsqueda o el árbol.
- [Informe de cuatro páginas](informe/output/pdf/informe-kuramoto.pdf), [póster A1](exposicion/poster/output/pdf/poster-kuramoto.pdf) y [respuestas para la defensa](exposicion/notas_defensa.md).

El umbral exacto del resultado es $3467/5000$. La referencia inferior es $\mu_0\approx0{,}69290770637$, atribuida a O'Keeffe. Para el supremo se comunica $[\mu_0,0{,}6934]$, con extremo superior cerrado. Los 15.511 nodos y las 7.756 hojas describen la cobertura; la reducción analítica sigue siendo parte de la prueba. El corolario para grafos requiere siete grupos de fase con las mismas hipótesis límite y orden creciente; las normalizaciones se comparan solo tras convertirlas.

**Uso de IA:** preparación y redacción por Codex (OpenAI). No acredita comprensión, revisión matemática, aprobación o ensayo del equipo. No se enviaron comunicaciones ni materiales a terceros. La última confirmación de ausencia de devolución de mentor fue el 19/10, no una nueva respuesta del 22/10.
