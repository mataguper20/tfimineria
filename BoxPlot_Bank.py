import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_csv('bank-additional.csv', encoding='ISO-8859-1', sep = ';')
plt.figure()
datos.boxplot()
plt.figure()
txt = ['age','duration','campaign','pdays','previous','emp.var.rate','cons.price.idx','cons.conf.idx','euribor3m','nr.employed']

for i in txt:
    plt.figure()
    datos.boxplot(column=[i])
    print("--------------------",i,"------------------------")
    print(datos.describe()[i])


txt=['duration','campaign','age']

print("ELIMINACIÓN DE DATOS")

for cols in txt:
    Q1 = datos[cols].quantile(0.25)
    Q3 = datos[cols].quantile(0.75)
    IQR = Q3 - Q1     
    print(Q1 - 1.5 * IQR," - ",Q3 + 1.5 * IQR)
    filter = (datos[cols] >= Q1 - 1.5 * IQR) & (datos[cols] <= Q3 + 1.5 *IQR)
    datos=datos.loc[filter]

txt=['age','campaign','duration']
for i in txt:
    plt.figure()
    datos.boxplot(column=[i])
    print("--------------------",i,"------------------------")
    print(datos.describe()[i])
