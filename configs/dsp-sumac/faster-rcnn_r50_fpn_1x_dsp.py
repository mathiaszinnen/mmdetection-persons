_base_ = [
    '../_base_/models/faster-rcnn_r50_fpn.py',
    '../_base_/datasets/dsp_detection.py',
    '../_base_/schedules/schedule_50e.py', '../_base_/default_runtime.py'
]

val_evaluator = dict(
    type='CocoMetric',
    ann_file='/hdd/datasets/dsp/annotations_valid.json',
    metric='bbox',
    format_only=False,
    backend_args=None)
test_evaluator = dict(
    type='CocoMetric',
    ann_file='/hdd/datasets/dsp/annotations_test.json',
    metric='bbox',
    format_only=False,
    backend_args=None)

model=dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1
        )
    )
)
