# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'ContainerClone',
    'ContainerConsole',
    'ContainerCpu',
    'ContainerDisk',
    'ContainerFeatures',
    'ContainerInitialization',
    'ContainerInitializationDns',
    'ContainerInitializationIpConfig',
    'ContainerInitializationIpConfigIpv4',
    'ContainerInitializationIpConfigIpv6',
    'ContainerInitializationUserAccount',
    'ContainerMemory',
    'ContainerMountPoint',
    'ContainerNetworkInterface',
    'ContainerOperatingSystem',
]

@pulumi.output_type
class ContainerClone(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vmId":
            suggest = "vm_id"
        elif key == "datastoreId":
            suggest = "datastore_id"
        elif key == "nodeName":
            suggest = "node_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerClone. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerClone.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerClone.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 vm_id: int,
                 datastore_id: Optional[str] = None,
                 node_name: Optional[str] = None):
        """
        :param int vm_id: The container identifier
        :param str datastore_id: The identifier for the datastore to create the
               disk in (defaults to `local`).
        :param str node_name: The name of the node to assign the container to.
        """
        ContainerClone._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            vm_id=vm_id,
            datastore_id=datastore_id,
            node_name=node_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             vm_id: Optional[int] = None,
             datastore_id: Optional[str] = None,
             node_name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if vm_id is None and 'vmId' in kwargs:
            vm_id = kwargs['vmId']
        if vm_id is None:
            raise TypeError("Missing 'vm_id' argument")
        if datastore_id is None and 'datastoreId' in kwargs:
            datastore_id = kwargs['datastoreId']
        if node_name is None and 'nodeName' in kwargs:
            node_name = kwargs['nodeName']

        _setter("vm_id", vm_id)
        if datastore_id is not None:
            _setter("datastore_id", datastore_id)
        if node_name is not None:
            _setter("node_name", node_name)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> int:
        """
        The container identifier
        """
        return pulumi.get(self, "vm_id")

    @property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> Optional[str]:
        """
        The identifier for the datastore to create the
        disk in (defaults to `local`).
        """
        return pulumi.get(self, "datastore_id")

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[str]:
        """
        The name of the node to assign the container to.
        """
        return pulumi.get(self, "node_name")


