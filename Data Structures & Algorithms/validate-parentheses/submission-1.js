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
    const list = s.split("")
    const stack = []
    for (let i in list) {
        if (stack.length > 0 && this.isMatch(stack[stack.length - 1], list[i])) {
            stack.pop()
        }
        else {
            stack.push(list[i])
        }

    }
    console.log(stack)
    console.log(stack.length)
    return stack.length===0

    }
}
