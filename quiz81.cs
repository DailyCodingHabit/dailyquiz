

using System;				
public class Quiz
{
	public static void Main()
	{
        string coding = "123";
    	char [] destination = { 'D', 'a', 'i', 'l', 'y'};
        coding.CopyTo ( 0, destination, 2, coding.Length );
		char habit = '.';
		Console.WriteLine(coding.PadRight(5, habit));
	}
}



// 123..