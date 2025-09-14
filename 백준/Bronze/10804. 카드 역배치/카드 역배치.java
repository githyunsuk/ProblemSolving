import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] arr = new int[21];
		for(int i=1; i<21; i++) {
			arr[i] = i;
		}
		
		for(int i=0; i<10; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			for(int j=a, k=b; j<(a+b)/2 + 1; j++, k--) {
				int temp = arr[j];
				arr[j] = arr[k];
				arr[k] = temp;
			}
			
		}
		
		for(int i=1; i<arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}