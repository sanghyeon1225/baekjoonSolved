import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int time = s.nextInt();
        int[] arr = new int[26];
        int count = 0;
        
        for(int k = 0; k < time; k++){
            String str = s.next();
            int index = -1;
            boolean boo = true;
            
            for(int i = 0; i < arr.length; i++)
                arr[i] = 0;
            for(int i = 0; i < str.length(); i++){
                if(index != (str.charAt(i) - 'a') && arr[str.charAt(i) - 'a'] == 0)
                    arr[str.charAt(i) - 'a']++;
                else if(index == (str.charAt(i) - 'a'))
                    arr[str.charAt(i) - 'a']++;    
                else if(index != (str.charAt(i) - 'a') && arr[str.charAt(i) - 'a'] != 0)
                    boo = false;
                index = str.charAt(i) - 'a';
            }
            if(boo == true)
                count++;
        }
        System.out.println(count);
    }
}