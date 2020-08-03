#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.85374e+17,'s^-1'), n=-1.83768, w0=(1.12119e+06,'J/mol'), E0=(173502,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025527331643530864, var=13.437761713163445, Tref=1000.0, N=45, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 7.413007202868565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.413007202868565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 7.413007202868565
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.14434e+12,'s^-1'), n=-0.213861, w0=(1.183e+06,'J/mol'), E0=(155605,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06556540274050643, var=1.0896267833368551, Tref=1000.0, N=17, correlation='Root_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.2573837067834743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.2573837067834743""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.2573837067834743
""",
)

entry(
    index = 3,
    label = "Root_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.88716e+29,'s^-1'), n=-5.61524, w0=(953250,'J/mol'), E0=(176721,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3220579739815748, var=31.902856012731114, Tref=1000.0, N=4, correlation='Root_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R
    Total Standard Deviation in ln(k): 12.132458496976666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.132458496976666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.132458496976666
""",
)

entry(
    index = 4,
    label = "Root_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.50267e+13,'s^-1'), n=-0.29146, w0=(1.0665e+06,'J/mol'), E0=(250540,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.7355e+23,'s^-1'), n=-3.54792, w0=(1.11685e+06,'J/mol'), E0=(190508,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1911917618497877, var=8.835450755532378, Tref=1000.0, N=13, correlation='Root_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.439353310943183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.439353310943183""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.439353310943183
""",
)

entry(
    index = 6,
    label = "Root_2R!H->C",
    kinetics = ArrheniusBM(A=(5.12574e+08,'s^-1'), n=0.714448, w0=(1.13564e+06,'J/mol'), E0=(161206,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05529808856753447, var=19.135234226976447, Tref=1000.0, N=7, correlation='Root_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C
    Total Standard Deviation in ln(k): 8.908420703730865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C
Total Standard Deviation in ln(k): 8.908420703730865""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C
Total Standard Deviation in ln(k): 8.908420703730865
""",
)

