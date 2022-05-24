""""
    Program to generate the standard way of reading a number with complete punctuation.
    Last Edited By: Shivam Soni , sonishivama@gmail.com
    Last Edited On: May 25, 2022
"""
class SectionC:
    def sayNumber(self, num):
        """
            Function to return the standard way of reading a number with complete punctuation.

            Args:     
                int (num): Number to get reading way for.
            Returns:
                string: standard way of reading the input number
        """

        #Define standard List a and b, for standard counting from 1-20 and in Tens 
        ones='zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ')
        tens='zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split(' ')

        
        def helperFunction(num,run=0):
            #Helper function for generating the text for num

            #Check if bith Number is equal to 0 and run>1 then we return empty string
            if (num==0 and run>1): return ""
            #Else check if run is greated than 1, if true go inside else go to next
            if run>1:
                #Check if number is less than 100, then return 'and' concatenated with recursively call of helper function after decreasing run by 1.
                if num<100: return 'and ' + helperFunction(num,-1)

                # Else return ', ' concatenated with recursively call of helper function after decreasing run by 1.
                return ', ' + helperFunction(num,-1)
            #Else check if numbers is less than 20, then return the value of list-> ones with index ==num   
            if num<20:return ones[num]

            #Else check if numbers is less than 100, then get the value of list-> tens with index==float division of num by 10   
            if num<100: return tens[num//10]+ (' '+ones[num%10] if num%10>0 else '')

            #Check for limit, between hundred, thousand, million, billion and trillion return accordingly 
            for limit,red,name in zip([3,6,9,12,15],[2,3,6,9,12],[' hundred ',' thousand ',' million ',' billion ',' trillion ']):
                if num<10**limit: return helperFunction(num//10**red,0)+ name + helperFunction(num%10**red,2)
        
        tmp=helperFunction(num)+'.'
        tmp=tmp[0].upper()+tmp[1:].replace(' .','.').replace(',.','.').replace(' ,',',')
        return tmp

if __name__=="__main__":

    #Standard workflow, initialize object of class, take input from user -> call the function -> save to result -> print result
    secB = SectionC()
    try:
        num = int(input("Please Enter any integer from 0 to 999,999,999,999,999. \n"))

        #Handle base case:
        if num<0:
            print("Please check input, it is not correct! \n Should be any integer from 0 to 999,999,999,999,999 ")
        else:
            result = secB.sayNumber(num)
            print(result)
    except Exception as e:
        print("Please check input, it is not correct! \n Should be any integer from 0 to 999,999,999,999,999 ", e)

    



