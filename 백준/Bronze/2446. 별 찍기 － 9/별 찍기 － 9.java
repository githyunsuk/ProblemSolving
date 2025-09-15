import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		
		for(int i=N; i>=1; i--) {
			for(int j=1; j<=N-i; j++ ) System.out.print(" ");
			for(int j = 1; j <= i * 2 - 1; j++) System.out.print("*");
	
			System.out.println();
		}
		
		for(int i=1; i<=N-1; i++) {
			for(int j=1; j<= N-i-1; j++) System.out.print(" ");
			for(int k=1; k<= i*2+1; k++) System.out.print("*");
			System.out.println();
		}
		
	}
}