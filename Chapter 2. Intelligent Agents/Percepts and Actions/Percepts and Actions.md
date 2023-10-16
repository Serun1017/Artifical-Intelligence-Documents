
---
- 에이전트는 [[Percepts(인식)]]과 [[Actions(행동)]] 과정으로 작동한다.
- 아래와 같이 청소기 Agents의 경우 가지게 되는 Percepts와 Actions은 다음과 같다.
![[Percepts and Actions.png]]

- 해당 Percepts를 통해 연결되는 Actions를 도출하는 과정은 다음과 같다.
![[Percepts and Actions2.png]]

- Percept Sequence가 Agent Function의 입력으로 들어오면 Action이 결과로 나오게 된다. 즉, 위 표에 따르면 [A, Clean] (방 A에 있는데 그 방이 깨끗하면) -> Right(방 B로 이동해라) 라고 정의될 수 있다.

- 이 같이 표를 통해 Agent Function을 정의하게 되면 모든 가능한 percept sequence에 대해 정의해주어야 하며 그랬을 때 비로소 Deterministic(결정적) 하다고 한다.
- 결정적이라는 것은 Agent가 어떤 state에 있을 때 다음에 취해야 할 행동이 100% 결정되어 있다는 것을 의미하며, 반대로 확률적으로 결정되는 모델을 Stochastic model이라 한다.
