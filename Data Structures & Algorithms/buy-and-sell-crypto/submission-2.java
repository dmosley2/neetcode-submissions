class Solution {
    public int maxProfit(int[] prices) {
        if(prices.length < 2){
            return 0;
        }
        int sell = 1;
        int buy = 0;
        int profit = Math.max(0, prices[sell] - prices[buy]);
        for (int i = 1; i < prices.length; i++){
            if(prices[i] < prices[buy]){
                buy = i;
            }
            int currentProfit = prices[i] - prices[buy];
            if(currentProfit > profit){
                profit = currentProfit;
                sell = i;
            }
        }
        return Math.max(0, profit);
    }
}