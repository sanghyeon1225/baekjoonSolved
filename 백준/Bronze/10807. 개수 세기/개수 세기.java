import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int[] a = new int[num];
        
        for(int i = 0; i < num ; i++){
            a[i] = s.nextInt();
        }
        
        int find = s.nextInt();
        int count = 0;
        for(int i = 0; i < num ; i++){
            if(find == a[i])
                count++;
        }
        System.out.println(count);
    }
}