_base_ = [
    '../_base_/models/faster-rcnn_r50_fpn.py',
    '../_base_/datasets/dsp_detection.py',
    '../_base_/schedules/schedule_50e.py', '../_base_/default_runtime.py'
]

model=dict(
  backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')),
    roi_head=dict(
        bbox_head=dict(
            num_classes=1
        )
    )
)
