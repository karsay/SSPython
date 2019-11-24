import socket

target_host = "www.google.com"
target_port = 80

#ソケットオブジェクトの生成(ipv4,tcp)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#サーバへ接続
client.connect((target_host,target_port))

#データの送信
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#データの受信
responce = client.recv(4096)

print(responce)