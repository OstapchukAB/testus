#current:parent
namespace={"global":"-"}
namespaces_vars={"global":[]}

def create(nm_current,nm_parent):
    parent = namespace.get(nm_current)
    if parent !=nm_parent:
        namespace[nm_current]=nm_parent
        namespaces_vars[nm_current]=[]

def add(nm_current,varname):
    ns = namespace.get(nm_current)
    if ns:
        varrs=namespaces_vars.get(nm_current)
        if varname not in varrs:
            namespaces_vars[nm_current].append(varname)
def get_nm_for_var(nm,varname):
    parent=namespace.get(nm)
    varss= namespaces_vars.get(nm) #проверим в текущем namespace
    if varss and varname in varss:#нашли возвращаем
        return nm
    elif parent=="-" and varname not in varss:#если в глобальном простарнстве дальше идти некуда
        return None
        #поищем на верхнем уровне
    elif parent:
        return get_nm_for_var(parent,varname)



#n=int(input())
n=9
w=["add global a","create foo global","add foo b","get foo a","get foo c","create bar foo","add bar a","get bar a","get bar b"]
for i in range(n):
   # s=input()
    s=w[i]
    s=s.split()
    if s[0]=="create":       
        create(s[1],s[2])
    elif s[0]=="add":
        add(s[1],s[2])
    elif s[0]=="get":
        result=get_nm_for_var(s[1],s[2])
        print(result)

                       
                       
                         
                    
               
            




        
