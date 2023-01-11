import re
from sqlite3 import Date
import gspread
from datetime import date, timedelta


sa = gspread.service_account()

sh = sa.open('Sierra Platoon')




def get_A2_grades():

    wks = sh.worksheet('A2')
    sheet = wks.get('A2:H44')
    
    grade_dict = {}
    for record in sheet:
    
        grade_dict[record[0]] = {
            'correctness': record[1],
            'design': record[2],
            'bonus': record[3],
            'penalty': record[4],
            'total': record[5],
            'percentage': record[6]
        }

    with open('./assessment2_grades.txt', 'w') as file:
        for name, data in grade_dict.items():

            string = """
%s : 
---------
Correctness: %s/13
> notes: 

Code design: %s/8
> notes: 

Bonus: %s

Total: %s
___________________________________

            """ % (name, data['correctness'], data['design'], data['bonus'], data['percentage'])
            file.write(string)


def get_A3_grades():

    wks = sh.worksheet('A3')
    sheet = wks.get('A2:I44')
    
    grade_dict = {}
    for record in sheet:
    
        grade_dict[record[0]] = {
            'api': record[1],
            'structure': record[2],
            'styling': record[3],
            'functionality': record[4],
            'bonus': record[5],
            'penalty': record[6],
            'total': record[7],
            'percentage': record[8]
        }

    with open('./assessment3_grades.txt', 'w') as file:
        for name, data in grade_dict.items():

            string = """
%s : 
---------
API Integration: %s/4
Website Structure: %s/6
Website Styling: %s/6
Website Functionality: %s/5
Bonus: %s

----------------
Total: %s
___________________________________

            """ % (name, data['api'], data['structure'], data['styling'], data['functionality'], data['bonus'], data['percentage'])
            file.write(string)


def get_A4_grades():

    wks = sh.worksheet('A4')
    sheet = wks.get('A1:Q44')
    
 
    categories  = []
    subcategories = []

    for index , item in enumerate(sheet[0]):
        
        categories.append(item)
        # if item == "":
        #     categories.append(sheet[1][index])
        # else:
    
    for item in sheet[1]:
        
        subcategories.append(item)   

    with open('./assessment4_grades.txt', 'w') as file:
        for record in sheet[2:]:

            string = """
%s : 
---------
"""  % (record[0])

            string += "\nStatus: %s\n" %(record[2])

            for index, category in enumerate(categories[3:-2]):
                
                if len(category) <2:
                    string += """    > %s : %s/2
""" % (subcategories[index+3], record[index+3])

                else: 
                    string += """
%s 
    > %s : %s/2
""" % (category, subcategories[index+3], record[index+3])
                
            string += """
--------
Total: %s        

----------------------------------
            """ % (record[1])

            file.write(string)


"""
API Integration: %s/4
Website Structure: %s/6
Website Styling: %s/6
Website Functionality: %s/5
Bonus: %s

----------------
Total: %s
___________________________________

            """


# get_A2_grades()
# get_A3_grades()
get_A4_grades()
