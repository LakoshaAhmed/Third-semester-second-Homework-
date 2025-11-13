#Here are two dictionaries - the `paid_money` dictionary - the amount of gold that this boyar paid to the treasury and the 
#`real_money` dictionary - the amount of gold that the boyar actually earned.

#Using a for lprint a list of the names of the boyars who paid less than a tenth of their real income - 
#these are the boyars who will have to be impaled next month.



paid_money = {"Козьма Григорьевич": 70,
              "Аврам Стефанович": 101,
              "Захарий Григорьевич": 15,
              "Онцифор Лукинич": 208}

real_money = {"Козьма Григорьевич": 1000,
              "Аврам Стефанович": 900,
              "Захарий Григорьевич": 400,
              "Онцифор Лукинич": 2000}
to_be_impaled = []
for name in paid_money:
    if name in real_money:
        if paid_money[name] < real_money[name] /10 :
            to_be_impaled.append(name)

print ("Boyars to be impaled next month:",to_be_impaled)
