import math
from flask import Flask, render_template, request, jsonify  # type: ignore
from Network.network import get_photos



app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/")
def index():
    query = request.args.get("q", "nature")          # 🔍 đúng với tên tham số q
    color = request.args.get("c", "")                # 🎨 đúng với tên tham số c
    page = int(request.args.get("page", 1))          # 🧭 đúng với tên tham số page
    per_page = int(request.args.get("per_page", 20)) # 🧮 đúng với tên per_page

    photos, total_results = get_photos(query, color, page, per_page)
    total_pages = math.ceil(total_results / per_page)

    return render_template(
        "gallery.html",
        photos=photos,
        current_query=query,
        current_color=color,
        page=page,
        per_page=per_page,
        total_pages=total_pages
    )


