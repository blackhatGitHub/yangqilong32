#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class  Student:

    empCount = 0
    su_Countwl163=0
    su_Countwl161=0

    def __init__(self, name, su_no, male, su_class):
        self.name = name
        self.su_no=su_no
        self.male=male
        self.su_class=su_class
        Student.empCount += 1
        if self.su_class == 'wl163':
           Student.su_Count163 += 1
        elif self.su_class ==  'wl161' :
             Student.su_Count161 += 1
   
    def displaySutinfo(self):
     print "Total Employee %d" % Student.empCount
 
    def displaySudent(self):
      print "Name : ", self.name,  ", su_no: ", self.su_no , "male:",self.male, "su_class:",self.su_class
