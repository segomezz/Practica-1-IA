import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Variables y rangos
riesgo = ctrl.Antecedent(np.arange(0, 11, 1), 'riesgo')
rentabilidad = ctrl.Antecedent(np.arange(0, 21, 1), 'rentabilidad')
horizonte = ctrl.Antecedent(np.arange(0, 31, 1), 'horizonte')
recomendacion = ctrl.Consequent(np.arange(0, 11, 1), 'recomendacion')
recomendacion.defuzzify_method = 'centroid'

# 2. Funciones de pertenencia

# Riesgo
riesgo['bajo'] = fuzz.trapmf(riesgo.universe, [0, 0, 2, 4])
riesgo['medio'] = fuzz.trimf(riesgo.universe, [3, 5, 7])
riesgo['alto'] = fuzz.trapmf(riesgo.universe, [6, 8, 10, 10])
riesgo['muy_alto'] = np.power(riesgo['alto'].mf, 2)
riesgo['casi_alto'] = np.sqrt(riesgo['alto'].mf)

# Rentabilidad
rentabilidad['baja'] = fuzz.gaussmf(rentabilidad.universe, 3, 2)
rentabilidad['media'] = fuzz.gaussmf(rentabilidad.universe, 10, 2)
rentabilidad['alta'] = fuzz.gaussmf(rentabilidad.universe, 17, 2)
rentabilidad['muy_alta'] = np.power(rentabilidad['alta'].mf, 2)
rentabilidad['ligeramente_alta'] = np.sqrt(rentabilidad['alta'].mf)
rentabilidad['extremadamente_alta'] = np.power(rentabilidad['alta'].mf, 3)

# Horizonte
horizonte['corto'] = fuzz.trimf(horizonte.universe, [0, 5, 10])
horizonte['medio'] = fuzz.trimf(horizonte.universe, [10, 15, 20])
horizonte['largo'] = fuzz.trimf(horizonte.universe, [20, 25, 30])
horizonte['muy_largo'] = np.power(horizonte['largo'].mf, 2)
horizonte['ligeramente_corto'] = np.sqrt(horizonte['corto'].mf)

# Recomendación
recomendacion['baja'] = fuzz.trimf(recomendacion.universe, [0, 2, 4])
recomendacion['aceptable'] = fuzz.trimf(recomendacion.universe, [3, 5, 7])
recomendacion['alta'] = fuzz.trimf(recomendacion.universe, [6, 8, 10])

# 3. Graficas funciones de pertenencia

def mostrar_funciones(var, nombre):
    plt.figure(figsize=(8, 4))
    for etiqueta in var.terms:
        plt.plot(var.universe, var[etiqueta].mf, label=etiqueta)
    plt.title(f'{nombre}')
    plt.xlabel(nombre)
    plt.ylabel('μ(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

mostrar_funciones(riesgo, 'riesgo')
mostrar_funciones(rentabilidad, 'rentabilidad')
mostrar_funciones(horizonte, 'horizonte')
mostrar_funciones(recomendacion, 'recomendacion')

# 4. Reglas 
rules = [
    ctrl.Rule(riesgo['bajo'] & rentabilidad['alta'], recomendacion['alta']),
    ctrl.Rule(riesgo['alto'] & rentabilidad['baja'], recomendacion['baja']),
    ctrl.Rule(riesgo['medio'] & rentabilidad['media'], recomendacion['aceptable']),
    ctrl.Rule(riesgo['bajo'] | horizonte['largo'], recomendacion['alta']),
    ctrl.Rule(riesgo['alto'] & horizonte['corto'], recomendacion['baja']),
    ctrl.Rule(~riesgo['alto'] & rentabilidad['alta'], recomendacion['alta']),
    ctrl.Rule(riesgo['medio'] & horizonte['medio'], recomendacion['aceptable']),
    ctrl.Rule(rentabilidad['baja'] & horizonte['largo'], recomendacion['aceptable']),
    ctrl.Rule(riesgo['alto'] | rentabilidad['alta'], recomendacion['aceptable']),
    ctrl.Rule(riesgo['bajo'] & rentabilidad['muy_alta'], recomendacion['alta']),
    ctrl.Rule(riesgo['medio'] & rentabilidad['ligeramente_alta'], recomendacion['aceptable']),
    ctrl.Rule(riesgo['bajo'] & horizonte['muy_largo'], recomendacion['alta']),
    ctrl.Rule(riesgo['muy_alto'] & horizonte['corto'], recomendacion['baja']),
    ctrl.Rule(rentabilidad['extremadamente_alta'] & riesgo['bajo'], recomendacion['alta']),
    ctrl.Rule(horizonte['ligeramente_corto'] & rentabilidad['media'], recomendacion['aceptable']),
    ctrl.Rule(riesgo['casi_alto'] & rentabilidad['media'], recomendacion['aceptable']),
    ctrl.Rule(horizonte['medio'] & rentabilidad['muy_alta'], recomendacion['alta']),
    ctrl.Rule(riesgo['bajo'] & rentabilidad['baja'], recomendacion['aceptable']),
]

# 5. Crear sistema y simular
sistema_ctrl = ctrl.ControlSystem(rules)
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Datos de prueba
sistema.input['riesgo'] = 3
sistema.input['rentabilidad'] = 18
sistema.input['horizonte'] = 12

sistema.compute()

def clasificar_recomendacion(valor):
    if valor < 3.5:
        return "Baja"
    elif valor < 6.5:
        return "Aceptable"
    else:
        return "Alta"

num = sistema.output['recomendacion']
categoria = clasificar_recomendacion(num)

print("Nivel de recomendacion:", round(num, 2))
print("Clasificacion:", categoria)

# string para Experta
hecho_para_experta = f"(nivel-recomendacion {categoria})"
print("Hecho para sistema experto:", hecho_para_experta)
