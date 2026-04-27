import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        int n = word.length();
        for(int i=0; i<n; i=i+1) {
            if ((i+1)%10!=0) {
                System.out.print(word.charAt(i));
            }
            else {
                System.out.println(word.charAt(i));
            }
        }
    }
}
