# ============================================================
# SCRIPT 1: Limpieza del dataset Cars_Datasets_2025.csv
# Autor: Claude / Anthropic  |  Fecha: 2026
# Input:  Cars_Datasets_2025.csv
# Output: Cars_Datasets_2025_clean.csv
# ============================================================

import pandas as pd
import re

####################################################################
# SECCIÓN 1 — Carga del archivo
####################################################################

df = pd.read_csv('Cars_Datasets_2025.csv', encoding='latin1')
print(f'Filas cargadas: {len(df)}')
print('Columnas originales:', df.columns.tolist())

####################################################################
# SECCIÓN 2 — Limpieza de espacios
####################################################################

# Quitar espacios en nombres de columnas
df.columns = df.columns.str.strip()

# Quitar espacios en todas las columnas de texto
for col in df.select_dtypes(include=['object', 'str']).columns:
    df[col] = df[col].str.strip()

####################################################################
# SECCIÓN 3 — Columnas de texto a mayúsculas
####################################################################

text_cols = ['Company Names', 'Cars Names', 'Engines', 'Fuel Types']
for col in text_cols:
    df[col] = df[col].str.upper()

####################################################################
# SECCIÓN 4 — Helper: extraer primer número de un string
####################################################################

def extract_first_number(val):
    """Extrae el primer valor numérico de un string.
    Ej: '70-85 hp' → 70.0 | '1,200 cc' → 1200.0
    """
    if pd.isna(val):
        return val
    val = str(val).strip()
    m = re.search(r'[\d,]+\.?\d*', val)
    if m:
        return float(m.group().replace(',', ''))
    return None

####################################################################
# SECCIÓN 5 — Columnas numéricas: renombrar + limpiar unidades
####################################################################

# CC / Battery Capacity → numeric (cc)
df['CC/Battery Capacity (cc)'] = df['CC/Battery Capacity'].apply(extract_first_number)
df.drop(columns=['CC/Battery Capacity'], inplace=True)

# HorsePower → numeric (hp)
df['HorsePower (hp)'] = df['HorsePower'].apply(extract_first_number)
df.drop(columns=['HorsePower'], inplace=True)

# Total Speed → numeric (km/h)
df['Total Speed (km/h)'] = df['Total Speed'].apply(extract_first_number)
df.drop(columns=['Total Speed'], inplace=True)

# Performance → numeric (sec)
df['Performance 0-100 (sec)'] = df['Performance(0 - 100 )KM/H'].apply(extract_first_number)
df.drop(columns=['Performance(0 - 100 )KM/H'], inplace=True)

# Cars Prices → numeric (USD)
def clean_price(val):
    if pd.isna(val):
        return val
    val = str(val).strip().replace('$', '').replace(',', '').replace(' ', '')
    m = re.search(r'[\d]+\.?\d*', val)
    return float(m.group()) if m else None

df['Cars Prices (USD)'] = df['Cars Prices'].apply(clean_price)
df.drop(columns=['Cars Prices'], inplace=True)

# Torque → numeric (Nm)
df['Torque (Nm)'] = df['Torque'].apply(extract_first_number)
df.drop(columns=['Torque'], inplace=True)

####################################################################
# SECCIÓN 6 — Reordenar columnas y guardar
####################################################################

col_order = [
    'Company Names', 'Cars Names', 'Engines',
    'CC/Battery Capacity (cc)', 'HorsePower (hp)',
    'Total Speed (km/h)', 'Performance 0-100 (sec)',
    'Cars Prices (USD)', 'Fuel Types', 'Seats', 'Torque (Nm)'
]
df = df[col_order]

df.to_csv('Cars_Datasets_2025_clean.csv', index=False)
print('✅ Archivo guardado: Cars_Datasets_2025_clean.csv')
print(df.head(3).to_string())
