class Solution {
    public boolean solution(int x) {
        
        String[] list = String.valueOf(x).split("");
        
        int sum = 0;
        for(String s : list) {
            sum += Integer.parseInt(s);
        }
        
        return x % sum == 0 ? true : false;
    }
}