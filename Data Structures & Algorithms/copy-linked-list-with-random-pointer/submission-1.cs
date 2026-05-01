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
        Dictionary<Node, Node> newLL = new Dictionary<Node, Node>();

        Node cur = head;
        while (cur != null) {
            newLL[cur] = new Node(cur.val);
            cur = cur.next;
        }

        cur = head;
        while (cur != null) {
            if (cur.next != null)       { newLL[cur].next = newLL[cur.next]; }
            if (cur.random != null)     { newLL[cur].random = newLL[cur.random]; }
            cur = cur.next;
        }

        return newLL[head];
    }
}