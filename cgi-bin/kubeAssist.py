#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sb
import cgi

# returns the keywords related to name and resource image etc.
def keywordExtract(sentence):
    # words : list of words in the sentence
    words = sentence.split()
    resources = ['pod', 'pods', 'po', 'deployment', 'deployments','deploy', 'service', 'svc', 'services' ]
    
    # Tasks can be performed.
    operations = {
                    'get':['get', 'show'], 
                    'run':['run', 'launch'], 
                    'create': ['create'],
                    'delete': ['remove', 'delete'], 
                    'delete all --all': ['everything', 'all'],
                    'expose': ['serivce', 'expose'],
                    'describe': ['details', 'describe'],
                    'scale': ['scale', 'replica', 'replicas']
    }

    # This is a dictionary which will contain all the necessary keywords for the command.
    keywords = {}

    # All the operations which can be performed.
    operationsAll = []
    for x in operations:
        operationsAll += operations[x]

    # For retrieving command
    for word in words:
        if word.lower() in operationsAll:
            for command, val in operations.items():
                if  word.lower() in val:
                    keywords['command'] = command
                    break
                else:
                    keywords['command'] = ''

    # For retrieving resource
    for word in words:
        if word.lower() in resources:
            keywords['resource'] = word
            break
        else:
            keywords['resource'] = ''

    # Retieving port
    if keywords['command'] != 'get' or keywords['command'] != 'describe':
        for word in words:
            try:
                int(word)
                keywords['port'] = word
                break
            except:
                keywords['port'] = ''

        if 'called' in words:
            keywords['name'] = words[words.index('called')+1]
        elif 'name' in words:
            keywords['name'] = words[words.index('name')+1]
        elif 'named' in words:
            keywords['name'] = words[words.index('named')+1]
        else:
            keywords['name'] = ''

        if 'image.' in words:
            keywords['image'] = words[words.index('image.')-1]
        elif 'image' in words:
            keywords['image'] = words[words.index('image')-1]
        else:
            keywords['image']= ''
  
    return keywords

def executeCommand(cmd):
    return sb.getoutput(cmd)


# Main code starts from here. 
# field = cgi.FieldStorage()
# command = field.getvalue("command")
command = input()

# There are two types of inputs which can be provided by the user. 
if command[0].strip() == '1':
    print("#" + command[1:] + "\n\n" + executeCommand(command[1:].strip()))
elif command[0] == '2':
    keywords = keywordExtract(command[1:].strip())
    if keywords['command'] == 'scale':
        cmd = 'kubectl {} --replicas={} {}/{}'.format(keywords['command'], keywords['port'], keywords['resource'], keywords['name'])
    elif keywords['command'] == 'expose':
        cmd = 'kubectl {} {} {} --port={} --type=NodePort'.format(keywords['command'], keywords['resource'], keywords['name'], keywords['port'])
    elif keywords['image'] != '':
        cmd = 'kubectl {} {} {} --image={}'.format(keywords['command'], keywords['resource'], keywords['name'], keywords['image']) 
    else:
        cmd = 'kubectl {} {} {} {}}'.format(keywords['command'], keywords['resource'], keywords['name'], keywords['image']) 
    
    print("#" + cmd + "\n\n" + executeCommand(cmd))
