"""
KY-026 불꽃 센서 임계값 기반 감지 예제

이 예제는 아날로그 값을 이용한 임계값 기반 불꽃 감지를 보여줍니다.
"""

from ky026_flame_sensor import KY026FlameSensor
import time

# 핀 설정
ANALOG_PIN = 9
DIGITAL_PIN = 10

# 임계값 설정 (0-4095 범위에서 조정)
FLAME_THRESHOLD = 2000  # 이 값보다 높으면 불꽃으로 판단

def main():
    """
    임계값 기반 불꽃 감지 예제
    """
    print("KY-026 불꽃 센서 임계값 기반 감지")
    print("임계값: {}".format(FLAME_THRESHOLD))
    print("=" * 40)
    
    # 센서 객체 생성
    flame_sensor = KY026FlameSensor(ANALOG_PIN, DIGITAL_PIN)
    
    # 초기 센서 값 측정 (기준값 설정용)
    print("초기 센서 값 측정 중...")
    baseline_values = []
    for i in range(10):
        val = flame_sensor.read_analog()
        baseline_values.append(val)
        print("  측정 {}: {}".format(i + 1, val))
        time.sleep(0.1)
    
    baseline_avg = sum(baseline_values) / len(baseline_values)
    print("기준값 평균: {:.1f}".format(baseline_avg))
    print()
    
    try:
        while True:
            # 센서 값 읽기
            analog_val, digital_val = flame_sensor.read_sensor()
            
            # 임계값 기반 판단
            threshold_detected = analog_val > FLAME_THRESHOLD
            
            # 불꽃 감지 상태 표시 (임계값 기반)
            
            # 결과 출력
            print("아날로그: {:4d} | 디지털: {} | 임계값감지: {} | 기준값차이: {:+.1f}".format(
                analog_val,
                "감지" if digital_val else "없음",
                "감지" if threshold_detected else "없음",
                analog_val - baseline_avg
            ))
            
            # 불꽃 감지 시 경고
            if threshold_detected or digital_val:
                print("  ⚠️  불꽃 감지됨!")
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("프로그램 종료")

if __name__ == "__main__":
    main()
