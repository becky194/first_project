#bmi calculator for weight i.e body mass index
name1 = "emeka"
height_m1 = 8
weight_kg1 = 50

name2 = "nneka"
height_m2 = 8
weight_kg2 = 50

name3 = "chioma"
height_m3 = 65
weight_kg3 = 50

def bmi_calculator (name, height_m, weight_kg):
    bmi = weight_kg / (height_m **2)
    print ("BMI:")
    print(bmi)
    if bmi < 25:
        return name + " You are not over weight"
    else:
        return name + " You are over weight!!"
    
result1  = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3= bmi_calculator(name3, height_m3, weight_kg3)

print (result1)
print (result2)
print (result3)


