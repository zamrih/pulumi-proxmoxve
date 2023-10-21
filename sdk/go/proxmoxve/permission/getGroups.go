// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package permission

import (
	"context"
	"reflect"

	"github.com/muhlba91/pulumi-proxmoxve/sdk/v5/go/proxmoxve/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Retrieves basic information about all available user groups.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/muhlba91/pulumi-proxmoxve/sdk/v5/go/proxmoxve/Permission"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Permission.GetGroups(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetGroups(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetGroupsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetGroupsResult
	err := ctx.Invoke("proxmoxve:Permission/getGroups:getGroups", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getGroups.
type GetGroupsResult struct {
	// The group comments.
	Comments []string `pulumi:"comments"`
	// The group identifiers.
	GroupIds []string `pulumi:"groupIds"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
}

func GetGroupsOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetGroupsResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetGroupsResult, error) {
		r, err := GetGroups(ctx, opts...)
		var s GetGroupsResult
		if r != nil {
			s = *r
		}
		return s, err
	}).(GetGroupsResultOutput)
}

// A collection of values returned by getGroups.
type GetGroupsResultOutput struct{ *pulumi.OutputState }

func (GetGroupsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetGroupsResult)(nil)).Elem()
}

func (o GetGroupsResultOutput) ToGetGroupsResultOutput() GetGroupsResultOutput {
	return o
}

func (o GetGroupsResultOutput) ToGetGroupsResultOutputWithContext(ctx context.Context) GetGroupsResultOutput {
	return o
}

func (o GetGroupsResultOutput) ToOutput(ctx context.Context) pulumix.Output[GetGroupsResult] {
	return pulumix.Output[GetGroupsResult]{
		OutputState: o.OutputState,
	}
}

// The group comments.
func (o GetGroupsResultOutput) Comments() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetGroupsResult) []string { return v.Comments }).(pulumi.StringArrayOutput)
}

// The group identifiers.
func (o GetGroupsResultOutput) GroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetGroupsResult) []string { return v.GroupIds }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetGroupsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetGroupsResult) string { return v.Id }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetGroupsResultOutput{})
}
