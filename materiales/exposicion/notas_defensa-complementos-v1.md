# Notas para preparar la defensa

## Eje actual: cota asintótica 0,6934

El usuario eligió este foco el 22/10/2026. El informe actual tiene cuatro páginas y la charla editable nueva tiene quince diapositivas. El guion suma 900 segundos como objetivo, sin ensayo medido. El PPTX v12 y el póster son versiones anteriores. Las notas restantes conservan los complementos históricos; no delimitan por sí solas el eje actual.

**¿Qué se demuestra exactamente?** Para sucesiones de plantillas homogéneas en equilibrio exacto, con siete masas límite positivas, fases límite j*pi/2 para j=(0,0,1,1,2,2,3) y Hessiano finito positivo fuera de la rotación, limsup mu < 0,6934. Se permiten internos incompletos, asimetrías, adyacencias límite cero y distintas escalas. No se cubren masas límite nulas u otras geometrías. El corolario de grafos requiere siete grupos de fase, orden creciente y Hessiano completo estricto.

**¿Por qué C4, de conectividad 3/4, no lo contradice?** El C4 exacto tiene ceros adicionales en el Hessiano. La positividad estricta es una hipótesis finita. No se clasifica un límite semidefinido como estrictamente estable ni se deduce estabilidad no lineal de esos ceros.

**¿Por qué completar internos está permitido?** Se usa solo como relajación de condiciones necesarias para una cota superior. Aumenta grados y debilita las pruebas variacionales. No se construye un nuevo equilibrio finito mediante esa operación. No se invierte el bloque interno original, que puede ser singular.

**¿Por qué z no es cero si hay distintas escalas?** Se normaliza por la desviación angular máxima y se extrae una subsucesión de offsets con máximo uno. Antes de usar centros se excluyen por grado el flujo común cero y los flujos de mitades cero. Con flujos positivos, equilibrio y cortes igualan los centros por flujo con W. Si las tres separaciones internas principales fueran cero, todos los offsets serían cero, contradiciendo la normalización.

**¿Bastan las dos formas cuadráticas para construir un equilibrio?** No se usa esa suficiencia. Son condiciones necesarias: una combinación convexa que resulta definida positiva menos la identidad contradice que un vector no nulo satisfaga ambas. Dos condiciones necesarias bastan para una exclusión, aunque no caractericen toda realización.

**¿Qué hace diferente la desigualdad de masas?** El flujo por masa de cada mitad está acotado por ambas hojas vecinas. Con flujo total uno, una identidad de sumandos no negativos da chi_i M_i <= M_vecina. Propagar esas relaciones conserva información que se pierde al sustituir todas las masas por cotas separadas.

**¿El certificado solo evalúa puntos?** El árbol cubre el cubo completo con bisecciones racionales, incluidos los bordes. Las cotas de raíces amplían los intervalos. Los tests de comparación y Bernstein son desigualdades uniformes sobre cada caja. Los números flotantes solo proponen parámetros. El verificador no importa constructor, predicados ni un solucionador espectral. La reducción analítica sigue siendo parte esencial de la prueba.

**¿Por qué el intervalo del supremo se escribe cerrado arriba?** El teorema da limsup < 0,6934 para cada sucesión con sus límites positivos. Al tomar el supremo sobre todas esas sucesiones no se declara un margen uniforme extra. Por eso se informa [mu0; 0,6934], sin afirmar que se alcance el extremo superior.

**¿Por qué el punto racional 0,6932 no es un récord?** Solo satisface las condiciones proyectadas. No aporta masas realizadas, transportes, fases o Hessiano de Kuramoto. Demuestra una barrera de la relajación concreta: esas desigualdades no pueden excluir ese punto. No constituye un nuevo contraejemplo de Kuramoto ni refuta que mu0 sea óptimo en una clase mayor.

