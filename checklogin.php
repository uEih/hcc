<?php
	
	//opens database
   class MyDB extends SQLite3
   {
      function __construct()
      {
         $this->open('UserAccounts.db');
      }
   }
   $db = new MyDB();

   //username and pw from index.html
   $user = $_REQUEST['myusername'] ; 
   $pw = $_REQUEST['mypassword'] ;

   //if there is a database, it opens.
   if(!$db){
      echo $db->lastErrorMsg();
   } else {
      echo "Opened database successfully\n";
   }

   $result = $db->query("SELECT * FROM login WHERE user = '$user' AND password = '$pw'");
   $fromDB = $result->fetchArray();
   if ($fromDB['user'] == $user) {
     echo "It worked";
     header("location:splash.html");
   };

   if($fromDB['user'] != $user){
   	  header("location:index2.html");
      echo "It failed";
      exit;
   };

?>
