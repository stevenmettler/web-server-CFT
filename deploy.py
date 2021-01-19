#!/usr/bin/python

import sys
import subprocess

print("Stack Name: %s" % (sys.argv[1]))
print("Key Pair Name: %s" % (sys.argv[2]))
stackName = sys.argv[1]
keyPair = sys.argv[2]
print("Creating stack...")

bashCommand = "aws cloudformation deploy --template-file web-server-cft.yaml --stack-name {} --region us-east-1 --parameter-overrides KeyPair={} --capabilities CAPABILITY_NAMED_IAM".format(stackName, keyPair)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()



