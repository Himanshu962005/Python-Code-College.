# Q9.Write a Function that Takes a String Input and Checks if it's a Palindrome or Not.
def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    return "Not Palindrome"
s = input("Enter String : ")
print(palindrome(s))