**¿Qué normalización usa el corolario?** Al agregar grafos por promedios se usa P_ii=2e(V_i)/n_i² y el grado de plantilla es el promedio del grupo dividido por n. Así delta/n <= mu(T). Las diferencias con (delta+1)/n y delta/(n−1) se anulan al crecer n; no se igualan a orden finito. La convención diagonal uno del complemento de hojas completas es distinta y se convierte explícitamente.

**¿Qué queda por revisar?** La reducción analítica y el contraste de novedad requieren revisión independiente. La construcción inferior y mu0 se atribuyen a O'Keeffe. Codex realizó deducciones, búsquedas, código y redacción, incluidos constructor y verificadores. La separación de programas no acredita revisión humana. No se afirmó haber ganado ni se entregó material al evento.

Prueba central: `../cota_flujos_06934.md`. Fuentes y certificado: `../kit-cota-flujos-06934-v1.zip`. Contenido editable y notas: `charla-asintotica.json` y `guion-15-minutos.md`.

---


Borrador iniciado el 18/10/2026, actualizado el 19/10/2026, asistido por Codex. Acompaña al guion y a las demostraciones; no acredita comprensión ni revisión del equipo.

## La separación finita que abre la exposición

Con $x=(20,20,20,20,20,20,33)/153$ y las coordenadas racionales fijadas, toda plantilla en equilibrio con Hessiano de clusters semidefinido positivo, internos completos y opuestos vacíos satisface $\mu<0.68877337417$. Sus doce densidades adyacentes son libres: la cota cubre también elecciones sin simetría. Un testigo estricto con los mismos datos geométricos y solo el opuesto $(1,4)$ positivo satisface $\mu>0.68877357363$. La diferencia entre el testigo y la cota superior es mayor que $1.99\times10^{-7}$ por aritmética racional.

Por tanto, en esta geometría vaciar todos los opuestos pierde conectividad. No se demuestra que el testigo sea óptimo sobre otras geometrías ni se mejora $\mu_0$. El testigo conserva internos completos y reajusta densidades adyacentes: no consiste solo en agregar una arista a una plantilla inalterada. La prueba y las fracciones completas están en `../obstruccion_patron_finito.md`.

## Por qué la cota dual es una prueba

Como extensión técnica posterior a los materiales de exposición, `../separacion_abierta.md` prueba que la ventaja sigue siendo mayor que $1.99\times10^{-7}$ en una caja de radio $10^{-17}$ de masas y coordenadas. No exige preservar reflexión ni antipodalidad; en cada nueva geometría se vuelve a corregir equilibrio. El radio es conservador, no una tolerancia práctica. Esta extensión no está en las diapositivas ni el póster actuales y no debe incorporarse verbalmente sin revisar su prueba.

El grado mínimo está acotado por un promedio convexo de grados. Para $\lambda\geq0$, suma uno, $W\succeq0$ y equilibrio $b=0$, se tiene $\mu\leq\lambda^Td+\operatorname{tr}(WH)+\eta^Tb$. Al expandir en las densidades libres, la caja $0\leq p_e\leq1$ da $\mu\leq\kappa+\sum_e\max(0,a_e)$. Los multiplicadores racionales solo necesitan ser factibles; no se requieren optimalidad ni complementariedad exactas del SDP.

El constructor propuso los datos numéricamente; el verificador reconstruyó por aristas la expresión y comprobó con fracciones tanto el testigo como la cota. Sus nueve controles son cuatro entradas válidas y cinco corrupciones rechazadas. Esta suite es distinta de las nueve comprobaciones del cuaderno original.

## El traslado a grafos simples de la diapositiva 14

La cota superior no exige bloques regulares. Si se agrupan los vértices de igual fase y cada hoja es un clique, la plantilla de densidades promedio tiene equilibrio y Hessiano semidefinido cuando el grafo los tiene. Su grado mínimo de plantilla es el mínimo de los **promedios** de grados, más uno, dividido por $n$. Eso es mayor o igual que $(\delta+1)/n$; no se identifica promedio con mínimo.

