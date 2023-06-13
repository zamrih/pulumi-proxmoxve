# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'FirewallIPSetCidrArgs',
    'FirewallLogRatelimitArgs',
    'FirewallRulesRuleArgs',
    'FirewallSecurityGroupRuleArgs',
]

@pulumi.input_type
class FirewallIPSetCidrArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 comment: Optional[pulumi.Input[str]] = None,
                 nomatch: Optional[pulumi.Input[bool]] = None):
        pulumi.set(__self__, "name", name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if nomatch is not None:
            pulumi.set(__self__, "nomatch", nomatch)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def nomatch(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "nomatch")

    @nomatch.setter
    def nomatch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "nomatch", value)


@pulumi.input_type
class FirewallLogRatelimitArgs:
    def __init__(__self__, *,
                 burst: Optional[pulumi.Input[int]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 rate: Optional[pulumi.Input[str]] = None):
        if burst is not None:
            pulumi.set(__self__, "burst", burst)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if rate is not None:
            pulumi.set(__self__, "rate", rate)

    @property
    @pulumi.getter
    def burst(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "burst")

    @burst.setter
    def burst(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "burst", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def rate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "rate")

    @rate.setter
    def rate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rate", value)


@pulumi.input_type
class FirewallRulesRuleArgs:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dest: Optional[pulumi.Input[str]] = None,
                 dport: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 iface: Optional[pulumi.Input[str]] = None,
                 log: Optional[pulumi.Input[str]] = None,
                 macro: Optional[pulumi.Input[str]] = None,
                 pos: Optional[pulumi.Input[int]] = None,
                 proto: Optional[pulumi.Input[str]] = None,
                 security_group: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 sport: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        if action is not None:
            pulumi.set(__self__, "action", action)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if dest is not None:
            pulumi.set(__self__, "dest", dest)
        if dport is not None:
            pulumi.set(__self__, "dport", dport)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if iface is not None:
            pulumi.set(__self__, "iface", iface)
        if log is not None:
            pulumi.set(__self__, "log", log)
        if macro is not None:
            pulumi.set(__self__, "macro", macro)
        if pos is not None:
            pulumi.set(__self__, "pos", pos)
        if proto is not None:
            pulumi.set(__self__, "proto", proto)
        if security_group is not None:
            pulumi.set(__self__, "security_group", security_group)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if sport is not None:
            pulumi.set(__self__, "sport", sport)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def dest(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dest")

    @dest.setter
    def dest(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dest", value)

    @property
    @pulumi.getter
    def dport(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dport")

    @dport.setter
    def dport(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dport", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def iface(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "iface")

    @iface.setter
    def iface(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iface", value)

    @property
    @pulumi.getter
    def log(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "log")

    @log.setter
    def log(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log", value)

    @property
    @pulumi.getter
    def macro(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "macro")

    @macro.setter
    def macro(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "macro", value)

    @property
    @pulumi.getter
    def pos(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "pos")

    @pos.setter
    def pos(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pos", value)

    @property
    @pulumi.getter
    def proto(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "proto")

    @proto.setter
    def proto(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proto", value)

    @property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_group")

    @security_group.setter
    def security_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_group", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def sport(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sport")

    @sport.setter
    def sport(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sport", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class FirewallSecurityGroupRuleArgs:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 dest: Optional[pulumi.Input[str]] = None,
                 dport: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 iface: Optional[pulumi.Input[str]] = None,
                 log: Optional[pulumi.Input[str]] = None,
                 macro: Optional[pulumi.Input[str]] = None,
                 pos: Optional[pulumi.Input[int]] = None,
                 proto: Optional[pulumi.Input[str]] = None,
                 security_group: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 sport: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        if action is not None:
            pulumi.set(__self__, "action", action)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if dest is not None:
            pulumi.set(__self__, "dest", dest)
        if dport is not None:
            pulumi.set(__self__, "dport", dport)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if iface is not None:
            pulumi.set(__self__, "iface", iface)
        if log is not None:
            pulumi.set(__self__, "log", log)
        if macro is not None:
            pulumi.set(__self__, "macro", macro)
        if pos is not None:
            pulumi.set(__self__, "pos", pos)
        if proto is not None:
            pulumi.set(__self__, "proto", proto)
        if security_group is not None:
            pulumi.set(__self__, "security_group", security_group)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if sport is not None:
            pulumi.set(__self__, "sport", sport)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def dest(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dest")

    @dest.setter
    def dest(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dest", value)

    @property
    @pulumi.getter
    def dport(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dport")

    @dport.setter
    def dport(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dport", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def iface(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "iface")

    @iface.setter
    def iface(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iface", value)

    @property
    @pulumi.getter
    def log(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "log")

    @log.setter
    def log(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log", value)

    @property
    @pulumi.getter
    def macro(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "macro")

    @macro.setter
    def macro(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "macro", value)

    @property
    @pulumi.getter
    def pos(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "pos")

    @pos.setter
    def pos(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pos", value)

    @property
    @pulumi.getter
    def proto(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "proto")

    @proto.setter
    def proto(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proto", value)

    @property
    @pulumi.getter(name="securityGroup")
    def security_group(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_group")

    @security_group.setter
    def security_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_group", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def sport(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sport")

    @sport.setter
    def sport(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sport", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

