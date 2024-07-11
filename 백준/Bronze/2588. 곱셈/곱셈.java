import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int b = s.nextInt();
        
         if(b < 100 || b > 999) {
            System.out.println("두 번째 정수는 세 자리 정수여야 합니다.");
            return;
        }
        int first = a * (b % 10);
        int second = a * (b / 10 % 10);
        int third = a * (b / 100);
        int result = first + (second * 10) + (third * 100);
        System.out.println(first);
        System.out.println(second);
        System.out.println(third);
        System.out.println(result);
    }
}