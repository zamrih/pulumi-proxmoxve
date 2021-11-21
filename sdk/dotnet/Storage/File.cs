// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ProxmoxVE.Storage
{
    [ProxmoxVEResourceType("proxmoxve:Storage/file:File")]
    public partial class File : Pulumi.CustomResource
    {
        /// <summary>
        /// The content type
        /// </summary>
        [Output("contentType")]
        public Output<string?> ContentType { get; private set; } = null!;

        /// <summary>
        /// The datastore id
        /// </summary>
        [Output("datastoreId")]
        public Output<string> DatastoreId { get; private set; } = null!;

        /// <summary>
        /// The file modification date
        /// </summary>
        [Output("fileModificationDate")]
        public Output<string> FileModificationDate { get; private set; } = null!;

        /// <summary>
        /// The file name
        /// </summary>
        [Output("fileName")]
        public Output<string> FileName { get; private set; } = null!;

        /// <summary>
        /// The file size in bytes
        /// </summary>
        [Output("fileSize")]
        public Output<int> FileSize { get; private set; } = null!;

        /// <summary>
        /// The file tag
        /// </summary>
        [Output("fileTag")]
        public Output<string> FileTag { get; private set; } = null!;

        /// <summary>
        /// The node name
        /// </summary>
        [Output("nodeName")]
        public Output<string> NodeName { get; private set; } = null!;

        /// <summary>
        /// The source file
        /// </summary>
        [Output("sourceFile")]
        public Output<Outputs.FileSourceFile?> SourceFile { get; private set; } = null!;

        /// <summary>
        /// The raw source
        /// </summary>
        [Output("sourceRaw")]
        public Output<Outputs.FileSourceRaw?> SourceRaw { get; private set; } = null!;


        /// <summary>
        /// Create a File resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public File(string name, FileArgs args, CustomResourceOptions? options = null)
            : base("proxmoxve:Storage/file:File", name, args ?? new FileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private File(string name, Input<string> id, FileState? state = null, CustomResourceOptions? options = null)
            : base("proxmoxve:Storage/file:File", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing File resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static File Get(string name, Input<string> id, FileState? state = null, CustomResourceOptions? options = null)
        {
            return new File(name, id, state, options);
        }
    }

    public sealed class FileArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The content type
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// The datastore id
        /// </summary>
        [Input("datastoreId", required: true)]
        public Input<string> DatastoreId { get; set; } = null!;

        /// <summary>
        /// The node name
        /// </summary>
        [Input("nodeName", required: true)]
        public Input<string> NodeName { get; set; } = null!;

        /// <summary>
        /// The source file
        /// </summary>
        [Input("sourceFile")]
        public Input<Inputs.FileSourceFileArgs>? SourceFile { get; set; }

        /// <summary>
        /// The raw source
        /// </summary>
        [Input("sourceRaw")]
        public Input<Inputs.FileSourceRawArgs>? SourceRaw { get; set; }

        public FileArgs()
        {
        }
    }

    public sealed class FileState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The content type
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// The datastore id
        /// </summary>
        [Input("datastoreId")]
        public Input<string>? DatastoreId { get; set; }

        /// <summary>
        /// The file modification date
        /// </summary>
        [Input("fileModificationDate")]
        public Input<string>? FileModificationDate { get; set; }

        /// <summary>
        /// The file name
        /// </summary>
        [Input("fileName")]
        public Input<string>? FileName { get; set; }

        /// <summary>
        /// The file size in bytes
        /// </summary>
        [Input("fileSize")]
        public Input<int>? FileSize { get; set; }

        /// <summary>
        /// The file tag
        /// </summary>
        [Input("fileTag")]
        public Input<string>? FileTag { get; set; }

        /// <summary>
        /// The node name
        /// </summary>
        [Input("nodeName")]
        public Input<string>? NodeName { get; set; }

        /// <summary>
        /// The source file
        /// </summary>
        [Input("sourceFile")]
        public Input<Inputs.FileSourceFileGetArgs>? SourceFile { get; set; }

        /// <summary>
        /// The raw source
        /// </summary>
        [Input("sourceRaw")]
        public Input<Inputs.FileSourceRawGetArgs>? SourceRaw { get; set; }

        public FileState()
        {
        }
    }
}