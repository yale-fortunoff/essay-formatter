from yaml import load, Loader
import os


def load_project_settings(markdown_dir: str):
    project_settings_path = os.path.join(markdown_dir, "settings.yaml")
    print(f"Looking for path: {project_settings_path}")
    if os.path.exists(project_settings_path):
        print(f"Path exists: {project_settings_path}")
        return load(open(project_settings_path, encoding="utf-8").read(), Loader=Loader)
