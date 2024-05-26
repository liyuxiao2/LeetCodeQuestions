package Easy.RemoveLinkedList;

class Solution {
    public ListNode removeElements(ListNode head, int val) {
        //edge case
        while (head != null && head.val == val) {
            head = head.next;
        }
        
        ListNode previous = null, cur = head;
        
        //catch 
        while(cur !=null){
            if(cur.val == val){
                previous.next = cur.next;
            }
            else{
                previous = cur;
            }
            cur = cur.next;
        }
        
        return head;
    }
}