#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 

def main():
    height = 1.75
    weight = 80.5
    bmi = weight / (pow(height, 2))
    if bmi < 18.5:
        print('BMI is{} ,过轻'.format(bmi))
    elif bmi < 25:
        print('BMI is {},正常'.format(bmi))
    elif bmi < 28:
        print('BMI is {},过重'.format(bmi))
    elif bmi < 32:
        print('BMI is {},肥胖'.format(bmi))
    else:
        print('BMI is {},严重肥胖'.format(bmi))
        

if __name__ == '__main__':
    main()
