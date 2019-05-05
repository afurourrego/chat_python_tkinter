from client.startup_window import StartupGui

if __name__ == '__main__':
    f = open('/Users/afuro/Documents/GitHub/chat_python_tkinter/serverinfo', 'r')
    temp = f.readline().strip().split()
    ip = temp[1]
    temp = f.readline().strip().split()
    port = int(temp[1])
    start = StartupGui(ip, port)
    #input()
