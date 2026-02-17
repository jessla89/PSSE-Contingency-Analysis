
def otdf_csv(savfile='savnw.sav', dfxfile='savnw.dfx',accfile = 'savnw.acc',csvfile = 'savnw.csv'):

    import psspy, arrbox.dfax_pp
    import pssarrays
  

    psspy.psseinit()

    psspy.case(savfile)

    rlst = pssarrays.otdf_factors(dfxfile)

 
    csvfile_h = open(csvfile,'w')
    report    = csvfile_h.write
    element = 'Element,'+ 'Result Observed,'+', '.join(rlst.melement)
    
    report(element)
    report('\n')
    colabel_list = rlst.colabel
    

    for test_colabel in colabel_list:
        stype = 'contingency'
        busmsm = 0.5
        sysmsm = 5.0
        
        rlstacc = pssarrays.accc_solution(accfile, test_colabel, stype, busmsm, sysmsm)
        report('\n')
        index_colabel = colabel_list.index(test_colabel)
        list_mvaflow = [str(i) for i in rlstacc.mvaflow]
        
        list_ampflow = [str(i) for i in rlstacc.ampflow]
       
        report('\n')
        mva = test_colabel + ',' +'MVA FLOW'+','+', '.join(list_mvaflow)
        report(mva)
        report('\n')
        amp = test_colabel + ',' +'AMP FLOW'+','+', '.join(list_ampflow)
        report(amp)
        report('\n')
        list_odtf = [str(i) for i in rlst.factor[index_colabel]]
       
        otdf = test_colabel + ',' +'OTDF FACTOR'+','+ ', '.join(list_odtf)
        report(otdf)
        report('\n')
        
        rlstsum = pssarrays.accc_summary(accfile)
        list_rating = [str(i) for i in rlstsum.rating.b]
        rating = test_colabel +',' + 'Rating' +','+', '.join(list_rating)
        report(rating)
        report('\n')

    csvfile_h.close()
    print('Done')
if __name__ == '__main__':

    import psse35
    otdf_csv()