import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Cargar datos
df = pd.read_csv("covid19_tweets.csv")

# Definir las columnas numéricas a analizar
numerical_columns = ["user_followers", "user_friends", "user_favourites"]

# Crear un boxplot para cada columna numérica
for column in numerical_columns:
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, y=column)
    plt.title(f"Boxplot de {column} del conjunto de datos de Tweets sobre COVID-19")
    plt.ylabel("Cantidad")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Crear histogramas para las columnas numéricas
for column in numerical_columns:
    sns.histplot(df[column], bins=20, kde=False)
    plt.xlabel(f'Número de {column}')
    plt.ylabel('Frecuencia')
    plt.title(f'Histograma de {column}')
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

# Preparar datos para clustering
features = df[numerical_columns].dropna()
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Método del codo para determinar el valor de k
inertia = []
k_values = range(1, 10)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(k_values, inertia, marker='o')
plt.title('Método del Codo para Determinar K')
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inertia')
plt.show()

# Determinar el número óptimo de clusters
k_optimo = 3  # Asumiendo que después de revisar el método del codo decidimos este valor

# Aplicar K-means con el número óptimo de clusters
kmeans = KMeans(n_clusters=k_optimo, random_state=42)
clusters = kmeans.fit_predict(features_scaled)
features['Cluster'] = clusters

# Obtener los centros de los clusters
centros = kmeans.cluster_centers_
print("Centros de los clusters:\n", centros)

# Visualizar los resultados del clustering
plt.figure(figsize=(10, 6))
sns.scatterplot(x=features_scaled[:,0], y=features_scaled[:,1], hue=clusters, palette='viridis')
plt.title('Clustering K-means de Seguidores vs. Amigos')
plt.xlabel('Seguidores (escalados)')
plt.ylabel('Amigos (escalados)')
plt.show()
