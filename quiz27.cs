

using System;		
public class Quiz
{
	public static void Main()
	{
		int a = 8;
		double b = 4.5;
		a++;
		double c = Math.Floor(a++ %4 + b);
		Console.Write(c);
	}
}

