public class prime
{
	public static void main ()	{
	 	int count = 0, n = 12;
	 	int i;
		if (n == 1) {
			System.out.println("Given number is neither prime nor composite");
		}
	 	else {
	    	if (n == 2) {
	     		System.out.println("Given number is prime");
	    	}
	     	else {
	     		for ( i = 2; i < n; i++ ) {
	         		if (n % i == 0) {
	         			count = count + 1;
	         		}
	     		}
	     	}
	 	}

	 	if (count > 0)
			System.out.println("Given number is not Prime");
 		else
 			System.out.println("Given number is prime");
	}
}