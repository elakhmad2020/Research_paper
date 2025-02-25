# probit_analysis.py

import pandas as pd
import statsmodels.api as sm

# Step 1: Define Variable Mappings
variable_mapping = {
    # Dependent Variable
    "Interested_in_takaful": {
        "description": "Willing to take a Takaful plan?",
        "data_type": "Binary (0=No, 1=Yes)",
        "values": {
            0: "No",
            1: "Yes"
        }
    },

    # Independent Variables
    "Hospital_visits": {
        "description": "Average hospital visits per year",
        "data_type": "Integer",
        "values": "Count of visits (e.g., 0, 1, 2, 3, 5, 10)"
    },
    "Health_spending": {
        "description": "Annual healthcare expenses (NGN)",
        "data_type": "Float",
        "values": "Amount in NGN (e.g., 5000, 10000, 250000)"
    },
    "Hospital_choice": {
        "description": "Type of hospital attended",
        "data_type": "String",
        "values": {
            "Government": "Government Hospital",
            "Private": "Private Hospital",
            "Anyone": "No specific preference"
        }
    },
    "Chronic_condition": {
        "description": "Has chronic condition?",
        "data_type": "Binary (0=No, 1=Yes)",
        "values": {
            0: "No",
            1: "Yes"
        }
    },
    "Chronic_disease_type": {
        "description": "Type of chronic condition",
        "data_type": "String",
        "values": "Disease names (e.g., Hypertension, Diabetes, Peptic Ulcer Disease)"
    },
    "Family_size": {
        "description": "Household size",
        "data_type": "Integer",
        "values": "Number of family members (e.g., 1, 2, 5, 8)"
    },
    "Health_insurance_aware": {
        "description": "Knows about health insurance?",
        "data_type": "Binary (0=No, 1=Yes)",
        "values": {
            0: "No",
            1: "Yes"
        }
    },
    "Takaful_aware": {
        "description": "Familiar with Takaful?",
        "data_type": "Binary (0=No, 1=Yes)",
        "values": {
            0: "No",
            1: "Yes"
        }
    },
    "Willingness_to_pay": {
        "description": "Annual amount willing to pay for Takaful",
        "data_type": "Float",
        "values": "Amount in NGN (e.g., 10000, 50000, 120000)"
    },
    "Payment_frequency": {
        "description": "Preferred payment plan",
        "data_type": "Integer",
        "values": {
            1: "Daily",
            2: "Monthly",
            3: "Yearly",
            4: "Unknown"
        }
    }
}

# Step 2: Print Variable Descriptions (Optional)
print("Variable Descriptions:")
for variable, details in variable_mapping.items():
    print(f"\nVariable: {variable}")
    print(f"Description: {details['description']}")
    print(f"Data Type: {details['data_type']}")
    if isinstance(details['values'], dict):
        print("Values:")
        for key, value in details['values'].items():
            print(f"  {key}: {value}")
    else:
        print(f"Values: {details['values']}")
print("-" * 60)

# Step 3: Load the Data
data = pd.read_csv('Survey - Data.csv')

# Step 4: Check for Missing Values
print("\nStep 1: Checking for missing values in each column:")
print(data.isnull().sum())

# Step 5: Handle Missing Values
# Drop rows with missing values in key columns
data = data.dropna(subset=['Hospital_visits', 'Health_spending', 
'Chronic_condition', 'Interested_in_takaful'])

# Verify that there are no missing values
print("\nStep 2: Missing values after handling:")
print(data.isnull().sum())

# Step 6: Ensure Dependent Variable is Binary
# Convert 'Interested_in_takaful' to binary (0 and 1)
data['Interested_in_takaful'] = data['Interested_in_takaful'].apply(lambda 
x: 1 if x == 1 else 0)

# Verify the conversion
print("\nStep 3: Value counts for 'Interested_in_takaful':")
print(data['Interested_in_takaful'].value_counts())

# Step 7: Define Dependent and Independent Variables
# Dependent variable
y = data['Interested_in_takaful']

# Independent variables
X = data[['Hospital_visits', 'Health_spending', 'Chronic_condition', 
'Family_size', 'Health_insurance_aware', 'Takaful_aware']]

# Step 8: Add a Constant to Independent Variables
X = sm.add_constant(X)

# Step 9: Fit the Probit Model
probit_model = sm.Probit(y, X)
probit_results = probit_model.fit()

# Step 10: Print the Summary of the Model
print("\nStep 4: Probit Model Summary:")
print(probit_results.summary())

# Save the probit model summary to a text file
with open('probit_results.txt', 'w') as f:
    f.write(probit_results.summary().as_text())

# Save the cleaned data to a CSV file
data.to_csv('cleaned_survey_data.csv', index=False)