Para los testigos inferiores se usa el Lema 2 del preprint con un denominador común. Se adelgazan solo las diagonales, se realiza por el lema y se completan los grupos de fase igual. Estas aristas no cambian equilibrio y añaden un Laplaciano positivo. El grado final de cada vértice del cluster $i$ es $nd_i-1$, de modo que $(\delta+1)/n=\mu(P)$ exactamente. Los dos grafos tienen el mismo orden y fases.

El orden tiene 113 cifras. Es una prueba de existencia por un lema atribuido; no se seleccionaron los desplazamientos ni se enumeraron aristas. Un único enlace opuesto en la plantilla significa un par de clusters enlazado con muchas aristas en el grafo, no agregar una sola arista al grafo original. La prueba y las conversiones están en `../separacion_grafos_simples.md`; sus ocho controles son otra suite distinta.

## Cómo leer los intervalos del gráfico

El eje muestra $10^7(\mu-0.688773)$ para hacer visible la separación. No son barras de error estadísticas. El encierro restringido combina un testigo estricto y una cota dual para ese patrón. El otro usa el testigo de un solo opuesto como cota inferior, y una cota superior que permite **todas** las densidades fuera de la diagonal. Esta cota amplia también vale para el patrón del testigo. Los decimales del gráfico se usan para representar extremos racionales; no constituyen la prueba.

## Qué aporta y qué se atribuye

La constante, la construcción de siete clusters y su predictor se atribuyen a O'Keeffe v1. La dualidad débil es estándar. Menara y colaboradores (2022) ya formulan asignación de pesos mediante incidencia, seno y espacio de ciclos. No se presenta el diseño lineal de pesos como una idea nueva. La novedad de la separación concreta y del teorema límite restringido sigue pendiente de revisión; la charla no afirma que se haya establecido.

## Alcance del máximo global

El máximo es global respecto de $r,q,w$ en el conjunto polinómico reducido $D,R\geq0$. Se conservan el patrón de siete clusters, la reflexión A/C, las mitades iguales y las masas proporcionales a $(r,r,1,1,r,r,1+q)$. El resultado no da una cota superior para todos los grafos ni cubre otros desdoblamientos o los términos a separación finita. En la frontera semidefinida se alcanza $\mu_0$; en el conjunto estricto es un supremo.

El valor $\mu_0$ y la construcción inicial proceden del preprint de O'Keeffe. En su IV.3 la optimalidad local aparece como observación numérica de un modelo más amplio. El teorema del cuaderno no debe presentarse como resolución de toda esa observación: prueba un máximo global en la subfamilia especificada.

## La imagen de las raíces y la prueba

El gráfico usa raíces numéricas y coordenadas redondeadas para su representación. La ausencia de otros cruces no se deduce de mirar el gráfico: la garantizan las dos resultantes y los 28 coeficientes de Bernstein encerrados con fracciones racionales. El argumento de continuidad requiere además comprobar el orden de las raíces en los extremos y que cada cuadrática conserve una única raíz positiva relevante. Esas partes están escritas en `optimalidad_global.md`.

## Equilibrio antes de estabilidad

Un Hessiano calculado en un punto que no es equilibrio no certifica estabilidad de un estado estacionario. El verificador racional exige primero que los siete residuos sean exactamente cero. Un control que modifica una densidad falla en ese paso.

## Fijar W y restringir a la rotación

Si $H\mathbf1=0$, entonces

$$
y^THy=(y-y_W\mathbf1)^TH(y-y_W\mathbf1).
$$

Todo vector puede llevarse al gauge $y_W=0$ sin cambiar su energía cuadrática. Por tanto, positividad estricta en ese gauge equivale a positividad para todo vector que no sea rotación, y en particular en $\mathbf1^\perp$. El gauge no es una base ortonormal: sus autovalores y pivotes no son los autovalores transversales normalizados.

