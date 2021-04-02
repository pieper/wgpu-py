"""
All wgpu structs.
"""

# THIS CODE IS AUTOGENERATED - DO NOT EDIT

_use_sphinx_repr = False


class Struct:
    def __init__(self, name, **kwargs):
        self._name = name
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __iter__(self):
        return iter([key for key in dir(self) if not key.startswith("_")])

    def __repr__(self):
        options = ", ".join(f"'{x}'" for x in self)
        if _use_sphinx_repr:  # no-cover
            return options
        return f"<{self.__class__.__name__} {self._name}: {options}>"


# There are 45 structs

RequestAdapterOptions = Struct(
    "RequestAdapterOptions",
    power_preference="enums.PowerPreference",
)  #:

DeviceDescriptor = Struct(
    "DeviceDescriptor",
    label=str,
    extensions="List[enums.ExtensionName]",
    limits="structs.Limits",
)  #:

Limits = Struct(
    "Limits",
    max_bind_groups=int,
    max_dynamic_uniform_buffers_per_pipeline_layout=int,
    max_dynamic_storage_buffers_per_pipeline_layout=int,
    max_sampled_textures_per_shader_stage=int,
    max_samplers_per_shader_stage=int,
    max_storage_buffers_per_shader_stage=int,
    max_storage_textures_per_shader_stage=int,
    max_uniform_buffers_per_shader_stage=int,
    max_uniform_buffer_binding_size=int,
)  #:

BufferDescriptor = Struct(
    "BufferDescriptor",
    label=str,
    size=int,
    usage="flags.BufferUsage",
    mapped_at_creation=bool,
)  #:

TextureDescriptor = Struct(
    "TextureDescriptor",
    label=str,
    size="Union[List[int], structs.Extent3D]",
    mip_level_count=int,
    sample_count=int,
    dimension="enums.TextureDimension",
    format="enums.TextureFormat",
    usage="flags.TextureUsage",
)  #:

TextureViewDescriptor = Struct(
    "TextureViewDescriptor",
    label=str,
    format="enums.TextureFormat",
    dimension="enums.TextureViewDimension",
    aspect="enums.TextureAspect",
    base_mip_level=int,
    mip_level_count=int,
    base_array_layer=int,
    array_layer_count=int,
)  #:

SamplerDescriptor = Struct(
    "SamplerDescriptor",
    label=str,
    address_mode_u="enums.AddressMode",
    address_mode_v="enums.AddressMode",
    address_mode_w="enums.AddressMode",
    mag_filter="enums.FilterMode",
    min_filter="enums.FilterMode",
    mipmap_filter="enums.FilterMode",
    lod_min_clamp=float,
    lod_max_clamp=float,
    compare="enums.CompareFunction",
)  #:

BindGroupLayoutDescriptor = Struct(
    "BindGroupLayoutDescriptor",
    label=str,
    entries="List[structs.BindGroupLayoutEntry]",
)  #:

BindGroupLayoutEntry = Struct(
    "BindGroupLayoutEntry",
    binding=int,
    visibility="flags.ShaderStage",
    type="enums.BindingType",
    has_dynamic_offset=bool,
    min_buffer_binding_size=int,
    view_dimension="enums.TextureViewDimension",
    texture_component_type="enums.TextureComponentType",
    multisampled=bool,
    storage_texture_format="enums.TextureFormat",
)  #:

BindGroupDescriptor = Struct(
    "BindGroupDescriptor",
    label=str,
    layout="GPUBindGroupLayout",
    entries="List[structs.BindGroupEntry]",
)  #:

BindGroupEntry = Struct(
    "BindGroupEntry",
    binding=int,
    resource="Union[GPUSampler, GPUTextureView, structs.BufferBinding]",
)  #:

BufferBinding = Struct(
    "BufferBinding",
    buffer="GPUBuffer",
    offset=int,
    size=int,
)  #:

PipelineLayoutDescriptor = Struct(
    "PipelineLayoutDescriptor",
    label=str,
    bind_group_layouts="List[GPUBindGroupLayout]",
)  #:

ShaderModuleDescriptor = Struct(
    "ShaderModuleDescriptor",
    label=str,
    code=str,
    source_map=dict,
)  #:

ProgrammableStageDescriptor = Struct(
    "ProgrammableStageDescriptor",
    module="GPUShaderModule",
    entry_point=str,
)  #:

ComputePipelineDescriptor = Struct(
    "ComputePipelineDescriptor",
    label=str,
    layout="GPUPipelineLayout",
    compute_stage="structs.ProgrammableStageDescriptor",
)  #:

RenderPipelineDescriptor = Struct(
    "RenderPipelineDescriptor",
    label=str,
    layout="GPUPipelineLayout",
    vertex_stage="structs.ProgrammableStageDescriptor",
    fragment_stage="structs.ProgrammableStageDescriptor",
    primitive_topology="enums.PrimitiveTopology",
    rasterization_state="structs.RasterizationStateDescriptor",
    color_states="List[structs.ColorStateDescriptor]",
    depth_stencil_state="structs.DepthStencilStateDescriptor",
    vertex_state="structs.VertexStateDescriptor",
    sample_count=int,
    sample_mask=int,
    alpha_to_coverage_enabled=bool,
)  #:

RasterizationStateDescriptor = Struct(
    "RasterizationStateDescriptor",
    front_face="enums.FrontFace",
    cull_mode="enums.CullMode",
    depth_bias=int,
    depth_bias_slope_scale=float,
    depth_bias_clamp=float,
)  #:

