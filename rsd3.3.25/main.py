import date_check
import time_check
import datetime
from datetime import date
import os

today = date.today()

with open(r'log.txt', 'r') as file:
        # read all content from a file using read()
        content = file.read()
        # check if string present or not
        if (f"{today}") in content:

            print('Do no execute')


        else:
            with open(r'check.txt', 'r') as file:
                content = file.read()
                if ("weekdaystart") in content:
                    print("run")
                else:
                    print("end")

            print('Replace this text with program')


def main():
    pass

if __name__ == "__main__":
    main()

