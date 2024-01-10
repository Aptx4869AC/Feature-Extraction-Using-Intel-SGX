#!/bin/bash

# @Author: Jh Li
# @github: https://github.com/Aptx4869AC
# @Created: 2024-01-11

set -e
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" >/dev/null 2>&1 && pwd )"

#  Install python and dependencies to specified position
/root/miniconda/bin/conda create --prefix $script_dir/python-occlum -y python=3.7.8 matplotlib imageio numpy opencv-python-headless scipy


