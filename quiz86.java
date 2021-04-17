

public class DailyCodingHabit{  
    public static void main(String args[]){      
        int a[][]= {{1,2,3},{1,2,3}};    
        int b[][]= a;  
        for(int i=0;i<2;i++) {    
            for(int j=0;j<2;j++) {       
                a[i][j]+=a[i][j]*b[i][j];      
            }    
        }    
        System.out.print(a[1][1]); 
    }
}  


// 8