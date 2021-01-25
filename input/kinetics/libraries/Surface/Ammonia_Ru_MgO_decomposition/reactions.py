#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ru_MgO_decomposition"
shortDesc = u""
longDesc = u"""
Based primarily on "Kinetic Analysis of Decomposition of Ammonia over Nickel and Ruthenium Catalysts"
https://doi.org/10.1252/jcej.14we431
"""
entry(
    index = 1,
    label = " NH3 + X <=> NH3_X ",
    kinetics = StickingCoefficient(
        A = 8.36E1,
        n = 0,
        Ea = (0, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""""",
    metal = "Ru",
)

entry(
    index = 2,
    label = " N_X + N_X  <=>  N2 + X + X ",
    kinetics = SurfaceArrhenius(
        A = (1.34E14, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (105.8, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Ru",
)

#rmgpy.exceptions.DatabaseError: RMG does not accept reactions with more than 3 reactants in its solver. Reaction NH3_X + X + X + X <=> N_X + H_X + H_X + H_X in kinetics library Surface/Ammonia_Ru_MgO_decomposition has 4 reactants.
#In this paper, the NH3 dehydrogenation step is written as a single-step reaction
#because dehydrogenation of NH3 proceeds very rapidly. 
#Also, the rate of formation of NH3 from N(a) and H(a) is much slower than 
#the rate of NH3 dehydrogenation under the reaction conditions in this study(atmospheric pressure)
#entry(
#    index = 3,
#    label = " NH3_X + X + X + X <=>  N_X + H_X + H_X + H_X ",
#    kinetics = SurfaceArrhenius(
#        A= (6.26E5, 'm^2/(mol*s)'),  #need to check the unit of A
#        n = 0.0,
#        Ea = (123.5, 'kJ/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""""",
#    longDesc = u"""
#""",
#    metal = "Ru",
#)

entry(
    index = 4,
    label = " H_X + H_X <=>  H2 + X + X ",
    kinetics = SurfaceArrhenius(
        A = (7.18E2, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (67.8, 'kJ/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""
""",
    metal = "Ru",
)