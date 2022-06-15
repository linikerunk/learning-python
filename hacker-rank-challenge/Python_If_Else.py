"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so we print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
"""

def weird(n):
    if n % 2 == 1 or n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')
    # if n % 2 != 0 and n >= 6 and n <= 20:
    #     print("Weird")
    # elif n % 2 == 0 and n >= 2 and n <= 5:
    #     print ("Not Weird")
    # elif n % 2 == 0 and n >= 6 and n <= 20:
    #     print("Weird")
    # elif n > 20 and n % 2 == 0:
    #     print("Not Weird")
    # elif n % 2 != 0 and n > 20:
    #     print("Weird")
    # else:
    #     print("Weird")


if __name__ == '__main__':
    n = int(input().strip())
    weird(n)
