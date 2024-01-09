/*
 * Merge Sorted Arrays
 * Difficulty: Easy

 * > https://leetcode.com/problems/merge-sorted-array
 */


using System;

public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        if (m == 0)
        {
            for (int i = 0; i < n; i++)
            {
                nums1[i] = nums2[i];
            }
        }
        else if (n != 0)
        {
            // Double pointer for nums1 and nums2
            int i = m - 1;
            int j = n - 1;
            while (j >= 0)
            {
                Console.WriteLine("i={0} j={1}", i, j);
                if (i >= 0 && nums1[i] > nums2[j])
                {
                    nums1[i + j + 1] = nums1[i];
                    i--;
                }
                else
                {
                    nums1[i + j + 1] = nums2[j];
                    j--;
                }
            }
        }
    }
}

public class RunSol
{
    static void Main(string[] args)
    {
        Solution sol = new Solution();

        int[] nums1 = { 1, 2, 3, 0, 0, 0 };
        int[] nums2 = { 2, 5, 6 };
        sol.Merge(nums1, 3, nums2, 3);
        Console.WriteLine(string.Join(", ", nums1));
    }
}