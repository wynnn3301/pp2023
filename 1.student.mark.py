def nhap_hocsinh(danhsach_hocsinh):   # Ham nhap so hoc sinh
    so_hoc_sinh = int(input('Nhap so hoc sinh: '))
    for i in range(so_hoc_sinh):
        small_hs = []
        id_hs = input('Nhap id hs: ')
        ten_hs = input('Nhap ten hs: ')
        dob_hs = input('Nhap dob hs: ')
        small_hs.append(id_hs)
        small_hs.append(ten_hs)
        small_hs.append(dob_hs)
        danhsach_hocsinh.append(small_hs)


def nhap_khoa_hoc (khoa_hoc):   # Ham nhap thong tin cua khoa hoc
    so_kh = int(input('So khoa hoc: '))
    for i in range(so_kh): 
        small_kh = []
        id_kh = input('ID cua khoa hoc: ')
        ten_kh = input('Ten khoa hoc: ')
        small_kh.append(id_kh)
        small_kh.append(ten_kh)
        khoa_hoc.append(small_kh)
    

def chon_va_nhapdiem (khoa_hoc, small_kh):  # Ham chon khoa hoc va nhap diem
    pick_kh = input('nhap khoa hoc muon chon: ')
    for i in list(khoa_hoc):                # Loop trong list
        for i in list(small_kh):            # Loop trong list be
            if pick_kh == small_kh[0]:
                dict_diem = {}
                diem = int(input('Nhap diem cua hs: '))
                dict_diem['diem'] = diem
                khoa_hoc.append(dict_diem)

danhsach_hocsinh = []
khoa_hoc = []

