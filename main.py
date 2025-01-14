import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn as sb

IMDBcsv=pd.read_csv("IMDB Dataset.csv")
IMDBdf=pd.DataFrame(IMDBcsv)

#print(IMDBdf.info())
#print(IMDBdf.isnull().sum())

#print(IMDBdf.head(3))
#print(IMDBdf.tail(3))
#print(IMDBdf.max())

subset=IMDBdf.iloc[:42, 76:]
#print(subset)

#plt.figure(figsize=(10,10))
#sb.boxplot(y="Runtime",x="IMDB_Rating",data=IMDBdf,palette="pastel")
#plt.show()

#plt.figure(figsize=(10,10))
#sb.countplot(hue="Series_Title",data=IMDBdf,x="IMDB_Rating",palette="pastel")
#plt.show()

plt.figure(figsize=(10,10))
sb.countplot(data=IMDBdf,x="IMDB_Rating",palette="pastel")
plt.show()