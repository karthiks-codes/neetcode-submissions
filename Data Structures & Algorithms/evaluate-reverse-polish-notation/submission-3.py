class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        
        for i in tokens:
            if i == '+':
                num.append(num.pop() + num.pop())
                print(num[-1])
            elif i == '-':
                a, b = num.pop(), num.pop()
                num.append(b-a)
                print(num[-1])
            elif i == '*':
                num.append(num.pop() * num.pop())
                print(num[-1])
            elif i == '/':
                a, b = num.pop(), num.pop()
                num.append(int(b/a))
                print(num[-1])
            else:
                num.append(int(i))
                print(num[-1])
            

        
        return num[0]
            
            



        