
using System.IO;
using System;
class Program
{
    static void Main()
    {
        string b = "True";
        bool daily, habit = false;
        daily = habit == false;
        if(daily != (habit != bool.Parse(b))) {
            Console.Write(b);
        } else {
            Console.WriteLine(!daily);
        }
    }
}