@pulumi.output_type
class ContainerConsole(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ttyCount":
            suggest = "tty_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerConsole. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerConsole.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerConsole.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 tty_count: Optional[int] = None,
                 type: Optional[str] = None):
        """
        :param bool enabled: Whether to enable the network device (defaults
               to `true`).
        :param int tty_count: The number of available TTY (defaults to `2`).
        :param str type: The type (defaults to `unmanaged`).
        """
        ContainerConsole._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
            tty_count=tty_count,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: Optional[bool] = None,
             tty_count: Optional[int] = None,
             type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if tty_count is None and 'ttyCount' in kwargs:
            tty_count = kwargs['ttyCount']

        if enabled is not None:
            _setter("enabled", enabled)
        if tty_count is not None:
            _setter("tty_count", tty_count)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Whether to enable the network device (defaults
        to `true`).
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="ttyCount")
    def tty_count(self) -> Optional[int]:
        """
        The number of available TTY (defaults to `2`).
        """
        return pulumi.get(self, "tty_count")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type (defaults to `unmanaged`).
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ContainerCpu(dict):
    def __init__(__self__, *,
                 architecture: Optional[str] = None,
                 cores: Optional[int] = None,
                 units: Optional[int] = None):
        """
        :param str architecture: The CPU architecture (defaults to `amd64`).
        :param int cores: The number of CPU cores (defaults to `1`).
        :param int units: The CPU units (defaults to `1024`).
        """
        ContainerCpu._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            architecture=architecture,
            cores=cores,
            units=units,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             architecture: Optional[str] = None,
             cores: Optional[int] = None,
             units: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if architecture is not None:
            _setter("architecture", architecture)
        if cores is not None:
            _setter("cores", cores)
        if units is not None:
            _setter("units", units)

    @property
    @pulumi.getter
    def architecture(self) -> Optional[str]:
        """
        The CPU architecture (defaults to `amd64`).
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def cores(self) -> Optional[int]:
        """
        The number of CPU cores (defaults to `1`).
        """
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter
    def units(self) -> Optional[int]:
        """
        The CPU units (defaults to `1024`).
        """
        return pulumi.get(self, "units")


@pulumi.output_type
class ContainerDisk(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "datastoreId":
            suggest = "datastore_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerDisk. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerDisk.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerDisk.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 datastore_id: Optional[str] = None,
                 size: Optional[int] = None):
        """
        :param str datastore_id: The identifier for the datastore to create the
               disk in (defaults to `local`).
        :param int size: Volume size (only for ZFS storage backed mount points).
               Can be specified with a unit suffix (e.g. `10G`).
        """
        ContainerDisk._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            datastore_id=datastore_id,
            size=size,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             datastore_id: Optional[str] = None,
             size: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if datastore_id is None and 'datastoreId' in kwargs:
            datastore_id = kwargs['datastoreId']

        if datastore_id is not None:
            _setter("datastore_id", datastore_id)
        if size is not None:
            _setter("size", size)

    @property
    @pulumi.getter(name="datastoreId")
    def datastore_id(self) -> Optional[str]:
        """
        The identifier for the datastore to create the
        disk in (defaults to `local`).
        """
        return pulumi.get(self, "datastore_id")

    @property
    @pulumi.getter
    def size(self) -> Optional[int]:
        """
        Volume size (only for ZFS storage backed mount points).
        Can be specified with a unit suffix (e.g. `10G`).
        """
        return pulumi.get(self, "size")


@pulumi.output_type
class ContainerFeatures(dict):
    def __init__(__self__, *,
                 fuse: Optional[bool] = None,
                 keyctl: Optional[bool] = None,
                 nesting: Optional[bool] = None):
        """
        :param bool fuse: Whether the container supports FUSE mounts (defaults
               to `false`)
        :param bool keyctl: Whether the container supports `keyctl()` system
               call (defaults to `false`)
        :param bool nesting: Whether the container is nested (defaults
               to `false`)
        """
        ContainerFeatures._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            fuse=fuse,
            keyctl=keyctl,
            nesting=nesting,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             fuse: Optional[bool] = None,
             keyctl: Optional[bool] = None,
             nesting: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if fuse is not None:
            _setter("fuse", fuse)
        if keyctl is not None:
            _setter("keyctl", keyctl)
        if nesting is not None:
            _setter("nesting", nesting)

    @property
    @pulumi.getter
    def fuse(self) -> Optional[bool]:
        """
        Whether the container supports FUSE mounts (defaults
        to `false`)
        """
        return pulumi.get(self, "fuse")

    @property
    @pulumi.getter
    def keyctl(self) -> Optional[bool]:
        """
        Whether the container supports `keyctl()` system
        call (defaults to `false`)
        """
        return pulumi.get(self, "keyctl")

    @property
    @pulumi.getter
    def nesting(self) -> Optional[bool]:
        """
        Whether the container is nested (defaults
        to `false`)
        """
        return pulumi.get(self, "nesting")


@pulumi.output_type
class ContainerInitialization(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ipConfigs":
            suggest = "ip_configs"
        elif key == "userAccount":
            suggest = "user_account"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerInitialization. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerInitialization.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerInitialization.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dns: Optional['outputs.ContainerInitializationDns'] = None,
                 hostname: Optional[str] = None,
                 ip_configs: Optional[Sequence['outputs.ContainerInitializationIpConfig']] = None,
                 user_account: Optional['outputs.ContainerInitializationUserAccount'] = None):
        """
        :param 'ContainerInitializationDnsArgs' dns: The DNS configuration.
        :param str hostname: The hostname.
        :param Sequence['ContainerInitializationIpConfigArgs'] ip_configs: The IP configuration (one block per network
               device).
        :param 'ContainerInitializationUserAccountArgs' user_account: The user account configuration.
        """
        ContainerInitialization._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            dns=dns,
            hostname=hostname,
            ip_configs=ip_configs,
            user_account=user_account,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             dns: Optional['outputs.ContainerInitializationDns'] = None,
             hostname: Optional[str] = None,
             ip_configs: Optional[Sequence['outputs.ContainerInitializationIpConfig']] = None,
             user_account: Optional['outputs.ContainerInitializationUserAccount'] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if ip_configs is None and 'ipConfigs' in kwargs:
            ip_configs = kwargs['ipConfigs']
        if user_account is None and 'userAccount' in kwargs:
            user_account = kwargs['userAccount']

        if dns is not None:
            _setter("dns", dns)
        if hostname is not None:
            _setter("hostname", hostname)
        if ip_configs is not None:
            _setter("ip_configs", ip_configs)
        if user_account is not None:
            _setter("user_account", user_account)

    @property
    @pulumi.getter
    def dns(self) -> Optional['outputs.ContainerInitializationDns']:
        """
        The DNS configuration.
        """
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        The hostname.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="ipConfigs")
    def ip_configs(self) -> Optional[Sequence['outputs.ContainerInitializationIpConfig']]:
        """
        The IP configuration (one block per network
        device).
        """
        return pulumi.get(self, "ip_configs")

    @property
    @pulumi.getter(name="userAccount")
    def user_account(self) -> Optional['outputs.ContainerInitializationUserAccount']:
        """
        The user account configuration.
        """
        return pulumi.get(self, "user_account")


@pulumi.output_type
class ContainerInitializationDns(dict):
    def __init__(__self__, *,
                 domain: Optional[str] = None,
                 server: Optional[str] = None):
        """
        :param str domain: The DNS search domain.
        :param str server: The DNS server.
        """
        ContainerInitializationDns._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain=domain,
            server=server,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain: Optional[str] = None,
             server: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if domain is not None:
            _setter("domain", domain)
        if server is not None:
            _setter("server", server)

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        """
        The DNS search domain.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def server(self) -> Optional[str]:
        """
        The DNS server.
        """
        return pulumi.get(self, "server")


