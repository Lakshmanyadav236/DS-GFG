#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        i, j = 0, 0
        union = []
        
        # Traverse both arrays and append unique elements
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                if len(union) == 0 or union[-1] != a[i]:
                    union.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if len(union) == 0 or union[-1] != b[j]:
                    union.append(b[j])
                j += 1
            else:  # when a[i] == b[j], append only once
                if len(union) == 0 or union[-1] != a[i]:
                    union.append(a[i])
                i += 1
                j += 1
        
        # Append remaining elements from a
        while i < len(a):
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        
        # Append remaining elements from b
        while j < len(b):
            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
            j += 1
        
        return union
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends