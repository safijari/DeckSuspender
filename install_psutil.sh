#!/bin/bash
wget https://files.pythonhosted.org/packages/96/2f/caec18213f6a67852f6997fb0673ae08d2e93d1b81573edb93ba4ef06970/pip-22.1.2-py3-none-any.whl -P /tmp
wget https://files.pythonhosted.org/packages/6d/c6/6a4e46802e8690d50ba6a56c7f79ac283e703fcfa0fdae8e41909c8cef1f/psutil-5.9.1-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl -P /tmp
python /tmp/pip-22.1.2-py3-none-any.whl/pip install /tmp/psutil-5.9.1-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl