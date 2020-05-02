# Week 1

`#Hash` `#Stack` `#Queue` `#Heap` `#Sort` `#Search` `#Greedy`

## 

### 숙제

- [해시<sup>Hash</sup>](https://programmers.co.kr/learn/courses/30/parts/12077)
- [스택<sup>Stack</sup>/큐<sup>Queue</sup>](https://programmers.co.kr/learn/courses/30/parts/12081)
- [힙<sup>Heap</sup>](https://programmers.co.kr/learn/courses/30/parts/12117)

## 

### 알고리즘

- 정렬<sup>Sort</sup>
- 완전탐색<sup>Brute-Force</sup>
- 탐욕법<sup>Greedy</sup>

## 

### 모의 테스트

- [2018 KAKAO - 비밀지도](https://programmers.co.kr/learn/courses/30/lessons/17681)
- [2018 KAKAO - 다트 게임](https://programmers.co.kr/learn/courses/30/lessons/17682)

## 

### 유용한 함수

- <code>**str.zfill(*width*)**</code>

    문자열의 왼쪽을 '0'으로 채워서 *width* 길이로 만들어준다.

    ```
    >>> "101.zfill(5)
    '00101'
    ```

- <code>**bin(*x*)**</code>

    정수 *x* 를 이진수 문자열로 나타낸다. 단, 앞에 '0b'를 포함한다.

    ```
    >>> bin(9)
    '0b101'
    ```

- <code>**str.isdigit()**</code>

    *string* 의 모든 문자들이 숫자면 True를, 그렇지 않으면 False를 반환한다.

    ```
    >>> "123".isdigit()
    True
    >>> "a123".isdigit()
    False
    ```

    참고: <code>str.isalpha()</code>, <code>str.isalnum()</code>

- <code>**re.findall(*pattern, string, flags=0*)**</code>

    *string*에서 *pattern* 에 매칭되는 모든 문자열의 리스트를 반환한다.

    ```
    >>> import re
    >>> re.findall("[a-zA-Z]+", "I am a student")
    ['I', 'am', 'a', 'student']
    ```

## 

### 참고 자료

- [Python Documentation - Built-in Functions](https://docs.python.org/ko/3/library/functions.html)
- [Python Documentation - re](https://docs.python.org/3/library/re.html)
- [해시 알고리즘 유투브 영상](https://www.youtube.com/watch?v=Vi0hauJemxA)