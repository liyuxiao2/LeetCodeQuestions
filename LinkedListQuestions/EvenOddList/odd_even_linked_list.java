import LinkedListQuestions.MergeTwoSortedList.ListNode;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head == null){
            return head;
        }
        
        ListNode odd = head,  even = head.getNext(), evenHead = even;

        
        while(even != null && even.getNext() != null){
            odd.setNext(odd.getNext().getNext());
            even.setNext(even.getNext().getNext());
            even = even.getNext();
            odd = odd.getNext();
        }

        
        odd.setNext(evenHead);
        return head;
        
    }
}