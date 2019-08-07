
v =(easygui.fileopenbox())
v=("'"+v+"'")
str1=''
for i in v:
    if(i=='EOF'):
        break
    elif(i=='\\'):
        str1=str1+'/'
    else:
        str1=str1+str(i)
print(str1)




#print(os.path.normpath(var))
#var.replace('\\','/')


#import easygui
#easygui.egdemo()
