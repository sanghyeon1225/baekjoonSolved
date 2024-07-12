import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        int time = s.nextInt();
        int[] a = new int[num];
        
        for(int i = 0; i < num; i++){ //공 번호 1,2,3,4,5로 초기화
            a[i] = i+1;
        }
        
        for(int i = 0; i < time; i++){
            int start = s.nextInt();
            int end = s.nextInt();
            int tmp = a[start - 1];
            a[start - 1] = a[end - 1];
            a[end - 1] = tmp;
        }
        for(int arr: a){
            System.out.println(arr);
        }
    }
}