"""
KY-026 불꽃 센서 기본 사용 예제

이 예제는 아두이노 코드를 ESP32 S3 마이크로파이썬으로 포팅한 것입니다.
원본 아두이노 코드와 동일한 동작을 수행합니다.

연결:
- 아날로그 핀: GPIO 9 (A0에 해당)
- 디지털 핀: GPIO 10
"""

from ky026_flame_sensor import KY026FlameSensor
import time

# 핀 설정 (ESP32 S3 기준)
ANALOG_PIN = 9     # 아날로그 입력 핀
DIGITAL_PIN = 10   # 디지털 입력 핀

def main():
    """
    메인 함수 - 아두이노 코드와 동일한 동작
    """
    print("KY-026 불꽃 센서 테스트 시작")
    print("아날로그 핀: GPIO {}".format(ANALOG_PIN))
    print("디지털 핀: GPIO {}".format(DIGITAL_PIN))
    print("---")
    
    # 센서 객체 생성
    flame_sensor = KY026FlameSensor(ANALOG_PIN, DIGITAL_PIN)
    
    try:
        while True:
            # 아날로그 값 읽기
            sensor_value = flame_sensor.read_analog()
            
            # 디지털 값 읽기
            digital_val = flame_sensor.read_digital()
            
            # 센서 값 출력 (아두이노 코드와 동일)
            print("센서 값: {}".format(sensor_value))
            print("디지털 값: {}".format("감지됨" if digital_val else "감지 안됨"))
            
            # 500ms 대기 (아두이노 코드와 동일)
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("프로그램 종료")

if __name__ == "__main__":
    main()
