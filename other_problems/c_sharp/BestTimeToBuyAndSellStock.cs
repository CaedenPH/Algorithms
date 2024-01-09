/*
 * Best Time to Buy And Sell Stock
 * Difficulty: Easy

 * > https://leetcode.com/problems/best-time-to-buy-and-sell-stock
 */


using System;

public class Solution
{
    public int MaxProfit(int[] prices)
    {
        int max = 0;
        int start = prices[0];

        for (int i = 0; i < prices.Length; i++)
        {
            int price = prices[i];
            if (start > price)
            {
                start = price;
            }
            else
            {
                max = Math.Max(max, price - start);
            }

        }
        return max;
    }
}

public class RunSol
{
    static void Main(string[] args)
    {
        Solution sol = new Solution();

        int[] prices = { 7, 1, 5, 3, 6, 4 };
        Console.WriteLine(sol.MaxProfit(prices));
    }
}
