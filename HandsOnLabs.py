#!/usr/bin/env python
# coding: utf-8

# In[99]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df= pd.read_csv("C:/Users/tecnica911/Desktop/CARO/AB_NYC_2019.csv", sep = ",")


# In[100]:


#imprimir las primeras 5 filas
df.head()


# In[101]:


#imprimir las ultimas 5 filas
df.tail() 


# In[102]:


#dimensiones del dataset
print(df.shape)


# In[103]:


#Obtener la totalidad de registros por columnas-->analizar valores missing (los datos que no se poseen en el df)
df.count()


# In[135]:


#info
df.info()


# In[104]:


df.dtypes #verificar el tipo de datos


# In[105]:


#verificar la estructura del dataset
type(df)


# In[106]:


#Listar los nombres de las columnas del dataset
print(df.columns)


# In[ ]:


#completar valores missing
#df.fillna({'columna a completar': 0}, inplace = True)


# In[ ]:


#para filtrar datos
#df[df['price']<100]


# In[ ]:


#Listado de los 10 alojamientos con mayor cantidad de review o mas visitados
#df.nlargest(10, 'number_of_reviews')


# In[ ]:


#10 mejores datos segun frecuencia de aparicion
#df['neighbourhood o datos a solicitar de columna'.value_counts().head(10)]


# In[148]:


#x=todas las variables que no sean mi target, y= es el target
X= df.drop("price", axis=1) #drop se utiliza para eliminar datos de una columna, axis es por donde lo hace. inplace = True sirve para sobreescribir el objeto
y=df.price


# In[149]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


# In[150]:


from sklearn.tree import DecisionTreeClassifier
tree= DecisionTreeClassifier(max_depth=2, random_state=42) #max_depth es el nivel de profundidad. La semilla es la reproducibilidad, para que de el mismo resultado


# In[151]:


tree.fit(X_train, y_train) #Entrenar el modelo


# In[152]:


y_train_pred = tree.predict(X_train) #prediccion en train
y_test_pred = tree.predict(X_test) #prediccion en test. Esto se realiza para saber si predicen parecidos los dos.


# In[153]:


from sklearn.metrics import accuracy_score #medir la bondad de un modelo
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)
print('% de aciertos sobre el set de entrenamiento:', train_accuracy)
print('% de acietos sobre el set de evaluacion:', test_accuracy)


# In[154]:


import seaborn as sns
import matplotlib.pyplot as plt

# Suponiendo que ya has definido 'importances' y 'columns'

# Crea un gráfico de barras
sns.barplot(x=columns, y=importances)
plt.title('Importancias')
plt.xticks(rotation=90)  # Rota las etiquetas del eje x en 90 grados para una mejor legibilidad si es necesario
plt.show()

#import seaborn as sns
#importances = tree.feature_importances_
#columns = X.columns
#sns.barplot(columns, importances)
#plt.title('importancias')
#plt.show()

