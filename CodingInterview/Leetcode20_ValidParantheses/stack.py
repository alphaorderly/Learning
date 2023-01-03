class Solution(object):
    def isValid(self, s):
        stack = list()
        for ch in s:
            # 열리는 괄호 일시 무조거 집어 넣어줌.
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            # 닫히는 괄호마다 같은 쌍이면 POP
            elif len(stack) != 0 and ch == ')' and stack[len(stack)-1] == '(':
                stack = stack[:len(stack)-1]
            elif len(stack) != 0 and ch == '}' and stack[len(stack)-1] == '{':
                stack = stack[:len(stack)-1]
            elif len(stack) != 0 and ch == ']' and stack[len(stack)-1] == '[':
                stack = stack[:len(stack)-1]
            # 닫히면서 쌍이 맞지 않으면 FALSE
            else:
                return False
        
        # 문자열을 전부 돌고도 스택에 값이 남아있으면 FALSE
        if len(stack) != 0:
            return False
        else:
            return True

s = Solution()

print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))