import java.util.Scanner;
import java.util.ArrayList;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> intArr = new ArrayList<>();

        for(int i=0; i<n; i++) {
            intArr.add(sc.nextInt());
        }
        intArr.sort(Comparator.naturalOrder());

        ArrayList<Integer> result = new ArrayList<>();
        for(int i=0; i<n; i++) {
            int chk = intArr.get(i);
            if(result.contains(chk)) {
                continue;
            }
            else {
                result.add(chk);
            }
        }
       for(int i=0; i<result.size(); i++) {
           System.out.print(result.get(i)+" ");
       }
    }
}
