# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:34:11 2020

@author: Barbara
"""
#input 
print("Enter your annual salary:")
annual_salary = float(input())
print("Enter the percent of your salary to save, as a decimal:")
portion_saved = float(input())
print("Enter the cost of your dream home:")
total_cost = float(input())

#defining variables
portion_down_payment= 0.25 * total_cost
initial_savings=0.0 
monthly_salary=annual_salary/12
portion_saved=0.1*monthly_salary
r=0.04

current_savings= initial_savings
number_of_months=0 
investments=0

#calculations
while (current_savings < portion_down_payment):
        current_savings= current_savings + portion_saved + investments
        number_of_months= number_of_months +1
        investments= current_savings*r/12
        
#printing results
print("number of months: %d" %number_of_months)