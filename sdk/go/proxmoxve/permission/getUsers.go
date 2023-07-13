// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package permission

import (
	"github.com/muhlba91/pulumi-proxmoxve/sdk/v5/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetUsers(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetUsersResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetUsersResult
	err := ctx.Invoke("proxmoxve:Permission/getUsers:getUsers", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getUsers.
type GetUsersResult struct {
	Comments        []string   `pulumi:"comments"`
	Emails          []string   `pulumi:"emails"`
	Enableds        []bool     `pulumi:"enableds"`
	ExpirationDates []string   `pulumi:"expirationDates"`
	FirstNames      []string   `pulumi:"firstNames"`
	Groups          [][]string `pulumi:"groups"`
	// The provider-assigned unique ID for this managed resource.
	Id        string   `pulumi:"id"`
	Keys      []string `pulumi:"keys"`
	LastNames []string `pulumi:"lastNames"`
	UserIds   []string `pulumi:"userIds"`
}
