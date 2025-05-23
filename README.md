<p align="center">
<img src="https://raw.githubusercontent.com/Project-MONAI/MONAI/dev/docs/images/MONAI-logo-color.png" width="50%" alt='project-monai'>
</p>

💡 If you want to know more about MONAI Deploy WG vision, overall structure, and guidelines, please read [MONAI Deploy](https://github.com/Project-MONAI/monai-deploy) main repo first.

# MONAI Deploy App SDK
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)


MONAI Deploy App SDK offers a framework and associated tools to design, develop and verify AI-driven applications in the healthcare imaging domain.

## Features

- Build medical imaging inference applications using a flexible, extensible & usable Pythonic API
- Easy management of inference applications via programmable Directed Acyclic Graphs (DAGs)
- Built-in operators to load DICOM data to be ingested in an inference app
- Out-of-the-box support for in-proc PyTorch based inference, as well as remote inference via Triton Inference Server
- Easy incorporation of MONAI based pre and post transformations in the inference application
- Package inference application with a single command into a portable MONAI Application Package
- Locally run and debug your inference application using App Runner

## User Guide

User guide is available at [docs.monai.io](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/).

## Citation

If you have used MONAI in your research, please cite us! The citation can be exported from: [https://arxiv.org/abs/2212.14177](https://arxiv.org/abs/2212.14177).

## Installation

To install [the current release](https://pypi.org/project/monai-deploy-app-sdk/), you can simply run:

```bash
pip install monai-deploy-app-sdk
```

### Prerequisites

- This SDK depends on [NVIDIA Holoscan SDK](https://pypi.org/project/holoscan/) for its core implementation as well as its CLI, hence inherits its prerequisites, e.g. Ubuntu 22.04 with glibc 2.35 on X86-64 and NVIDIA dGPU drivers version 535 or above.
- [CUDA 12.2](https://developer.nvidia.com/cuda-12-2-0-download-archive) or above is required along with a supported NVIDIA GPU with at least 8GB of video RAM.
- If inference is not used in an example application and a GPU is not installed, at least [CUDA 12 runtime](https://pypi.org/project/nvidia-cuda-runtime-cu12/) is required, as this is one of the requirements of Holoscan SDK. In addition, the `LIB_LIBRARY_PATH` must be set to include the installed shared library, e.g. in a Python 3.10 env, ```export LD_LIBRARY_PATH=`pwd`/.venv/lib/python3.10/site-packages/nvidia/cuda_runtime/lib:$LD_LIBRARY_PATH```
- Python: 3.9 to 3.12

## Getting Started

Getting started guide is available at [here](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/getting_started/index.html).

```bash
pip install monai-deploy-app-sdk

# Clone monai-deploy-app-sdk repository for accessing examples.
git clone https://github.com/Project-MONAI/monai-deploy-app-sdk.git
cd monai-deploy-app-sdk

# Install necessary dependencies for simple_imaging_app
pip install matplotlib Pillow scikit-image

# Execute the app locally
python examples/apps/simple_imaging_app/app.py -i examples/apps/simple_imaging_app/input/brain_mr_input.jpg -o output

# Package app (creating MAP Docker image), using `-l DEBUG` option to see progress.
# Also please note that postfix will be added to user supplied tag for identifying CPU architecture and GPU type etc.
monai-deploy package examples/apps/simple_imaging_app -c examples/apps/simple_imaging_app/app.yaml -t simple_app:latest --platform x86_64 -l DEBUG

# Run the app with docker image and an input file locally
## Copy a test input file to 'input' folder
mkdir -p input && rm -rf input/*
cp examples/apps/simple_imaging_app/input/brain_mr_input.jpg input/
## Launch the app
monai-deploy run simple_app-x64-workstation-dgpu-linux-amd64:latest -i input -o output
```

### [Tutorials](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/getting_started/tutorials/index.html)

Tutorials are provided to help getting started with the App SDK, to name but a few below.

#### [1) Creating a simple image processing app](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/getting_started/tutorials/simple_app.html)

#### [2) Creating MedNIST Classifier app](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/getting_started/tutorials/mednist_app.html)

YouTube Video (to be updated with the new version):

- [MedNIST Classification Example](https://www.youtube.com/watch?v=WwjilJFHuU4)

### [3) Creating a Segmentation app](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/getting_started/tutorials/segmentation_app.html)

YouTube Video (demonstrating the previous version of the App SDK):

- [Spleen Organ Segmentation - Jupyter Notebook Tutorial](https://www.youtube.com/watch?v=cqDVxzYt9lY)
- [Spleen Organ Segmentation - Deep Dive](https://www.youtube.com/watch?v=nivgfD4pwWE)

### [4) Creating a Segmentation app including visualization with Clara Viz](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/getting_started/tutorials/segmentation_clara-viz_app.html)

### [5) Creating a Segmentation app consuming a MONAI Bundle](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/getting_started/tutorials/monai_bundle_app.html)

### [Examples](https://docs.monai.io/projects/monai-deploy-app-sdk/en/stable/getting_started/examples.html)

<https://github.com/Project-MONAI/monai-deploy-app-sdk/tree/main/examples/apps> has example apps that you can see, to name but a few

- simple_imaging_app
- ai_livertumor_seg_app
- ai_spleen_seg_app
- ai_unetr_seg_app
- dicom_series_to_image_app
- mednist_classifier_monaideploy
- ai_remote_infer_app


## Contributing

For guidance on making a contribution to MONAI Deploy App SDK, see the [contributing guidelines](https://github.com/Project-MONAI/monai-deploy/blob/main/CONTRIBUTING.md).

## Community

To participate, please join the MONAI Deploy App SDK weekly meetings on the [calendar](https://calendar.google.com/calendar/u/0/embed?src=c_954820qfk2pdbge9ofnj5pnt0g@group.calendar.google.com&ctz=America/New_York) and review the [meeting notes](https://docs.google.com/document/d/1viIh3vyP6_gZBKcnu7gb8fU0tm9aWBOcKCMGezIWNQw/edit#).

Join the conversation on Twitter [@ProjectMONAI](https://twitter.com/ProjectMONAI) or join our [Slack channel](https://forms.gle/QTxJq3hFictp31UM9).

Ask and answer questions over on [MONAI Deploy App SDK's GitHub Discussions tab](https://github.com/Project-MONAI/monai-deploy-app-sdk/discussions).

## Links

- Website: <https://monai.io>
- API documentation: <https://docs.monai.io/projects/monai-deploy-app-sdk>
- Code: <https://github.com/Project-MONAI/monai-deploy-app-sdk>
- Project tracker: <https://github.com/Project-MONAI/monai-deploy-app-sdk/projects>
- Issue tracker: <https://github.com/Project-MONAI/monai-deploy-app-sdk/issues>
- Wiki: <https://github.com/Project-MONAI/monai-deploy-app-sdk/wiki>
- Test status: <https://github.com/Project-MONAI/monai-deploy-app-sdk/actions>
- PyPI package: <https://pypi.org/project/monai-deploy-app-sdk>
