# Python program to export PSSE accc contingency solution in excel format
import pssexcel
pssexcel.accc('savnw.acc', ['s','v','b'], colabel='',stype='contingency', busmsm=0.5, sysmsm=5.0,
                       rating='a', namesplit=False,xlsfile='savnwacc.xlsx', sheet='', overwritesheet=True, show=False, ratecon='b',
                       baseflowvio=False,basevoltvio=False, flowlimit=100.0, flowchange=0.0, voltchange=0.0,swdrating='a',
                       swdratecon='b',baseswdflowvio=False,basenodevoltvio=False,overloadreport=True)