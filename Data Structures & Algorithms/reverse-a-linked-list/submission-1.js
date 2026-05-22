/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        let curr = head
        let prev = null
        let next = null
        while (curr) {
            next = curr.next;
            // Reverse pointer
            curr.next = prev;
            // Move prev and curr forward
            prev = curr;
            // console.log(prev.value)
            curr = next;
        }
        return prev
    }
}