## Los ceros adicionales

Un modo de rotación nulo siempre está presente. Otros ceros dejan inconcluso el test lineal. La plantilla de cuatro fases a cuarto de vuelta pasa equilibrio pero tiene forma de clusters degenerada; el verificador la rechaza por un pivote cero. No se concluye estabilidad solo por semidefinitud.

## Racionalización por bosque

Se adelgazan primero las densidades positivas para disponer de margen. Al aproximar puntos del círculo, se conservan sus clases de igualdad y antipodalidad. Por ello, todo enlace entre componentes del grafo de senos no nulos sigue llevando flujo cero. La suma de desequilibrios ponderados es exactamente cero en cada componente, y un árbol en cada una permite corregirlos.

El caso desconectado explica por qué la prueba usa un bosque. Los vértices aislados del grafo auxiliar ya tienen desequilibrio cero y no necesitan corrección. Las aristas del bosque tienen seno no nulo, lo que hace continuas sus correcciones al refinar la aproximación.

## Estabilidad tras racionalizar

La positividad estricta es abierta en los datos de una plantilla con un número fijo de clusters. Las correcciones tienden a cero, de modo que una aproximación suficientemente cercana conserva esa positividad y las fuerzas internas positivas. El argumento demuestra existencia de aproximaciones y no proporciona una cota uniforme para sus denominadores. Tampoco racionaliza las fases angulares: racionaliza seno y coseno.

## El ejemplo certificado y los récords

El ejemplo compacto previo alcanza aproximadamente $0.6877247359$. Supera $11/16$ y queda por debajo de $\mu_0\approx0.6929077063$. Sirve para ilustrar un certificado verificable con Python estándar y se conserva como antecedente; no es el testigo de la separación que ahora abre la charla. Ninguno de esos ejemplos constituye un récord.

Los datos de las plantillas son exactos; los decimales del póster y los gráficos son representaciones para lectura. El ejemplo previo y el caso finito usan coordenadas racionales dadas por arcotangentes, distintas de la parametrización angular lineal a separación finita.

## Plantilla y grafo simple

El certificado comprueba las hipótesis del Lema 2 del preprint y eso implica existencia de grafos simples con el equilibrio estable. No se enumeraron sus aristas ni se seleccionaron explícitamente los conjuntos de desplazamientos. La conclusión de realización debe atribuirse a ese lema, y no anunciarse como un grafo explícito construido en el cuaderno.

En el certificado racional anterior, realizado sin completar después los clusters, $\delta/n=\mu$ de la plantilla adelgazada; entonces la propuesta usa $\mu+1/n$ y la otra normalización es $\mu n/(n-1)$. En los dos grafos completados de la separación que abre la charla se usa otra plantilla de referencia: $\delta/n=\mu_{\rm original}-1/n$, $(\delta+1)/n=\mu_{\rm original}$ y $\delta/(n-1)=(n\mu_{\rm original}-1)/(n-1)$. Precisar siempre a cuál plantilla se refiere $\mu$.

## Qué prueban los experimentos

Las 430 combinaciones racionales son dos grillas deterministas concretas. La selección compacta minimiza el denominador entre sus casos aceptados que superan $11/16$. No demuestra un mínimo de denominador sobre todas las plantillas. Las búsquedas previas sin mejoras tampoco certifican sincronización global ni ausencia de contraejemplos.

La nueva grilla de flujos produjo 180 testigos estrictos, todos verificados con fracciones. Su mejor valor es aproximadamente $0.6928144512<\mu_0$. Un único arranque local de 219 evaluaciones dio un extremo estricto de aproximadamente $0.6905544056<\mu_0$. Las búsquedas tienen dominios y soportes acotados; no acotan otras plantillas. Las diferencias diminutas entre otros testigos no certifican diferencias entre óptimos. Datos y restricciones: `../exploracion_flujos.md`.

