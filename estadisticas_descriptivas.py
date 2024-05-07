import pandas as pd

def estadisticas_region(df, region):
    # Filtrar los datos por región
    datos_region = df[df['region'] == region]
    
    # Calcular estadísticas
    produccion_total = datos_region['Total Volume'].sum()
    precio_promedio = datos_region['AveragePrice'].mean()
    precio_std = datos_region['AveragePrice'].std()
    total_bags = datos_region[['Small Bags', 'Large Bags', 'XLarge Bags']].sum().sum()
    
    # Verificar que total_bags no sea cero para evitar división por cero
    if total_bags > 0:
        porcentaje_small = (datos_region['Small Bags'].sum() / total_bags) * 100
        porcentaje_large = (datos_region['Large Bags'].sum() / total_bags) * 100
        porcentaje_xlarge = (datos_region['XLarge Bags'].sum() / total_bags) * 100
    else:
        porcentaje_small = porcentaje_large = porcentaje_xlarge = 0

    # Imprimir resultados
    print(f"Estadísticas para {region}:")
    print(f"Producción Total: {produccion_total}")
    print(f"Precio Promedio: {precio_promedio:.2f} si hay datos suficientes")
    print(f"Desviación Estándar del Precio: {precio_std:.2f} si hay datos suficientes")
    print(f"Porcentaje de Bolsas Pequeñas: {porcentaje_small:.2f}%")
    print(f"Porcentaje de Bolsas Grandes: {porcentaje_large:.2f}%")
    print(f"Porcentaje de Bolsas Extragrandes: {porcentaje_xlarge:.2f}%")
    print("\n")

# Archivo CSV
df = pd.read_csv('avocado_full.csv')

# Mostrar todas las regiones únicas en el dataset con el fin de que no se omita ninguna region
print("Regiones disponibles en el dataset:")
print(df['region'].unique())

# Listado de regiones para análisis
regiones = ['NewYork', 'California', 'Charlotte']

# función de estadísticas para cada región
for region in regiones:
    estadisticas_region(df, region)
