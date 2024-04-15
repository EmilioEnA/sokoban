
class Sokoban:

    Personaje = 0
    Cajas = 1
    Metas = 2
    Paredes = 3
    Piso = 4
    Pesonaje_meta = 5
    Caja_meta = 6

    def __init__(self):
        # Define el mapa de juego
        self.mapa = [

           [3,3,3,3,3,3,3,3,3,3],
           [3,4,4,4,4,4,4,4,4,3],
           [3,4,1,4,4,4,1,4,4,3],
           [3,3,3,3,4,4,3,3,4,3],
           [3,4,4,4,4,3,4,4,4,3],
           [3,3,3,4,0,4,4,4,4,3],
           [3,2,2,3,4,4,4,4,4,3],
           [3,4,4,4,4,4,4,4,4,3],
           [3,4,4,4,4,4,4,4,4,3],
           [3,3,3,3,3,3,3,3,3,3]
        ]


        self.personaje_columna = 4
        self.personaje_fila = 5
        #posicion inicial del psj
    

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)


    def mover_arriba(self):
        # 29 Personaje, espacio
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] =0
            self.personaje_fila -=1
        # 30 Personaje, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5
            self.personaje_fila -=1
        # 31 Personaje, caja, espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -=1
        # 32 Personaje, caja, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        # 33  Personaje, caja_meta, espacio 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        # 34 Personaje, caja_meta, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        # 35 Personaje_meta, espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.personaje_fila -=1
        # 36 Personaje_meta, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila -=1
        # 37 Personaje_meta, caja, espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -=1
        # 38 Personaje_meta, caja, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        # 39 Personaje_meta, caja_meta, espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -=1
        # 40 Personaje_meta, caja_meta, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        
    def mover_abajo(self):
        # 41 Personaje, espacio
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] =0
            self.personaje_fila +=1
        # 42 Personaje, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5
            self.personaje_fila +=1
        # 43 Personaje, caja, espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila +=1
        # 44 Personaje, caja, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila +=1
        # 45 Personaje, caja_meta, espacio 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila +=1
        # 46 Personaje, caja_meta, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila +=1
        # 47 Personaje_meta, espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.personaje_fila +=1
        # 48 Personaje_meta, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.personaje_fila +=1
        # 49 Personaje_meta, caja, espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila +=1
        # 50 Personaje_meta, caja, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila +=1
        # 51 Personaje_meta, caja_meta, espacio
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila +=1
        # 52 Personaje_meta, caja_meta, meta
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila +=1


 

    def jugar(self):
        while True:
            self.imprimirMapa()
            movimiento = input(" !! Usa las teclas w/a/s/d como si fuern las flechas y escribe salir para abandonar el juego:  ")
            if movimiento == 'd':
                self.mover_derecha()
            elif movimiento == 'a':
                self.mover_izquierda()
            elif movimiento == 'w':
                self.mover_arriba()
            elif movimiento == 's':
                self.mover_abajo()
            elif movimiento == 'salir':
                exit()
    def nivel_completado(self):
        for fila in self.mapa:
         for elemento in fila:
             if elemento == 1: #si aun hay cajas no se termina 
                 return False
        return True #si ya no hay cajas ganas

sokoban = Sokoban()
sokoban.jugar()
# se creo el juego y esta listo para jugarse
