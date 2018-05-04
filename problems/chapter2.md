---
layout: mathPage
title: Chapter 2 Solution
author: Mohamed Abdallah
---
# Information Theory

1. Suppose that X is a random variable that takes on values from an M-letter alphabet. Show that $0 \leq \mathcal{H(x)} \leq \log_2 \mathcal{M}$

    > **Solution**

    - The Entropy should be maximal if all the events occur with same probability (uncertainty maximise when all possible events are equi-probable). 
    - $$ \mathcal{H}_n\left( \mathcal{p}_0, \cdots, \mathcal{p}_{n-1}\right)\leq\mathcal{H}_n\left(\frac{1}{n}, \cdots, \frac{1}{n} \right) = log_{\ base}(\mathcal{n})
    $$

2. An experiment has 2 binary random variable outputs X & Y, with the shown joint probabilities. Calculate the amount of information gained, or expected, from knowing each of the following:

    > **Solution**

    1. $\mathcal i (Y_{= 1}) = 4.05$
    2. The value of X
        - $\mathcal i (X_{= 0}) = 5.64$,  $\mathcal i (X_{= 1}) = 4.05$
    3. The value of Y, given x= 0 : $\mathcal i (X_{= 0}) = 5.64$
    4. The values of both x,y :
        - $\mathcal i (Y_{= 0}, X_{=0}) = 2.32$
        - $\mathcal i (Y_{= 0}, X_{=1}) = 3.32$
        - $\mathcal i (Y_{= 1}, X_{=0}) = 3.32$
        - $\mathcal i (Y_{= 1}, X_{=1}) = 0.737$

    5. The average common information X and Y: Entropy = $\mathcal H=\Sigma\ \mathcal P (Y,X) * \mathcal i (Y,X) = 0.2* 2.32 + 0.1* 3.32 + 0.1* 3.32 + 0.6* 0.737 = 2.465$

# Markov finite state Model

1. A source emits iid symbols form the alphabet {a, b, & c}, with the following probabilities. Calculate the entropy of that source.
    > **Solution**

    - Entropy : $-\Sigma_{i=0}^{i=n-1} \mathcal{P(a_i)}*\log_2(\mathcal {P(a_i)}) = 1.5$

2. The probability of the current symbol, X n , emitted form the previous source, is found to be related to the previous symbol, X n-1 , as shown in table. Recalculate the entropy of the source.

    > **Solution**

    - $\mathcal{H(S_j)} = -\Sigma_{i=0}^{i=n-1} \mathcal{P(x_i\vert S_j)}*log_2(\mathcal{P(x_i\vert S_i)})$
        1. $\mathcal{H}(S_a) = 1.4056 $
        2. $\mathcal{H}(S_b) = 1.4056 $
        3. $\mathcal{H}(S_c) = 1.0613 $
    - Entropy: $\Sigma_{i=0}^{i=n-1} \mathcal{P(S_i)}*\mathcal{H(S_i)} = 1.2334$

3. The bases of a genomic sequence have the probabilities shown. Calculate the self-information of “C”, and the entropy of the sequence.

    > **Solution**

    - Self-entropy of C : $-\log_2\mathcal{P(c)} = 3$
    - The Entropy of the whole Seq. :$-\Sigma_{i=0}^{i=n-1} \mathcal{P(a_i)}*\log_2(\mathcal{P(a_i)}) = 1.75$

4. The probability of the any base, B n , in the previous sequence, is found to be related to its previous base, B n-1 , by the probabilities given in the following table. Recalculate the entropy of the sequence.

    > **Solution**

    - $\mathcal{H(S_j)} = -\Sigma_{i=0}^{i=n-1} \mathcal{P(x_i\vert S_j)}*log_2(\mathcal{P(x_i\vert S_i)})$
        1. $\mathcal{H}(S_A) = 1.846$
        2. $\mathcal{H}(S_C) = 1.922$
        3. $\mathcal{H}(S_G) = 1.686$
        4. $\mathcal{H}(S_T) = 1.368$
    - New entropy of the sequence = $\Sigma_{i=0}^{i=n-1} \mathcal{P(S_i)}*\mathcal{H(S_i)} = 1.576425$

