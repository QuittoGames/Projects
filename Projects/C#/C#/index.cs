using System;
using data;

namespace index
{
    class Program
    {
        static void Main(string[] args)
        {
            // Acessando diretamente a variável 'idade' estática da classe Data
            Console.WriteLine("Hello, World!");
            Console.ReadLine();
            Console.WriteLine("Idade: " + Data.idade);  // Acessando a variável estática diretamente
        }
    }
}
