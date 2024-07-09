def maxScore(cardPoints, k):
    n = len(cardPoints)
    current_sum = sum(cardPoints[:k])
    max_sum = current_sum
    for i in range(1, k + 1):
        current_sum = current_sum - cardPoints[k - i] + cardPoints[-i]
        max_sum = max(max_sum, current_sum)     
    return max_sum
print(maxScore([1, 2, 3, 4, 5, 6, 1], 3))  # Output: 12
print(maxScore([2, 2, 2], 2))  # Output: 4
print(maxScore([9, 7, 7, 9, 7, 7, 9], 7))  # Output: 55




# 2nd solution for custom input pl comment out above code to run below
# Program to support user input:

def maxScore(cardPoints, k):
    n = len(cardPoints)
    current_sum = sum(cardPoints[:k])
    max_sum = current_sum
    for i in range(1, k + 1):
        current_sum = current_sum - cardPoints[k - i] + cardPoints[-i]
        max_sum = max(max_sum, current_sum)
    return max_sum
cardPoints = list(map(int, input("Enter the card points separated by spaces: ").split()))
k = int(input("Enter the number of cards to take: "))
print("Maximum score:", maxScore(cardPoints, k))
