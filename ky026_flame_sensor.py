"""
KY-026 불꽃 센서 모듈을 위한 ESP32 S3 마이크로파이썬 라이브러리

이 라이브러리는 KY-026 불꽃 센서를 ESP32 S3에서 사용할 수 있도록 합니다.
아날로그와 디지털 출력을 모두 지원합니다.

작성자: ESP32 S3 마이크로파이썬 포팅
원본: 아두이노 센서 37종 키트 - 불꽃 감지센서 모듈(FLAME KY-026)
"""

import machine
import time
from machine import Pin, ADC

class KY026FlameSensor:
    """
    KY-026 불꽃 센서 클래스
    
    아날로그 핀과 디지털 핀을 사용하여 불꽃을 감지합니다.
    """
    
    def __init__(self, analog_pin, digital_pin, led_pin=None):
        """
        KY-026 불꽃 센서 초기화
        
        Args:
            analog_pin (int): 아날로그 입력 핀 번호
            digital_pin (int): 디지털 입력 핀 번호  
            led_pin (int, optional): LED 출력 핀 번호
        """
        self.analog_pin = analog_pin
        self.digital_pin = digital_pin
        self.led_pin = led_pin
        
        # 아날로그 핀 설정
        self.adc = ADC(Pin(analog_pin))
        self.adc.atten(ADC.ATTN_11DB)  # 0-3.3V 범위
        
        # 디지털 핀 설정
        self.digital_input = Pin(digital_pin, Pin.IN)
        
        # LED 핀 설정 (선택사항)
        if led_pin is not None:
            self.led = Pin(led_pin, Pin.OUT)
            self.led.value(0)
        else:
            self.led = None
            
        # 센서 값 저장 변수
        self.sensor_value = 0
        
    def read_analog(self):
        """
        아날로그 센서 값 읽기
        
        Returns:
            int: 0-4095 범위의 아날로그 값
        """
        self.sensor_value = self.adc.read()
        return self.sensor_value
    
    def read_digital(self):
        """
        디지털 센서 값 읽기
        
        Returns:
            bool: True (불꽃 감지됨), False (불꽃 감지 안됨)
        """
        return bool(self.digital_input.value())
    
    def read_sensor(self):
        """
        센서 값 읽기 (아날로그와 디지털 모두)
        
        Returns:
            tuple: (analog_value, digital_value)
        """
        analog_val = self.read_analog()
        digital_val = self.read_digital()
        return analog_val, digital_val
    
    def set_led(self, state):
        """
        LED 제어
        
        Args:
            state (bool): True (켜기), False (끄기)
        """
        if self.led is not None:
            self.led.value(1 if state else 0)
    
    def auto_led_control(self):
        """
        디지털 센서 값에 따라 LED 자동 제어
        
        Returns:
            bool: 디지털 센서 값
        """
        digital_val = self.read_digital()
        self.set_led(digital_val)
        return digital_val
    
    def get_sensor_info(self):
        """
        센서 정보 반환
        
        Returns:
            dict: 센서 정보 딕셔너리
        """
        analog_val, digital_val = self.read_sensor()
        return {
            'analog_value': analog_val,
            'digital_value': digital_val,
            'flame_detected': digital_val,
            'analog_pin': self.analog_pin,
            'digital_pin': self.digital_pin,
            'led_pin': self.led_pin
        }
    
    def print_sensor_data(self):
        """
        센서 데이터를 시리얼로 출력 (디버깅용)
        """
        analog_val, digital_val = self.read_sensor()
        print("센서 값: {}".format(analog_val))
        print("불꽃 감지: {}".format("감지됨" if digital_val else "감지 안됨"))
        print("---")
