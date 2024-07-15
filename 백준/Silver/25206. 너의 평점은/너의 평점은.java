import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        double sum = 0;
        double gradetotal = 0;
        for(int i = 0; i < 20; i++){
            String str = s.next();
            double grade = s.nextDouble();
            String ranking = s.next();
            double rank = 0.0;
            
            if(ranking.equals("A+"))
                rank = 4.5;
            else if(ranking.equals("A0"))
                rank = 4.0;
            else if(ranking.equals("B+"))
                rank = 3.5;
            else if(ranking.equals("B0"))
                rank = 3.0;
            else if(ranking.equals("C+"))
                rank = 2.5;
            else if(ranking.equals("C0"))
                rank = 2.0;
            else if(ranking.equals("D+"))
                rank = 1.5;
            else if(ranking.equals("D0"))
                rank = 1.0;
            else if(ranking.equals("F"))
                rank = 0.0;
            
            if (!ranking.equals("P")) {
                sum += grade * rank;
                gradetotal += grade;
            }
        }
        System.out.printf("%.4f\n", sum / gradetotal);
    }
}