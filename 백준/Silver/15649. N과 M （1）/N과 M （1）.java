import java.util.Scanner;


public class Main {
	public static void main(String[] args)
	{
		 Scanner sc = new Scanner(System.in);
		 
		 int n = sc.nextInt();
		 int m = sc.nextInt();
		 int[] visited = new int[n];
		 int[] sequence = new int[m];
		 makeSequence(n, m, sequence, visited, 0);
		 
	}
	
	static void makeSequence(int a, int b, int[] arr, int[] visit, int cnt) {
		if (cnt == b) {
			for (int i=0; i<b; i++) {
				System.out.print(arr[i] + " ");
			}
			System.out.print("\n");
		}
		else {
			for (int i=0; i<a; i++) {
				if (visit[i] == 0) {
					arr[cnt] = i+1;
					visit[i] = 1;
					makeSequence(a, b, arr, visit, cnt+1);
					visit[i] = 0;
				}
			}
		}
	}
}