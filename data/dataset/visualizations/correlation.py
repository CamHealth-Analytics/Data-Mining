import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('../FACT_MATERNAL_MORTALITY.csv')  # Adjust the path as needed

# Compute the correlation matrix
corr_matrix = df.corr()

# Plot the heatmap
plt.figure(figsize=(12, 8))  # Set the size of the plot
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)  # Create the heatmap
plt.title('Correlation Matrix')  # Title of the plot
plt.show()  # Display the plot
