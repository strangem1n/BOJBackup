import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextDouble()) {
            double n = sc.nextFloat();
            double b = sc.nextFloat();
            double m = sc.nextFloat();

            double interest = 1 + b/100;

            int year = 0;
            while(n<=m) {
                year++;
                n *= interest;
            }
            System.out.println(year);
        }
    }
}
