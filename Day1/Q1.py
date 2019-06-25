#Question 1 PALINDROME

input_string=raw_input("Enter a String: ")
temp=input_string[::-1]
if temp==input_string:
    print("YES! INPUT STRING IS PALINDROME!!")
else:
    print("NO! INPUT STRING IS NOT A PALINDROME!!")
