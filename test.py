import numpy as np

def Chuanhoa(X, min_val = 0, max_val = 1):
    min_X = min(X)
    max_X = max(X)
    new_X = [(x - min_X) / (max_X - min_X) * (max_val - min_val) + min_val for x in X]
    return new_X

def Bai1():
    print('Nhập vector X: ')
    X = list(map(int, input().split()))
    new_X = Chuanhoa(X, -1, 1)
    print('Mảng X sau khi chuẩn hóa: ', end = '')
    for x in new_X: print(x, end = ' ')

def Bai2():
    d1, d2 = {}, {}
    n1 = int(input('Nhập số lượng sinh viên cần nhập của từ điển 1: '))
    for i in range(n1):
        msv = input(f'Nhập mã sinh viên của sinh viên thứ {i + 1}: ')
        diem = float(input(f'Nhập điểm QTHT của sinh viên thứ {i + 1}: '))
        d1[msv] = diem
    n2 = int(input('Nhập số lượng sinh viên cần nhập của từ điển 2: '))
    for i in range(n2):
        msv = input(f'Nhập mã sinh viên của sinh viên thứ {i + 1}: ')
        diem = float(input(f'Nhập điểm QTHT của sinh viên thứ {i + 1}: '))
        d2[msv] = diem
    d = {}
    for key, val in d1.items():
        if key not in d2:
            d[key] = 0
        else:
            d[key] = d1[key] * 0.4 + d2[key] * 0.6

    for key, val in d2.items():
        if key not in d1:
            d[key] = 0
        else:
            d[key] = d1[key] * 0.4 + d2[key] * 0.6

    print('Từ điển kết quả: ', d)

class TacGia:
    def __init__(self, Ten, Email, GioiTinh):
        self.Ten = Ten
        self.Email = Email
        self.GioiTinh = GioiTinh

    def __str__(self):
        return f'Tên tác giả: {self.Ten}, Email tác giả: {self.Email}, Giới Tính tác giả: {self.GioiTinh}'

class Sach:
    def __init__(self, TieuDe, DSTacGia, NXB, GiaBan):
        self.TieuDe = TieuDe
        self.DSTacGia = DSTacGia
        self.NXB = NXB
        self.GiaBan = GiaBan

    def __str__(self):
        return f'Tiêu đề: {self.TieuDe}, Nhà xuất bản: {self.NXB}, Giá bán: {self.GiaBan}'

def Bai3():
    n = int(input('Nhập số lượng sách cần thêm: '))
    a = []
    for i in range(n):
        print(f'Nhập thông tin cho cuốn sách thứ {i + 1}:')
        TieuDe = input('Nhập tiêu đề cho cuốn sách: ')
        TacGia = input('Nhập danh sách tác giả: ').split(', ')
        NXB = input('Nhập nhà xuất bản: ')
        GiaBan = input('Nhập giá bán: ')
        x = Sach(TieuDe, TacGia, NXB, GiaBan)
        a.append(x)
    str = input('Nhập tên tác giá cần tìm kiếm sách: ')
    for x in a:
        if str in x.DSTacGia:
            print(x)



if __name__ == '__main__':
    Bai3()