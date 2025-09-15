# ============================================
# Data Analysis & Visualization on Iris Dataset
# ============================================

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Create directory for plots
PLOT_DIR = "plots"
os.makedirs(PLOT_DIR, exist_ok=True)

# -----------------------
# Task 1: Load & Explore
# -----------------------

try:
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to DataFrame

    print("✅ Dataset loaded successfully!\n")

    # Display first few rows
    print("🔎 First 5 rows of the dataset:")
    print(df.head(), "\n")

    # Data types and missing values
    print("📋 Dataset Info:")
    print(df.info(), "\n")

    print("❓ Missing values per column:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (Iris has no missing values, but handle just in case)
    df = df.dropna()
    print("🧹 Data cleaned (missing values handled).\n")

except FileNotFoundError:
    print("❌ File not found. Please check the dataset path.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")


# -----------------------
# Task 2: Basic Analysis
# -----------------------

print("📊 Basic Statistics:")
print(df.describe(), "\n")

# Group by species (target)
grouped = df.groupby("target").mean()
print("📊 Mean values grouped by species:")
print(grouped, "\n")

# Interesting finding
print("💡 Finding: Iris-setosa generally has smaller petal length and width compared to other species.\n")


# -----------------------
# Task 3: Visualizations
# -----------------------

# 1. Line chart
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length over Index")
plt.xlabel("Index (simulated time)")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.savefig(os.path.join(PLOT_DIR, "line_chart.png"))
plt.show()

# 2. Bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x="target", y="petal length (cm)", data=df, estimator="mean", ci=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.savefig(os.path.join(PLOT_DIR, "bar_chart.png"))
plt.show()

# 3. Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig(os.path.join(PLOT_DIR, "histogram.png"))
plt.show()

# 4. Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.savefig(os.path.join(PLOT_DIR, "scatter_plot.png"))
plt.show()

print(f"📂 All plots have been saved inside the '{PLOT_DIR}/' directory.")
