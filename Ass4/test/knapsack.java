//This is the java program to implement the knapsack problem using Dynamic Programming
//		import java.util.Scanner;
 
public class Knapsack_DP 
{
    static int max(int a, int b) 
    { 
        return (a > b)? a : b; 
    }
    static int knapSack(int W, int[] wt, int[] val, int n)
    {
        int i, w;
        int [][]K = new int[10][10];
 
	   // Build table K[][] in bottom up manner
        for (i = 0; i <= n; i++)
        {
            for (w = 0; w <= W; w++)
            {
                if (i==0 || w==0){
                    K[i][w] = 0;
                }
                if (wt[i-1] <= w){
                    // K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]);
                }
                else{
                    K[i][w] = K[i-1][w];
                }
  		    }          
        }
 
        return K[n][W];
    }
 
    public static void main()
    {
        int n = 5;
        System.out.println("Enter the items weights: ");
        int []wt = new int[n];
        wt[0] = 11;
        wt[1] = 12;
        wt[2] = 13;
        wt[3] = 14;
        wt[4] = 15;
        int []val = new int[n];
        val[0] = 1;val[1] = 2;val[2] = 3;val[3]=4;val[4] = 5;
        int W = 3;
        int ans = knapSack(W, wt, val, n);
    	System.out.println(ans);
    }
}