# Zodiac
Function written in Python 3.7 which determines a user's western zodiac sign, given thir birth month and day. Originally written for use
as an AWS Lambda function, and was built in the Lambda code editor.

Data validation is included, so function is fully modular and ready to be used by larger applications.

To use, simply pass the variables "month" and "day" to the function. Month should be a string, day should be an integer. The code is 
smart enough to check this, and will return an error message if either the day or month are not valid. It will also
convert all letters in "month" to lowercase, and remove any whitespace. 

Update 1.2 - "day" will be typecast to integer upon initialization. Front-end website can only pass a number, so no need to worry about receiving a non-numeric character. However, if used in such a way that a non-numeric character or string could be passed to variable "day", some code will need to be updated to account for this. 
