# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:15:22 2021

@author: T430
"""

from math import sqrt

class equationsolver:
    def __init__(self, a=0, b=0, c=0):
        self.slope = a
        self.slopen = b
        self.constant = c
        
    def form(self):
        print(f'({self.slope})x^2 + ({self.slopen})x + ({self.constant}) = 0')
        
    def solution(self):
        test = (self.slopen^2 - 4*self.slope*self.constant)
        base = 2*self.slope
        front = -self.slopen/base 
        if test >= 0:
            self.out = (-self.slopen+sqrt(test))/(2*self.slope)
            self.out1 = (-self.slopen-sqrt(test))/(2*self.slope)
            print(f'x = {self.out}, {self.out1}')
        else:
            test = -test
            test = sqrt(test)
            test = test/base
            print ('Imaginary number')
            print (f'x={front}-{test}i, {front}+{test}i')
        
fiit = equationsolver(1,5,-14)               
fiit.form()
fiit.solution()




fiit = equationsolver(1,5,14)               
fiit.form()
fiit.solution()

equationsolver.solution(fiit)


'''has to add more here'''











































