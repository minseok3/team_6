def check_concentration(gas_name, concentration):
    legal_limits = {
        'NO2': 0.03,  # 이산화질소(ppm)
        'CO': 9,  # 일산화탄소(ppm)
        'SO2': 0.02,  # 아황산가스(ppm)
    }

    if gas_name in legal_limits:
        legal_limit = legal_limits[gas_name]
        if concentration <= legal_limit:
            print(f"입력한 {gas_name} 농도는 안전 기준에 도달했습니다.")
        else:
            print(f"입력한 {gas_name} 농도는 안전 기준을 초과했습니다.")
    else:
        print(f"{gas_name}에 대한 안전 기준이 없습니다.")


# 사용자가 입력할 가스 선택
selected_gases = ['NO2', 'CO', 'SO2']
print("다음 중 하나를 선택하여 농도를 입력하세요:", selected_gases)

while True:
    gas_name = input("가스 이름을 입력하세요 (종료하려면 'exit' 입력): ")

    if gas_name.lower() == 'exit':
        print("프로그램을 종료합니다.")
        break

    if gas_name in selected_gases:
        try:
            concentration = float(input(f"{gas_name} 농도를 입력하세요 (ppm 단위): "))
            check_concentration(gas_name, concentration)
        except ValueError:
            print("유효한 숫자를 입력하세요.")
    else:
        print("유효한 가스 이름을 입력하세요.")