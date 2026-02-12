# User-validation checker
Problem Statement
The program asks for four things:
- Full Name
- Email ID
- Mobile Number
- Age
- 
  It checks each one based on certain rules. If everything’s good, you get “User Profile is VALID.” If not, you get “User Profile is INVALID.

   
Validation Rules
  
   - Full Name: Has to have at least two words. Can’t start or end with a space.
   - Email ID: Needs at least one @ and one . Can’t start with @.
  -  Mobile Number: Exactly 10 digits, only numbers, and shouldn’t start with 0.
  -  Age: Must be over 18 and no more than 60.


  
Algorithm
- Ask for your full name, email, mobile number, and age.
- Check the full name for the right number of spaces and no leading or trailing spaces.
- Check the email for @ and . and make sure it’s not starting with @.
- Check the mobile number for length, digits, and starting digit.
- Make sure the age is in the right range.
- Print out if the profile is valid or not.

 Code Snippets
 
  <img width="1729" height="1107" alt="Screenshot 2026-01-29 194930" src="https://github.com/user-attachments/assets/d8a7f4ab-1307-4fd8-ac30-486dc13ca79b" />
  
  # Smart ID & Credential Validator
  
  ## Problem Statement

This program is part of a university Smart Registration System.
It validates student credentials before approving an account.

The program takes:

- Student ID
 - Email ID
 - Password
 - Referral Code

If all inputs are valid, it prints APPROVED.
Otherwise, it prints REJECTED.

## Validation Rules

- Student ID must follow the format CSE-XX
- Email ID must contain @, ., and end with .edu
- Password must be at least 8 characters, start with an uppercase letter, and contain a digit
- Referral Code must follow the format REF##@

## Approach

- Read all inputs from the user.
- Validate each input using string operations and conditions.
- Check all rules one by one.
- Print APPROVED if all validations pass, else REJECTED.

## Constraints

- Strings and conditional statements only
- No loops, lists, regex, or external libraries
<img width="1786" height="1042" alt="image" src="https://github.com/user-attachments/assets/355e1cab-b39e-4cc5-97b4-334ae0a13c92" />

# Student Performance Analyzer
## Description

This program analyzes student marks using basic Python concepts.
Marks are stored in a list, updated using a personalized rule, and then classified into performance categories.

## Concepts Used

- for loop

- list

- string

-conditional statements

## Classification Rules

- 90–100 → Excellent

- 75–89 → Very Good

- 60–74 → Good

- 40–59 → Average

- 0–39 → Fail

- < 0 or > 100 → Invalid

## Personalized Logic

Personalization is based on the last digit of the registration number:

If the digit is even, all marks are decreased by 1

If the digit is odd, all marks are increased by 1

This personalization changes the final classification.

## Output

Displays category for each mark

Counts total valid students

Counts total failed students

Prints final summary
## sample test case output

enter no.of student marks:3

enter marks of student in subject 1:23

enter marks of student in subject 2:34

enter marks of student in subject 3:45

Enter your registration number last digit: 4

marks after updation: [22, 33, 44]

22 ->fail

33 ->fail

44 ->average

total valid students are : 3

total fail students are: 2
<img width="1807" height="1007" alt="image" src="https://github.com/user-attachments/assets/22bccb24-e74b-4746-b638-4da4197556a5" />

# Student Data Filter Program
## Problem Statement

This program processes a mixed list of numbers and strings.
It separates them into two different lists using a for loop.
It also applies one personalized logic rule.
## Base Logic

- If element is number → add to numberList

- If element is string → add to stringList

- Ignore empty strings ("")

- Count total numbers

- Count total strings

## Personalization Used

Option B – Name Length Logic

My Name: Mahesh
Name Length: 6

If name length is even →
Remove the first element from both lists

If name length is odd →
Remove the last element from both lists

Since my name length is even,
the first element is removed from both lists.

## Output Format

- Display final Number List

- Display final String List

- Display Total Numbers

- Display Total Strings

## Concepts Used

- List

- For loop

- Conditional statements

- String handling

## Rules Followed

- No dictionary

- No set

- No filter() or map()

- No list comprehension

- No hard-coded output
<img width="1864" height="1138" alt="image" src="https://github.com/user-attachments/assets/c60cf7a8-c550-41c8-9ced-608412b53eca" />


  
