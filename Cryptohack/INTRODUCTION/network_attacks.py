from telnetlib import Telnet

jsonMessage = '{"buy":"flag"}'

if __name__ == '__main__':
    with Telnet('socket.cryptohack.org', 11112) as tn:
        tn.write(jsonMessage.encode('ascii'))
        print(tn.read_all().decode('ascii'))
