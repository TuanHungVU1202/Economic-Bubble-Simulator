import random

import matplotlib.pyplot as plt
import pandas as pd

data = []


def cal_range(starting_point, total_data_points, phase_number):
    # randomly a coeffiction for each phase
    phase_coef = random.uniform(0.5, 1)

    phase_total_data_points = (total_data_points / 6) * phase_coef
    # print(phase_total_data_points)
    phase_virtual_mean = list(range(starting_point, int(starting_point + phase_total_data_points)))
    phase_last_point = phase_virtual_mean[-1]
    # print(phase_data)

    # 4 phases only
    if phase_number == 1:
        range_coef = random.uniform(0, 1.5)
    if phase_number == 2:
        range_coef = random.uniform(1, 3)
    if phase_number == 3.1:
        range_coef = random.uniform(2, 4)
    if phase_number == 3.2:
        range_coef = random.uniform(3, 10)
    if phase_number == 4.1:
        range_coef = random.uniform(1, 2)
    if phase_number == 4.2:
        range_coef = random.uniform(0.1, 1)

    # print(range_coef)
    # for each elements in phase_data
    # range_data_each_phase
    boundaries_each_point = []
    for element in phase_virtual_mean:
        boundaries_each_point.append(element + element * range_coef)
    return phase_virtual_mean, phase_last_point, range_coef


total_points = 350
start_point = 2
boundaries = []

# Phase 1: Stealth
stealth_virtual_mean, stealth_last_point, stealth_range_coef = cal_range(start_point, total_points, 1)
for each_point in stealth_virtual_mean:
    upper_limit = each_point + each_point * stealth_range_coef
    lower_limit = each_point - each_point * stealth_range_coef
    each_point_boundaries = [lower_limit, upper_limit]
    boundaries.append(each_point_boundaries)

# Phase 2: Awareness
aware_virtual_mean, aware_last_point, aware_range_coef = cal_range(stealth_last_point + 1, total_points, 2)
for each_point in aware_virtual_mean:
    upper_limit = each_point + each_point * aware_range_coef
    each_point_boundaries = [each_point, upper_limit]
    boundaries.append(each_point_boundaries)

# Phase 3: Mania
mania1_virtual_mean, mania1_last_point, mania1_range_coef = cal_range(aware_last_point + 1, total_points, 3.1)
for each_point in mania1_virtual_mean:
    upper_limit = each_point + each_point * mania1_range_coef
    each_point_boundaries = [each_point, upper_limit]
    boundaries.append(each_point_boundaries)

mania2_virtual_mean, mania2_last_point, mania2_range_coef = cal_range(mania1_last_point + 1, total_points, 3.2)
for each_point in mania2_virtual_mean:
    upper_limit = each_point + each_point * mania2_range_coef
    each_point_boundaries = [each_point, upper_limit]
    boundaries.append(each_point_boundaries)

# Phase 4: Blow off
blow1_virtual_mean, blow1_last_point, blow1_range_coef = cal_range(mania2_last_point + 1, total_points, 4.1)
for each_point in blow1_virtual_mean:
    upper_limit = each_point + each_point * blow1_range_coef
    each_point_boundaries = [each_point, upper_limit]
    boundaries.append(each_point_boundaries)

blow2_virtual_mean, blow2_last_point, blow2_range_coef = cal_range(blow1_last_point + 1, total_points, 4.2)
for each_point in blow2_virtual_mean:
    upper_limit = each_point + each_point * blow2_range_coef
    lower_limit = each_point - each_point * blow2_range_coef
    each_point_boundaries = [lower_limit, upper_limit]
    boundaries.append(each_point_boundaries)

for each_boundary in boundaries:
    data_point = random.uniform(each_boundary[0], each_boundary[1])
    data.append(data_point)

df = pd.DataFrame(data)
plt.plot(data)
# plt.plot(df.rolling(5).mean())
plt.show()