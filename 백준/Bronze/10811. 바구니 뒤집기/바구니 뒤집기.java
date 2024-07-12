import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int time = s.nextInt();
        int[] arr = new int[num];
        
        for(int i = 0; i < arr.length; i++)
            arr[i] = i + 1;
        
        for(int i = 0; i < time; i++){
            int a = s.nextInt();
            int b = s.nextInt();
            for(int j = 0; j < (b-a)/2 + 1 ; j++){
                int temp = arr[a-1+j];
                arr[a-1+j] = arr[b-1-j];
                arr[b-1-j] = temp;
            }
        }
        for(int result: arr){
            System.out.println(result);
        }
    }
}