# Experiments in the alphabet collection

cwd should be `alphabet`

We assume a layout like the following:

```
git
├── comp560-nanoGPT
│   ├── sample.py
│   └── train.py
└── your-repo
    └── alphabet
        ├── README.md
        ├── config
        │   ├── basic.py
        │   ├── mixed.py
        │   └── reverse.py
        ├── data
        ├── out
        └── useful-commands.md
```


## basic model

Training:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/train.py config/basic.py
```


Sampling:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/sample.py config/basic.py --num_samples=1 --max_new_tokens=100 --seed=2
```


## mixed model

Training:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/train.py config/mixed.py
```


Sampling:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/sample.py config/mixed.py --num_samples=1 --max_new_tokens=100 --seed=2
```


## reverse model

Training:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/train.py config/reverse.py
```


Sampling:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/sample.py config/reverse.py --num_samples=1 --max_new_tokens=100 --seed=2
```

## students model

Training:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/train.py config/students.py
```


Sampling:
```
NANOGPT_CONFIG=../../comp560-nanoGPT/configurator.py  python -u ../../comp560-nanoGPT/sample.py config/students.py --num_samples=1 --max_new_tokens=100 --seed=2
```
