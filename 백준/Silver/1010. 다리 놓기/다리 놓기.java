import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=0; i<t; i++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int new_n = m - n;
            if(n > new_n) {
                n = new_n;
            }
            int cnt = n;
            long result = 1;
            for (int j=0; j<cnt; j++) {
                result *= m;
                m -= 1;
            }
            for (int j=0; j<cnt; j++) {
                result /= n;
                n -= 1;
            }
            System.out.println(result);
        }
    }
}
