# Week 3

`#DP` `#DFS` `#BFS` `#Trie` `#Binary Search` `#re`

## 

### 숙제

- [동적계획법<sup>Dynamic Programming</sup>](https://programmers.co.kr/learn/courses/30/parts/12263)
- [깊이/너비 우선 탐색<sup>DFS/BFS</sup>](https://programmers.co.kr/learn/courses/30/parts/12421)

## 

### 알고리즘

- 이분탐색<sup>Binary Search</sup>

    - 자료를 반으로 계속해서 나누어 탐색하는 방법으로, 반드시 **정렬**된 자료여야 한다.

    - 다음은 자료 <code>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</code>가 주어졌을 때 7을 찾는 과정이다.

        <img width="70%" alt="binary_search" src="https://github.com/airotod/algorithm-study/blob/master/images/binary_search.gif">

## 

### 모의 테스트

- [카카오 인턴십 코딩 테스트 실전 모의고사](https://programmers.co.kr/competitions/145/kakao-internship-test)

## 

### 유용한 함수

- **정규 표현식<sup>re, Regular expressions</sup>**

    - **정규 표현식이란**

        정규 표현식(또는 정규식)은 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어로, 특정 규칙의 문자열을 찾는데 유용하게 사용된다. 정규식에는 특수 문자와 일반 문자가 모두 포함될 수 있는데, 특수 문자에는 다음과 같은 것들이 있다.

        - <code>**.**</code>: 줄 바꿈 문자인 <code>\n</code>을 제외한 모든 문자와 매치된다.

        - <code>**^**</code>와 <code>**\A**</code>: 문자열의 처음과 매치된다. <code>^</code>에 <code>re.MULTILINE</code> 또는 <code>re.M</code> 옵션을 주는 경우, 각 줄의 처음과 매치한다.

        - <code>**$**</code>와 <code>**\Z**</code>: 문자열의 끝과 매치된다. <code>$</code>에 <code>re.MULTILINE</code> 또는 <code>re.M</code> 옵션을 주는 경우, 각 줄의 끝과 매치된다.

        - <code>**\***</code>: \* 바로 앞의 문자가 0번 이상 반복될 때 매치된다.

        - <code>**+**</code>: \+ 바로 앞의 문자가 0번 이상 반복될 때 매치된다.

        - <code>**?**</code>: ? 바로 앞의 문자가 0번 또는 1번 반복될 때 매치된다. <code>\{0, 1\}</code>과 동일하다.

        - <code>**\{m\}**</code>: \{m\} 바로 앞의 문자가 m번 반복될 때 매치된다.

        - <code>**{m, n\}**</code>: \{m, n\} 바로 앞의 문자가 m번 이상 n번 이하 반복될 때 매치된다.

        - <code>**\\**</code>: 특수 문자를 문자 자체로 매치되게 하고 싶을 때 사용하는 escape 문자이다.

        - <code>**[]**</code>: 문자열 집합을 가리킬 때 사용된다. 예를 들어 <code>[abc]</code>는 'a', 'b', 'c' 중 하나와 매치된다. <code>'-'</code>를 사용하면 문자열의 범위를 지정할 수 있다. 예를 들어, <code>[0-9]</code>는 숫자, <code>[a-zA-Z]</code>는 알파벳에 매치된다. 그리고 [] 내에서는 특수 문자들도 문자 자체로 매치된다. <code>^</code>를 [] 안에 첫 번째로 입력하는 경우 [] 내에 포함되지 않는 문자들과 매치된다.

        - <code>**|**</code>: "또는"을 의미한다.

        - <code>**()**</code>: 괄호로 둘러싸인 모든 것과 매치된다.

        - <code>**\B**</code>와 <code>**\b**</code>

        - <code>**\D**</code>와 <code>**\d**</code>: <code>\d</code>는 숫자와 매치되며 <code>[0-9]</code>와 동일한 의미이다. <code>\D</code>는 숫자가 아닌 것과 매치되며 <code>[^0-9]</code>와 동일한 의미이다.

        - <code>**\S**</code>와 <code>**\s**</code>: <code>\S</code>는 whitespace가 아닌 문자와 매치되며 <code>[^\t\n\r\f\v]</code>와 동일한 의미이다. <code>\s</code>는 whitespace와 매치되며 <code>[\t\n\r\f\v]</code>와 동일한 의미이다.

        - <code>**\W**</code>와 <code>**\w**</code>: <code>\w</code>는 숫자 또는 알파벳과 매치되며 <code>[a-zA-Z0-9_]</code>와 동일한 의미이다. <code>\W</code>는 숫자 또는 알파벳이 아닌 문자와 매치된다.

        이외에도 다양한 특수 문자가 존재한다.

    - <code>**re.compile(*pattern, flags=0*)**</code>

        정규 표현식 패턴을 정규 표현식 객체로 컴파일하며, <code>match()</code>나 <code>search()</code>를 사용하여 매칭에 사용될 수 있다. 다음 두 방식은 동일한 의미이지만, <code>re.compile()</code>을 사용하는 경우 정규 표현식 객체의 결과를 저장하여 재사용할 수 있다. 특정 옵션을 줄 수도 있다.

        ```
        >>> prog = re.compile(pattern)
        >>> result = prog.match(string)
        ```

        ```
        >>> result = re.match(pattern, string)
        ```

    - <code>**re.search(*pattern, string, flags=0*)**</code>

        *string* 에서 *pattern* 과 매치되는 첫 번째 위치를 조사한 후, 매치되는 것이 있으면 match 객체를, 그렇지 않으면 None을 반환한다.

        ```
        >>> print(re.search('[a-z]+', 'python'))
        <_sre.SRE_Match object at 0x01F3FA68>
        >>> print(re.match('[a-z]+', '3 python'))
        <_sre.SRE_Match object at 0x01F3FA30>
        ```

    - <code>**re.match(*pattern, string, flags=0*)**</code>

        *string* 의 처음부터 *pattern* 과 매치되는지 조사한 후, 매치되면 match 객체를, 그렇지 않으면 None을 반환한다.

        ```
        >>> print(re.match('[a-z]+', 'python'))
        <_sre.SRE_Match object at 0x01F3F9F8>
        >>> print(re.match('[a-z]+', '3 python'))
        None
        ```

    - <code>**re.findall(*pattern, string, flags=0*)**</code>

        *string* 에서 *pattern* 에 매치되는 모든 문자열의 리스트를 반환한다.

        ```
        >>> print(re.findall('[a-z]+', 're is awesome'))
        ['re', 'is', 'awesome']
        ```

    - <code>**re.finditer(*pattern, string, flags=0*)**</code>

        *string* 에서 *pattern* 에 매치되는 모든 문자열에 대해 match 객체로 이루어진 iterator 객체를 반환한다.

        ```
        >>> print(re.finditer('[a-z]+', 're is awesome'))
        <callable_iterator object at 0x0000018865670390>
        ```

    - <code>**re.split(*pattern, string, maxsplit=0, flags=0*)**</code>

        *pattern* 의 발생에 따라 *string* 을 분리한다. *pattern* 에 괄호가 사용되는 경우, 모든 그룹의 텍스트를 반환한다. *maxsplit* 에 0보다 큰 값을 지정할 경우, 해당 수만큼 분리한 후 나머지는 리스트의 마지막 요소로 반환한다.

        ```
        >>> re.split(r'\W+', 'Words, words, words.')
        ['Words', 'words', 'words', '']
        >>> re.split(r'(\W+)', 'Words, words, words.')
        ['Words', ', ', 'words', ', ', 'words', '.', '']
        >>> re.split(r'\W+', 'Words, words, words.', 1)
        ['Words', 'words, words.']
        >>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
        ['0', '3', '9']
        >>> re.split(r'(\W+)', '...words, words...')
        ['', '...', 'words', ', ', 'words', '...', '']
        ```

## 

### 참고 자료

- [Python Documentation - re](https://docs.python.org/3/library/re.html)
- [점프 투 파이썬 - 정규표현식 (2)](https://wikidocs.net/4308)
- [점프 투 파이썬 - 정규표현식 (3)](https://wikidocs.net/4309)