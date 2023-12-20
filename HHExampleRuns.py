# example runs showing different functionality of HistoHydrograph.py
# Can run through the command terminal or in an IDE of your choice
# if using the command line, copy be sure to copy the code and csvs into a common directory, then...
# ... call $python HHExampleRuns.py 1 (for standard histohydrograph)
# ... call $python HHExampleRuns.py 2 (for histohydrograph showing stage on secondary y-axis)
# ... call $python HHExampleRuns.py 3 (for histohydrograph of two rivers on the same plot)


import sys
import numpy as np
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import time
from HistoHydrograph import HistoHydrograph

virgin = pd.read_csv("USGS_VirginRiverAtSpringdale.csv", parse_dates = ['Date']) # read in csvs
stjoe = pd.read_csv("USGS_StJoeRiverAtSouthBend.csv", parse_dates = ['Date'])

vf = virgin['discharge, cfs'] # virgin river flow column
vs = virgin['gage height, ft'] # stage
vd = virgin.Date # and dates

jf = stjoe['discharge, cfs'] # st joe flow

if __name__ == '__main__':
    if sys.argv[1] == "1": # example with simple hydrograph
        HistoHydrograph(vd, vf, label = 'Virgin River\nat Springdale, UT', xlabel = 'Date', \
                        ylabel = 'Discharge [cfs]', bins = 500, color = 'k')

    if sys.argv[1] == "2": # add stage data
        HistoHydrograph(vd, vf, yarray2 = vs, label = 'Discharge, Virgin River\nat Springdale, UT', \
                        label2 = 'Stage', xlabel = 'Date', ylabel = 'Discharge [cfs]', \
                        ylabel2 = 'Stage [ft]', bins = 100)

    if sys.argv[1] == "3": # compare two discharges
        HistoHydrograph(vd, vf, yarray2 = jf, label = 'Discharge, Virgin River\nat Springdale, UT', \
                        label2 = 'Discharge, St. Joe River\nat South Bend, IN', xlabel = 'Date', \
                        ylabel = 'Virgin River Discharge [cfs]', ylabel2 = 'St Joe River Discharge [cfs]', 
                        bins = 100, bins2 = 30, legendloc = [0.3, 0.7])

else:
    # example 1: just the histohydrograph
    HistoHydrograph(vd, vf, label = 'Virgin River\nat Springdale, UT', xlabel = 'Date', \
                    ylabel = 'Discharge [cfs]', bins = 500, color = 'k')

    # example 2: add stage
    HistoHydrograph(vd, vf, yarray2 = vs, label = 'Discharge, Virgin River\nat Springdale, UT', \
                    label2 = 'Stage', xlabel = 'Date', ylabel = 'Discharge [cfs]', \
                    ylabel2 = 'Stage [ft]', bins = 100)

    # example 3: compare to a second river
    HistoHydrograph(vd, vf, yarray2 = jf, label = 'Discharge, Virgin River\nat Springdale, UT', \
                    label2 = 'Discharge, St. Joe River\nat South Bend, IN', xlabel = 'Date', \
                    ylabel = 'Virgin River Discharge [cfs]', ylabel2 = 'St Joe River Discharge [cfs]', 
                    bins = 100, bins2 = 30, legendloc = [0.3, 0.7])

