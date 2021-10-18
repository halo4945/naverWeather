from naverWeather import * #naverWeather 모듈 import
l = naverWeather.map_cityNum.keys() # l에 key값들 리스트 저장
print(naverWeather().getWeather()) #?
for s in l :#iterator
    print(naverWeather(s).getWeather())
