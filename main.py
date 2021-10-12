# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Output as op
import Cluster as clu
import matplotlib.pyplot as plt


def read_data(_filename):
    output_list = []

    time_list = []
    he_atom_num_list = []
    he_clu_num_list = []

    with open(_filename) as f:
        line = f.readline()
        line = line.split()
        flag = -1
        count = 0
        # flag代表是否为初始情况
        while line:
            assert line == ['Cluster']
            # 遇到Cluster就创建一个output对象
            # 找到时间和步数变量
            time = f.readline().strip().split(':')[1]
            step = f.readline().strip().split(':')[1]
            total_clu_num = f.readline()[16:]
            # 用时间和步数初始化一个output对象
            temp_output = op.Output(time, step, total_clu_num)

            line = f.readline()
            line = line.split()

            while line and line[0].isdigit():
                # 定义kind数组
                kind = [line[2], line[4], line[6], line[8]]
                pos = [line[9], line[10], line[11]]
                # print(kind, pos)
                # 创建临时cluster
                temp_cluster = clu.Cluster()
                # 给临时cluster赋值
                temp_cluster.assign_kind(kind)
                temp_cluster.assign_pos(pos)
                # 将临时cluster添加到output对象中
                temp_output.add_cluster(temp_cluster)
                # 读取一次output中的迭代
                line = f.readline()
                line = line.split()

            # 将temp_output 加到output_list中
            output_list.append(temp_output)

            if len(output_list) > 100:
                for i in range(len(output_list)):
                    time_list.append(output_list[i].get_time())
                    he_atom_num_list.append(output_list[i].get_he_atom_num())
                    he_clu_num_list.append(output_list[i].get_he_clu_num())
                output_list.clear()

            print(count, len(output_list))
            count += 1
    # 添加最后一个output
    output_list.append(temp_output)

    # 获得output_list 开始遍历
    for i in range(len(output_list)):
        time_list.append(output_list[i].get_time())
        he_atom_num_list.append(output_list[i].get_he_atom_num())
        he_clu_num_list.append(output_list[i].get_he_clu_num())

    # 可以准备数据处理
    plt.plot(time_list, he_atom_num_list)
    plt.xscale('log')
    plt.show()
    input()

    plt.xscale('log')
    plt.plot(time_list, he_clu_num_list)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = 'D:\\OKMC\\更改trap_mutation\\1000K\\500appmBe\\OUTPUT_NEW\\2021y10m7d16h8m49s' \
               '\\cluster_output.txt'
    read_data(filename)