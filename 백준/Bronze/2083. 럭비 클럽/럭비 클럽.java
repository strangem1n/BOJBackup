import java.util.Objects;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String name = sc.next();
            String junior = "Junior";
            String senior = "Senior";
            int age = sc.nextInt();
            int kg = sc.nextInt();
            if (age > 17 || kg >= 80) {
                System.out.println(name + " " + senior);
            }else if (name.equals("#") && age == 0 && kg == 0) {
                System.exit(0);
            }else {
                System.out.println(name + " " + junior);
            }
        }
    }
}
