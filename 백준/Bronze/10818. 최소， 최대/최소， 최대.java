import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int[] a = new int[num];
        for(int i = 0; i < num; i++){
            a[i] = s.nextInt();
        }
        int max = a[0];
        int min = a[0];
        for(int i = 1; i < num ; i++){
            if(max < a[i])
                max = a[i];
            if(min > a[i])
                min = a[i];
        }
        System.out.println(min + " " + max);
    }
}
