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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        if(!list1 && !list2){
            return 
        }
        let curr1 = list1
        let curr2 = list2
        let result = new ListNode()
        result.val = null
        let currResult = result
        while (curr1 || curr2){
            console.log(curr1.val, curr2.val)
            if(curr1.val<=curr2.val){
                currResult.val = curr2.val
                currResult.next = new ListNode()
            }
            else{
                currResult.val = curr2.val
                currResult.next = new ListNode()
            }
            
            curr1 = curr1.next
            
            curr2 = curr2.next
            }
            console.log(result)
            return result
        }
    }

