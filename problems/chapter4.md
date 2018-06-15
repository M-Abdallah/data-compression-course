---
layout: mathPage
title: Chapter 4 Solution
author: Mohamed Abdallah
---
# Arithmetic Coding

1. 
    | Symbols | A | C | G |
   |Count | 9 | 2 | 17 | 
   
   What is the word length required for a digital arithmetic encoder to unambiguously encode the
above symbols?

    > Solution
    - Wordlength = 6 bits

2. Calculate the cumulative count and the total count for the above symbols.

    > Solution

    | Symbols | A | C | G || Total Count |
   |Count | 9 | 11 | 28 || 28 | 

3. Using a word length of 8 bits, encode the symbols “CACG”. Use the table given below to report your results. Give l and u in binary form. Use E to identify the scale operation. Assume the given initial l & u values, and initial scale3 = 4.

    > Solution

    | Step | Symbol | L | U | E(scale) | scale 3 | code |
    |-------|---------|--|--|------------|--------|------|
    | n-1  | - | 00111111 | 11000001 | - | 4 | - |
    | n   | C | 01101001 | 01110011 | E1 | 0 | 01111 |
    | n+1 | - | 11010010 | 11100111 | E2 | 0 | 011111 |
    | n+2 | - | 10100100 | 11001111 | E2 | 0 | 0111111 |
    | n+3 | - | 01001000 | 10011111 | E3 | 1 | - |
    | n+4 | - | 00010000 | 10111111 | - | 1 | - |
    | n+5 | A | 00100000 | 01001000 | E1 | 0 | 011111101 |
    | n+6 | - | 00100000 | 10010001 | - | 0 | - |
    | n+7 | C | 01000100 | 01001101 | E1 | 0 | 0111111010 |
    | n+8 | - | 10001000 | 10011011 | E2 | 0 | 01111110101 |
    | n+9 | - | 00010000 | 00110111 | 2E1 | 0 |0111111010100 |
    | n+10 | - | 01000000 | 11011111 | - | 0 | - |
    | n+11 | G | 01111110 | 11011111 | - | 0 | - |

4. Using a word length of 8 bits, decode the first 5 symbols of the stream “0111000100000111110010000001111001010101001010010101”. Use the table given below to report your results. Give l and u in binary form. Use E to identify the scale operation. Assume the given initial l & u values, and initial scale3 = 4.

    > Solution

    | Step | Symbol | L | U | Tag | E(Scale) | scale3 |
    |------|--------|---|--|-------|----------|--------|
    |n-1|-|00111111|11000001|01110001|-|4|
    |n |C|01101001|01110010|1|0|
    |n+1|-|11010010|11100101|11100010|2|0|
    |n+2|-|10100100|11001011|11000100|2|0|
    |n+3|-|01001000|10010111|10001000|3|1|
    |n+4|-|0001000|10101111|00010000|-|1|
    |n+5|A|00010000|01001010|00010000|1|0|
    |n+6|-|00100000|10010101|00100000|-|0|
    |n+7|A|00100000|01000110|00100000|1|0|
    |n+8|-|01000000|10001101|01000001|3|1|
    |n+9|G|00000000|10011011|10000011|-|1|
    |n+10|G|00111100|10011011|10000011|-|1|