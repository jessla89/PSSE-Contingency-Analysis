
def otdf_csv(savfile='savnw.sav', dfxfile='savnw.dfx', csvfile = 'savnw.csv'):

    import psspy
    import pssarrays
    
    psspy.psseinit()
    psspy.case(savfile)
    
    rlst = pssarrays.otdf_factors(dfxfile)
    csvfile_h = open(csvfile,'w')
    report    = csvfile_h.write
    
    element = 'Element,'+', '.join(rlst.melement)
    report(element)
    report('\n')
    
    colabel_list = rlst.colabel
    for test_colabel in colabel_list:   
        report('\n')
        index_colabel = colabel_list.index(test_colabel)
        list_odtf = [str(i) for i in rlst.factor[index_colabel]]
        otdf = test_colabel + ',' + ', '.join(list_odtf)
        report(otdf)
        report('\n')
    csvfile_h.close()
    print('Done')
if __name__ == '__main__':

    import psse35

    otdf_csv()
