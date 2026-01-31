Test Cases for Simple Calculator Application (Markdown)

TC-01: Addition of two positive numbers



Test Case ID: TC\_ADD\_01



Test Description:

Verify that the calculator correctly adds two positive numbers.



Preconditions:



Calculator application is launched



Input fields are empty



Test Steps:



Enter 10 in Number 1 field



Enter 20 in Number 2 field



Click on the Add (+) button



Expected Result:



Result should be displayed as 30



TC-02: Subtraction resulting in negative number



Test Case ID: TC\_SUB\_01



Test Description:

Verify subtraction when the result is a negative number.



Preconditions:



Calculator application is launched



Test Steps:



Enter 10 in Number 1 field



Enter 25 in Number 2 field



Click on the Subtract (-) button



Expected Result:



Result should be displayed as -15



TC-03: Multiplication with decimal values



Test Case ID: TC\_MUL\_01



Test Description:

Verify multiplication of decimal numbers.



Preconditions:



Calculator application is launched



Test Steps:



Enter 2.5 in Number 1 field



Enter 4 in Number 2 field



Click on the Multiply (\*) button



Expected Result:



Result should be displayed as 10.0



TC-04: Division of two valid numbers



Test Case ID: TC\_DIV\_01



Test Description:

Verify division operation with valid inputs.



Preconditions:



Calculator application is launched



Test Steps:



Enter 20 in Number 1 field



Enter 5 in Number 2 field



Click on the Divide (/) button



Expected Result:



Result should be displayed as 4



TC-05: Division by zero (Invalid input)



Test Case ID: TC\_DIV\_02



Test Description:

Verify error message when dividing by zero.



Preconditions:



Calculator application is launched



Test Steps:



Enter 10 in Number 1 field



Enter 0 in Number 2 field



Click on the Divide (/) button



Expected Result:



Error message should be displayed like “Division by zero is not allowed”



TC-06: Non-numeric input validation



Test Case ID: TC\_INV\_01



Test Description:

Verify calculator behavior when non-numeric characters are entered.



Preconditions:



Calculator application is launched



Test Steps:



Enter abc in Number 1 field



Enter 5 in Number 2 field



Click on the Add (+) button



Expected Result:



Error message should be displayed



Calculation should not be performed



TC-07: BODMAS rule validation



Test Case ID: TC\_BODMAS\_01



Test Description:

Verify calculator follows BODMAS rule for expression 10 + 2 \* 5.



Preconditions:



Calculator application supports expressions



Test Steps:



Enter 10 + 2 \* 5



Click on Calculate



Expected Result:



Result should be 20 (Multiplication first, then addition)

