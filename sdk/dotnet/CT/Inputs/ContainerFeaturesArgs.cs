// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.CT.Inputs
{

    public sealed class ContainerFeaturesArgs : global::Pulumi.ResourceArgs
    {
        [Input("nesting")]
        public Input<bool>? Nesting { get; set; }

        public ContainerFeaturesArgs()
        {
        }
        public static new ContainerFeaturesArgs Empty => new ContainerFeaturesArgs();
    }
}