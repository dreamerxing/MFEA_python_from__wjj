from MFEA.mfea import mfea
from BENCHMARK.task import Task
from BENCHMARK.benchmark import CI_HS, CI_MS, CI_LS, PI_HS, PI_MS, PI_LS, NI_HS, NI_MS, NI_LS


if __name__=="__main__":
    # tasks = CI_HS()
    tasks_list = [CI_HS, CI_MS, CI_LS, PI_HS, PI_MS, PI_LS, NI_HS, NI_MS, NI_LS]
    for task_func in tasks_list:
        tasks = task_func()
        print('-------------------'+tasks+'-----------------')

        TotalEvaluations, bestobj, bestind = mfea(tasks, reps=1)
