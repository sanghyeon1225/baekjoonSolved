import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();
        double[] arr = new double[num];
        
        for(int i = 0; i < arr.length; i++){
            arr[i] = s.nextInt();
        }
        
        double max = arr[0];
        double sum = 0;
        
        for(int i = 1; i < arr.length; i++){
            if(max < arr[i])
                max = arr[i];
        }
        
        for(int i = 0; i < arr.length; i++){
            arr[i] = arr[i]/max * 100;
            sum += arr[i];
        }
        System.out.println(sum/arr.length);
    }
}