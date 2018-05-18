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
def e1Edit ( u, l ): 
    return int(u*2 +1) , int(l*2)
# lower and upper E2 scaling
def e2Edit(u, l, scale):
    return int( 2*u - scale + 1 ), int( 2*l - scale )
# lower and upper E3 scaling
def e3Edit(u, l, scale):
    return int( 2*u - scale/2 +1 ), int( 2*l - scale/2 )


def tagValue(t, l, u, tC):
    return np.floor( ((t-l+1)*tC-1)/(u-l+1) ) 