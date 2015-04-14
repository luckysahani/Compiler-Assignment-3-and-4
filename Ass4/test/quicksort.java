class Helloworld
{
    public static int partition(int[] arr, int left, int right)
    {
          int i = left, j = right;
          int tmp;
          int pivot = arr[(left + right) / 2];
         
          while (i <= j) {
                while (arr[i] < pivot){
                      i++;
                }
                while (arr[j] > pivot){
                      j--;
                }
                if (i <= j) {
                      tmp = arr[i];
                      arr[i] = arr[j];
                      arr[j] = tmp;
                      i++;
                      j--;
                }
          }
         
          return i;
    }
     
    public static void quickSort(int[] arr, int left, int right) {
          int index = partition(arr, left, right);
          if (left < index - 1)
                quickSort(arr, left, index - 1);
          if (index < right)
                quickSort(arr, index, right);
    }
    public static void main(){
        int [] arr = new int[5];
        arr[0] = 3;
        arr[1] = 1;
        arr[2] = 10;
        arr[3] = -2;
        arr[4] = 5;
        quickSort(arr,0,4);
        for(int i = 0 ;i < 5 ; i++){
        	System.out.println(arr[i]);
        	System.out.println("\n");
        }
    }
}
