# Carlos Javier Ramos Martinez
def calcular_promedio(temps):
    return sum(temps) / len(temps)

def temperaturas_fuera_rango(temps, min_limite, max_limite):
    return [t for t in temps if t < min_limite or t > max_limite]

def crear_informe(temps):
    total = len(temps)
    promedio = calcular_promedio(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    
    informe = (
        f"Reporte de Temperaturas:\n"
        f"Total de registros: {total}\n"
        f"Promedio de temperatura: {promedio:.2f}\n"
        f"Temperatura más alta: {max_temp}\n"
        f"Temperatura más baja: {min_temp}\n"
    )
    
    return informe

# Lista de temperaturas de ejemplo
temperaturas = [22.5, 23.0, 21.8, 22.3, 22.9, 23.1, 22.8]

# Calcular y mostrar el promedio de las temperaturas
promedio = calcular_promedio(temperaturas)
print(f"El promedio de las temperaturas es: {promedio}")

# Identificar y mostrar las temperaturas fuera del rango especificado
fuera_rango = temperaturas_fuera_rango(temperaturas, 22.0, 23.0)
print(f"Las temperaturas fuera del rango 22.0 a 23.0 grados Celsius son: {fuera_rango}")

# Generar y mostrar el informe de temperaturas
informe = crear_informe(temperaturas)
print(informe)