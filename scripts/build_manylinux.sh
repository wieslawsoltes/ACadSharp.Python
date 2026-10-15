#!/usr/bin/env bash
# Called inside an official manylinux_2_28 container by build.yml.
set -euo pipefail
export PATH="/opt/python/cp312-cp312/bin:$PATH"
dnf install -y clang zlib-devel openssl-libs libicu
curl -fsSL https://dot.net/v1/dotnet-install.sh -o /tmp/acadsharp-dotnet-install.sh
bash /tmp/acadsharp-dotnet-install.sh --channel 10.0 --install-dir /opt/acadsharp-dotnet
export DOTNET_ROOT=/opt/acadsharp-dotnet
export PATH="$DOTNET_ROOT:$PATH"
python -m pip install build auditwheel
python scripts/build_native.py --rid "$NATIVE_RID"
export ACADSHARP_NATIVE_DIR="$PWD/artifacts/native/$NATIVE_RID"
python -m build --wheel --outdir dist-native-unrepaired packaging/native
auditwheel repair dist-native-unrepaired/*.whl --wheel-dir dist-native
