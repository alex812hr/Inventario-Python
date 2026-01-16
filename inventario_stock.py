import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración estética de los gráficos
sns.set_theme(style="whitegrid")


class AuditoriaInventarioLocal:
    def __init__(self, ruta_excel):
        self.ruta_excel = ruta_excel
        self.df_stock = None
        self.df_salidas = None
        self.reporte_operativo = {}

    def procesar(self):
        print(f"🔄 Procesando archivo: {self.ruta_excel}...")

        # 1. Cargar las hojas del Excel local
        try:
            # Es necesario tener instalada la librería 'openpyxl' (pip install openpyxl)
            ing = pd.read_excel(self.ruta_excel, sheet_name='INGRESOS')
            sal = pd.read_excel(self.ruta_excel, sheet_name='SALIDAS')
        except Exception as e:
            print(f"❌ Error al leer el Excel: {e}")
            return False

        # 2. Tratamiento de Fechas y Filtro de Atendidos
        sal['FECHA_C'] = pd.to_datetime(sal['FECHA_C'])
        sal['FECHA2'] = pd.to_datetime(sal['FECHA2'])

        # Calculamos días de atención solo para registros con EST1 == 1
        sal['DIAS_ATENCION'] = (sal['FECHA2'] - sal['FECHA_C']).dt.days
        self.df_salidas = sal.copy()

        # 3. Lógica de Trazabilidad (ITEM + N_COMPRA)
        # Solo descontamos lo atendido (EST1 == 1)
        df_sal_atendidas = sal[sal['EST1'] == 1].groupby(['ITEM', 'N_COMPRA'])['CANT_AG'].sum().reset_index()
        df_ing_total = ing.groupby(['ITEM', 'PRODUCTO', 'N_COMPRA'])['CANT_INGRESADA'].sum().reset_index()

        # Unir para obtener el stock actual por Orden de Compra
        self.df_stock = pd.merge(df_ing_total, df_sal_atendidas, on=['ITEM', 'N_COMPRA'], how='left').fillna(0)
        self.df_stock['STOCK_ACTUAL'] = self.df_stock['CANT_INGRESADA'] - self.df_stock['CANT_AG']

        # 4. Hallar la Orden de Compra (OC) más rápida
        oc_atendidas = sal[sal['EST1'] == 1].dropna(subset=['DIAS_ATENCION'])
        if not oc_atendidas.empty:
            oc_rapidas = oc_atendidas.groupby('N_COMPRA')['DIAS_ATENCION'].mean().sort_values()
            self.reporte_operativo['mejor_oc'] = oc_rapidas.index[0]
            self.reporte_operativo['mejor_tiempo'] = oc_rapidas.values[0]

        return True

    def generar_reporte_visual(self):
        if self.df_stock is None: return

        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        # Gráfico 1: Estado de Pedidos
        estados = self.df_salidas['EST1'].value_counts()
        axes[0].pie(estados, labels=['Atendidos', 'Pendientes'], autopct='%1.1f%%', colors=['#4CAF50', '#FF5252'],
                    startangle=140)
        axes[0].set_title('Eficiencia de Atención (Estado de Pedidos)')

        # Gráfico 2: Top 10 Productos con mayor Stock
        top_stock = self.df_stock.sort_values('STOCK_ACTUAL', ascending=False).head(10)
        sns.barplot(ax=axes[1], x='STOCK_ACTUAL', y='PRODUCTO', data=top_stock, palette='viridis')
        axes[1].set_title('Top 10 Productos con Mayor Stock Disponible')

        plt.tight_layout()
        plt.show()

    def exportar_resultados(self):
        nombre_salida = 'REPORTE_FINAL_LOCAL.xlsx'
        self.df_stock.to_excel(nombre_salida, index=False)
        print(f"✅ Reporte exportado exitosamente como: {nombre_salida}")


# --- INICIO DEL SCRIPT ---
if __name__ == "__main__":
    # AQUÍ PON EL NOMBRE DE TU ARCHIVO EXCEL (debe estar en la misma carpeta que el script)
    archivo_excel = '/Users/alexander/Desktop/PROJECT_BCP.xlsx'

    if os.path.exists(archivo_excel):
        auditor = AuditoriaInventarioLocal(archivo_excel)
        if auditor.procesar():
            print(f"\n🏆 OC MÁS RÁPIDA: #{auditor.reporte_operativo.get('mejor_oc')}")
            print(f"⏱️ Tiempo promedio: {auditor.reporte_operativo.get('mejor_tiempo'):.2f} días")

            auditor.generar_reporte_visual()
            auditor.exportar_resultados()
    else:
        print(f"❌ No se encontró el archivo '{archivo_excel}' en esta carpeta.")

