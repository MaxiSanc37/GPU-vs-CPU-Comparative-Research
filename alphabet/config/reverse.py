# train a miniature character-level model
# consisting of fixed strings consisting of a few characters in alphabetical order.
# This will be good for testing completions of different lengths.

out_dir = 'out/reverse'
eval_interval = 50 # keep frequent because we'll overfit
eval_iters = 20
log_interval = 1 

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'liberate-cot'
wandb_run_name = 'reverse'

dataset = 'reverse'
gradient_accumulation_steps = 1
batch_size = 12
block_size = 16

# very very small GPT model
n_layer = 4
n_head = 4
n_embd = 240  # need n_embd % n_head == 0
dropout = 0.0

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 0 # 100 # not super necessary potentially

device = 'cpu'  # run on cpu only
compile = False # do not torch compile the model

