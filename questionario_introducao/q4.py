first_day, first_hour = input().split()
last_day, last_hour = input().split()

def convert_to_seconds(day, hour):
    hours = int(day)*24
    h, m, s = hour.split(":")
    hours += int(h)
    converted = (hours*60*60) + (int(m)*60) + int(s)
    return converted, int(hours), int(m), int(s)



def convert_date(day1, hour1, min1, sec1, day2, hour2, min2, sec2 ):
    if day1 >= day2:
        print("Data inválida!")
    else:
        duration_days, duration_hours = int((hour2 - hour1)/24), int((hour2 - hour1) % 24)
        if min2 - min1 < 0:
             duration_hours -= 1
             duration_minutes = 60 + min2 - min1
        else:
            duration_minutes = min2 -min1
        if sec2 - sec1 < 0:
            duration_minutes -= 1
            duration_second = 60 + sec2 - sec1
        else:
            duration_second = sec2 -sec1
        print(f"{duration_days} dia(s)")
        print(f"{duration_hours} hora(s)")
        print(f"{duration_minutes} minuto(s)")
        print(f"{duration_second} segundo(s)")

d1, h1, m1, s1= convert_to_seconds(first_day, first_hour)
d2, h2, m2, s2= convert_to_seconds(last_day, last_hour)
convert_date(d1, h1, m1, s1, d2, h2, m2, s2)



