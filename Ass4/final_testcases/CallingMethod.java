public class CallingMethodsInSameClass
{
	public static void printOne() {
		System.out.println("Hello World");
	}

	public static void printTwo() {
		printOne();
		printOne();
	}
	public static void main() {
		printOne();
		printOne();
		printTwo();
	}
}