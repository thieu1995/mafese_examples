#!/usr/bin/env python
# Created by "Thieu" at 08:44, 14/07/2023 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

from mafese import get_dataset, MultiMhaSelector


PATH_SAVE = "history/HillValley"
EPOCH = 200
POP_SIZE = 50
TEST_SIZE = 0.2
ESTIMATOR = "knn"

data = get_dataset("Hill-valley")
data.split_train_test(test_size=TEST_SIZE)

list_optimizers = ("BaseGA", "OriginalHGS", "OriginalARO", "OriginalEFO", "OriginalTLO", "BaseSMA", "AugmentedAEO", "OriginalRUN")
list_paras = [
    {"name": "GA", "epoch": EPOCH, "pop_size": POP_SIZE},
    {"name": "HGS", "epoch": EPOCH, "pop_size": POP_SIZE},
    {"name": "ARO", "epoch": EPOCH, "pop_size": POP_SIZE},
    {"name": "EFO", "epoch": EPOCH, "pop_size": POP_SIZE},
    {"name": "TLO", "epoch": EPOCH, "pop_size": POP_SIZE},
    {"name": "SMA", "epoch": EPOCH, "pop_size": POP_SIZE},
    {"name": "AAEO", "epoch": EPOCH, "pop_size": POP_SIZE},
    {"name": "RUN", "epoch": EPOCH, "pop_size": POP_SIZE},
]
feat_selector = MultiMhaSelector(problem="classification", estimator=ESTIMATOR,
                            list_optimizers=list_optimizers, list_optimizer_paras=list_paras,
                            transfer_func="vstf_01", obj_name="AS")

feat_selector.fit(data.X_train, data.y_train, n_trials=10, n_jobs=10, verbose=False, save_path=PATH_SAVE)
feat_selector.export_boxplot_figures()
feat_selector.export_convergence_figures()

feat_selector.evaluate(estimator=ESTIMATOR, data=data, metrics=["AS", "PS", "RS"], save_path=PATH_SAVE, verbose=False)
