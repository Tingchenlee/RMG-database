#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 24,
    label = "CH2X_1 + HOX_3 <=> CH3X_4 + OX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.39E17, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(19000.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Deutschmann Ni""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R24
""",
	metal = "Ni",
)

entry(
    index = 26,
    label = "CHX_1 + HOX_3 <=> CH2X_4 + OX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.40E18, 'm^2/(mol*s)'),
        n = 0.101,
        Ea=(42400.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R26
""",
	metal = "Ni",
)

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R28.
#entry(
#    index = 27,
#    label = "OX_5 + CHX_4 <=> HOX_3 + CX_1 ",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A=(2.47E17, 'm^2/(mol*s)'),
#        n = 0.312,
#        Ea=(57700.0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    #rank = 3,
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#Delgado et al
#Catalysts, 2015, 5, 871-904. Reaction R27
#""",
#    metal = "Ni",
#)

entry(
    index = 28,
    label = "HOX_3 + CX_1 <=> OX_5 + CHX_4 ",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.43E17, 'm^2/(mol*s)'),
        n = -0.312,
        Ea=(118900.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R28
""",
	metal = "Ni",
)

entry(
    index = 39,
    label = "O* + HCO* <=> OH* + CO*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.298e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea=(0., 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 39 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.0e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.298e17 m^2/(mol*s)
""",
    metal = "Cu",
)
entry(
    index = 40,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(1.784e+21,'cm^2/(mol*s)'), n=0, Ea=(139911,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt211_oxidation
Original entry: NH2_X +O_X <=> NH_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 4.7E12(1/s)/2.634E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 41,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.291e+21,'cm^2/(mol*s)'), n=0, Ea=(45350,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt211_oxidation
Original entry: NH_X + O_X <=> N_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
This reaction used RMG's surface site density of Pt211 = 2.634E-9(mol/cm^2) to calculate the A factor.
A = 3.4E12(1/s)/2.634E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "211",
)

entry(
    index = 42,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.215e+21,'cm^2/(mol*s)'), n=0, Ea=(78157,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111_oxidation
Original entry: NH2_X +O_X <=> NH_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5.5E12(1/s)/2.483E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.141e+21,'cm^2/(mol*s)'), n=0, Ea=(154380,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111_oxidation
Original entry: NH_X + O_X <=> N_X + OH_X
"Structure- and Temperature-Dependence of Pt-Catalyzed Ammonia Oxidation Rates and Selectivities."
DMa, Hanyu; Schneider, William F.(2019). ACS Catalysis, 9(3), 2407-2414. 
https://doi.org/10.1021/acscatal.8b04251
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.8E12(1/s)/2.483E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "H2NX + O* <=> OH* + HNX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.46e+21,'cm^2/(mol*s)'), n=0, Ea=(87,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111
Original entry: NH2_X +O_X <=> NH_X + OH_X
"Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study"
W. K. Offermans, A. P. J. Jansen, R. A. van Santen, G. Novell-Leruth, J. M. Ricart, and J. Pérez-Ramírez
The Journal of Physical Chemistry C 2007 111 (47), 17551-17557
https://doi.org/10.1021/jp073083f
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 6.1E12(1/s)/2.483E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "HNX-2 + O* <=> OH* + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.06e+21,'cm^2/(mol*s)'), n=0, Ea=(84,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Abstraction""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111
Original entry: NH_X +O_X <=> N_X + OH_X
"Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study"
W. K. Offermans, A. P. J. Jansen, R. A. van Santen, G. Novell-Leruth, J. M. Ricart, and J. Pérez-Ramírez
The Journal of Physical Chemistry C 2007 111 (47), 17551-17557
https://doi.org/10.1021/jp073083f
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.6E12(1/s)/2.483E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "111",
)

