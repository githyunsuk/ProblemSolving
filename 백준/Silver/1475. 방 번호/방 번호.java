import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String num = br.readLine();
		int[] arr = new int[10];
		
		for(int i=0; i<num.length(); i++) {
			arr[num.charAt(i) - '0']++;
		}
		
		int temp = (arr[6] + arr[9] + 1) / 2;
		arr[6] = temp;
		arr[9] = temp;
		
		
		
		int max = 1;
		for(int i : arr) {
			max = Math.max(i, max);
		}
		
		System.out.println(max);
	}
}