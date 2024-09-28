import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data=pd.read_csv(r"C:\Users\arohi\OneDrive\Desktop\Task_1\API_SP.POP.TOTL_DS2_en_csv_v2_3401680.csv",skiprows=4)
print(data.head())
print(data.columns)

population_2006=data['2006'].dropna()
plt.figure(figsize=(10,6))
plt.hist(population_2006, bins=20, color='brown', edgecolor='black')
plt.title('Population Distribution Across Countries in 2006')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()

#Average Population
years=[str(year) for year in range(1999,2023)]

if all(year in data.columns for year in years):
    mean_population_by_year=data[years].mean()
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x=mean_population_by_year.index, y=mean_population_by_year.values,palette="coolwarm")
    plt.title('Average Population by Year', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Average Population', fontsize=12)
    plt.tight_layout()
    plt.show()
    plt.xticks(rotation=45)
    
    
    #Population Distribution
    age_data={'Age Group': ['0-20', '21-40','41-60','61-80','80+'],
    'Population(Mil)': [400,700,550,350,90]}
    age_df=pd.DataFrame(age_data)
    
    plt.figure(figsize=(10,6))
    sns.barplot(x='Age Group',y='Population(Mil)',data=age_df,palette="coolwarm")
    plt.title('Population Distribution by Age')
    plt.xlabel('Average Group')
    plt.ylabel('Population(Mil)')
    plt.tight_layout()
    plt.show()
else:
    print("Year columns not found in dataset.")