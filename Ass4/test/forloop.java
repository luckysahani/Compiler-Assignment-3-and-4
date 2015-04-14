class HelloWorld
{
	public static int main(int a)
	{
		int [] b = new int [15];
		int i = 0;
		for(i = 0 ;i < 15; i++){
			b[i] = i;
		}
		int sum = 0;
		int j;
		for(j = 0 ;j < 15; j++){
			sum =sum + b[j];
		}
		System.out.println(sum);
	}
}