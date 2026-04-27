import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();
        int[] hands = new int[2*n];
        for(int i=0; i<2*n; i++) {
            hands[i] = sc.nextInt();
        }
        int[] game = new int[t];
        for(int i=0; i<t; i++) {
            game[i] = sc.nextInt();
        }

        int idx = 0;
        for(int i=0; i<t; i++) {
            idx = (idx + game[i] - 1) % (2 * n);
            System.out.print(hands[idx] + " ");
        }
    }
}
