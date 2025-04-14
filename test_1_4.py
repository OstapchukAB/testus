#current:parent
namespace={"global":""}
vars_in_ns={}

def create(nm_current,nm_parent):
    parent = namespace.get(nm_current)
    if parent !=nm_parent:
        namespace[nm_current]=nm_parent

def add(nm_current,varname):
    ns = namespace.get(nm_current)
    if ns:
        varrs=vars_in_ns.get(nm_current)
        if varrs:
            if varname not in varrs:
                vars_in_ns[nm_current]=varrs.add(varname)
def get_nm_for_var(nm,varname):
    parent=namespace.get(nm)
    varss= vars_in_ns.get(nm) #проверим в текущем namespace
    if varss and varname in varss:#нашли возвращаем
        return nm
    elif parent=="" and varname not in varss:#если в глобальном простарнстве дальше идти некуда
        return None
        #поищем на верхнем уровне
    elif parent:
        return get_nm_for_var(parent,varname)



n=int(input())
for _ in range(n):
    s=input()
    s=s.split()
    if s[0]=="create":       
        create(s[1],s[2])
    elif s[0]=="add":
        add(s[1],s[2])
    elif s[0]=="get":
        get_nm_for_var(s[1],s[2])

                       
                       
                         
                    
               
            




        
