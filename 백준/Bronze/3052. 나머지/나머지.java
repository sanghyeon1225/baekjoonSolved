import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int[] arr = new int[42];
        for(int i = 0; i < 10; i++){
            int a = s.nextInt();
            arr[a % 42]++;
        }
        int count = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] >= 1)
                count++;
        }
        System.out.println(count);
    }
}