#Exercice 1 :

import numpy as np
week1_sleep=[6,7,8,5,9]
week2_sleep=[7,6,8,7,6]
days_vector=["Monday","Tuesday","Wednesday","Thursday","Friday"]
daily_difference=np.array(week2_sleep)-np.array(week1_sleep)
total_week1=0
for i in week1_sleep :
    total_week1+=i
total_week2=0
for i in week2_sleep :
    total_week2+=i
average_week1=total_week1/len(week1_sleep)
average_week2=total_week2/len(week2_sleep)
slept_more_first_week=average_week1>average_week2

#la valeur de slept_more_first_week est True donc c'est la premiere semaine
for i in range(len(days_vector)) :
    if days_vector[i]=="Wednesday" :
        sleep_wednesday_week1=week1_sleep[i]
midweek_sleep_week2=[]
for i in range(len(days_vector)) :
      if days_vector[i] in ["Tuesday","Wednesday","Thursday"] :
          midweek_sleep_week2.append(week2_sleep[i])
sleep_enough_week1=[]
for i in week1_sleep :
    sleep_enough_week1.append(i>=8)
sleep_succeful_days_week1=[]
for i in week1_sleep :
    if i>=8 :
        sleep_succeful_days_week1.append(i)

#Exercice 2 :

import numpy as np
import pandas as pd
df=pd.read_excel("C:\\Users\\hp\\Downloads\\Feuille de calcul sans titre.xlsx")
x=df.head()
print(x)
# only the scores are numerical
print("Ce dataset presente :")
print(df.info())
print("Voici quelque information sur la Data :\n",df.describe())
print(df.sample(10))

import matplotlib.pyplot as plt
import seaborn as sns
df["math score"].hist(bins=10)
plt.show()

df["reading score"].hist(bins=10)
plt.show()

df["writing score"].hist(bins=10)
plt.show()

sns.boxplot(x='gender', y='math score', data=df)
plt.show()

plt.scatter(df['math score'], df['reading score'])
plt.show()

correlation_mx = df[['math score', 'reading score', 'writing score']].corr()
sns.heatmap(correlation_mx)
plt.show()
