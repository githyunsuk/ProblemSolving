class Solution {
    public long solution(int a, int b) {
        
        long result = 0;
        
        if(a > b) {
            int c = a;
            a = b;
            b = c;
        } else if(a == b) {
            return a;
        }
        
        for(int i=a; i<b+1; i++) {
            result += i;
        }
        
        return result;
    }
}