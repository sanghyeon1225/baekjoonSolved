import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int time = s.nextInt();
        int[] a = new int[num];
        for(int i = 0; i < num; i++){ //바구니의 공 모두 0으로 초기화
            a[i] = 0;
        }
        for(int i = 0; i < time; i++){
            int start = s.nextInt();
            int end = s.nextInt();
            int n = s.nextInt();
            for(int j = start - 1; j < end; j++){
                a[j] = n;
            }
        }
        for(int arr: a){
            System.out.println(arr);
        }
    }
}