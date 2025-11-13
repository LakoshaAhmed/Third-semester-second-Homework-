#1.Longest word in a line
#2. Number of words per line
#3. Turns every word in a line backwards`
#4. Removes all digits from a string
#5. Replaces all uppercase letters with lowercase ones, and all lowercase letters with uppercase ones
#6. Checks if a string is a palindrome (ignoring spaces, case and punctuation, just letters and numbers)
#7. If the string is not a palindrome, then outputs the first 5 characters of the string in reverse order
def get_extended_string_info(text):
    words = text.split() 
    longest = max (words, key = len) 
    reversed_words = [word[::-1] for word in words]
    removing_digits= ''.join(char for char in text if not char.isdigit())
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    is_palindrome = cleaned == cleaned[::-1]
    if is_palindrome:
        palindrome_result = "The string is a palindrome."
    else:
        palindrome_result = text[:5][::-1]
        

    return longest , len(words) , reversed_words , removing_digits , text.swapcase() , cleaned == cleaned[::-1] , palindrome_result
text1 = "Iam maI"
text2="I did this code long time ago. "
x= get_extended_string_info(text1)
y=get_extended_string_info(text2)
print (x)
print(y)