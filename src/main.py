# ================= FUNCTION =================
def conversion(tipo_pesos, valor_dolar):
  pesos = float(input("¿Cuantos " + tipo_pesos + " " + "tienes?: " ))
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes $" + dolares +  " dolares")

# ================= MENU =================
menu = """
********************************
BIENVENIDO AL
    __   ___   ____   __ __    ___  ____    _____  ___   ____      
   /  ] /   \ |    \ |  |  |  /  _]|    \  / ___/ /   \ |    \     
  /  / |     ||  _  ||  |  | /  [_ |  D  )(   \_ |     ||  D  )    
 /  /  |  O  ||  |  ||  |  ||    _]|    /  \__  ||  O  ||    /     
/   \_ |     ||  |  ||  :  ||   [_ |    \  /  \ ||     ||    \     
\     ||     ||  |  | \   / |     ||  .  \ \    ||     ||  .  \    
 \____| \___/ |__|__|  \_/  |_____||__|\_|  \___| \___/ |__|\_|    
                                                                   
  _____  ______ 
 |  __ \|  ____|
 | |  | | |__   
 | |  | |  __|  
 | |__| | |____ 
 |_____/|______|
                                    
  __  __  ____  _   _ ______ _____           _____ 
 |  \/  |/ __ \| \ | |  ____|  __ \   /\    / ____|
 | \  / | |  | |  \| | |__  | |  | | /  \  | (___  
 | |\/| | |  | | . ` |  __| | |  | |/ /\ \  \___ \ 
 | |  | | |__| | |\  | |____| |__| / ____ \ ____) |
 |_|  |_|\____/|_| \_|______|_____/_/    \_\_____/ 
                                                   
____________________________________________________________

[1] - Pesos colombianos
[2] - Pesos argentinos 
[3] - Pesos mexicanos
_____________________________________________________________
Escribe el indice de la opcion que deseas convertir a dolares: """
opcion = input(menu)


# ================= CONDICION IF =================
if opcion == '1':
  conversion("Pesos colombianos", 3875)
elif opcion == '2':
  conversion("Pesos argentinos", 65)

elif opcion == '3':
  conversion("Pesos mexicanos", 24)

else: 
  print("""
  *******************************
              ERROR
  *******************************
  Introduce un indice valido!
  """)
  

