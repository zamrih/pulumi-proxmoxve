// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Network
{
    [ProxmoxVEResourceType("proxmoxve:Network/firewallAlias:FirewallAlias")]
    public partial class FirewallAlias : global::Pulumi.CustomResource
    {
        /// <summary>
        /// IP/CIDR block
        /// </summary>
        [Output("cidr")]
        public Output<string> Cidr { get; private set; } = null!;

        /// <summary>
        /// Alias comment
        /// </summary>
        [Output("comment")]
        public Output<string?> Comment { get; private set; } = null!;

        /// <summary>
        /// The ID of the container to manage the firewall for.
        /// </summary>
        [Output("containerId")]
        public Output<int?> ContainerId { get; private set; } = null!;

        /// <summary>
        /// Alias name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the node.
        /// </summary>
        [Output("nodeName")]
        public Output<string?> NodeName { get; private set; } = null!;

        /// <summary>
        /// The ID of the VM to manage the firewall for.
        /// </summary>
        [Output("vmId")]
        public Output<int?> VmId { get; private set; } = null!;


        /// <summary>
        /// Create a FirewallAlias resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FirewallAlias(string name, FirewallAliasArgs args, CustomResourceOptions? options = null)
            : base("proxmoxve:Network/firewallAlias:FirewallAlias", name, args ?? new FirewallAliasArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FirewallAlias(string name, Input<string> id, FirewallAliasState? state = null, CustomResourceOptions? options = null)
            : base("proxmoxve:Network/firewallAlias:FirewallAlias", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/muhlba91/pulumi-proxmoxve",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing FirewallAlias resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FirewallAlias Get(string name, Input<string> id, FirewallAliasState? state = null, CustomResourceOptions? options = null)
        {
            return new FirewallAlias(name, id, state, options);
        }
    }

    public sealed class FirewallAliasArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// IP/CIDR block
        /// </summary>
        [Input("cidr", required: true)]
        public Input<string> Cidr { get; set; } = null!;

        /// <summary>
        /// Alias comment
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// The ID of the container to manage the firewall for.
        /// </summary>
        [Input("containerId")]
        public Input<int>? ContainerId { get; set; }

        /// <summary>
        /// Alias name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the node.
        /// </summary>
        [Input("nodeName")]
        public Input<string>? NodeName { get; set; }

        /// <summary>
        /// The ID of the VM to manage the firewall for.
        /// </summary>
        [Input("vmId")]
        public Input<int>? VmId { get; set; }

        public FirewallAliasArgs()
        {
        }
        public static new FirewallAliasArgs Empty => new FirewallAliasArgs();
    }

    public sealed class FirewallAliasState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// IP/CIDR block
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        /// <summary>
        /// Alias comment
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// The ID of the container to manage the firewall for.
        /// </summary>
        [Input("containerId")]
        public Input<int>? ContainerId { get; set; }

        /// <summary>
        /// Alias name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the node.
        /// </summary>
        [Input("nodeName")]
        public Input<string>? NodeName { get; set; }

        /// <summary>
        /// The ID of the VM to manage the firewall for.
        /// </summary>
        [Input("vmId")]
        public Input<int>? VmId { get; set; }

        public FirewallAliasState()
        {
        }
        public static new FirewallAliasState Empty => new FirewallAliasState();
    }
}