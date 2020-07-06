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