# Decodability

1. Determine whether each of the following codes is uniquely decodable (UD), prefix, instantaneous, or near instantaneous:

    > **Solution**

    | Code           | UD  | Prefix | Instantaneous | Near-Instant |
    | -------------- | --- | ------ | ------------- | ------------ |
    | {0,01,11,111}  | NO  | NO     |     NO        |NO
    | {0,01,110,111} | NO  | NO     |     NO        |NO
    | {0,10,110,111} |  YES| YES    |     YES       | NO
    | {1,10,110,111} |  NO | NO     | NO            | NO

2. An alphabet of 7 symbols, had code lengths of 2, 2, 3, 3, 3, 3, & 3 bits. Is this code uniquely decodable? Why?
    > **Solution**
    - Answer: No
    - Reason : Does not satisfy the Kraft-Milan inequality
         $\Sigma_{i=0}^{i=n-1} 2^{-l_i} = 1.125$

3. What the largest number is of symbols that can be coded using a ternary (i.e. 3 symbols) code, while the code length of each symbol does not exceed 3? Why?
    > **Solution**
    - Answer:
        1. 7 prefix canonical
        2. 27 3-bit for trinary code
    - Reason:
        1. The max number of nodes prefix = 
            $(n_{\ base\ of\ bits} -1 )L_{\ number\ of\ bits} + 1$

        2. The max number trinary code: $Base^{\ length}$

4. 14 symbols are coded using a ternary (i.e. 3) code. The code lengths are 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3,3, 3, & 3. Is this code uniquely decodable? Why?
    > **Solution**

    - Answer : yes
    - Reason : Its satisfy the kraft Milan Inequality : $\Sigma_{i=0}^{i=n-1} 3^{-l_i} = \frac{26}{27}$

5. An alphabet of 7 symbols, had code lengths of 2, 2, 3,3, 3, 3, & 3 bits. Is this code uniquely decodable? Why?

    > **Solution**

    - Answer: No
    - Reason : Does not satisfy the Kraft-Milan inequality
         $\Sigma_{i=0}^{i=n-1} 2^{-l_i} = 1.125$

6. Using Kraft’s Inequality, check the decidability of the following code table. Next, check the code table. Is the code decodable? Why? Calculate the entropy, the average code length, and the redundancy

     **Solution**

    1. Kraft’s inequality result: $\Sigma_{i=0}^{i=n-1} 2^{-l_i} = 1$

    2. Decodability based on Kraft’s inequality: Yes

    3. Is the code decodable? No

    4. Why? Following these steps

        1. You get a dangling suffix that is a codeword.
        2. There are no more unique dangling suffixes.

        - example: db may be decoded as bc

    5. Average Code Length = $\Sigma_{i=0}^{i=n-1} \mathcal{P(a_i)}*{l_i} = 2.625$

    6. Redundancy = $\left[2.625 -(-\Sigma_{i=0}^{i=n-1} \mathcal{P(a_i)}*\log_2(\mathcal{P(a_i)})\right] = 2.625 - 1.75 = 0.875$

7. Assume a 5-symbol alphabet {A, B, C, D, & E}.

    - Build a prefix code for the symbols.

    > **Solution**

    | Letter | Code |
    |--------|------|
    |   A    |  0   |
    |   B    | 10   |
    |   C    |110   |
    |   D    |1110  |
    |   E    |1111  |

    <div class="mermaid">
        graph TB
            0((#0))-- 1 -->1((#1))
            1-- 1 -->2((#2))
            2-- 1 -->3((#3))
            subgraph 111
            3-- 0 -->D
            3-- 1 -->E
            end
            subgraph 11
            2-- 0 -->C
            end
            subgraph 1
            1-- 0 -->B
            end
            subgraph 
            0-- 0 -->A
            end
    </div>

    - Code the following sequence: CBABAA

        > **Solution**

        1101001000
