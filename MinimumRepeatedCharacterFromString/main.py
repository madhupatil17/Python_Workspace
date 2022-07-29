# Given a sting, return the character that appears the minimum number of times in the string.
# If there is a tie in the minimum number of times a character appears in the string return the character that appears
# first in the string. Input Format:
# Single line with no space denoting the input string. OutputFormat:
# Single character denoting the least frequent character. Sample Input:
# cdadcda Sample Output:
# c Explanation:
# C and A both are with minimum frequency. So c is the answer because it comes first with less index.

question = "aaappplleee"
repeating_char = ""
no_of_times = 0
index = 0
no_of_times = question.count(question[0])

for char in question:
    if question.count(char) < no_of_times:
        repeating_char = char
        no_of_times = question.count(char)
        index = question.index(char)

print(f"{repeating_char} = {no_of_times} = {index}")
