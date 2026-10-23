# Notas para preparar la defensa

## Eje actual: cota asintótica 0,6934

Preparado para **Los Kuramotardos**, con el foco elegido por el usuario el 22/10/2026. Ese día el usuario confirmó que el equipo todavía no revisó la prueba; conviene empezar por la [primera lectura](../primera-lectura-cota-06934.md). La revisión ampliada de la charla del 23/10 tiene quince diapositivas y [guion](guion-15-minutos-minimos-locales-v2.md) de 900 segundos como objetivo, sin ensayo medido. El [informe ampliado](../informe/output/pdf/informe-minimos-locales-v2.pdf) tiene cinco páginas y el [póster ampliado](poster/output/pdf/poster-minimos-locales-v2.pdf) una hoja A1; ambos exigen mínimos locales reales, posiblemente degenerados. El póster original y el [guion breve anterior](../guion-checkpoint-equipo.md) conservan la hipótesis estricta. El PPTX v12 y las [notas previas de complementos](notas_defensa-complementos-v1.md) se conservan como material histórico. Estas respuestas no acreditan comprensión ni revisión del equipo.

**¿Qué se demuestra exactamente?** Para sucesiones de plantillas homogéneas, con siete masas límite positivas, fases límite j*pi/2 para j=(0,0,1,1,2,2,3) y un mínimo local real de la energía en cada elemento finito, limsup mu < 0,6934. Se permite degeneración, además de internos incompletos, asimetrías, adyacencias límite cero y distintas escalas. No se cubren masas límite nulas u otras geometrías. El corolario requiere mínimos locales del grafo constantes en siete grupos y orden creciente. Restringir la energía a esos movimientos conserva minimalidad; no se impone Hessiano completo estricto.

**¿Por qué C4, de conectividad 3/4, no lo contradice?** En las cuatro fases exactas, la semidefinitud vacía los opuestos y el equilibrio iguala los cuatro flujos adyacentes a T. Si T>0, girar A por −t y B por t da un descenso exacto T[sin(2t)−2sin(t)] para giros positivos pequeños. Un mínimo local exige T=0 y tiene conectividad a lo sumo 1/4. Por ello una subsucesión de grado alto debe tener separación h positiva. Es la adaptación ponderada del Lema 11 de Lepsveridze–Zhang, no una clasificación basada solo en ceros del Hessiano.

**¿Por qué completar internos está permitido?** Se usa solo como relajación de condiciones necesarias para una cota superior. Aumenta grados y debilita las pruebas variacionales. No se construye un nuevo equilibrio finito mediante esa operación. No se invierte el bloque interno original, que puede ser singular.

**¿Por qué z no es cero si hay distintas escalas?** Se normaliza por la desviación angular máxima y se extrae una subsucesión de offsets con máximo uno. Antes de usar centros se excluyen por grado el flujo común cero y los flujos de mitades cero. Con flujos positivos, equilibrio y cortes igualan los centros por flujo con W. Si las tres separaciones internas principales fueran cero, todos los offsets serían cero, contradiciendo la normalización. La [auditoría de flujos y centros](../auditoria_flujos_centros.md) explicita que $f_i\geq(2u-1)x_i/2>0$ antes de dividir por el flujo total y que $\|z\|^2\geq\min_L x_{2L}x_{2L+1}>0$ con masas normalizadas. La cota positiva depende de la sucesión; no se afirma un margen común a toda la clase.

**¿Bastan las dos formas cuadráticas para construir un equilibrio?** No se usa esa suficiencia. Son condiciones necesarias: una combinación convexa que resulta definida positiva menos la identidad contradice que un vector no nulo satisfaga ambas. Dos condiciones necesarias bastan para una exclusión, aunque no caractericen toda realización.

**¿Qué hace diferente la desigualdad de masas?** El flujo por masa de cada mitad está acotado por ambas hojas vecinas. Con flujo total uno, una identidad de sumandos no negativos da chi_i M_i <= M_vecina. Propagar esas relaciones conserva información que se pierde al sustituir todas las masas por cotas separadas.

**¿El certificado solo evalúa puntos?** El árbol cubre el cubo completo con bisecciones racionales, incluidos los bordes. Las cotas de raíces amplían los intervalos. Los tests de comparación y Bernstein son desigualdades uniformes sobre cada caja. Los números flotantes solo proponen parámetros. El verificador no importa constructor, predicados ni un solucionador espectral. La reducción analítica sigue siendo parte esencial de la prueba.

**¿Por qué el intervalo del supremo se escribe cerrado arriba?** El teorema da limsup < 0,6934 para cada sucesión con sus límites positivos. Al tomar el supremo sobre todas esas sucesiones no se declara un margen uniforme extra. Por eso se informa [mu0; 0,6934], sin afirmar que se alcance el extremo superior.

**¿Por qué el punto racional 0,6932 no es un récord?** Solo satisface las condiciones proyectadas. No aporta masas realizadas, transportes, fases o Hessiano de Kuramoto. Demuestra una barrera de la relajación concreta: esas desigualdades no pueden excluir ese punto. No constituye un nuevo contraejemplo de Kuramoto ni refuta que mu0 sea óptimo en una clase mayor.

