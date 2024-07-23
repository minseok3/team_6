def check_concentration(gas_name, concentration):
    legal_limits = {
        'NO2': 0.03,  # 이산화질소 기준 농도 (ppm)
        'CO': 9,  # 일산화탄소 기준 농도 (ppm)
        'SO2': 0.02  # 아황산가스 기준 농도 (ppm)
    }

    if gas_name in legal_limits:
        legal_limit = legal_limits[gas_name]
        if concentration <= legal_limit:
            print(f"입력한 {gas_name} 농도는 안전 기준에 도달했습니다.")
        else:
            print(f"입력한 {gas_name} 농도는 안전 기준을 초과했습니다.")
    else:
        print(f"{gas_name}는(은) 유효한 유해가스가 아닙니다.")


# 선택할 수 있는 유해가스 리스트
available_gases = ['NO2', 'CO', 'SO2']

# 사용자에게 선택받기
print("선택할 수 있는 유해가스: ", available_gases)
selected_gas = input("측정하고자 하는 유해가스를 선택하세요: ")

if selected_gas in available_gases:
    try:
        concentration = float(input(f"{selected_gas} 농도를 입력하세요 (ppm 단위): "))
        check_concentration(selected_gas, concentration)
    except ValueError:
        print("유효한 숫자를 입력하세요.")
else:
    print("선택한 유해가스가 올바르지 않습니다.")