# <유농알>

**: 파이썬을 이용한 유해가스농도 측정 자동 계산기**

유농알은 밀폐공간에서의 유해가스 사용 작업을 위해 개발된 애플리케이션으로, 근로자가 착용하는 가스 농도 측정 기기를 통해 산소, 일산화탄소, 탄산가스, 황화수소, 탄화수소를 측정합니다.

농도가 기준을 초과하면 주의 및 경고 알림을 제공하여 질식, 발작, 혼절 등의 위험을 예방하며, 작업장의 유해가스 농도를 안전 수준으로 유지합니다.

개발 계획에는 각 유해가스의 측정된 수치를 입력 변수로 활용하고, 이를 기준으로 정상, 주의, 경고를 알리는 함수를 개발했습니다.

**허용범위 :**

탄화수소 (HC): 25 ppm 미만

산소 (O2): 18 ~ 23.5 %

이산화탄소(탄산가스) (CO2): 1.5 ppm 미만

일산화탄소 (CO): 9 ppm 미만

황화수소 (H2S): 10 ppm 미만
어플리케이션 목적

![image](https://github.com/user-attachments/assets/f2bffa3e-7f2d-4202-8202-9e0e02326d2d) 

1.유해가스 농도를 자동으로 측정하고 경고하는 것을 목적으로 한다.
  어플리케이션 네이밍의 의미

2.'유농알'은 '유해가스 농도 측정 알리미'의 줄임말이다.

3.어플리케이션의 활용 가치

  -a. 밀폐공간에서 작업하는 기업과 근로자를 대상으로 한다
  
  -b. 다양한 유해가스의 농도를 측정하여, 정해진 기준을 초과할 경우 경고를 발생시킨다.
  
  -c. 근로자를 유해가스로부터 보호하고 작업장의 안전을 유지한다.

4. 어플리케이션 개발 계획

  a. 입력 변수는 각 유해가스의 측정된 수치이다.
  
  b. 개발된 함수는 입력된 수치가 기준을 초과할 경우 경고를 알리는 역할을 한다.
  
  c. 연산은 조건문, 반복문, 함수 등을 활용하여 수행된다.

5. 어플리케이션 개발 과정

  a. 각 함수는 사용자로부터 가스 종류와 농도 값을 받아들이고, 정해진 기준을 초과하는지 평가한다.
  
  b. 발생한 에러는 산소의 농도 범위와 기준 재분류 시 발생했으며, if 문과 elif 문을 추가하여 해결했다.
  
  c. 해결책 적용 후 어플리케이션이 정상적으로 작동하게 되었다.
