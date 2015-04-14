class HelloWorld
{
	public static int main(int a)
	{
		int [] b = new int [5];
		int i = 0;
		for(i = 0 ;i < 5; i++){
			b[i] = i;
		}
		int sum = 0;
		int j;
		for(j = 0 ;j < 5; j++){
			sum =sum + b[j];
		}
		System.out.println(sum);
	}
}