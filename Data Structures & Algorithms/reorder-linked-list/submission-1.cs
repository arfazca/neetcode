/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public void ReorderList(ListNode head) {
        if (head==null) return;
        List<ListNode> nodes = new List<ListNode>();
        ListNode curr = head;
        while (curr!=null)
        {
            nodes.Add(curr);
            curr=curr.next;
        }
        int i=0, j=nodes.Count-1;
        while (i<j)
        {
            nodes[i++].next=nodes[j];
            if (i>=j) break;
            nodes[j--].next=nodes[i];
        }
        nodes[i].next=null;
    }
}