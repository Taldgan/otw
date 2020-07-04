<?php
function xor_encrypt($in) {
    $key = $in;
    $text = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
	    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
    $ah = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D');
    $test = xor_encrypt($ah);
    print $test;


?>
