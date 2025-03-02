import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
data = pd.read_csv('Survey - Data.csv')

# 1. Summarize numerical variables
print("Summary of Numerical Variables:")
print(data[['Hospital_visits', 'Health_spending', 'Family_size', 
'Willingness_to_pay']].describe())

# 2. Summarize categorical variables
print("\nPercentage of Chronic Conditions:")
print(data['Chronic_condition'].value_counts(normalize=True)) 
#Percentage of chronic conditions

print("\nPercentage Aware of Health Insurance:")
print(data['Health_insurance_aware'].value_counts(normalize=True)) 
#Percentage aware of health insurance

print("\nPercentage Aware of Takaful:")
print(data['Takaful_aware'].value_counts(normalize=True)) 
#Percentage aware of takaful

print("\nPercentage Interested in Takaful:")
print(data['Interested_in_takaful'].value_counts(normalize=True)) 
#Percentage interested in takaful

# 3. Cross-tabulation: Chronic condition vs. awareness
print("\nHealth Insurance Awareness by Chronic Condition:")
print(pd.crosstab(data['Chronic_condition'], 
data['Health_insurance_aware'], normalize='index'))  
#Row percentages

print("\nTakaful Awareness by Chronic Condition:")
print(pd.crosstab(data['Chronic_condition'], data['Takaful_aware'], 
normalize='index'))  
#Row percentages

# 4. Visualizations
# Bar chart: Chronic condition vs. health insurance awareness
sns.countplot(x='Chronic_condition', hue='Health_insurance_aware', 
data=data)
plt.title('Health Insurance Awareness by Chronic Condition')
plt.savefig('health_insurance_awareness.png')  
# Save the plot as an image plt.close()

# Bar chart: Chronic condition vs. takaful awareness
sns.countplot(x='Chronic_condition', hue='Takaful_aware', data=data)
plt.title('Takaful Awareness by Chronic Condition')
plt.savefig('takaful_awareness.png')  
#Save the plot as an image plt.close()

# Histogram: Willingness to pay
sns.histplot(data['Willingness_to_pay'], bins=20, kde=True)
plt.title('Distribution of Willingness to Pay')
plt.savefig('willingness_to_pay.png')  
#Save the plot as an image plt.close()

print("\nDescriptive analysis completed. Check the generated images for visualizations.")
