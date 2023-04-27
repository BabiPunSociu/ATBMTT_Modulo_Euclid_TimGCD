
# Thuat toan Euclid tìm UCLN
# Tinh chat:    GCD(a,b) = GCD(b, a mod b) với b<=a

def nhapSoTuNhien(mes):
    while True:
        a = input(mes)
        try:
            a = int(a) 
            if a >= 0: return a 
            else:
                print('Bạn phải nhập số tự nhiên.')
        except ValueError:
            print('Bạn phải nhập số tự nhiên.')


def GCD(a, b):
    A,B = 0,0   # khai bao bien
    # Đưa về A>=B
    if a>=b: A,B = a,b 
    else: A,B = b,a
    while True:
        if B==0: return A 
        r = A%B 
        A,B = B, r 

if __name__ == "__main__":
    while True:
        a = nhapSoTuNhien("Nhập số tự nhiên a = ")
        b = nhapSoTuNhien("Nhập số tự nhiên b = ")
        print('GCD(%d,%d) = %d'%(a, b, GCD(a,b)))
        print('Bạn muốn tiếp tục không? y-tiep tuc   n-thoat')
        if input('Lua chon cua ban la: ').upper().strip() == 'N':
            print('Tam biet')
            break 
        print('----------------------------------------------------------')