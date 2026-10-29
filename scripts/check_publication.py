"""Inspect the Git index, never print credential contents.

Optional --private-env and --private-project paths are local-only comparisons.
Do not commit those private files or reports containing their values.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

parser=argparse.ArgumentParser()
parser.add_argument('--private-env',type=Path)
parser.add_argument('--private-project',type=Path)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]

def git(*parts):
    return subprocess.check_output(['git','-C',str(root),*parts])

secrets={}
if args.private_env:
    for line in args.private_env.read_text().splitlines():
        match=re.match(r'^([A-Z_]+)=(.*)$',line.strip())
        if match:
            value=match[2].strip().strip('\"\'')
            if value:secrets[match[1]]=value
if args.private_project:
    project=json.loads(args.private_project.read_text())
    for key in ['projectId','orgId']:
        if project.get(key):secrets['HOSTING_'+key]=project[key]

patterns={
 'private_key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
 'github_token':r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b',
 'aws_access_key':r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
 'api_key':r'\bsk-(?:proj-)?[A-Za-z0-9_-]{25,}\b',
 'credential_url':r'https?://[^\s/:]+:[^\s/@]+@',
 'credential_query':r'[?&](?:access_token|api_key|secret|password)=[A-Za-z0-9_%.-]{8,}',
 'personal_home_path':r'/Users/[A-Za-z0-9_. -]+/',
 'linked_hosting_id':r'\b(?:prj_|team_)[A-Za-z0-9]{15,}\b',
 'live_host':r'\b[A-Za-z0-9.-]+\.vercel\.app\b',
}
errors=[]
paths=[p.decode() for p in git('ls-files','-z').split(b'\0') if p]
for name in paths:
    p=Path(name)
    if any(part in {'.vercel','node_modules','__pycache__'} for part in p.parts):errors.append((name,'private/generated directory'))
    if '.private.' in p.name or p.name in {'secrets.env','.env','.DS_Store','validation_report.json'} or (p.name.startswith('.env.') and p.name!='.env.example') or p.suffix in {'.pem','.key','.p12','.pfx','.pyc'}:
        errors.append((name,'private/generated filename'))
    if p.parts[:2]==('mcp-server','data'):errors.append((name,'generated server data'))
    content=git('show',':'+name)
    try:text=content.decode('utf8')
    except UnicodeDecodeError:
        errors.append((name,'unreviewed binary'));continue
    for label,pattern in patterns.items():
        if re.search(pattern,text,re.I if label in {'credential_query'} else 0):errors.append((name,label))
    for label,value in secrets.items():
        if label.startswith('HOSTING_') or value.isdigit():
            found=value in text
        else:
            pattern=r'[\W_]*'.join(re.escape(c) for c in value if c.isalnum())
            found=bool(re.search(pattern,text,re.I)) if pattern else False
        if found:errors.append((name,'active value: '+label))
result={'status':'FAIL' if errors else 'PASS','staged_files_checked':len(paths),'private_value_types_compared':len(secrets),'violations':[{'file':file,'check':check} for file,check in errors]}
print(json.dumps(result,indent=2))
sys.exit(bool(errors))
