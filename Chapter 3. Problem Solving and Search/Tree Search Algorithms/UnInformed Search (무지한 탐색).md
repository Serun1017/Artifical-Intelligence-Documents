
---
UnInformed Search (무지한 탐색)는 문제 해결을 위해 상태 공간을 탐색할 때 추가적인 정보 없이 기본적인 탐색 전략을 사용하는 알고리즘이다. 주어진 상태 공간에서 가능한 모든 경로를 균등하게 탐색하며, 상태 간의 연결 관계만을 고려한다.

---
# 특징

- UnInformed Search는 추가 정보나 휴리스틱을 사용하지 않으므로 상태 간의 연결 정보만을 고려한다.
- 완전성(Completeness)을 보장한다. 즉, 목표 상태가 존재하면 반드시 찾아낸다.
- 최적성(Optimality)은 보장되지 않는다. 즉, 찾은 해결책이 최소 비용이 아닐 수 있다.
- 메모리 사용량과 실행 시간은 입력 문제에 따라 다를 수 있다.

---
# 종류

## [[Bredth-First Search (너비 우선 탐색)]]

- Bredth-First Search (너비 우선 탐색)은 탐색 시작 지점부터 인접한 상태를 우선적으로 탐색하며, 목표 상태를 찾을 때까지 점진적으로 넓게 확장하는 전략을 따른다.
## [[Uniform-Cost Search (일정량 탐색)]]

- Uniform-Cost Search (일정량 탐색)는 상태 공간에서 최소 비용 경로를 찾기 위한 탐색 알고리즘으로 경로의 비용을 고려하여 탐색을 수행하며, 시작 상태에서 목표 상태로 이르는 최소 비용 경로를 찾기 위해 사용된다.
## [[Depth-First Search (깊이 우선 탐색)]]

- Depth-Frist Search (깊이 우선 탐색)은 그래프나 트리에서 사용되는 탐색 알고리즘 중 하나로, 특히 그래프의 깊이 방향으로 탐색을 수행하는 알고리즘이다.
## [[Depth-Limited Search (깊이 제한 탐색)]]

- Depth-Limited Search (깊이 제한 탐색)은 깊이 우선 탐색(DFS)의 한 변형으로, 깊이 제한을 설정하여 상태 공간을 탐색하는 알고리즘이다.
## [[Iterative Deepending Search (점차적 깊이 제한 탐색)]]

- Iterative Deepending Search (점차적 깊이 제한 탐색)는 깊이 제한 탐색(DLS)의 한 변형으로 깊이 제한을 점진적으로 늘리면서 깊이 제한 탐색을 반복하는 알고리즘이다.

---
# Summary of Algorithms

![[Summary of Uniform Search.png]]