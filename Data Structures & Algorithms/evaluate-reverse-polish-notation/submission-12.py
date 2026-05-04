class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # O(n) time and O(n) space
        intList = []
        opList = ['+', '-', '*', '/']
        # if int, append to intlist
        # if op, remove first 2 el from intlist, use op on it put it nack to intlist
        for smt in tokens:
            if smt not in opList:
                intList.append(smt)
                if len(tokens) == 1:
                    return int(intList[0])
                
            else:
                if len(intList) == 0:
                    continue
                
                int1 = int(intList.pop())
                int2 = int(intList.pop())
                if smt == "+":
                    res = int2 + int1
                elif smt == "-":
                    res = int2 - int1
                elif smt == "*":
                    res = int2 * int1
                elif smt == "/":
                    if int2 == 0:
                        intList.append(0)
                        continue
                    else:
                        res = math.trunc(int2 / int1)
                intList.append(res)
        
        return intList[0]

