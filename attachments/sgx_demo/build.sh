#!/bin/bash

# @Author: Jh Li
# @github: https://github.com/Aptx4869AC
# @Created: 2024-01-11

set -e

BLUE='\033[1;34m'
NC='\033[0m'

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" >/dev/null 2>&1 && pwd )"
python_dir="$script_dir/occlum_instance/image/opt/python-occlum"

if [ -d occlum_instance ]; then
    rm -r occlum_instance
fi

occlum new occlum_instance


cd occlum_instance
copy_bom -f ../opencv.yaml --root image --include-dir /opt/occlum/etc/template

if [ ! -d $python_dir ];then
    echo "Error: cannot stat '$python_dir' directory"
    exit 1
fi

new_json="$(jq '.env.default += ["PYTHONHOME=/opt/python-occlum"] |
        	.resource_limits.kernel_space_heap_size ="2048MB"|
		.resource_limits.user_space_size = "1680MB" |
                .resource_limits.max_num_of_threads = 64 |
                .process.default_heap_size = "512MB" ' Occlum.json)" && \
echo "${new_json}" > Occlum.json
occlum build --sgx-mode SIM

