#!/usr/bin/env bash


tools/dist_train.sh configs/dsp-sumac/faster-rcnn_r101_fpn_1x_dsp.py 2 --work-dir work_dirs/r101_4/
tools/dist_train.sh configs/dsp-sumac/faster-rcnn_r101_fpn_1x_dsp.py 2 --work-dir work_dirs/r101_5/
