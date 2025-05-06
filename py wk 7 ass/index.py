import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    print("Dataset loaded successfully")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
    exit(1)

# Display the first few rows
print("\nFirst few rows of the dataset:")
print(df.head())

# Explore the dataset
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Compute basic statistics
print("\nBasic statistics of the numerical columns:")
print(df.describe())

# Group by species and compute means
grouped = df.groupby('species').mean()
print("\nGrouped by species (mean of numerical columns):")
print(grouped)

print("\nSepal and Petal Length Comparison per Species:")
print(grouped[['sepal length (cm)', 'petal length (cm)']])

# Set up visualization style
sns.set(style="whitegrid")

# 1. Line chart: Simulated trend of average petal length over time
time = pd.date_range(start="2020-01-01", periods=10, freq="M")
avg_petal_len = [df['petal length (cm)'].mean()] * 10

plt.figure(figsize=(8, 6))
plt.plot(time, avg_petal_len, marker='o', color='blue', label='Avg Petal Length')
plt.title('Petal Length Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='viridis')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of Sepal Length
plt.figure(figsize=(8, 6))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True, color='green')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='Set1')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()
