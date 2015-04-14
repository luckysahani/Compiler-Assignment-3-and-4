public class SwapElementsExample {
 
 
        private static void swap(int num1, int num2) {
               
                int temp = num1;
                num1 = num2;
                num2 = temp;
               
                System.out.println("\nAfter Swapping\n");
                System.out.println(num1);
                System.out.println(num2);
               
        }
        public static void main() {
               
                int num1 = 10;
                int num2 = 20;
               
                System.out.println("\nBefore Swapping\n");
                System.out.println(num1);
                System.out.println(num2);
               
                //swap the value
                swap(num1, num2);
        }
}