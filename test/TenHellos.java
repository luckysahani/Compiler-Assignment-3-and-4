
public class TenHellos { 
   public static void main(String[] args) {

      // print out special cases whose ordinal doesn't end in th
      System.out.println("1st Hello");
      System.out.println("2nd Hello");
      System.out.println("3rd Hello");

      // count from i = 4 to 10
      int i = 4;
      while (i <= 10) {
         System.out.println(i + "th Hello");
         i = i + 1;
      }

   }
}
