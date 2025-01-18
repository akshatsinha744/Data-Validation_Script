import pandas as pd
import re
data = pd.read_csv(r'C:\Users\Admin\Desktop\Akshat\question9_validation_dataset.csv')


def validate_csv(data):
    for index,row in data.iterrows():
        if(row.age<0):
            print(index,row['name'],'Negative Age')

    for index,row in data.iterrows():
        if(row['salary']<0):
            print(index,row['name'],row['salary'],'Negative Salary')

    for index,row in data.iterrows():
        email = row.get('email','')
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print(index,row['name'],row['email'],'Error in Email')

validate_csv(data)