public class PrimitiveParameters
{	
	public static void falsSwap(int x, int y)
	{	
		System.out.println("In falseSwap go. x: ");
		System.out.println(x);
		System.out.println(" y: ");
		System.out.println(y);
		int temp = x;
		x = y;
		y = temp;
		System.out.println("In falseSwap go. x: ");
		System.out.println(x);
		System.out.println(" y: ");
		System.out.println(y);
	}
	
	public static void moreParameters(int a, int b)
	{	
		System.out.println("In moreParameters go. a: ");
		System.out.println(a);
		System.out.println(" b: ");
		System.out.println(b);
		a = a * b;
		b = 12;
		System.out.println("In moreParameters go. a: ");
		System.out.println(a);
		System.out.println(" b: ");
		System.out.println(b);
		falsSwap(b,a);
		System.out.println("In moreParameters go. a: ");
		System.out.println(a);
		System.out.println(" b: ");
		System.out.println(b);
	}

	public static void go()
	{	int x = 3;
		int y = 2;
		System.out.println("In method go. x: ");
		System.out.println(x);
		System.out.println(" y: ");
		System.out.println(y);
		falsSwap(x,y);
		System.out.println("In method go. x: ");
		System.out.println(x);
		System.out.println(" y: ");
		System.out.println(y);
		moreParameters(x,y);
		System.out.println("In method go. x: ");
		System.out.println(x);
		System.out.println(" y: ");
		System.out.println(y);
	}
	
	
	
	public static void main()
	{	go();
	}
}