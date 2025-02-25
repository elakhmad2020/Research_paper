import pandas as pd 

#Load the CSV file
data = pd.read_csv( 'Survey - Data.csv')

#Display the rows 
print(data.head(259))
