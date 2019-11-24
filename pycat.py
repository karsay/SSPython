import sys
import socket
import getopt
import threading
import subprocess

#グローバル変数の定義
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
  print("pycat python netcat tool")
  print("")
  print("Usage: pycat.py -t target_host -p port")
  print("-l --listen")
  print("-e --execute=file_to_run")
  print("-c --command")
  print("-u --upload=destination")
  print("")
  print("")
  print("Examples:")
  print("pycat. -t 192.168.1.0 -p 5555 -l -c")
  print("pycat. -t 192.168.1.0 -p 5555 -l -u c:\\target.exe")
  print("pycat. -t 192.168.1.0 -p 5555 -l -e \"cat /etc/passwd\"")
  print("echo 'ABCDEG' | ./pycat.py -t 192.168.11.12 -p 135")
  sys.exit()

def main():
  global listen
  global port
  global execute
  global command
  global upload_destination
  global target

  #実行時引数なければ使い方を表示
  if not len(sys.argv[1:]):
    usage()

  #コマンドラインオプションの読み込み
  try:
    opts, args = getopt.getopt(
      sys.argv[1:],
      "hle:t:p:cu:",
      ["help","listen","execute=","target=",
       "port=","command","upload="])
  except getopt.GetoptError as err:
    print(err)
    usage()