import wave # this is the wave.py file in the local folder
import matplotlib.pyplot as plt
# np.set_printoptions(threshold=np.nan) # show full arrays, dataframes, etc. when printing

class Signal(object):
    """
    An ECG/EKG signal

    Attributes:
        name: A string representing the record name.
        data : 1-dimensional array with input signal data 
    """

    def __init__(self, name, data):
        """Return a Signal object whose record name is *name*,
        signal data is *data*,
        R peaks array of coordinates [(x1,y1), (x2, y2),..., (xn, yn)]  is *RPeaks*"""
        self.name = name
        self.data = data
        
        RPeaks = wave.getRPeaks(data, 150)
        self.RPeaks = RPeaks[1]
        self.inverted = RPeaks[0]
        if self.inverted: # flip the inverted signal
            self.data = -data
        
        Pwaves = wave.getPWaves(self)
        self.PPintervals = Pwaves[0]
        self.Ppeaks = Pwaves[1]
        
        self.baseline = wave.getBaseline(self)
        
        #RR interval
        self.RRintervals = wave.RR_interval(self.RPeaks)
        #self.RRintervals_bin = wave.RR_intervals
        
        #noise features:
        #self.
        baseline = wave.getBaseline(self)
        self.baseline = baseline[0]
        self.RRIntervalMeanStd = baseline[1] # Standard deviation of all RR interval means
            
    def plotRPeaks(self):
        fig = plt.figure(figsize=(9.7, 6)) # I used figures to customize size
        ax = fig.add_subplot(111)
        ax.plot(self.data)
        # ax.axhline(self.baseline)
        ax.plot(*zip(*self.RPeaks), marker='o', color='r', ls='')
        ax.set_title(self.name)
        plt.show()
        
        
    # TODO: add error handling for crazy cases of data i.e. A04244, A00057
    # Wrap the whole thing in a try catch, assign as AF if there's an error
    # Set everything to N in the beginning
    
    # TODO: Write bash scrip including pip install for pywavelets

# Imperatively grabbing features
#data = wave.load('A00057')
#signal = Signal('A00057', data)
#signal.plotRPeaks()


records = wave.getRecords('N') # N O A ~
#data = wave.load(records[7])
#sig = Signal(records[7],data)
#
#sig.plotRPeaks()
#
#wave.getQS(sig)

#RR interval stuff
#error_list = []
#for i in records:    
filename = 'A06495'
try:
    data = wave.load(filename)
    print ('working on Record:' + filename)
    sig = Signal(filename,data)
    
    sig.plotRPeaks()
    wave.plot(sig.data[2000:4000])
       
    
except:
    print ('stupid EKG found: ')
        
        

#records = wave.getRecords('A') # N O A ~
#data = wave.load(records[7])
#sig = Signal(records[7],data)

#sig.plotRPeaks()



