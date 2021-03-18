#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.02E14, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(11.5, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
    Xu, Clayton, Balakotaiah, Harold et al.
    doi: 10.1016.j.apcatb.2007.08.008
""",
    metal = "Pt",
)

entry(
    index = 4,
    label = "HOCXO_1 + Ni_4 <=> OCX_3 + HOX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.46E20, 'm^2/(mol*s)'),
        n = -0.213,
        Ea=(54300.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R4
""",
    metal = 'Ni',
)

entry(
    index = 10,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.586e16, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(12.9139069, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 10 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
4.667E11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.586e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 9,
    label = "NH2_X + Ni_4 <=> NHX_1 + HX_5",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (2.718e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (75.74, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH2 Surface Dissociation""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R9
    """,
    metal = "Ni",
)

entry(
    index = 11,
    label = "NHX_2 + Ni_4 <=> NX + HX_5",
    kinetics = SurfaceArrhenius(
        A = (6.213e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (22.93, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH Surface Dissociation""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R11
    """,
    metal = "Ni",
)

entry(
    index = 16,
    label = "CH2X_3 + HX_5 <=> CH3X_1 + Ni_4",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A=(3.09E19, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(57200.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R16
""",
    metal = "Ni",
)


entry(
    index = 18,
    label = "CHX_3 + HX_5 <=> CH2X_1 + Ni_4",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(9.77E20, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(81000.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R18
""",
    metal = "Ni",
)

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R20.
#entry(
#    index = 19,
#    label = "CHX_1 + Ni_4 <=> CX_3 + HX_5",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A=(9.88E16, 'm^2/(mol*s)'),
#        n = 0.5,
#        Ea=(21900.0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    rank = 10,
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#Delgado et al
#Catalysts, 2015, 5, 871-904. Reaction R19
#""",
#    metal = "Ni"
#)

entry(
    index = 20,
    label = "CX_3 + HX_5 <=> CHX_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.70E20, 'm^2/(mol*s)'),
        n = -0.5,
        Ea=(157900., 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R20
""",
    metal = "Ni",
)

entry(
    index = 28,
    label = "HCOO* + Ni_4 <=> HCO* + OX_3",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(8.733e16, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 28 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.570E12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 8.733e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 31,
    label = "HCOH* + HX_5 <=> CH2OH* + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.257e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(54.4228933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 32 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
3.698E12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.257e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 32,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.25E16, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(29600.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R32
""",
    metal = "Ni",
)

entry(
    index = 15,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(7.452e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(38.7417207, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 15 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.193E13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 7.452e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 36,
    label = "CH3O2* + Ni_4 <=> CH2OH*_2 + OX_3",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.864e18, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(46.3517015, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 36 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.485E13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.864e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 48,
    label = "CXHO_1 + Ni_4 <=> OCX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.71E17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R8
""",
    metal = "Ni",
)

entry(
    index = 26,
    label = "OCX_3 + HX_5 <=> CXHO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.140e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(22.8299425, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 26 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.240E12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.140e17 m^2/(mol*s)
""",
    metal = "Cu",
)
entry(
    index = 49,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.01e+21,'cm^2/(mol*s)'), n=0, Ea=(110,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111
Original entry: NH2_X + X <=> NH_X + H_X
"Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study"
W. K. Offermans, A. P. J. Jansen, R. A. van Santen, G. Novell-Leruth, J. M. Ricart, and J. Pérez-Ramírez
The Journal of Physical Chemistry C 2007 111 (47), 17551-17557
https://doi.org/10.1021/jp073083f
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 5E12(1/s)/2.483E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.9e+21,'cm^2/(mol*s)'), n=0, Ea=(118,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Pt111
Original entry: NH_X + X <=> N_X + H_X
"Ammonia Dissociation on Pt(100), Pt(111), and Pt(211): A Comparative Density Functional Theory Study"
W. K. Offermans, A. P. J. Jansen, R. A. van Santen, G. Novell-Leruth, J. M. Ricart, and J. Pérez-Ramírez
The Journal of Physical Chemistry C 2007 111 (47), 17551-17557
https://doi.org/10.1021/jp073083f
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A = 7.2E12(1/s)/2.483E-9(mol/cm^2)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(7.36e+15,'cm^2/(mol*s)'), n=0, Ea=(189.04,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """N2 Surface_Adsorption_Dissociative""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Ni111_decomposition
Original entry: NH2_X + X <=> NH_X + H_X
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
    index = 52,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.14e+19,'cm^2/(mol*s)'), n=0, Ea=(57.87,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Ni111_decomposition
Original entry: NH_X + X <=> N_X + H_X
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

entry(
    index = 53,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.3e+20,'cm^2/(mol*s)'), n=0, Ea=(86.81,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Ni211_decomposition
Original entry: NH2_X + X <=> NH_X + H_X
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
    index = 54,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.34e+21,'cm^2/(mol*s)'), n=0, Ea=(100.31,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ammonia_Ni211_decomposition
Original entry: NH_X + X <=> N_X + H_X
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

