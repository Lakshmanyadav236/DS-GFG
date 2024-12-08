class Solution:
    def leaders(self, arr):
        ans=[]
        n=len(arr)
        max_ele=arr[n-1]
        ans.append(arr[n-1])
        for i in range(n-2,-1,-1):
            if arr[i]>=max_ele:
                ans.append(arr[i])
                max_ele=arr[i]
        return ans[::-1]

#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends