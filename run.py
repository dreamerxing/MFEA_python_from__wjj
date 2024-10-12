import pandas as pd
import os
from MFEA.mfea import mfea
from BENCHMARK.task import Task
from BENCHMARK.benchmark import CI_HS, CI_MS, CI_LS, PI_HS, PI_MS, PI_LS, NI_HS, NI_MS, NI_LS


if __name__=="__main__":
    # tasks = CI_HS()
    save_dir = r'./result'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    results = []
    tasksall = [CI_HS, CI_MS, CI_LS, PI_HS, PI_MS, PI_LS, NI_HS, NI_MS, NI_LS]
    # tasksall = [CI_HS]
    for idx, task_func in enumerate(tasksall):
        tasks = task_func()
        print('-----------------------' + task_func.__name__ + '----------------------------')
        TotalEvaluations, bestobj, bestind = mfea(tasks, p_il=0, reps=1)
        # results.append((TotalEvaluations, bestobj, bestind))
        index = pd.MultiIndex.from_product([range(bestobj.shape[0]), range(bestobj.shape[1])], names=['rep', 'gen'])
        record_data = pd.DataFrame(bestobj.reshape(-1, bestobj.shape[-1]), index=index, columns=['obj1', 'obj2'])
        # record_data = pd.DataFrame(arr_2d)
        file_name = 'task'+ '_' + str(idx+1)
        path = os.path.join(save_dir, file_name)
        record_data.to_csv(path + '.csv')






