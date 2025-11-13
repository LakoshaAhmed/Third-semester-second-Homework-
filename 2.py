#Here is a list of some of the princes of Kyiv and the years of their reign.

#Using list comprehension and condition print a list of names of boyars who paid less than a tenth of their real income - 
#these are the boyars who will have to be impaled next month.
paid_money = {"Козьма Григорьевич": 70,
              "Аврам Стефанович": 101,
              "Захарий Григорьевич": 15,
              "Онцифор Лукинич": 208}

real_money = {"Козьма Григорьевич": 1000,
              "Аврам Стефанович": 900,
              "Захарий Григорьевич": 400,
              "Онцифор Лукинич": 2000}
candidates = [name for name in paid_money 
                        if paid_money[name] < real_money[name] / 10]

print("these are the boyars who will have to be impaled next month: ")
print(candidates)
