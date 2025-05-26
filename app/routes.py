from flask import Blueprint, jsonify

from flask import Blueprint, request, jsonify
from mailgrab.mailgrab import extract_emails, get_url_ctn

app = Blueprint('routes', __name__)

@app.route("/extract")
def extract():
    url = request.args.get('url')
    if not url:
        return {"error": True, "content": "Missing URL"}, 400

    try:
        html = get_url_ctn(url)
        emails = extract_emails(html)
        return {'error': False, "content": emails}
    except Exception as e:
        return {"error": True, "content": str(e)}

