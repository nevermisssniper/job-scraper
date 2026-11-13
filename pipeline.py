"""Offline-first job discovery. Nothing runs, scrapes, or sends mail on import."""
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode


def canonical_url(url):
    parts = urlsplit(url)
    if parts.scheme not in ('http', 'https') or not parts.netloc:
        raise ValueError('Job URLs must be absolute HTTP(S) URLs')
    query = [(k,v) for k,v in parse_qsl(parts.query) if not k.lower().startswith('utm_')]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip('/') or '/', urlencode(sorted(query)), ''))


def normalize(job):
    title = str(job.get('title','')).strip()
    if not title: raise ValueError('Each job needs a title')
    url = job.get('url') or next(iter(sorted(job.get('href',[]))), '')
    url = canonical_url(url)
    education = job.get('education','unknown')
    if education not in ('degree','no-degree','unknown'): education='unknown'
    return {**job, 'title':title, 'url':url, 'education':education,
            'id':hashlib.sha256(url.encode()).hexdigest()[:20]}


def ingest(jobs, database):
    """Persist seen IDs across runs; rollback an invalid batch as a unit."""
    clean = [normalize(j) for j in jobs]
    with sqlite3.connect(database) as db:
        db.execute('CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, payload TEXT NOT NULL)')
        new=[]
        for job in clean:
            exists=db.execute('SELECT 1 FROM jobs WHERE id=?',(job['id'],)).fetchone()
            db.execute('INSERT OR REPLACE INTO jobs VALUES (?,?)',(job['id'],json.dumps(job)))
            if not exists:new.append(job)
    return new


def main(argv=None):
    parser=argparse.ArgumentParser(description='Import job listings without paid APIs or email side effects')
    parser.add_argument('--input',default=str(Path(__file__).parent/'examples/jobs.json'))
    parser.add_argument('--database',default='jobs.sqlite3')
    parser.add_argument('--education',choices=['all','degree','no-degree','unknown'],default='all')
    parser.add_argument('--output',help='Write matching new listings as JSON')
    args=parser.parse_args(argv)
    new=ingest(json.loads(Path(args.input).read_text()),args.database)
    matches=[j for j in new if args.education=='all' or j['education']==args.education]
    result={'new_count':len(new),'matches':matches,'note':'Unknown education stays unknown; verify the original posting.'}
    text=json.dumps(result,indent=2)
    if args.output:Path(args.output).write_text(text+'\n')
    print(text)
    return 0

if __name__=='__main__':raise SystemExit(main())
