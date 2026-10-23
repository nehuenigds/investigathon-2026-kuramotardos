# La cota 0,6934 también alcanza mínimos locales degenerados

22/10/2026. Deducción asistida por Codex. Es una ampliación de hipótesis de la [cota anterior](cota_flujos_06934.md), con la misma constante y el mismo certificado racional. Novedad bibliográfica y revisión matemática humana independientes pendientes.

Se contrastaron antes O'Keeffe, [IV.3 de v1](https://arxiv.org/html/2610.21271v1), y Lepsveridze–Zhang, [Lema 11 de v1](https://arxiv.org/html/2608.20010v1). El argumento cúbico que descarta las cuatro fases exactas es conocido y se atribuye a esta última fuente. Aquí se adapta a plantillas y se combina con la reducción y la cobertura 0,6934 del cuaderno.

## Enunciado

Sean $T_\ell=(x^{(\ell)},\theta^{(\ell)},P^{(\ell)})$ plantillas homogéneas de siete clusters, con $x_i^{(\ell)}>0$, suma uno y $P=P^T\in[0,1]^{7\times7}$. Supongamos que **cada $\theta^{(\ell)}$ es un mínimo local**, posiblemente no estricto, de

$$E_T(\theta)=\sum_{i<j}x_ix_jP_{ij}[1-\cos(\theta_i-\theta_j)].$$

Tras una rotación común, exigir

$$x_i^{(\ell)}\longrightarrow\bar x_i>0,\qquad
\theta_i^{(\ell)}\longrightarrow j_i\pi/2,\qquad j=(0,0,1,1,2,2,3).$$

Entonces

$$\boxed{\limsup_\ell\min_i(P^{(\ell)}x^{(\ell)})_i<\frac{3467}{5000}=0{,}6934.}$$

No se exige Hessiano transversal estrictamente positivo. La condición es ser un **mínimo local real**, no solo pasar equilibrio y semidefinitud. Se conservan masas límite positivas, cuatro fases y reparto `(2,2,2,1)`. No se obtiene una cota universal ni se incluyen masas límite nulas u otras geometrías.

## 1. El punto que sustituye la hipótesis estricta

**Lema.** En una plantilla cuyas fases son exactamente los cuatro cuartos de vuelta, con cuatro hojas no vacías, un mínimo local no tiene enlaces entre hojas distintas. En particular, $\mu(T)\leq1/4$.

**Prueba.** Poner $a_{ij}=x_ix_jP_{ij}$ y agregar conductancias por hojas A, B, C, W. La semidefinitud necesaria del Hessiano, probada con $(1,0,-1,0)$ y $(1,2,1,0)$, da $-4a_{AC}\geq0$ y $-4a_{BW}\geq0$. Los opuestos son nulos. El equilibrio sumado por hojas iguala las cuatro conductancias adyacentes a un mismo $T\geq0$. Rotar A por $-t$ y B por $t$ produce exactamente

$$\Delta E=T[\sin(2t)-2\sin t]=-2T\sin t(1-\cos t).$$

Si $T>0$, esto es negativo para todo $0<t<\pi$, contradiciendo minimalidad. Luego $T=0$. Cada grado es a lo sumo la masa de su hoja, y la menor de cuatro masas que suman uno no supera $1/4$. Las masas positivas y las densidades no negativas convierten las conductancias agregadas nulas en enlaces individuales nulos. $\square$

La demostración no clasifica un equilibrio a partir de ceros del Hessiano: utiliza un descenso explícito de la energía. Con $r=\tan(t/2)>0$ la identidad equivalente es

$$\Delta E=-\frac{8Tr^3}{(1+r^2)^2}<0\quad(T>0).$$

## 2. Auditoría del resto de la reducción

La positividad estricta del Hessiano en la nota base se utiliza para asegurar que $h_\ell=\max_i|\theta_i^{(\ell)}-j_i\pi/2|$ es positivo. El resto de su demostración superior utiliza únicamente equilibrio y semidefinitud. La suficiencia de otra caracterización de perfiles no interviene aquí.

Para comprobar esta dependencia, los pasos de la reducción son:

| Paso | Hipótesis que utiliza |
| --- | --- |
| Residuos exactamente nulos | Minimalidad local y $x_i>0$ dan $\partial_iE=x_iF_i=0$ |
| Hessiano semidefinido | Condición necesaria de segundo orden de un mínimo local |
| Identidad $S_h=O(h^2)$ | Equilibrio, offsets acotados y masas/densidades acotadas |
| Opuestos $O(h^2)$ y cuatro cortes | Pruebas no negativas del Hessiano y control de la traza de su restricción a hojas |
| Completar internos como relajación | $0\preceq J_o\preceq J$; la invertibilidad de $J$ viene de las masas positivas, no de estricta positividad de $H$ |
| Flujos positivos antes de tomar centros | La contradicción de grado límite al menos $u>2/3$ excluye flujos cero |
| Vector variacional $z\ne0$ | Máximo de offsets normalizados igual a uno y centros por flujo coincidentes |
| Masas, grados y capacidades | Desigualdades necesarias, sin márgenes espectrales finitos |
| Exclusión matricial | $M_\alpha-I\succ0$ del certificado contradice $z^TM_\alpha z\leq\|z\|^2$ para $z\ne0$ |