## Novedad y atribución

La revisión bibliográfica es acotada. Canale es un antecedente directo para convertir grafos ponderados en simples. Las herramientas de flujos en árboles y puntos racionales del círculo son conocidas. Se propone revisar la combinación usada en el lema de racionalización y la optimalidad de la subfamilia. La ausencia de un antecedente en las lecturas realizadas no demuestra novedad.

## Uso de IA y pendientes reales

Codex realizó derivaciones, código, búsquedas, verificaciones y redacción. Constructor y verificador separados proceden del mismo agente. La portada usa una ilustración de `image_gen`, identificada como conceptual. El prompt y la copia están en el proyecto. Las notas contienen fuentes por diapositiva.

Todavía faltan revisión humana, un ensayo medido y reunir los historiales completos de IA para la entrega. El guion propone tiempos que suman 15 minutos; no registra una duración ensayada. No se presentó ningún material al evento.

## Complemento del 19/10: por qué no basta reducir la separación

La nota `../enlaces_opuestos_limite.md` fue la primera obstrucción adicional. Para masas y patrón principal fijos, fases prescritas hasta $O(h^3)$ y doce correcciones adyacentes libres a primer orden, la estabilidad obliga a que los opuestos sean $O(h^2)$. Dos pruebas cuadráticas dan cotas por $D$ y $R$; por el teorema anterior no aumentan la conectividad límite sobre $\mu_0$. Si ese valor límite se alcanza, los opuestos deben ser $o(h^2)$. Esa primera versión no cubre masas variables con $h$; la ampliación posterior siguiente sí las admite bajo su perfil explícito. El informe y la charla actuales exponen la ampliación; el póster conserva el contenido anterior.

El constructor compacto con $q=13/20,w=7/5$ tiene $D=-33/10000$. Es estable a $h=1/200$, pero al reducirlo a $10^{-6}$ se certifica una dirección de energía negativa en un equilibrio exacto. Esto no contradice la separación finita; evita extrapolarla como una familia estable hasta cero. La prueba general no depende de estos controles puntuales. Novedad y revisión independiente siguen pendientes.

La recuperación de historiales de texto visible y sus cortes se documentó en `../trazabilidad/README.md`. Esa cobertura parcial no se presenta como un historial bruto completo. El usuario confirmó nuevamente el 19/10 que el equipo sigue sin devolución de mentor.

## Un ejemplo pequeño para distinguir estabilidad y sincronía

`../grafo_explicito_canale.md` reproduce una red conocida de Canale con 24 vértices, 180 aristas y grado 15. Admite sincronía y un equilibrio no sincronizado, ambos estrictos módulo rotación. La comprobación usa el Hessiano completo, no solo el de ocho grupos, y conserva las tres normalizaciones: $\delta/n=5/8$, $(\delta+1)/n=2/3$ y $\delta/(n-1)=15/23$. Las dos trayectorias cercanas ayudan a explicar que ser estable no implica tener todas las fases iguales. Son ilustraciones numéricas; el certificado exacto justifica los equilibrios. Es reproducción conocida, sin atribuirle novedad o confundirla con los grafos existenciales de la separación principal.

## Complemento posterior: variar masas y términos superiores

La prueba de `../patron_principal_limite.md` ya no supone masas fijas ni derivadas. Basta converger al perfil explícito de masas, fases reescaladas y adyacencias. Una identidad exacta de equilibrio limita la suma de pesos adyacentes del Hessiano; la semidefinitud fuerza opuestos $O(h^2)$ y dos variaciones internas producen $D,R\geq0$. El teorema algebraico previo da $\mu_\infty\leq\mu_0$ para ese perfil. No se debe decir que esto cubre cualquier perturbación de C4 ni todas las configuraciones de siete clusters.

