import pandas as pd

def check_concentration(gas_name, concentration):
    legal_limits = {
        "HC": 25,    # 인화성가스
        "O2": [18, 23.5],   # 산소
        "CO2": 1.5,   # 탄산가스
        "CO": 9,   # 일산화탄소
        "H2S": 10,   # 황화수소
    }

    if gas_name in legal_limits:
        legal_limit = legal_limits[gas_name]
        if gas_name != 'O2':
            if legal_limit * 0.85 < concentration < legal_limit:
                result = f"주의 : 입력한 {gas_name} 농도는 안전 기준 85%를 초과했습니다."
            elif concentration <= legal_limit:
                result = f"안전 : 입력한 {gas_name} 농도는 안전 기준에 부합합니다."
            else:
                result = f"위험 : {gas_name}의 농도는 안전 기준을 초과했습니다."
        else:
            if legal_limits["O2"][0] <= concentration < legal_limits["O2"][1]:
                result = f"안전 : 입력한 {gas_name} 농도는 안전 기준에 부합합니다."
            else:
                result = f"위험 : 입력한 {gas_name} 농도는 안전 기준을 초과했습니다."
    else:
        result = f"오류 : {gas_name}은(는) 유효하지 않은 가스 이름입니다."

    return result

# 사용자가 입력할 가스 선택
selected_gases = ['O2', 'CO', 'CO2', 'H2S', 'HC']
print("다음 중 하나를 선택하여 농도를 입력하세요:", selected_gases)

results = []

while True:
    gas_name = input("가스 이름을 입력하세요 (종료하려면 'exit' 입력): ")

    if gas_name.lower() == 'exit':
        print("프로그램을 종료합니다.")
        break

    if gas_name in selected_gases:
        try:
            concentration = float(input(f"{gas_name} 농도를 입력하세요 (ppm,% 단위): "))
            result = check_concentration(gas_name, concentration)
            results.append((gas_name, concentration, result))
        except ValueError:
            print("유효한 숫자를 입력하세요.")
    else:
        print("유효한 가스 이름을 입력하세요.")

# 전체 결과 출력
print("\n전체 결과:")
for gas_name, concentration, result in results:
    if gas_name == "O2":
        print(f"{result} 가스: {gas_name}, 농도: {concentration} %")
    else:
        print(f"{result} 가스: {gas_name}, 농도: {concentration} ppm")

# 결과를 DataFrame으로 변환하여 Excel 파일에 저장
try:
    df = pd.DataFrame(results, columns=['Gas', 'Concentration', 'Result'])
    df.to_excel('가스농도_결과.xlsx', index=False)
    print("Excel 파일로 저장했습니다.")
except Exception as e:
    print(f"Excel 파일 저장 중 오류가 발생했습니다: {e}")

print("프로그램을 종료했습니다.")