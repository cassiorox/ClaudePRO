Create ad groups (ad-groups)
https://developers.google.com/google-ads/api/docs/campaigns/create-ad-groups
Baixado para Google Ads API v23

# Create Ad Groups

(Fallback URL: original .../ad-groups/overview returned 404; canonical guide is .../campaigns/create-ad-groups.)

The best way to set up new ad groups in the API is to use the Add Ad Groups code example in the Basic Operations folder of your client library. Ad groups are created via AdGroupService.MutateAdGroups. Key fields: name, status (e.g., ENABLED), campaign (resource name), type (e.g., SEARCH_STANDARD), and optional cpc_bid_micros.

## Python code example
```python
import uuid
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

def main(client: GoogleAdsClient, customer_id: str, campaign_id: str) -> None:
    ad_group_service = client.get_service("AdGroupService")
    campaign_service = client.get_service("CampaignService")

    # Create ad group.
    ad_group_operation = client.get_type("AdGroupOperation")
    ad_group = ad_group_operation.create
    ad_group.name = f"Earth to Mars cruises {uuid.uuid4()}"
    ad_group.status = client.enums.AdGroupStatusEnum.ENABLED
    ad_group.campaign = campaign_service.campaign_path(customer_id, campaign_id)
    ad_group.type_ = client.enums.AdGroupTypeEnum.SEARCH_STANDARD
    ad_group.cpc_bid_micros = 10000000

    operations = [ad_group_operation]

    ad_group_response = ad_group_service.mutate_ad_groups(
        customer_id=customer_id,
        operations=operations,
    )
    print(f"Created ad group {ad_group_response.results[0].resource_name}.")
```

You may add as many ad groups as you need by appending more AdGroupOperation objects to the operations list (batching). cpc_bid_micros is in micros (1,000,000 = 1 currency unit; example uses 10,000,000 = $10).

(Java, C#, PHP, Ruby, and Perl samples are also available on the source page.)

Page last updated 2026-05-13 UTC. Content reflects Google Ads API v23 (latest serving; samples reference v24 client library).
