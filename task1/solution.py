def what_is_my_sign(day, month):
    signs = {
    "Овен": [(21, 3), (20, 4)],
    "Телец": [(21, 4), (20, 5)],
    "Близнаци": [(21, 5), (20, 6)],
    "Рак": [(21, 6), (21, 7)],
    "Лъв": [(22, 7), (22, 8)],
    "Дева": [(23, 8), (22, 9)],
    "Везни": [(23, 9), (22, 10)],
    "Скорпион": [(23, 10), (21, 11)],
    "Стрелец": [(22, 11), (21, 12)],
    "Козирог": [(22, 12), (19, 1)],
    "Водолей": [(20, 1), (18, 2)],
    "Риби": [(19, 2), (20, 3)] 
    }
    for k in signs.keys():
        start_day = signs[k][0][0]
        start_month = signs[k][0][1]
        final_day = signs[k][1][0]
        final_month = signs[k][1][1]
        if day>=start_day and month == start_month or day<=final_day and month == final_month:
            return k
