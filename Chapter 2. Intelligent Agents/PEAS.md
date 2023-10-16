
---
PEAS는 에이전트의 동작과 행동을 이해하고 모델링하는데 사용되며, 에이전트의 목적과 목표를 멍확하게 정의하는데 도움이 된다.
PEAS는 에이전트의 시스템 구성을 명확히 정의하고, 에이전트의 목적, 동작 및 평가 척도를 이해하는데 도움을 주는 중요한 도구이다. PEAS를 사용하면 인공 지능 시스템의 목표와 동작을 설계하고 분석하는데 도움이 된다.

---
# 구성 요소

## 1. Performance measure (성능 측정)

- "Performance measure"는 에이전트의 작업을 평가하고 성공 또는 실패를 판단하기 위한 척도 또는 지표이다.
- 에이전트가 목표를 달성하거나 주어진 작업을 얼마나 효과적으로 수행하는 지를 나타내며, 이를 통해 에이전트의 성과를 측정한다.
## 2. Environment (환경)

- "Environment"는 에이전트가 상호작용하는 외부 세계 또는 컨텍스트를 나타낸다.
- 에이전트는 환경으로부터 정보를 수집하고 환경에 영향을 미친다. 환경은 에이전트의 작업 공간으로, 작업을 수행하거나 목표를 달성하기 위한 상황을 제공한다.
## 3. Actuators (행동 수행 장치)

- "Actuators"는 에이전트가 환경과 상호작용하고 환경에 영향을 미치기 위해 사용하는 출력 장치나 수단을 나타낸다.
- 에이전트의 행동은 Actuators를 통해 환경에 반영된다.
## 4. Sensors (센서)

- "Sensors"는 에이전트가 환경으로부터 정보를 수집하고 Percepts(인식)을 생성하는데 사용되는 입력 장치 또는 수단이다.
- 센서는 에이전트가 주어진 상황을 인식하고 정보를 수집하는 데 필요한 도구이다.

---
# 예시

## The Task of designing an automated taxi

### 1. Performance measure
   - safety, destination, profits, legality, comfort ...
### 2. Environment
   - US streets / freeways, traffic, pedestrians, weather ...
### 3. Actuators
   - steering, accelerator, brake, horn, speaker / display ...
### 4. Sensors
   - video, accelerometers, gauges, engine sensors, keyboard, GPS ...

## Internet Shopping Agent

### 1. Performance measure
   - price, quality, appropriateness, efficiency ...
### 2. Environment
   - current and future WWW sites, vendors, shippers ...
### 3. Actuators
   - display to user, follow URL, fill in form ...
### 4. Sensors
   - HTML pages (text, graphics, scripts ...)