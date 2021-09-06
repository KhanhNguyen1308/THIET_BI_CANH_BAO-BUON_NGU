def trang_thai_dau(thuoc, mui_ten, gd, R, goc_chinh, goc_nghieng):
    if thuoc:
        if (gd[1]+R/2)<=mui_ten[1]:
            trang_thai = 'Cui'
            mode = 1
        elif mui_ten[1] <= (gd[1]-R/2):
            trang_thai = 'Ngang'
            mode = 8
        else:
            if -20 <= goc_nghieng <= 20:
                trang_thai = 'Thang' 
                mode = 0
            elif goc_nghieng < -20:
                trang_thai = 'Nghieng phai'
                mode = 2
            else:
                trang_thai = 'Nghieng trai'
                mode = 3
    else:
        if mui_ten[0] <= gd[0] and mui_ten[1] <= gd[1]:
            if goc_chinh <= 45:
                trang_thai = 'Nhin phai'
                mode = 6
            else:
                trang_thai = 'Ngang'
                mode = 8
        elif mui_ten[0] > gd[0] and mui_ten[1] <= gd[1]:
            if goc_chinh <= 45:
                trang_thai = 'Nhin trai'
                mode = 7
            else:
                trang_thai = 'Ngang'
                mode = 8
        elif mui_ten[0] <= gd[0] and mui_ten[1] > gd[1]:
            if -45 <= goc_chinh <= -20:
                trang_thai = 'Cui phai'
                mode = 4
            elif goc_chinh > -20:
                trang_thai = 'Nhin phai'
                mode = 6
            else:
                trang_thai = 'Cui'
                mode = 1
        elif mui_ten[0] > gd[0] and mui_ten[1] > gd[1]:
            if 20 <= goc_chinh <= 45:
                trang_thai = 'Cui trai'
                mode = 5
            elif goc_chinh < 20:
                trang_thai = 'Nhin trai'
                mode = 7
            else:
                trang_thai = 'Cui'
                mode = 1
    trang_thai_trc = trang_thai
    return trang_thai, mode, trang_thai_trc


def trang_thai_mat(ty_le_mat, ty_le_mat_phai, ty_le_mat_trai, dem, mode, canh_bao, trang_thai_trc):
    if mode == 0:
        if ty_le_mat <= 0.25:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 1:
        if ty_le_mat <= 0.3:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 2:
        if ty_le_mat <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                    larm = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 3:
        if ty_le_mat <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 4:
        if ty_le_mat_trai <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 5:
        if ty_le_mat_phai <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 6:
        if ty_le_mat_trai <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                    canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 7:
        if ty_le_mat_phai <= 0.28:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    elif mode == 8:
        if ty_le_mat <= 0.25:
            trang_thai = 'Nham'
            dem += 1
            if dem >= 20:
                canh_bao = True
        else:
            trang_thai = 'Mo'
            dem = 0
            canh_bao = False
    trang_thai_trc = trang_thai
    return trang_thai, trang_thai_trc, dem, canh_bao


def gat_dau(trang_thai_trc, mode, dem, gat_num, trang_thai, canh_bao):
    if trang_thai_trc == 0 and mode == 0 and trang_thai == "Mo":
        trang_thai_trc == mode
        gat_num = 0
        canh_bao = False
    if mode == 1 and trang_thai_trc == 0:
        if trang_thai == "Nham":
            dem += 1
            trang_thai_trc = mode
    if mode == 0 and trang_thai_trc == 1:  
        if dem <= 10 and dem != 0:
            gat_num += 1
            dem = 0
            canh_bao = True
    return gat_num, dem, trang_thai_trc, canh_bao