import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String s = br.readLine();
		int[] arr = new int[26];
		char[] charArr = s.toCharArray();
		
		for(char c : charArr) {
			arr[c - 'a'] += 1; 
		}
		
		for(int i : arr) {
			System.out.print(i + " ");
		}
		
	}
}