import java.util.Scanner;

public class QuizGme{

    public static void main(String[] args) {
        String[] questions = {
            "What is the capital of France?",
            "What is 5 + 7?",
            "What is the largest planet in our solar system?",
            "Who wrote 'Romeo and Juliet'?",
            "What is the boiling point of water in Celsius?"
        };

        String[] answers = {
            "paris",
            "12",
            "jupiter",
            "shakespeare",
            "100"
        };

        int score = 0;
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < questions.length; i++) {
            System.out.println("\nQuestion " + (i + 1) + ": " + questions[i]);
            System.out.print("Your answer: ");
            String userAnswer = scanner.nextLine().toLowerCase().trim();

            if (userAnswer.equals(answers[i])) {
                System.out.println("Correct!");
                score++;
            } else {
                System.out.println("Wrong! The correct answer was: " + answers[i]);
            }
        }

        System.out.println("\n--- QUIZ FINISHED ---");
        System.out.println("Your score: " + score + " out of " + questions.length);

        scanner.close();
    }
}