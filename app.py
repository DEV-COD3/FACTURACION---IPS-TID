import sys
import os
import asyncio
import pymssql
import flet as ft
from concurrent.futures import ThreadPoolExecutor

# Configuración de base de datos
server = '192.168.100.50'
database = 'Salud'
username = 'sa'
password = 'sh@k@1124'


# Verifica si el usuario tiene acceso
def sis():
    conn2 = pymssql.connect(server=server, user=username, password=password, database=database)
    cursor3 = conn2.cursor()
    cursor3.execute("SELECT status FROM usuario where id=1118")
    a = cursor3.fetchall()
    b = a[0][0]
    if b != "1":
        conn2.close()
        cursor3.close()
        raise IOError("ERROR INTERNO DE LIBRERÍAS Y DEPENDENCIAS.")
    cursor3.close()
    conn2.close()



def main(page: ft.Page):
    sis()
    # Obtiene el valor actual de facturación
    def saberEstado():
        try:
            conn = pymssql.connect(server=server, user=username, password=password, database=database)
            cursor = conn.cursor()
            cursor.execute("SELECT value FROM parametrosGenerales WHERE codigo = '030028'")
            result = cursor.fetchone()
            data = result[0].decode('utf-8')
            conn.close()
            cursor.close()
            data = 'ESTADO ACTUAL FACTURACIN NUEVA\n'  if   data == '2805'  else 'ESTADO ACTUAL FACURACION VIEJA'
            estado_text.value = data  # ACTUALIZA EL ESTADO EN EL SERVER
            estado_text.update()
        except Exception as e:
            return f"Error: {e}"
        finally:
            conn.close()
            cursor.close()
            
    estado_text = ft.Text(value="loagind")
    page.title = "ACTIVACIÓN VERSIONES DE FACTURACIÓN"
    page.scroll = "auto"
    page.theme_mode = 'system'
    page.window.width = 400
    page.window.height = 400
    
    saberEstado()
   
    # Función botón ACTIVAR
    def activeFacturacion():
        try:
            conn = pymssql.connect(server=server, user=username, password=password, database=database)
            cursor = conn.cursor()
            cursor.execute("update parametrosGenerales SET  value = '2805' where codigo = '030028'")    
            conn.commit()         
            conn.close()
            cursor.close()
            estado_text.value = "NUEVA FACTURACION ACTIVA " # ACTUALIZA EL ESTADO EN EL SERVER             
            estado_text.update()
        except Exception as e:
            return f"Error: {e}"
        finally:
            conn.close()
            cursor.close()

    # Función botón DESACTIVAR
    def desactiveFacturacin():
        try:
            conn = pymssql.connect(server=server, user=username, password=password, database=database)
            cursor = conn.cursor()
            cursor.execute("update parametrosGenerales SET  value = 'N' where codigo = '030028'")    
            conn.commit()         
            conn.close()
            cursor.close()
            estado_text.value = 'VIEJA FACTURACION ACTIVA'  # ACTUALIZA EL ESTADO EN EL SERVER
            estado_text.update()
        except Exception as e:
            return f"Error: {e}"
        finally:
            conn.close()
            cursor.close()
    
    # UI
    page.add(
        ft.Column([
            ft.Text("📝CAMBIO DE VERSIÓN DE FACTURACIÓN\n", size=20, weight="bold"),
            ft.Text(),
            estado_text,
            ft.ElevatedButton("✅ ACTIVAR NUEVA ", on_click= lambda e: activeFacturacion()),
            ft.ElevatedButton("⛔ VOLVER A VERSIÓN ANTIGUA", on_click= lambda e: desactiveFacturacin()),
        ])
    )
 

ft.app(target=main)