**¿Qué normalización usa el corolario?** Al agregar grafos por promedios se usa P_ii=2e(V_i)/n_i² y el grado de plantilla es el promedio del grupo dividido por n. Así delta/n <= mu(T). Las diferencias con (delta+1)/n y delta/(n−1) se anulan al crecer n; no se igualan a orden finito. La convención diagonal uno del complemento de hojas completas es distinta y se convierte explícitamente.

**¿Qué queda por revisar?** La reducción analítica y el contraste de novedad requieren revisión independiente. La construcción inferior y mu0 se atribuyen a O'Keeffe. Codex realizó deducciones, búsquedas, código y redacción, incluidos constructor y verificadores. La separación de programas no acredita revisión humana. No se afirmó haber ganado ni se entregó material al evento.

**Versiones para revisar.** La [nota de mínimos locales](../cota_minimos_locales_06934.md) extiende 0,6934 sin exigir Hessiano finito estricto, manteniendo las demás hipótesis límite. Exige ser un mínimo local real: equilibrio y semidefinitud solos no bastan. El informe ampliado y sus controles están en el [paquete v2](../paquete-revision-asintotica-ampliada-equipo-v2.zip), cuya [guía](../revision_asintotica_ampliada_equipo.md) reproduce las comprobaciones. La charla editable actual, revisión 6, y el póster ampliado ya exponen esa ampliación. El ZIP v2 conserva la charla de la revisión estricta 4 y el póster estricto; no contiene los nuevos medios ni se reescribió. La fuente nativa de la revisión anterior está conservada. El guion breve sigue estricto. Revisar la ampliación antes de usarla en la defensa; no se registra revisión del equipo.

