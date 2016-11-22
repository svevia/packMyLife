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

def generateBasic(target,level,f):
    count = 0
    delimiter = ['','.',' ',',']
    end = ['.','?','!','']
    inter = ['']

    
    if level >= 3:
        delimiter.append('_')
    if level >= 5:
        delimiter.append('/')
        delimiter.append(':')

    
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
                ## Without capital
                print(target.firstname,d,target.lastname,i,e,file=f,sep='')
                print(target.lastname,d,target.firstname,i,e,file=f,sep='')

                ## First letter of first word in capital
                print(target.firstname.title(),d,target.lastname,i,e,file=f,sep='')
                print(target.lastname.title(),d,target.firstname,i,e,file=f,sep='')

                ## First letter of every word in capital
                print(target.firstname.title(),d,target.lastname.title(),i,e,file=f,sep='')
                print(target.lastname.title(),d,target.firstname.title(),i,e,file=f,sep='')

                ## First letter of last word in capital
                print(target.firstname,d,target.lastname.title(),i,e,file=f,sep='')
                print(target.lastname,d,target.firstname.title(),i,e,file=f,sep='')
                count += 8


    count += generateFurther(target,level,f,end,inter)
    print(count, "password generated")

def generateFurther(target,level,f,end,inter):
    count = 0
    for p in target.furtherInformation:
        print(p,file=f,sep='')
        print(p.title(),file=f,sep='')
        count += 2
        for e in end:
            for i in inter:
                print(p,i,e,file=f,sep='')
                print(p.title(),i,e,file=f,sep='')
                count += 2

    return count
    
    
def main():
    file = sys.stdout
    level = 1

    i=1
    while i < len(sys.argv):
        if(sys.argv[i] == '-c'):#add common password to the list
            i+=1
            commonPass = sys.argv[i]
        elif(sys.argv[i].startswith('-o')):#output in a file
            i+=1
            file = open(sys.argv[i],'w')
        elif(sys.argv[i].startswith('-l')):#change the level
            i+=1
            level = int(sys.argv[i])
        else:
            print("Don't know the option", sys.argv[i])
            sys.exit()
        i+=1
    target = init()
    generateBasic(target,level, file)


if __name__ == "__main__":
    main()

    
