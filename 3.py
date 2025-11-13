### 3. One day, one more, yes one day - part 1. (1 point)

#Here is a list of some of the princes of Kyiv and the years of their reign.

#Your task is using the lambda function and the sort function to sort them in ascending order of the number of years they spent on the throne.
rulers = [{"name": "Олег Вещий", "year_start": 882, "year_end": 912},
          {"name": "Игорь Рюрикович", "year_start": 912, "year_end": 945},
          {"name": "Ольга", "year_start": 945, "year_end": 960},
          {"name": "Святослав Игоревич", "year_start": 945, "year_end": 972},
          {"name": "Ярополк Святославич", "year_start": 972, "year_end": 978},
          {"name": "Владимир Святославич", "year_start": 978, "year_end": 1015}]
sorted_rulers = sorted(rulers, key=lambda x: x["year_end"] - x["year_start"])

for ruler in sorted_rulers:
    reign_years = ruler["year_end"] - ruler["year_start"]
    print(f"{ruler['name']}: {reign_years} years")