<html>
<head>
    <title>Pie Flavored Pi</title>
    <link rel="stylesheet" type="text/css" href="../style/main.css" />
</head>
<body>

    <h1>Eventually the top post of each day from <a href="http://www.reddit.com/r/AnimalTextGifs">/r/AnimalTextGifs</a> will be uploaded here</h1>

<?php
	$fh = fopen("posts.txt", 'r');
    $pageText = fread($fh, 25000);
	echo nl2br($pageText);
?>

<iframe src="http://i.imgur.com/R8qHgDD.gifv" name="content" width="100%" height="70%"></iframe>


</body>
</html>
