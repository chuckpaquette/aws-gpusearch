import boto3
# import pprint
from botocore.config import Config

my_config = Config(
    region_name = 'us-east-1',
)

client = boto3.client('ec2', config = my_config)

#EC2 Architectures
architecture=['x86_64','arm64','x86_64_mac','arm64_mac'] # Required
virtualization=['hvm'] # Required
# The minimum and maximum number of vCPUs
vcpu_min=0 # Required
vcpu_max=256 # Required
# The minimum and maximum amount of memory in MB
memory_min=64000 # Required
memory_max=256000 # Required
# Minimum and maximum network bandwidth in GB
network_bw_min=10
network_bw_max=123
#CPU Types
cpu_manuf=['amd','intel','amazon-web-services']

response = client.get_instance_types_from_instance_requirements(
    DryRun=False,
    ArchitectureTypes=architecture,
    VirtualizationTypes=virtualization,
    InstanceRequirements={
        'VCpuCount': {
            'Min': vcpu_min,
            'Max': vcpu_max
        },
        'MemoryMiB': {
            'Min': memory_min,
            'Max': memory_max
        },
        'CpuManufacturers': cpu_manuf,
        'InstanceGenerations': [
            'current'
        ],
        'AcceleratorTypes': [
            'gpu',
        ],
        'AcceleratorManufacturers': [
            'nvidia',
        ],
        'NetworkBandwidthGbps': {
            'Min': network_bw_min,
            'Max': network_bw_max
        }
    },
)

print('Here are the EC2 NVIDIA instacnes with the following attributes')
print(f' - vCPU Min:{vcpu_min} Max:{vcpu_max}')
print(f' - Memory Min:{memory_min} Max:{memory_max}')
print(f' - Network BW Min:{network_bw_min} Max:{network_bw_max}')
print('============================')

ec2_list = []
ec2_string = ""
# print(response['InstaceTypes'])
for each_ec2 in response['InstanceTypes']:
    ec2_list.append(each_ec2['InstanceType'])
    # print(each_ec2['InstanceType'])

# print(ec2_list)
# print(ec2_string)

response = client.describe_instance_types(
    InstanceTypes=ec2_list,
)
# print(response['InstanceTypes'])
# pprint.pprint(response)
for each_ec2 in response['InstanceTypes']:
    print(each_ec2['InstanceType'])
    print(each_ec2['GpuInfo'])
    print(f"Memory Info: {each_ec2['MemoryInfo']}")
    print(f"Placement Group: {each_ec2['PlacementGroupInfo']}")
    print(f"Processor Info: {each_ec2['ProcessorInfo']}")
    print(f"vCPU Info: {each_ec2['VCpuInfo']}")
    print("===========")

    # Request Syntax
    # From: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_instance_types_from_instance_requirements.html
    """
    response = client.get_instance_types_from_instance_requirements(
    DryRun=True|False,
    ArchitectureTypes=[
        'i386'|'x86_64'|'arm64'|'x86_64_mac'|'arm64_mac',
    ],
    VirtualizationTypes=[
        'hvm'|'paravirtual',
    ],
    InstanceRequirements={
        'VCpuCount': {
            'Min': 123,
            'Max': 123
        },
        'MemoryMiB': {
            'Min': 123,
            'Max': 123
        },
        'CpuManufacturers': [
            'intel'|'amd'|'amazon-web-services',
        ],
        'MemoryGiBPerVCpu': {
            'Min': 123.0,
            'Max': 123.0
        },
        'ExcludedInstanceTypes': [
            'string',
        ],
        'InstanceGenerations': [
            'current'|'previous',
        ],
        'SpotMaxPricePercentageOverLowestPrice': 123,
        'OnDemandMaxPricePercentageOverLowestPrice': 123,
        'BareMetal': 'included'|'required'|'excluded',
        'BurstablePerformance': 'included'|'required'|'excluded',
        'RequireHibernateSupport': True|False,
        'NetworkInterfaceCount': {
            'Min': 123,
            'Max': 123
        },
        'LocalStorage': 'included'|'required'|'excluded',
        'LocalStorageTypes': [
            'hdd'|'ssd',
        ],
        'TotalLocalStorageGB': {
            'Min': 123.0,
            'Max': 123.0
        },
        'BaselineEbsBandwidthMbps': {
            'Min': 123,
            'Max': 123
        },
        'AcceleratorTypes': [
            'gpu'|'fpga'|'inference',
        ],
        'AcceleratorCount': {
            'Min': 123,
            'Max': 123
        },
        'AcceleratorManufacturers': [
            'nvidia'|'amd'|'amazon-web-services'|'xilinx',
        ],
        'AcceleratorNames': [
            'a100'|'v100'|'k80'|'t4'|'m60'|'radeon-pro-v520'|'vu9p'|'inferentia'|'k520',
        ],
        'AcceleratorTotalMemoryMiB': {
            'Min': 123,
            'Max': 123
        },
        'NetworkBandwidthGbps': {
            'Min': 123.0,
            'Max': 123.0
        },
        'AllowedInstanceTypes': [
            'string',
        ]
    },
    MaxResults=123,
    NextToken='string'
)
    """