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

  
