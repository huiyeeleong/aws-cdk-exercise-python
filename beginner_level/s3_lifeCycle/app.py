#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from aws_cdk import core

from s3_life_cycle.s3_life_cycle_stack import S3LifeCycleStack


app = core.App()
S3LifeCycleStack(app, "S3LifeCycleStack")

app.synth()
