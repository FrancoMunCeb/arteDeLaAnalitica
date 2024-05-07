# Aguactes de las vegas 
#Autor A01655440

import pandas as pd
from tabulate import tabulate

# el archivo CSV
df = pd.read_csv('avocado_full.csv')

# Filtrar los datos para obtener solo los registros de aguacates de Las Vegas
aguacates_las_vegas = df[df['region'] == 'Las Vegas']

# resulatdos en formato
print(tabulate(aguacates_las_vegas, headers='keys', tablefmt='psql', showindex=False))