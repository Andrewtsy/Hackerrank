# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())    
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())
