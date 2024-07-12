import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int[] arr = new int[31];
        for(int i = 0; i < 28; i++) {
            int on = s.nextInt();
            arr[on] = 1;
        }
        for(int i = 1; i < arr.length; i++){
            if(arr[i] != 1)
                System.out.println(i);
        }
    }
}