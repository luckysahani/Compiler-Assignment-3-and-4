class HelloWorld
{
	int y,x;
	public static int hp(int b){
		System.out.println("\nHelloWorld\n");
		y=1;x=2;
		return b;
	}
	public static int hi(int a)
	{
		int b;
		int [] h = new int [4];
		int sum=0;
		h[0] = 4;
		for(int i = 0; 5!=i  ; i++){
			sum++;
			sum = sum + h[i];
			// if(i!=0) return 0;
		}
		System.out.println("grabage\n");
		return sum;
	}
}

class Face{
	int y,x;
	public static int main(int b){
		HelloWorld hel = new HelloWorld();
		HelloWorld hel2 = new HelloWorld();
		// hel.hp(0);
		// hel.z;
		int a=hel.hp(0);
		// hel2.y=hel.x+hel.y;
		System.out.println(a+2);
	}
}