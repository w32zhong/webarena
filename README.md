# WebArena: A Realistic Web Environment for Building Autonomous Agents
Upstream: https://github.com/web-arena-x/webarena

```bash
docker build . -t webarena
docker run --gpus all --ipc=host --ulimit memlock=-1 \
    -v $HOME/.cache:/root/.cache \
    -v `pwd`/output:/workspace/output \
    -it webarena
```

## Citation
If you use our environment or data, please cite our paper:
```
@article{zhou2023webarena,
  title={WebArena: A Realistic Web Environment for Building Autonomous Agents},
  author={Zhou, Shuyan and Xu, Frank F and Zhu, Hao and Zhou, Xuhui and Lo, Robert and Sridhar, Abishek and Cheng, Xianyi and Bisk, Yonatan and Fried, Daniel and Alon, Uri and others},
  journal={arXiv preprint arXiv:2307.13854},
  year={2023}
}
```
