class HelloWorld
{
	int f,g;
	public static void hello(int c){
		int b;
		b = 5;
		if(b < 6){
			b = 7;
		}
		else {
			b = 3;
		}
	}
	public static void main(String args[])
	{
		int a;
		a = 5;
		if(a < 6){
			a = 7;
		}
		else {
			a = 3;
		}
		hello(a);
	}
}