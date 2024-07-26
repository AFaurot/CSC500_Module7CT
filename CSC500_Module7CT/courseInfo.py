#print_menu function to output options for user input
def print_menu():
    print("Choose your course to print information for: \n")
    print("1 = CSC101 \n2 = CSC102 \n3 = CSC103 \n"
          "4 = NET110 \n5 = COM241 \n0 = Exit Program \n" )

def main():

#Dictionary to associate room number with course number
    room_number = dict(CSC101 = "3004", CSC102 = "4501", CSC103 = "6755",
                   NET110 = "1244", COM241 = "1411")
#Dictionary to associate instructor name with course number
    instructor = dict(CSC101 = "Haynes", CSC102 = "Alvarado", CSC103 = "Rich",
                   NET110 = "Burke", COM241 = "Lee")
#Dictionary to associate meeting time with course number
    meeting_time = dict(CSC101 = "8:00 a.m", CSC102 = "9:00 a.m", CSC103 = "10:00 a.m",
                   NET110 = "11:00 a.m", COM241 = "1:00 p.m.")
    print_menu()
    command = input("Enter command :")
    #While loop to keep program running until user chooses to end it.
    while command != '0':

        if command == '1':
            print("\nCSC101: Room = {}, Instructor = {}, Meeting Time = {} \n"
                  .format(room_number['CSC101'], instructor['CSC101'], meeting_time['CSC101'] ))
        elif command == '2':
            print("\nCSC102: Room = {}, Instructor = {}, Meeting Time = {} \n"
                  .format(room_number['CSC102'], instructor['CSC102'], meeting_time['CSC102']))
        elif command == '3':
            print("\nCSC103: Room = {}, Instructor = {}, Meeting Time = {} \n"
                  .format(room_number['CSC103'], instructor['CSC103'], meeting_time['CSC103']))
        elif command == '4':
            print("\nNET110: Room = {}, Instructor = {}, Meeting Time = {} \n"
                  .format(room_number['NET110'], instructor['NET110'], meeting_time['NET110']))
        elif command == '5':
            print("\nCOM241: Room = {}, Instructor = {}, Meeting Time = {} \n"
                  .format(room_number['COM241'], instructor['COM241'], meeting_time['COM241']))
        else:
            print("Invalid command\n")

        #Ask if the user wants to check another course or exit program
        check = input("Check another course?\nY = Yes. Any other character exits program : ")

        if check == 'y' or check == 'Y':
            print_menu()
            command = input("Enter next command : ")
        else:
            command = '0'

if __name__ == '__main__' : main()