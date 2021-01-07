#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Fe100"
shortDesc = u""
longDesc = u"""
Based primarily on 
"Theoretical study of the ammonia nitridation rate on an Fe (100) surface: A combined density functional theory and kinetic Monte Carlo study"
https://doi.org/10.1063/1.4896610
"""
#In general, the atomic vibrational modes at these points are also used to calculate the pre-factor 
#in the kinetic Monte Carlo. All events in this study used a standard value of 10^13 s−1 for the atomic pre-factor

entry(
    index = 1,
    label = " NH3_X <=> NH3 + X ",
    kinetics = SurfaceArrhenius(
        A=(1E13, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (34.74, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Fe" ,
)

#Use NH3* -> N* +3H* dissociation mechanism rather than step-by-step
entry(
    index = 2,
    label = " NH3_X + X + X + X <=>  N_X + H_X + H_X + H_X ",
    kinetics = SurfaceArrhenius(
        A= (1E13, 'm^2/(mol*s)'),  #need to check the unit of A
        n = 0.0,
        Ea = (221.93, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Fe",
)