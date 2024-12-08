import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations():
    """
    Create visualizations of the cleaned NHANES data
    """
    # Load the cleaned data
    cleaned_data = pd.read_csv('data/cleaned_data.csv')

    # Example visualization: Distribution of age
    plt.figure(figsize=(10, 6))
    sns.histplot(cleaned_data['RIDAGEYR'], bins=30, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig('visualizations/age_distribution.png')
    plt.close()

    # Example visualization: BMI vs. Age
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='RIDAGEYR', y='BMXBMI', data=cleaned_data)
    plt.title('BMI vs. Age')
    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.savefig('visualizations/bmi_vs_age.png')
    plt.close()

    # Correlation matrix
    plt.figure(figsize=(12, 8))
    correlation_matrix = cleaned_data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.savefig('visualizations/correlation_matrix.png')
    plt.close()

    # Distribution of BMI by Gender
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='RIAGENDR', y='BMXBMI', data=cleaned_data)
    plt.title('BMI Distribution by Gender')
    plt.xlabel('Gender (1=Male, 2=Female)')
    plt.ylabel('BMI')
    plt.savefig('visualizations/bmi_by_gender.png')
    plt.close()

    # Summary statistics
    summary_stats = cleaned_data.describe()
    summary_stats.to_csv('visualizations/summary_statistics.csv')

    # Age vs. Blood Pressure (if available)
    if 'BPXSY1' in cleaned_data.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='RIDAGEYR', y='BPXSY1', data=cleaned_data)
        plt.title('Age vs. Systolic Blood Pressure')
        plt.xlabel('Age')
        plt.ylabel('Systolic Blood Pressure')
        plt.savefig('visualizations/age_vs_blood_pressure.png')
        plt.close()

if __name__ == "__main__":
    create_visualizations()
