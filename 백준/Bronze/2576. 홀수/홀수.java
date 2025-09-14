import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int min = 100;
		int sum = 0;
		for(int i=0; i<7; i++) {
			int temp = Integer.parseInt(br.readLine());
			if(temp % 2 != 0) {
				sum += temp;
				if(temp < min) {
					min = temp;
				}
			}
		}
		
		if(sum == 0) {
			System.out.println(-1);
			return;
		}
		System.out.println(sum);
		System.out.println(min);
	}
}
