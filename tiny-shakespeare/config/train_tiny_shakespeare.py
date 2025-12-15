# train a very miniature character-level shakespeare model

import os


out_dir = 'out'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 20
log_interval = 1

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'tiny-shakespeare'
wandb_run_name = 'embryonic-gpt'

dataset = 'shakespeare_char'
gradient_accumulation_steps = 1
batch_size = 12
block_size = 64

# embryonic GPT model
n_layer = 3
n_head = 3
n_embd = 126 # need n_embd % n_head == 0
dropout = 0.0

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 2000
lr_decay_iters = 2000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

device = 'cpu'
compile = False
