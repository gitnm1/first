import socket
# from threading import Thread
import sys

HOST = '127.0.0.1'
PORT = 8888


# 이미지 받는 함수
def read_image(sock, name):
    print("들어욤")
    # 사이즈 받기
    size = sock.recv(5)
    print(size)
    int_size = int.from_bytes(size, "little")
    print(int_size)
    type(int_size)
    print("여기 옴?")

    # 이미지 받기
    file = sock.recv(int_size)

    with open('C:/Users/2021j/Pictures/' + name+ '.png', 'wb') as f:
        try:
            f.write(file)
            print('파일 받기 완료. 전송량 %d' % size)
        except Exception as ex:
            print("파일 에러 %s" % ex)


def Run():
    print(sys.version)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print("hello, word!")
        print("연결")
        name = input('저장할 파일 이름 ')

        # 이름 보내기
        sock.send(name.encode())
        # 서버에서 잘 받았는지 받기
        t_read = sock.recv(30)
        t_data = t_read.decode()
        print("받은 데이터 %s" % t_data)

        # 이미지 받는 함수
        read_image(sock, name)


Run()