@pulumi.output_type
class ContainerInitializationIpConfig(dict):
    def __init__(__self__, *,
                 ipv4: Optional['outputs.ContainerInitializationIpConfigIpv4'] = None,
                 ipv6: Optional['outputs.ContainerInitializationIpConfigIpv6'] = None):
        """
        :param 'ContainerInitializationIpConfigIpv4Args' ipv4: The IPv4 configuration.
        :param 'ContainerInitializationIpConfigIpv6Args' ipv6: The IPv4 configuration.
        """
        ContainerInitializationIpConfig._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ipv4=ipv4,
            ipv6=ipv6,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ipv4: Optional['outputs.ContainerInitializationIpConfigIpv4'] = None,
             ipv6: Optional['outputs.ContainerInitializationIpConfigIpv6'] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if ipv4 is not None:
            _setter("ipv4", ipv4)
        if ipv6 is not None:
            _setter("ipv6", ipv6)

    @property
    @pulumi.getter
    def ipv4(self) -> Optional['outputs.ContainerInitializationIpConfigIpv4']:
        """
        The IPv4 configuration.
        """
        return pulumi.get(self, "ipv4")

    @property
    @pulumi.getter
    def ipv6(self) -> Optional['outputs.ContainerInitializationIpConfigIpv6']:
        """
        The IPv4 configuration.
        """
        return pulumi.get(self, "ipv6")


