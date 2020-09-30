from domain import InstanceDataset, KMeans
from utils import export_dataset

CASES = [2, 3, 4]


def summarize(instanceDataset: InstanceDataset, ys: list):
    purities = []
    for case in CASES:
        print("{} {} {}".format("=" * 10, str(case) + " clusters", "=" * 10))
        kmeans = KMeans(instanceDataset, case)
        kmeans.rotate_all()
        max_per_cluster = {}
        for index, instance in enumerate(instanceDataset.instances):
            export_dataset(instanceDataset, "kmeans_k" + str(case))
            if instance.group not in max_per_cluster.keys():
                max_per_cluster[instance.group] = {}

            if ys[index] not in max_per_cluster[instance.group]:
                max_per_cluster[instance.group][ys[index]] = 0

            max_per_cluster[instance.group][ys[index]] += 1

        print(max_per_cluster)
        max_ys = [max(group.values()) for group in max_per_cluster.values()]
        purity = (1 / instanceDataset.rows) * sum(max_ys)
        purities.append(purity)
        print("Purity {} clusters: {}".format(case, purity))

    lowest_purity = max(enumerate(purities), key=lambda a: a[1])[0]

    print("=" * 40, "\n", "O K-means  de {}  cluster(s) possui maior pureza.".format(CASES[lowest_purity]))
