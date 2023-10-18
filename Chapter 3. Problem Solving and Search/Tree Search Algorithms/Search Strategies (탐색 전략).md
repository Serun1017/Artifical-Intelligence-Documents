
---
Search Strategies (탐색 전략)은 인공 지능 및 문제 해결 분야에서 사용되는 알고리즘으로, 상태 공간에서 목표 상태를 찾거나 원하는 상태로 이동하기 위한 방법을 정의한다. 다양한 탐색 전략이 존재하며, 이러한 전략은 다음과 같은 주요 특성에 따라 구분된다.

---
# 특성
## 1. Completeness (완전성)

- 완전한 탐색 전략은 목표 상태를 찾을 수 있는 경우 항상 찾아낸다. 모든 가능한 경로를 탐색하고, 문제 해결이 가능한 경우 반드시 해결한다.
- 불완전한 탐색 전략은 목표 상태를 찾지 못할 수 있다.
## 2. Time Complexity (시간 복잡도)

- 시간 복잡도는 목표 상태를 찾는 데 걸리는 시간을 나타낸다.
- 일부 전략은 효율적인 시간 복잡도를 갖지만, 다른 전략은 오랜 시간이 걸릴 수 있다.
## 3. Space Complexity (공간 복잡도-메모리 사용량)

- 공간 복잡도는 탐색 중에 유지해야 하는 노드 및 상태의 양을 나타낸다. 일부 탐색 전략은 적은 메모리를 사용하며, 다른 전략은 더 많은 메모리를 필요로 할 수 있다.
## 4. Optimality (최적성)

- 최적 탐색 전략은 최적의 경로 또는 해결책을 찾아낸다. 즉, 경로의 비용이 최소인 해결책을 제공한다.

---
# Time, Space Complexity 측정

- Time, Space Complexity는 다음으로 측정할 수 있다.
  - *b - maximum branching factor of the search tree*
  - *d - depth of the least-cost solution*
  - *m - maximum depth of the state space (may be infinite)*
