# MIT License

# Copyright (c) 2020 ExplosionAI GmbH

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import typer
from pathlib import Path

import spacy


def create_config(model_name: str, component_to_update: str, output_path: Path, train_path: str, dev_path: str):
    nlp = spacy.load(model_name)

    # create a new config as a copy of the loaded pipeline's config
    config = nlp.config.copy()

    # revert most training settings to the current defaults
    default_config = spacy.blank(nlp.lang).config
    config["corpora"] = default_config["corpora"]
    config["training"] = default_config["training"]
    config["paths"]["train"] = train_path
    config["paths"]["dev"] = dev_path

    # set the vectors if the loaded pipeline has vectors
    if len(nlp.vocab.vectors) > 0:
        config["paths"]["vectors"] = model_name

    # source all components from the loaded pipeline and freeze all except the
    # component to update
    config["training"]["frozen_components"] = []
    for pipe_name in nlp.component_names:
        config["components"][pipe_name] = {"source": model_name}
        if pipe_name != component_to_update:
            config["training"]["frozen_components"].append(pipe_name)

    # save the config
    config.to_disk(output_path)


if __name__ == "__main__":
    typer.run(create_config)