
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int index = s.nextInt();
        int[] a = new int[num];
        
        for(int i = 0; i < num ; i++){
            a[i] = s.nextInt();
        }
        
        for(int i = 0; i < num ; i++){
            if(a[i] < index)
                System.out.println(a[i]);
        }
    }
}
