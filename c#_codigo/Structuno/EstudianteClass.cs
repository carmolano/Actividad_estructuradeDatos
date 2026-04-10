using System;




public struct EstudianteStruct {
    public string nombre;
    public int edad;
    public double promedio;

 public EstudianteStruct(string n , int e , double p ) {
        nombre = n ;
        edad = e ;
        promedio = p;


    }
}
class ProgramPrueba {
    static void Main() {

EstudianteStruct[] lista = {
          new EstudianteStruct("Jorge",21,4.0),
          new EstudianteStruct("Carlos", 23,5.0),
          new EstudianteStruct("Andres", 30, 3.5)

 };

    Console.WriteLine("---Punto 3: recorrio de  structs----");
    foreach (var est in lista) {
            Console.WriteLine($"Nombre:{est.nombre}, Promedio:{est.promedio}");
        

 

 lista[1].promedio = 4.8;
 Console.WriteLine($"\nPromedio actualizado de {lista[1].nombre}:{lista[1].promedio}");
    }

   }

}

  



