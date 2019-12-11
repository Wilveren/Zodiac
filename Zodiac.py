#Author: William Everett McLean www.wmcleancv.ninja
#Purpose: Originally written as a Lambda function. Receives a Month and Date as input, determines
#         the appropriate western zodiak sign, and returns a formatted line of text with the sign.

import json

print('Loading function')


def lambda_handler(event, context):
    month=event['month'] #Line for month input
    day=event['day'] #Line for day input
	#Data sanitization. Convert all characters in month to lowercase, and remove any blank spaces.
    month = month.lower() 
    month = month.strip()
	#First if statement makes sure day is an integer number, that it is not negative, and that 
	#it is less than 32. If any of this is not true, no other checking is done, error message
	#will be output.
    if  (isinstance(day, int)) and (day < 32) and (day >= 1): 
        if (month == 'december') and (day <= 31):
            astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
        elif (month == 'january') and (day<=31):
            astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
        elif (month == 'february') and (day <=29):
            astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
        elif (month == 'march') and (day<=31):
            astro_sign = 'Pisces' if (day < 21) else 'Aries'
        elif (month == 'april') and (day <=30):
            astro_sign = 'Aries' if (day < 20) else 'Taurus'
        elif (month == 'may') and (day <=31):
            astro_sign = 'Taurus' if (day < 21) else 'Gemini'
        elif (month == 'june') and (day <=30):
            astro_sign = 'Gemini' if (day < 21) else 'Cancer'
        elif (month == 'july') and (day <=31):
            astro_sign = 'Cancer' if (day < 23) else 'Leo'
        elif (month == 'august') and (day <= 31):
            astro_sign = 'Leo' if (day < 23) else 'Virgo'
        elif (month == 'september') and (day <=30):
            astro_sign = 'Virgo' if (day < 23) else 'Libra'
        elif (month == 'october') and (day <= 31):
            astro_sign = 'Libra' if (day < 23) else 'Scorpio'
        elif (month == 'november') and (day <= 30):
            astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
        else:
            astro_sign = "None, because that's not a valid date." #If the month entered is not a real month, or is misspelled, 
			                                                      #astro-sign is set to error message.
    else:
        astro_sign = "None, because that's not a valid date." #Error message that is set if first if statement is not true.
    return{
        "Your Zodiac Sign is ": astro_sign
    }
