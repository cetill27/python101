from pathlib import Path
import json

path  =Path('expense.json')


if path.exists():
    expenses = json.loads(path.read_text())
else:
    expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount  =float(input("Enter amount: "))
    expenses.append({"name":name,"amount":amount})

    content = json.dumps(expenses)
    path.write_text(content)

def show_expenses():
    if not expenses:
        print("No expenses added ye")
    else:
        # for e in expenses:
        #     print(e["name"],e["amount"])
        content = path.read_text()
        data  =json.loads(content)
        print(data)
while True:
    print("\n1.Add Expense")
    print("2.Show Expenses")
    print("3.Total Expense")
    print("4.Exit")

    

    choice  = input("Choose option: ")
    if choice =="1":
        add_expense()
    elif  choice =="2":
        show_expenses()
    elif choice =="3":
        total = sum(e["amount"] for e in expenses)
        print("Total spent : ",total)