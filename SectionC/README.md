# Section C: Code Challenge

## Option 1: Say the Number
Problem Statement: Create a function that takes a numeral (just digits without separators (e.g. 19093 instead of 19,093) and returns the standard way of reading a number, complete with punctuation.

## Description:
- ### Instructions to run the code:
	- Step1: Clone the repostitory 
	- Step2: Goto SectionC folder, and run the file ***say_the_number.py***
	- Step3: Enter the number to generate its output.

- ### Instructiont to run the testSuit:
	- Goto SectionC Folder and run the following command from terminal: ***python3 -m unittest tests.py***
    - It consist of 3 test cases :
		- sayNumber(0) ➞ "Zero."
		- sayNumber(11) ➞ "Eleven."
		- sayNumber(90376000010012) ➞ "Ninety trillion, three hundred and seventy six billion, ten thousand and twelve."

- ### The worst-case space complexity is O(n) as we are initializing a list for ones and tens words.
