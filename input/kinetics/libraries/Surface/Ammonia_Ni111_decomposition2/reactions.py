#!/usr/bin/env python
# encoding: utf-8

name = "Ammonia_Ni111_decomposition2"
shortDesc = u""
longDesc = u"""
Based primarily on "Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells"
https://doi.org/10.1016/j.ces.2011.07.007
Srinivas Apparia, Vinod M.Janardhanan, Sreenivas Jayantib, Lubow Maierc, Steffen Tischerc, Olaf Deutschmannc
Chemical Engineering Science
Volume 66, Issue 21, 1 November 2011, Pages 5184-5191
"""

entry(
    index = 1,
    label = "H2 + X + X <=> H_X + H_X",
    kinetics = StickingCoefficient(
        A = 1E-2,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R1""",
    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
    metal = 'Ni',
)

entry(
    index = 2,
    label = "N2 + X + X <=> N_X + N_X",
    kinetics = StickingCoefficient(
        A = 1E-6,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R2""",
    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
    metal = 'Ni',
)

entry(
    index = 3,
    label = "O2 + X + X <=> O_X + O_X",
    kinetics = StickingCoefficient(
        A = 1E-2,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R3""",
    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
	metal = "Ni",
)

entry(
    index = 7,
    label = "H_X + O_X <=> OH_X + X",
    kinetics = SurfaceArrhenius(
        A = (5E22, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (97900, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R7""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Ni",
)

entry(
    index = 8,
    label = "H_X + OH_X <=> H2O_X + X",
    kinetics = SurfaceArrhenius(
        A = (3E20, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (42700, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R8""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Ni",
)

entry(
    index = 10,
    label = "H2O + X <=> H2O_X",
    kinetics = StickingCoefficient(
        A = 1E-1,
        n = 0,
        Ea = (62090, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R10""",
    longDesc = u"""Surface_Adsorption""",
	metal = "Ni",
)

entry(
    index = 11,
    label = "NH3 + X <=> NH3_X",
    kinetics = StickingCoefficient(
        A = 1.1E-2,
        n = 0,
        Ea = (0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R11""",
    longDesc = u"""Surface_Adsorption_vdW """,
    metal = 'Ni',
)

entry(
    index = 12,
    label = "NH3_X + X <=> NH2_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (5.72E22, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (78990, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R12""",
    longDesc = u"""Surface_Dissociation_vdW""",
    metal = "Ni",
)

entry(
    index = 13,
    label = "NH2_X + X <=> NH_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (2.72E22, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (75740, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R13""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Ni",
)

entry(
    index = 14,
    label = "NH_X + X <=> N_X + H_X",
    kinetics = SurfaceArrhenius(
        A = (6.21E19, 'm^2/(mol*s)'), 
        n = 0.0,
        Ea = (22930, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""R14""",
    longDesc = u"""Surface_Dissociation""",
    metal = "Ni",
)

entry(
    index = 96,
    label = "OH_X + OH_X <=> O_X + H2O_X",
    kinetics = SurfaceArrhenius(
        A = (3E21, 'm^2/(mol*s)'),  
        n = 0.0,
        Ea = (100000, 'J/mol'),  
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    shortDesc = u"""Reverse R95""",
    longDesc = u"""""",
    metal = 'Ni',
)

#entry(
#    index = 48,
#    label = "H_X + H_X <=> H2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (3.32E19, 'm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (82210, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R1""",
#    longDesc = u"""H2 Surface_Adsorption_Dissociative""",
#    metal = 'Ni',
#)

#entry(
#    index = 49,
#    label = "N_X + N_X <=> N2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (4.44E22, 'm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (210840, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R2""",
#    longDesc = u"""N2 Surface_Adsorption_Dissociative""",
#    metal = 'Ni',
#)

#entry(
#    index = 50,
#    label = "O_X + O_X <=> O2 + X + X",
#    kinetics = SurfaceArrhenius(
#        A = (3.93E23, 'm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (473410, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R3""",
#    longDesc = u"""O2 Surface_Adsorption_Dissociative""",
#	metal = "Ni",
#)

#entry(
#    index = 54,
#    label = "OH_X + X <=> H_X + O_X",
#    kinetics = SurfaceArrhenius(
#        A = (1.76E21, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (36000, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R7""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Ni",
#)

#entry(
#    index = 55,
#    label = "H2O_X + X <=> H_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (2.07E21, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (91070, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R8""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Ni",
#)


#entry(
#    index = 57,
#    label = "H2O_X <=> H2O + X",
#    kinetics = SurfaceArrhenius(
#        A = (4.75E12, '1/s'),  
#        n = 0.0,
#        Ea = (62090, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R10""",
#    longDesc = u"""Surface_Adsorption""",
#	metal = "Ni",
#)

#entry(
#    index = 58,
#    label = "NH3_X <=> NH3 + X",
#    kinetics = SurfaceArrhenius(
#        A = (8.21E14, '1/s'),  
#        n = 0.0,
#        Ea = (78630, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R11""",
#    longDesc = u"""Surface_Adsorption_vdW """,
#    metal = 'Ni',
#)

#entry(
#    index = 59,
#    label = "NH2_X + H_X <=> NH3_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (1.32E24, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (48810, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R12""",
#    longDesc = u"""Surface_Dissociation_vdW""",
#    metal = "Ni",
#)

#entry(
#    index = 60,
#    label = "NH_X + H_X <=> NH2_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (3.70E19, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (74870, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R13""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Ni",
#)

#entry(
#    index = 61,
#    label = "N_X + H_X <=> NH_X + X",
#    kinetics = SurfaceArrhenius(
#        A = (2.07E19, 'm^2/(mol*s)'), 
#        n = 0.0,
#        Ea = (15604, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""Reverse R14""",
#    longDesc = u"""Surface_Dissociation""",
#    metal = "Ni",
#)

#entry(
#    index = 95,
#    label = "O_X + H2O_X <=> OH_X + OH_X",
#    kinetics = SurfaceArrhenius(
#        A = (5.87E23, 'm^2/(mol*s)'),  
#        n = 0.0,
#        Ea = (210270, 'J/mol'),  
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    shortDesc = u"""R95""",
#    longDesc = u"""""",
#    metal = 'Ni',
#)
