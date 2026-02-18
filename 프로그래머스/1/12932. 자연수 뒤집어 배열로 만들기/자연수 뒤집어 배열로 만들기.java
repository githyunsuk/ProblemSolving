class Solution {
    public int[] solution(long n) {
        
        int length = String.valueOf(n).length();
        
        int[] list = new int[length];
        
        for(int i=0; i<length; i++) {
            list[i] = (int) (n % 10);
            n /= 10;
        }
        
        return list;
    }
}