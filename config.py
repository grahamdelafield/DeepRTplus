train_path = '../data/rt_prediction/training.txt' # 'data/mod_train_2.txt' 
test_path = '../data/rt_prediction/testing.txt' 
result_path = '../data/rt_prediction/pred.txt'
log_path = '../data/rt_prediction/pred.log'
save_prefix = 'peaks_epochs'
pretrain_path = '' # 'param/dia_all_epo20_dim24_conv10/dia_all_epo20_dim24_conv10_filled.pt' # 'param/dia_all_trans_mod_epo20_dim24_conv10.pt' 
dict_path = '' # 'data/mod.txt'

conv1_kernel = 10
conv2_kernel = 10

# add after main analysis and heatmap analysis done:
min_rt = 0
max_rt = 80 # 70 # 110 # 264
time_scale = 60 # 1 # 60
max_length = 49

# dia params:
'''
min_rt = -60
max_rt = 184
time_scale = 60
max_length = 66
'''

# unmod params:
'''
min_rt = 0
max_rt = 264
time_scale = 60
max_length = 38
'''

# mod params:
'''
min_rt = 0
max_rt = 110
time_scale = 60
max_length = 50
'''

# SCX params:
'''
min_rt = 0
max_rt = 46
time_scale = 1
max_length = 49
'''

# LUNA_HILIC params:
'''
min_rt = 0
max_rt = 42
time_scale = 1
max_length = 46
'''

# Xbridge params:
'''
min_rt = 9
max_rt = 46
time_scale = 1
max_length = 51
'''

# ATLANTIS_SILICA params:
'''
min_rt = 9
max_rt = 46
time_scale = 1
max_length = 49
'''

# LUNA_SILICA params:
'''
min_rt = 9
max_rt = 47
time_scale = 1
max_length = 48
'''