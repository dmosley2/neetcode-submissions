class Solution {
    public boolean isHappy(int n) {
        HashMap<Integer, Integer> numbers = new HashMap<>();
        int number = n;
        while(!numbers.containsKey(number)){
            Integer result = sumOfSquares(number);
            numbers.put(number, result);
            System.out.println(number + " " + result);
            if(result == 1){
                return true;
            }
            number = result;
        }
        return false;
    }

    public Integer sumOfSquares(int n){
        Integer sum = 0;
        while(n > 0){
            sum += (int)Math.pow(n%10, 2);
            n = n/10;
        }
        return sum;
    }
}
