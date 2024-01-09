/*
 * Contains Duplicates
 * Difficulty: Easy

 * > https://leetcode.com/problems/contains-duplicate
 */

using System;
using System.Collections.Generic;

public class Solution
{
    public bool ContainsDuplicate(int[] nums)
    {
        Dictionary<int, bool> numberExists = new Dictionary<int, bool>();

        foreach (int num in nums)
        {
            bool _;
            if (numberExists.TryGetValue(num, out _))
            {
                return true;
            }
            numberExists.Add(num, true);
        }
        return false;
    }
}

public class RunSol
{
    static void Main(string[] args)
    {
        Solution sol = new Solution();

        int[] nums = { 1, 2, 3, 1 };
        Console.WriteLine(sol.ContainsDuplicate(nums));
    }
}
