import java.util.Scanner;

public class ATMSimulator {
    private static Scanner scanner = new Scanner(System.in);
    private static double balance = 1000.00; // Starting balance
    private static String pin = "1234"; // Default PIN
    
    public static void main(String[] args) {
        System.out.println("=== ATM SIMULATOR ===");
        
        // PIN verification
        System.out.print("Enter PIN: ");
        String enteredPin = scanner.nextLine();
        
        if (!enteredPin.equals(pin)) {
            System.out.println("Invalid PIN! Exiting...");
            return;
        }
        
        // Main menu loop
        while (true) {
            System.out.println("\n--- MAIN MENU ---");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");
            System.out.print("Choose option: ");
            
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    checkBalance();
                    break;
                case 2:
                    deposit();
                    break;
                case 3:
                    withdraw();
                    break;
                case 4:
                    System.out.println("Thank you! Goodbye.");
                    return;
                default:
                    System.out.println("Invalid option!");
            }
        }
    }
    
    private static void checkBalance() {
        System.out.println("Your balance: $" + String.format("%.2f", balance));
    }
    
    private static void deposit() {
        System.out.print("Enter amount to deposit: $");
        double amount = scanner.nextDouble();
        
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: $" + String.format("%.2f", amount));
            System.out.println("New balance: $" + String.format("%.2f", balance));
        } else {
            System.out.println("Amount must be positive!");
        }
    }
    
    private static void withdraw() {
        System.out.print("Enter amount to withdraw: $");
        double amount = scanner.nextDouble();
        
        if (amount <= 0) {
            System.out.println("Amount must be positive!");
        } else if (amount > balance) {
            System.out.println("Insufficient balance!");
        } else {
            balance -= amount;
            System.out.println("Withdrawn: $" + String.format("%.2f", amount));
            System.out.println("Remaining balance: $" + String.format("%.2f", balance));
        }
    }
}