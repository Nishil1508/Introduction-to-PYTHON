# Write a Python function that checks whether a passed string is palindrome or not

def is_palindrome(s):

    s = s.replace(" ", "").lower()
    
    if s == s[::-1]:
        return True
    else:
        return False


string = "A man a plan a canal Panama"
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
