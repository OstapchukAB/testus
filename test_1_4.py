#child-parent
namespace={"global":"global"}
vars_in_ns={}



n=int(input())
idx_namespace=0
idx_vars=0
for _ in range(n):
    s=input()
    s=s.split()
    if s[0]=="create":       
         parent = namespace.get(s[2])
         child=namespace.get(s[1])
         if parent==None or child==None:
              namespace[s[1]]=s[2]
    elif s[0]=="add":
          ns = namespace.get(s[1])
          v=f"{s[1]}-{s[2]}"
          if ns:
            var_=vars_in_ns.get(v)
            if var_==None:
                       vars_in_ns[v]=s[2]
    elif s[0]=="get":
        if f"{s[1]}-{s[2]}" in vars_in_ns:
            print(s[1])
        else : ## если нашли сразу то поищеи есть ли она вообще
            for k,v in vars_in_ns.items():
                 if v==s[2]: # где-то есть
                    print("Необходимо поискать в верхнем пространстве имен")  #тут поискать в верхнем пространстве имен
            else:# нет вообще в списке
                print("None")

                       
                       
                         
                    
               
            




        
