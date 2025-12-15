cwd should be `tiny-shakespeare`

We assume a layout like the following:

```
git
├── comp560-nanoGPT
│   ├── sample.py
│   └── train.py
└── your-repo
    └── tiny-shakespeare
        ├── README.md
        ├── config
        │   └── train_tiny_shakespeare.py
        ├── data
        ├── out
        └── useful-commands.md
```

Training:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/train.py config/train_tiny_shakespeare.py
```

Sampling:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/sample.py config/train_tiny_shakespeare.py --num_samples=1 --max_new_tokens=100 --seed=1
```
