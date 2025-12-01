class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = ""

        def backtrack(open_count, close_count, curr):
            if open_count == n and close_count == n:
                result.append(curr)
                return

            if open_count < n: 
                backtrack(open_count + 1, close_count, curr + "(")

            if close_count < open_count:
                backtrack(open_count, close_count + 1, curr + ")")

        backtrack(0,0, curr)
        return result


