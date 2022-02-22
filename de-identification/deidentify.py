import NodeType
import yaml
import pprint


def deidentify(data=None, policy=None):
    pass


def parse_policy(policy):
    primary_cmds = ("show", "blur", "hide", "none")
    positions = ("last", "first", "index")
    range_cmds = ("to")
    policy_dict = {}
    with open(policy, "r") as stream:
        try:
            policy_dict = yaml.safe_load(stream)
            print(policy_dict)
        except yaml.YAMLError as exc:
            print(exc)


policy = "/Users/richardm/Documents/app_dev/APP-BASE/PrivacyLab/de-identification/policies/sample_policy.yml"
parse_policy(policy)
