
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int time = sc.nextInt();
        for(int i = 0 ; i < time ; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            long result = 1;
            
            for(int j = 0; j < a; j++){
                result *= (b-j);
                result /= (j+1); // 원래는 a-j로 했었는데 그러면 분모에 0을 넣는 경우가 생겨서 오류 발생
            }
            
            System.out.println(result);
        }
    }
}
