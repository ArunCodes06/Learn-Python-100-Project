# greeting
print("Welcome To The Tip Calculator !")
bill = float(input("what is your fill ? $"))
tip = int(input("What percentage of tip would u like to give ? 10 12 15"))
people = int(input("how many people split he bill?"))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"each person should pay: ${final_amount}")
