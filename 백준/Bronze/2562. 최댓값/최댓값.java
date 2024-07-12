import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int[] a = new int[9];
        for(int i = 0; i < 9; i++){
            a[i] = s.nextInt();
        }
        int max = a[0];
        int index = 1;
        for(int i = 1; i < 9; i++){
            if(max < a[i]){
                max = a[i];
                index = i+1;
            }
        }
        System.out.println(max);
        System.out.println(index);
    }
}