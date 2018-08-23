# Hello đến với dự án minecraft build - app 
## https://huystart17.github.io/minecraft-app-teky-project/

Dự án được tham gia với 
1. Quốc Bảo  
2. Trung Kiên 
3. Hoàng Hà
4. Mai 
5. Hoàng 
6. Hiếu
Yêu cầu cài visual studio code https://code.visualstudio.com/ ,và git https://git-scm.com/

Sau khi cài xong các bạn mở *visual studio code* 
Bấm tổ hợp "ctr" + "Shift" + "p" 
Sau đó gõ "git clone"
Sau đó đồng ý và lưu dự án về

## Các thư viện sử dụng
1. mcpi

## Cấu trúc chương trình
```pre
root 
-- app.py ....
-- lib
-- -- Building.py
-- -- Nature.py
-- -- ....
-- mcpi 
```
### Thư viện này giúp các bạn tạo công trình nhanh hơn xịn hơn
### Thư viện giúp lấy các vị trí toạ độ khu vực trong minecraft tại các toạ độ tương đối
### THư viện này giúp bạn có thể quản lý thông tin, sự kiện diễn ra trong game

### Tiến trình - đã tiến hành 
1. Đã có nhà cửa cơ bản
2. Đã có các đồ vật cơ bản
3. Đã có các sự vật trong thiên nhiên cơ bản

### Tiến trình - cần làm
A. Công trình phức tạp : 
  1. Nhà nhiều tầng 
  2. Nhà rộng 
  3. Nhà có rào bao quanh
  4. Nhà hình chữ L 
  5. Nhà có thể tuỳ biến được
  6. Tháp cao tầng
  7. Chung cư
  8. Nhà cực dài
  9. Nhà cực sâu
  10. Nhà bên đường 
  11. Khu phố với nhà 2 bên đường
B. Hàm hỗ trợ:
  1. Hàm getCenter (x,y,z, x1,y1,z1) trả về toạ độ chính giữa giữa giữa 2 điểm
  2. Hàm getDistance(x,y,z, x1,y1,z1) Trả về khoảng cách giữa 2 điểm
  3. Giả sử có 2 diểm x,y,z và x1,y,z1 nằm trên mặt phẳng, hàm corners sẽ trả về toạ độ của 4 góc dưới dạng mảng


## Ứng dụng với các sự kiện

### Tạo game command giúp người chơi có thể tạo công trình nhanh với tên của công trình
### Tra cứu c
