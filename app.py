from flask import Flask, render_template, request  # type: ignore
from Network.network import get_photos
import urllib.parse

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # Lấy query string từ form
    query = request.args.get("q", default="winter")

    color = request.args.get("c", default="")

    # Encode query để an toàn với tiếng Việt và URL
    query_encoded = urllib.parse.quote(query)

    # Gọi hàm lấy ảnh, truyền query đã mã hóa nếu cần
    photos = get_photos(query_encoded, color)

    return render_template("gallery.html", photos=photos, current_query=query)
