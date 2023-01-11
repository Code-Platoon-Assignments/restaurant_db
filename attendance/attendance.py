import re
from sqlite3 import Date
import gspread  #https://pypi.org/project/gsheets/
from datetime import date, timedelta


def update_student_list():

    sa = gspread.service_account()

    sh = sa.open('Sierra Platoon')
    wks = sh.worksheet('Student Info')

    student_list = wks.get('A2:A43')
    student_list = [item for sublist in student_list for item in sublist]

    with open('./student_list.txt', 'w') as file:
        file.writelines("%s\n" % l for l in student_list)


def get_students_list_from_file():

    with open('./student_list.txt', 'r') as file:
        lines = file.readlines()
        lines = [i.strip() for i in lines]
        print(lines)
        return lines

# update_student_list()


# student_list = get_students_list_from_file()
sa = gspread.service_account()
sh = sa.open('Sierra Platoon')
sheet = sh.worksheet('Attendance')

today = date.today()
yesterday = today - timedelta(days=1)

date_string = yesterday.strftime('%m/%d/%Y')


# criteria_re = re.compile(rf'^{date_string}')
# cell_list = sheet.findall(criteria_re

records = sheet.get_all_records()
for record in records:
    print(record)

# all_records = sheet.get_all_records()
# daily_records = {}

# for record in all_records:

#     print()


# if len < 42 compare student list to daily_record
