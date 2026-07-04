import java.util.Scanner;

public class Grade {
    public static String calctGrade(double score){
        if (score >=70) {
            return "A";
        } else if (score >=60){
            return "B";
        }else if (score >=50){
           return "C";
        }else if (score >=40){
           return "D";
        }else if (score <=39){
            return "E";
        }else{
            return "Invalid Score";
        }
    }
    public static void main(String[] args){
        Scanner Mwenesi = new Scanner(System.in);
        System.out.print("Enter Student name:");
        String name = Mwenesi.nextLine();

        System.out.print("Enter Student Score(0-100):");
        double score = Mwenesi.nextDouble();

        String grade = calctGrade(score);

        System.out.println("Student Name:"+name);
        System.out.println("Your score is:"+score);
        System.out.println("Grade:"+ grade);

        Mwenesi.close();
    }
}