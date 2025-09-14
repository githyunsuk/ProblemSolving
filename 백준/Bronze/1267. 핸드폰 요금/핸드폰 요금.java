import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());
		int sumM = 0, sumY = 0;
		for(int i=0; i<N; i++) {
			int num = Integer.parseInt(st.nextToken());
			sumY += (num / 30 + 1) * 10;
			sumM += (num / 60 + 1) * 15;
		}
		
		if(sumY < sumM) {
			System.out.println("Y " + sumY);
		} else if (sumM < sumY) {
			System.out.println("M " + sumM);
		} else {
			System.out.println("Y " + "M " + sumM);
		}
	}
}