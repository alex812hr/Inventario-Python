# 📊 Inventario-Python

Este proyecto fue desarrollado para automatizar el control de stock de productos en la Red de Salud.

## 🚀 Funcionalidades
- **Trazabilidad Total:** Cruce de datos por Código de Item y Número de Orden de Compra (OC).
- **Lógica de Negocio:** Filtrado de transacciones basado en estados de atención (EST1).
- **Métricas de Eficiencia:** Cálculo automático del Lead Time (tiempo de respuesta) por cada pedido.
- **Visualización:** Generación de gráficos de stock crítico y eficiencia operativa.

## 🛠️ Tecnologías
- **Lenguaje:** Python
- **Librerías:** Pandas (Análisis de datos), Matplotlib/Seaborn (Visualización).
- **Paradigma:** Programación Orientada a Objetos (POO).

## 📖 Diccionario de Datos

Para este análisis se utilizaron reglas de negocio específicas basadas en la operativa real del almacén:

| Columna | Definición | Regla de Negocio Aplicada |
| :--- | :--- | :--- |
| **N_COMPRA** | Orden de Compra (OC) | Se utiliza como llave de trazabilidad para asegurar que el stock se descuente del lote correcto. |
| **EST1** | Estado de Atención | **1**: Pedido Atendido (se descuenta del stock). <br> **0**: Pedido Pendiente/No Atendido (se ignora en el cálculo). |
| **FECHA_C** | Fecha de Emisión | Fecha en la que se genera el documento de pedido. |
| **FECHA2** | Fecha de Salida | Fecha efectiva de entrega. Se usa para calcular el *Lead Time* de atención. |
| **CANT_AG** | Cantidad Egresada | Cantidad física que sale del almacén central. |
