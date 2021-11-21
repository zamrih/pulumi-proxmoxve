// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export function getClusterAliases(opts?: pulumi.InvokeOptions): Promise<GetClusterAliasesResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("proxmoxve:Cluster/getClusterAliases:getClusterAliases", {
    }, opts);
}

/**
 * A collection of values returned by getClusterAliases.
 */
export interface GetClusterAliasesResult {
    readonly aliasIds: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}