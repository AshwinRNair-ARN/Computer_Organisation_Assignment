error=''
linenumber=1
linenumber_pass2=1
commands=[]

registers={
    'R0':'000',
    'R1':'001',
    'R2':'010',
    'R3':'011',
    'R4':'100',
    'R5':'101',
    'R6':'110',
    'FLAGS':'111',

}

opcode={
    'add': ("00000",'A',3),
    'sub': ("00001",'A',3),
    'mov': ("00010",'B',2),
    'mov2': ("00011",'C',2),  #fix this somehow
    'ld': ("00100",'D',2),
    'st': ("00101",'D',2),
    'mul': ("00110",'A',3),
    'div': ("00111",'C',2),
    'rs': ("01000",'B',2),
    'ls': ("01001",'B',3),
    'xor': ("01010",'A',3),
    'or': ("01011",'A',3),
    'and': ("01100",'A',3),
    'not': ("01101",'C',2),
    'cmp': ("01110",'C',2),
    'jmp': ("01111",'E',1),
    'jlt': ("10000",'E',1),
    'jgt': ("10001",'E',1),
    'je': ("10010",'E',1),
    'hlt': ("10011",'F',0),

}

variablesymbols={}
labelsymbols={}

errorlist={
'a':'Typos in instruction name or register name',
'b': 'Use of undefined variables',
'c': 'Use of undefined labels',
'd': 'Illegal use of FLAGS register',
'e': 'Illegal Immediate values (less than 0 or more than 255)',
'f': 'Misuse of labels as variables or vice-versa',
'g': 'Variables not declared at the beginning',
'h': 'Missing hlt instruction',
'i': 'hlt not being used as the last instruction',
'j': 'Wrong syntax used for instructions (For example, add instruction being used as a type B instruction)',
'k': 'General Syntax Error'
}




"""To accept till EOF and store each line in a list commands[]"""
def readdata():
    while True:                         
            try:
                line=input()
                commands.append(line)       
            except EOFError:
                break

def pass1():

    pc=0
    
    global error
    global variablesymbols
    global labelsymbols
    notvar=0

    global linenumber

    for line in commands:
        if line=='':
            linenumber+=1
            continue

        words=line.split()
        
        if words[0] =='var':    #check for variables
            if len(words) !=2:
                error='k'
                return
            elif not(words[1].replace('_', '').isalnum()):
                error='k'
                return

            elif notvar==1: # if its 1, it means variable is defined in middle
                error='g'
                return
            else:
                variablesymbols[words[1]]=None
                linenumber+=1
        

        elif words[0][-1]==':':
            if not(words[0][0:-1].replace('_', '').isalnum()):
                error='k'
                return
        
            elif words[1] not in opcode:
                error='a'
                return
            
            else:
                labelsymbols[words[0]]=pc
                notvar=1
                pc+=1
                linenumber+=1
                                           

        elif words[0] in opcode:
            notvar=1
            pc+=1          
            linenumber+=1 
      
        else:
        
            error='a'
            return
    
    for x in variablesymbols:
        variablesymbols[x]=pc
        pc+=1

def pass2(): 

    global linenumber_pass2
    global error
    
    for line in commands:
        if line=='':
            linenumber_pass2+=1
            continue
        
        words=line.split()

        if words[0] =='var':
            linenumber_pass2+=1
            continue

        elif:
            






    






def main():
    readdata()      # Read all data first
    pass1()         # first pass to set the variables and labels
    if error=='':
        print(variablesymbols)
        print(labelsymbols)
        pass2()


    else:
        print(errorlist[error],"at line",linenumber)


if __name__ == "__main__":
    main()


