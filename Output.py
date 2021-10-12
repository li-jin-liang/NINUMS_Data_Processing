class Output:

    # Record the cluster_output in one specific step
    def __init__(self, time, step, total_clu_num):
        self._time = float(time)
        self._step = float(step)
        self._total_clu_num = int(total_clu_num)
        self._obj_list = []

        # 体系中 he 的总原子个数
        self._he_atom_num = 0
        # 体系中 有he的团簇个数
        self._he_clu_num = 0

    def add_cluster(self, cluster):
        self._obj_list.append(cluster)
        if cluster.he_num() > 0:
            self._he_atom_num += cluster.he_num()
            self._he_clu_num += 1

    def get_he_atom_num(self):
        return self._he_atom_num

    def get_he_clu_num(self):
        return self._he_clu_num

    def get_time(self):
        return self._time

