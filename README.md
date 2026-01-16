# 📊 Control de Inventarios (Python)

Este proyecto desarrolla una solución automatizada para la conciliación de stock y el análisis de eficiencia operativa de la **Red de Salud Tacna**. Utiliza Python para transformar registros administrativos complejos en indicadores clave de desempeño (KPIs).

## 🎯 Objetivo del Proyecto
Optimizar la trazabilidad de insumos médicos mediante el procesamiento de grandes volúmenes de datos, asegurando la integridad de la información y midiendo los tiempos de respuesta del almacén (Lead Time).

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías:** * `Pandas`: Limpieza y manipulación de datos.
    * `Matplotlib` / `Seaborn`: Visualización de métricas y dashboards.
* **Paradigma:** Programación Orientada a Objetos (POO).
* **Entorno:** Google Colab / Local.

## 📖 Diccionario de Datos y Reglas de Negocio
Para asegurar la precisión del análisis, el sistema aplica las siguientes definiciones lógicas:

| Columna | Definición | Regla de Negocio Aplicada |
| :--- | :--- | :--- |
| **N_COMPRA** | Orden de Compra (OC) | Llave de trazabilidad; vincula ingresos con salidas específicas. |
| **EST1** | Estado de Atención | **1**: Atendido (se descuenta stock) / **0**: Pendiente (se ignora). |
| **FECHA_C** | Fecha de Emisión | Fecha origen del requerimiento. |
| **FECHA2** | Fecha de Entrega | Fecha efectiva de salida para el cálculo de eficiencia. |
| **CANT_AG** | Cantidad Egresada | Unidades físicas entregadas por el almacén. |

## 🚀 Funcionalidades Principales
1. **Cálculo de Stock por Trazabilidad:** Cruce de información mediante múltiples llaves (`ITEM` + `N_COMPRA`) para evitar duplicidad o errores de saldo.
2. **Análisis de Lead Time:** Medición de días transcurridos entre la emisión y la atención del pedido.
3. **Módulo de Data Quality:** Detección automática de inconsistencias (ej. fechas de salida anteriores a las de emisión) para limpieza de datos.
4. **Dashboard de Gestión:** Visualización del estado de pedidos y alertas de productos críticos (Top 10 reabastecimiento).

## 📈 Visualizaciones
El sistema genera automáticamente:
* **Gráfico de Eficiencia:** Porcentaje de pedidos atendidos vs. pendientes.

## 📁 Estructura del Repositorio
* `inventario_stock.py`: Script principal bajo paradigma POO.
* `data_almacen.xlsx`: Dataset utilizado para el análisis (Ingresos y Salidas).
* `REPORTE_FINAL.xlsx`: Output generado con el stock conciliado y métricas.

---

