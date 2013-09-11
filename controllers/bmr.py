# coding: utf8


def bmr_calculator():
    form=FORM(TABLE(TR(("Weight",INPUT(_type="text",_name="w",requires=IS_NOT_EMPTY()),"kilograms")),
                     TR("Height",INPUT(_type="text",_name="h",requires=IS_NOT_EMPTY()),"centimeters"),
                     TR("Age",INPUT(_type="text",_name="a",requires=IS_NOT_EMPTY())),
                     TR("Gender",SELECT('Male','Female',_name="g",requires=IS_IN_SET(['Male','Female']))),
                     TR("",INPUT(_type="submit",_value="Calculate"))))
    if form.accepts(request,session):
        #response.flash="form accepted"
        response.vars = calculate()
        return dict(form=form,vars=response.vars)
    elif form.errors:
        response.flash="All fields are mandatory"
    else:
        #response.flash="please fill the form"
        pass
    
    return dict(form=form)



def calculate():    
    weight = float(request.vars.w.strip())
    height = float(request.vars.h.strip())
    age = float(request.vars.a.strip())
    gender = request.vars.g.strip()
    
    if(int(age)>120): return ("Please provide correct age information")
    #print weight,height,age,gender
    bmr = calculate_bmr(weight,height,age,gender)
    if bmr: return float("{0:.0f}".format(bmr))
    else:
        respronse.flash= "There was a problem calculating BMR, Please try again later" 
        return false
