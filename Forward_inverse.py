# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:16:39 2022

@author: sanjay
"""

#Inverse

import math as m
#cartisian coordinates
x2=
y2=
#length of the links
l1=
l2=

desired_theta2=m.acos((x2*x2 + y2*y2 -l1*l1 -l2*l2)/(2*l1*l2))
desired_theta1=m.atan2(y2, x2)-m.atan2(l2*m.sin(desired_theta2), l1+l2*m.cos(desired_theta2))


#forward

theta1=
theta2=

xy_0 = np.array([0, 0])    #  (x0, y0)
xy_1 = np.array([np.cos(theta1), np.sin(theta1)]) *l1 + xy_0  # (x1, y1)
xy_2 = np.array([np.cos(theta1 + theta2), np.sin(theta1 + theta2)]) * l2 + xy_1 #endeffector