**¿Mejora la cota universal conocida?** No se puede afirmar eso. [Lepsveridze–Zhang, Teorema 1](https://arxiv.org/html/2608.20010v1), no fija eta. El resultado del cuaderno tiene una clase y una constante explícitas; no es una comparación numérica entre cotas universales.

## Pasos delicados, con las cuentas a mano

La [auditoría del paso variacional](../auditoria_paso_variacional.md), añadida después del paquete congelado, desarrolla las estimaciones uniformes y conserva el término de residuo antes de usar equilibrio. Explica por qué cada corte se cancela por separado y cómo obtener las dos desigualdades sin invertir el bloque interno original. Su comprobador separa identidades exactas de controles a 120 dígitos; no sustituye la revisión humana de la reducción completa.

**¿Por qué los opuestos son de orden h² sin derivar los datos?** Fijar W y normalizar por la desviación angular máxima $h$. Escribir $u_i=(\theta_i-j_i\pi/2)/h$, $d_{ij}=u_i-u_j$ y $a_{ij}=x_ix_jP_{ij}$. Los offsets quedan acotados aunque haya varias escalas. La identidad exacta de equilibrio y restos trigonométricos uniformes dan $S_h=O(h^2)$, con $S_h=\sum_{\rm ady}a_{ij}\cos(\theta_i-\theta_j)$. Probar semidefinitud con las rotaciones de hojas $(1,0,-1,0)$ y $(1,2,1,0)$ da, respectivamente,

$$S_h-4\sum_{A-C}a_{ij}\cos(hd_{ij})\geq0,\qquad S_h-4\sum_{B-W}a_{ij}\cos(hd_{ij})\geq0.$$

Los cosenos tienden a uno y las masas límite son positivas: cada densidad opuesta es $O(h^2)$. El Hessiano restringido a indicadores de hojas es semidefinido y tiene traza $O(h^2)$. Su norma está acotada por esa traza; por tanto, cada entrada adyacente es $O(h^2)$. Dividirla por $h$ produce cada uno de los cuatro cortes principales nulos. No se exige una expansión diferenciable de masas o densidades. Véase [la reducción base, apartado 1](../cota_perfil_general.md#1-normalizar-la-separación-y-completar-solo-como-relajación).

**¿Dónde se descartan los flujos cero?** Bajo la contradicción de grado límite al menos $u=3467/5000$, con internos completados solo como relajación, el flujo común cero deja como grados únicamente las masas de hojas; el mínimo no supera $1/4$. Si una mitad tiene flujo cero, su grado es la masa de su hoja, como máximo $1-u<u$. Se descartan ambos casos antes de definir centros por flujo y antes de reescalar el flujo común a uno. Los demás flujos son entonces positivos; no se está dividiendo por un límite posiblemente nulo.

**¿Cómo se evita invertir un bloque interno singular?** Sean $J_o$ los internos originales y $J$ los completos. Se tiene $0\preceq J_o\preceq J$, con $J$ diagonal estrictamente positivo porque las masas límite lo son. El bloque cruzado principal $C$ no cambia al completar internos. En cada prueba modal, tomar $\zeta=-J^{-1}C^Te_i$ da

$$0\leq E_o+2(C\zeta)_i+\zeta^TJ_o\zeta
\leq E+2(C\zeta)_i+\zeta^TJ\zeta
=E-(CJ^{-1}C^T)_{ii}.$$

Aquí $E_o=k^TJ_ok$ y $E=k^TJk$. Omitir la contribución no positiva de los opuestos solo relaja la condición. Se usa $J^{-1}$, nunca $J_o^{-1}$. Esto prueba una condición necesaria; no afirma que completar internos preserve los residuos de un equilibrio finito.

**¿Se puede explicar la desigualdad nueva sin el programa?** Sí. En una hoja dividida de masas $m_0,m_1$, normalizar $f_0+f_1=1$ y poner $\tau_i=f_i/m_i$. El equilibrio principal hace iguales los flujos entrantes y salientes de cada mitad. La capacidad de una hoja vecina de masa $B$ impone $\tau_0,\tau_1\leq B$. Como $m_0\tau_0+m_1\tau_1=1$,

$$B-\tau_0\tau_1(m_0+m_1)
=m_0\tau_0(B-\tau_1)+m_1\tau_1(B-\tau_0)\geq0.$$

Con $\chi=\tau_0\tau_1$, se obtiene $\chi M\leq B$ para cada vecina. Dividir por la masa bruta total $N$ da las seis desigualdades sobre masas relativas. La prueba no supone mitades iguales. El [texto central, apartado 2](../cota_flujos_06934.md#2-refuerzo-que-permite-bajar-la-cota) explica su propagación.

**¿Dónde entra la misma escala en grados y cortes?** Tras normalizar cada corte a flujo uno, el promedio de grado de una hoja de masa bruta $M_i$ es $M_i+2/M_i$; en W ese es su grado exacto. De grado mínimo al menos $uN$ se deduce $N^2\leq2/[y_i(u-y_i)]$, con $y_i=M_i/N$. Se excluyen primero cotas inferiores $L_i$ incompatibles con $L_i\leq y_i\leq1-u$ o con la suma uno. Como $u>2/3$, $t(u-t)$ es creciente en $[0,1-u]$. Así, con $D=\max_i L_i(u-L_i)$, se tiene $N^2\leq2/D$.

El mismo corte de flujo uno exige $1\leq M_pM_q$. Si $r,s$ son las otras hojas, $y_py_q\leq(1-L_r-L_s)^2/4$, por lo que

$$\frac4{(1-L_r-L_s)^2}\leq N^2\leq\frac2D.$$

De aquí sale $(1-L_r-L_s)^2\geq2D$. No se igualan grado mínimo y promedio; se usa que el mínimo no supera el promedio de ninguna hoja. Véanse [las capacidades agregadas, apartados 2–3](../cota_capacidades_agregadas.md#2-cotas-inferiores-de-masas-y-escala-común).

**¿Cuáles son exactamente las dos matrices que se combinan?** Para $a=\chi_A,b=\chi_B,c=\chi_C$ y covarianzas normalizadas $\kappa,\lambda$, las formas necesarias son $\|L_1z\|^2\leq\|z\|^2$ y $\|L_2z\|^2\leq\|z\|^2$, con

$$L_1=\begin{pmatrix}0&\kappa&0\\-\kappa&2b&-\lambda\\0&\lambda&0\end{pmatrix},\qquad
L_2=\begin{pmatrix}2a&-\kappa&0\\\kappa&0&-\lambda\\0&-\lambda&2c\end{pmatrix}.$$

Por tanto, $z^T[\alpha L_1^TL_1+(1-\alpha)L_2^TL_2-I]z\leq0$ para todo $\alpha\in[0,1]$. Como $z\ne0$, certificar la matriz entre corchetes estrictamente positiva produce una contradicción. Las hojas matriciales lo hacen uniformemente sobre su caja; las demás hojas excluyen una condición de masas o capacidades. No se usa la suficiencia de estas dos formas para construir un equilibrio. Las identidades y menores se comprueban en `verify_covariance_reduction.py`.

**¿Qué parte no valida el verificador racional?** Comprueba el dominio declarado, su partición y todas las justificaciones implementadas. No lee la demostración en prosa ni certifica por sí mismo que toda sucesión de Kuramoto se reduzca a ese dominio. Esa correspondencia, la validez de la reducción analítica y la novedad necesitan revisión humana independiente. Los ejemplos finitos y las alteraciones rechazadas ayudan a detectar errores; no sustituyen esa revisión.

## Fuentes y complementos

- [Prueba central y alcance](../cota_flujos_06934.md), [paquete matemático](../kit-cota-flujos-06934-v1.zip) y [guía de reproducción](../kit_cota_flujos_06934.md).
- [Guion largo](guion-15-minutos.md), contenido editable `charla-asintotica.json` y [guion breve del checkpoint](../guion-checkpoint-equipo.md).
- [Notas históricas conservadas](notas_defensa-complementos-v1.md): separación finita, traslados existenciales, pruebas del perfil restringido y ejemplo conocido de Canale. Las referencias allí a diapositivas o materiales «actuales» pertenecen a sus versiones anteriores.

**Uso de IA:** Codex (OpenAI) preparó las respuestas y sus cuentas a partir del cuaderno. Se conserva la atribución de la construcción y de $\mu_0$ a O'Keeffe. Esta preparación no es un ensayo, una revisión humana independiente ni una comprobación de novedad.
