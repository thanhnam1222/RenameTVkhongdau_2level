"""
RenameTVkhongdau_2level v1.01 b2501
Tác giả: NamNT (thanhnam1222@gmail.com)
Chức năng:
     Đổi tên file, folder Tiếng Việt có dấu thành không dấu 2 cấp độ folder hiện hành và fodler con
Tham khảo code của longnh.com
"""
import os
import re

"""List các ký tự cần thay đổi"""
patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '–': '-',                ''' Gạch ngang dài thành dấu trừ -'''
    'Ý': 'Y',                ''' Ý , ý chưa đổi được '''
    '[ỳýỷỹỵ]': 'y'
}
"""
Hàm Convert from 'Tiếng Việt có dấu' thành 'Tieng Viet khong dau'
text: input string to be converted
Return: string converted
"""
def convert(text):
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output

"""đường dẫn folder chứa các file cần đổi tên"""
print("Đang thực hiện xin chờ giây lát...")
folder_path = "."

# Doi ten file + folder level 1 (folder hiện hành)
ds1 = os.listdir(folder_path)
for file in ds1:
    link=os.path.join(folder_path, file)
    newlink= os.path.join(folder_path, convert(file))
    oldpath = link    
    newpath = newlink
    if (oldpath!=newpath):
        try:
            os.rename(oldpath, newpath)
        except OSError as error:
            print(f"Error renaming file: {error}")
ans='y'
#ans=input('Đã xong thư mục hiện hành. Bạn có muốn Đổi tên không dấu thư mục con (y/n)?')
if (ans=='y'):
# Đổi tên file + folder level 2 (folder con)
# Có Cập nhật lại danh sách folder
    ds1 = os.listdir(folder_path)
    for file1 in ds1: 
        file2 = os.path.join(folder_path, file1)
        if os.path.isdir(file2):  # Kiểm tra nếu là thư mục thì đổi tên thành phần bên trong
            ds2 = os.listdir(file2)
            for file in ds2:
                link=os.path.join(file2, file)
                newlink= os.path.join(file2, convert(file))
                oldpath = link
                newpath = newlink
                if (oldpath!=newpath):
                    try:
                        os.rename(oldpath, newpath)
                    except OSError as error:
                        print(f"Error renaming file: {error}") 
#t=input("Đã xong.Nhấn phím bất kỳ để tắt")
