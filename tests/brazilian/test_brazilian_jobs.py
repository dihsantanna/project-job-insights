from src.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"
expected = ["title", "salary", "type"]


def test_brazilian_jobs():
    for job in read_brazilian_file(path):
        keys = job.keys()

        assert len(keys) == len(expected)

        for key in keys:
            assert key in expected
