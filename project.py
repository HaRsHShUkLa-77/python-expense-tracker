#return
# ↓
# Function ko band karta hai.
# Aur value wapas bhej sakta hai.

from datetime import datetime
import json

from pathlib import Path

database = 'expensetracker.json'
data = {'expenses' : []}

if Path(database).exists():
    with open(database, 'r') as f:
        data=json.load(f)

def save():
    with open (database, 'w')as f:
        json.dump(data, f, indent=4)


        



class ExpenseTracker:

    def generate_id(self):
        if len(data['expenses']) == 0:
            return 1

        max_id = 0

        for expense in data['expenses']:
            if expense['eid'] > max_id:
                max_id = expense['eid']

        return max_id + 1

    def add(self):
        
        date = datetime.now().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%H:%M:%S')
        eid = self.generate_id()
        category = input('enter category: ').lower()
        
        try:
            amount = float(input ('enter amount to expend: '))
            if amount <=0:
                print('Amount must be greater than 0')
                return

        except ValueError:
            print('enter the amount in digits')
            return
            
        description = input('enter what you have spent on: ')

        

            
            
        data['expenses'].append({
                
                'date' : date,
                'time' : time,
                'eid' : eid,
                'category' : category,
                'amount' : amount,
                'description': description

            })

        save()
        
    def viewexpenses(self):
        if len(data['expenses'])==0:
            print('no expense yet')
            return
        total = 0
        for i in data['expenses']:
            total+=1
            print(f'----- EXPENSE {total} -----')
            for key, values in i.items():
                print(f'{key} : {values}')
            print()

    def searchexpenses(self):  #***
        category = input('enter category: ').lower()
        found = False
        for i in data['expenses']:
            if i['category'] == category:
                found = True
                print(f'----- EXPENSE -----')
                for key, values in i.items():
                    print(f'{key} : {values}')
        if not found:
            print('category not found')

    def deleteexpenses(self):
        eid = int(input('enter eid to delete expenses: '))
        for i in data['expenses']:
            if i['eid']== eid:
                data['expenses'].remove(i)
                save()
                print ('expense deleted')
                return
        print('invalid expense ID') 
        
        
    def totalexpenses(self):
        if len(data['expenses']) == 0:
            print('No expenses found. Total expense is 0.')
            return
        total=0
        for i in data['expenses']:
            total+= i['amount']
        print(f'Total Expenses: ₹{total}')

    def categoryreport(self):
        if len(data['expenses']) == 0:
            print('No expenses found. Total expense is 0.')
            return
        
        d={}
        for i in data['expenses']:
            if i['category'] in d:
                d[i['category']] += i['amount']
            else:
                d[i['category']] = i['amount']
        
        print('----- CATEGORY REPORT -----')
                
        for key, values in d.items():
                print(f'{key} : {values}')

e=ExpenseTracker()

print('enter 1 to add expenses')
print('enter 2 to view expenses')
print('enter 3 to search expenses')
print('enter 4 delete expenses')
print('enter 5 to check the total expenses')
print('enter 6 to check the category report ')
print('enter 7 to end the programme')


while True:
   
    
    try:
        user = int(input('enter your choice: '))
        print(f'You entered: {user}')
    except ValueError:
        print('enter a valid choice')
        continue
    

    if user==1:
        e.add()

    elif user==2:
        
        e.viewexpenses()
    
    elif user==3:
        e.searchexpenses()

    elif user==4:
        e.deleteexpenses()

    elif user==5:
        e.totalexpenses()

    elif user==6:
        e.categoryreport()

    elif user==7:
        print('Visit Again') 
        break     

    else:
        print('invalid choice')

        
            


        

            
                
        





        

