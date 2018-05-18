from  arithmaticUtilties import *
import numpy as np



class arithmaticDecoder:
    
    def __init__( self, seq, m, letters, cumCount ):
        self.sequence = seq
        self.uLimit = 2**m -1
        self.lLimit = 0
        self.m = m
        self.scale = 2**m
        self.letters = letters
        self.cdf = cumCount
        self.shiftIter = 0
        self.decoded = []
        self.tagBin = self.sequence[0:self.shiftIter+self.m]
        self.tagDec = np.packbits( self.tagBin )[0]
        self.tag = tagValue( self.tagDec, self.lLimit, self.uLimit, self.cdf.max() )
        
    def decode(self):
        
        def updateTag(self):
            self.tagDec = np.packbits( self.tagBin )[0]    
            self.tag = tagValue( self.tagDec, self.lLimit, self.uLimit, self.cdf.max() )

        def tagShift(self):
            if (self.shiftIter <= len(self.sequence)-self.m):
                self.shiftIter+=1
                self.tagBin = self.sequence[self.shiftIter:self.shiftIter+self.m]
                updateTag(self)

        def scale123():
            if (self.shiftIter <= len(self.sequence)-self.m):
            # Check for E1
                if ( self.lLimit < self.scale/2 and self.uLimit < self.scale/2 ):
                    print('E1')
                    # Change the limits (Scaling)
                    self.uLimit , self.lLimit = e1Edit( self.uLimit, self.lLimit )
                    print(self.uLimit , self.lLimit)
                    tagShift(self)
                    scale123()
                # Check for E2
                elif ( self.lLimit >= self.scale/2  and self.uLimit >= self.scale/2 ):
                    print('E2')
                    # Change the limits (Scaling)
                    self.uLimit , self.lLimit = e2Edit( self.uLimit, self.lLimit, self.scale )
                    print(self.uLimit , self.lLimit)
                    tagShift(self)
                    scale123()
                # Check for E3
                elif ( self.lLimit >= self.scale/4  and self.uLimit < 3*self.scale/4 ):
                    print('E3')
                    # Change the limits (Scaling)
                    self.uLimit , self.lLimit = e3Edit( self.uLimit, self.lLimit, self.scale )
                    print(self.uLimit , self.lLimit)
                    tagShift(self)
                    self.tagBin[0] = np.abs( self.tagBin[0]-1 )
                    updateTag(self)
                    print( self.tagBin,self.tagDec ,self.tag )
                    
                    scale123()
        
        while(self.shiftIter <= len(self.sequence)-self.m and len(self.decoded)< self.cdf.max()):
            self.tag = tagValue( self.tagDec, self.lLimit, self.uLimit, self.cdf.max() )
            idx = np.argwhere( self.cdf <= self.tag ).argmax()
            self.decoded.append( self.letters[idx] )
            print( self.decoded )
            self.lLimit, self.uLimit = luEdit( self.uLimit, self.lLimit, self.cdf[idx], self.cdf[idx+1], self.cdf.max() )
            print(self.uLimit , self.lLimit)
            scale123()
        
        return self.decoded
