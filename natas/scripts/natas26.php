<?php 
base64_encode(serialize(base64_encode(serialize("<?php passthru('echo HELLO'); ?>"))));

?>
