# 📊 powerBI-classes

Dos proyectos desarrollados durante el curso **Inteligencia de Negocios con Power BI – Nivel Intermedio** (CONECO, jul–ago 2025).
 
---
 
## 📁 Contenido del repositorio
 
```
├── corp_trimestral/
│   └── corp_trimestral.pbix
├── supercars/
│   ├── Cars_Datasets_2025.csv
│   ├── Cars_Datasets_2025_clean.csv
│   ├── Cars_Datasets_2025_final.csv
│   ├── script1_limpieza_original.py
│   ├── script2_validacion_clean.py
│   └── supercars.pbix
└── README.md
```
 
---
 
## 🏢 Proyecto 1 — Corp Trimestral Dashboard
 
Reporte de ventas 2021–2022 segmentado por vendedor, línea de producto y región (Perú).
 
**Stack:** Power Query · Modelo estrella · DAX
 
**Highlights:**
- Lima concentra el **87%** de ventas totales (S/ 170,997,982)
- Top vendedor: **Juan Mejía** con S/ 60,032,093
- Línea dominante: **Cómputo** en todas las regiones
 
🔗 [Ver en Power BI Service](https://app.powerbi.com/view?r=eyJrIjoiY2EyYzE2ZjItYWJmMS00MzdjLWFjOTEtZGFjZjkzZTQwNDY5IiwidCI6ImNjY2UyZTE1LWRjZTgtNDk2MS04YzNlLWM1MzQ2MWIyOTE2NCJ9)
 
---
 
## 🚗 Proyecto 2 — Supercars Explorer
 
Explorador interactivo del dataset [Cars Datasets 2025](https://www.kaggle.com/datasets/abdulmalik1518/cars-datasets-2025) de Kaggle.
 
**Stack:** Python (pandas · re) → Power BI
 
**KPIs principales:** Precio · Potencia (HP) · Aceleración 0–100
 
**Pipeline de limpieza:**
 
```python
# Extrae el primer número de strings como "70-85 hp" o "1,200 cc"
def extract_first_number(val):
    m = re.search(r"[\d,]+\.?\d*", str(val).strip())
    return float(m.group().replace(",", "")) if m else None
```
 
Los scripts transforman 6 columnas con unidades mezcladas en texto a valores numéricos limpios, eliminan duplicados y validan rangos lógicos antes de cargar a Power BI.
 
🔗 [Ver en Power BI Service](https://app.powerbi.com/view?r=eyJrIjoiZmNjZTc3ZWEtMTZiYi00OTk1LWEwODItOWNiM2YxYmRmY2FjIiwidCI6ImNjY2UyZTE1LWRjZTgtNDk2MS04YzNlLWM1MzQ2MWIyOTE2NCJ9)
 
---
 
## 🛠️ Tecnologías
 
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)
 
---
 
## 📖 Documentación completa
 
¿Quieres ver el proceso detallado, los hallazgos y el razonamiento detrás de cada decisión?
 
**👉 [Lee el artículo completo en omargpax.vercel.app](https://omargpax.vercel.app/post/power-bi-intermedio-cars-corp)**
 
