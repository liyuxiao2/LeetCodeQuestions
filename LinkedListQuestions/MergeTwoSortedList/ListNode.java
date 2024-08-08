package LinkedListQuestions.MergeTwoSortedList;

public class ListNode {

    int val;
    private ListNode next;
    ListNode() {}
    public ListNode getNext() {
        return next;
        
    }
    public void setNext(ListNode next) {
        this.next = next;
        
    }
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.setNext(next); }
    
}
