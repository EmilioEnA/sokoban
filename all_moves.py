
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


    def mover_derecha(self):
        # 0, 4 / 4, 0
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.personaje_columna += 1 
        # 0, 1, 4 / 4, 0, 1 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa [self.personaje_fila][self.personaje_columna+ 1 ] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 
            self.personaje_columna += 1 
        # 0, 2 / 4, 5
        elif self.mapa[self.personaje_fila][self.personaje_columna ] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna ] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 
            self.personaje_columna += 1 
        # 5, 4 / 6,0 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa [self.personaje_fila][self.personaje_columna + 1] == 4: 
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.personaje_columna += 1 
        # 0, 1, 2 / 4, 0, 6
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1 ] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 
            self.personaje_columna += 1  
        # 0, 6, 4 /  4, 5, 2
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5 
            self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 1 
            self.personaje_columna += 1 
        # 0, 6 , 2 / 4, 5, 6
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1 ] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6  
            self.personaje_columna += 1 
        # 5, 2 / 2, 5
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1]  == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2  
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5  
            self.personaje_columna += 1   
        # 5, 1, 4 / 2, 0, 1
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0  
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1 
        # 5, 1, 2 / 2, 0, 6
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 
            self.personaje_columna += 1 
        # 5 , 6, 4 / 2, 5, 1
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1
        # 5, 6, 2 / 2, 5, 6
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1


    def mover_izquierda(self):
        # 4, 0 - 0, 4 
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
        # 4, 5 - 0, 2
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
        # 4,1,0 / 1,0,4
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1
        # 2,1,0 / 6,0,4
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1]  = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2]  = 6
            self.personaje_columna -= 1
        # 4,6,0 / 1,5,4
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1

        # 2,6,0 / 6,5,4
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
        # 4,6 / 0,2
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
        # 2,5 / 5,2
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
        # 4,1,5 / 1,0,2
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1
        # 2,1,5 / 6,0,2
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
        # 4,6,5/ 1,5,2
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1
        # 2,6,5 / 6,5,2
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1

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

sokoban = Sokoban()
sokoban.jugar()
# se creo el juego y esta listo para jugarse