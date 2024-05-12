from diagrams import Diagram, Cluster
from diagrams.gcp.analytics import (
    BigQuery,
    PubSub,
    Dataflow,
)
from diagrams.gcp.database import SQL
from diagrams.gcp.storage import Storage
from diagrams.onprem.analytics import Superset

graph_attr = {
    "fontsize": "12",
    "bgcolor": "grey95",
}

with Diagram(
    "Built with diagrams - https://github.com/mingrammer/diagrams",
    filename="sample_pipeline",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    with Cluster("Source data"):
        sources_group = [Storage("GCS"), PubSub("Streaming data")]

    with Cluster("Tranformation Layer"):
        dataflow = Dataflow("Cloud Dataflow")

    with Cluster("Databases"):
        db_group = SQL("Cloud SQL")

    with Cluster("Data Warehouse"):
        dwh = BigQuery("BigQuery")

    sources_group >> dataflow
    dataflow >> dwh
    db_group >> dwh
    dwh >> Superset("Dashboarding")
