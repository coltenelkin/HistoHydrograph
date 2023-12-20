import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

def HistoHydrograph(xArray, yArray, **kwargs):
    ### function HISTOHYDROGRAPH creates an hydrograph attached to a histogram of the data.
    # the inputs are:
    # an x array size n x 1 or 1 x n. Generally dates but any array will do
    # a y array also size n x 1 or 1 x n. Generally stage or discharge, but any positive array will work
    # OPTIONAL: 
        # yarray2: a second y array that will graph on a secondary axis. Must also be positive. Note that yarray2 should have the same size as arrays x and y
        # color: color for the plotted data
        # color2: color for second y array item. Ignored if no y array 2 is passed
        # label: label for a legend
        # label2: label for secondary y axis item. Ignored if no y array 2 is passed
        # xlabel: label for the x axis
        # ylabel: label for the y axis
        # ylabel2: label for secondary y axis if a second axis is included. Ignored if no yarray2 is passed
        # bins: either a scalar number of bins or an array of bins to use for the histogram. Default is 30
        # bins2: same as bins, but for a secondary y array
        # density: true if you want the histogram to show relative density as opposed to count. Do not resize the figure if you use TRUE
        # legendloc: [l1, l2] array with the legend location within the figure. l1, l2 values between 0 and 1. 
    
    # Final note: dependencies include numpy as np, matplotlib, pyplot (as plt), and time
    x = xArray
    y = yArray
    for key, value in kwargs.items():
        if key.lower() == 'yarray2':
            y2 = value
            
        if key.lower() == 'label':
            label = value

        if key.lower() == 'label2':
            label2 = value
            
        if key.lower() == 'xlabel':
            xlabel = value

        if key.lower() == 'ylabel':
            ylabel = value

        if key.lower() == 'ylabel2':
            ylabel2 = value

        if key.lower() == 'density':
            density = value

        if key.lower() == 'bins':
            bins = value

        if key.lower() == 'bins2':
            bins2 = value

        if key.lower() == 'color':
            color = value

        if key.lower() == 'color2':
            color2 = value

        if key.lower() == 'legendloc':
            legendloc = value

    if 'label' not in locals():
        label = '__nolabel__'
    if 'label2' not in locals():
        label2 = '__nolabel__'
    if 'xlabel' not in locals():
        xlabel = None
    if 'ylabel' not in locals():
        ylabel = None
    if 'ylabel2' not in locals():
        ylabel2 = None
    if 'density' not in locals():
        density = False
    if 'bins' not in locals():
        bins = 30
    if 'bins2' not in locals():
        if hasattr(bins, "__len__"):
            bins2 = 30
        else:
            bins2 = bins
    if 'color' not in locals():
        color = 'tab:blue'
    if 'color2' not in locals():
        color2 = 'tab:orange'
    if 'legendloc' not in locals():
        legendloc = [.7, .7]
        

    if 'y2' in locals():
        if len(x) != len(y) or len(x) != len(y2): 
            print('Note that x, y, and y2 arrays are not the same length.\nTrimming to match the shorter array...')
            time.sleep(1)
            minlen = min([len(x), len(y), len(y2)])
            x = x[:minlen]
            y = y[:minlen]
            y2 = y2[:minlen]
        
        # initialize figure
        fig, (a0, ax) = plt.subplots(1, 2, width_ratios = [5, 2], sharey = True)
        fig.set_figwidth(10)
        fig.subplots_adjust(wspace=0.002)
        

        # left plot, drawing y array 1
        a0.plot(x, y, label = label, color = color)
        a0.tick_params(axis="y",direction="in", length = 10, color = 'k', width = 1)
        a0.set_ylabel(ylabel)
        a0.set_xlabel(xlabel)
        ylims = a0.get_ylim()

        # right plot, drawing y array 1
        hist = ax.hist(y, bins = bins, orientation = 'horizontal', density = density, color = color)
        ax.tick_params(axis="y",direction="inout", length = 20, color = 'k', width = 1)
        if density: # if density is on, we need to correct for the bin width. This is why you shouldn't adjust size when density is turned on.
            corrFactor = hist[1][1] - hist[1][0]
            xticklabels = ax.get_xticklabels()
            newlabels = []
            for xticklabel in xticklabels:
                num = float(xticklabel.get_text())
                newlabel = round(num * corrFactor * 100) / 100
                newlabels = np.append(newlabels, newlabel)
            ax.set_xticklabels(newlabels)
            ax.set_xlabel('Relative Density')
        else:
            ax.set_xlabel('Count, n = '+str(int(hist[0].sum())))
        ax.set_ylim(ylims)
        

        # left plot drawing y array 2
        a02 = a0.twinx()
        a02.plot(x, y2, color = color2, label = label2, alpha = 0.6)
        a02.tick_params(axis="y",direction="inout", width = 2, color = 'b', length = 12)
        a02.set_yticklabels([])
        fig.subplots_adjust(wspace=0)
        
        # right plot drawing y array 2
        ax2 = ax.twinx()
        flowHist = ax2.hist(flow, orientation = 'horizontal', bins = bins2, color = color2, alpha = 0.6)
        ax2.set_ylabel('Discharge [cfs]')
        ax2.set_ylim([fmin, fmax])
        ax2.tick_params(axis="y", color = 'b', width = 2, length = 6)

    
        if label != '__nolabel__' or label2 != '__nolabel__':
            fig.legend(loc=legendloc)





    # single y-array
    else:
        if len(x) != len(y): 
            print('Note that x and y arrays are not the same length.\nTrimming to match the shorter array...')
            time.sleep(1)
            if len(x) > len(y):
                x = x[:len(y)]
            else:
                y = y[:len(x)]
        
        # initialize figure
        fig, (a0, ax) = plt.subplots(1, 2, width_ratios = [5, 2], sharey = True)
        fig.set_figwidth(10)
        fig.subplots_adjust(wspace=0)

        # left plot drawing
        a0.plot(x, y, label = label, color = color)
        a0.tick_params(axis="y",direction="in", length = 10, color = 'k', width = 1)
        a0.set_ylabel(ylabel)
        a0.set_xlabel(xlabel)
        ylims = a0.get_ylim()
        
        # right plot drawing
        hist = ax.hist(y, bins = bins, orientation = 'horizontal', density = density, color = color)
        ax.tick_params(axis="y",direction="inout", length = 20, color = 'k', width = 1)
        if density: # if density is on, we need to correct for the bin width. This is why you shouldn't adjust size when density is turned on.
            corrFactor = hist[1][1] - hist[1][0]
            xticklabels = ax.get_xticklabels()
            newlabels = []
            for xticklabel in xticklabels:
                num = float(xticklabel.get_text())
                newlabel = round(num * corrFactor * 100) / 100
                newlabels = np.append(newlabels, newlabel)
            ax.set_xticklabels(newlabels)
            ax.set_xlabel('Relative Density')
        else:
            ax.set_xlabel('Count, n = '+str(int(hist[0].sum())))
        ax.set_ylim(ylims)

        if label != '__nolabel__':
            fig.legend(loc=legendloc)
        
                

HistoHydrograph(dates, stage, yarray2 = flow, 
                bins = 100,
                color = [0.2, 0.7, 0.2], color2 = 'k',
                label = 'Stage at 435.47 RL', label2 = 'Discharge at\nSwan Falls Dam')