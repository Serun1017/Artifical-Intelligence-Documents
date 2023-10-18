
---
문제의 유형 (Problem Types)은 문제의 상태 공간(State Space), 관측 가능성(Observable), 확정성(Determinisitic)에 따라 다양한 유형으로 구분할 수 있다.
각 문제 유형은 다른 문제 해결 전략과 기술을 필요로 하며, 에이전트가 목표를 달성하기 위한 적절한 방법을 선택하고 적용하게 된다.

---
# [[Single-State Problem (단일 상태 문제)]]

- 단일 상태 문제 (Single-State Problem)은 에이전트가 어떤 상태에 있을 것인지 정확히 알 수 있다. (Fully Observable, 완전 관찰 가능)
- 단일 상태 문제에서 목표는 초기 상태에서 목표 상태로 가는 단일 순차적인 해결책을 찾는 것이다. (Deterministic, 확정적)
---
# Conformant Problem (준수 문제)

- 준수 문제 (Conformant Problem)에서 에이전트는 현재 어디에 있는지 모를 수 있다. (Non-Observable, 비 관찰 가능)
- 준수 문제에서 해결책은 에이전트가 목표 상태에 도달하거나 어떤 상태로 이동해야 하는 순차적인 행동 계획이다.
---
# Contingency Problem (위험 문제)

- 위험 문제 (Contingency Problem)에서 에이전트가 상태 및 환경에 대한 불확실성을 가질 수 있다. (Nondeterministic, 비 결정적)
- 위험 문제에서 에이전트의 인식은 환경의 변화로부터 새로운 정보를 얻는다. (Partially Observable, 부분적 관찰 가능)
- 해결책은 환경의 변화에 따라 조정되는 "Contingent Plan" 또는 "Policy" 이다. 때로는 탐색과 실행이 교차될 수 있다.

---
# Exploration Problem (탐사 문제)

- 탐사 문제 (Exploration Problem)에서 에이전트는 전체 상태 공간에 대한 정보를 갖고 있지 않다. (Unknown State Space, 알 수 없는 상태 공간)
- 탐사 문제에서 에이전트는 실시간으로 환경을 탐사하고 상태 및 행동에 대한 정보를 획득하며, 최적의 해결책을 찾는 데 필요한 탐색을 수행한다.

---
# Example: Vacuum World

- 다음의 Vacuum Agent의 Problem Types별 문제 인식 및 해결 탐색 방식은 다음과 같다.
![[Problem Types_Example.png]]

1. Single-State Problem (단일 상태 문제)
   - 단일 상태 문제에서는 처음 시작 지점을 정한다. 
   - 만약 위의 상태 중 5 번의 상태가 처음 시작 지점이라고 한다면 단일 상태 문제이므로 해결 방법(Solution)은 [Right, Suck] 이다.
   - 단일 상태 문제로 문제를 인식하고 해결하기 위해서는 반드시 처음 시작 지점을 에이전트가 알고 있어야 한다. 또한 처음 시작 지점에서 결정된 해결 방법(Solution)에 따라 해당 위치에 먼지가 없어도 반드시 [Suck]을 수행한다.
2. Conformant Problem (준수 문제)
   - 준수 문제에서는 에이전트의 현재 위치를 완전히 알 수 없다. 따라서 시작 지점은 {1, 2, 3, 4, 5, 6, 6, 7, 8} 중 하나 이다.
   - 준수 문제에서 해결책(Solution)은 목표 상태에 도달하거나 어떤 상태로 이동해야 하는 순차적인 행동 계획이므로 [Right, Suck, Left, Suck] 이다.
   - 준수 문제로 문제를 인식하고 해결한다면 이동한 상태의 환경을 고려하지 않는다. 따라서 이동한 위치의 먼지가 없어도 반드시 [Suck]을 수행한다.
3. Contingency Problem (위험 문제)
   - 위험 문제에서 에이전트는 환경의 상태 및 변화를 알 수 있다. 또한 부분적으로 현재의 위치를 알 수 있다.
   - 위험 문제에서 해결책(Solution)은 에이전트의 상태에 의해 결정될 수 있다. 때문에 현재 상태가 5 번의 상태라고 할 때, 해결책(Solution)은 [Right, if dirt then Suck] 이다.
   - 위험 문제로 문제를 인식하고 해결한다면 에이전트가 현재 상태를 부분적으로 인식하고 Action을 수행한다. 따라서 현재 상태를 5 번 상태라고 에이전트가 인식한 후, [Right]을 수행한 후, 해당 환경의 [dirt]이 있는 지 확인한 후 있을 경우 [Suck]을 수행한다.
