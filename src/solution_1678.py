from typing import List


class Solution:
    def interpret(self, command: str) -> str:
        stack: List[str] = []

        for string in command:
            if string == ")":
                if stack[-1] == "(":
                    stack.pop()
                    stack.append("o")

                if "".join(stack[-3:]) == "(al":
                    del stack[-3:]
                    stack.append("al")
            else:
                stack.append(string)

        return "".join(stack)

    # def interpret_2(self, command: str) -> str:
    #     return command.replace("()", "o").replace("(al)", "al")
