import java.util.ArrayList;
import java.util.Scanner;

public class ContactBook {

    static class Contact {
        String name;
        String phone;
        String email;

        Contact(String name, String phone, String email) {
            this.name = name;
            this.phone = phone;
            this.email = email;
        }
    }

    public static void main(String[] args) {
        ArrayList<Contact> contacts = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n--- CONTACT BOOK ---");
            System.out.println("1. Add Contact");
            System.out.println("2. View Contacts");
            System.out.println("3. Search Contact");
            System.out.println("4. Delete Contact");
            System.out.println("5. Exit");

            System.out.print("Enter your choice: ");
            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.print("Enter name: ");
                String name = scanner.nextLine();

                System.out.print("Enter phone number: ");
                String phone = scanner.nextLine();

                System.out.print("Enter email: ");
                String email = scanner.nextLine();

                contacts.add(new Contact(name, phone, email));
                System.out.println("Contact added!");

            } else if (choice.equals("2")) {
                System.out.println("\nYour contacts:");
                if (contacts.size() == 0) {
                    System.out.println("No contacts yet.");
                } else {
                    for (int i = 0; i < contacts.size(); i++) {
                        Contact c = contacts.get(i);
                        System.out.println((i + 1) + ". " + c.name + " | " + c.phone + " | " + c.email);
                    }
                }

            } else if (choice.equals("3")) {
                System.out.print("Enter name to search: ");
                String searchName = scanner.nextLine();
                boolean found = false;

                for (int i = 0; i < contacts.size(); i++) {
                    Contact c = contacts.get(i);
                    if (c.name.equalsIgnoreCase(searchName)) {
                        System.out.println("Found: " + c.name + " | " + c.phone + " | " + c.email);
                        found = true;
                    }
                }

                if (!found) {
                    System.out.println("Contact not found.");
                }

            } else if (choice.equals("4")) {
                System.out.println("\nYour contacts:");
                for (int i = 0; i < contacts.size(); i++) {
                    Contact c = contacts.get(i);
                    System.out.println((i + 1) + ". " + c.name);
                }
                System.out.print("Enter contact number to delete: ");
                int num = Integer.parseInt(scanner.nextLine());

                if (num >= 1 && num <= contacts.size()) {
                    Contact removed = contacts.remove(num - 1);
                    System.out.println(removed.name + " deleted!");
                } else {
                    System.out.println("Invalid contact number.");
                }

            } else if (choice.equals("5")) {
                System.out.println("Goodbye!");
                break;

            } else {
                System.out.println("Invalid choice, try again.");
            }
        }

        scanner.close();
    }
}