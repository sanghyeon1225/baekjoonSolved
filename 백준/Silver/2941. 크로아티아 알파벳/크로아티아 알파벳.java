import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        String str = s.next();
        String[] alp = {"dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="};
        
        for (String cro : alp) {
            if (str.contains(cro)) {
                str = str.replace(cro, "q");  // q는 크로아티아 알파벳에 포함되지 않는 문자
            }
        }
        System.out.println(str.length());
    }
}