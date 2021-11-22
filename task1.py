duration = int(input("enter your time in second: "))
days = duration // 3600 // 24
hours = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60

print("days-", days, ', hours-', hours, ", minutes-", minutes, ", seconds-", seconds)
