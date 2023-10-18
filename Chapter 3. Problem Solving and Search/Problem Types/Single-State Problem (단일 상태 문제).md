
---
Single-State Problem (단일 상태 문제)는 에이전트가 초기 상태에서 시작하여 목표 상태에 도달하기 위한 문제를 해결하는 유형이다. 단일 상태 문제 에서  에이전트는  어떤 상태에 있을 것인지 정확히 알 수 있다. (Fully Observable, 완전 관찰 가능) 단일 상태 문제에서 목표는 초기 상태에서 목표 상태로 가는 단일 순차적인 해결책을 찾는 것이다. (Deterministic, 확정적)
단일 상태 문제는 초기 상태(Initial State), 후속 함수(Successor Function), 목표 테스트(Goal Test), 경로 비용(Path Cost)으로 정의된다.

---
# Initial State (초기 상태)

- 문제(Problem)의 시작점으로, 에이전트가 문제를 해결하기 위해 시작하는 상태이다.
- 에이전트의 초기 위치나 상태를 나타낸다.

---
# Successor Function (후속 함수)

- 에이전트가 수행 가능한 액션과 해당 액션을 수행한 후에 어떤 새로운 상태로 이동하는지를 정의하는 함수이다.

---
# Goal Test (목표 테스트)

- 에이전트가 목표에 도달했는지를 확인하는 기준을 나타낸다.
- 목표는 명시적인 형태일 수도 있고, 암묵적인 조건일 수도 있다.

---
# Path Cost (경로 비용)

- 초기 상태에서 목표 상태까지 도달하기 위한 비용을 나타낸다.
- 이 비용은 주로 액션의 수행 횟수, 거리, 또는 다른 측정 항목의 합계로 정의된다.

---
# Example: Romania

- 다음과 같이 Arad에서 Bucharest로 향하는 최단 거리를 구하는 에이전트를 만든다고 한다.
![[Problem-Solving Agents_Example.png]]

1. Initial State (초기 상태)
   - 처음 위치: Arad
2. Succssor Function (후속 함수)
   - 위의 경우 현재 에이전트가 위치한 도시에서 이동할 수 있는 다른 도시의 집합이다.
     - *S(X) = set of action-state pairs*
     - *S(Arad) = {(Arad -> Zerind, Zerind),...}*
3. Goal Test (목표 테스트)
   - 위의 경우 현재 에이전트가 위치한 도시가 Bucharest인지 검증함으로서 테스트를 진행한다.
     - *x = "at Bucharest"*
4. Path Cost (경로 비용)
   - 위의 경우 현재 에이전트가 위치한 도시를 위해 이동한 경로들의 합이 될 수 있다.
     - *g(x) = sum of path that agent transit*
5. Solution (해결책)
   - Solution은 Action의 Sequence로 이루어져 있다. 따라서 Arad에서 Bucharest까지 갈 수 있는 모든 경로가 Solution이 될 수 있다. 이 중 최적의 경로는 문제에서 제시된 조건인 최단 거리를 만족하는 방법이 최적의 해결책이 될 수 있다.