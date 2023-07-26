/*
 * Baseball Game
 * Difficulty: Easy

 * > https://leetcode.com/problems/baseball-game

 * Notes:
 *  - Beats 98% of time solutions using C#
 *  - First C# solution
 */


using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int CalPoints(string[] operations)
    {
        List<int> scores = new List<int>();

        for (int i = 0; i < operations.Length; i++)
        {
            string item = operations[i];

            if (item == "+")
            {
                scores.Add(scores[scores.Count - 1] + scores[scores.Count - 2]);
            }
            else if (item == "D")
            {
                scores.Add(scores[scores.Count - 1] * 2);
            }
            else if (item == "C")
            {
                scores.RemoveAt(scores.Count - 1);
            }
            else
            {
                int number = int.Parse(item);
                scores.Add(number);
            }
        }
        return scores.Sum();
    }
}

public class RunSol
{
    static void Main(string[] args)
    {
        Solution sol = new Solution();

        string[] operations = { "5", "2", "C", "D", "+" };
        Console.WriteLine(sol.CalPoints(operations));
    }
}