//json encode, then xorencrypt
<?php
function xor_encrypt($in) {
    $key = $in;
    $text = json_encode(array('{"showpassword":"yes","bgcolor":"#ffffff"}'));
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
	    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
    $key = substr(exec('php xordecrypt.php'), 0, 4);
    $test = xor_encrypt('qw8J');
    #$test = xor_encrypt($key);
    print base64_encode($test);
?>
