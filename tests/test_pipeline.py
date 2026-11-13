import importlib.util
from pathlib import Path
import pytest
spec=importlib.util.spec_from_file_location('pipeline',Path(__file__).parents[1]/'pipeline.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def test_persistent_deduplication(tmp_path):
    a={'title':'A','url':'https://example.com/job/?utm_source=test'}
    b={'title':'A updated','url':'https://example.com/job'}
    assert len(m.ingest([a],tmp_path/'jobs.db'))==1
    assert m.ingest([b],tmp_path/'jobs.db')==[]
def test_unknown_is_not_assumed_eligible(tmp_path):
    assert m.ingest([{'title':'A','url':'https://example.com/a'}],tmp_path/'j.db')[0]['education']=='unknown'
def test_invalid_batch_does_not_write(tmp_path):
    with pytest.raises(ValueError):m.ingest([{'title':'A','url':'javascript:bad'}],tmp_path/'j.db')
