#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.88175e+08,'s^-1'), n=1.02402, w0=(1.183e+06,'J/mol'), E0=(163199,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024954204374586366, var=5.668387833110564, Tref=1000.0, N=5, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 4.835647721748436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 4.835647721748436""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 4.835647721748436
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.05586e+09,'s^-1'), n=0.901614, w0=(1.183e+06,'J/mol'), E0=(153839,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013988350281361622, var=3.310141215464579, Tref=1000.0, N=3, correlation='Root_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.68252020871715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.68252020871715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.68252020871715
""",
)

entry(
    index = 3,
    label = "Root_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.0786e+07,'s^-1'), n=1.38493, w0=(1.183e+06,'J/mol'), E0=(180119,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.97374e+08,'s^-1'), n=1.02884, w0=(1.183e+06,'J/mol'), E0=(139192,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.38397e+10,'s^-1'), n=0.696144, w0=(1.183e+06,'J/mol'), E0=(164801,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

