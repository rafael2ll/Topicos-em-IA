from .distance.euclidean_distance import EuclideanDistance


def calc_swc(instanceDataset):
    distance = EuclideanDistance()
    silhuetas = []
    for i, instance in enumerate(instanceDataset.instances):
        distances_inner_cluster = []
        distances_other_cluster = []
        for j, other_instance in enumerate(instanceDataset.instances):
            if i is not j and other_instance.group == instance.group:
                d = distance.calc_dist(instance.row, other_instance.row)
                print("[SAME]Distance {} to {}: {}".format(i + 1, j + 1, d))
                distances_inner_cluster.append(d)
            elif i is not j and other_instance.group != instance.group:
                d = distance.calc_dist(instance.row, other_instance.row)
                print("[OTHER]Distance {} to {}: {}".format(i + 1, j + 1, d))
                distances_other_cluster.append(d)

        m_inner = sum(distances_inner_cluster) / len(distances_inner_cluster)
        m_outer = sum(distances_other_cluster) / len(distances_other_cluster)
        silhueta = (m_outer - m_inner) / max([m_outer, m_inner])
        silhuetas.append(silhueta)
        print("Mean distance of {} to cluster {}: {}".format(i + 1, instance.group, m_inner))
        print("Mean distance of {} to other cluster: {}".format(i + 1, m_outer))
        print("Silhuette: ({} - {})/ {} = {}".format(m_outer, m_inner, max([m_outer, m_inner]), silhueta))
        print("*" * 40)

    swc = (1 / instanceDataset.rows) * sum(silhuetas)
    print(
        "SWC= (1/{})x{}= {:.3f}".format(instanceDataset.rows, " + ".join(["{:.2f}".format(a) for a in silhuetas]), swc))
    return swc


def calc_sswc(instanceDataset, kmeans):
    print("-" * 56)
    print("{}{}{}".format(":" * 25, " SSWC ", ":" * 25))
    print("-" * 56)

    distance = EuclideanDistance()
    silhuetas = []
    for i, instance in enumerate(instanceDataset.instances):
        m_inner = distance.calc_dist(instance.row, kmeans.centroids[instance.group])
        m_outer = None
        j = 0
        for c_idex, centroid in enumerate(kmeans.centroids):
            if c_idex == instance.group:
                continue
            m = distance.calc_dist(instance.row, centroid)
            if not m_outer or m_outer > m:
                m_outer = m
                j = c_idex
        silhueta = (m_outer - m_inner) / max([m_outer, m_inner])
        silhuetas.append(silhueta)
        print("Mean distance of {} to his cluster centroid {}: {:.2f}".format(i + 1, instance.group, m_inner))
        print("Mean distance of {} to centroid[{}]: {:.2f}".format(i + 1, j, m_outer))
        print(
            "Silhuette: ({:.2f} - {:.2f})/ {:.2f} = {:.2f}".format(m_outer, m_inner, max([m_outer, m_inner]), silhueta))
        print("*" * 40)

    swc = (1 / instanceDataset.rows) * sum(silhuetas)
    print(
        "SSWC= (1/{})x({})= {:.3f}".format(instanceDataset.rows, " + ".join(["{:.2f}".format(a) for a in silhuetas]),
                                         swc))
    print("-"*56)
    return swc
