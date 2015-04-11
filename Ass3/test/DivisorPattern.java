public class DivisorPattern {

    public static void main(String[] args) { 
        int N = Integer.parseInt(args[0]);

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                if (i % j == 0 || j % i == 0) {
                    System.out.print("* "); 
                }
                else {
                    System.out.print("  "); 
                }
            }
            System.out.println(i);
        }
    }
}
