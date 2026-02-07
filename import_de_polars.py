import polars as pl
import pandas as pd  # Para comparar

# =============================================================================
# 1. CREAR DATAFRAMES
# =============================================================================
print("1. CREAR DATAFRAMES")
print("=" * 60)

# POLARS: Crear DataFrame desde un diccionario
df_polars = pl.DataFrame({
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Elena'],
    'edad': [25, 30, 28, 35, 27],
    'ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Valencia', 'Barcelona'],
    'salario': [30000, 45000, 38000, 52000, 41000]
})

print("\nDataFrame en Polars:")
print(df_polars)

# Para comparar con Pandas (sintaxis similar)
df_pandas = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Elena'],
    'edad': [25, 30, 28, 35, 27],
    'ciudad': ['Madrid', 'Barcelona', 'Huesca', 'Valencia', 'Murcia'],
    'salario': [30000, 45000, 38000, 52000, 41000]
})
print("\nDataFrame en Pandas:")
print(df_pandas)
