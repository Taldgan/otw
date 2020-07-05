<?php
function xor_encrypt($in) {
    $key = substr(exec('php xordecrypt.php'), 0, 4);
    $text = $in; 
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
	    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$payload = array( "showpassword"=>"yes","bgcolor"=>"#ffffff");
$test = base64_encode(xor_encrypt(json_encode($payload)));
print $test;

?>
