


public class dailyCodingHabitQuiz {
    private static int b(int i) {
        if (--i <= 1)
            return 1;
        else
            return(2 + b(i-1));
    }

     public static void main(String []a){
        System.out.print(b(4));
     }
}