En particular, con perfil $r=1,q=13/20,w=7/5$, $D=-33/10000$ impide cualquier sucesión estable que cumpla esas hipótesis, aun con masas variables y convergencia no suave. Esto no niega los testigos finitos: para continuar de forma estable hasta cero habría que cambiar el perfil de primer orden. El corolario de grafos usa promedios y una convención diagonal distinta, y requiere orden tendiendo a infinito para comparar las normalizaciones. El informe de cinco páginas y las diapositivas 10–12 de la charla v12 incorporan la ampliación. Su novedad y revisión humana siguen pendientes.

## ¿Qué pasa con mitades desiguales?

La ampliación de `../perfil_general_cuatro_hojas.md`, posterior a la charla v12, caracteriza perfiles principales `(2,2,2,1)` con adyacencias positivas y tres separaciones no nulas mediante equilibrio, cortes y tres pruebas escalares. Incluye la construcción de una sucesión estricta; una matriz completada por sí sola no bastaría. Para una deformación explícita con masas, desplazamientos y densidades cruzadas ligados por un parámetro $t$, las tres pruebas son $2t(1-t)D$, $2t(1-t)R$ y $2t(1-t)(4r^2+Kw^2)$. Los grados no dependen de $t$. Por tanto, esa familia mantiene el máximo global $\mu_0$; la igualdad admite distintos repartos de mitades. No se prueba una cota máxima para todos los perfiles generales. El artículo ya menciona cualitativamente la propiedad de mitades desiguales como observación numérica. Hay ejemplos racionales estrictos con repartos 20/80 y 80/20; son inferiores al récord conocido. Esta ampliación requiere revisión antes de incorporarla a la exposición.

## ¿Hay una cota para una clase más general cerca de C4?

`../cota_perfil_general.md` prueba que el límite superior de conectividades es menor que 0,70 para sucesiones de siete clusters con masas límite positivas que se acercan a cuatro cuartos de vuelta con reparto `(2,2,2,1)` y Hessiano finito positivo fuera de la rotación. No exige reflexión, mitades iguales, internos completos ni la misma escala de separación. Una relajación de los internos y cotas de transporte reducen el problema a tres parámetros; un árbol racional cubre todo el cubo y excluye conectividad límite al menos 0,70. El verificador separado comprueba las hojas y la cobertura con Python estándar. La novedad y la reducción analítica necesitan revisión humana. Es una cota asintótica de esa clase: no se aplica a cualquier geometría finita ni determina la conectividad crítica general. El C4 exactamente degenerado tiene 3/4 y ceros extra, por lo que no satisface la hipótesis estricta. Este resultado aún no está en la charla v12.

La mejora posterior de `../cota_capacidades_agregadas.md` sustituye 0,70 por 0,6935 en la misma clase. La capacidad total de cada corte da una cota inferior de la escala común; los grados de las cuatro hojas dan una cota superior. Conservar ambas excluye más perfiles que las capacidades enlace a enlace. El certificado racional nuevo tiene 5.735 hojas y no depende del máximo declarado por un optimizador. La diferencia con la construcción conocida es menor que 0,000593, sin demostrar que sea el óptimo ni modificar el umbral general. Esta ampliación tampoco está en la charla v12 y requiere revisión antes de incorporarla.

## ¿Por qué no se obtiene directamente 0,69291?

`../cota_flujos_por_masa.md` añade la condición necesaria `chi_i M_i <= M_vecina`. Sin embargo, un punto racional satisface estrictamente ambas formas de estabilidad y todas las restricciones proyectadas incluso con umbral 0,6932. Eso demuestra un límite de la relajación concreta: subdividirla más no elimina ese punto. No es un equilibrio de Kuramoto ni un contraejemplo a la conjetura de que el valor conocido sea óptimo para una clase mayor. Hacen falta restricciones adicionales que liguen los transportes a las masas realizadas. El kit nuevo conserva ese punto y cuatro controles finitos estrictos; la tentativa 0,6934 se comprueba por separado y no se usa aquí como resultado.
