/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node copyRandomList(Node head) {
        if (head==null) return null;
        Dictionary<Node,Node> newLL = new Dictionary<Node,Node>();
        Node curr = head;
        while (curr!=null) 
        {
            newLL[curr]=new Node(curr.val);
            curr=curr.next;
        }
        curr=head;
        while (curr!=null)
        {
            if (curr.next!=null) { newLL[curr].next=newLL[curr.next]; }
            if (curr.random!=null) { newLL[curr].random=newLL[curr.random]; }
            curr=curr.next;
        }
        return newLL[head];
    }
}
