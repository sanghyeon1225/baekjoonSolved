import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String str = s.next();
        int answer = 1;
        for(int i = 0; i < str.length() / 2 + 1; i++){
            if(str.charAt(i) != str.charAt(str.length() - i - 1))
                answer = 0;
        }
        System.out.println(answer);
    }
}