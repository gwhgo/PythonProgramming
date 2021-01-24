def outahere():
    import os
    print('Byte os world')
    os._exit(99)
    prnt('Never reached')

if __name__ == '__main__':
    outahere()
