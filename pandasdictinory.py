import pandas as pd
data={
	'Name' :['Saketh','Chaitanya','Sai','Avinash','Chakri'],
	'Age' :[19,20,18,19,20],
	'City' :['Srikakulam','Vizag','Nellore','Chennai','Eluru']
}
df=pd.DataFrame(data)
print("DataFrame:\n",df)
print("First 3 rows using head():",df.head(3))
print("\nSelect a Single column(Name):\n",df['Name'])
print("\nSelect Multiple columns(Name,Marks):\n",df[['Name','Age']])
print("\nSelect a Single Row:\n",df.iloc[3])
print("\nSelect a Range of Rows(2 to 4):\n",df.iloc[2:5])

	
