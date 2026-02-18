class Solution {
    public int[] solution(long n) {
        
        String[] list = String.valueOf(n).split("");
        
        int[] answer = new int[list.length];
        
        for(int i=list.length-  1; i>=0; i--) {
            answer[list.length - 1 - i] = Integer.parseInt(list[i]);
        }
        
        return answer;
    }
}