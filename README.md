This little function was inspired by a figure in a presentation in one of the ESPS talks at AGU's Fall 2023 meeting. It reads in a timeseries of river flow data (doens't have to be a hydrograph; any two arrays of the same length will do) and produces a plot connected to a horizontal histogram of the data. It is capable of handling up to two y-axis arrays (see the examples below).
Hydrograph only:
![Discharge](https://github.com/coltenelkin/HistoHydrograph/assets/55114059/9674b9df-24e6-47fd-84ad-592c7b8e5b3b)

Hydrograph and Stage.
![DischargeAndStage](https://github.com/coltenelkin/HistoHydrograph/assets/55114059/b6b88635-9935-4d40-bae7-bb319420fe62)


See the HHExampleRuns.py script to create your own example figures. You can either open it in an IDE or download the scripts and data to a directory, open the command terminal, navigate to the directory, and call 
$python HHExampleRuns.py * 
where the * is either 1, 2, or 3 (depending on which figure you'd like to create).
