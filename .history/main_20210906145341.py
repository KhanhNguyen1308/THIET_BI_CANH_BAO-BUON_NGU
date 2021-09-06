import cv2
import time
import math
import numpy as np
import mediapipe as mp
from threading import Thread
from ham import play_sound, draw_point, ty_le_mat, khoang_cach, giao_diem, duong_tron
from trang_thai_dau import trang_thai_dau, trang_thai_mat, gat_dau

dem = 0
mode = 0
prev_status = 0
gat_num = 0
dem_gat = 0
ty_le_tb = 0
ty_le_mat_trai = 0
ty_le_mat_phai = 0
tt_mat = ''
tt_mat_trc = ''
Tu_the = ''
Tu_the_trc = ''

canh_bao = False
# avg = open("Text/avg.txt", "+w")
# md = open("Text/mode.txt", "+w")


mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
cap = cv2.VideoCapture(0)
canh_bao = False
i = 0

while True:
    ret, img = cap.read()
    key = cv2.waitKey(50)
    pTime = time.time()
    ih, iw = img.shape[0], img.shape[1]
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results:
        face = []
        mat_trai = []
        mat_phai = []
        try:
            for face_lms in results.multi_face_landmarks:
                for lm in face_lms.landmark:
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])
            mat_trai.append([face[263], face[374], face[380], face[382], face[385], face[386]])
            mat_phai.append([face[130], face[145], face[153], face[155], face[158], face[159]])
            img = draw_point(img, mat_trai, mat_phai)
            ty_le_mat_phai, ty_le_mat_trai, ty_le_tb = ty_le_mat(mat_trai, mat_phai)
            phai = (int((face[162][0]+face[127][0])/2), int((face[162][1]+face[127][1])/2))
            trai = (int((face[389][0]+face[356][0])/2), int((face[389][1]+face[356][1])/2))
            gd = giao_diem(face[130], face[263], face[152],face[151])
            trung_tam = (int((phai[0]+trai[0])/2), int((phai[1]+trai[1])/2))
            ban_kinh = int((khoang_cach(gd, (face[155][0], face[155][1]))+khoang_cach(gd, (face[382][0], face[382][1])))/2)
    
            cv2.circle(img, gd, ban_kinh, (0, 255, 0), 1)
            x_max = gd[0]+ban_kinh
            x_min = gd[0]-ban_kinh
            y_max = gd[1]+ban_kinh
            y_min = gd[1]-ban_kinh
            x = int(2*(gd[0] - trung_tam[0])) + trung_tam[0]
            y = int(2*(gd[1] - trung_tam[1])) + trung_tam[1]
            mui_ten = (x, y)
            x_1 = (mui_ten[0] - gd[0])
            if x_1 == 0:
                x_1 = 1
            x_2 = (face[155][0] - gd[0])
            if x_2 == 0:
                x_2 = 1
            n = (mui_ten[1] - gd[1])/x_1
            m = (face[155][1] - gd[1])/ x_2
            goc_chinh = int(math.degrees(math.atan(n)))
            goc_nghieng = int(math.degrees(math.atan(m)))
            thuoc= duong_tron(mui_ten, gd, ban_kinh)
            Tu_the, mode, Tu_the_trc = trang_thai_dau(thuoc, mui_ten, gd, ban_kinh, goc_chinh, goc_nghieng)
            tt_mat, tt_mat_trc, dem, canh_bao = trang_thai_mat(ty_le_tb, ty_le_mat_phai, ty_le_mat_trai, dem, mode, canh_bao, tt_mat_trc)
            gat_num, dem_gat, prev_status, canh_bao = gat_dau(prev_status, mode, dem_gat, gat_num, tt_mat, canh_bao)
            # md.write(str(mode/10)+"\n")
            # avg.write(str(round(ty_le_tb,3))+"\n")
            if canh_bao:
                cv2.putText(img, "CANH BAO!!!", (int(iw/2)-200, int(ih/2)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

            cv2.circle(img, gd, 2, (255, 0, 0), -1)
            cv2.circle(img, phai, 2, (255, 255, 0), -1)
            cv2.circle(img, trai, 2, (255, 255, 0), -1)
            cv2.circle(img, mui_ten, 2, (255, 255, 0), -1)
            cv2.circle(img, trung_tam, 2, (0, 0, 255), -1)

            cv2.circle(img, (face[151][0],face[151][1]), 2, (0, 255, 0), -1)
            cv2.circle(img, (face[152][0],face[152][1]), 2, (0, 255, 0), -1)
            cv2.circle(img, (face[130][0],face[130][1]), 2, (0, 0, 255), -1)
            cv2.circle(img, (face[263][0],face[263][1]), 2, (0, 0, 255), -1)
            cv2.circle(img, (face[155][0], face[155][1]), 2, (255, 255, 0), -1)
            cv2.circle(img, (face[382][0], face[382][1]), 2, (255, 255, 0), -1)

            cv2.line(img, gd, mui_ten, (0, 0, 255), 1)
            cv2.line(img, (face[130][0],face[130][1]), (face[263][0],face[263][1]), (0, 255, 255), 1)
            cv2.line(img, (face[151][0],face[151][1]), (face[152][0],face[152][1]), (0, 255, 255), 1)
            cv2.line(img, (face[130][0], gd[1]), (face[263][0], gd[1]), (0, 255, 255), 1)

            # cv2.putText(img, Tu_the, (x-20,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
            
        except Exception:
            Tu_the = Tu_the_trc
    cTime = time.time()
    fps = int(1 / (cTime - pTime))
    cv2.putText(img, str(fps), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, "Tu the: "+Tu_the, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, "Trang thai mat: " + tt_mat, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    cv2.putText(img, "Gat dau: " + str(gat_num), (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    pTime = cTime
    cv2.imshow('results', img)
    if key == ord('q'):
        break
    if key == ord('f'):
        print(str(round(ty_le_mat_trai,3)))
    if key == ord('z'):
        print(str(goc_chinh))
    if key == ord('r'):
        print(str(round(ty_le_mat_phai,3)))
    if key == ord('a'):
        cv2.imwrite("img/img_"+Tu_the+"_"+tt_mat+".jpg", img)

cap.release()
cv2.destroyAllWindows()
