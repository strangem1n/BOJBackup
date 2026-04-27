import java.util.Scanner;


public class Main {
	public static void main(String[] args)
	{
		 Scanner sc = new Scanner(System.in);
		 
		 int n = sc.nextInt();
		 String[] words = new String[n];
		 for(int i=0; i<n; i++) {
			 String new_word = sc.next();
			 words[i] = new_word;
		 }
		 System.out.println(getCommand(words));
		 
	}
	
	static String getCommand(String[] arr) {
		String[] result = arr[0].split("");
		int word_length = arr[0].length();
		for(int i=0; i<word_length; i++) {
			char charAt = arr[0].charAt(i);
			for(int j=1; j<arr.length; j++) {
				char comparechar = arr[j].charAt(i);
				if(charAt != comparechar) {
					result[i] = "?";
					break;
				}
			}
		}
		return String.join("",  result);
	}
}