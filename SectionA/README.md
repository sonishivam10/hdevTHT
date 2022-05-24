# Section A: Code Review 
Given a question that a hypothetical student asks and the student’s submitted code. Required to answer the question and review their code’s correctness, efficiency, style and documentation.

## Option 2: Java Task : 


**Each Feedback category is assigned a reference number in Code at the end of line**

## Code Review:
- ### Correctness:

    - (Reference ***#CR1***) It will generate syntax error - as there is misspelled function call -  **reverseString instead of reverse_stringThe** .

    - (Reference ***#CF1***) Function call missing  - There is no call to function on this line which is required to generate the fibonaaci number. There should have been a function call similar to reverse_string one.

    - (Reference ***#CF2***) Invalid Name of Function Declared for Fibonaaci number generation, the 'function' keyword itself is used which is not accepted and a specific function name should be provided.

    - (Reference ***#CF3***) The function for generating Fibonnaci number is not **Generalized** for any 'N' provided as in the task description. It should have taken user input and generated Fibonacci for that N insted of printing Fibonnaci for N==10. <br>
    Also, it will give error as variable maxNumber is already defined in method <T>function(T). We cannot redefine it inside the function.<br>, better to change the type of parameter to int as there will also be bad operand types for binary operator '<=' 
    
    

- ### Style:

    - Overall code style is good, it could have been better given the naming convention was improved for functions.
    - (Reference ***#SF1***)  2nd function **FOR loop** needs to be indented properly for better readability as to which function it belongs . 
    - (Reference ***#SR1***) Printing on every recursive call is good while debuggin, but for production cost it is not required. Here in reverse_string function, "String to be passed in Recursive Function: " is repeatadly printed for every call.
    
- ### Efficiency:
    - Overall functions are effienct in Time complexity: O(n);

- ### Documentation:
    - Proper documentation is done for the particular code with comments for every line with description. 

``` java
public class recursion {
 
	public static void main(String[] args) {
 
		// Saves the string that would be reversed
		String myStr = "emosewA si avaJ";
 
 
		//create Method and pass and input parameter string 
		String reversed = reverse_string(myStr); 
		System.out.println("The reversed string is: " + reversed + 
                                   "\nFibonacci Series of 10 numbers:0 1 1 2 3 5 8 13 21 34 "); // *C1*
	}
 
 
	//Method take string parameter and check string is empty or not
	public static String reverse_string(String myStr)
	{
		if (myStr.isEmpty()){
		 System.out.println("String in now Empty");
		 return myStr;
		}
		//Calling Function Recursively
		System.out.println("String to be passed in Recursive Function: "+myStr.substring(1)); // *SR1*
		return reverseString(myStr.substring(1)) + myStr.charAt(0);} // *#CR1*

	public static <T> void function(T maxNumber) {    // *CF2*  *CF3*
		int maxNumber = 10; // *CF3*
		int previousNumber = 0;
		int nextNumber = 1;
		 
	    System.out.print("Fibonacci Series of "+maxNumber+" numbers:");
 
	for (int i = 1; i <= maxNumber; ++i){ // *CF3* , *SF1*
	    System.out.print(previousNumber+" ");
	    // On each iteration, we are assigning second number
	    // to the first number and assigning the sum of last two
	    // numbers to the second number
	    int sum = previousNumber + nextNumber;
	    previousNumber = nextNumber;
	    nextNumber = sum;
	    }
 
	}
 
}
```




