
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# archivo CSV
df = pd.read_csv("covid19_tweets.csv")

# Definir las columnas numéricas a analizar
numerical_columns = ["user_followers", "user_friends", "user_favourites"]

# Crear un boxplot para cada columna numérica
for column in numerical_columns:
    plt.figure(figsize=(8, 6))  # Definir el tamaño de la figura
    sns.boxplot(data=df, y=column)  # Crear un boxplot
    plt.title(f"Boxplot de {column} del conjunto de datos de Tweets sobre COVID-19")  # Título del gráfico
    plt.ylabel("Cantidad")  # Etiqueta del eje Y
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Añadir rejilla al gráfico
    plt.show()  # Mostrar el gráfico

# Crear histogramas para las columnas numéricas
sns.histplot(df['user_followers'], bins=20, kde=False, color='blue')
plt.xlabel('Número de Seguidores')
plt.ylabel('Frecuencia')
plt.title('Histograma de Seguidores de Usuario')
plt.show()

sns.histplot(df['user_friends'], bins=20, kde=False, color='green')
plt.xlabel('Número de Amigos')
plt.ylabel('Frecuencia')
plt.title('Histograma de Amigos de Usuario')
plt.show()

sns.histplot(df['user_favourites'], bins=20, kde=False, color='orange')
plt.xlabel('Número de Favoritos')
plt.ylabel('Frecuencia')
plt.title('Histograma de Favoritos de Usuario')
plt.show()

# Seleccionar solo las columnas numéricas del dataframe
numeric_df = df.select_dtypes(include='number')

# Calcular la matriz de correlación de las columnas numéricas
corr_matrix = numeric_df.corr()

# Visualizar la matriz de correlación usando un mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=.5, fmt=".2f")
plt.title('Mapa de Calor de Correlación')
plt.show()
