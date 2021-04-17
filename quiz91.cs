
using System;
public class Program
{
    public static void Main()
    {
        string daily = "Daily Coding Habit";
        int coding = daily.IndexOf("i");
        int habit = coding | 2;
        habit <<= 2;
        Console.WriteLine(daily[habit]); 
    }
}


// d