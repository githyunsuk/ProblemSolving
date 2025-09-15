import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		
		for(int i=1; i<=N; i++) {
			for(int j=1; j<=i; j++) System.out.print("*");
			for(int k=1; k<=N*2 - i*2; k++) System.out.print(" ");
			for(int l=1; l<=i; l++) System.out.print("*");
			System.out.println();
		}
		
		
		for(int i=N-1; i>=1; i--) {
			for(int j=1; j<=i; j++) System.out.print("*");
			for(int k=1; k<=N*2 - i*2; k++) System.out.print(" ");
			for(int l=1; l<=i; l++) System.out.print("*");
			System.out.println();
		}
		
	}
}