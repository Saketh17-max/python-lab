import csv
data=[
	['S.No','Roll no','Name'],
	[1,101,'Ravi'],
	[2,102,'Raghu Ram'],
	[3,103,'Tony']
	]
with open('table.csv','w',newline='') as f:
	wf=csv.writer(f)
	wf.writerows(data)	