@pulumi.output_type
class ContainerInitializationIpConfigIpv4(dict):
    def __init__(__self__, *,
                 address: Optional[str] = None,
                 gateway: Optional[str] = None):
        """
        :param str address: The IPv6 address (use `dhcp` for
               autodiscovery).
        :param str gateway: The IPv6 gateway (must be omitted
               when `dhcp` is used as the address).
        """
        ContainerInitializationIpConfigIpv4._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address=address,
            gateway=gateway,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address: Optional[str] = None,
             gateway: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if address is not None:
            _setter("address", address)
        if gateway is not None:
            _setter("gateway", gateway)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The IPv6 address (use `dhcp` for
        autodiscovery).
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def gateway(self) -> Optional[str]:
        """
        The IPv6 gateway (must be omitted
        when `dhcp` is used as the address).
        """
        return pulumi.get(self, "gateway")


@pulumi.output_type
class ContainerInitializationIpConfigIpv6(dict):
    def __init__(__self__, *,
                 address: Optional[str] = None,
                 gateway: Optional[str] = None):
        """
        :param str address: The IPv6 address (use `dhcp` for
               autodiscovery).
        :param str gateway: The IPv6 gateway (must be omitted
               when `dhcp` is used as the address).
        """
        ContainerInitializationIpConfigIpv6._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address=address,
            gateway=gateway,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address: Optional[str] = None,
             gateway: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if address is not None:
            _setter("address", address)
        if gateway is not None:
            _setter("gateway", gateway)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The IPv6 address (use `dhcp` for
        autodiscovery).
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def gateway(self) -> Optional[str]:
        """
        The IPv6 gateway (must be omitted
        when `dhcp` is used as the address).
        """
        return pulumi.get(self, "gateway")


@pulumi.output_type
class ContainerInitializationUserAccount(dict):
    def __init__(__self__, *,
                 keys: Optional[Sequence[str]] = None,
                 password: Optional[str] = None):
        """
        :param Sequence[str] keys: The SSH keys for the root account.
        :param str password: The password for the root account.
        """
        ContainerInitializationUserAccount._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            keys=keys,
            password=password,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             keys: Optional[Sequence[str]] = None,
             password: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if keys is not None:
            _setter("keys", keys)
        if password is not None:
            _setter("password", password)

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[str]]:
        """
        The SSH keys for the root account.
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        The password for the root account.
        """
        return pulumi.get(self, "password")


@pulumi.output_type
class ContainerMemory(dict):
    def __init__(__self__, *,
                 dedicated: Optional[int] = None,
                 swap: Optional[int] = None):
        """
        :param int dedicated: The dedicated memory in megabytes (defaults
               to `512`).
        :param int swap: The swap size in megabytes (defaults to `0`).
        """
        ContainerMemory._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            dedicated=dedicated,
            swap=swap,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             dedicated: Optional[int] = None,
             swap: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if dedicated is not None:
            _setter("dedicated", dedicated)
        if swap is not None:
            _setter("swap", swap)

    @property
    @pulumi.getter
    def dedicated(self) -> Optional[int]:
        """
        The dedicated memory in megabytes (defaults
        to `512`).
        """
        return pulumi.get(self, "dedicated")

    @property
    @pulumi.getter
    def swap(self) -> Optional[int]:
        """
        The swap size in megabytes (defaults to `0`).
        """
        return pulumi.get(self, "swap")


