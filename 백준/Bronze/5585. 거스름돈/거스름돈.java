import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int money = 1000 - sc.nextInt();
        int exchange = 0;
        int[] coins = {500, 100, 50, 10, 5, 1};
        int i = 0;
        while (money != 0) {
            if (money >= coins[i]) {
                exchange++;
                money -= coins[i];
            }
            else {
                i++;
            }
        }
        System.out.println(exchange);
    }
}
