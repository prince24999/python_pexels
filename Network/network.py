import requests

from Control.photo import Photo, Root


def get_photos(query: str) -> [Photo]:  # type: ignore

    url = f"https://api.pexels.com/v1/search?query={query}&orientation=landscape&size=large&color=&locale=&page=1&per_page=100"
    headers = {
        "Authorization": "Y3dDyi8upPyObSyzc6swlKMR0YyGgfLunIoHCvgkXwALQ9cev030eIMQ"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        photos = Root.from_dict(
            data
        ).photos  # Chuyển đổi dữ liệu JSON thành đối tượng Root và lấy thuộc tính photos
        # Hoặc bạn có thể sử dụng Root.from_dict(data) để lấy toàn bộ đối
        # tượng Root nếu cần thiết
        print(f"Số lượng ảnh: {len(photos)}")
        # print(f"Tên nhiếp ảnh gia ảnh đầu tiên: {photos[0].photographer}")
        return photos  # Trả về dữ liệu JSON
    else:
        print("Gọi API thất bại:", response.status_code)
        return None
