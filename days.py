days = ['saturday', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday']
currentday = input("what day is today?\n")
aod = input("in how many days will your package arrive?\n")

x = int(aod)
day = 0
week=-1
while currentday != str(days[day]):
    day += 1

if currentday in days: #knowing current day, find the pos of current day within days
    while x > day-7:
        x-=7
        week +=1
    if week >= 1:
        if week > 1:
            print('your package will arrive in '+ str(week) +' weeks on a '+days[day + x])
        else:
            print('your package will arrive in 1 week on a '+days[day + x])
    else:
        print('your package will arrive on '+days[day + x])
    
else:
    pass