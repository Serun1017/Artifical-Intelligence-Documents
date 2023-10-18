
---
문제 해결 에이전트 (Problem-Solving Agent)는 인공지능 분야에서 사용되는 에이전트로, 주어진 문제나 작업을 해결하고 최적의 해결책을 찾는데 특화된 컴퓨터 프로그램 또는 시스템을 나타낸다. 이러한 에이전트는 다양한 작업을 수행하고, 주어진 문제를 분석하여 해결책을 찾는 데 중점을 둔다.

![[Problem-Solving Agents.png]]

문제 해결 에이전트는 위와 같이 현재 상태(State)에 의한 목표(Goal) 설정, 현재 상태(State)와 목표(Goal)에 의한 문제(Problem) 설정, 문제에 대한 해결책(Sequence) 탐색(Search) 과정을 반복하여 가장 최적의 해결책(Sequence)을 찾고 이를 수행(Action)한다. 문제 해결 에이전트는 이 과정을 반복함으로서 일련의 최적의 해결 순서(Sequence)의 집합들을 통해 수행(Action)함으로써 최적의 해결책을 찾는다.

---
# Problem (문제)
- "Problem (문제)"은 문제 해결 에이전트가 해결하려는 구체적인 작업 또는 과제를 나타낸다.
- 문제에는 초기 상태 (Initial State), 목표 상태 (Goal Test), 가능한 액션 집합 (Actions), 문제의 제약 조건 (Path Cost), 목표 달성 방법(Transition Model) 등이 포함된다.
- 문제를 명확하게 정의하는 것은 문제 해결 에이전트가 올바른 방식으로 작동하기 위한 핵심 단계이다.

---
# Goal (목표)
- "Goal (목표)"은 문제 해결 에이전트가 달성하려는 원하는 상태나 목표를 나타낸다.
- 목표는 문제 해결 에이전트가 초기 상태에서 목표 상태로 이동하는 것을 나타내며, 목표 달성을 위한 기준으로 작용한다.
- 에이전트의 목표는 문제에 따라 다를 수 있으머, 이를 달성하기 위한 해결책을 찾는 것이 주요 목표이다.

---
# State (상태)
- "State (상태)"는 문제 해결 과정 중에서 시스템 또는 환경의 특정 상태를 나타낸다.
- 상태는 에이전트가 문제 해결 과정에서 존재하는 특정 상황이며, 주어진 상태에서 가능한 액션을 수행할 수 있다.
- 상태는 초기 상태에서 시작하여 액션을 통해 변경되며, 목표 상태에 도달하기 위해 연결된다.

---
# Sequence (순서)
- "Sequence (순서)"는 문제 해결 에이전트가 상태와 액션을 연결하여 문제를 해결하기 위한 일련의 단골과 액션 순서를 의미한다.
- 이러한 순서는 상태 공간 (State Space)을 탐색하고 목표 상태에 도달하기 위한 경로를 나타낸다.
- 문제 해결 과정에서 정확한 순서를 찾는 것은 목표 달성을 가능하게 한다.

---
# Example: Romania

- 아래와 같은 지도(그래프)가 주어졌을 때, Arad에서 Bucharest를 가기 위한 문제 해결 에이전트(Problem-Solving Agent)를 만들기 위한 Problem, Goal, State, Sequence는 다음과 같다.
![[Problem-Solving Agents_Example.png]]

1. Formulate Goal
   - Be in Bucharaest
2. Formulate Problem
   - State: Various Cities
   - Actions: Drive between Cities
3. Find Solution
   - Sequence of Cities. 
     - example: Arad, Sibiu, Fagaras, Bucharest