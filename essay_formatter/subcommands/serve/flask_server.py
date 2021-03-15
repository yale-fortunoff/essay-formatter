from flask import Flask, jsonify, send_from_directory
import os

def serve(build_dir: str):
    app = Flask(__name__, static_folder=build_dir)
    root_dir = os.getcwd()
    print("root_dir", root_dir)
    site_dir = os.path.join(root_dir, build_dir)

    @app.route('/', defaults={'path': 'index.html'})
    @app.route('/<path:path>')
    def serve_file(path):
        print("serve_file", path)
        filename = path
        file_path = os.path.join(site_dir, path)
        print(file_path)
        if not os.path.exists(file_path):
            print(f"File {path} :: {file_path} not found, defaulting to index.html")
            filename = "index.html"
        else:
            print("File exists")

        
        return send_from_directory(site_dir, filename)

    app.run()

