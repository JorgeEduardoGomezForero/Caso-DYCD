# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 10:28:45 2021

@author: Jorge Eduardo Gomez Forero
"""

import numpy as np
import pandas as pd
import pandas_profiling
from seaborn import load_dataset

#ruta de trabajo
ruta = 'C:/03_Jorge/04_Personal/Caso_DYCD/'

#Lee el archivo de excel
file_excel=pd.ExcelFile(ruta + '10_db_prueba_DYCD.xlsx')


# Se pasa a un dataframe y se coloca el nombre de la hoja con la que se va ha trabajar.
db_report_Tot=file_excel.parse('db_Ajus')

#Nombre de las Columnas que se encuentran en la hoja seleccionada y que se van a excluir dado
#que no toda su informaciòn se encuentra con valor igual a cero o corresponden a datos del cliente
#a los cuales no es necesario realizar estudio de estadistica descriptiva.
db_report_Tot =db_report_Tot.drop(['NumeroIdentificacion','NombreCliente','NumeroTelefono1','NumeroTelefono2',
                      'NumeroTelefono3','Celular1','Celular2','Direccion1','Email1','Email2',
                      'SaldoCapital','VrGarantiaActual','TasaTarjeta','TasaAutoEfectivo',
                      'TasaVehiculos','P_Edad','Politica_Ingresos','AciertaA_Ins','AciertaA_TDC',
                      'Cierre','CondicionDesercion','FechaUltimoMovimiento'],axis=1)

#Genera base discriminada por producto.
#Importante: dado que Libranza solo presenta un caso, se incluyo en la base de Libre Inversión
db_report_Veh = db_report_Tot[db_report_Tot['Producto'] == 'vehiculo']
db_report_LInv = db_report_Tot[db_report_Tot['Producto'] != 'vehiculo']

db_report_Veh =db_report_Veh.drop(['Producto'],axis=1)
db_report_LInv =db_report_LInv.drop(['Producto'],axis=1)

db_report_Tot.head()
db_report_Tot.describe()
profile = pandas_profiling.ProfileReport(db_report_Tot,title='Exploración Clientes DYCD')
profile.to_file(output_file="21_PerilTotDYCD.html")

db_report_Veh.head()
db_report_Veh.describe()
profile = pandas_profiling.ProfileReport(db_report_Veh,title='Exploración Vehículo Clientes DYCD')
profile.to_file(output_file="22_PerilVehDYCD.html")

db_report_LInv.head()
db_report_LInv.describe()
profile = pandas_profiling.ProfileReport(db_report_LInv,title='Exploración Libre Inversión Clientes DYCD')
profile.to_file(output_file="23_PerfilLInvDYCD.html")

