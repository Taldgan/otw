<?php
function xor_encrypt($text) {
	$key = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw');
	$outText = '';

 	// Iterate through each character
	for($i=0;$i<strlen($text);$i++) {
		$outText .= $text[$i] ^ $key[$i % strlen($key)];
 	}
  	return $outText;
}
$data = array('showpassword'=>'no', 'bgcolor'=>'#ffffff');
print xor_encrypt(json_encode($data))
?>
