import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int[] arr = {1, 1, 2, 2, 2, 8};
        for(int i = 0; i < arr.length; i++){
            arr[i] = arr[i] - s.nextInt();
        }
        for(int res : arr){
            System.out.println(res);
        }
    }
}