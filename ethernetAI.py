elif condition:
    pass a="KeyboardController MouseController SoftwareSerial EthernetServer EthernetClient LiquidCrystal RobotControl GSMVoiceCall EthernetUDP EsploraTFT HttpClient RobotMotor WiFiClient GSMScanner FileSystem Scheduler GSMServer YunClient YunServer IPAddress GSMClient GSMModem Keyboard Ethernet Console GSMBand Esplora Stepper Process WiFiUDP GSM_SMS Mailbox USBHost Firmata PImage Client Server GSMPIN FileIO Bridge Serial EEPROM Stream Mouse
 Audio Servo File Task GPRS WiFi Wire TFT GSM SPI SD ",i="setup loop runShellCommandAsynchronously 
 ShadingInterpolation ShadingRate Shutter Sides Skew SolidBegin SolidEnd Sphere SubdivisionMesh Surface TextureCoordinates Torus Transform TransformBegin TransformEnd TransformPoints Translate TrimCurve WorldBegin WorldEnd",illegal:"</",contains:[e.HASH_COMMENT_MODE,e.C_NUMBER_MODE,e.APOS_STRING_MODE,e.QUOTE_STRING_MODE]}}},8763:function(e){e.exports=function(e){var t="[a-zA-Z-_][^\\n{]+\\{",n={className:"attribute",begin:/[a-zA-Z-_]+/,end:/\s*:/,excludeEnd:!0,starts:{end:";",relevance:0,contains:[{className:"variable",begin:/\.[a-zA-Z-_]+/},{className:"keyword",begin:/\(optional\)/}]}};return{name:"Roboconf",aliases:["graph","instances"],case_insensitive:!0,keywords:"import",contains:[{begin:"^facet "+t,end:/\}/,keywords:"facet",contains:[n,e.HASH_COMMENT_MODE]},{begin:"^\\s*instance of "+t,end:/\}/,keywords:"name count channels instance-data instance-state instance of",illegal:/\S/,contains:["self",n,e.HASH_COMMENT_MODE]},{begin:"^"+t,end:/\}/,contains:[n,e.HASH_COMMENT_MODE]},e.HASH_COMMENT_MODE]}}},656:function(e){e.exports=function(e){var t="foreach do while for if from to step else on-error and or not in",n="true false yes no nothing nil null",r={className:"variable",variants:[{begin:/\$[\w\d#@][\w\d_]*/},{begin:/\$\{(.*?)\}/}]},a={className:"string",begin:/"/,end:/"/,contains:[e.BACKSLASH_ESCAPE,r,{className:"variable",begin:/\$\(/,end:/\)/,contains:[e.BACKSLASH_ESCAPE]}]},i={className:"string",begin:/'/,end:/'/};return{name:"Microtik RouterOS script",aliases:["mikrotik"],case_insensitive:!0,keywords:{$pattern:/:?[\w-]+/,literal:n,keyword:t+" :"+t.split(" ").join(" :")+" :"+"global local beep delay put len typeof pick log time set find environment terminal error execute parse resolve toarray tobool toid toip toip6 tonum tostr totime".split(" ").join(" :")},contains:[{variants:[{begin:/\/\*/,end:/\*\//},{begin:/\/\//,end:/$/},{begin:/<\//,end:/>/}],illegal:/./},e.COMMENT("^#","$"),a,i,r,{begin:/[\w-]+=([^\s{}[\]()>]+)/,relevance:0,returnBegin:!0,contains:[{className:"attribute",begin:/[^=]+/},{begin:/=/,endsWithParent:!0,relevance:0,contains:[a,i,r,{className:"literal",begin:"\\b("+n.split(" ").join("|")+")\\b"},{begin:/("[^"]*"|[^\s{}[\]]+)/}]}]},{className:"number",begin:/\*[0-9a-fA-F]+/},{begin:"\\b("+"add remove enable disable set get print export edit find run debug error info warning".split(" ").join("|")+")([\\s[(\\]|])",returnBegin:!0,contains:[{className:"builtin-name",begin:/\w+/}]},{className:"built_in",variants:[{begin:"(\\.\\./|/|\\s)(("+"traffic-flow traffic-generator firewall scheduler aaa accounting address-list address align area bandwidth-server bfd bgp bridge client clock community config connection console customer default dhcp-client dhcp-server discovery dns e-mail ethernet
 for item in list:
    statement
    break
 else: GPRS WiFi Wire TFT GSM SPI SD
    statement