import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password = 'Egyptiancobra27!',
    host='127.0.0.1',
    database='education',
    auth_plugin='mysql_native_password'
)

cursor = cnx.cursor()

def validate_college_name(college):
    """
    Validates and transforms college name.
    Return transformed name if valid, None if invalid
    """
    college = college.strip()

    if not college:
        print("Error: College  name cannot be empty")
        return None
    
    #Check if college name contains only letters and spaces
    if not all(c.isalpha() or c.isspace() for c in college):
        print("Error: College name must contain only letters and spaces")
        return None
    
    #Transform: remove extra spaces and capitalize first letter of each word
    return ' '.join(word.capitalize() for word in college.split())

def validate_student_count(student):
    """
    Validates student population count.
    Returns integer if Valid, None if invalid.
    """
    try:
        student_count= int(student)
        if student_count < 0:
            print("Error: Student population cannot be a negative")
            return None
        return student_count
    except ValueError:
        print("Error: Student population must ba a valid number")
        return None

college = input('Enter college name: ')
students = input('Enter student population: ')

validate_college_var = validate_college_name(college)
validate_student_var = validate_student_count(students)

query = (f'INSERT INTO `colleges` VALUES(NULL, "{validate_college_var}",{validate_student_var}, NULL, NULL, NULL)')
cursor.execute(query)
cnx.commit()

query= ("SELECT * FROM colleges")
cursor.execute(query)

#Print
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()