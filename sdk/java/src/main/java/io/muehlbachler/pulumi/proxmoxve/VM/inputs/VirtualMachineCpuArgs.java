// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package io.muehlbachler.pulumi.proxmoxve.VM.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class VirtualMachineCpuArgs extends com.pulumi.resources.ResourceArgs {

    public static final VirtualMachineCpuArgs Empty = new VirtualMachineCpuArgs();

    /**
     * The CPU architecture (defaults to `x86_64`).
     * 
     */
    @Import(name="architecture")
    private @Nullable Output<String> architecture;

    /**
     * @return The CPU architecture (defaults to `x86_64`).
     * 
     */
    public Optional<Output<String>> architecture() {
        return Optional.ofNullable(this.architecture);
    }

    /**
     * The number of CPU cores (defaults to `1`).
     * 
     */
    @Import(name="cores")
    private @Nullable Output<Integer> cores;

    /**
     * @return The number of CPU cores (defaults to `1`).
     * 
     */
    public Optional<Output<Integer>> cores() {
        return Optional.ofNullable(this.cores);
    }

    /**
     * The CPU flags.
     * - `+aes`/`-aes` - Activate AES instruction set for HW acceleration.
     * - `+amd-no-ssb`/`-amd-no-ssb` - Notifies guest OS that host is not
     *   vulnerable for Spectre on AMD CPUs.
     * - `+amd-ssbd`/`-amd-ssbd` - Improves Spectre mitigation performance with
     *   AMD CPUs, best used with &#34;virt-ssbd&#34;.
     * - `+hv-evmcs`/`-hv-evmcs` - Improve performance for nested
     *   virtualization (only supported on Intel CPUs).
     * - `+hv-tlbflush`/`-hv-tlbflush` - Improve performance in overcommitted
     *   Windows guests (may lead to guest BSOD on old CPUs).
     * - `+ibpb`/`-ibpb` - Allows improved Spectre mitigation on AMD CPUs.
     * - `+md-clear`/`-md-clear` - Required to let the guest OS know if MDS is
     *   mitigated correctly.
     * - `+pcid`/`-pcid` - Meltdown fix cost reduction on Westmere, Sandy- and
     *   Ivy Bridge Intel CPUs.
     * - `+pdpe1gb`/`-pdpe1gb` - Allows guest OS to use 1 GB size pages, if
     *   host HW supports it.
     * - `+spec-ctrl`/`-spec-ctrl` - Allows improved Spectre mitigation with
     *   Intel CPUs.
     * - `+ssbd`/`-ssbd` - Protection for &#34;Speculative Store Bypass&#34; for Intel
     *   models.
     * - `+virt-ssbd`/`-virt-ssbd` - Basis for &#34;Speculative Store Bypass&#34;
     *   protection for AMD models.
     * 
     */
    @Import(name="flags")
    private @Nullable Output<List<String>> flags;

    /**
     * @return The CPU flags.
     * - `+aes`/`-aes` - Activate AES instruction set for HW acceleration.
     * - `+amd-no-ssb`/`-amd-no-ssb` - Notifies guest OS that host is not
     *   vulnerable for Spectre on AMD CPUs.
     * - `+amd-ssbd`/`-amd-ssbd` - Improves Spectre mitigation performance with
     *   AMD CPUs, best used with &#34;virt-ssbd&#34;.
     * - `+hv-evmcs`/`-hv-evmcs` - Improve performance for nested
     *   virtualization (only supported on Intel CPUs).
     * - `+hv-tlbflush`/`-hv-tlbflush` - Improve performance in overcommitted
     *   Windows guests (may lead to guest BSOD on old CPUs).
     * - `+ibpb`/`-ibpb` - Allows improved Spectre mitigation on AMD CPUs.
     * - `+md-clear`/`-md-clear` - Required to let the guest OS know if MDS is
     *   mitigated correctly.
     * - `+pcid`/`-pcid` - Meltdown fix cost reduction on Westmere, Sandy- and
     *   Ivy Bridge Intel CPUs.
     * - `+pdpe1gb`/`-pdpe1gb` - Allows guest OS to use 1 GB size pages, if
     *   host HW supports it.
     * - `+spec-ctrl`/`-spec-ctrl` - Allows improved Spectre mitigation with
     *   Intel CPUs.
     * - `+ssbd`/`-ssbd` - Protection for &#34;Speculative Store Bypass&#34; for Intel
     *   models.
     * - `+virt-ssbd`/`-virt-ssbd` - Basis for &#34;Speculative Store Bypass&#34;
     *   protection for AMD models.
     * 
     */
    public Optional<Output<List<String>>> flags() {
        return Optional.ofNullable(this.flags);
    }

    /**
     * The number of hotplugged vCPUs (defaults
     * to `0`).
     * 
     */
    @Import(name="hotplugged")
    private @Nullable Output<Integer> hotplugged;

    /**
     * @return The number of hotplugged vCPUs (defaults
     * to `0`).
     * 
     */
    public Optional<Output<Integer>> hotplugged() {
        return Optional.ofNullable(this.hotplugged);
    }

    /**
     * Enable/disable NUMA. (default to `false`)
     * 
     */
    @Import(name="numa")
    private @Nullable Output<Boolean> numa;

    /**
     * @return Enable/disable NUMA. (default to `false`)
     * 
     */
    public Optional<Output<Boolean>> numa() {
        return Optional.ofNullable(this.numa);
    }

    /**
     * The number of CPU sockets (defaults to `1`).
     * 
     */
    @Import(name="sockets")
    private @Nullable Output<Integer> sockets;

    /**
     * @return The number of CPU sockets (defaults to `1`).
     * 
     */
    public Optional<Output<Integer>> sockets() {
        return Optional.ofNullable(this.sockets);
    }

    /**
     * The VGA type (defaults to `std`).
     * 
     */
    @Import(name="type")
    private @Nullable Output<String> type;

    /**
     * @return The VGA type (defaults to `std`).
     * 
     */
    public Optional<Output<String>> type() {
        return Optional.ofNullable(this.type);
    }

    /**
     * The CPU units (defaults to `1024`).
     * 
     */
    @Import(name="units")
    private @Nullable Output<Integer> units;

    /**
     * @return The CPU units (defaults to `1024`).
     * 
     */
    public Optional<Output<Integer>> units() {
        return Optional.ofNullable(this.units);
    }

    private VirtualMachineCpuArgs() {}

    private VirtualMachineCpuArgs(VirtualMachineCpuArgs $) {
        this.architecture = $.architecture;
        this.cores = $.cores;
        this.flags = $.flags;
        this.hotplugged = $.hotplugged;
        this.numa = $.numa;
        this.sockets = $.sockets;
        this.type = $.type;
        this.units = $.units;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(VirtualMachineCpuArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private VirtualMachineCpuArgs $;

        public Builder() {
            $ = new VirtualMachineCpuArgs();
        }

        public Builder(VirtualMachineCpuArgs defaults) {
            $ = new VirtualMachineCpuArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param architecture The CPU architecture (defaults to `x86_64`).
         * 
         * @return builder
         * 
         */
        public Builder architecture(@Nullable Output<String> architecture) {
            $.architecture = architecture;
            return this;
        }

        /**
         * @param architecture The CPU architecture (defaults to `x86_64`).
         * 
         * @return builder
         * 
         */
        public Builder architecture(String architecture) {
            return architecture(Output.of(architecture));
        }

        /**
         * @param cores The number of CPU cores (defaults to `1`).
         * 
         * @return builder
         * 
         */
        public Builder cores(@Nullable Output<Integer> cores) {
            $.cores = cores;
            return this;
        }

        /**
         * @param cores The number of CPU cores (defaults to `1`).
         * 
         * @return builder
         * 
         */
        public Builder cores(Integer cores) {
            return cores(Output.of(cores));
        }

        /**
         * @param flags The CPU flags.
         * - `+aes`/`-aes` - Activate AES instruction set for HW acceleration.
         * - `+amd-no-ssb`/`-amd-no-ssb` - Notifies guest OS that host is not
         *   vulnerable for Spectre on AMD CPUs.
         * - `+amd-ssbd`/`-amd-ssbd` - Improves Spectre mitigation performance with
         *   AMD CPUs, best used with &#34;virt-ssbd&#34;.
         * - `+hv-evmcs`/`-hv-evmcs` - Improve performance for nested
         *   virtualization (only supported on Intel CPUs).
         * - `+hv-tlbflush`/`-hv-tlbflush` - Improve performance in overcommitted
         *   Windows guests (may lead to guest BSOD on old CPUs).
         * - `+ibpb`/`-ibpb` - Allows improved Spectre mitigation on AMD CPUs.
         * - `+md-clear`/`-md-clear` - Required to let the guest OS know if MDS is
         *   mitigated correctly.
         * - `+pcid`/`-pcid` - Meltdown fix cost reduction on Westmere, Sandy- and
         *   Ivy Bridge Intel CPUs.
         * - `+pdpe1gb`/`-pdpe1gb` - Allows guest OS to use 1 GB size pages, if
         *   host HW supports it.
         * - `+spec-ctrl`/`-spec-ctrl` - Allows improved Spectre mitigation with
         *   Intel CPUs.
         * - `+ssbd`/`-ssbd` - Protection for &#34;Speculative Store Bypass&#34; for Intel
         *   models.
         * - `+virt-ssbd`/`-virt-ssbd` - Basis for &#34;Speculative Store Bypass&#34;
         *   protection for AMD models.
         * 
         * @return builder
         * 
         */
        public Builder flags(@Nullable Output<List<String>> flags) {
            $.flags = flags;
            return this;
        }

        /**
         * @param flags The CPU flags.
         * - `+aes`/`-aes` - Activate AES instruction set for HW acceleration.
         * - `+amd-no-ssb`/`-amd-no-ssb` - Notifies guest OS that host is not
         *   vulnerable for Spectre on AMD CPUs.
         * - `+amd-ssbd`/`-amd-ssbd` - Improves Spectre mitigation performance with
         *   AMD CPUs, best used with &#34;virt-ssbd&#34;.
         * - `+hv-evmcs`/`-hv-evmcs` - Improve performance for nested
         *   virtualization (only supported on Intel CPUs).
         * - `+hv-tlbflush`/`-hv-tlbflush` - Improve performance in overcommitted
         *   Windows guests (may lead to guest BSOD on old CPUs).
         * - `+ibpb`/`-ibpb` - Allows improved Spectre mitigation on AMD CPUs.
         * - `+md-clear`/`-md-clear` - Required to let the guest OS know if MDS is
         *   mitigated correctly.
         * - `+pcid`/`-pcid` - Meltdown fix cost reduction on Westmere, Sandy- and
         *   Ivy Bridge Intel CPUs.
         * - `+pdpe1gb`/`-pdpe1gb` - Allows guest OS to use 1 GB size pages, if
         *   host HW supports it.
         * - `+spec-ctrl`/`-spec-ctrl` - Allows improved Spectre mitigation with
         *   Intel CPUs.
         * - `+ssbd`/`-ssbd` - Protection for &#34;Speculative Store Bypass&#34; for Intel
         *   models.
         * - `+virt-ssbd`/`-virt-ssbd` - Basis for &#34;Speculative Store Bypass&#34;
         *   protection for AMD models.
         * 
         * @return builder
         * 
         */
        public Builder flags(List<String> flags) {
            return flags(Output.of(flags));
        }

        /**
         * @param flags The CPU flags.
         * - `+aes`/`-aes` - Activate AES instruction set for HW acceleration.
         * - `+amd-no-ssb`/`-amd-no-ssb` - Notifies guest OS that host is not
         *   vulnerable for Spectre on AMD CPUs.
         * - `+amd-ssbd`/`-amd-ssbd` - Improves Spectre mitigation performance with
         *   AMD CPUs, best used with &#34;virt-ssbd&#34;.
         * - `+hv-evmcs`/`-hv-evmcs` - Improve performance for nested
         *   virtualization (only supported on Intel CPUs).
         * - `+hv-tlbflush`/`-hv-tlbflush` - Improve performance in overcommitted
         *   Windows guests (may lead to guest BSOD on old CPUs).
         * - `+ibpb`/`-ibpb` - Allows improved Spectre mitigation on AMD CPUs.
         * - `+md-clear`/`-md-clear` - Required to let the guest OS know if MDS is
         *   mitigated correctly.
         * - `+pcid`/`-pcid` - Meltdown fix cost reduction on Westmere, Sandy- and
         *   Ivy Bridge Intel CPUs.
         * - `+pdpe1gb`/`-pdpe1gb` - Allows guest OS to use 1 GB size pages, if
         *   host HW supports it.
         * - `+spec-ctrl`/`-spec-ctrl` - Allows improved Spectre mitigation with
         *   Intel CPUs.
         * - `+ssbd`/`-ssbd` - Protection for &#34;Speculative Store Bypass&#34; for Intel
         *   models.
         * - `+virt-ssbd`/`-virt-ssbd` - Basis for &#34;Speculative Store Bypass&#34;
         *   protection for AMD models.
         * 
         * @return builder
         * 
         */
        public Builder flags(String... flags) {
            return flags(List.of(flags));
        }

        /**
         * @param hotplugged The number of hotplugged vCPUs (defaults
         * to `0`).
         * 
         * @return builder
         * 
         */
        public Builder hotplugged(@Nullable Output<Integer> hotplugged) {
            $.hotplugged = hotplugged;
            return this;
        }

        /**
         * @param hotplugged The number of hotplugged vCPUs (defaults
         * to `0`).
         * 
         * @return builder
         * 
         */
        public Builder hotplugged(Integer hotplugged) {
            return hotplugged(Output.of(hotplugged));
        }

        /**
         * @param numa Enable/disable NUMA. (default to `false`)
         * 
         * @return builder
         * 
         */
        public Builder numa(@Nullable Output<Boolean> numa) {
            $.numa = numa;
            return this;
        }

        /**
         * @param numa Enable/disable NUMA. (default to `false`)
         * 
         * @return builder
         * 
         */
        public Builder numa(Boolean numa) {
            return numa(Output.of(numa));
        }

        /**
         * @param sockets The number of CPU sockets (defaults to `1`).
         * 
         * @return builder
         * 
         */
        public Builder sockets(@Nullable Output<Integer> sockets) {
            $.sockets = sockets;
            return this;
        }

        /**
         * @param sockets The number of CPU sockets (defaults to `1`).
         * 
         * @return builder
         * 
         */
        public Builder sockets(Integer sockets) {
            return sockets(Output.of(sockets));
        }

        /**
         * @param type The VGA type (defaults to `std`).
         * 
         * @return builder
         * 
         */
        public Builder type(@Nullable Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type The VGA type (defaults to `std`).
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        /**
         * @param units The CPU units (defaults to `1024`).
         * 
         * @return builder
         * 
         */
        public Builder units(@Nullable Output<Integer> units) {
            $.units = units;
            return this;
        }

        /**
         * @param units The CPU units (defaults to `1024`).
         * 
         * @return builder
         * 
         */
        public Builder units(Integer units) {
            return units(Output.of(units));
        }

        public VirtualMachineCpuArgs build() {
            return $;
        }
    }

}
