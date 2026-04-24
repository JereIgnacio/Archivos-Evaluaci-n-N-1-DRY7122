acl = int(input("Ingresa numero de ACL: "))
 
if (1 <= acl <= 99) or (1300 <= acl <= 1999):
    print("ACL Estandar")
elif (100 <= acl <= 199) or (2000 <= acl <= 2699):
    print("ACL Extendida")
else:
    print("No corresponde a una ACL")










