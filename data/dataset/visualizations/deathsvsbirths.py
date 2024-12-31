import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
# Adjust the path to your CSV file as necessary
df = pd.read_csv('../FACT_MATERNAL_MORTALITY.csv')  # Ensure the file path is correct

# Check if the numerical columns exist
if 'number_of_births' in df.columns and 'number_of_maternal_deaths' in df.columns:
    # Drop missing values in the selected columns
    df = df.dropna(subset=['number_of_births', 'number_of_maternal_deaths'])
    
    # Create the scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='number_of_births', y='number_of_maternal_deaths', data=df)
    
    # Add titles and labels
    plt.title('Scatter Plot: Number of Births vs. Number of Maternal Deaths', fontsize=16)
    plt.xlabel('Number of Births', fontsize=14)
    plt.ylabel('Number of Maternal Deaths', fontsize=14)
    
    # Display the plot
    plt.show()
else:
    print("Error: One or both of the required columns ('number_of_births', 'number_of_maternal_deaths') are missing.")
