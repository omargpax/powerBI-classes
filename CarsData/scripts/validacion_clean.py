# ============================================================
# SCRIPT 2: Limpieza directa del CSV ya generado
#           (Cars_Datasets_2025_clean.csv)
# Aplica: validaciones, tipos correctos, nulos, exportación
# Input:  Cars_Datasets_2025_clean.csv
# Output: Cars_Datasets_2025_final.csv
# ============================================================

import pandas as pd
import numpy as np

####################################################################
# SECCIÓN 1 — Carga del archivo limpio
####################################################################

df = pd.read_csv('Cars_Datasets_2025_clean.csv')
print(f'Filas: {len(df)} | Columnas: {len(df.columns)}')
print(df.dtypes)

####################################################################
# SECCIÓN 2 — Verificar y forzar tipos de datos correctos
####################################################################

numeric_cols = [
    'CC/Battery Capacity (cc)', 'HorsePower (hp)',
    'Total Speed (km/h)', 'Performance 0-100 (sec)',
    'Cars Prices (USD)', 'Torque (Nm)'
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

str_cols = ['Company Names', 'Cars Names', 'Engines', 'Fuel Types', 'Seats']
for col in str_cols:
    df[col] = df[col].astype(str).str.strip().str.upper()

####################################################################
# SECCIÓN 3 — Reporte de nulos
####################################################################

nulls = df.isnull().sum()
print('\nNulos por columna:')
print(nulls[nulls > 0] if nulls.any() else '  Sin nulos ✅')

# Eliminar filas con más del 50% de columnas nulas
threshold = len(df.columns) * 0.5
df = df.dropna(thresh=threshold)

####################################################################
# SECCIÓN 4 — Eliminar duplicados
####################################################################

before = len(df)
df = df.drop_duplicates(subset=['Company Names', 'Cars Names'])
after = len(df)
print(f'\nDuplicados eliminados: {before - after}')

####################################################################
# SECCIÓN 5 — Validar rangos lógicos
####################################################################

# Velocidades deben ser > 0 y razonables (< 500 km/h)
invalid_speed = df[~df['Total Speed (km/h)'].between(0, 500, inclusive='right')]
if len(invalid_speed) > 0:
    print(f'⚠️  Velocidades fuera de rango: {len(invalid_speed)} filas')
    df = df[df['Total Speed (km/h)'].between(0, 500, inclusive='right') | df['Total Speed (km/h)'].isna()]

# Precios deben ser > 0
df = df[df['Cars Prices (USD)'].isna() | (df['Cars Prices (USD)'] > 0)]

####################################################################
# SECCIÓN 6 — Exportar resultado final
####################################################################

df.to_csv('Cars_Datasets_2025_final.csv', index=False)
print(f'\n✅ Exportado: Cars_Datasets_2025_final.csv  ({len(df)} filas)')
print('\nResumen estadístico:')
print(df[numeric_cols].describe().round(2).to_string())
