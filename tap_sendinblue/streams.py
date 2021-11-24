"""Stream type classes for tap-sendinblue."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_sendinblue.client import SendinblueStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ListsStream(SendinblueStream):
    """Define custom stream."""
    name = "lists"
    path = "/contacts/lists"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.lists[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("totalBlacklisted", th.IntegerType),
        th.Property("totalSubscribers", th.IntegerType),
        th.Property("uniqueSubscribers", th.IntegerType),
        th.Property("folderId", th.IntegerType),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "list_id": record["id"],
        }


class CampaignsStream(SendinblueStream):
    """Define custom stream."""
    name = "campaigns"
    path = "/emailCampaigns"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.campaigns[*]"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
    ).to_dict()


class ListMembersStream(SendinblueStream):
    """Define custom stream."""
    name = "listmembers"
    path = "/contacts/lists/{list_id}/contacts"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.contacts[*]"
    parent_stream_type = ListsStream

    schema = th.PropertiesList(
        th.Property("email", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("emailBlacklisted", th.BooleanType),
        th.Property("smsBlacklisted", th.BooleanType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("modifiedAt", th.DateTimeType),
        th.Property("attributes", th.ObjectType(
                th.Property("value", th.StringType), th.Property("label", th.StringType)
            ),
        ),
    ).to_dict()
