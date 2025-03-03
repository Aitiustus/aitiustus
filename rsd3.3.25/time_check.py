#https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime

from datetime import datetime

check = open('check.txt', 'a+')

start_time_str = '06::30::00'
start_time_object = datetime.strptime(start_time_str, '%H::%M::%S').time()
#print(type(start_time_object))
#print(start_time_object)

end_time_str = '02::00::00'
end_time_object = datetime.strptime(end_time_str, '%H::%M::%S').time()
#print(type(end_time_object))
#print(end_time_object)

time = datetime.now()
formatted_time = time.time()  # Simplified way to get time object directly
#print(type(formatted_time))    # Should be <class 'datetime.time'>
#print(formatted_time)          # Outputs current time in H:M:S format

try:
    start_time_object < formatted_time < end_time_object,
    check.write('start')
    #print("start")
except: print("pause")

