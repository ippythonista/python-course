# Exercise 14

Validate a CPF.

- Must have 11 digits
- Digits can't be a sequence

- First digit:
    - Collect the sum of the first 9 digits of the CPF
      by multiplying each value by a
      countdown starting from 10
    - Add up all the results
    - Multiply the previous result by 10
    - Obtain the remainder of the division of the previous calculation by 11
    - If the previous result is greater than 9:
        - the result is 0
    - Otherwise:
        - the result is the value of the calculation
- Second digit:
    - Collect the sum of the first 9 digits of the CPF + the `first digit`
      by multiplying each value by a
      countdown starting from 11
    - Add up all the results
    - Multiply the previous result by 10
    - Obtain the remainder of the division of the previous calculation by 11
    - If the previous result is greater than 9:
        - the result is 0
    - Otherwise:
        - the result is the value of the calculation

Validate the CPF by checking if generated CPF matches the one entered.
