#!/bin/sh

kubens ito1 && kubectl patch deployments wordpress -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "sail-5"}}}}}'
kubens ito2 && kubectl patch deployments wordpress -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "sail-3"}}}}}'
kubens ito3 && kubectl patch deployments wordpress -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "sail-4"}}}}}'
kubens ito4 && kubectl patch deployments wordpress -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "sail-4"}}}}}'
kubens ito5 && kubectl patch deployments wordpress -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "sail-5"}}}}}'
kubens ito6 && kubectl patch deployments wordpress -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "sail-3"}}}}}'
kubens ito7 && kubectl patch deployments wordpress -p '{"spec": {"template": {"spec": {"nodeSelector": {"kubernetes.io/hostname": "sail-5"}}}}}'