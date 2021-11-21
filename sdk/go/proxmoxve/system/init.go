// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package system

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/muhlba91/pulumi-proxmoxve/sdk/go/proxmoxve"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "proxmoxve:System/certifi:Certifi":
		r = &Certifi{}
	case "proxmoxve:System/dNS:DNS":
		r = &DNS{}
	case "proxmoxve:System/hosts:Hosts":
		r = &Hosts{}
	case "proxmoxve:System/time:Time":
		r = &Time{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := proxmoxve.PkgVersion()
	if err != nil {
		fmt.Printf("failed to determine package version. defaulting to v1: %v\n", err)
	}
	pulumi.RegisterResourceModule(
		"proxmoxve",
		"System/certifi",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"proxmoxve",
		"System/dNS",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"proxmoxve",
		"System/hosts",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"proxmoxve",
		"System/time",
		&module{version},
	)
}