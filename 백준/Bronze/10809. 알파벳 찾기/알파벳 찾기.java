import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int[] arr = new int[26];
        String str = s.next();
        
        for(int i = 0; i < arr.length; i++){
            arr[i] = -1;
        }
        
        for(int i = 0; i < str.length(); i++){
            char ch = str.charAt(i);
            if(arr[ch - 'a'] == -1)
                arr[ch - 'a'] = i;
        }
        
        for(int res: arr){
            System.out.print(res + " ");
        }
    }
}