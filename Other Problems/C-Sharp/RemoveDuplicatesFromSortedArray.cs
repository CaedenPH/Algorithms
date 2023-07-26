/*
 * Remove Duplicates From Sorted Arrays
 * Difficulty: Easy

 * > https://leetcode.com/problems/remove-duplicates-from-sorted-list
 */

using System;

public class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution
{
    public ListNode DeleteDuplicates(ListNode head)
    {
        if (head is null)
        {
            return head;
        }

        ListNode newHead = new ListNode(head.val);
        ListNode newList = newHead;

        while (head is not null)
        {
            if (head.val != newList.val)
            {
                newList.next = new ListNode(head.val);
                newList = newList.next;
            }
            head = head.next;
        }
        return newHead;
    }
}

public class RunSol
{
    static void Main(string[] args)
    {
        Solution sol = new Solution();

        ListNode head = new ListNode(1, new ListNode(1, new ListNode(2)));
        Console.WriteLine(sol.DeleteDuplicates(head));
    }
}