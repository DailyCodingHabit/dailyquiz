



// File: SingleObject.java
public class SingleObject {
   private static SingleObject instance = new SingleObject();

   private SingleObject(){}

   //Get the only object available
   public static SingleObject getInstance(){
      return instance;
   }

   public void showMessage(){
      System.out.println("Hello DailyCodingHabit!");
   }
}

// File: Main.java
public class Main {
   public static void main(String[] args) {
      SingleObject object = SingleObject.getInstance();

      object.showMessage();
   }
}



