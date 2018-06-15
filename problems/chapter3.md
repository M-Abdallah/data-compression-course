---
layout: mathPage
title: Chapter 3 Solution
author: Mohamed Abdallah
---
# Huffman Coding

1. Design each of the following codes, and then calculate its average coding length, and redundancy, per symbol.

    > Solution

    - A minimum variance Huffman code for the alphabet {A, B, C, D}, with probabilities, 0.1, 0.2, 0.3, & 0.4, respectively.

    | Min-Var Huffman |
    | Symbol | Code   |
    |   A   |   001   |
    |   B   |   000   |
    |   C   |   01    |
    |   D   |   1     |
    |L_Average | 1.9 bits/s |
    | Redundancy | 0.054 bit/s|

    - Huffman

    |   Huffman |
    | Symbol | Code   |
    |   A   |   011   |
    |   B   |   010   |
    |   C   |   00    |
    |   D   |   1     |
    |L_Average | 1.9 bits/s |
    | Redundancy | 0.054 bit/s|

    - A minimum variance extended Huffman code for the binary alphabet {0, 1},with probabilities 0.1 and 0.9, respectively. Generate a code word for every block of 3 symbols.

    | Extended Huffman    |
    | Symbol | Code       |
    |   000   |   11111   |
    |   001   |   11110   |
    |   010   |   11101   |
    |   011   |   110     |
    |   100   |   11100   |
    |   101   |   101     |
    |   110   |   100     |
    |   111   |   0       |
    |L_Average | 0.5325 bits/s |
    | Redundancy | 0.0635 bit/s|

    - A 3-bit Tunstall code for the above binary alphabet.

    | Tunstall Code   |
    | Symbol | Code   |
    |   0   |   000   |
    |   10   |   001   |
    |   110  |   010    |
    |   1110   |   011     |
    |   11110   |   100   |
    |   111110   |   101   |
    |   1111110   |   110    |
    |   11111110   |   111    |
    |L_Average | 0.8673 bits/s |
    | Redundancy | 0.398 bit/s|

2. An alphabet is composed of the 6 symbols {A, C, N, T, Y, Δ}. Design a minimum length code
for the alphabet. Assign short codes for small index symbols. Use this code as a starting code
during next problems.
    > Solution 

    | Symbol | Code   |
    |   A   |   00    |
    |   C   |   01    |
    |   N   |   100   |
    |   T   |   101   |
    |   Y   |   110   |
    |   #   |   111   |

    <div class="mermaid">
        graph TB
            0((#0))-- 0 -->1((#0))
            0-- 1 -->2((#1))
            2-- 0 -->3((#10))
            2-- 1 -->4((#11))
            subgraph 0
            1-- 0 -->A
            1-- 1 -->C
            end
            subgraph 10
            3-- 0 -->N
            3-- 1 -->T
            end
            subgraph 11
            4-- 0 -->Y
            4-- 1 -->#
            end
    </div>

3. Using adaptive Huffman coding,

    > Solution

    - code the following: “ACACTAN”. Show the development of the coding tree, and the code generated for each symbol

    |Apaptive Huffman  | Symbol | A   | C   | A | C  | T    | A   | N |
    |                  |---------------------------------------------------  
    |                  |Code    |0,00 |0,01 |1  | 01 |00,101| 0   |100,100 |

    - Decode the first 5 symbols of the same alphabet, form the stream“0111011001011001101100001111011000101001100011010101”

    |Apaptive Huffman  | Symbol | $\delta$ | Y   | Y | $\delta$  |  Y   |
    |                  |---------------------------------------------------  
    |                  |Code    |0,111     |0,110| 01| 0         |11  |


4. Use the Golomb code, with m=2, to code the above sequence.

    > Solution

    |Golomb Code       | Symbol | A   | C   | A | C  | T    | A   | N |
    |                  |---------------------------------------------------  
    |                  |Code    |00   | 01  | 00| 01 |101   | 00  |100 |

    |Move to front     | Symbol | A   | C   | A | C  | T    | A   | N |
    |                  |---------------------------------------------------  
    |                  |Code    | 0   | 1  | 1 | 1   | 3    | 2     | 3 |

5. Code the number 6. First, use Golomb code with m=3. Next use Recursive indexing, with a representation alphabet of size 3. Use variable length code for entropy coding, with smaller numbers having short length. Draw the VLC tree. Label different parts of each code.

    > Solution

    | | Golomb Code | Recursive Indexing |
    ------------------------------------
    | Code         | 1100   | 1111110   |
