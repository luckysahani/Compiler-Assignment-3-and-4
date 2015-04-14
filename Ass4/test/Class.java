class HelloWorld
{
	int y,x;
	public static int hp(int b){
		y = 3;
	}
	public static int hi(int a)
	{
		int b;
		int [] h = new int [4];
		int sum;
		h[0] = 4;
		for(int i = 0; i< 15 ; i++){
			sum = sum + h[i];
		}
	}
}

class Face{
	int y,x;
	public static int main(int b){
		HelloWorld hel = new HelloWorld();
		hel.y = 3;
		int a = hel.y;
		System.out.println(a);
	}
}