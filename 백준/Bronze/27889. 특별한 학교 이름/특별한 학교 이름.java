import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String school = sc.next();
        String fullname = "";
        switch (school) {
            case "NLCS": fullname = "North London Collegiate School";
            break;
            case "BHA": fullname = "Branksome Hall Asia";
            break;
            case "KIS": fullname = "Korea International School";
            break;
            case "SJA": fullname = "St. Johnsbury Academy";
            break;
        }
        System.out.println(fullname);
    }
}
