#!/usr/bin/env python3

import os
import json
from jinja2 import Environment, FileSystemLoader
from datetime import datetime, timedelta

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "TabbyML").strip()

env = Environment(loader=FileSystemLoader("."))
template = env.get_template("meta/README.tmpl.md")

with open("models.json", "r") as f:
    models = json.load(f)

completion_models = [x for x in models if 'prompt_template' in x]
chat_models = [x for x in models if 'chat_template' in x]

rendered_template = template.render(completion_models=completion_models, chat_models=chat_models, gh_user=GITHUB_USERNAME)

with open("README.md", "w") as f:
    f.write(rendered_template)
print("README.md generated")
