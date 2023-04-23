#!/bin/bash
set -e -u -x

function repair_wheel {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" --plat "$PLAT" -w /lttbc/dist/
    fi
}


# Install a system package required by our library
# yum install -y atlas-devel

ls -la /opt/python/

# Compile wheels for python 3.1*
for PYBIN in /opt/python/cp31*/bin; do
    "${PYBIN}/pip" install -r /lttbc/requirements.txt
    "${PYBIN}/pip" wheel /lttbc/ --no-deps -w dist/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    repair_wheel "$whl"
done

# Install packages and test for python 3.1*
for PYBIN in /opt/python/cp31*/bin; do
     "${PYBIN}/pip" install lttbc --no-index -f /lttbc/dist
#     (cd "$HOME"; "${PYBIN}/nosetests" lttbc)
done
