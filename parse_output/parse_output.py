import sys
import textfsm

output_file = sys.argv[1]

with open('processing_status.template') as template, open(output_file) as output:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(output.read())

for header, res in zip(fsm.header, *result):
    if res.isalpha():
        res = '\"' + res + '\"'
    print(header, ':', res)
