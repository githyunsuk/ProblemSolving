class Solution {
    boolean solution(String s) {
        
        s = s.toLowerCase();
        
        int p = 0;
        int y = 0; 
        
        char[] list = s.toCharArray();
        for(char c : list) {
            if (c == 'p') p += 1;
            if (c == 'y') y += 1;
        }
        
        return p == y ? true : false;

        

    }
}