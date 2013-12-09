<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>Court Watch Program</title>

<link rel="stylesheet" type="text/css" href="style.css">

</head>

<body>

<div class="container">
  	<div class="headerRight">
  		<div class="headerLeft">
        <a href="form.html">New Form</a> &nbsp;&nbsp;&nbsp;
        <a href="upload.html">Upload</a> &nbsp;&nbsp;&nbsp; 
        <a href="search.html">Search</a>  &nbsp;&nbsp;&nbsp;
		<a href="data.html">Data</a>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <a href="logout.html">Log Out</a>
  		</div>
 	<a href="splash.html">COURT WATCH</a>
 	</div>

  	<div class="content">
  		<div class="searchcontent2">
  			<h3>Search Results</h3>

        <table width="100%" border="1px solid">
			<?php
			$con=mysqli_connect("url","user","pass","exceltable");
			// Check connection
			if (mysqli_connect_errno())
			  {
			  echo "Failed to connect to MySQL: " . mysqli_connect_error();
			  }

			$result = mysqli_query($con,"SELECT * FROM exceltable WHERE caseNumber LIKE '%term%'");

			echo "<table border='1'>
			<tr>
			<th>Form Number</th>
			<th>Voulenteer Number</th>
			<th>Case Number</th>
			</tr>";

			while($row = mysqli_fetch_array($result))
			  {
			  echo "<tr>";
			  echo "<td>" . $row['caseNumber'] . "</td>";
			  echo "<td>" . $row['formNumber'] . "</td>";
			  echo "<td>" . $row['caseNumber'] . "</td>";
			  echo "</tr>";
			  }
			echo "</table>";

			mysqli_close($con);
			?>
        </table>

  		</div>
	</div>
 </div>
</body>
</html>
