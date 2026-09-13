class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)                   # Total number of days
        answer = [0] * n                        # Initialize output list with 0s
        stack = []                              # Stack to store indices of unresolved days

        for i, current_temp in enumerate(temperatures):     # Loop through each day and its temperature
        # Check if current day is warmer than the day at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()            # Pop index of the cooler day
                answer[index] = i - index      # Calculate the wait time for a warmer day
            stack.append(i)                    # Push current day's index onto the stack

        return answer                          # Return the final result list
