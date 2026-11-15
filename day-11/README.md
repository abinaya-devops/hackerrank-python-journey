Day 11 – String Validators

Platform: HackerRank
Language: Python
Challenge: String Validators
Status: Completed ✅

📌 Problem Description

Given a string "S", check whether it contains:

1. Alphanumeric characters
2. Alphabetical characters
3. Digits
4. Lowercase characters
5. Uppercase characters

Print "True" if at least one character matches the condition; otherwise, print "False".

💡 Concepts Learned

1. String Validation Methods

Method| Purpose
"isalnum()"| Checks letters and numbers
"isalpha()"| Checks alphabetic characters
"isdigit()"| Checks digits
"islower()"| Checks lowercase characters
"isupper()"| Checks uppercase characters

2. For Loop

Used "for char in S" to iterate through each character in the string.

The "char" variable stores the current character during each iteration.

3. any() Function

Used "any()" to check whether at least one character satisfies a given condition.

- Returns "True" if at least one condition is True.
- Returns "False" if all conditions are False.

4. Generator Expression

Learned to use:

any(char.isdigit() for char in S)

This checks each character without creating a separate list.

💻 Solution

if __name__ == '__main__':
    S = input()

    print(any(char.isalnum() for char in S))
    print(any(char.isalpha() for char in S))
    print(any(char.isdigit() for char in S))
    print(any(char.islower() for char in S))
    print(any(char.isupper() for char in S))

🧪 Sample Input

qA2

📤 Sample Output

True
True
True
True
True

📚 Key Takeaways

- Practiced Python's built-in string validation methods.
- Understood character-by-character iteration using a "for" loop.
- Learned how "any()" works.
- Practiced generator expressions.
- Understood the difference between checking an entire string and checking whether it contains at least one matching character.

Day 11 successfully completed! 🎯
