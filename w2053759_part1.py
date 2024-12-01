# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 20222066
# Date: 01/12/2023

import w2053759_part1_4
import w2053579_part3

#Variable Initialization
passes = 0
defer = 0
fail = 0
result=''
repeat = ''
data=[]
accepted = True
progress_count=0
trailer_count=0
retriver_count=0
exclude_count=0
check=''

def Check_Validity(value):
    "To check validity of input"
    try:
        value = int(value)
        if value not in [0,20,40,60,80,100,120]:
            print ('Out of range\n')
            accepted = True
        else:
            accepted = False
    except ValueError:
        print ('Integer required\n')
        accepted = True
    return (accepted)

def Quit_function():
    while True:
        print('\nWould you like to enter another set of data?')
        repeat = input("Enter 'y' for yes or 'q' to quit and view results:")
        repeat.lower()
        print('')

        if (repeat == 'y'):
            break
        elif (repeat == 'q'):
            break
        else:
            print('\nInvalid command Retry')
            continue
    return(repeat)

def check_student_or_teacher():
    print('This Program is to predict progression outcome at the end of each academic year.')
    while True:
        check=input("\nIf you are a student enter '1' or if your a staff member enter '2': ")
        if check=='1' or check=='2':
            print('')
            break
        else:
            print('\nInvalid command Retry')
            continue
    return(check)

check=check_student_or_teacher()

while True:
    while accepted:
        passes=input('Please enter your credits at pass:')
        accepted=Check_Validity(passes)
    accepted = True
    while accepted:
        defer=input('Please enter your credit at defer:')
        accepted=Check_Validity(defer)
    accepted = True
    while accepted:
        fail = input('Please enter your credit at fail:')
        accepted=Check_Validity(fail)
    accepted = True    

    #after checking validity making inputs to integer
    passes=int(passes)      
    defer=int(defer)
    fail=int(fail)

    if (passes+defer+fail != 120):
        print('Total incorrect\n')
        continue   
    elif (passes == 120):
        result='Progress'
        progress_count += 1
    elif (passes == 100):
        result='Progress (module trailer)'
        trailer_count += 1
    elif (fail < 80):
        result='Do not progress - module retriever'
        retriver_count += 1
    elif (fail >= 80):
        result='Exclude'
        exclude_count += 1
    print(result)
    
    if check=='1':
        break

    #part 2
    data.append(f'{result} - {passes}, {defer}, {fail}')

    repeat=Quit_function()

    if (repeat == 'q'):
        #histogram
        w2053759_part1_4.histogram(int(progress_count),int(trailer_count),int(retriver_count),int(exclude_count)) 

        #part 2
        print('Part 2:')
        for item in data:
            print(item)

        #part 3
        w2053579_part3.create_textfile(data)
        break
