using System;

using System.Collections.Generic;
using System.Runtime.CompilerServices;

public class Estudianteone
{
    public string  Nombre {get; set;}
    public int Edad {get; set;}
    public  Double Promedio {get; set;}

     public  Estudianteone(string nombre , int edad  , double promedio)
    {
        Nombre = nombre;

        Edad = edad;

        Promedio = promedio;
        
    }


    public void MostrarInfor()
    {
        Console.WriteLine($"[OBJETO]   Estudiante: {Nombre} | Edad:{Edad} | Promedio:{Promedio} ");

    }



    public void SetPromedio(double nuevoPromedio)
    {
        Promedio = nuevoPromedio;
    }


}


class Progra

{
    
    static void Main()
    {
        

        List<Estudianteone> listaObjetos = new List<Estudianteone>();

        listaObjetos.Add(new Estudianteone("jorge pantoja", 21 ,4.0));
        listaObjetos.Add(new Estudianteone("carlos molano ", 23 ,5.0));
        listaObjetos.Add(new Estudianteone("andres bravo ", 30 ,3.0));



        Console.WriteLine("----Informacion en el objeto------");
        foreach (var est in listaObjetos)
        {
            est.MostrarInfor();
        }

        listaObjetos[1].SetPromedio(4.2);
        Console.WriteLine($"\bPromedio modificado para {listaObjetos[1].Nombre}:");
        listaObjetos[1].MostrarInfor();
    }
}