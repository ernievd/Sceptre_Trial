
from troposphere import Template, Parameter, Ref
from troposphere.ec2 import VPC


class Vpc(object):
    def __init__(self, sceptre_user_data):
        self.template = Template()
        self.sceptre_user_data = sceptre_user_data
        self.add_vpc()

    def add_vpc(self):
        self.vpc = self.template.add_resource(VPC(
            "VirtualPrivateCloud",
            CidrBlock=self.sceptre_user_data["cidr_block"]
        ))


def sceptre_handler(sceptre_user_data):
    vpc = Vpc(sceptre_user_data)
    return vpc.template.to_json()


















# from troposphere import Template, Parameter, Ref, Tags
# from troposphere.ec2 import VPC
#
# class Vpc(object):
#     def __init__(self, sceptre_user_data):
#         self.template = Template()
#         self.sceptre_user_data = sceptre_user_data
#         self.add_vpc()
#
#     def add_vpc(self):
#         self.vpc = self.template.add_resource(VPC(
#             "Virtual Private Cloud",
#             CidrBlock=self.sceptre_user_data["CidrBlock"],
#             EnableDnsSupport=True,
#             EnableDnsHostnames=False,
#             InstanceTenancy="default",
#             Tags=Tags(
#                 Owner=self.sceptre_user_data["Engineer"],
#                 Environment=self.sceptre_user_data["Environment"]
#             )
#         ))
#
#
# def sceptre_handler(sceptre_user_data):
#     vpc = Vpc(sceptre_user_data)
#     return vpc.template.to_json()
