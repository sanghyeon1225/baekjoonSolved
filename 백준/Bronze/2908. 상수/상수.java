import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String str1 = s.next();
        String str2 = s.next();
        char[] ch1 = new char[3];
        char[] ch2 = new char[3];
        
        for(int i = 0; i < 3; i++){
            ch1[i] = str1.charAt(2-i);
            ch2[i] = str2.charAt(2-i);
        }
        str1 = new String(ch1);
		str2 = new String(ch2);
        
        int a = Integer.parseInt(str1);
        int b = Integer.parseInt(str2);
        
        System.out.println(a>b?a:b);
	}
 
}