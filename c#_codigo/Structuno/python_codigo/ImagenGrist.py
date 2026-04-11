
class ImagenGris:
    def __init__(self, ancho, alto, pixeles):
        self.ancho = ancho
        self.alto = alto
        self.pixeles = pixeles
    
    def invertir_colores(self):
        for y in range(self.alto):
             for x in range(self.ancho):
                 self.pixeles[y][x] = 255 - self.pixeles[y][x]
                 
                 
    def ajustar_brillo(self, ajuste):
       for  y in range(self.alto):
          for x in range(self.ancho):
            nuevo_valor = self.pixeles[y][x] + ajuste
            self.pixeles[y][x] = max(0, min(255, nuevo_valor))
            
            
            
    def detectar_bordes(self):
        bordes_pixeles = [[0 for _ in range(self.ancho)] for _ in  range(self.alto)]                 
        for y in range(self.alto - 1):
            for x in range(self.ancho - 1):
                diff_x = abs(self.pixeles[y][x] - self.pixeles[y][x+1])
                diff_y = abs(self.pixele[y][x]  - self.pixeles[y+1][x]) 
                bordes_pixeles[y][x] = max(diff_x , diff_y)
        return ImagenGris(self.ancho, self.alto, bordes_pixeles)
  
  
  
  
    def imprimir (self):
      for fila in self.pixeles:
          print(" ".join(f"{p:03}" for p in fila))
          
      print()
          
          
          
if __name__ == "__main__":          
    matriz_inicial = [
        [50, 100, 150, 200],
        [50, 100, 150, 200],
        [50, 100, 150, 200],
        [50, 100, 150, 200]    
    ]
          
    img = ImagenGris(4 , 4, matriz_inicial)
 
 
    print ("----Imagen Original ---")
    img.imprimir() 
 
    img.invertir_colores()
    print("--Imagen Invertida aqui----")
    img.imprimir()


    img.ajustar_brillo(50)
    print("----imagen Aclarada ---")
    img.imprimir()         
                          

          

                          
