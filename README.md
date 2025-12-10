# Classical-Mechanics-II


# Mecánica Clásica
## Formalismo Lagrangiano, Formalismo Hamiltoniano, Fuerzas Centrales, Scattering y Pequeñas Oscilaciones

---

# 4. Formalismo Lagrangiano

El formalismo lagrangiano surge del **principio de mínima acción**, que establece que la trayectoria física de un sistema es aquella que minimiza la acción:

$$
S[q] = \int_{t_1}^{t_2} L(q_i, \dot{q}_i, t)\, dt
$$

donde el **Lagrangiano** es:

$$
L = T - V
$$

## 4.1 Ecuaciones de Euler–Lagrange
La condición $\delta S = 0 $ conduce a:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_j}\right) -
\frac{\partial L}{\partial q_j} = 0
$$

Estas ecuaciones reemplazan a la segunda ley de Newton, especialmente útiles cuando:

- hay restricciones holónomas,
- se usan coordenadas generalizadas,
- el sistema posee simetrías.

## 4.2 Simetrías y teorema de Noether
Toda simetría continua del Lagrangiano implica una cantidad conservada.

Ejemplos:

- **Invarianza temporal** → Conservación de la energía  
- **Invarianza espacial** → Conservación del momento lineal  
- **Invarianza rotacional** → Conservación del momento angular

## 4.3 Coordenadas cíclicas
Una coordenada es cíclica si:

$$
\frac{\partial L}{\partial q_j} = 0
$$

→ Se conserva su momento conjugado:

$$
p_j = \frac{\partial L}{\partial \dot{q}_j} = \text{cte}
$$

---

# 5. Formalismo Hamiltoniano

El formalismo hamiltoniano reescribe la dinámica en términos de posiciones y momentos generalizados.

## 5.1 Transformación de Legendre
A partir del Lagrangiano:

$$
p_j = \frac{\partial L}{\partial \dot{q}_j}
$$

se define el Hamiltoniano:

$$
H(q,p,t) = \sum_j p_j \dot{q}_j - L
$$

Para sistemas conservativos:

$$
H = T + V = E
$$

## 5.2 Ecuaciones de Hamilton
La dinámica está dada por:

$$
\dot{q}_j = \frac{\partial H}{\partial p_j}, \qquad
\dot{p}_j = -\frac{\partial H}{\partial q_j}
$$

Ventajas:

- forma canónica elegante,
- simetría entre coordenadas y momentos,
- prepara el terreno para la mecánica cuántica,
- natural en espacios de fase.

## 5.3 Paréntesis de Poisson
La evolución temporal de cualquier observable es:

$$
\dot{f} = \{f, H\} + \frac{\partial f}{\partial t}
$$

Con:

$$
\{f,g\} = \sum_{j=1}^n
\left(
\frac{\partial f}{\partial q_j}\frac{\partial g}{\partial p_j} -
\frac{\partial f}{\partial p_j}\frac{\partial g}{\partial q_j}
\right)
$$

Reglas fundamentales:

$$
\{q_i,p_j\} = \delta_{ij},\qquad
\{q_i,q_j\}=0,\qquad
\{p_i,p_j\}=0
$$

---

# 6. Fuerzas Centrales

Un sistema tiene fuerza central si:

$$
\vec{F}(r) = F(r)\,\hat{r}
$$

## 6.1 Consecuencias inmediatas
- El momento angular se conserva:
  $$
  \vec{L} = \vec{r} \times \vec{p} = \text{constante}
  $$
- El movimiento se reduce a un **plano**.
- La dinámica radial es equivalente a un sistema unidimensional con un potencial efectivo.

## 6.2 Potencial efectivo
$$
V_{\text{eff}}(r)= V(r)+\frac{L^2}{2mr^2}
$$

Permite clasificar:

- órbitas circulares,
- órbitas cerradas (elípticas),
- trayectorias abiertas (parabólicas/hiperbólicas).

## 6.3 Ecuación de Binet
Usando $u = 1/r$:

$$
\frac{d^2u}{d\phi^2} + u = -\frac{m}{L^2}\frac{d}{du}V(1/u)
$$

Clave para resolver órbitas de potencias y el potencial de Kepler.

---

# 7. Scattering (Dispersión)

El scattering estudia el desvío de una partícula al atravesar un potencial central.

## 7.1 Parámetro de impacto y ángulo de dispersión
El parámetro de impacto $b$ y el ángulo de dispersión $theta$ están relacionados por:

$$
\theta = \pi - 2\int_{r_{\min}}^\infty
\frac{b\; dr}{r^2\sqrt{1 - \frac{b^2}{r^2} - \frac{2V(r)}{E}}}
$$

## 7.2 Sección eficaz diferencial
$$
\frac{d\sigma}{d\Omega} = \frac{b}{\sin\theta}\left|\frac{db}{d\theta}\right|
$$

### Caso clásico: Dispersión de Rutherford
Si
$$
V(r) = \frac{\alpha}{r},
$$
entonces:
$$
\frac{d\sigma}{d\Omega} =
\left(\frac{\alpha}{2mv_0^2}\right)^2 \frac{1}{\sin^4(\theta/2)}
$$

---

# 8. Pequeñas Oscilaciones

Para un sistema con equilibrio estable $q_i=q_{i0}$:

$$
\left.\frac{\partial V}{\partial q_i}\right|_{q_{i0}}=0
$$

## 8.1 Expansión cuadrática del potencial
$$
V \approx V_0 + \frac12 \sum_{ij} k_{ij}\eta_i\eta_j
$$

Con:

$$
\eta_i = q_i - q_{i0}
$$

## 8.2 Energía cinética
$$
T = \frac12 \sum_{ij} m_{ij}\dot{\eta}_i\dot{\eta}_j
$$

## 8.3 Ecuación matricial de oscilación
$$
M\ddot{\eta}+K\eta = 0
$$

Solución → Problema de autovalores:

$$
\det(K - \omega^2 M) = 0
$$

Los autovectores describen **modos normales**, y los autovalores $\omega^2$ son las **frecuencias normales**.

## 8.4 Diagonalización del Lagrangiano
Las coordenadas normales $Q_i$ permiten:

$$
L = \frac12\sum_i (\dot{Q}_i^2 - \omega_i^2 Q_i^2)
$$

Cada modo es un **oscilador armónico independiente**.

---

# 9. Conclusiones generales

- El formalismo lagrangiano y hamiltoniano proporcionan visiones profundas y simétricas de la dinámica.  
- Las fuerzas centrales permiten estudiar órbitas, estabilidad y dispersión.  
- El scattering muestra cómo las partículas interactúan sin colisionar.  
- Las pequeñas oscilaciones explican modos colectivos de vibración en sistemas desde moléculas hasta estrellas.

---

# 10. Bibliografía Sugerida

- Fetter and Walecka - *Theorical mechanics of particles and continua*
- L. Landau & E. Lifshitz — *Mechanics*  
- W. Hauser - *Introduction to the principles of mechanics*
- H. Goldstein — *Classical Mechanics*  
- Marion & Thornton — *Classical Dynamics of Particles and Systems*






