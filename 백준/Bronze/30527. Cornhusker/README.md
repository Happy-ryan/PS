# [Bronze III] Cornhusker - 30527 

[문제 링크](https://www.acmicpc.net/problem/30527) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 사칙연산

### 제출 일자

2025년 10월 2일 22:41:45

### 문제 설명

<p>Corn farmers need to do pre-harvest yield estimates to determine the approximate number of bushels of corn their farm will produce. They do this to determine if they have enough storage space (grain bins) to store the harvested crop or if they'll have to store the corn elsewhere, like a co-op (which costs \$\$\$). They also use these estimates when negotiating the future market prices of their corn. Estimates are typically done about a month or two before harvest. By this time, the ears have formed and the kernels on the ears are mostly developed (this makes counting the kernels easier).</p>

<p>According to the <em>University of Nebraska-Lincoln</em>, <em>Nebraska Extension for Educators</em>, the standard way to estimate corn yield is to calculate the number of bushels of corn per acre. To make the calculations easier, they use an area of 1/1000th of an acre, which, with 30" row spacing, is a section of one row about 17'5" long. Within that 17'5", five ears are chosen at random. For each ear, the number of kernels are counted by multiplying the number of rows of kernels around by the number of kernels over the length of the ear. The totals for each of the five ears are added together and then divided by five to determine the average number of kernels per ear of corn. This number is then multiplied by the total number of ears of corn in the 17'5" section of row. This gives you the total number of kernels in 1/1000th of an acre. This number is then divided by the <em>Kernel Weight Factor</em> (<em>KWF</em>). The <em>KWF</em> is a function of how wet (or dry) the growing season is and is typically a value between 75 (wet) and 95 (dry). The resulting quotient is the number of bushels/acre the farmer can expect to harvest.</p>

<p>For example, suppose that the average number of kernels per ear is 512 (16 kernels around by 32 kernels lengthwise), and there are 25 ears in the 17'5" of row with a <em>KWF</em> of 85. The farmer could then expect:</p>

<p>$$\frac{25\times 512}{85}\ = \ 150\ bushels$$</p>

<p>Since farmers are quite conservative in their estimates, all calculations are done as integers with no rounding.</p>

### 입력 

 <p>Input consists of two lines. The first line contains 10 space separated integer values representing the number of kernels around ($A$) and number of kernels long ($L$) for each of five ears of corn ($8 \leq A \leq 24$), ($20 \leq L \leq 50$).</p>

<p>The second line contains 2 space separated integer values representing the number of ears of corn, $N$, in the 17'5" row ($10 \leq N \leq 50$) and the $KWF$ ($75 \leq KWF \leq 95$).</p>

### 출력 

 <p>Output a single integer equal to the estimated number of bushels of corn per acre the farmer can expect given the input supplied.</p>

