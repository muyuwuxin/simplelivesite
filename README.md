#最小的直播后端
Django==1.10.5
用户通过register注册，然后用apply申请，申请完后，通过django admin设置允许直播，然后用户可以选择打开状态。当处于打开状态的时候可以进行直播。

#服务端
##直播地址
已验证
docker pull jasonrivers/nginx-rtmp
docker run -p 47621:1935 -p 12973:8080 jasonrivers/nginx-rtmp

rtmp://118.193.152.71:47621/live/mystream
http://118.193.152.71:12973/hls/mystream.m3u8

##通过websocket实现弹幕
https://github.com/ListFranz/websocketchatroom