@pulumi.output_type
class ContainerMountPoint(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "mountOptions":
            suggest = "mount_options"
        elif key == "readOnly":
            suggest = "read_only"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerMountPoint. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerMountPoint.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerMountPoint.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 path: str,
                 volume: str,
                 acl: Optional[bool] = None,
                 backup: Optional[bool] = None,
                 mount_options: Optional[Sequence[str]] = None,
                 quota: Optional[bool] = None,
                 read_only: Optional[bool] = None,
                 replicate: Optional[bool] = None,
                 shared: Optional[bool] = None,
                 size: Optional[str] = None):
        """
        :param str path: Path to the mount point as seen from inside the
               container.
        :param str volume: Volume, device or directory to mount into the
               container.
        :param bool acl: Explicitly enable or disable ACL support.
        :param bool backup: Whether to include the mount point in backups (only
               used for volume mount points).
        :param Sequence[str] mount_options: List of extra mount options.
        :param bool quota: Enable user quotas inside the container (not supported
               with ZFS subvolumes).
        :param bool read_only: Read-only mount point.
        :param bool replicate: Will include this volume to a storage replica job.
        :param bool shared: Mark this non-volume mount point as available on all
               nodes.
        :param str size: Volume size (only for ZFS storage backed mount points).
               Can be specified with a unit suffix (e.g. `10G`).
        """
        ContainerMountPoint._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            path=path,
            volume=volume,
            acl=acl,
            backup=backup,
            mount_options=mount_options,
            quota=quota,
            read_only=read_only,
            replicate=replicate,
            shared=shared,
            size=size,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             path: Optional[str] = None,
             volume: Optional[str] = None,
             acl: Optional[bool] = None,
             backup: Optional[bool] = None,
             mount_options: Optional[Sequence[str]] = None,
             quota: Optional[bool] = None,
             read_only: Optional[bool] = None,
             replicate: Optional[bool] = None,
             shared: Optional[bool] = None,
             size: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if path is None:
            raise TypeError("Missing 'path' argument")
        if volume is None:
            raise TypeError("Missing 'volume' argument")
        if mount_options is None and 'mountOptions' in kwargs:
            mount_options = kwargs['mountOptions']
        if read_only is None and 'readOnly' in kwargs:
            read_only = kwargs['readOnly']

        _setter("path", path)
        _setter("volume", volume)
        if acl is not None:
            _setter("acl", acl)
        if backup is not None:
            _setter("backup", backup)
        if mount_options is not None:
            _setter("mount_options", mount_options)
        if quota is not None:
            _setter("quota", quota)
        if read_only is not None:
            _setter("read_only", read_only)
        if replicate is not None:
            _setter("replicate", replicate)
        if shared is not None:
            _setter("shared", shared)
        if size is not None:
            _setter("size", size)

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path to the mount point as seen from inside the
        container.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def volume(self) -> str:
        """
        Volume, device or directory to mount into the
        container.
        """
        return pulumi.get(self, "volume")

    @property
    @pulumi.getter
    def acl(self) -> Optional[bool]:
        """
        Explicitly enable or disable ACL support.
        """
        return pulumi.get(self, "acl")

    @property
    @pulumi.getter
    def backup(self) -> Optional[bool]:
        """
        Whether to include the mount point in backups (only
        used for volume mount points).
        """
        return pulumi.get(self, "backup")

    @property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[Sequence[str]]:
        """
        List of extra mount options.
        """
        return pulumi.get(self, "mount_options")

    @property
    @pulumi.getter
    def quota(self) -> Optional[bool]:
        """
        Enable user quotas inside the container (not supported
        with ZFS subvolumes).
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[bool]:
        """
        Read-only mount point.
        """
        return pulumi.get(self, "read_only")

    @property
    @pulumi.getter
    def replicate(self) -> Optional[bool]:
        """
        Will include this volume to a storage replica job.
        """
        return pulumi.get(self, "replicate")

    @property
    @pulumi.getter
    def shared(self) -> Optional[bool]:
        """
        Mark this non-volume mount point as available on all
        nodes.
        """
        return pulumi.get(self, "shared")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        Volume size (only for ZFS storage backed mount points).
        Can be specified with a unit suffix (e.g. `10G`).
        """
        return pulumi.get(self, "size")


