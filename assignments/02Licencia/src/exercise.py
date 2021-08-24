
def main():
    #Escribe tu código debajo de esta línea
    def mine():
        if edad <18:
            print ("No cumples requisitos") 
        else:
            edad>=18
            ID=str(input("¿Tienes identificación oficial? (s/n):"))
        if ID =="s":
            print ("Trámite de licencia concedido")
        if ID =="n":
            print ("No cumples requisitos") 
        if (ID != "s") and (ID != "n"):
            print ("Respuesta incorrecta")
    edad=int(input("Ingresa tu edad:"))
    mine ()
    pass


if __name__ == '__main__':
    main()
