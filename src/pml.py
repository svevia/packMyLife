import sys
from Target import Target

def init():
    print("PML")
    firstname = input("Firstname: ")
    lastname = input("lastname: ")
    dateOfBirth = input("date of birth [DD/MM/YYYY] : ")
    postCode = input("post code : ")

    furtherInformation = []
    info = 'a'
    while(info!=''):
        info = input("furtherInformation : ")
        if(info != ''):
            furtherInformation.append(info)



    target = Target(firstname, lastname, dateOfBirth, postCode, furtherInformation)
    return target



    


def main():
    target = init()
    for i in sys.argv:
        if(i == '-c'):
            commonPass = True
        elif(i.startswith('-o')):
            file = i.split("=",2)[1]






if __name__ == "__main__":
    main()

    
