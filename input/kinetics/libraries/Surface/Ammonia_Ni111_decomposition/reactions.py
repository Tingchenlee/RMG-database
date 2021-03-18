#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ni111_decomposition"
shortDesc = u""
longDesc = u"""
Based primarily on "Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
Fuel Processing Technology. Vol 108, April 2013, 112-117
doi:10.1016/j.fuproc.2012.05.030
"""

entry(
    index = 1,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (1.35E21, 'cm^2/(mol*s)'),
        n = 0.,
        Ea = (106.10, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni111
6.73E10 s^-1 / 3.148E-9 mol/cm^2 =  1.35E21 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 2,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (9.49E19, 'cm^2/(mol*s)'),
        n = 0.,
        Ea = (110.92, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni111
2.32E7 s^-1 / 3.148E-9 mol/cm^2 = 9.49E19 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 3,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (7.36E15, 'cm^2/(mol*s)'),
        n = 0.,
        Ea = (189.04, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni111
4.26E12 s^-1 / 3.148E-9 mol/cm^2 =  7.36E15 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "111",
)

entry(
    index = 4,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.14E19, 'cm^2/(mol*s)'),
        n = 0.,
        Ea = (57.87, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni111
2.99E11 s^-1 / 3.148E-9 mol/cm^2 = 2.14E19 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "111",
)
