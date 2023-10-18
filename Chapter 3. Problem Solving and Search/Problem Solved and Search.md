
---
# [[Problem-Solving Agents]]

- 문제 해결 에이전트 (Problem-Solving Agents)는 주어진 문제를 해결하기 위해 상태 공간을 탐색하는 에이전트이다.

---
# [[Problem Types]]

- 문제의 상태 공간(State Space), 관측 가능성(Observable), 결정론성(Determinisitic)에 따라 다른 유형의 문제를 구분할 수 있다.
	- [[Single-State Problem (단일 상태 문제)]]
	- Conformant Problem (준수 문제)
	- Contingency Problem (위험 문제)
	- Exploration Problem (탐사 문제)

---
# [[Single-State Problem (단일 상태 문제)]]

- Single-State Problem (단일 상태 문제)는 에이전트가 초기 상태에서 시작하여 목표 상태에 도달하기 위한 문제를 해결하는 유형이다.

---
# [[State Space (상태 공간)]]

- State Space (상태 공간)은 문제에 대한 가능한 모든 상태의 집합을 나타낸다.

---
# [[Tree Search Algorithms (트리 탐색 알고리즘)]]

- Tree Search Algorithms (트리 탐색 알고리즘)은 그래프 또는 트리 구조에서 목표 상태를 찾거나 원하는 상태로 이동하기 위해 사용되는 알고리즘이다. 크게 UnInformed Search와 Informed Search로 나눌 수 있다.

## [[Search Strategies (탐색 전략)]]
- Search Strategies (탐색 전략)은 상태 공간에서 목표 상태를 찾거나 원하는 상태로 이동하기 위한 방법을 정의한다.
- 크게 UnInformed Search 와 Informed Search 로 나눌 수 있다.

### [[UnInformed Search (무지한 탐색)]]

- UnInformed Search (무지한 탐색)는 문제 해결을 위해 상태 공간을 탐색할 때 추가적인 정보 없이 기본적인 탐색 전략을 사용하는 알고리즘이다.

### [[Informed Search Algorithms|Informed Search (정보를 활용한 탐색)]]

- Informed Search (정보를 활용한 탐색)는 추가적인 정보나 휴리스틱(heuristic)을 활용하여 탐색을 더 효율적으로 수행하는 알고리즘이다.

---
# [[Informed Search Algorithms|Graph Search(그래프 탐색)]]

![[Graph Search.png]]