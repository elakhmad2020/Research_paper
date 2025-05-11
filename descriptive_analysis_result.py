import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
data = pd.read_csv('Survey - Data.csv')

# Create a function to write output to both console and file
def save_descriptive_analysis(filename="descriptive_results.txt"):
    with open(filename, 'w') as file:
        # 1. Summarize numerical variables
        file.write("Summary of Numerical Variables:\n")
        summary_stats = data[['Hospital_visits', 'Health_spending', 'Family_size',
                             'Willingness_to_pay']].describe()
        file.write(summary_stats.to_string(float_format="%0.2f"))
        file.write("\n\n")
        
        print("Summary of Numerical Variables:")
        print(summary_stats.to_string(float_format="%0.2f"))

        # 2. Summarize categorical variables
        file.write("Percentage of Chronic Conditions:\n")
        chronic = data['Chronic_condition'].value_counts(normalize=True)
        file.write(str(chronic))
        file.write("\n\n")
        
        print("\nPercentage of Chronic Conditions:")
        print(chronic)

        file.write("Percentage Aware of Health Insurance:\n")
        insurance = data['Health_insurance_aware'].value_counts(normalize=True)
        file.write(str(insurance))
        file.write("\n\n")
        
        print("\nPercentage Aware of Health Insurance:")
        print(insurance)

        file.write("Percentage Aware of Takaful:\n")
        takaful = data['Takaful_aware'].value_counts(normalize=True)
        file.write(str(takaful))
        file.write("\n\n")
        
        print("\nPercentage Aware of Takaful:")
        print(takaful)

        file.write("Percentage Interested in Takaful:\n")
        interest = data['Interested_in_takaful'].value_counts(normalize=True)
        file.write(str(interest))
        file.write("\n\n")
        
        print("\nPercentage Interested in Takaful:")
        print(interest)

        # 3. Cross-tabulation: Chronic condition vs. awareness
        file.write("Health Insurance Awareness by Chronic Condition:\n")
        cross_insurance = pd.crosstab(data['Chronic_condition'],
                                     data['Health_insurance_aware'], normalize='index')
        file.write(str(cross_insurance))
        file.write("\n\n")
        
        print("\nHealth Insurance Awareness by Chronic Condition:")
        print(cross_insurance)

        file.write("Takaful Awareness by Chronic Condition:\n")
        cross_takaful = pd.crosstab(data['Chronic_condition'],
                                  data['Takaful_aware'], normalize='index')
        file.write(str(cross_takaful))
        file.write("\n\n")
        
        print("\nTakaful Awareness by Chronic Condition:")
        print(cross_takaful)

        file.write("\nDescriptive analysis completed. Check the generated images for visualizations.")
        
        print("\nDescriptive analysis completed. Check the generated images for visualizations.")
        print(f"\nResults saved to {filename}")

# Run the analysis and save results
save_descriptive_analysis()

# Generate visualizations (keep your existing visualization code here)
# plt.savefig('health_insurance_awareness.png')
# plt.savefig('takaful_awareness.png')
# etc.
