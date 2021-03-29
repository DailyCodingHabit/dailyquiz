




using System;			
public class Quiz
{
	public static void Main()
	{
		string daily = "codinghabit";
		string a = "";
		foreach (char c in daily) {
			if (c >= 'm') {
				a += c;
			}
		}
		Console.Write(a);
	}
}

