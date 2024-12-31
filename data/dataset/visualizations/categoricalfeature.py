import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('../DIM_LOCATION.csv')  # Adjust the path as needed

# Create a count plot for a categorical feature
plt.figure(figsize=(10, 6))  # Set the size of the plot
sns.countplot(x='region', data=df)  # Replace 'categorical_column' with your actual column name
plt.title('Count Plot of Categorical Column')  # Title of the plot
plt.xlabel('Category')  # Label for the x-axis
plt.ylabel('Count')  # Label for the y-axis
plt.show()  # Display the plot
