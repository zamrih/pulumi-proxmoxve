// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.CT.Outputs
{

    [OutputType]
    public sealed class ContainerFeatures
    {
        /// <summary>
        /// Whether the container supports FUSE mounts (defaults
        /// to `false`)
        /// </summary>
        public readonly bool? Fuse;
        /// <summary>
        /// Whether the container supports `keyctl()` system
        /// call (defaults to `false`)
        /// </summary>
        public readonly bool? Keyctl;
        /// <summary>
        /// Whether the container is nested (defaults
        /// to `false`)
        /// </summary>
        public readonly bool? Nesting;

        [OutputConstructor]
        private ContainerFeatures(
            bool? fuse,

            bool? keyctl,

            bool? nesting)
        {
            Fuse = fuse;
            Keyctl = keyctl;
            Nesting = nesting;
        }
    }
}
