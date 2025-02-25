import pandas as pd
import statsmodels.api as sm

data = pd.read_csv('Survey - Data.csv')

y = data['Interested_in_takaful']
X = data[['Hospital_visits', 'Health_spending', 'Chronic_condition', 
'Family_size', 'Health_insurance_aware', 'Takaful_aware']]

X = sm.add_constant(X)

probit_model = sm.Probit(y,X)
probit_results = probit_model.fit()

print(probit_results.summary())
