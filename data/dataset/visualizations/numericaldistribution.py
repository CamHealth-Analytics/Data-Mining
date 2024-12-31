import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the dataset
df = pd.read_csv('../FACT_MATERNAL_MORTALITY.csv') 

# Displaying column names
print("Columns in the dataset:", df.columns)

# Plot numerical column
sns.histplot(df['number_of_maternal_deaths'], bins=30, kde=True)  
plt.title('Distribution of Numerical Column')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
