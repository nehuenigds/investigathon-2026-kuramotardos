# Revisar la cota asintótica 0,6934

22/10/2026. Borrador asistido por Codex. Leer `cota_flujos_06934.md` junto con las notas de reducción incluidas.

La cota se refiere a sucesiones estrictas de siete clusters con masas límite positivas, cuyas fases convergen a cuatro cuartos de vuelta en reparto `(2,2,2,1)`. Permite asimetrías, internos incompletos y distintas escalas de separación. No determina la conectividad crítica general. La construcción conocida y esta cota dejan un intervalo de ancho menor que 0,000493 para el supremo de valores límite de esa clase.

Desde una copia extraída, con Python 3.11 o posterior y sin `-O`:

```text
python -B -S verify_profile_upper_mass_flow.py
python -B -S profile_upper_mass_flow_checks.py
python -B -S mass_flow_lemma_checks.py
python -B verify_covariance_reduction.py
python -B verify_global_optimum.py
```

Las tres primeras órdenes usan Python estándar. El verificador de cobertura reconstruye las 15.511 cajas y hojas desde el cubo raíz y comprueba sus desigualdades con fracciones, raíces enteras y Bernstein racional. No importa el constructor, sus predicados, NumPy ni un solucionador espectral. Los controles rechazan seis alteraciones del certificado y conservan tres testigos finitos estrictos. Los controles de la desigualdad de masas conservan cuatro testigos previos y comprueban 24 desigualdades. El equilibrio exacto se comprueba antes de estabilidad. Constructor y comprobadores proceden del mismo agente, por lo que su separación no constituye revisión humana independiente.

Las dos órdenes simbólicas necesitan SymPy y sus dependencias según `requirements-verificacion.txt`. La última reproduce el intervalo algebraico anterior para la constante de referencia, no el teorema superior nuevo. No hace falta ejecutar las búsquedas ni reconstruir el árbol para verificar el certificado guardado.

La nota de flujos del 20/10 conserva su estado histórico, anterior a terminar la cobertura 0,6934. Su testigo racional sigue mostrando que las desigualdades proyectadas no bastan para obtener 0,69291: satisface la relajación a 0,6932, sin realizar transportes o un equilibrio de Kuramoto. No es una nueva cota inferior. El intento incompleto de 0,69291 y los 24 arranques numéricos se incluyen con sus límites, fallos y semilla. Para relanzar el constructor o la búsqueda se necesitan NumPy y SciPy; no forman parte de las cinco órdenes anteriores.

`MANIFEST.json` liga las fuentes y los datos. Los verificadores regeneran JSON, por lo que conviene usar una copia y comparar después sus huellas. El recibo externo `profile_upper_mass_flow_kit_validation.json` registra la reproducción aislada fuera de W y Drive. Las órdenes simbólicas usan la caché de bibliotecas existente; no se probó una instalación nueva ni se reconstruyeron medios. El paquete no contiene el repositorio completo, historiales completos de IA, PDFs fuente ni medios de exposición. Los paquetes anteriores permanecen congelados.

Codex (OpenAI) realizó consulta, deducción, código, cálculos, controles y redacción. No hubo subagentes, revisión humana independiente, comunicaciones, publicación ni entrega al evento. La novedad bibliográfica y la revisión del argumento analítico siguen pendientes.
