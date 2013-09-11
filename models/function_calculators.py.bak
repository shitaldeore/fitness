# coding: utf8
#BMR = 10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) + 5         (man)
#BMR = 10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) - 161     (woman)
#Metric BMI Formula BMI = ( Weight in Kilograms / ( Height in Meters x Height in Meters ) )

def calculate_bmr(weight, height, age, gender):
		try :
			BMR = 0.0
			if(gender.lower()=='male'):
				BMR=(10*weight)+(6.25*height)-(5*age)+5
			else:
				BMR=10*weight+6.25*height-5*age-161
			print "BMR ", BMR	
			return BMR
			#print "BMR calculated", BMR
		except Exception, e:
			#print "Error occurred while calculating BMR" + str(e)
			return False
		return
		
		
def calculate_bmi(weight,height):
    try:
        BMI = 0.0
        BMI=float(weight/(height*height))
        #print "In function", BMI, weight, height
        return BMI
    except Exception, e1:
        #print "Error occurred while calculating BMR" + str(e1)
        return False
