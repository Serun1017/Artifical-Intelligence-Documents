
---
Tree Search Algorithms (트리 탐색 알고리즘)은 그래프 또는 트리 구조에서 목표 상태를 찾거나 원하는 상태로 이동하기 위해 사용되는 알고리즘이다. 이러한 알고리즘은 인공 지능, 문제 해결, 경로 계획, 게임 트리 탐색 등 다양한 응용 분야에서 사용된다.

![[Tree Search Algorithms.png]]

---
# Example: Romania Tree Graph

- Step 1.
![[Tree Search Algorithms_Romania_Example1.png]]
- Start in Arad

- Step 2.
![[Tree Search Algorithms_Romania_Example2.png]]
- Search Child Node: Shibu, Timisoara, Zerind

- Step 3.
![[Tree Search Algorithms_Romania_Example3.png]]
- Move to Child Node and Search Child Node
  - Move to "Sibiu"
  - Search Child Node: Arad, Fagaras, Oradea, Rimnicu Vilcea

---
# 기본 개념

1. State (상태)
   - 상태는 물리적인 구성물의 표현으로, 문제 해결 과정에서 에이전트가 있을 수 있는 상황 또는 구성을 나타낸다.
   - 이것은 구체적인 문제 공간에서 특정 상황을 나타내는데 사용된다.
2. Node (노드)
   - 노드는 탐색 트리 (Search Tree)의 일부를 나타내는 데이터 구조이다.
   - 노드는 상태 (State)와 함께 부모 노드, 자식 노드, 깊이 (Depth), 경로 비용 (Path Cost) 등의 정보를 포함한다.
3. 부모 (Parent) 노드
   - 특정 노드의 부모 노드는 해당 노드로 이동하는 경로에서 직전에 방문한 노드를 나타낸다.
4. 자식 (Children) 노드
   - 특정 노드의 자식 노드는 해당 노드로부터 다음에 방문할 수 있는 노드 들을 나타낸다.
5. 깊이 (Depth)
   - 노드의 깊이는 루트 노드에서 해당 노드까지 이동하는 데 필요한 단계 수를 나타낸다.
6. 경로 비용 (Path Cost)
   - 경로 비용은 시작 노드로부터 현재 노드까지 이르는데 필요한 비용을 나타낸다.
   - 이것은 문제의 특성에 따라 다를 수 있으며, 경로의 비용을 최소화하려는 목표를 가질 수 있다.
7. Expand 함수
   - Expand 함수는 탐색 알고리즘에서 사용되며, 새로운 노드를 생성하고 다양한 필드를 채우는 역할을 한다.
   - Expand 함수는 문제의 Successor Function을 활용하여 문제에서 가능한 다음 상태 (State)을 생성하고, 각 상태에 해당하는 새로운 노드르 생성한다.

---
# Example: Generatl Tree Search

![[Tree Search Algorithms_General Tree Search Example.png]]

---
# [[Search Strategies (탐색 전략)]]

- Search Strategies (탐색 전략)은 상태 공간에서 목표 상태를 찾거나 원하는 상태로 이동하기 위한 방법을 정의한다.
- 크게 UnInformed Search 와 Informed Search 로 나눌 수 있다.

### [[UnInformed Search (무지한 탐색)]]

- UnInformed Search (무지한 탐색)는 문제 해결을 위해 상태 공간을 탐색할 때 추가적인 정보 없이 기본적인 탐색 전략을 사용하는 알고리즘이다.

### [[Informed Search Algorithms|Informed Search (정보를 활용한 탐색)]]

- Informed Search (정보를 활용한 탐색)는 추가적인 정보나 휴리스틱(heuristic)을 활용하여 탐색을 더 효율적으로 수행하는 알고리즘이다.