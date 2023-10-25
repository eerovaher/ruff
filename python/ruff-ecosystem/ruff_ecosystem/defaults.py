from ruff_ecosystem.projects import CheckOptions, Project, Repository

# TODO: Consider exporting this as JSON
DEFAULT_TARGETS = [
    # Project(repo=Repository(owner="DisnakeDev", name="disnake", ref="master")),
    # Project(repo=Repository(owner="PostHog", name="HouseWatch", ref="main")),
    # Project(repo=Repository(owner="RasaHQ", name="rasa", ref="main")),
    # Project(repo=Repository(owner="Snowflake-Labs", name="snowcli", ref="main")),
    # Project(repo=Repository(owner="aiven", name="aiven-client", ref="main")),
    # Project(repo=Repository(owner="alteryx", name="featuretools", ref="main")),
    # Project(
    #     repo=Repository(owner="apache", name="airflow", ref="main"),
    #     check_options=CheckOptions(select="ALL"),
    # ),
    # Project(repo=Repository(owner="aws", name="aws-sam-cli", ref="develop")),
    # Project(repo=Repository(owner="bloomberg", name="pytest-memray", ref="main")),
    Project(
        repo=Repository(owner="bokeh", name="bokeh", ref="branch-3.3"),
        check_options=CheckOptions(select="ALL"),
    ),
    # Project(repo=Repository(owner="commaai", name="openpilot", ref="master")),
    # Project(repo=Repository(owner="demisto", name="content", ref="master")),
    # Project(repo=Repository(owner="docker", name="docker-py", ref="main")),
    # Project(repo=Repository(owner="freedomofpress", name="securedrop", ref="develop")),
    # Project(repo=Repository(owner="fronzbot", name="blinkpy", ref="dev")),
    # Project(repo=Repository(owner="ibis-project", name="ibis", ref="master")),
    # Project(repo=Repository(owner="ing-bank", name="probatus", ref="main")),
    # Project(repo=Repository(owner="jrnl-org", name="jrnl", ref="develop")),
    # Project(repo=Repository(owner="latchbio", name="latch", ref="main")),
    # Project(repo=Repository(owner="lnbits", name="lnbits", ref="main")),
    # Project(repo=Repository(owner="milvus-io", name="pymilvus", ref="master")),
    # Project(repo=Repository(owner="mlflow", name="mlflow", ref="master")),
    # Project(repo=Repository(owner="model-bakers", name="model_bakery", ref="main")),
    # Project(repo=Repository(owner="pandas-dev", name="pandas", ref="main")),
    # Project(repo=Repository(owner="prefecthq", name="prefect", ref="main")),
    # Project(repo=Repository(owner="pypa", name="build", ref="main")),
    # Project(repo=Repository(owner="pypa", name="cibuildwheel", ref="main")),
    # Project(repo=Repository(owner="pypa", name="pip", ref="main")),
    # Project(repo=Repository(owner="pypa", name="setuptools", ref="main")),
    # Project(repo=Repository(owner="python", name="mypy", ref="master")),
    # Project(
    #     repo=Repository(
    #         owner="python",
    #         name="typeshed",
    #         ref="main",
    #     ),
    #     check_options=CheckOptions(select="PYI"),
    # ),
    # Project(repo=Repository(owner="python-poetry", name="poetry", ref="master")),
    # Project(repo=Repository(owner="reflex-dev", name="reflex", ref="main")),
    # Project(repo=Repository(owner="rotki", name="rotki", ref="develop")),
    # Project(repo=Repository(owner="scikit-build", name="scikit-build", ref="main")),
    # Project(
    #     repo=Repository(owner="scikit-build", name="scikit-build-core", ref="main")
    # ),
    # Project(repo=Repository(owner="sphinx-doc", name="sphinx", ref="master")),
    # Project(repo=Repository(owner="spruceid", name="siwe-py", ref="main")),
    # Project(repo=Repository(owner="tiangolo", name="fastapi", ref="master")),
    # Project(repo=Repository(owner="yandex", name="ch-backup", ref="main")),
    # Project(
    #     repo=Repository(owner="zulip", name="zulip", ref="main"),
    #     check_options=CheckOptions(select="ALL"),
    # ),
]