
using System;				
public class Quiz
{
	public static void Main()
	{
		string daily = "codinghabit";
		daily = daily.Remove(4,4);
		daily = daily.Insert(4,"e");
		Console.WriteLine(daily);
	}
}


