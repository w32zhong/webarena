# Author: Wei Zhong
FROM nvcr.io/nvidia/pytorch:23.11-py3
WORKDIR /workspace
RUN git clone https://github.com/t-k-cloud/tkarch.git && \
    pushd tkarch && cd dotfiles && ./overwrite.sh && \
    popd && rm -rf tkarch/.git
RUN apt update && apt install -y tmux
ADD ./3rd_party ./3rd_party
RUN cd ./3rd_party/causal-conv1d; \
    patch < ../causal-conv1d.patch; \
    cat ./setup.py; \
    python setup.py build; \
    python setup.py install; \
    rm -rf build/ *.egg-info dist; \
    echo python ../blackmamba/test/test_causal_conv1d.py
RUN cd ./3rd_party/mamba; \
    patch < ../mamba.patch; \
    cat ./setup.py; \
    python setup.py build; \
    python setup.py install; \
    rm -rf build/ *.egg-info dist; \
    echo python ../mamba.test.py
RUN pip install playwright==1.32.1; \
    playwright install-deps; \
    playwright install
ADD . webarena
RUN cd ./webarena; \
    pip install -r requirements.txt; \
    pip install -e .
RUN python -c 'import nltk; nltk.download("punkt")'
WORKDIR /workspace/webarena
CMD ./run.sh
