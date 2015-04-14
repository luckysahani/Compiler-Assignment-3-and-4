public class fibo {
	int asm;
    public int fib(int n) {
   //      int x;
   //      int y;
   //      int z;
	  //   if(n <= 1) {
			// // System.out.println(n);
	  //       return n;
	  //   } 
	  //   else {
	  //       x = fib(n-1);
	  //       y = fib(n-2);
	  //       z = x+y;
	  //       return z;
	  //   }
    	asm = 5;
    	return asm;
    }
}

public class fin{
	public int main(){
		fibo fibcal = new fibo();
		int a = fibcal.fib(10);
	    System.out.println(a);
		// int [] a = new  int [5]; 
	}
}