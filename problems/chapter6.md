---
layout: mathPage
title: Chapter 6 Solution
author: Mohamed Abdallah
---
# Predictive

## Burrows-Wheeler transform

|0| A | C | A | C | A | T || || A | C | A | C | A | T |
|1| C | A | C | A | T | A || || A | C | A | T | A | C |
|2| A | C | A | T | A | C || || A | T | A | C | A | C |
|3| C | A | T | A | C | A || || C | A | C | A | T | A |
|4| A | T | A | C | A | C || || C | A | T | A | C | A |
|5| T | A | C | A | C | A || || T | A | C | A | C | A |

code : 0, TCCAAA

|Sequence|Index in the MtV|0| 1| 2| 3| 4|
|N |3 |A |C |T |N |Δ|
|N |0 |N |A |C |T |Δ|
|Δ |4 |N |A |C |T |Δ|
|Δ |0 |Δ |N |A |C |T|
|Δ |0 |Δ |N |A |C |T|
|N |1 |Δ |N |A |C |T|

code: 304001

|A|||C|
|A|||N|
|A|||A|
|A|||C|
|C|||A|
|C|||A|
|N|||A|

seq: ANACAAC
## Associative Coder of Buyanovsky (ACB)

| A/CGACGA | 1 | A/CGACGA |
| AC/GACGA | 2 | ACGA/CGA |
| ACG/ACGA | 3 | AC/GACGA |
| ACGA/CGA | 4 | ACGAC/GA |
| ACGAC/GA | 5 | ACG/ACGA |
| ACGACG/A | 6 | ACGACG/A |

Code {‘2-2’,1,’A’}

| A/CGACGACA | 1 | A/CGACGACA |
| AC/GACGACA | 4 | ACGA/CGACA |
| ACG/ACGACA | 7 | ACGACGA/CA |
| ACGA/CGACA | 2 | AC/GACGACA |
| ACGAC/GACA | 5 | ACGAC/GACA |
| ACGACG/ACA | 8 | ACGACGAC/A |
| ACGACGA/CA | 3 | ACG/ACGACA |
| ACGACGAC/A | 6 | ACGACG/ACA |

Code {‘0’,0,’T’}