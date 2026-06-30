#Empty Dictionary
studentreport = {}

#Add report
studentreport["Baldeep"]= {"english":80 , "maths":80, "science":75}
studentreport["Tanya"]= {"english":90 , "maths":95, "science":85}
studentreport["Gaytri"]= {"english":85 , "maths":60, "science":90}
studentreport["Hitesh"]= {"english":40 , "maths":60, "science":80}

#ADD FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def add_function():
    print("\nADD NEW STUDENT DETAILS----\n")
    name = input("Enter Student Name :")

    print("\nSUBJECTS------------->")
    english = int(input("Enter English Marks : "))
    maths = int(input("Enter Maths Marks : "))
    science = int(input("Enter Science Marks : "))
    studentreport[name]= {"english":english, "maths":maths, "science":science}


#DELETE FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def delete_function():
    print("\nDELETE STUDENT>>>>>\n")
    name = input("Enter Student Name :")
    if name in studentreport:
        studentreport.pop(name)
    else: 
        print("Student Not Exist")


#UPDATE FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def update_function():
    print("\nUPDATE EXISTING STUDENTS DETAILS----\n")
    name = input("Enter Student Name :")
    if name in studentreport:
        print("\nSUBJECTS-------------->")
        english = int(input("Enter English Marks : "))
        maths = int(input("Enter Maths Marks : "))
        science = int(input("Enter Science Marks : "))
        studentreport[name]= {"english":english, "maths":maths, "science":science}
    else: 
        print("Student Not exist")

#def avg_function():



#SEARCH FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def search_function():
    print("\nSEARCH STUDENT IN REPORT CARD>>>>>>>\n")
    try:
        name = input("Enter Student Name :")
        search =studentreport[name]
        print(f"Name : {name} - English : {search['english']}, Maths : {search['maths']}, Science : {search['science']}")
    except KeyError:
        print("Student Not Exist")


#SHOW FUNCTION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def show_function():
    print("\nSTUDENT REPORT CARD\n")
    for student,subjects in studentreport.items():
        print(f"{student}- English : {subjects['english']}, Maths : {subjects['maths']}, Science : {subjects['science']}")


#Add New Student In Report Card..................................................
add_function()

#Delete Existing Student From Report Card........................................
delete_function()

#Update Students Grades...........................................................
update_function()

#Search Student From Report Card..................................................
search_function()

#Show Students Grades.............................................................
show_function()