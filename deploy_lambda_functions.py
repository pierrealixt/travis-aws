import os
import re
import subprocess


def get_lambda_functions_on_aws():
    p = subprocess.Popen('aws lambda list-functions --region us-west-2', 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT)

    lambda_functions_on_aws = []
    for line in p.stdout.readlines():
        line = line.decode("utf-8").strip()
        results = re.search(
            "\"(FunctionName)\": \"([a-zA-Z_]+)\",", 
            line.strip())
        if results:
            lambda_functions_on_aws.append(results.group(2))
    return lambda_functions_on_aws

if __name__ == "__main__":
    # main()
    functions = get_lambda_functions_on_aws()
    print(functions)