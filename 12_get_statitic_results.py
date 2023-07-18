#!/usr/bin/env python
# Created by "Thieu" at 17:50, 18/07/2023 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import pandas as pd

PATH_READ = "history"
list_data = ["Arrhythmia", "BreastEW", "Digits", "Ionosphere",
             "Madelon", "WaveformEW", "gauss5012", "gauss7517"]

list_mean = []
list_std = []
list_min = []
list_max = []
for idx, data in enumerate(list_data):
    df = pd.read_csv(f"{PATH_READ}/{data}/best_fitness.csv")
    mm = df.groupby("model")["best_fitness"].mean().to_frame().rename(columns={'best_fitness': data})
    ms = df.groupby("model")["best_fitness"].std().to_frame().rename(columns={'best_fitness': data})
    mi = df.groupby("model")["best_fitness"].min().to_frame().rename(columns={'best_fitness': data})
    ma = df.groupby("model")["best_fitness"].max().to_frame().rename(columns={'best_fitness': data})
    list_mean.append(mm.T)
    list_std.append(ms.T)
    list_min.append(mi.T)
    list_max.append(ma.T)
df_mean = pd.concat(list_mean)
df_mean.to_csv(f"{PATH_READ}/statistic_mean.csv")
df_std = pd.concat(list_std)
df_std.to_csv(f"{PATH_READ}/statistic_std.csv")
df_min = pd.concat(list_min)
df_min.to_csv(f"{PATH_READ}/statistic_min.csv")
df_max = pd.concat(list_max)
df_max.to_csv(f"{PATH_READ}/statistic_max.csv")
