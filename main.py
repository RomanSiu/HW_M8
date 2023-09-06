from datetime import date, datetime
from collections import defaultdict

def get_birthdays_per_week(users):
    dict_with_days = defaultdict(list)
        
    today = date.today()
    
    for dict1 in users:
        usr_date = dict1["birthday"].replace(year=today.year)
        res = usr_date - today
        res = str(res).split(", ")
        res = int(res[0].removesuffix(" days").removesuffix(" day"))
        if res < -356:
            res = abs(res + 356)
            usr_date = dict1["birthday"].replace(year=today.year + 1)
        if 0 <= res <= 7:
            w_day = usr_date.weekday()
            if w_day == 1:
                dict_with_days["Tuesday"].append(dict1["name"])
            elif w_day == 2:
                dict_with_days["Wednesday"].append(dict1["name"])
            elif w_day == 3:
                dict_with_days["Thursday"].append(dict1["name"]) 
            elif w_day == 4:
                dict_with_days["Friday"].append(dict1["name"]) 
            else:
                dict_with_days["Monday"].append(dict1["name"])  
        else:
            continue
        
    return dict_with_days


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 9, 6).date()}, {"name": "Han Solo", "birthday": datetime(1976, 9, 9).date()}, 
        {"name": "Bobo", "birthday": datetime(1976, 10, 1).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
