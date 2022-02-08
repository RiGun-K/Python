import seaborn as sns
import pandas as pd
titanic = sns.load_dataset("titanic")
titanic.to_csv('C:/Users/RiGun/Python/통계분석/titanic.csv', index = False)

print(titanic.isnull().sum())
