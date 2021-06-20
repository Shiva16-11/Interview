# Problem 1
# Problem Description 
#   Given a array of integers A of size N and an integer B. 
#   Return number of non-empty subsequences of A of size B having sum <= 1000. 
# Problem Constraints 
# 1 <= N <= 20 
# 1 <= A[i] <= 1000 
# 1 <= B <= N 
# Input Format 
# The rst argument given is the integer array A. 
# The second argument given is the integer B. 
# Output Format 
# Return number of subsequences of A of size B having sum <=1000. Example Input 
# Input 1: 
# A = [1, 2, 8] 
# B = 2 
# Input 2: 
# A = [5, 17, 1000, 11] 
# B = 4 
# Example Output 
# Output 1: 3 
# Output 2: 0 
# Example Explanation 
# Explanation 1: 
# {1, 2}, {1, 8}, {2, 8} 

def countSubsequenceWithGivenSum(arr, b, s, index, dp):
    #b --- length of subsequence
    #s ---- given sum; 1000 in this problem
    #dp ---- dp array
    if b == 0 and s >= 0:
        return 1

    if index < 0:
        return 0
        
    if dp[s][b][index] != -1:
        return dp[s][b][index]
    else:
        dp[s][b][index] = countSubsequenceWithGivenSum(arr, b - 1, s - arr[index], index - 1, dp) + countSubsequenceWithGivenSum(arr, b, s, index - 1, dp)
            
        return dp[s][b][index]


arr = [1, 2, 8]
subsequencelength = 2
arraylength = len(arr)
dp = [[[-1 for x in range(arraylength + 1)] for x in range(subsequencelength + 1)] for x in range(1001)]
print(countSubsequenceWithGivenSum(arr, subsequencelength, 1000, arraylength - 1, dp))
