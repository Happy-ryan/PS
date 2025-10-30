# [Bronze IV] Driving Dilemma - 34363 

[문제 링크](https://www.acmicpc.net/problem/34363) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 사칙연산

### 제출 일자

2025년 10월 31일 00:35:53

### 문제 설명

<p>The day has finally come for Rishi to take his driving test. He's learned all of the rules of the road. He has practiced for many hours, and now he just needs to follow all of the rules of the road to pass the driving test.</p>

<p>Rishi's first challenge comes at the first intersection. As he approaches the intersection, the light turns yellow! If he does not make it to the other side of the intersection before the light turns red, he will have violated the rules of the road and will fail the test.</p>

<p>Because Rishi is a good driver, he is driving at exactly the speed limit, and will continue going at exactly the speed limit as he goes through the intersection. Rishi is also very good at determining distances, so he knows exactly how many feet away from the end of the intersection he is. And, since Rishi has practiced driving so much, he also knows exactly how many seconds the light will remain yellow before turning red. After turning red, the traffic light will remain red.</p>

<p><strong>If Rishi continues driving at exactly the speed limit, will he make it to the end of the intersection or beyond that point before the light turns red?</strong> (For the purpose of this problem, you can assume that Rishi and his car are a single point with no length or width.)</p>

### 입력 

 <p>The first line of input will contain of a single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D446 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>≤</mo><mi>S</mi><mo>≤</mo><mn>10</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10 \leq S \leq 10\,000$</span></mjx-container>, the speed limit (in miles per hour) of the road Rishi is driving on.</p>

<p>The second line of input will contain of a single real number <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D437 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>D</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \leq D \leq 100\,000$</span></mjx-container>, the distance (in feet) to the end of the intersection. The number will have at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container> digits after the decimal point.</p>

<p>The third line of input will contain a single real number <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D447 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>T</mi><mo>≤</mo><mn>100</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \leq T \leq 100\,000$</span></mjx-container>, the amount of time (in seconds) before the traffic light turns red. The number will have at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container> digits after the decimal point.</p>

<p>In order to avoid problems with rounding, you are guaranteed that Rishi will be at least one foot from the end of the intersection, or at least one foot after the end of the intersection when the light turns red. Note your comparisons should still be exact; do not factor in this guarantee into your answer.</p>

### 출력 

 <p>If Rishi will make it through the intersection before the light turns red, output "MADE IT" (without the quotes). Otherwise, output "FAILED TEST" (without the quotes).</p>

