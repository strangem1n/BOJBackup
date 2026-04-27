import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int[] num = {a, b, c};
        for(int i=2; i>0; i-=1) {
            for(int j=0; j<i; j++) {
                if (num[j] > num[j+1]) {
                    int temp = num[j+1];
                    num[j+1] = num[j];
                    num[j] = temp;
                }
            }
        }
        System.out.println(num[1]);
    }
}
