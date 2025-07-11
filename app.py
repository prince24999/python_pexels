import math
from flask import Flask, render_template, request, send_file  # type: ignore
from Network.network import get_photos
import urllib.parse
import requests # type: ignore
from io import BytesIO
import os
from urllib.parse import urlparse


app = Flask(__name__)
app.jinja_env.filters['url_encode'] = lambda u: urllib.parse.quote(u)

@app.route("/", methods=["GET"])
@app.route("/")
def index():
    query = request.args.get("q", "nature")          # 🔍 đúng với tên tham số q
    color = request.args.get("c", "")                # 🎨 đúng với tên tham số c
    page = int(request.args.get("page", 1))          # 🧭 đúng với tên tham số page
    per_page = int(request.args.get("per_page", 80)) # 🧮 đúng với tên per_page

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

@app.route('/photo')
def photoview():
    photographer = request.args.get('pgr', 'Unknown Photographer')
    image_url = request.args.get('img')
    alt_text = request.args.get('alt')
    return render_template('photoview.html', image_url=image_url, alt_text=alt_text, photographer=photographer)




@app.route('/download')
def download():
    image_url = request.args.get('img')
    response = requests.get(image_url)

    # Lấy tên file từ URL
    parsed_url = urlparse(image_url)
    filename = os.path.basename(parsed_url.path)  # Trích phần cuối URL

    return send_file(BytesIO(response.content), as_attachment=True, download_name=filename)