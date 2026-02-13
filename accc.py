# Python program to conduct AC contingency calculation
psspy.case(r"""savnw.sav""")
psspy.fdns([0,1,0,0,0,0,99,0])
psspy.dfax_2([1,1,0],r"""savnw.sub""",r"""savnw.mon""",r"""savnw.con""",r"""savnw.dfx""")
psspy.accc_with_dsp_3(0.1,[0,0,0,0,1,2,0,0,0,2,0],r"""CON""",r"""savnw.dfx""",r"""savnw.acc""","","","")
