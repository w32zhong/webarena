# Author: Wei Zhong
FROM nvcr.io/nvidia/pytorch:23.11-py3
WORKDIR /workspace
RUN git clone https://github.com/t-k-cloud/tkarch.git && \
    pushd tkarch && cd dotfiles && ./overwrite.sh && \
    popd && rm -rf tkarch/.git
RUN apt update && apt install -y tmux
ADD . webarena
RUN cd webarena/3rd_party/causal-conv1d; \
    git apply ../causal-conv1d.patch; \
    python setup.py build; \
    python setup.py install; \
    rm -rf build/ *.egg-info dist; \
    python ../blackmamba/test/test_causal_conv1d.py
RUN cd webarena/3rd_party/mamba; \
    git apply ../mamba.patch; \
    python setup.py build; \
    python setup.py install; \
    rm -rf build/ *.egg-info dist; \
    python ../mamba.test.py
CMD /bin/bash
