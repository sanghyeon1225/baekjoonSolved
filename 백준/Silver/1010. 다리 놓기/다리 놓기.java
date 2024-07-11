import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int time = sc.nextInt();
        for (int i = 0; i < time; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println(combination(b, a));
        }
    }

    // 조합을 계산하는 함수
    public static int combination(int n, int r) {
        if (r > n - r) {
            r = n - r; // 더 작은 r을 선택하여 계산을 최적화합니다.
        }
        long result = 1; // 중간 계산이 커질 수 있으므로 long 사용
        for (int i = 0; i < r; i++) {
            result *= (n - i);
            result /= (i + 1);
        }
        return (int) result;
    }
}
