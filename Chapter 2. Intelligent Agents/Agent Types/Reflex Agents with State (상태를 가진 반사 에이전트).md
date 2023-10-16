
---
Reflex Agents with State (상태를 가진 반사 에이전트)는 현재 상태 뿐만 아니라 환경의 이력을 고려하여 행동을 선택한다. 에이전트의 "상태"는 환경에서 수집한 정보와 이전 상태를 나타낸다. 상태를 고려함으로써 에이전트는 조금 더 복잡한 환경에서 효과적으로 작동할 수 있다.

![[Reflex Agents with State.png]]

---
# 예시

- Reflex Vacuum Agent
  - static으로 Reflex Vacuum Agent의 현재 위치를 지속적으로 저장하고 주변 상태를 계속해서 인식하며 status를 업데이트 한다.
  - 만약 status가 Dirty이면 그에 따른 Action을 수행한다.
  - 그 외의 경우 계속 환경을 인식하고 업데이트하며 Action을 수행한다.
![[Reflex Agents with State_Example.png]]