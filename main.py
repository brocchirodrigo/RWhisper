import os
import uuid

from flask import Flask, request, jsonify, json

from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename

from convert import convert
from transcribe_whisper import transcribe_whisper


app = Flask(__name__)


uploads_dir = os.path.join(app.instance_path, 'cache')
os.makedirs(uploads_dir, exist_ok=True)


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e.name)), 404


@app.route('/', methods=['POST'])
def upload():
    global save_as
    global new_name_file_saved

    try:
        file = request.files['file']
        save_as = os.path.join(uploads_dir, secure_filename(file.filename))
        file.save(save_as)

        uuid_file = uuid.uuid4()
        new_name_file = str(uuid_file)+'.mp3'
        new_name_file_saved = os.path.join(uploads_dir, new_name_file)

        convert(save_as, new_name_file_saved)
        os.remove(save_as)

        result = transcribe_whisper(new_name_file_saved)
        os.remove(new_name_file_saved)
        return jsonify(text=result)
    except:
        os.remove(save_as)
        os.remove(new_name_file_saved)
        raise Exception("Erro ao executar a rotina de conversão e transcrição")


if __name__ == '__main__':
    app.run(debug=False)
