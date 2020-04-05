#!/usr/bin/python
import  matplotlib.pyplot  as  plt

HOSTS_PATH = 'hosts'

def get_hosts():
    hosts = set()
    with open(HOSTS_PATH, 'r') as hosts_f:
        for line in hosts_f:
            if line.strip() != '':
                hosts.add(line)
    return hosts

def get_data_for_host(host):
    data = []
    with open(host + '.usage.txt') as f:
        for line in f:
            val = float(line.strip())
            data.append(float(val))
    return data


# MAIN
hosts = get_hosts()

# Common
plt.rcParams.update({'font.size': 20})
fig, axes = plt.subplots(len(hosts), 1, figsize=(12.1, len(hosts) * 6.2), sharex=False)

i = 0
for host in hosts:
    vals = axes[i].get_yticks()
    axes[i].set_yticklabels(['{:,.0%}'.format(x) for x in vals])
    axes[i].set_ylabel("Utilisation")

    axes[i].plot(get_data_for_host(host.strip()))
    axes[i].set_ylim([0, 105])

    i += 1

axes[0].set_title("CPU usage")
axes[len(hosts) - 1].set_xlabel("Time [seconds]")

plt.savefig("utilisation.png", dpi=300, pad_inches = 0.1,  bbox_inches = 'tight',)