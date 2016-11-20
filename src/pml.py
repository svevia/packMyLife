import sys
from Target import Target

def init():
    print("PML")
    firstname = input("Firstname: ")
    lastname = input("lastname: ")
    dateOfBirth = input("date of birth [DD/MM/YYYY] : ").split('/')
    postCode = input("post code : ")

    furtherInformation = []
    info = 'a'
    while(info!=''):
        info = input("furtherInformation : ")
        if(info != ''):
            furtherInformation.append(info)



    target = Target(firstname, lastname, dateOfBirth, postCode, furtherInformation)
    return target

def generate(target,level=1):
    count = 0
    delimiter = ['-','.',' ','_', '/','']
    end = ['.','?','!','']
    if target.postCode != '':
        end.append(target.postCode[:2])
        end.append(target.postCode)
    if target.dateOfBirth != ['']:
        end.append(target.dateOfBirth[2])
        end.append(target.dateOfBirth[2][-2:])

    ### print basic password (only 1 parameter)
    print (target.firstname)
    print (target.lastname)
    count += 2

    ### generate basic password with first name and lastname
    for d in delimiter:
        for e in end:
            print(target.firstname,d,target.lastname,e,sep='')
            print(target.lastname,d,target.firstname,e,sep='')
            count += 2

    print(count, "password generated")


    
def main():
    target = init()
    for i in sys.argv:
        if(i == '-c'):
            commonPass = True
        elif(i.startswith('-o')):
            file = i.split("=",2)[1]
        elif(i.startswith('-l')):
            level = i.split("=",2)[1]
    generate(target)


if __name__ == "__main__":
    main()

    
