"""
KY-026 불꽃 센서 고급 사용 예제

이 예제는 라이브러리의 모든 기능을 활용한 고급 사용법을 보여줍니다.
"""

from ky026_flame_sensor import KY026FlameSensor
import time

# 핀 설정
ANALOG_PIN = 9
DIGITAL_PIN = 10

def main():
    """
    고급 사용 예제
    """
    print("KY-026 불꽃 센서 고급 예제")
    print("=" * 30)
    
    # 센서 객체 생성
    flame_sensor = KY026FlameSensor(ANALOG_PIN, DIGITAL_PIN)
    
    # 센서 정보 출력
    sensor_info = flame_sensor.get_sensor_info()
    print("센서 설정 정보:")
    for key, value in sensor_info.items():
        print("  {}: {}".format(key, value))
    print()
    
    try:
        for i in range(20):  # 20번 반복
            print("측정 횟수: {}".format(i + 1))
            
            # 방법 1: 개별 읽기
            analog_val = flame_sensor.read_analog()
            digital_val = flame_sensor.read_digital()
            print("  아날로그 값: {}".format(analog_val))
            print("  디지털 값: {}".format(digital_val))
            
            # 방법 2: 한번에 읽기
            analog_val2, digital_val2 = flame_sensor.read_sensor()
            print("  한번에 읽기 - 아날로그: {}, 디지털: {}".format(analog_val2, digital_val2))
            
            # 방법 3: 디지털 값 읽기
            flame_detected = flame_sensor.read_digital()
            print("  불꽃 감지 상태: {}".format("감지됨" if flame_detected else "감지 안됨"))
            
            # 방법 4: 센서 정보 딕셔너리
            info = flame_sensor.get_sensor_info()
            print("  센서 정보: 아날로그={}, 디지털={}, 불꽃감지={}".format(
                info['analog_value'], 
                info['digital_value'], 
                info['flame_detected']
            ))
            
            print("-" * 20)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("프로그램 종료")

if __name__ == "__main__":
    main()
