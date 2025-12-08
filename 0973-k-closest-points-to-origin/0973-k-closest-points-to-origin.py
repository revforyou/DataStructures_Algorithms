import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize an empty min-heap
        minHeap = []
        
        # Step 1: Convert each point into a tuple of (distance^2, x, y) and add to the heap list
        for x, y in points:
            # Use x**2 and y**2 (correct syntax for exponentiation, not ^ which is XOR)
            dist_squared = x**2 + y**2
            # Store distance first so heap compares by distance
            minHeap.append((dist_squared, x, y))

        # Step 2: Turn the list into a valid min-heap
        heapq.heapify(minHeap)

        # Step 3: Pop k closest points from the heap
        result = []
        for _ in range(k):
            # heappop pops the smallest element based on the distance
            dist, x, y = heapq.heappop(minHeap)
            result.append([x, y])

        return result
