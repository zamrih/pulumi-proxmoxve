// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Cluster
{
    [ProxmoxVEResourceType("proxmoxve:Cluster/clusterIPSet:ClusterIPSet")]
    public partial class ClusterIPSet : Pulumi.CustomResource
    {
        /// <summary>
        /// List of IP or Networks
        /// </summary>
        [Output("cidrs")]
        public Output<ImmutableArray<Outputs.ClusterIPSetCidr>> Cidrs { get; private set; } = null!;

        /// <summary>
        /// IPSet comment
        /// </summary>
        [Output("comment")]
        public Output<string?> Comment { get; private set; } = null!;

        /// <summary>
        /// IPSet name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterIPSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterIPSet(string name, ClusterIPSetArgs? args = null, CustomResourceOptions? options = null)
            : base("proxmoxve:Cluster/clusterIPSet:ClusterIPSet", name, args ?? new ClusterIPSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ClusterIPSet(string name, Input<string> id, ClusterIPSetState? state = null, CustomResourceOptions? options = null)
            : base("proxmoxve:Cluster/clusterIPSet:ClusterIPSet", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ClusterIPSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterIPSet Get(string name, Input<string> id, ClusterIPSetState? state = null, CustomResourceOptions? options = null)
        {
            return new ClusterIPSet(name, id, state, options);
        }
    }

    public sealed class ClusterIPSetArgs : Pulumi.ResourceArgs
    {
        [Input("cidrs")]
        private InputList<Inputs.ClusterIPSetCidrArgs>? _cidrs;

        /// <summary>
        /// List of IP or Networks
        /// </summary>
        public InputList<Inputs.ClusterIPSetCidrArgs> Cidrs
        {
            get => _cidrs ?? (_cidrs = new InputList<Inputs.ClusterIPSetCidrArgs>());
            set => _cidrs = value;
        }

        /// <summary>
        /// IPSet comment
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// IPSet name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ClusterIPSetArgs()
        {
        }
    }

    public sealed class ClusterIPSetState : Pulumi.ResourceArgs
    {
        [Input("cidrs")]
        private InputList<Inputs.ClusterIPSetCidrGetArgs>? _cidrs;

        /// <summary>
        /// List of IP or Networks
        /// </summary>
        public InputList<Inputs.ClusterIPSetCidrGetArgs> Cidrs
        {
            get => _cidrs ?? (_cidrs = new InputList<Inputs.ClusterIPSetCidrGetArgs>());
            set => _cidrs = value;
        }

        /// <summary>
        /// IPSet comment
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// IPSet name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ClusterIPSetState()
        {
        }
    }
}