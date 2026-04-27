# [Silver I] Double or One Thing - 25093 

[문제 링크](https://www.acmicpc.net/problem/25093) 

### 성능 요약

메모리: 32412 KB, 시간: 40 ms

### 분류

그리디 알고리즘, 문자열

### 제출 일자

2025년 5월 10일 20:58:18

### 문제 설명

<p>You are given a string of uppercase English letters. You can highlight any number of the letters (possibly all or none of them). The highlighted letters do not need to be consecutive. Then, a new string is produced by processing the letters from left to right: non-highlighted letters are appended once to the new string, while highlighted letters are appended twice.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 444px; height: 21px;"></p>

<p>For example, if the initial string is <code>HELLOWORLD</code>, you could highlight the <code>H</code>, the first and last <code>L</code>s and the last <code>O</code> to obtain <code><span style="background-color: #fee183;">H</span>E<span style="background-color: #fee183;">L</span>LOW<span style="background-color: #fee183;">O</span>R<span style="background-color: #fee183;">L</span>D</code> ⇒ <code>HHELLLOWOORLLD</code>. Similarly, if you highlight nothing, you obtain <code>HELLOWORLD</code>, and if you highlight all of the letters, you obtain <code>HHEELLLLOOWWOORRLLDD</code>. Notice how each occurrence of the same letter can be highlighted independently.</p>

<p>Given a string, there are multiple strings that can be obtained as a result of this process, depending on the highlighting choices. Among all of those strings, output the one that appears first in alphabetical (also known as lexicographical) order.</p>

<p>Note: A string $s$ appears before a different string $t$ in alphabetical order if $s$ is a prefix of $t$ or if at the first place $s$ and $t$ differ, the letter in $s$ is earlier in the alphabet than the letter in $t$. For example, these strings are in alphabetical order: <code>CODE</code>, <code>HELLO</code>, <code>HI</code>, <code>HIM</code>, <code>HOME</code>, <code>JAM</code>.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $T$. $T$ test cases follow. Each test case is described in a single line containing a single string $S$.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from 1) and $y$ is the string that comes first alphabetically from the set of strings that can be produced from $S$ by the process described above.</p>