**Prueba de la ampliación.** Suponer que el límite superior de grados es al menos $u=3467/5000$ y extraer una subsucesión que lo realice. En ella los grados son eventualmente mayores que $1/4$. El lema descarta $h_\ell=0$ en esa cola. Podemos por tanto normalizar offsets y extraer las mismas subsucesiones compactas de masas y densidades de la [reducción base](cota_perfil_general.md).

Cada mínimo local proporciona las dos condiciones necesarias indicadas en la tabla. La identidad, las pruebas del Hessiano, la relajación de internos y la exclusión de flujos cero funcionan con semidefinitud. El argumento de centros conserva $z\ne0$, aunque una o dos separaciones principales sean nulas. Las [capacidades agregadas](cota_capacidades_agregadas.md) y la [propagación de masas vecinas](cota_flujos_06934.md) dan el mismo cubo $[967/1533,1533/967]^3$ y las mismas dos formas necesarias de estabilidad.

El certificado `profile_upper_certificate_06934-v1.json` excluye ese dominio completo, con sus 15.511 nodos y 7.756 hojas. No exige que las formas necesarias sean estrictas: certifica desigualdades estrictas que contradicen sus versiones no estrictas. La contradicción prueba el enunciado. $\square$

Esta auditoría de dependencias es una lectura matemática del argumento, no una verificación automática de la demostración en prosa. Sigue necesitando revisión humana independiente.

## 3. Corolario para grafos simples

Sean grafos simples no dirigidos de orden creciente con mínimos locales de su energía, constantes en siete grupos. Suponer proporciones límite positivas y las fases límite indicadas. No se impone positividad estricta del Hessiano completo.

Poner $x_i=n_i/n$, $P_{ij}=e(V_i,V_j)/(n_in_j)$ para $i\ne j$ y $P_{ii}=2e(V_i)/n_i^2$. Si $U$ repite una fase en cada grupo, se tiene exactamente

$$E_T(\varphi)=\frac1{n^2}E_G(U\varphi).$$

Restringir un mínimo local a esos movimientos conserva minimalidad, incluso sin regularidad de bloques. El grado de plantilla es el promedio del grupo dividido por $n$, de modo que $\delta/n\leq\mu(T)$. La ampliación da

$$\limsup\delta/n<0{,}6934.$$

Las normalizaciones $(\delta+1)/n$ y $\delta/(n-1)$ comparten esa cota al crecer $n$; no se igualan a orden finito. No se afirma que todo mínimo local de cualquier grafo tenga siete fases o se acerque al patrón indicado.

## 4. Ejemplo exacto que muestra por qué no basta H semidefinido

Tomar masas $x=(1,1,1,1,1,1,2)/8$, fases base $j\pi/2$ y densidades uno dentro de cada hoja y entre hojas adyacentes, cero entre opuestas. El equilibrio es exacto y $\mu=3/4$. El Hessiano de clusters es

$$H=\frac1{64}\operatorname{diag}\left(
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},0\right).$$

Es semidefinido, con tres ceros adicionales a la rotación. Rotar las hojas A y B como en el lema tiene $T=1/16$ y da $\Delta E=-r^3/[2(1+r^2)^2]<0$. Por tanto no es un mínimo local. Es un contraejemplo a reemplazar la hipótesis del enunciado por **solo** equilibrio y semidefinitud. No es un nuevo estado estable ni una mejora inferior de conectividad.

`verify_quarter_turn_local_minima.py` comprueba las identidades simbólicas, las condiciones exactas de este ejemplo y tres descensos racionales. Los puntos perturbados solo son testigos de menor energía; no se anuncian como equilibrios.

## Fuentes, reproducción y materiales

```text
python -B verify_quarter_turn_local_minima.py
```

Necesita SymPy de la caché externa existente. El JSON de resultados liga las notas de reducción y el certificado por SHA-256. El script no vuelve a ejecutar ni reconstruye el árbol; su reproducción completa consta en el paquete matemático anterior. El argumento continuo es la prueba escrita y sus identidades, no los tres valores de ejemplo.

La construcción inferior de [O'Keeffe v1](https://arxiv.org/html/2610.21271v1) sigue dando $\mu_0$ porque los mínimos estrictos también son mínimos locales. El intervalo del supremo de la clase ampliada se conserva como $[\mu_0,0{,}6934]$, sin afirmar que el extremo superior se alcance. No se compara numéricamente con un valor no explicitado de $\eta$ en el teorema universal de Lepsveridze–Zhang.

El informe, la charla, el póster y los paquetes congelados conservan el enunciado anterior con Hessiano estricto. Siguen siendo correctos para esa subclase, pero no incluyen esta ampliación. El resultado y su interés bibliográfico requieren revisión antes de incorporarlos a la defensa.

**Uso de IA:** consulta, deducción, código y texto por Codex (OpenAI). El descenso cúbico es una herramienta atribuida, no una novedad reclamada. No hubo subagentes, revisión humana independiente, comunicaciones, publicación ni entrega al evento.