entry(
    index = 7,
    label = "Root_N-2R!H->C",
    kinetics = ArrheniusBM(A=(6.14326e+16,'s^-1'), n=-1.8361, w0=(998167,'J/mol'), E0=(161987,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11555023331306274, var=26.70157621268825, Tref=1000.0, N=3, correlation='Root_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2R!H->C
    Total Standard Deviation in ln(k): 10.649508637103624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2R!H->C
Total Standard Deviation in ln(k): 10.649508637103624""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2R!H->C
Total Standard Deviation in ln(k): 10.649508637103624
""",
)

entry(
    index = 8,
    label = "Root_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.30229e+08,'s^-1'), n=0.995367, w0=(1.183e+06,'J/mol'), E0=(138104,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9718999497707853, var=2.1443634782942387, Tref=1000.0, N=4, correlation='Root_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.377622613249818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.377622613249818""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.377622613249818
""",
)

entry(
    index = 9,
    label = "Root_Ext-2R!H-R_7R!H->O",
    kinetics = ArrheniusBM(A=(7.47098e+12,'s^-1'), n=-0.267196, w0=(1.183e+06,'J/mol'), E0=(99317.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-2R!H-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(6.10297e+12,'s^-1'), n=-0.219372, w0=(1.183e+06,'J/mol'), E0=(156998,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3117547243793353, var=0.7508021641026269, Tref=1000.0, N=12, correlation='Root_Ext-2R!H-R_N-7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O
    Total Standard Deviation in ln(k): 2.520383036618955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.520383036618955""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 2.520383036618955
""",
)

entry(
    index = 11,
    label = "Root_Ext-5R!H-R_1R!H->O",
    kinetics = ArrheniusBM(A=(8.03589e+12,'s^-1'), n=-0.810259, w0=(938500,'J/mol'), E0=(143073,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004915336118469724, var=82.45074987938592, Tref=1000.0, N=2, correlation='Root_Ext-5R!H-R_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_1R!H->O
    Total Standard Deviation in ln(k): 18.215824782958304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_1R!H->O
Total Standard Deviation in ln(k): 18.215824782958304""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_1R!H->O
Total Standard Deviation in ln(k): 18.215824782958304
""",
)

entry(
    index = 12,
    label = "Root_Ext-5R!H-R_N-1R!H->O",
    kinetics = ArrheniusBM(A=(4.13276e+40,'s^-1'), n=-8.82706, w0=(968000,'J/mol'), E0=(198398,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.41831525179713547, var=127.90749284116275, Tref=1000.0, N=2, correlation='Root_Ext-5R!H-R_N-1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_N-1R!H->O
    Total Standard Deviation in ln(k): 23.723834234968486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_N-1R!H->O
Total Standard Deviation in ln(k): 23.723834234968486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_N-1R!H->O
Total Standard Deviation in ln(k): 23.723834234968486
""",
)

entry(
    index = 13,
    label = "Root_Ext-4R!H-R_1R!H->O",
    kinetics = ArrheniusBM(A=(9.86671e+06,'s^-1'), n=1.56749, w0=(1.183e+06,'J/mol'), E0=(173559,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017669080471101054, var=0.33083863833173466, Tref=1000.0, N=9, correlation='Root_Ext-4R!H-R_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O
    Total Standard Deviation in ln(k): 1.1974897084813658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O
Total Standard Deviation in ln(k): 1.1974897084813658""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O
Total Standard Deviation in ln(k): 1.1974897084813658
""",
)

entry(
    index = 14,
    label = "Root_Ext-4R!H-R_N-1R!H->O",
    kinetics = ArrheniusBM(A=(1.72895e+30,'s^-1'), n=-5.70034, w0=(968000,'J/mol'), E0=(195158,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2423246446776112, var=19.20035227257598, Tref=1000.0, N=4, correlation='Root_Ext-4R!H-R_N-1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O
    Total Standard Deviation in ln(k): 9.393245465651558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O
Total Standard Deviation in ln(k): 9.393245465651558""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O
Total Standard Deviation in ln(k): 9.393245465651558
""",
)

entry(
    index = 15,
    label = "Root_2R!H->C_1R!H->O",
    kinetics = ArrheniusBM(A=(2.24445e+09,'s^-1'), n=0.522783, w0=(1.16358e+06,'J/mol'), E0=(160104,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0815033601955616, var=23.53871194379916, Tref=1000.0, N=6, correlation='Root_2R!H->C_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O
    Total Standard Deviation in ln(k): 9.931097443018086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O
Total Standard Deviation in ln(k): 9.931097443018086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O
Total Standard Deviation in ln(k): 9.931097443018086
""",
)

entry(
    index = 16,
    label = "Root_2R!H->C_N-1R!H->O",
    kinetics = ArrheniusBM(A=(1.0177e+12,'s^-1'), n=-0.245873, w0=(968000,'J/mol'), E0=(182727,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_2R!H->C_N-1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_N-1R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_N-1R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-2R!H->C_2NOS->S",
    kinetics = ArrheniusBM(A=(1.43424e+08,'s^-1'), n=0.644242, w0=(953500,'J/mol'), E0=(106636,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-2R!H->C_2NOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-2R!H->C_2NOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-2R!H->C_N-2NOS->S",
    kinetics = ArrheniusBM(A=(5.03649e+09,'s^-1'), n=0.289241, w0=(1.0205e+06,'J/mol'), E0=(165640,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016015533849458193, var=0.027743929771675672, Tref=1000.0, N=2, correlation='Root_N-2R!H->C_N-2NOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S
    Total Standard Deviation in ln(k): 0.3741589167898476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 0.3741589167898476""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 0.3741589167898476
""",
)

entry(
    index = 19,
    label = "Root_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.56017e+12,'s^-1'), n=-0.119702, w0=(1.183e+06,'J/mol'), E0=(135771,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.82163e+08,'s^-1'), n=0.989298, w0=(1.183e+06,'J/mol'), E0=(138899,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9514830544978642, var=2.010530764035632, Tref=1000.0, N=2, correlation='Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 5.2332386811796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.2332386811796""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.2332386811796
""",
)

entry(
    index = 21,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R",
    kinetics = ArrheniusBM(A=(1.73802e+13,'s^-1'), n=-0.371068, w0=(1.183e+06,'J/mol'), E0=(156146,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3020733575836822, var=0.59095043896255, Tref=1000.0, N=7, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
    Total Standard Deviation in ln(k): 2.3000843134657973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
Total Standard Deviation in ln(k): 2.3000843134657973""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R
Total Standard Deviation in ln(k): 2.3000843134657973
""",
)

entry(
    index = 22,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.0988e+10,'s^-1'), n=0.632459, w0=(1.183e+06,'J/mol'), E0=(164532,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14086930923198027, var=0.05370774337580898, Tref=1000.0, N=3, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.8185389619247819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8185389619247819""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8185389619247819
""",
)

entry(
    index = 23,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.19613e+13,'s^-1'), n=-0.375547, w0=(1.183e+06,'J/mol'), E0=(152765,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_Ext-5R!H-R_1R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5279.23,'s^-1'), n=1.38734, w0=(938500,'J/mol'), E0=(119664,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-5R!H-R_1R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_1R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_1R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_1R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_Ext-5R!H-R_N-1R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.77467e+13,'s^-1'), n=-1.06001, w0=(968000,'J/mol'), E0=(89904,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-5R!H-R_N-1R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_N-1R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_N-1R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-5R!H-R_N-1R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_Ext-4R!H-R_1R!H->O_7R!H->O",
    kinetics = ArrheniusBM(A=(5.40789e+14,'s^-1'), n=-0.823434, w0=(1.183e+06,'J/mol'), E0=(200846,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008726972437150324, var=0.04557818763103101, Tref=1000.0, N=2, correlation='Root_Ext-4R!H-R_1R!H->O_7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_7R!H->O
    Total Standard Deviation in ln(k): 0.44991893248605175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_7R!H->O
Total Standard Deviation in ln(k): 0.44991893248605175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_7R!H->O
Total Standard Deviation in ln(k): 0.44991893248605175
""",
)

entry(
    index = 27,
    label = "Root_Ext-4R!H-R_1R!H->O_N-7R!H->O",
    kinetics = ArrheniusBM(A=(4.72908e+06,'s^-1'), n=1.66491, w0=(1.183e+06,'J/mol'), E0=(172562,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06209838620188961, var=0.15842678483127076, Tref=1000.0, N=7, correlation='Root_Ext-4R!H-R_1R!H->O_N-7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O
    Total Standard Deviation in ln(k): 0.9539680385815258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O
Total Standard Deviation in ln(k): 0.9539680385815258""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O
Total Standard Deviation in ln(k): 0.9539680385815258
""",
)

entry(
    index = 28,
    label = "Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(8.67997e+32,'s^-1'), n=-6.52321, w0=(968000,'J/mol'), E0=(192392,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.243442907479481, var=26.977901364434064, Tref=1000.0, N=3, correlation='Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.024310800072813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.024310800072813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.024310800072813
""",
)

entry(
    index = 29,
    label = "Root_2R!H->C_1R!H->O_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.02018e+11,'s^-1'), n=-0.0739297, w0=(1.183e+06,'J/mol'), E0=(160258,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0038766176496688475, var=47.42603160880866, Tref=1000.0, N=4, correlation='Root_2R!H->C_1R!H->O_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R
    Total Standard Deviation in ln(k): 13.815661203148398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.815661203148398""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.815661203148398
""",
)

entry(
    index = 30,
    label = "Root_2R!H->C_1R!H->O_5R!H->O",
    kinetics = ArrheniusBM(A=(1.95284e+06,'s^-1'), n=1.88752, w0=(1.183e+06,'J/mol'), E0=(168117,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_2R!H->C_1R!H->O_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_2R!H->C_1R!H->O_N-5R!H->O",
    kinetics = ArrheniusBM(A=(185531,'s^-1'), n=1.69565, w0=(1.0665e+06,'J/mol'), E0=(150436,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_2R!H->C_1R!H->O_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-2R!H->C_N-2NOS->S_2NO->O",
    kinetics = ArrheniusBM(A=(2.3921e+11,'s^-1'), n=-0.284346, w0=(1.0665e+06,'J/mol'), E0=(165328,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-2R!H->C_N-2NOS->S_2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-2R!H->C_N-2NOS->S_N-2NO->O",
    kinetics = ArrheniusBM(A=(1.00939e+08,'s^-1'), n=0.86916, w0=(974500,'J/mol'), E0=(165909,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_N-2R!H->C_N-2NOS->S_N-2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2R!H->C_N-2NOS->S_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.72964e+12,'s^-1'), n=-0.154553, w0=(1.183e+06,'J/mol'), E0=(129036,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.72501e+14,'s^-1'), n=-0.67985, w0=(1.183e+06,'J/mol'), E0=(156885,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14831052526099403, var=0.05092668287625909, Tref=1000.0, N=2, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.8250468940116295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8250468940116295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8250468940116295
""",
)

entry(
    index = 36,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.26982e+13,'s^-1'), n=-0.442684, w0=(1.183e+06,'J/mol'), E0=(141988,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008973802109952855, var=1.7601356034708961, Tref=1000.0, N=4, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.6822313187810094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.6822313187810094""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.6822313187810094
""",
)

entry(
    index = 37,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.41068e+13,'s^-1'), n=-0.43239, w0=(1.183e+06,'J/mol'), E0=(160784,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008055355569653555, var=0.1636224322977239, Tref=1000.0, N=2, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.8311603334693084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8311603334693084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8311603334693084
""",
)

entry(
    index = 38,
    label = "Root_Ext-4R!H-R_1R!H->O_7R!H->O_Ext-7O-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(5.41006e+14,'s^-1'), n=-0.823484, w0=(1.183e+06,'J/mol'), E0=(200218,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-4R!H-R_1R!H->O_7R!H->O_Ext-7O-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_7R!H->O_Ext-7O-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_7R!H->O_Ext-7O-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_7R!H->O_Ext-7O-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_7C-inRing",
    kinetics = ArrheniusBM(A=(1.18223e+12,'s^-1'), n=-0.0806669, w0=(1.183e+06,'J/mol'), E0=(164116,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing",
    kinetics = ArrheniusBM(A=(3.93467e+06,'s^-1'), n=1.69077, w0=(1.183e+06,'J/mol'), E0=(172691,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.047593991409819986, var=0.10410275539571957, Tref=1000.0, N=6, correlation='Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing
    Total Standard Deviation in ln(k): 0.766409835904944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing
Total Standard Deviation in ln(k): 0.766409835904944""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing
Total Standard Deviation in ln(k): 0.766409835904944
""",
)

entry(
    index = 41,
    label = "Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.0248e+36,'s^-1'), n=-7.48492, w0=(968000,'J/mol'), E0=(188130,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3572259686467468, var=77.35995211821744, Tref=1000.0, N=2, correlation='Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 18.53010112249282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 18.53010112249282""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 18.53010112249282
""",
)

entry(
    index = 42,
    label = "Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.72253e+12,'s^-1'), n=-0.0948638, w0=(1.183e+06,'J/mol'), E0=(172576,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0053888222478077645, var=0.5959934434744609, Tref=1000.0, N=3, correlation='Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 1.5612074955319186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5612074955319186""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5612074955319186
""",
)

entry(
    index = 43,
    label = "Root_2R!H->C_1R!H->O_Ext-3R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(981181,'s^-1'), n=-0.141465, w0=(1.183e+06,'J/mol'), E0=(124049,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_2R!H->C_1R!H->O_Ext-3R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing",
    kinetics = ArrheniusBM(A=(1.75623e+14,'s^-1'), n=-0.68222, w0=(1.183e+06,'J/mol'), E0=(156891,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing",
    kinetics = ArrheniusBM(A=(7.16993e+12,'s^-1'), n=-0.258319, w0=(1.183e+06,'J/mol'), E0=(155989,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.01133e+12,'s^-1'), n=-0.317664, w0=(1.183e+06,'J/mol'), E0=(115676,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(5.77584e+12,'s^-1'), n=-0.330794, w0=(1.183e+06,'J/mol'), E0=(148158,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.84721e+12,'s^-1'), n=-0.302094, w0=(1.183e+06,'J/mol'), E0=(150154,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006801173647055783, var=0.016504986209969107, Tref=1000.0, N=2, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.2746401658299856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2746401658299856""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2746401658299856
""",
)

entry(
    index = 49,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(4.04251e+12,'s^-1'), n=-0.258404, w0=(1.183e+06,'J/mol'), E0=(154724,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(7.65417e+13,'s^-1'), n=-0.52566, w0=(1.183e+06,'J/mol'), E0=(166257,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R",
    kinetics = ArrheniusBM(A=(139248,'s^-1'), n=2.06526, w0=(1.183e+06,'J/mol'), E0=(165686,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6647699906393877, var=1.1672292739411867, Tref=1000.0, N=4, correlation='Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R
    Total Standard Deviation in ln(k): 3.836159769370438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.836159769370438""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.836159769370438
""",
)

entry(
    index = 52,
    label = "Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.0786e+07,'s^-1'), n=1.38493, w0=(1.183e+06,'J/mol'), E0=(180119,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(7.30892e+12,'s^-1'), n=-0.913499, w0=(968000,'J/mol'), E0=(92814.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_N-1R!H->O_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(6.26347e+11,'s^-1'), n=0.219786, w0=(1.183e+06,'J/mol'), E0=(170925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0058163353471268765, var=2.1167643769249636, Tref=1000.0, N=2, correlation='Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 2.931323893522042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.931323893522042""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.931323893522042
""",
)

entry(
    index = 55,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing",
    kinetics = ArrheniusBM(A=(8.29948e+12,'s^-1'), n=-0.271204, w0=(1.183e+06,'J/mol'), E0=(151786,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing",
    kinetics = ArrheniusBM(A=(8.55485e+12,'s^-1'), n=-0.320523, w0=(1.183e+06,'J/mol'), E0=(148430,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.43227e+13,'s^-1'), n=-0.435883, w0=(1.183e+06,'J/mol'), E0=(171149,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.42317e+12,'s^-1'), n=-0.355627, w0=(1.183e+06,'J/mol'), E0=(168309,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.07376e+12,'s^-1'), n=-0.349886, w0=(1.183e+06,'J/mol'), E0=(167015,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R!H-R_1R!H->O_N-7R!H->O_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.08466e+14,'s^-1'), n=-0.414807, w0=(1.183e+06,'J/mol'), E0=(173074,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, correlation='Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2R!H->C_1R!H->O_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

