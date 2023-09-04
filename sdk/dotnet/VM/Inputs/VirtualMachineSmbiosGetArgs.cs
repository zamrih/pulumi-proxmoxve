// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.VM.Inputs
{

    public sealed class VirtualMachineSmbiosGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("family")]
        public Input<string>? Family { get; set; }

        [Input("manufacturer")]
        public Input<string>? Manufacturer { get; set; }

        [Input("product")]
        public Input<string>? Product { get; set; }

        [Input("serial")]
        public Input<string>? Serial { get; set; }

        [Input("sku")]
        public Input<string>? Sku { get; set; }

        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        [Input("version")]
        public Input<string>? Version { get; set; }

        public VirtualMachineSmbiosGetArgs()
        {
        }
        public static new VirtualMachineSmbiosGetArgs Empty => new VirtualMachineSmbiosGetArgs();
    }
}