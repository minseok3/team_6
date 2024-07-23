def check_gas_levels(hc, o2, co2, co, h2s):
    # 기준 수치 설정
    thresholds = {
        "HC": 25,  # 인화성가스
        "O2": (18, 23.5),  # 산소
        "CO2": 1.5,  # 탄산가스
        "CO": 30,  # 일산화탄소
        "H2S": 10  # 황화수소
    }

    # 위험도 평가
    warnings = []

    # 인화성가스 체크
    if hc > thresholds["HC"]:
        warnings.append("인화성가스(HC) 수치가 기준을 초과했습니다.")

    # 산소 체크
    if o2 < thresholds["O2"][0] or o2 > thresholds["O2"][1]:
        warnings.append("산소(O2) 수치가 기준을 초과했습니다.")

    # 탄산가스 체크
    if co2 > thresholds["CO2"]:
        warnings.append("탄산가스(CO2) 수치가 기준을 초과했습니다.")

    # 일산화탄소 체크
    if co > thresholds["CO"]:
        warnings.append("일산화탄소(CO) 수치가 기준을 초과했습니다.")

    # 황화수소 체크
    if h2s > thresholds["H2S"]:
        warnings.append("황화수소(H2S) 수치가 기준을 초과했습니다.")

    # 경고 메시지 출력
    if warnings:
        print("경고! 다음 수치가 기준을 초과했습니다:")
        for warning in warnings:
            print(f"- {warning}")
    elif


    else:
        print("모든 수치가 안전 기준 이내입니다.")


# 사용자 입력 예시
hc_input = float(input("인화성가스(HC) 수치를 입력하세요 (%): "))
o2_input = float(input("산소(O2) 수치를 입력하세요 (%): "))
co2_input = float(input("탄산가스(CO2) 수치를 입력하세요 (%): "))
co_input = float(input("일산화탄소(CO) 수치를 입력하세요 (ppm): "))
h2s_input = float(input("황화수소(H2S) 수치를 입력하세요 (ppm): "))

# 가스 수치 체크
check_gas_levels(hc_input, o2_input, co2_input, co_input, h2s_input)