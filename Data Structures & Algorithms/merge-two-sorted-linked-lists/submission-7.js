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
            return new ListNode([])
        }
        let curr1 = list1
        let curr2 = list2
        let result = new ListNode()
        result.val = null
        let currResult = result
        
        while (curr1 || curr2){
            // if(!curr2 && !curr1){
            //     break
            // }
            console.log(curr1?.val, curr2?.val)
            if(!curr2&& curr1 || curr1?.val<curr2?.val && curr1 ){
                currResult.val = curr1.val
                // console.log("<",curr1.val, curr2.val)
                if(!curr2&& !curr1?.next){
                    return result
                }
                currResult.next = new ListNode()
                currResult = currResult.next
                console.log("<",result)
                curr1 = curr1.next
            }
            else if(!curr1&& curr2 || curr1?.val>curr2?.val && curr2 ){
                currResult.val = curr2.val
                // console.log(">",curr1.val, curr2.val)
                if(!curr2?.next && !curr1){
                    return result
                }
                currResult.next = new ListNode()
                currResult = currResult.next
                console.log(">", result)
                curr2 = curr2.next
            }
            else {
                
                currResult.val = curr2.val
                currResult.next = new ListNode(curr1.val)
                currResult = currResult.next
                currResult.next = new ListNode()
                currResult = currResult.next
                console.log("1 1", result)
                if(!curr2?.next && !curr1?.next){
                    return result
                }
                curr1 = curr1.next
                curr2 = curr2.next
                
            }
            }
            console.log("final",result)
            return result
        }
    }

