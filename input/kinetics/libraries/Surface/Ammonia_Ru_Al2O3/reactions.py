#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ru_Al2O3"
shortDesc = u""
longDesc = u"""
Based primarily on "Correlating Particle Size and Shape of Supported Ru/γ-Al2O3 Catalysts with NH3 Decomposition Activity"
https://doi.org/10.1021/ja902587k
yman M. Karim, Vinay Prasad, Giannis Mpourmpakis, William W. Lonergan, Anatoly I. Frenkel, Jingguang G. Chen†, and Dionisios G. Vlachos
J. Am. Chem. Soc. 2009, 131, 34, 12230–12239
"""

entry(
    index = 1,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = 7.73E-4,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R1""",
    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
    metal = 'Ru',
)

entry(
    index = 2,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 2.41,   #should be less than 1? maybe change it to SurfaceArrhenius?
        n = 0,
        Ea = (38492, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R2""",
    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
    metal = 'Ru',
)

entry(
    index = 11,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 2.79E-1,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R11""",
    longDesc = u"""Surface_Adsorption_vdW """,
    metal = 'Ru',
)

entry(
    index = 12,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.62E9, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (85772, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R12""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Ru",
)

entry(
    index = 13,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (1.10E16, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (124683, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R13""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Ru",
)

entry(
    index = 14,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (6.4E14, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (103344, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R14""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Ru",
)

#entry(
#    index = 48,
#    label = "H_X + H_X <=> H2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (2.5E12, 'm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (102926, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R1""",
#    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
#    metal = 'Ru',
#)

#entry(
#    index = 49,
#    label = "N_X + N_X <=> N2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (1.18E15, 'm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (115896, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R2""",
#    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
#    metal = 'Ru',
#)

#entry(
#    index = 58,
#    label = "NH3_X <=> NH3 + X",
#    kinetics = SurfaceArrhenius(
#        A = (6.55E13, '1/s'),  
#        n = 0.0,
#        Ea = (83680, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R11""",
#    longDesc = u"""Surface_Adsorption_vdW """,
#    metal = 'Ru',
#)

#entry(
#    index = 59,
#    label = "NH2_X + H_X <=> NH3_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (3.81E16, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (102508, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R12""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Ru",
#)

#entry(
#    index = 60,
#    label = "NH_X + H_X <=> NH2_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (4.99E14, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (129704, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R13""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Ru",
#)

#entry(
#    index = 61,
#    label = "N_X + H_X <=> NH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (1.58E15, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (105018, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R14""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Ru",
#)