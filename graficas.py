import matplotlib.pyplot as plt  # necesario para las graficas


# metodo para graficar todas las estrellas
def allstars():
    plt.figure()  # nueva figura

    text = "stars.txt"
    f = open(text, encoding='utf8').read()
    cad = f.splitlines()

    equis = []  # arreglo de coords x
    yes = []    # arreglo de coords y

    for x in cad:
        star = x.split()
        x = float(star[0])
        y = float(star[1])
        equis.append(x)
        yes.append(y)

    with plt.style.context('dark_background'):
        plt.scatter(equis, yes, 1, marker='*', color='white')
        # se decidio dar como limites de los ejes -1.3 y 1.3 
        # ya que se queria dar un poco de espacio a la grafica
        # teniendo en cuenta que las estrellas se encuentran
        # ubicadas entre -1 y 1.
        plt.axis([-1.3,1.3,-1.3,1.3])
        plt.title("Estrellas")
        plt.xlabel("Coord. X")
        plt.ylabel("Coord. Y")
        plt.savefig("allstars.png")


# como en este metodo se grafican las estrellas,
# las partes dedicadas a las estrellas se podrian 
# cambiar por el metodo de allstars() sin embargo
# el metodo allstars contiene un plt.figure el cual
# haria una sobrecarga de figuras al metodo y no
# funcionaria de manera adecuada.
def cns(name):     
    text = "stars.txt"    # para las estrellas
    f = open(text, encoding='utf8').read()
    cad = f.splitlines()
    # la creacion del array de estrellas con nombre
    connombre = []
    # debido a que el metodo tiene como parametro
    # una cad de caracteres que seria el nombre de
    # x constelacion, este metodo lo que hace es
    # reemplazar el nombre de la constelacion con
    # el fin de usar su archivo y realizar la debida
    # graficacion de la constelacion
    constela = "constelaciones/"+name+".txt"
    d = open(constela, encoding='utf8').read()
    cad2 = d.splitlines()
    equis= []
    yes = []
    plt.figure()
    # con el siguiente metodo se recogen
    # las coordenadas x y y de cada estrella
    # con el fin de graficarlas todas, tal y
    # como se hace el metodo allstars()
    for x in cad:
            star = x.split()
            x = float(star[0])
            y = float(star[1])
            equis.append(x)
            yes.append(y)

    # en el sgte para se crea un arreglo
    # con cada una de las estrellas que
    # tienen nombre, esto con el fin de
    # buscar de manera rápida las coords
    # de las estrellas que se encuentren
    # en una constelacion. 
    # no es un metodo necesario ya que 
    # de igual manera se podía buscar en
    # el archivo stars.txt.
    for x in cad: 
        star = x.split()                             
        if len(star) > 6:       # al tener mas que 6 casillas se garantiza
            connombre.append(x) # el hecho de que la estrella tenga nombre.


    for x in cad2: #para cada union de estrellas en la cons
        strellas = x.split(',') # dividimos para tener cada estrella de cada par
        es = []  # arreglo para coords x de cada par de estrellas
        im = []  # arreglo para coords y de cada par de estrellas
        for m in strellas: #para cada estrella
            for j in connombre: #para cada estrella con nombre se busca si tiene el mismo nombre
                if m in j:
                    aux = j.split() #separa por espacio la info de cada estrella
                    es.append(float(aux[0])) # x's de las estrellas
                    im.append(float(aux[1])) # y's de las estrellas
        with plt.style.context('dark_background'):
            plt.scatter(equis, yes, 1, marker='*', color='white')
            plt.axis([-1.3,1.3,-1.3,1.3])
            plt.title(name)
            plt.xlabel("Coord. X")
            plt.ylabel("Coord. Y")
            plt.plot(es,im, color='red')
            plt.savefig(name+".png")

def allcns(): 
    # plt.figure() crea una nueva figura
    # para que no se superpongan las graficas
    # de los otros metodos.
    plt.figure()  

    # el archivo de nombrescns no fue dado
    # por el enunciado pero es creado con
    # el fin de tener un archivo con el 
    # nombre de todas las constelaciones.
    filename = "nombrescns.txt"   
    nombrescns = open(filename, encoding='utf8').read()
    nombrescns = nombrescns.splitlines()  # splitlines necesario para
    for x in nombrescns:                  # dividir por lineas el archivo.

        # este for para cada constelacion sirve
        # para dibujar cada una de las constelaciones
        text = "stars.txt"
        f = open(text, encoding='utf8').read()
        cad = f.splitlines()
        connombre = []
        constela = "constelaciones/"+x+".txt"
        # con esto se lee el archivo de cada
        # una de las constelaciones en cada
        # ciclo que realice el para.
        d = open(constela, encoding='utf8').read()
        cad2 = d.splitlines()
        equis= []  # arreglo de coords x
        yes = []   # arreglo de coords y

        # en el sgte para se recogen las coords
        # x y y de cada una de las estrellas en
        # el archivo stars.txt con el fin de 
        # graficarlas.
        for x in cad:
                star = x.split()
                x = float(star[0])
                y = float(star[1])
                equis.append(x)
                yes.append(y)

        # en el sgte para se crea un arreglo
        # con cada una de las estrellas que
        # tienen nombre, esto con el fin de
        # buscar de manera rápida las coords
        # de las estrellas que se encuentren
        # en una constelacion. 
        # no es un metodo necesario ya que 
        # de igual manera se podía buscar en
        # el archivo stars.txt.
        for x in cad: 
            star = x.split()                             
            if len(star) > 6:
                connombre.append(x)


        for x in cad2: #para cada union de estrellas en la cons
            strellas = x.split(',')  # dividimos para obtener el
            es = []                  # nombre de las dos estrellas
            im = []                  # en cada union.
            for m in strellas: #para cada estrella de la union
                for j in connombre: # para cada estrella connombre
                    if m in j:      # se busca la estrella.
                        aux = j.split() #separa por espacio la info de cada estrella
                        es.append(float(aux[0])) # x's de las estrellas
                        im.append(float(aux[1])) # y's de las estrellas
            # el estilo 'dark background' da un aspecto oscuro
            # a la grafica para simular las estrellas en el 
            # firmamento.
            with plt.style.context('dark_background'):
                plt.scatter(equis, yes, 1, marker='*', color='white')
                plt.axis([-1.3,1.3,-1.3,1.3])
                plt.title("All Const. & Stars")
                plt.xlabel("Coord. X")
                plt.ylabel("Coord. Y")
                plt.plot(es,im, color='red')
                plt.savefig("allcons.png")

allcns()