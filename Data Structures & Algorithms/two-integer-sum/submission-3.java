
class Solution {
    // import java.util.HashMap;
    public int[] twoSum(int[] nums, int target) {
        //Store num (key) and index (value)
        HashMap<Integer,Integer> numsMap = new HashMap<>();
        int[] returnVal = {0,0};
        numsMap.put(nums[0], 0);
        for(int i = 1; i <= nums.length - 1; i++){

            int dif = target - nums[i];
            if(numsMap.containsKey(dif)){
                if (i > numsMap.get(dif)){
                    returnVal[0] = numsMap.get(dif);
                    returnVal[1] = i;
                    return returnVal;
                }
                else{
                    returnVal[0] = i;
                    returnVal[1] = numsMap.get(dif);
                    return returnVal;
                }
            }
            else{
                numsMap.put(nums[i], i);
            }
        }
        return returnVal;
    }
}
