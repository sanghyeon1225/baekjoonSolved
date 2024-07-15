import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int[] arr = new int[26];
        String str = s.next();
        
        for (int i = 0; i < str.length(); i++){
			if ('A' <= str.charAt(i) && str.charAt(i) <= 'Z') { 
				arr[str.charAt(i) - 'A']++;
			}
			else {
				arr[str.charAt(i) - 'a']++;
			}
		}
        
        int max = -1;
        char res = '?';
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > max){
                max = arr[i];
                res = (char) (i + 65);
            }
            else if (arr[i] == max)
                res = '?';
        }
        System.out.println(res);
    }
}