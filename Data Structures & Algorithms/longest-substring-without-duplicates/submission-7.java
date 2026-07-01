class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] string = s.toCharArray();
        if(string.length < 2)
            return string.length;
        int l = 0;
        int r = 1;
        HashMap<Character, Integer> substring = new HashMap<>();
        substring.put(string[l], l);
        int largestLength = substring.size();
        int curLength = 1;
        while((l < string.length) && (r < string.length)){
            if(!substring.containsKey(string[r])){
                substring.put(string[r], r);
            }
            else{
                while(substring.containsKey(string[r]) && l < string.length){
                    substring.remove(string[l]);
                    l++;
                }
                substring.put(string[r], r);
            }
            curLength = substring.size();
            if(curLength > largestLength)
                largestLength = curLength;
            r++;
            System.out.println(substring.toString());
        }
        return largestLength;
    }
}
