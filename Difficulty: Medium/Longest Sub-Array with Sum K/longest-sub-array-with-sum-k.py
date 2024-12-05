# User function Template for python3

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        prefix_sum_map = {}  # To store (prefix_sum: index)
        prefix_sum = 0       # To keep track of the running sum
        maxlen = 0           # To store the maximum length of subarray

        for i in range(len(arr)):
            prefix_sum += arr[i]  # Update the running sum

        # Check if the prefix sum equals k
            if prefix_sum == k:
                maxlen = i + 1  # Update maxlen if subarray starts from index 0

        # Check if (prefix_sum - k) exists in the map
            if (prefix_sum - k) in prefix_sum_map:
            # Update maxlen based on the length of this subarray
                maxlen = max(maxlen, i - prefix_sum_map[prefix_sum - k])

        # Add prefix_sum to the map if not already present
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i

        return maxlen


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends