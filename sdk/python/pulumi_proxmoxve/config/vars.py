# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

import types

__config__ = pulumi.Config('proxmoxve')


class _ExportableConfig(types.ModuleType):
    @property
    def virtual_environment(self) -> Optional[str]:
        return __config__.get('virtualEnvironment')
