#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Mo2N111_0.5"
shortDesc = u""
longDesc = u"""
Based primarily on "Anisotropic N-Modification of the Mo4 Ensemble for Efficient Ammonia Synthesis on Molybdenum Nitrides"
https://doi.org/10.1021/acs.jpcc.9b09405
"""

#entry(
#    index = 1,
#    label = "H2 + X + X <=> H_X + H_X",
#    kinetics = StickingCoefficient(
#        A = 5.39E8,
#        n = 0,
#        Ea = (0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R1""",
#    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
#    metal = 'Mo',
#)

#entry(
#    index = 2,
#    label = "N2 + X + X <=> N_X + N_X",
#    kinetics = StickingCoefficient(
#        A = 6.33,
#        n = 0,
#        Ea = (147570, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R2""",
#    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
#    metal = 'Mo',
#)

#entry(
#    index = 5,
#    label = "N2 + X <=> N2_X",
#    kinetics = StickingCoefficient(
#        A = 1.44E8,
#        n = 0,
#        Ea = (0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R5""",
#    longDesc = u"""N2 Surface_Adsorption_vdW""",
#    metal = 'Mo',
#)

#entry(
#    index = 11,
#    label = "NH3 + X <=> NH3_X",
#    kinetics = StickingCoefficient(
#        A = 4.86E16,
#        n = 0,
#        Ea = (0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R11""",
#    longDesc = u"""Surface_Adsorption_vdW """,
#    metal = 'Mo',
#)

#entry(
#    index = 12,
#    label = "NH3_X + X <=> NH2_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (7.72E4, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (105130, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R12""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Mo",
#)

#entry(
#    index = 13,
#    label = "NH2_X + X <=> NH_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (1.36E9, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (39540, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R13""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Mo",
#)

#entry(
#    index = 14,
#    label = "NH_X + X <=> N_X + H_X",
#    kinetics = SurfaceArrhenius(
#        A = (1.41E2, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (141780, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R14""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Mo",
#)

entry(
    index = 48,
    label = "H_X + H_X <=> H2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (1.49E3, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (156250, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R1""",
    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
    metal = 'Mo',
)

entry(
    index = 49,
    label = "N_X + N_X <=> N2 + X + X",
    kinetics = SurfaceArrhenius(
        A = (2.22E-11, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (331530, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R2""",
    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
    metal = 'Mo',
)

entry(
    index = 52,
    label = "N2_X <=> N2 + X",
    kinetics = SurfaceArrhenius(
        A = (4.89E16, '1/s'),  
        n = 0.0,
        Ea = (15430, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R5""",
    longDesc = u"""N2 Surface_Adsorption_vdW""",
    metal = 'Mo',
)

entry(
    index = 58,
    label = "NH3_X <=> NH3 + X",
    kinetics = SurfaceArrhenius(
        A = (9.67E9, '1/s'),  
        n = 0.0,
        Ea = (83910, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R11""",
    longDesc = u"""Surface_Adsorption_vdW """,
    metal = 'Mo',
)

entry(
    index = 59,
    label = "NH2_X + H_X <=> NH3_X + X",
    kinetics = SurfaceArrhenius(
        A = (4.68E1, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (158180, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R12""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Mo",
)

entry(
    index = 60,
    label = "NH_X + H_X <=> NH2_X + X",
    kinetics = SurfaceArrhenius(
        A = (2.88E2, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (134070, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R13""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Mo",
)

entry(
    index = 61,
    label = "N_X + H_X <=> NH_X + X",
    kinetics = SurfaceArrhenius(
        A = (4.39E3, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (123460, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R14""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Mo",
)