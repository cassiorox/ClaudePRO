Keyword Ideas (generate-keyword-ideas)
https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas
Baixado para Google Ads API v24

# Keyword Ideas

Using the [`KeywordPlanIdeaService`](https://developers.google.com/google-ads/api/reference/rpc/v24/KeywordPlanIdeaService), you
can search for new keywords that are relevant to your Google Search campaign,
or find historical metrics on keywords.

## Generate ideas

Generate keyword ideas for a campaign with
[`KeywordPlanIdeaService.GenerateKeywordIdeas`](https://developers.google.com/google-ads/api/reference/rpc/v24/KeywordPlanIdeaService/GenerateKeywordIdeas).

You can provide keyword and URL seeds to generate ideas. Set targeting
parameters such as locations, language, and network settings to narrow down
your search. Historical statistics such as search volume data are returned to
help you determine if you want to use the keywords for your campaign. For users
familiar with the Google Ads UI, this is similar to
[Keyword Planner](https://support.google.com/google-ads/answer/6325025).

There are several ways you can create seeds for generating new keywords:

- For words or phrases that describe what you're advertising,
use [`KeywordSeed`](https://developers.google.com/google-ads/api/reference/rpc/v24/KeywordSeed). This could be a general type
of business you are targeting such as plumbers, or it could be a product or
service you offer such as drain cleaning.

- For the URL of a webpage or entire website related to your business, use
[`UrlSeed`](https://developers.google.com/google-ads/api/reference/rpc/v24/UrlSeed). The URL seed targets only a specific
URL. If there are no hits, the search automatically expands up to the pages
from the same domain.

For URL seeds, the contents of hyperlinks are _not_ used to generate keyword
ideas.

- For both keyword seeds and a URL seeds, use
[`KeywordAndUrlSeed`](https://developers.google.com/google-ads/api/reference/rpc/v24/KeywordAndUrlSeed).

Using `KeywordAndUrlSeed` can result in a larger volume of keyword ideas, as
compared to just `UrlSeed`.

- For an entire site, use [`SiteSeed`](https://developers.google.com/google-ads/api/reference/rpc/v24/SiteSeed). Given a
top-level domain name, such as `www.example.com`, the site seed
generates up to 250,000 keyword ideas from publicly available information.


To narrow down your targeting, you can:

- Set the language with
[`GenerateKeywordIdeasRequest.language`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#language). See
[Language Constants](https://developers.google.com/google-ads/api/data/codes-formats#languages) for
valid IDs.
- Set the location with
[`GenerateKeywordIdeasRequest.geo_target_constants`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#geo_target_constants%5B%5D). See
[Geo Targets](https://developers.google.com/google-ads/api/data/geotargets) for valid IDs.
- Set the network with
[`GenerateKeywordIdeasRequest.keyword_plan_network`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#keyword_plan_network).
- Set whether to include adult keywords with
[`GenerateKeywordIdeasRequest.include_adult_keywords`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#include_adult_keywords).
- [Refine keywords](https://support.google.com/google-ads/answer/9907498) with
[`GenerateKeywordIdeasRequest.keyword_annotation`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#keyword_annotation%5B%5D).
- Set the date range with
[`GenerateKeywordIdeasRequest.historical_metrics_options`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#historical_metrics_options).

The result set in the response supports [pagination](https://developers.google.com/google-ads/api/docs/reporting/paging).

Ideas are returned with historical metrics which can be used to filter a list
down to use with forecasts. For example, you might only want to target high
search volumes to maximize the reach of your campaign, or you might want to
target only higher competition scores to boost your awareness.

### Java

```java
private void runExample(
    GoogleAdsClient googleAdsClient,
    long customerId,
    long languageId,
    List<Long> locationIds,
    List<String> keywords,
    @Nullable String pageUrl) {
  try (KeywordPlanIdeaServiceClient keywordPlanServiceClient =
      googleAdsClient.getLatestVersion().createKeywordPlanIdeaServiceClient()) {
    GenerateKeywordIdeasRequest.Builder requestBuilder =
        GenerateKeywordIdeasRequest.newBuilder()
            .setCustomerId(Long.toString(customerId))
            // Sets the language resource using the provided language ID.
            .setLanguage(ResourceNames.languageConstant(languageId))
            // Sets the network. To restrict to only Google Search, change the parameter below to
            // KeywordPlanNetwork.GOOGLE_SEARCH.
            .setKeywordPlanNetwork(KeywordPlanNetwork.GOOGLE_SEARCH_AND_PARTNERS);

    // Adds the resource name of each location ID to the request.
    for (Long locationId : locationIds) {
      requestBuilder.addGeoTargetConstants(ResourceNames.geoTargetConstant(locationId));
    }

    // Makes sure that keywords and/or page URL were specified. The request must have exactly one
    // of urlSeed, keywordSeed, or keywordAndUrlSeed set.
    if (keywords.isEmpty() && pageUrl == null) {
      throw new IllegalArgumentException(
          "At least one of keywords or page URL is required, but neither was specified.");
    }

    if (keywords.isEmpty()) {
      // Only page URL was specified, so use a UrlSeed.
      requestBuilder.getUrlSeedBuilder().setUrl(pageUrl);
    } else if (pageUrl == null) {
      // Only keywords were specified, so use a KeywordSeed.
      requestBuilder.getKeywordSeedBuilder().addAllKeywords(keywords);
    } else {
      // Both page URL and keywords were specified, so use a KeywordAndUrlSeed.
      requestBuilder.getKeywordAndUrlSeedBuilder().setUrl(pageUrl).addAllKeywords(keywords);
    }

    // Sends the keyword ideas request.
    GenerateKeywordIdeasPagedResponse response =
        keywordPlanServiceClient.generateKeywordIdeas(requestBuilder.build());
    // Prints each result in the response.
    for (GenerateKeywordIdeaResult result : response.iterateAll()) {
      System.out.printf(
          "Keyword idea text '%s' has %d average monthly searches and '%s' competition.%n",
          result.getText(),
          result.getKeywordIdeaMetrics().getAvgMonthlySearches(),
          result.getKeywordIdeaMetrics().getCompetition());
    }
  }
}
```
GenerateKeywordIdeas.java

### C#

```csharp
public void Run(GoogleAdsClient client, long customerId, long[] locationIds,
    long languageId, string[] keywordTexts, string pageUrl)
{
    KeywordPlanIdeaServiceClient keywordPlanIdeaService =
        client.GetService(Services.V24.KeywordPlanIdeaService);

    // Make sure that keywords and/or page URL were specified. The request must have
    // exactly one of urlSeed, keywordSeed, or keywordAndUrlSeed set.
    if (keywordTexts.Length == 0 && string.IsNullOrEmpty(pageUrl))
    {
        throw new ArgumentException("At least one of keywords or page URL is required, " +
            "but neither was specified.");
    }

    // Specify the optional arguments of the request as a keywordSeed, UrlSeed,
    // or KeywordAndUrlSeed.
    GenerateKeywordIdeasRequest request = new GenerateKeywordIdeasRequest()
    {
        CustomerId = customerId.ToString(),
    };

    if (keywordTexts.Length == 0)
    {
        // Only page URL was specified, so use a UrlSeed.
        request.UrlSeed = new UrlSeed()
        {
            Url = pageUrl
        };
    }
    else if (string.IsNullOrEmpty(pageUrl))
    {
        // Only keywords were specified, so use a KeywordSeed.
        request.KeywordSeed = new KeywordSeed();
        request.KeywordSeed.Keywords.AddRange(keywordTexts);
    }
    else
    {
        // Both page URL and keywords were specified, so use a KeywordAndUrlSeed.
        request.KeywordAndUrlSeed = new KeywordAndUrlSeed();
        request.KeywordAndUrlSeed.Url = pageUrl;
        request.KeywordAndUrlSeed.Keywords.AddRange(keywordTexts);
    }

    // Create a list of geo target constants based on the resource name of specified
    // location IDs.
    foreach (long locationId in locationIds)
    {
        request.GeoTargetConstants.Add(ResourceNames.GeoTargetConstant(locationId));
    }

    request.Language = ResourceNames.LanguageConstant(languageId);
    // Set the network. To restrict to only Google Search, change the parameter below to
    // KeywordPlanNetwork.GoogleSearch.
    request.KeywordPlanNetwork = KeywordPlanNetwork.GoogleSearchAndPartners;

    try
    {
        // Generate keyword ideas based on the specified parameters.
        var response =
            keywordPlanIdeaService.GenerateKeywordIdeas(request);

        // Iterate over the results and print its detail.
        foreach (GenerateKeywordIdeaResult result in response)
        {
            KeywordPlanHistoricalMetrics metrics = result.KeywordIdeaMetrics;
            Console.WriteLine($"Keyword idea text '{result.Text}' has " +
                $"{metrics.AvgMonthlySearches} average monthly searches and competition " +
                $"is {metrics.Competition}.");
        }
    }
    catch (GoogleAdsException e)
    {
        Console.WriteLine("Failure:");
        Console.WriteLine($"Message: {e.Message}");
        Console.WriteLine($"Failure: {e.Failure}");
        Console.WriteLine($"Request ID: {e.RequestId}");
        throw;
    }
}
```
GenerateKeywordIdeas.cs

### PHP

```php
public static function runExample(
    GoogleAdsClient $googleAdsClient,
    int $customerId,
    array $locationIds,
    int $languageId,
    array $keywords,
    ?string $pageUrl
) {
    $keywordPlanIdeaServiceClient = $googleAdsClient->getKeywordPlanIdeaServiceClient();

    // Make sure that keywords and/or page URL were specified. The request must have exactly one
    // of urlSeed, keywordSeed, or keywordAndUrlSeed set.
    if (empty($keywords) && is_null($pageUrl)) {
        throw new \InvalidArgumentException(
            'At least one of keywords or page URL is required, but neither was specified.'
        );
    }

    // Specify the optional arguments of the request as a keywordSeed, urlSeed,
    // or keywordAndUrlSeed.
    $requestOptionalArgs = [];
    if (empty($keywords)) {
        // Only page URL was specified, so use a UrlSeed.
        $requestOptionalArgs['url_seed'] = new UrlSeed(['url' => $pageUrl]);
    } elseif (is_null($pageUrl)) {
        // Only keywords were specified, so use a KeywordSeed.
        $requestOptionalArgs['keyword_seed'] = new KeywordSeed(['keywords' => $keywords]);
    } else {
        // Both page URL and keywords were specified, so use a KeywordAndUrlSeed.
        $requestOptionalArgs['keyword_and_url_seed'] =
            new KeywordAndUrlSeed(['url' => $pageUrl, 'keywords' => $keywords]);
    }

    // Create a list of geo target constants based on the resource name of specified location
    // IDs.
    $geoTargetConstants =  array_map(function ($locationId) {
        return ResourceNames::forGeoTargetConstant($locationId);
    }, $locationIds);

    // Generate keyword ideas based on the specified parameters.
    $response = $keywordPlanIdeaServiceClient->generateKeywordIdeas(
        new GenerateKeywordIdeasRequest([
            // Set the language resource using the provided language ID.
            'language' => ResourceNames::forLanguageConstant($languageId),
            'customer_id' => $customerId,
            // Add the resource name of each location ID to the request.
            'geo_target_constants' => $geoTargetConstants,
            // Set the network. To restrict to only Google Search, change the parameter below to
            // KeywordPlanNetwork::GOOGLE_SEARCH.
            'keyword_plan_network' => KeywordPlanNetwork::GOOGLE_SEARCH_AND_PARTNERS
        ] + $requestOptionalArgs)
    );

    // Iterate over the results and print its detail.
    foreach ($response->iterateAllElements() as $result) {
        /** @var GenerateKeywordIdeaResult $result */
        // Note that the competition printed below is enum value.
        // For example, a value of 2 will be returned when the competition is 'LOW'.
        // A mapping of enum names to values can be found at KeywordPlanCompetitionLevel.php.
        printf(
            "Keyword idea text '%s' has %d average monthly searches and competition as %d.%s",
            $result->getText(),
            is_null($result->getKeywordIdeaMetrics()) ?
                0 : $result->getKeywordIdeaMetrics()->getAvgMonthlySearches(),
            is_null($result->getKeywordIdeaMetrics()) ?
                0 : $result->getKeywordIdeaMetrics()->getCompetition(),
            PHP_EOL
        );
    }
}
```
GenerateKeywordIdeas.php

### Python

```python
def main(
    client: GoogleAdsClient,
    customer_id: str,
    location_ids: list[str],
    language_id: str,
    keyword_texts: list[str],
    page_url: str,
):
    keyword_plan_idea_service: KeywordPlanIdeaServiceClient = (
        client.get_service("KeywordPlanIdeaService")
    )
    keyword_competition_level_enum: KeywordPlanCompetitionLevelEnum = (
        client.enums.KeywordPlanCompetitionLevelEnum
    )
    keyword_plan_network: KeywordPlanNetworkEnum = (
        client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH_AND_PARTNERS
    )
    location_rns: list[str] = map_locations_ids_to_resource_names(
        client, location_ids
    )
    google_ads_service: GoogleAdsServiceClient = client.get_service(
        "GoogleAdsService"
    )
    language_rn: str = google_ads_service.language_constant_path(language_id)

    # Either keywords or a page_url are required to generate keyword ideas
    # so this raises an error if neither are provided.
    if not (keyword_texts or page_url):
        raise ValueError(
            "At least one of keywords or page URL is required, "
            "but neither was specified."
        )

    # Only one of the fields "url_seed", "keyword_seed", or
    # "keyword_and_url_seed" can be set on the request, depending on whether
    # keywords, a page_url or both were passed to this function.
    request: GenerateKeywordIdeasRequest = client.get_type(
        "GenerateKeywordIdeasRequest"
    )
    request.customer_id = customer_id
    request.language = language_rn
    request.geo_target_constants = location_rns
    request.include_adult_keywords = False
    request.keyword_plan_network = keyword_plan_network

    # To generate keyword ideas with only a page_url and no keywords we need
    # to initialize a UrlSeed object with the page_url as the "url" field.
    if not keyword_texts and page_url:
        request.url_seed.url = page_url

    # To generate keyword ideas with only a list of keywords and no page_url
    # we need to initialize a KeywordSeed object and set the "keywords" field
    # to be a list of StringValue objects.
    if keyword_texts and not page_url:
        request.keyword_seed.keywords.extend(keyword_texts)

    # To generate keyword ideas using both a list of keywords and a page_url we
    # need to initialize a KeywordAndUrlSeed object, setting both the "url" and
    # "keywords" fields.
    if keyword_texts and page_url:
        request.keyword_and_url_seed.url = page_url
        request.keyword_and_url_seed.keywords.extend(keyword_texts)

    keyword_ideas = keyword_plan_idea_service.generate_keyword_ideas(
        request=request
    )

    idea: GenerateKeywordIdeaResult
    for idea in keyword_ideas:
        competition_value = idea.keyword_idea_metrics.competition.name
        print(
            f'Keyword idea text "{idea.text}" has '
            f'"{idea.keyword_idea_metrics.avg_monthly_searches}" '
            f'average monthly searches and "{competition_value}" '
            "competition.\n"
        )
```
generate_keyword_ideas.py

### Ruby

```ruby
def generate_keyword_ideas(customer_id, location_ids, language_id, keywords,
    page_url)
  # GoogleAdsClient will read a config file from
  # ENV['HOME']/google_ads_config.rb when called without parameters
  client = Google::Ads::GoogleAds::GoogleAdsClient.new

  # Make sure that keywords and/or page URL were specified. The request must
  # have exactly one of urlSeed, keywordSeed, or keywordAndUrlSeed set.
  if keywords.reject {|k| k.nil?}.empty? && page_url.nil?
    raise "At least one of keywords or page URL is required."
  end

  kp_idea_service = client.service.keyword_plan_idea

  options_hash = if keywords.empty?
                   seed = client.resource.url_seed do |seed|
                     seed.url = page_url
                   end
                   {url_seed: seed}
                 elsif page_url.nil?
                   seed = client.resource.keyword_seed do |seed|
                     keywords.each do |keyword|
                       seed.keywords << keyword
                     end
                   end
                   {keyword_seed: seed}
                 else
                   seed = client.resource.keyword_and_url_seed do |seed|
                     seed.url = page_url
                     keywords.each do |keyword|
                       seed.keywords << keyword
                     end
                   end
                   {keyword_and_url_seed: seed}
                 end

  geo_target_constants = location_ids.map do |location_id|
    client.path.geo_target_constant(location_id)
  end

  include_adult_keywords = true

  response = kp_idea_service.generate_keyword_ideas(
    customer_id: customer_id,
    language: client.path.language_constant(language_id),
    geo_target_constants: geo_target_constants,
    include_adult_keywords: include_adult_keywords,
    # To restrict to only Google Search, change the parameter below to
    # :GOOGLE_SEARCH
    keyword_plan_network: :GOOGLE_SEARCH_AND_PARTNERS,
    **options_hash
  )

  response.each do |result|
    monthly_searches = if result.keyword_idea_metrics.nil?
                         0
                       else
                         result.keyword_idea_metrics.avg_monthly_searches
                       end
    competition = if result.keyword_idea_metrics.nil?
                    :UNSPECIFIED
                  else
                    result.keyword_idea_metrics.competition
                  end
    puts "Keyword idea text #{result.text} has #{monthly_searches} average " +
        "monthly searches and competition as #{competition}."
  end
end
```
generate_keyword_ideas.rb

### Perl

```perl
sub generate_keyword_ideas {
  my (
    $api_client,  $customer_id,   $location_ids,
    $language_id, $keyword_texts, $page_url
  ) = @_;

  # Make sure that keywords and/or page URL were specified. The request must have
  # exactly one of urlSeed, keywordSeed, or keywordAndUrlSeed set.
  if (not scalar @$keyword_texts and not $page_url) {
    die "At least one of keywords or page URL is required, " .
      "but neither was specified.";
  }

  # Specify the optional arguments of the request as a keywordSeed, urlSeed,
  # or keywordAndUrlSeed.
  my $request_option_args = {};
  if (!scalar @$keyword_texts) {
    # Only page URL was specified, so use a UrlSeed.
    $request_option_args->{urlSeed} =
      Google::Ads::GoogleAds::V24::Services::KeywordPlanIdeaService::UrlSeed->
      new({
        url => $page_url
      });
  } elsif (not $page_url) {
    # Only keywords were specified, so use a KeywordSeed.
    $request_option_args->{keywordSeed} =
      Google::Ads::GoogleAds::V24::Services::KeywordPlanIdeaService::KeywordSeed
      ->new({
        keywords => $keyword_texts
      });
  } else {
    # Both page URL and keywords were specified, so use a KeywordAndUrlSeed.
    $request_option_args->{keywordAndUrlSeed} =
      Google::Ads::GoogleAds::V24::Services::KeywordPlanIdeaService::KeywordAndUrlSeed
      ->new({
        url      => $page_url,
        keywords => $keyword_texts
      });
  }

  # Create a list of geo target constants based on the resource name of specified
  # location IDs.
  my $geo_target_constants = [
    map (
      Google::Ads::GoogleAds::V24::Utils::ResourceNames::geo_target_constant(
        $_),
      @$location_ids)];

  # Generate keyword ideas based on the specified parameters.
  my $keyword_ideas_response =
    $api_client->KeywordPlanIdeaService()->generate_keyword_ideas({
      customerId => $customer_id,
      # Set the language resource using the provided language ID.
      language =>
        Google::Ads::GoogleAds::V24::Utils::ResourceNames::language_constant(
        $language_id),
      # Add the resource name of each location ID to the request.
      geoTargetConstants => $geo_target_constants,
      # Set the network. To restrict to only Google Search, change the parameter below
      # to GOOGLE_SEARCH.
      keywordPlanNetwork => GOOGLE_SEARCH_AND_PARTNERS,
      %$request_option_args
    });

  # Iterate over the results and print its detail.
  foreach my $result (@{$keyword_ideas_response->{results}}) {
    printf "Keyword idea text '%s' has %d average monthly searches " .
      "and '%s' competition.\n", $result->{text},
      $result->{keywordIdeaMetrics}{avgMonthlySearches}
      ? $result->{keywordIdeaMetrics}{avgMonthlySearches}
      : 0,
      $result->{keywordIdeaMetrics}{competition}
      ? $result->{keywordIdeaMetrics}{competition}
      : "undef";
  }

  return 1;
}
```
generate_keyword_ideas.pl

### curl

```sh
# This code example generates keyword ideas.
#
# Variables:
#   API_VERSION,
#   CUSTOMER_ID,
#   DEVELOPER_TOKEN,
#   MANAGER_CUSTOMER_ID,
#   OAUTH2_ACCESS_TOKEN:
#     See https://developers.google.com/google-ads/api/rest/auth#request_headers
#     for details.
#
#   LANGUAGE: The resource name of the language to target. This is in the format
#     of "languageConstants/{criterion_id}". See
#     https://developers.google.com/google-ads/api/data/codes-formats#languages
#     for the available criterion_id values.
#   GEO_TARGET_CONSTANT: The resource name of the geo target constant to
#     generate keyword ideas for. This is in the format of
#     "geoTargetConstants/{criterion_id}". See
#     https://developers.google.com/google-ads/api/data/geotargets for the
#     available criterion_id values.
#   KEYWORD: The keyword to generate keyword ideas for.
#   URL: The URL of the website to generate keyword ideas for.
curl -f --request POST \
"https://googleads.googleapis.com/v${API_VERSION}/customers/${CUSTOMER_ID}:generateKeywordIdeas" \
--header "Content-Type: application/json" \
--header "developer-token: ${DEVELOPER_TOKEN}" \
--header "login-customer-id: ${MANAGER_CUSTOMER_ID}" \
--header "Authorization: Bearer ${OAUTH2_ACCESS_TOKEN}" \
--data @- <<EOF
{
  "language": "${LANGUAGE}",
  "geoTargetConstants": [
    "${GEO_TARGET_CONSTANT}"
  ],
  "includeAdultKeywords": false,
  "keywordPlanNetwork": "GOOGLE_SEARCH",
  "keywordAndUrlSeed": {
    "keywords": [
      "${KEYWORD}"
    ],
    "url": "${URL}"
  }
}
EOF
```
generate_keyword_ideas.sh

### Map to the UI

[`KeywordPlanIdeaService.GenerateKeywordIdeas`](https://developers.google.com/google-ads/api/reference/rpc/v24/KeywordPlanIdeaService/GenerateKeywordIdeas)
has similar functionality in the UI's Keyword Planner.

| Keyword Planner UI | Google Ads API |
| --- | --- |
| Enter Keywords and URLs | - [`GenerateKeywordIdeasRequest.keyword_and_url_seed`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#keyword_and_url_seed)<br>- [`GenerateKeywordIdeasRequest.keyword_seed`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#keyword_seed)<br>- [`GenerateKeywordIdeasRequest.url_seed`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#url_seed) |
| Locations | [`GenerateKeywordIdeasRequest.geo_target_constants`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#geo_target_constants[]) |
| Adult Keywords | [`GenerateKeywordIdeasRequest.include_adult_keywords`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#include_adult_keywords) |
| Language | [`GenerateKeywordIdeasRequest.language`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#language) |
| Search Networks | [`GenerateKeywordIdeasRequest.keyword_plan_network`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#keyword_plan_network) |
| Refine Keywords | [`GenerateKeywordIdeasRequest.keyword_annotation`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#keyword_annotation[]) |
| Date Range | [`GenerateKeywordIdeasRequest.historical_metrics_options`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeasRequest#historical_metrics_options) |
| Results: Keyword | [`GenerateKeywordIdeaResult.text`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeaResult#text) |
| Results: Metrics | [`GenerateKeywordIdeaResult.keyword_idea_metrics`](https://developers.google.com/google-ads/api/reference/rpc/v24/GenerateKeywordIdeaResult#keyword_idea_metrics) |