@pulumi.output_type
class ContainerNetworkInterface(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "macAddress":
            suggest = "mac_address"
        elif key == "rateLimit":
            suggest = "rate_limit"
        elif key == "vlanId":
            suggest = "vlan_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerNetworkInterface. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerNetworkInterface.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerNetworkInterface.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 bridge: Optional[str] = None,
                 enabled: Optional[bool] = None,
                 firewall: Optional[bool] = None,
                 mac_address: Optional[str] = None,
                 mtu: Optional[int] = None,
                 rate_limit: Optional[float] = None,
                 vlan_id: Optional[int] = None):
        """
        :param str name: The network interface name.
        :param str bridge: The name of the network bridge (defaults
               to `vmbr0`).
        :param bool enabled: Whether to enable the network device (defaults
               to `true`).
        :param bool firewall: Whether this interface's firewall rules should be
               used (defaults to `false`).
        :param str mac_address: The MAC address.
        :param int mtu: Maximum transfer unit of the interface. Cannot be
               larger than the bridge's MTU.
        :param float rate_limit: The rate limit in megabytes per second.
        :param int vlan_id: The VLAN identifier.
        """
        ContainerNetworkInterface._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            bridge=bridge,
            enabled=enabled,
            firewall=firewall,
            mac_address=mac_address,
            mtu=mtu,
            rate_limit=rate_limit,
            vlan_id=vlan_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             bridge: Optional[str] = None,
             enabled: Optional[bool] = None,
             firewall: Optional[bool] = None,
             mac_address: Optional[str] = None,
             mtu: Optional[int] = None,
             rate_limit: Optional[float] = None,
             vlan_id: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if mac_address is None and 'macAddress' in kwargs:
            mac_address = kwargs['macAddress']
        if rate_limit is None and 'rateLimit' in kwargs:
            rate_limit = kwargs['rateLimit']
        if vlan_id is None and 'vlanId' in kwargs:
            vlan_id = kwargs['vlanId']

        _setter("name", name)
        if bridge is not None:
            _setter("bridge", bridge)
        if enabled is not None:
            _setter("enabled", enabled)
        if firewall is not None:
            _setter("firewall", firewall)
        if mac_address is not None:
            _setter("mac_address", mac_address)
        if mtu is not None:
            _setter("mtu", mtu)
        if rate_limit is not None:
            _setter("rate_limit", rate_limit)
        if vlan_id is not None:
            _setter("vlan_id", vlan_id)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The network interface name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def bridge(self) -> Optional[str]:
        """
        The name of the network bridge (defaults
        to `vmbr0`).
        """
        return pulumi.get(self, "bridge")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Whether to enable the network device (defaults
        to `true`).
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def firewall(self) -> Optional[bool]:
        """
        Whether this interface's firewall rules should be
        used (defaults to `false`).
        """
        return pulumi.get(self, "firewall")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[str]:
        """
        The MAC address.
        """
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def mtu(self) -> Optional[int]:
        """
        Maximum transfer unit of the interface. Cannot be
        larger than the bridge's MTU.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter(name="rateLimit")
    def rate_limit(self) -> Optional[float]:
        """
        The rate limit in megabytes per second.
        """
        return pulumi.get(self, "rate_limit")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> Optional[int]:
        """
        The VLAN identifier.
        """
        return pulumi.get(self, "vlan_id")


@pulumi.output_type
class ContainerOperatingSystem(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "templateFileId":
            suggest = "template_file_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerOperatingSystem. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerOperatingSystem.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerOperatingSystem.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 template_file_id: str,
                 type: Optional[str] = None):
        """
        :param str template_file_id: The identifier for an OS template file.
        :param str type: The type (defaults to `unmanaged`).
        """
        ContainerOperatingSystem._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            template_file_id=template_file_id,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             template_file_id: Optional[str] = None,
             type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if template_file_id is None and 'templateFileId' in kwargs:
            template_file_id = kwargs['templateFileId']
        if template_file_id is None:
            raise TypeError("Missing 'template_file_id' argument")

        _setter("template_file_id", template_file_id)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter(name="templateFileId")
    def template_file_id(self) -> str:
        """
        The identifier for an OS template file.
        """
        return pulumi.get(self, "template_file_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type (defaults to `unmanaged`).
        """
        return pulumi.get(self, "type")


