from datetime import datetime,timedelta
from collections import defaultdict

def list_sort_by_date(lst):
    
    todays_date = datetime.now()
    
    def sort_funk(x):
        
        month,date = list(map(int,x['date'].split("-")[1:]))
        
        if not is_leap_year(todays_date.year) and month==2 and date == 29:
            month,date = 3,1
        
        return datetime(todays_date.year,month,date)
        
    result = sorted(lst, key = sort_funk)
    return result

def is_leap_year(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)

def next_week_birthdays(users: list) -> str:
    
    week_birthdays = defaultdict(list)
    todays_date = datetime.now()
    next_week_date = todays_date + timedelta(weeks=1)
    
    users = list_sort_by_date(users)
    
    for user in users:
        
        _,month,date = list(map(int, user['date'].split("-")))
        
        if not is_leap_year(todays_date.year) and month==2 and date == 29:
            month,date = 3,1
            
        birthday_date = datetime(todays_date.year,month,date)
         
        if todays_date <= birthday_date <= next_week_date and birthday_date.weekday() < 5:
            week_birthdays[birthday_date.strftime('%A')].append(user['name'])
        elif todays_date <= birthday_date <= next_week_date and birthday_date.weekday() >= 5:
            week_birthdays['Monday'].append(user['name'])
        else:
            pass
        
    result = '\n'.join([f"{k}: {', '.join(v)}" for k,v in week_birthdays.items()])
    return result