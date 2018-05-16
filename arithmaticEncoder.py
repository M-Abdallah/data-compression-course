import numpy as np
from collections import Counter

def seqCDF( sequence ):
    """[summary]
    
    Arguments:
        sequence {[str]} -- [description]
    
    Returns:
        [numpy.array] -- [tuple items and frequency]
    """
    array = np.array(Counter(sequence).most_common())
    # Finds the items in thee sequence
    letter = array[:,0]
    # Counts the frequency of the items in the sequence
    counts = np.array(array[:,1], dtype=int)
    # Cumulative density function
    cdf = np.append(0,counts.cumsum())
    
    return letter, cdf

# lowerEdit = lambda u , l, c, tC: int(l + np.floor( ( u - l +1 ) * c/tC ))
# upperEdit = lambda u , l, c, tC: int(l + np.floor( ( u - l +1 ) * c/tC ) - 1)

# luEdit = lambda u,l,c,cN,tC: (int(l + np.floor( ( u - l +1 ) * c/tC ))), (int(l + np.floor( ( u - l +1 ) * cN/tC ) - 1))
def luEdit( u,l,c,cN,tC ):
    """[summary]
    
    Arguments:
        u {[integer]} -- [upper limit]
        l {[integer]} -- [lower limit]
        c {[integer]} -- [previous cumulative count]
        cN {[integer]} -- [present cumulative count]
        tC {[integer]} -- [total count]
    
    Returns:
        [tuple] -- [new lower, new upper]
    """

    return (int(l + np.floor( ( u - l +1 ) * c/tC ))), (int(l + np.floor( ( u - l +1 ) * cN/tC ) - 1))
    
# lower and upper E1 scaling
e1Edit = lambda u, l: ( int(u*2 +1) , int(l*2) )
# lower and upper E2 scaling
e2Edit = lambda u, l, scale: ( int( 2*u - scale + 1 ), int( 2*l - scale ) )
# lower and upper E3 scaling
e3Edit = lambda u, l, scale: ( int( 2*u - scale/2 +1 ), int( 2*l - scale/2 ) )


class arrithmaticEncode:
    
    def __init__(self, seq):
        self.uLimit = 255
        self.lLimit = 0
        self.e3Count = 0
        self.code = []
        self.sequence = seq
        # self.letters, self.cdf = seqCDF(self.sequence)
        self.letters = np.array([ 'a','b','c' ])
        self.cdf = np.array([0,40,41,50])
        # Total count
        self.totalC = self.cdf.max()
        # # of bits
        self.m = 2 + np.ceil( np.log2(self.totalC) )
        # Word size
        self.scale = 2**(self.m)
        

    def encode(self):
        def scale123():
            # Check for E1
            if ( self.lLimit < self.scale/2 and self.uLimit < self.scale/2 ):
                print( 'E1' )
                # Send 0
                self.code.append(0)
                print(self.code)
                # Change the limits (Scaling)
                self.uLimit , self.lLimit = e1Edit( self.uLimit, self.lLimit )
                print( self.lLimit, self.uLimit )
                # Check for previous E3
                while (self.e3Count > 0):
                    self.code.append(1)
                    self.e3Count-=1
                # Check again
                scale123()
            # Check for E2
            elif ( self.lLimit >= self.scale/2  and self.uLimit >= self.scale/2 ):
                print( 'E2' )
                # Send 1
                self.code.append(1)
                print(self.code)
                # Change the limits ( Scaling) 
                self.uLimit , self.lLimit = e2Edit( self.uLimit, self.lLimit, self.scale )                
                print( self.lLimit, self.uLimit )
                # Check for previous E3
                while( self.e3Count > 0 ):
                    self.code.append(0)
                    print(self.code)
                    self.e3Count-=1
                # Check again
                scale123()
            # Check for E3
            elif ( self.lLimit >= self.scale/4  and self.uLimit < 3*self.scale/4 ):
                print( 'E3' )
                # Increment E3Count 
                self.e3Count +=1
                # Change limits (scaling)
                self.uLimit, self.lLimit = e3Edit( self.uLimit, self.lLimit, self.scale )
                print( self.lLimit, self.uLimit )
                # Check again
                scale123()
                
        
        for item in self.sequence:
            idx = list(self.letters).index(item)
            print(item)
            print(self.cdf[idx], self.cdf[idx+1])
            # Change the limit based on the element
            self.lLimit, self.uLimit = luEdit( self.uLimit, self.lLimit, self.cdf[idx], self.cdf[idx+1], self.totalC )
            # self.lLimit = lowerEdit( self.uLimit, self.lLimit, self.cdf[idx], self.totalC )
            # self.uLimit = upperEdit( self.uLimit, self.lLimit, self.cdf[idx+1], self.totalC )
            print( self.lLimit, self.uLimit )
            # Check for scaling
            scale123()
        
        # Send the first bit of the lower limit
        self.code.append( list(np.unpackbits( np.array([self.lLimit], dtype=np.uint8) ))[0] )
        print(self.code)
        # Check if the E3 count is more than 0, to send E3Count*ones
        while (self.e3Count > 0):
            self.code.append(1)
            print(self.code)
            self.e3Count-=1
        
        print(self.lLimit)
        # Send the rest of the lower limit
        for i in list(np.unpackbits( np.array([self.lLimit], dtype=np.uint8) )): self.code.append(i)
        print(self.code)
        
        return( self.code )