import java.util.ArrayList;
import java.util.Scanner;

public class T{

    public static void main(String[] args) {
        ArrayList<String> tasks = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- TO-DO LIST ---");
            System.out.println("1. Add task");
            System.out.println("2. View tasks");
            System.out.println("3. Remove task");
            System.out.println("4. Exit");

            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.print("Enter a new task: ");
                String task = scanner.nextLine();
                tasks.add(task);
                System.out.println("Task added!");

            } else if (choice.equals("2")) {
                System.out.println("\nYour tasks:");
                if (tasks.size() == 0) {
                    System.out.println("No tasks yet.");
                } else {
                    for (int i = 0; i < tasks.size(); i++) {
                        System.out.println((i + 1) + " - " + tasks.get(i));
                    }
                }

            } else if (choice.equals("3")) {
                System.out.println("\nYour tasks:");
                for (int i = 0; i < tasks.size(); i++) {
                    System.out.println((i + 1) + " - " + tasks.get(i));
                }
                System.out.print("Enter task number to remove: ");
                int taskNum = Integer.parseInt(scanner.nextLine());
                if (taskNum >= 1 && taskNum <= tasks.size()) {
                    String removed = tasks.remove(taskNum - 1);
                    System.out.println(removed + " removed!");
                } else {
                    System.out.println("Invalid task number.");
                }

            } else if (choice.equals("4")) {
                System.out.println("Goodbye!");
                break;

            } else {
                System.out.println("Invalid choice, try again.");
            }
        }

        scanner.close();
    }
}