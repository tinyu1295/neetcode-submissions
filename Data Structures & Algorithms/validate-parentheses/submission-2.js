class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isMatch(val1, val2) {
    if (val1 === "(" && val2 === ")") {
        return true
    }
    if (val1 === "{" && val2 === "}") {
        return true
    }
    if (val1 === "[" && val2 === "]") {
        return true
    }
    return false
}
    isValid(s) {
    const stack = []
    const closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{',
        };
    for (let i of s) {
        console.log(i)
        if(closeToOpen[i]){
            if(stack.length>0 && stack[stack.length-1]=== closeToOpen[i]){
                stack.pop()
            }
            else {
                return false
            }
        }
        else {
            stack.push(i)
        }

    }
    console.log(stack)
    console.log(stack.length)
    return stack.length===0

    }
}
