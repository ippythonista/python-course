# Exercise 15

Generate a CPF.

- First digit:
    - Collect the sum of the 9 digits generated
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
    - Collect the sum of the first 9 digits generated + the `first digit`
      by multiplying each value by a
      countdown starting from 11
    - Add up all the results
    - Multiply the previous result by 10
    - Obtain the remainder of the division of the previous calculation by 11
    - If the previous result is greater than 9:
        - the result is 0
    - Otherwise:
        - the result is the value of the calculation
