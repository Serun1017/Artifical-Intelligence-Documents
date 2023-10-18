
---
State Space (상태 공간)은 문제 해결에서 중요한 개념으로, 문제에 대한 가능한 모든 상태의 집합을 나타낸다. 각 상태는 문제의 특정 순간 또는 상황을 대표하며, 상태 공간은 이러한 상태들 간의 관계와 전이를 정의한다.
상태 공간 모델은 문제의 초기 상태에서 시작하여 목표 상태까지 도달하기 위한 경로를 찾는데 사용된다.
상태 공간 모델을 사용하여 에이전트는 초기 상태에서 시작하여 목표 상태로 이동하기 위한 가장 효율적인 경로 또는 액션 순서를 찾는다. 이것은 다양한 문제 해결 작업에서 중요한 개념이며, 다양한 알고리즘 및 기술을 사용하여 상태 공간을 탐색하고 해결책을 찾는다.

---
# 주요 원칙 및 고려 사항

- 상태 공간 (State Space)은 문제 해결에 사용되는 추상화된 표현이며, 현실 세계의 복잡성을 처리하고 문제를 해결하기 위해 필요한 [[Abstraction(추상화)]] 과정을 나타낸다.

1. 현실 세계의 복잡성
   - 현실 세계는 매우 복잡하며, 모든 세부사항을 정확하게 모델링하기는 어렵다. 따라서 문제 해결을 위해 상태 공간을 추상화해야 한다.
2. (추상화된) 상태와 액션
   - (추상화된) 상태는 실제 세계의 상태 집합을 나타낸다. 이는 실제 상태를 단순화하고 일반화한 것이다.
   - (추상화된) 액션은 실제 액션의 복잡한 조합을 나타낸다. 예를 들어 "Arad->Zerind"는 여러 경로, 우회 경로, 휴식 지점 등의 복잡한 조합을 대표한다.
3. (추상화된) 해결책
   - (추상화된) 해결책은 현실 세계에서 해결책이 되는 실제 경로 집합을 나타낸다. 추상화된 문제의 해결책은 실제 세계에서 실행 가능해야 한다.
4. 액션의 단순화
   - 추상화된 상태 공간은 원래 문제보다 "쉬운" 문제로 간주된다. 따라서 추상화된 액션은 원래 문제보다 단순하거나 이해하기 쉬워야 한다.

---
# Example: Vacuum world state space graph

- 다음의 Vacuum Agent의 State Space를 Graph로 그리면 다음과 같다.
![[State Space_Example.png]]

1. State
   - Integer dirt and robot Locations (ignore dirt amounts etc.)
2. Actions
   - *LEFT, RIGHT, SUCK, NoOp*
3. Goal Test
   - *Check No Dirt*
4. Path Cost
   - 1 per action (0 for *NoOp*)
---
# Example: The 8-puzzle

- 다음의 8-puzzle Agent의 State Space를 분석하면 다음과 같다.
![[State Space_Example2.png]]

1. States
   - Integer locations of tiles (ignore intermediate positions)
2. Actions
   - *Move Blank LEFT, RIGHT, UP, DOWN* (ignore unjamming etc.)
3. Goal Test
   - *Equals to Given Goal State*
4. Path Cost
   - 1 per move
----
# Example: Robotic Assembly

- 다음의 Robotic Assembly Agent의 State Space를 분석하면 다음과 같다.
![[State Space_Example3.png]]

1. States
   - Real-valued coordinates of robot joint angles
   - Parts of the object to be assembled
2. Actions
   - Continuous motions of robot joints
3. Goal Test
   - Complete Assembly with no robot included
4. Path Cost
   - Time to execute
