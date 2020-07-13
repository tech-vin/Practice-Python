from datetime import date

startDate = date(2014, 7, 2)
endDate = date(2014, 7, 11)
delta = endDate - startDate
print(delta.days)