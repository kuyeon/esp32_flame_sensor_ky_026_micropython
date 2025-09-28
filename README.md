# ESP32 S3 KY-026 불꽃 센서 마이크로파이썬 라이브러리

ESP32 S3에서 KY-026 불꽃 센서를 사용하기 위한 마이크로파이썬 라이브러리입니다.

> ⚠️ **주의**: 이 라이브러리는 아직 실제 하드웨어에서 테스트되지 않았습니다. 사용 전에 실제 환경에서 테스트해보시기 바랍니다.

## 개요

이 라이브러리는 아두이노용 KY-026 불꽃 센서 코드를 ESP32 S3 마이크로파이썬으로 포팅한 것입니다. 아날로그와 디지털 출력을 모두 지원하며, 간편한 API를 제공합니다.

## 특징

- 아날로그 및 디지털 센서 값 읽기
- 디지털 센서 값 읽기
- 임계값 기반 불꽃 감지
- 한글로 된 디버깅 출력
- 다양한 사용 예제 제공

## 하드웨어 연결

| KY-026 센서 | ESP32 S3 핀 | 설명 |
|-------------|-------------|------|
| VCC | 3.3V | 전원 |
| GND | GND | 그라운드 |
| A0 | GPIO 9 | 아날로그 출력 |
| D0 | GPIO 10 | 디지털 출력 |

## 파일 구조

```
├── ky026_flame_sensor.py    # 메인 라이브러리 파일
├── example_basic.py         # 기본 사용 예제 (아두이노 코드 포팅)
├── example_advanced.py      # 고급 사용 예제
├── example_threshold.py     # 임계값 기반 감지 예제
└── README.md               # 이 파일
```

## 설치 및 사용

1. `ky026_flame_sensor.py` 파일을 ESP32 S3에 업로드
2. 예제 파일 중 하나를 선택하여 실행

### 기본 사용법

```python
from ky026_flame_sensor import KY026FlameSensor

# 센서 객체 생성
flame_sensor = KY026FlameSensor(9, 10)  # 아날로그핀, 디지털핀

# 센서 값 읽기
analog_val, digital_val = flame_sensor.read_sensor()
print("아날로그 값: {}, 디지털 값: {}".format(analog_val, digital_val))

# 디지털 값 읽기
flame_detected = flame_sensor.read_digital()
```

## 예제 설명

### 1. example_basic.py
원본 아두이노 코드를 그대로 포팅한 기본 예제입니다. 아두이노 코드와 동일한 동작을 수행합니다.

### 2. example_advanced.py
라이브러리의 모든 기능을 활용한 고급 사용법을 보여줍니다.

### 3. example_threshold.py
아날로그 값을 이용한 임계값 기반 불꽃 감지 예제입니다.

## API 참조

### KY026FlameSensor 클래스

#### 생성자
```python
KY026FlameSensor(analog_pin, digital_pin, led_pin=None)
```

#### 주요 메서드

- `read_analog()`: 아날로그 센서 값 읽기 (0-4095)
- `read_digital()`: 디지털 센서 값 읽기 (True/False)
- `read_sensor()`: 아날로그와 디지털 값 모두 읽기
- `read_digital()`: 디지털 센서 값 읽기
- `get_sensor_info()`: 센서 정보 딕셔너리 반환
- `print_sensor_data()`: 센서 데이터 시리얼 출력

## 주의사항

- ESP32 S3의 ADC는 0-3.3V 범위에서 0-4095 값을 출력합니다
- 센서의 감도는 주변 환경에 따라 달라질 수 있습니다
- 임계값은 실제 환경에서 테스트하여 조정하세요

## 라이선스

이 프로젝트는 교육 목적으로 제작되었습니다.

## 원본 출처

아두이노 센서 37종 키트 - 불꽃 감지센서 모듈(FLAME KY-026)
작성자: COMPASS