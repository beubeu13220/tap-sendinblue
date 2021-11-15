"""Stream type classes for tap-sendinblue."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_sendinblue.client import SendinblueStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class ListsStream(SendinblueStream):
    """Define custom stream."""
    name = "lists"
    path = "/contacts/lists"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.lists[*]"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("id",th.IntegerType
        ),

        th.Property("name",th.StringType
        ),

        th.Property("totalBlacklisted",th.IntegerType,
        ),

        th.Property("totalSubscribers",th.IntegerType,
        ),

        th.Property("uniqueSubscribers",th.IntegerType,
        ),

        th.Property("folderId",th.IntegerType,
        ),

    ).to_dict()

class CampaignsStream(SendinblueStream):
    """Define custom stream."""
    name = "campaigns"
    path = "/emailCampaigns"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.campaigns[*]"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType
        ),

        th.Property("name",th.StringType,
        ),

    ).to_dict()

class ListMembersStream(SendinblueStream):
    """Define custom stream."""
    name = "listmembers"
    path = "/contacts/lists/{listId}/contacts"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.contacts[*]"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("email", th.StringType,
        ),

        th.Property("id",th.IntegerType,
        ),

        th.Property("emailBlacklisted",th.BooleanType,
        ),

        th.Property("smsBlacklisted",th.BooleanType,
        ),

        th.Property("createdAt",th.DateTimeType,
        ),

        th.Property("modifiedAt",th.DateTimeType,
        ),

        th.Property("attributes",th.DateTimeType,
        ),

        #th.Property("listIds",th.ArrayType(
        #    th.ObjectType(
        #        th.Property("id",th.IntegerType),
        #        th.Property("id",th.IntegerType),
        #        th.Property("id",th.IntegerType),
            #))
        #),
        
        #th.Property("listIds",th.ObjectType(
        #    th.ArrayType(th.IntegerType))),
        #th.Property("listIds",th.ArrayType(
        #    th.ObjectType("id",th.IntegerType))),
        #th.Property("listIds",th.ArrayType(th.IntegerType),
        #),
        #
        
        #th.Property("listUnsubscribed",th.ArrayType(th.IntegerType),
        #),

    ).to_dict()
