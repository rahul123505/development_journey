year = 1879

while year <= 2026:
    if year%4==0 and year%100!=0 or year%400==0:
        print(year)
    year = year+1
