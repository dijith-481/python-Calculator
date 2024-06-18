print("CALCULATOR")
num=[[]]
operators={'+','-','*','/','^'}
str=''
x=''
prev=''
pos=0
paren=0
def oper(minimum):
    match num[pos][minimum]:
        case '*':
            return num[pos][minimum-1]*num[pos][minimum+1]
        case '/':
            if num[pos][minimum+1] == 0:
                return ZeroDivisionError("Division by zero")
            else:
                return num[pos][minimum-1]/num[pos][minimum+1]
        case '-':
            return num[pos][minimum-1]-num[pos][minimum+1]
        case '+':
             return num[pos][minimum-1]+num[pos][minimum+1]
        case '^':
             return num[pos][minimum-1]**num[pos][minimum+1]
def calc():
    while num[pos].count('^')>0:
        minimum=num[pos].index('^')
        num[pos][minimum-1]=oper(minimum)
        num[pos].pop(minimum)
        num[pos].pop(minimum)
    while num[pos].count('*')+num[pos].count('/')>0:
        if num[pos].count('*')>0:
            index1=num[pos].index('*')
        else:
            index1=99
        if num[pos].count('/')>0:
            index2=num[pos].index('/')
        else:
            index2=99
        minimum=min(index1,index2)
        num[pos][minimum-1]=oper(minimum)
        num[pos].pop(minimum)
        num[pos].pop(minimum)
    while num[pos].count('-')>0:
        minimum=num[pos].index('-')
        num[pos][minimum-1]=oper(minimum)
        num[pos].pop(minimum)
        num[pos].pop(minimum)
    while num[pos].count('+')>0:
        minimum=num[pos].index('+')
        num[pos][minimum-1]=oper(minimum)
        num[pos].pop(minimum)
        num[pos].pop(minimum)
    return num[pos][0]

def check(x,prev,pos,paren,str):
    if x=='(' and prev=='' :
        str+=x
        paren +=1
        pos+=1
        num.append([])
    elif x==')' and paren >0 :
        str+=x
        paren -=1
        num[pos].append(float(prev))
        prev=calc()
        num.pop(-1)
        pos-=1
    elif x=="=":
        str+=x
        num[pos].append(float(prev))
        prev=calc()
        num.pop(-1)
        pos-=1
    elif x in operators and prev !='':
        str+=x
        num[pos].append(float(prev))
        num[pos].append(x)
        prev=''
    elif x.isdigit() or x=='.':
        str+=x
        prev+=x

    return prev,pos,paren,str

    
while x!="=":
    x=input('')
    prev,pos,paren,str =check(x,prev,pos,paren,str)
    print(str)
print(prev)   
