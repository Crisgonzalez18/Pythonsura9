import pandas as pd

tablaEmpleados= pd.read_csv('./empleados (1).csv')

#print(tablaEmpleados)

#print(tablaEmpleados.to_string())

#Filtro 1 quiero obtener datos de los analistas 1
'''
tablaAnalistas1= tablaEmpleados[tablaEmpleados['cargo']=='analista1'].head(50)
print(tablaAnalistas1)
archivoHTML= tablaAnalistas1.to_html()
archivoTEXTO= open("datosanalistas1.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

tablaAnalistas2= tablaEmpleados[tablaEmpleados['cargo']=='analista2'].head(50)
print(tablaAnalistas2)
archivoHTML2= tablaAnalistas2.to_html()
archivoTEXTO2= open("datosanalistas2.html","w")
archivoTEXTO2.write(archivoHTML2)
archivoTEXTO2.close()

'''
tablaAnalista3= (tablaEmpleados[(tablaEmpleados['salario']>5500000)&(tablaEmpleados['edad']<30)])
print(tablaAnalista3)
archivoHTML3= tablaAnalista3.to_html()
archivoTEXTO3= open("datosanalistas3.html","w")
archivoTEXTO3.write(archivoHTML3)
archivoTEXTO3.close()