ColorStateDescriptor = Struct(
    "ColorStateDescriptor",
    format="enums.TextureFormat",
    alpha_blend="structs.BlendDescriptor",
    color_blend="structs.BlendDescriptor",
    write_mask="flags.ColorWrite",
)  #:

BlendDescriptor = Struct(
    "BlendDescriptor",
    src_factor="enums.BlendFactor",
    dst_factor="enums.BlendFactor",
    operation="enums.BlendOperation",
)  #:

DepthStencilStateDescriptor = Struct(
    "DepthStencilStateDescriptor",
    format="enums.TextureFormat",
    depth_write_enabled=bool,
    depth_compare="enums.CompareFunction",
    stencil_front="structs.StencilStateFaceDescriptor",
    stencil_back="structs.StencilStateFaceDescriptor",
    stencil_read_mask=int,
    stencil_write_mask=int,
)  #:

StencilStateFaceDescriptor = Struct(
    "StencilStateFaceDescriptor",
    compare="enums.CompareFunction",
    fail_op="enums.StencilOperation",
    depth_fail_op="enums.StencilOperation",
    pass_op="enums.StencilOperation",
)  #:

VertexStateDescriptor = Struct(
    "VertexStateDescriptor",
    index_format="enums.IndexFormat",
    vertex_buffers="List[structs.VertexBufferLayoutDescriptor]",
)  #:

VertexBufferLayoutDescriptor = Struct(
    "VertexBufferLayoutDescriptor",
    array_stride=int,
    step_mode="enums.InputStepMode",
    attributes="List[structs.VertexAttributeDescriptor]",
)  #:

VertexAttributeDescriptor = Struct(
    "VertexAttributeDescriptor",
    format="enums.VertexFormat",
    offset=int,
    shader_location=int,
)  #:

CommandBufferDescriptor = Struct(
    "CommandBufferDescriptor",
    label=str,
)  #:

CommandEncoderDescriptor = Struct(
    "CommandEncoderDescriptor",
    label=str,
)  #:

TextureDataLayout = Struct(
    "TextureDataLayout",
    offset=int,
    bytes_per_row=int,
    rows_per_image=int,
)  #:

BufferCopyView = Struct(
    "BufferCopyView",
    offset=int,
    bytes_per_row=int,
    rows_per_image=int,
    buffer="GPUBuffer",
)  #:

TextureCopyView = Struct(
    "TextureCopyView",
    texture="GPUTexture",
    mip_level=int,
    origin="Union[List[int], structs.Origin3D]",
)  #:

ImageBitmapCopyView = Struct(
    "ImageBitmapCopyView",
    image_bitmap=memoryview,
    origin="Union[List[int], structs.Origin2D]",
)  #:

ComputePassDescriptor = Struct(
    "ComputePassDescriptor",
    label=str,
)  #:

RenderPassDescriptor = Struct(
    "RenderPassDescriptor",
    label=str,
    color_attachments="List[structs.RenderPassColorAttachmentDescriptor]",
    depth_stencil_attachment="structs.RenderPassDepthStencilAttachmentDescriptor",
    occlusion_query_set="GPUQuerySet",
)  #:

RenderPassColorAttachmentDescriptor = Struct(
    "RenderPassColorAttachmentDescriptor",
    attachment="GPUTextureView",
    resolve_target="GPUTextureView",
    load_value="Union[enums.LoadOp, Union[List[float], structs.Color]]",
    store_op="enums.StoreOp",
)  #:

RenderPassDepthStencilAttachmentDescriptor = Struct(
    "RenderPassDepthStencilAttachmentDescriptor",
    attachment="GPUTextureView",
    depth_load_value="Union[enums.LoadOp, float]",
    depth_store_op="enums.StoreOp",
    depth_read_only=bool,
    stencil_load_value="Union[enums.LoadOp, int]",
    stencil_store_op="enums.StoreOp",
    stencil_read_only=bool,
)  #:

RenderBundleDescriptor = Struct(
    "RenderBundleDescriptor",
    label=str,
)  #:

RenderBundleEncoderDescriptor = Struct(
    "RenderBundleEncoderDescriptor",
    label=str,
    color_formats="List[enums.TextureFormat]",
    depth_stencil_format="enums.TextureFormat",
    sample_count=int,
)  #:

FenceDescriptor = Struct(
    "FenceDescriptor",
    label=str,
    initial_value=int,
)  #:

QuerySetDescriptor = Struct(
    "QuerySetDescriptor",
    label=str,
    type="enums.QueryType",
    count=int,
    pipeline_statistics="List[enums.PipelineStatisticName]",
)  #:

SwapChainDescriptor = Struct(
    "SwapChainDescriptor",
    label=str,
    device="GPUDevice",
    format="enums.TextureFormat",
    usage="flags.TextureUsage",
)  #:

UncapturedErrorEventInit = Struct(
    "UncapturedErrorEventInit",
    error="Union[GPUOutOfMemoryError, GPUValidationError]",
)  #:

Color = Struct(
    "Color",
    r=float,
    g=float,
    b=float,
    a=float,
)  #:

Origin2D = Struct(
    "Origin2D",
    x=int,
    y=int,
)  #:

Origin3D = Struct(
    "Origin3D",
    x=int,
    y=int,
    z=int,
)  #:

Extent3D = Struct(
    "Extent3D",
    width=int,
    height=int,
    depth=int,
)  #: