import re
from sqlite3 import Date
import gspread
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


columns = {
    'timestamp': 'Timestamp',
    'name': 'Name',
    'confidence_yeserday_curriculum':'How confident are you feeling about yesterday\'s curriculum?',
    'feedback': 'How did yesterday\'s lecture go? Please provide feedback.',
    'progress': 'How are you feeling right now about your progress?',
    'overall_feeling': 'How are you feeling overall?',
    'pairing_partner': 'Yesterday\'s pairing partner',
    'pairing_session': 'How did your pairing session go yesterday?',
    'pairing_communication': 'How well did you and your partner communicate?',
    'pairing_partner_feedback': 'Any feedback for your pairing partner? (Your feedback will be given anonymously)',
    'email': 'Your Email Address (used to confirm your attendance)'
}

# student_list = get_students_list_from_file()

sa = gspread.service_account()

sh = sa.open('Sierra Daily Check-Ins (Responses)')
sheet = sh.worksheet('responses')

today = date.today()
yesterday = today - timedelta(days = 1)

date_string = yesterday.strftime('%m/%d/%Y') 

# records = sheet.
criteria_re = re.compile(rf'^{date_string}')
cell_list = sheet.findall(criteria_re)
for cell in cell_list:
    print(cell.row)
    
all_records = sheet.get_all_records()
daily_records = {}

for record in all_records:

    date = record['Timestamp'].split(' ')[0]
    name = record['Name']

    if date in daily_records:
        daily_records[date][name] = {
                'feedback': record[columns['feedback']],
                'confidence_score': record[columns['confidence_yeserday_curriculum']],
                'progress_score': record[columns['progress']],
                'overall_feeling_score': record[columns['overall_feeling']],
                'pairing_partner': record[columns['pairing_partner']],
                'pairing_session_score': record[columns['pairing_session']],
                'pairing_communication_score': record[columns['pairing_communication']],
                'pairing_partner_feedback' : record[columns['pairing_partner_feedback']],
                'email': record[columns['email']]
            }
    else: 
        daily_records[date] = {
            name: {
                'feedback': record[columns['feedback']],
                'confidence_score': record[columns['confidence_yeserday_curriculum']],
                'progress_score': record[columns['progress']],
                'overall_feeling_score': record[columns['overall_feeling']],
                'pairing_partner': record[columns['pairing_partner']],
                'pairing_session_score': record[columns['pairing_session']],
                'pairing_communication_score': record[columns['pairing_communication']],
                'pairing_partner_feedback' : record[columns['pairing_partner_feedback']],
                'email': record[columns['email']]
            }
        }          

for day in daily_records:
    print(day)
    print(daily_records[day])


# if len < 42 compare student list to daily_record



