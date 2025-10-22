import numpy as np
import plotly.graph_objects as go
from scipy.integrate import solve_ivp

# Definimos parámetros físicos
q = 1.6e-19   # Carga del protón (C)
m = 1.67e-27  # Masa del protón (kg)
B = 1.0       # Campo magnético en Tesla
E_max = 1e3   # Campo eléctrico máximo (V/m)
f_cyclotron = (q * B) / (2 * np.pi * m)  # Frecuencia de ciclotrón

# Ecuaciones del movimiento
def ciclotron(t, y):
    x, y, z, vx, vy, vz = y
    # Campo eléctrico alternante en la brecha (aproximación simplificada)
    E = E_max * np.cos(2 * np.pi * f_cyclotron * t) if abs(x) < 0.01 else 0
    # Fuerza de Lorentz
    ax = (q / m) * (vy * B + E)
    ay = (q / m) * (-vx * B)
    az = 0  # No hay movimiento en z (idealización 2D en el plano XY)
    return [vx, vy, vz, ax, ay, az]

# Condiciones iniciales con menor velocidad para observar la trayectoria
y0 = [0.01, 0, 0, 0, 1e4, 0]  # Velocidad inicial reducida

# Simulación numérica
t_span = (0, 1e-6)  # Aumentamos el tiempo de simulación para mejor visualización
t_eval = np.linspace(*t_span, 2000)  # Mayor resolución temporal
sol = solve_ivp(ciclotron, t_span, y0, t_eval=t_eval)

# Gráfico 3D interactivo con Plotly
fig = go.Figure()

# Agregar la trayectoria completa en espiral
fig.add_trace(go.Scatter3d(x=sol.y[0], y=sol.y[1], z=sol.y[2],
                           mode='lines',
                           line=dict(color='blue', width=2),
                           name='Trayectoria'))

# Agregar el punto de inicio
fig.add_trace(go.Scatter3d(x=[sol.y[0][0]], y=[sol.y[1][0]], z=[sol.y[2][0]],
                           mode='markers',
                           marker=dict(color='red', size=5, symbol='circle'),
                           name='Inicio'))

# Configuración del gráfico
fig.update_layout(title='Simulación de un Ciclotrón en 3D',
                  scene=dict(xaxis_title='X (m)',
                             yaxis_title='Y (m)',
                             zaxis_title='Z (m)'),
                  margin=dict(l=0, r=0, b=0, t=40))

# Mostrar gráfico interactivo
fig.show()
