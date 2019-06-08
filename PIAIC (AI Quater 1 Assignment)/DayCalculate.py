from datetime import datetime
date_format = "%d/%m/%Y"
e = input("Enter a date in (dd/mm/yy) Format: ")
f = input("Enter a date in (dd/mm/yy) Format: ")
a = datetime.strptime( e , date_format)
b = datetime.strptime( f , date_format)
delta = b - a
print ("There are", delta.days, "days in Between", e , "and" , f)