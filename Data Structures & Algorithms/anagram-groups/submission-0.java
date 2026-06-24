class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> results = new ArrayList<>();
        //String (value), count array (key)
        HashMap<String, List<String>> counts = new HashMap<>();
        int[] count = new int[26];
        for (String str : strs){
            Arrays.fill(count, 0);
            for (char c : str.toCharArray()){
                count[(int)c - 97] += 1;
            }
            if (counts.containsKey(Arrays.toString(count))){
                counts.get(Arrays.toString(count)).add(str);
            }
            else{
                counts.put(Arrays.toString(count), new ArrayList<String>());
                counts.get(Arrays.toString(count)).add(str);
            }
            // System.out.println(Arrays.toString(count));
        }
        // System.out.println(counts);
        for(String a : counts.keySet()){
            // System.out.println(counts.get(a));
            results.add(counts.get(a));
        }
        return results;
    }
}
