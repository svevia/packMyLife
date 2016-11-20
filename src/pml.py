import sys
from Target import Target

def init():
    print("PML")
    firstname = input("Firstname: ").lower()
    lastname = input("lastname: ").lower()
    dateOfBirth = input("date of birth [DD/MM/YYYY] : ").split('/')
    postCode = input("post code : ")

    furtherInformation = []
    info = 'a'
    while(info!=''):
        info = input("furtherInformation : ").lower()
        if(info != ''):
            furtherInformation.append(info)



    target = Target(firstname, lastname, dateOfBirth, postCode, furtherInformation)
    return target

def generate(target,level,f):
    count = 0
    delimiter = ['-','.',' ','_', '/','']
    end = ['.','?','!','']
    inter = ['']
    if target.postCode != '':
        inter.append(target.postCode[:2])
        inter.append(target.postCode)
    if (target.dateOfBirth != ['']) & (len(target.dateOfBirth) == 3):
        inter.append(target.dateOfBirth[2])
        inter.append(target.dateOfBirth[0]+target.dateOfBirth[1])
        inter.append(target.dateOfBirth[2][-2:])
        

    ### print basic password (only 1 parameter)
    print (target.firstname,file=f)
    print (target.lastname,file=f)
    count += 2

    ### generate basic password with first name and lastname
    for d in delimiter:
        for e in end:
            for i in inter:
                print(target.firstname,d,target.lastname,i,e,file=f,sep='')
                print(target.lastname,d,target.firstname,i,e,file=f,sep='')
                count += 2

    print(count, "password generated")


    
def main():
    file = sys.stdout
    level = 1
    target = init()
    for i in sys.argv:
        if(i == '-c'):
            commonPass = True
        elif(i.startswith('-o')):
            file = open(i.split("=",2)[1],'w')
        elif(i.startswith('-l')):
            level = i.split("=",2)[1]
    generate(target,level, file)


if __name__ == "__main__":
    main()

    
