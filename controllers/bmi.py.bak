# coding: utf8

#def index():

#This will create a form and call bmi_calculator.html passing the form object
def bmi_calculator():
    form=FORM(TABLE(TR("Weight",INPUT(_type="text",_name="w",requires=IS_NOT_EMPTY()),"kilograms"),
                     TR("Height",INPUT(_type="text",_name="h",requires=IS_NOT_EMPTY()),"centimeters"),
                     TR("",INPUT(_type="submit",_value="Calculate"))))
    if form.accepts(request,session):
        #response.flash="form accepted"
        response.vars =  bmi_calculate()
        return dict(form=form,vars=response.vars)
    elif form.errors:
        response.flash="All fields are mandatory"
    else:
        #response.flash="please fill the form"
        pass
    return dict(form=form)
    

#Actual calculation of bmi is done here.        
def bmi_calculate():
    weight = float(request.vars.w.strip())
    height = (float(request.vars.h.strip()))/100
    bmi=0.0
        
    bmi = calculate_bmi(weight,height)
    #bmi = float("{0:.1f}".format(bmi))
    
    if(bmi): return float("{0:.2f}".format(bmi))
    else :
        respronse.flash= "There was a problem calculating BMI, Please try again later"
        return
