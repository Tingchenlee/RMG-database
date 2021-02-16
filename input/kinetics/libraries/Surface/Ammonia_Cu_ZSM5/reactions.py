#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Cu_ZSM5"
shortDesc = u""
longDesc = u"""
Based primarily on "Detailed Kinetic Modeling of NH3 and H2O Adsorption, and NH3 Oxidation over Cu-ZSM-5"
https://doi.org/10.1021/jp802449s
J. Phys. Chem. C 2009, 113, 1393–1405
Hanna Sjovall, Richard J. Blint, and Louise Olsson
"""

#entry(
#    index = 3,
#    label = "O2 + X + X <=> O_X + O_X",
#    kinetics = StickingCoefficient(
#        A = 3.2E12,
#        n = 0,
#        Ea = (83250, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R3""",
#    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
#	metal = "Cu",
#)

#entry(
#    index = 6,
#    label = "O2 + X <=> O2_X",
#    kinetics = StickingCoefficient(
#        A = 3.2E12,
#        n = 0,
#        Ea = (48770, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R6""",
#    longDesc = u"""O2 Surface_Adsorption_vdW""",
#    metal = 'Cu',
#)

#entry(
#    index = 10,
#    label = "H2O + X <=> H2O_X",
#    kinetics = StickingCoefficient(
#        A = 1.18E3,
#        n = 0,
#        Ea = (0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R10""",
#    longDesc = u"""Surface_Adsorption""",
#	metal = "Cu",
#)

#entry(
#    index = 11,
#    label = "NH3 + X <=> NH3_X",
#    kinetics = StickingCoefficient(
#        A = 1.15E3,
#        n = 0,
#        Ea = (0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R11""",
#    longDesc = u"""Surface_Adsorption_vdW """,
#    metal = 'Cu',
#)

entry(
    index = 7,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (3.2E12, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (84370, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R7""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Cu",
)

entry(
    index = 15,
    label = "NH3_X +O_X <=> NH2_X + OH_X",
    kinetics = SurfaceArrhenius(
        A = (4.1E5, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (97360, 'J/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R15""",
    longDesc = u"""Surface_Abstraction_vdW""",
    metal = "Cu",
)

entry(
    index = 18,
    label = "NH3_X + OH_X <=> NH2_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (3.52E9, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (103930, 'J/mol'),   
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R18""",
    longDesc = u"""Doesn't fit RMG surface families""",
    metal = "Cu",
)

#O2 recombination?
entry(
    index = 50,
    label = "O_X + O_X <=> O2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (3.2E12, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (161390, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R3""",
    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
	metal = "Cu",
)

entry(
    index = 53,
    label = "O2_X <=> O2 + X",
    kinetics = SurfaceArrhenius(
        A = (3.2E12, '1/s'),  
        n = 0.0,
        Ea = (48770, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R6""",
    longDesc = u"""O2 Surface_Adsorption_vdW""",
    metal = 'Cu',
)

entry(
    index = 57,
    label = "H2O_X <=> H2O + X",
    kinetics = SurfaceArrhenius(
        A = (1.23E13, '1/s'),  
        n = 0.0,
        Ea = (119070, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R10""",
    longDesc = u"""Surface_Adsorption""",
	metal = "Cu",
)

entry(
    index = 58,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (1.23E10, '1/s'),  
        n = 0.0,
        Ea = (117920, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R11""",
    longDesc = u"""Surface_Adsorption_vdW """,
    metal = 'Cu',
)

