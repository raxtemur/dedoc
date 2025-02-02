"""Downloading models in advance inside the docker container."""
import os
import shutil

from huggingface_hub import hf_hub_download

from dedoc.config import get_config


def download_from_hub(out_dir: str, out_name: str, repo_name: str, hub_name: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.realpath(hf_hub_download(repo_id=f"dedoc/{repo_name}", filename=hub_name))
    shutil.move(path, os.path.join(out_dir, out_name))


def download(resources_path: str) -> None:

    download_from_hub(out_dir=resources_path,
                      out_name="scan_orientation_efficient_net_b0.pth",
                      repo_name="scan_orientation_efficient_net_b0",
                      hub_name="model.pth")

    download_from_hub(out_dir=resources_path,
                      out_name="font_classifier.pth",
                      repo_name="font_classifier",
                      hub_name="model.pth")

    download_from_hub(out_dir=resources_path,
                      out_name="paragraph_classifier.pkl.gz",
                      repo_name="paragraph_classifier",
                      hub_name="model.pkl.gz")

    line_clf_resources_path = os.path.join(resources_path, "line_type_classifiers")
    for classifier_type in ("diploma", "law", "law_txt", "tz", "tz_txt"):
        download_from_hub(out_dir=line_clf_resources_path,
                          out_name=f"{classifier_type}_classifier.pkl.gz",
                          repo_name="line_type_classifiers",
                          hub_name=f"{classifier_type}.pkl.gz")


if __name__ == "__main__":
    resources_path = get_config()["resources_path"]
    download(resources_path)
