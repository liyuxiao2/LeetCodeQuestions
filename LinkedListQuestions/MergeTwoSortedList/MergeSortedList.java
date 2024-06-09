package LinkedListQuestions.MergeTwoSortedList;


class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        //initialized dummy now to hold sum values
        ListNode dummy = new ListNode();
        ListNode cur = dummy;

        //holds onto the carry if the sum is greater than 10
        int carry = 0;

        while(l1 != null || l2 != null || carry != 0){

            int sum = (l1 != null ? l1.val: 0) + (l2 != null ? l2.val: 0) + carry;
            
            
            
            cur.next = new ListNode(sum % 10);
                        
            carry = sum/10;
            
            //check if were at the end of the linked list
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
            
            cur = cur.next;
        }
        
        //return the head
        return dummy.next;
    }
}