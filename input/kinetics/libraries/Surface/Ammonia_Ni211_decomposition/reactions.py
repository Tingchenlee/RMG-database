#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ni211_decomposition"
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
        A = (4.82E20, 'cm^2/(mol*s)'),
        n = 0.,
        Ea = (285.49, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""N2 Surface_Adsorption_Dissociative""",
    longDesc = u"""
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni211
1.61E12 s^-1 / 3.339E-9 mol/cm^2 = 4.82E20 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 2,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (5.50E19, 'cm^2/(mol*s)'),
        n = 0.,
        Ea = (63.66, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation_vdW""",
    longDesc = u"""
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni211
1.84E11 s^-1 / 3.339E-9 mol/cm^2 = 5.50E19 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 3,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.30E20, 'cm^2/(mol*s)'),
        n = 0.,
        Ea = (86.81, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni211
7.68E11 s^-1 / 3.339E-9 mol/cm^2 = 2.30E20 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "211",
)

entry(
    index = 4,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (3.34E21, 'cm^2/(mol*s)'),
        n = 0.,
        Ea = (100.31, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    shortDesc = u"""Surface_Dissociation""",
    longDesc = u"""
A factor is calculated by the Ea and the rate constant from table 2 in 
"Structure sensitivity of ammonia decomposition over Ni catalysts:
A computational and experimental study", Xuezhi Duan et al.
doi:10.1016/j.fuproc.2012.05.030

A factor from paper / surface site density of Ni211
1.12E13 s^-1 / 3.339E-9 mol/cm^2 = 3.34E21 cm^2/(mol*s)
""",
    metal = "Ni",
    facet = "211",
)
