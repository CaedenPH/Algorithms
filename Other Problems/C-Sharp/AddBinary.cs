/*
 * Add Binary
 * Difficulty: Easy

 * > https://leetcode.com/problems/add-binary
 */

using System;

public class Solution {
    public string AddBinary(string a, string b) {
        int result = Convert.ToInt32(a, 2) + Convert.ToInt32(b, 2);
        return Convert.ToString(result, 2);
    }
}

public class RunSol {
     static void Main(string[] args) {
        Solution sol = new Solution();

        Console.WriteLine(sol.AddBinary("11", "1"));
     }
}