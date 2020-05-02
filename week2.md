# Week 2

`#Sort` `#Search` `#Greedy` `#DP` `#DFS` `#BFS` `#Trie`

## 

### 숙제

- [정렬<sup>Sort</sup>](https://programmers.co.kr/learn/courses/30/parts/12198)
- [완전탐색<sup>Brute-Forse</sup>](https://programmers.co.kr/learn/courses/30/parts/12230)
- [탐욕법<sup>Greedy</sup>](https://programmers.co.kr/learn/courses/30/parts/12244)

## 

### 알고리즘

- 동적계획법<sup>Dynamic Programming</sup>
- 깊이/너비 우선 탐색<sup>DFS/BFS</sup>

## 

### 모의 테스트

- [2018 KAKAO - 프렌즈4블록](https://programmers.co.kr/learn/courses/30/lessons/17679)
- [2018 KAKAO - 파일명 정렬](https://programmers.co.kr/learn/courses/30/lessons/17686)
- [2018 KAKAO - 가사 검색](https://programmers.co.kr/learn/courses/30/lessons/60060)

## 

### 유용한 함수

- <code>**itertools.product(*\*iterables, repeat=1*)**</code>

    *iterables* 의 요소들 중 *r* 개의 Cartesian 곱을 만들어준다 다중 for 문과 동일하다. 예를 들면, <code>product(A, B)</code>는 <code>[(x, y) for x in A for y in B]</code>와 같다.

    ```
    >>> from itertools import product
    >>> list(product('abc', repeat=2))
    [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]
    ```

- <code>**itertools.permutations(*iterable, r=None*)**</code>

    *iterable* 의 요소들 중 *r* 개의 순열을 만들어준다. *r* 을 지정하지 않을 경우 *iterable* 요소 전체 길이가 기본값으로 지정된다.

    ```
    >>> from itertools import permutations
    >>> list(permutations('abc', 2))
    [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
    ```

- <code>**itertools.combinations(*iterable, r=None*)**</code>

    *iterable* 의 요소들 중 *r* 개의 조합을 만들어준다. *r* 을 지정하지 않을 경우 *iterable* 요소 전체 길이가 기본값으로 지정된다.

    ```
    >>> from itertools import combinations
    >>> list(combinations('abc', 2))
    [('a', 'b'), ('a', 'c'), ('b', 'c')]
    ```

- <code>**itertools.combinations_with_replacement(*iterable, r=None*)**</code>

    *iterable* 의 요소들 중 중복을 허용한 *r* 개의 순열을 만들어준다. *r* 을 지정하지 않을 경우 *iterable* 요소 전체 길이가 기본값으로 지정된다.

    ```
    >>> from itertools import combinations_with_replacement
    >>> list(combinations_with_replacement('abc', 2))
    [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]
    ```

## 

### 새로운 알고리즘

- **Trie 알고리즘**

    - **Trie를 사용하는 이유**

        트리에 존재하는 단어의 수를 N이라고 할 때, 정수형 탐색은 O(logN)만큼 걸리지만 문자열 탐색 같은 경우는 안에 들어 있는 문자열의 길이만큼 시간이 추가적으로 걸린다. 즉, 문자열의 최대 길이를 L이라고 할 때, O(L\*logN) 시간만큼 걸리게 된다. 이 문제를 해결하기 위해서 Trie라는 트리 구조를 이용하는 것이다.

        Hash 알고리즘 사용시, 탐색에 걸리는 시간 복잡도는 O(1)이지만, 공간 복잡도가 O(N)로 좋지 않다. Trie 구조는 Hash 알고리즘에 비해 시간 복잡도는 좋지 않지만 공간 복잡도가 효율적이다.

    - **Trie의 예**

        아래 예시는 bee, can, cat, cd의 네 개의 단어로 만든 Trie 구조이다.

        <img width="70%" alt="trie" src="https://github.com/airotod/algorithm-study/blob/master/images/trie.PNG">

        사전을 만든다고 생각하고 알파벳 하나당 하나의 가지를 친다. root 노드는 비워둔 채 그 자식 노드부터 시작한다. 단어를 탐색할 때는 DFS 알고리즘을 활용한다.

    - **Trie 알고리즘의 활용**

        검색어 자동완성, 사전 검색, 문자열 검사 등에 사용될 수 있다.

    - **Trie 알고리즘의 시간 복잡도**

        가장 긴 문자열의 길이를 L, 총 문자열의 수를 M이라고 하자.<br>
        생성시 O(M\*L): 모든 문자열들을 트리에 넣기 때문에 M개에 대해서 각각의 길이만큼 시간이 걸린다.
        탐색시 O(L): 가장 긴 문자열의 길이만큼만 시간이 걸린다.

    - **파이썬으로 Trie 구현**

        [trie.py](https://github.com/airotod/algorithm-study/blob/master/search/trie.py)

        - <code>insert</code> bee, can, cat, cd

            <img width="90%" alt="trie_insert" src="https://github.com/airotod/algorithm-study/blob/master/images/trie_insert.gif">

        - <code>search</code> caw, be, can

            <img width="90%" alt="trie_search" src="https://github.com/airotod/algorithm-study/blob/master/images/trie_search.gif">

## 

### 참고 자료

- [Python Documentation - itertools](https://docs.python.org/3/library/itertools.html)
- [파이썬으로 Trie 구현](https://gist.github.com/osori/29289bc21d453777c5133754e1d5dfd9)