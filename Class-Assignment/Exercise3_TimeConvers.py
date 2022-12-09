seconds_insert = eval(input("Insert a number of seconds"))

hour = seconds_insert // 3600
minute = (seconds_insert - (hour * 3600)) // 60
second = seconds_insert - (minute * 60) - (hour * 3600) 

print(f"Result: {hour}:{minute}:{second})