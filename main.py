#Empty Dictionary
studentreport = {}

#Add report
studentreport["Baldeep"]= {"english":80 , "maths":80, "science":75}
studentreport["Tanya"]= {"english":90 , "maths":95, "science":85}
studentreport["Gaytri"]= {"english":85 , "maths":60, "science":90}
studentreport["Hitesh"]= {"english":40 , "maths":60, "science":80}

#Update Student report
def update_function():
    print("UPDATE STUDENTS DETAILS----")
    name = input("Enter Student Name :")
    if name in studentreport:
        print("Subjects")
        english = input("Enter English Marks : ")
        maths = input("Enter Maths Marks : ")
        science = input("Enter Science Marks : ")
        studentreport[name]= {"english":english, "maths":maths, "science":science}
    else: 
        print("Student Not exist")

def show_function():
    for student,subjects in studentreport.items():
        print(f"{student}- English : {subjects['english']}, Maths : {subjects['maths']}, Science : {subjects['science']}")



#Update Students Grades...........................................................
update_function()

#Show Students Grades.............................................................
show_function()