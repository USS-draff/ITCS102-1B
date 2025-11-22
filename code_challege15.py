print("Student Information System")
print("===========================")
import os
import json
os.system('cls')
student_record = {}
while True:
    print("SELECT THE FOLLOWING OPTIONS")
    print("A - ADD STUDENT RECORD")
    print("B - PRINT ALL STUDENT RECORD")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - EXIT SYSTEM")

    choice  = input("SELECT FROM THE FOLLOWING OPTION ABOVE ---->").lower()

    if choice == "a":
        os.system('cls')
        print("ADDING STUDENT RECORD")

        ID = eval(input("Enter Student ID ----> " ))
        first_name = input("Enter Student First Name ----> ").lower()
        last_name = input("Enter Student Last Name ----> ").lower()
        Age = eval(input("Enter Student Age ---->" ))
        section = input("Enter Student Section ----> ")
        course = input("Enter Student Course ---->").lower()

        student_record[ID] = [first_name, last_name, Age, section, course]

        print("YOUR STUDENT RECORD HAS BEEN RECORDED.....")

        continue
    elif choice == 'b':
        os.system
        print("STUDENT PRINTING RECORD")

        for s, b in student_record.items():
            print(f"STUDENT ID - {s}, STUDENT INFORMATION {b}")

            continue
    elif choice == 'c':
        os.system("cls")
        print("FIND STUDENT RECORD")

        search_records = eval(input("PLEASE TYPE THE STUDENT ID YOU WANT TO SEE --->"))

        for record in student_record.keys():
            if search_records in student_record.keys():
                print(F"\nRECORD FOUND FOR ID NUMBER[] {search_records}")
            print("=========================") 
            
            for s in student_record[search_records]:
                print(f"------- {s}")
            print("=========================")
        else:
            print("STUDENT RECORD DOES NOT EXIST...")
           
        continue
    elif choice == 'd':
        os.system("cls")
        print("DELETE STUDENT RECORD")

        search_records = eval(input("PLEASE TYPE THE STUDENT ID YOU WANT TO SEE --->"))

        
        if search_records in student_record.keys():
            print(F"\nRECORD FOUND FOR ID NUMBER[] {search_records}")
            print("=========================") 
            
            for s in student_record[search_records]:
                    print(f"------- {s}")
            print("=========================")

            student_record.pop(search_records)
            print("STUDENT DATA HAS BEEN DELETED")
        else:
                print("STUDENT RECORD DOES NOT EXIST...")
                break
        continue
    elif choice == 'e':
        os.system("cls")
        print("EDIT STUDENT RECORD")

        search_records = eval(input("PLEASE TYPE THE STUDENT ID YOU WANT TO SEE --->"))

        for record in student_record.keys():
            if search_records in student_record.keys():
                print(F"\nRECORD FOUND FOR ID NUMBER[] {search_records}")
            print("=========================") 
            
            for s in student_record[search_records]:
                print(f"------- {s}")
            print("=========================")        

            first_name = input("Enter Student First Name ----> ").lower()
            last_name = input("Enter Student Last Name ----> ").lower()
            Age = eval(input("Enter Student Age ---->" ))
            section = input("Enter Student Section ----> ")
            course = input("Enter Student Course ---->").lower()

            student_record[search_records][0] = first_name
            student_record[search_records][1] = last_name
            student_record[search_records][2] = Age
            student_record[search_records][3] = section
            student_record[search_records][4] = course
            
            print("DATA HAS BEEN UPDATED")

    elif choice == 'f':
        os.system("cls")
        print("EXPORT STUDENT DATA")
        print("======================")

        with open("records.json", "w") as new_file:
            json.dump(student_record, new_file, indent = 4)

            print("DATA EPORTED TO records.json")

    elif choice == 'g':
        print("SYSTEM EXIT")
        break
    else:
        print("INVALID CHOICE. PLEASE SELECT AGAIN....")


    
