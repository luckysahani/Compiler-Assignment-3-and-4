class HelloWorld
{
	public static int printv(int g, int h, int k, int m)
	{
		int r = g + h + k + m;
		System.out.println(r);
	}
	public static int main(int c)
	{
		// int [] b = new int [15];
		// for(int i = 0;i < 15; i++){
		// 	b[i] = i;
		// }
		c = 0;
		for(int j = 0 ;j < 15; j++){
			c = c + j;
		}
		printv(c,c,c,15);
	}
}