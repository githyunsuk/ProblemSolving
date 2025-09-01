import java.util.*;

public class Main
{
	public static void main(String[] args)
	{
		Scanner scanner = new Scanner(System.in);
		
		int[] array = new int[9];
		for(int i=0; i<9; i++)
			array[i] = scanner.nextInt();
		
		int max = 0;
		int index = 0;
		
		for(int i=0; i<9; i++)
		{
			if(array[i] > max)
			{
				max = array[i];
				index = i+1;
			}
		}
		
		System.out.println(max + "\n" + index);
	}
}