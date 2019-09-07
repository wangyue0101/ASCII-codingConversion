# ASCII-codingConversion
ASCII编码转换脚本,用于编码或解码字符

当前支持的编码类型包括：
    八进制，十进制，HTML十进制，十六进制，HTML十六进制，URL
    
当前支持的解码类型包括：
    十进制，HTML十进制，十六进制，HTML十六进制，URL

Example:

    python onetothree.py -e "html_hex" -t "http://www.baidu.com"
    &#x68;&#x74;&#x74;&#x70;&#x3A;&#x2F;&#x2F;&#x77;&#x77;&#x77;&#x2E;&#x62;&#x61;&#x69;&#x64;&#x75;&#x2E;&#x63;&#x6F;&#x6D;

    python onetothree.py -d "de_html_hex" -t "&#x68;&#x74;&#x74;&#x70;&#x3A;&#x2F;&#x2F;&#x77;&#x77;&#x77;&#x2E;&#x62;&#x61;&#x69;&#x64;&#x75;&#x2E;&#x63;&#x6F;&#x6D;"
    http://www.baidu.com
    
    
后续考虑增加JS编码解码
