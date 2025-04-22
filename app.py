from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__, static_url_path='', static_folder='web')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return "Kein Bild hochgeladen", 400

    file = request.files['image']
    
    try:
        image = Image.open(file.stream)

        # Bildinformationen auslesen
        width, height = image.size
        mode = image.mode  # z.B. RGB
        colors = len(image.getcolors(maxcolors=1000000)) if image.mode == 'RGB' else "Nicht RGB"

        info = {
            "Breite": width,
            "Höhe": height,
            "Modus": mode,
            "Anzahl Farben (geschätzt)": colors
        }

        return jsonify(info)
    
    except Exception as e:
        return jsonify({"Fehler": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
