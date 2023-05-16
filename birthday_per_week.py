from datetime import datetime

users = [{"name": 'Ira', "birthday": datetime(year=2023, month=5, day=20)},
         {"name": 'Mira', "birthday": datetime(year=2023, month=5, day=21)},
         {"name": 'Lara', "birthday": datetime(year=2023, month=5, day=23)},
         {"name": 'Maxim', "birthday": datetime(year=2023, month=5, day=24)},
         {"name": 'Nora', "birthday": datetime(year=2023, month=5, day=25)}]

def get_birthdays_per_week(users):
    days = [[], [], [], [], []]
    name_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    current_date = datetime.now()
    current_day = current_date.day
    current_mon = current_date.month
    current_year = current_date.year
    current_week_day = current_date.weekday()
    if current_week_day == 0:
        m_delta = 0
    else:
        m_delta = 7 - current_week_day

    for el in users:
        if el["birthday"].date() in [datetime(day=current_day + m_delta - 2, month=current_mon, year=current_year).date(),
                                     datetime(day=current_day + m_delta - 1, month=current_mon, year=current_year).date(),
                                     datetime(day=current_day + m_delta, month=current_mon, year=current_year).date()]:
            days[0].append(el["name"])
        elif el["birthday"].date() == datetime(day=current_day + m_delta + 1, month=current_mon, year=current_year).date():
            days[1].append(el["name"])
        elif el["birthday"].date() == datetime(day=current_day + m_delta + 2, month=current_mon, year=current_year).date():
            days[2].append(el["name"])
        elif el["birthday"].date() == datetime(day=current_day + m_delta + 3, month=current_mon, year=current_year).date():
            days[3].append(el["name"])
        elif el["birthday"].date() == datetime(day=current_day + m_delta + 4, month=current_mon, year=current_year).date():
            days[4].append(el["name"])
    for i in range(5):
        if len(days[i]):
            print(name_days[i]+': '+', '.join(days[i]))


get_birthdays_per_week(users)
