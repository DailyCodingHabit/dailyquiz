

public class DailyCodingHabit{
     public static void main(String []args){
        int[] array1 = {1,2,3,4,5,6};
        int[] array2 = {0,0,0,0,0,0};
        System.arraycopy(array2,2,array1,2,2);
        for (int i : array2)
            System.out.print(i);
     }
}


// 000000