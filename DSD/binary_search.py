# coding: utf-8

"""
二分查找的四种变形
"""


def search_first_item1(array, target):
    """
    查找第一个匹配的元素, 第一种写法
    :return:
    """
    if not array:
        return -1

    start, end = 0, len(array) - 1

    while start <= end:  # FIXME: 这里有可能会出现死循环
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        elif array[mid] < target:
            start = mid
        else:  # 这个时候需要看mid是不是第一个与target相等的元素
            if mid == 0 or array[mid - 1] != target:
                return mid
            else:
                end = mid
    return -1


def search_first_item2(array, target):
    """
    查找第一个匹配的元素, 第一种写法
    :param array:
    :param target:
    :return:
    """
    if not array:
        return -1

    start, end = 0, len(array) - 1

    while start + 1 < end:
        mid = (start + end) / 2
        if array[mid] == target:
            end = mid
        elif array[mid] > target:
            end = mid
        elif array[mid] < target:
            start = mid

    if array[start] == target:
        return start

    if array[end] == target:
        return end

    return -1


def search_last_item(array, target):
    """
    查找最后一个匹配的元素
    :return:
    """
    if not array:
        return -1

    start, end = 0, len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid
        elif array[mid] < target:
            start = mid
        else:  # 这个时候需要看mid是不是最后一个与target相等的元素
            if array[mid + 1] != target:
                # mid+1 != target说明 下一个元素也不等于，
                return mid
            else:
                start = mid
    return -1



"""

systemctl stop firewalld
setenforce 0
sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config
swapoff -a

cat >> /etc/hosts << EOF
10.13.1.11 master1
10.13.1.15 node1
10.13.1.16 node2
EOF


yum install chrony -y
systemctl start chronyd
systemctl enable chronyd
chronyc sources


cat > /etc/sysctl.d/k8s.conf << EOF
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sysctl --system


modprobe -- ip_vs
modprobe -- ip_vs_rr
modprobe -- ip_vs_wrr
modprobe -- ip_vs_sh
modprobe -- nf_conntrack_ipv4
lsmod | grep ip_vs
lsmod | grep nf_conntrack_ipv4
yum install -y ipvsadm



wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo -O /etc/yum.repos.d/docker-ce.repo

yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo


if __name__ == '__main__':
    a = [1,3,4,5,6,8,8,8,11,18]
    t = 8
    print(search_first_item2(a, t))




kube-apiserver:v1.18.8                 # node节点不需要
kube-controller-manager:v1.18.8 # node节点不需要
kube-scheduler:v1.18.8                # node节点不需要
kube-proxy:v1.18.8
pause:3.2
etcd:3.4.3-0                                  # node节点不需要
coredns:1.6.7




kubeadm join 10.13.1.11:6443 --token abcdef.0123456789abcdef  --discovery-token-ca-cert-hash sha256:c214cf4c42766dd3d4ab2842c11efbefd54aa445993708ccdbdb8f111658445e

"""