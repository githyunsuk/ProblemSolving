import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		long a = Long.parseLong(st.nextToken());
		long b = Long.parseLong(st.nextToken());
		
		if(a > b) {
			long temp = a;
			a = b;
			b = temp;
		}
		
		if(a == b) System.out.println(0);
		else System.out.println(b - a - 1);
		
		for(long i=a+1; i<b; i++)
			System.out.print(i + " ");
	}
}