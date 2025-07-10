import requests

from Control.photo import Photo, Root


def get_photos(query: str, color: str, page: int = 1, per_page: int = 80) -> tuple[list[Photo], int]:  # type: ignore
    url = f"https://api.pexels.com/v1/search?query={query}&orientation=landscape&size=large&color={color}&locale=&page={page}&per_page={per_page}"
    print(f"URL: {url}")  # In ra URL để kiểm tra
    # Thêm header Authorization với API key
    headers = {
        "Authorization": "Y3dDyi8upPyObSyzc6swlKMR0YyGgfLunIoHCvgkXwALQ9cev030eIMQ"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        photos = Root.from_dict(data).photos
        total = data.get("total_results", 0)  # Lấy số lượng kết quả từ JSON gốc
        print(f"Số ảnh trong trang hiện tại: {len(photos)} / Tổng: {total}")
        return photos, total
    else:
        print("Gọi API thất bại:", response.status_code)
        return [], 0

