Create campaigns
https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns
Baixado para Google Ads API v23

[Skip to main content](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#main-content)

[![Google Ads API](https://developers.google.com/static/ads/images/ads_192px_clr.svg)](https://developers.google.com/google-ads/api)

- [GoogleAds API](https://developers.google.com/google-ads/api)

`/`

Language

- [English](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns)
- [Deutsch](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=de)
- [Español](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=es)
- [Español – América Latina](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=es-419)
- [Français](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=fr)
- [Indonesia](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=id)
- [Italiano](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=it)
- [Polski](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=pl)
- [Português – Brasil](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=pt-br)
- [Tiếng Việt](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=vi)
- [Türkçe](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=tr)
- [Русский](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=ru)
- [עברית](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=he)
- [العربيّة](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=ar)
- [فارسی](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=fa)
- [हिंदी](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=hi)
- [বাংলা](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=bn)
- [ภาษาไทย](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=th)
- [中文 – 简体](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=zh-cn)
- [中文 – 繁體](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=zh-tw)
- [日本語](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=ja)
- [한국어](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns?hl=ko)

[Sign in](https://developers.google.com/_d/signin?continue=https%3A%2F%2Fdevelopers.google.com%2Fgoogle-ads%2Fapi%2Fdocs%2Fcampaigns%2Fcreate-campaigns&prompt=select_account)

- On this page
- [Add campaigns](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#add_campaigns)
- [Display Expansion on Search campaigns](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#display_expansion_on_search_campaigns)
- [Campaign groups](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#campaign_groups)

Join us live on [Discord](https://discord.com/events/971845904002871346/1514967320227876966) on the Google Advertising and Measurement Community server and on [YouTube](https://www.youtube.com/watch?v=d7CVgPFlWQo) on June 25th at 10:00 AM EST! We will discuss the new features added in v24.2 of the Google Ads API.


- [Home](https://developers.google.com/)
- [Products](https://developers.google.com/products)
- [Google Ads API](https://developers.google.com/google-ads/api)

Was this helpful?



 Send feedback



# Create Campaigns    Stay organized with collections      Save and categorize content based on your preferences.

- On this page
- [Add campaigns](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#add_campaigns)
- [Display Expansion on Search campaigns](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#display_expansion_on_search_campaigns)
- [Campaign groups](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#campaign_groups)

![Spark icon](https://developers.google.com/_static/images/icons/spark.svg)

## Page Summary

outlined\_flag

- The best way to set up new campaigns in the API is to use the Add Campaigns code example in the Basic Operations folder of your client library, which handles authentication and walks through required settings like budget, bidding, type, and dates.

- Display Expansion on Search campaigns can help you get additional conversions on the Google Display Network using unspent Search budgets at similar cost per conversion as Search, and you can enable this by setting the `target_content_network` field to `true`.

- You can use the CampaignGroupService to create campaign groups for tracking the overall performance of multiple campaigns with similar goals.

- Each campaign can only belong to one campaign group at a time, and campaigns with shared budgets cannot be added to a campaign group.


## Add campaigns

The best way to set up new campaigns in the API is to use the **Add Campaigns** [code example](https://developers.google.com/google-ads/api/docs/client-libs) in the **Basic Operations** folder of your
client library. The sample handles all the background authentication tasks for
you and walks you through the settings required for establishing a new campaign,
including the budget, bidding strategy, campaign type, start & end dates, and
more.

## Display Expansion on Search campaigns

[Display Expansion on Search\\
campaigns](https://support.google.com/google-ads/answer/7193800) can help you get
additional conversions on the Google Display Network using unspent Search
budgets at similar cost per conversion as Search. You can enable Display
Expansion on Search campaigns by setting the
[`target_content_network`](https://developers.google.com/google-ads/api/reference/rpc/v24/Campaign.NetworkSettings#target_content_network)
field of the campaign's
[`network_settings`](https://developers.google.com/google-ads/api/reference/rpc/v24/Campaign#network_settings) to `true`.

The sample creates a shared [`CampaignBudget`](https://developers.google.com/google-ads/api/reference/rpc/v24/CampaignBudget)
for use with the new campaign. Check out the
[campaign budgets guide](https://developers.google.com/google-ads/api/docs/campaigns/budgets/overview) for other budget
options.

[Java](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#java)[C#](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#c)[PHP](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#php)[Python](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#python)[Ruby](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#ruby)[Perl](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#perl)[curl](https://developers.google.com/google-ads/api/docs/campaigns/create-campaigns#curl)More

```
// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package com.google.ads.googleads.examples.basicoperations;

import static com.google.ads.googleads.examples.utils.CodeSampleHelper.getPrintableDateTime;
import static com.google.ads.googleads.v24.enums.EuPoliticalAdvertisingStatusEnum.EuPoliticalAdvertisingStatus.DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING;

import com.beust.jcommander.Parameter;
import com.google.ads.googleads.examples.utils.ArgumentNames;
import com.google.ads.googleads.examples.utils.CodeSampleParams;
import com.google.ads.googleads.lib.GoogleAdsClient;
import com.google.ads.googleads.v24.common.ManualCpc;
import com.google.ads.googleads.v24.enums.AdvertisingChannelTypeEnum.AdvertisingChannelType;
import com.google.ads.googleads.v24.enums.BudgetDeliveryMethodEnum.BudgetDeliveryMethod;
import com.google.ads.googleads.v24.enums.CampaignStatusEnum.CampaignStatus;
import com.google.ads.googleads.v24.errors.GoogleAdsError;
import com.google.ads.googleads.v24.errors.GoogleAdsException;
import com.google.ads.googleads.v24.resources.Campaign;
import com.google.ads.googleads.v24.resources.Campaign.NetworkSettings;
import com.google.ads.googleads.v24.resources.CampaignBudget;
import com.google.ads.googleads.v24.services.CampaignBudgetOperation;
import com.google.ads.googleads.v24.services.CampaignBudgetServiceClient;
import com.google.ads.googleads.v24.services.CampaignOperation;
import com.google.ads.googleads.v24.services.CampaignServiceClient;
import com.google.ads.googleads.v24.services.MutateCampaignBudgetsResponse;
import com.google.ads.googleads.v24.services.MutateCampaignResult;
import com.google.ads.googleads.v24.services.MutateCampaignsResponse;
import com.google.common.collect.ImmutableList;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.joda.time.DateTime;

/** Adds new campaigns to a client account. */
public class AddCampaigns {

  /** The number of campaigns this example will add. */
  private static final int NUMBER_OF_CAMPAIGNS_TO_ADD = 2;

  private static class AddCampaignsParams extends CodeSampleParams {

    @Parameter(names = ArgumentNames.CUSTOMER_ID, required = true)
    private Long customerId;
  }

  public static void main(String[] args) {
    AddCampaignsParams params = new AddCampaignsParams();
    if (!params.parseArguments(args)) {

      // Either pass the required parameters for this example on the command line, or insert them
      // into the code here. See the parameter class definition above for descriptions.
      params.customerId = Long.parseLong("INSERT_CUSTOMER_ID_HERE");
    }

    GoogleAdsClient googleAdsClient = null;
    try {
      googleAdsClient = GoogleAdsClient.newBuilder().fromPropertiesFile().build();
    } catch (FileNotFoundException fnfe) {
      System.err.printf(
          "Failed to load GoogleAdsClient configuration from file. Exception: %s%n", fnfe);
      System.exit(1);
    } catch (IOException ioe) {
      System.err.printf("Failed to create GoogleAdsClient. Exception: %s%n", ioe);
      System.exit(1);
    }

    try {
      new AddCampaigns().runExample(googleAdsClient, params.customerId);
    } catch (GoogleAdsException gae) {
      // GoogleAdsException is the base class for most exceptions thrown by an API request.
      // Instances of this exception have a message and a GoogleAdsFailure that contains a
      // collection of GoogleAdsErrors that indicate the underlying causes of the
      // GoogleAdsException.
      System.err.printf(
          "Request ID %s failed due to GoogleAdsException. Underlying errors:%n",
          gae.getRequestId());
      int i = 0;
      for (GoogleAdsError googleAdsError : gae.getGoogleAdsFailure().getErrorsList()) {
        System.err.printf("  Error %d: %s%n", i++, googleAdsError);
      }
      System.exit(1);
    }
  }

  /**
   * Creates a new CampaignBudget in the specified client account.
   *
   * @param googleAdsClient the Google Ads API client.
   * @param customerId the client customer ID.
   * @return resource name of the newly created budget.
   * @throws GoogleAdsException if an API request failed with one or more service errors.
   */
  private static String addCampaignBudget(GoogleAdsClient googleAdsClient, long customerId) {
    CampaignBudget budget =
        CampaignBudget.newBuilder()
            .setName("Interplanetary Cruise Budget #" + getPrintableDateTime())
            .setDeliveryMethod(BudgetDeliveryMethod.STANDARD)
            .setAmountMicros(500_000)
            .build();

    CampaignBudgetOperation op = CampaignBudgetOperation.newBuilder().setCreate(budget).build();

    try (CampaignBudgetServiceClient campaignBudgetServiceClient =
        googleAdsClient.getLatestVersion().createCampaignBudgetServiceClient()) {
      MutateCampaignBudgetsResponse response =
          campaignBudgetServiceClient.mutateCampaignBudgets(
              Long.toString(customerId), ImmutableList.of(op));
      String budgetResourceName = response.getResults(0).getResourceName();
      System.out.printf("Added budget: %s%n", budgetResourceName);
      return budgetResourceName;
    }
  }

  /**
   * Runs the example.
   *
   * @param googleAdsClient the Google Ads API client.
   * @param customerId the client customer ID.
   * @throws GoogleAdsException if an API request failed with one or more service errors.
   */
  private void runExample(GoogleAdsClient googleAdsClient, long customerId) {

    // Creates a single shared budget to be used by the campaigns added below.
    String budgetResourceName = addCampaignBudget(googleAdsClient, customerId);

    List<CampaignOperation> operations = new ArrayList<>(NUMBER_OF_CAMPAIGNS_TO_ADD);

    for (int i = 0; i < NUMBER_OF_CAMPAIGNS_TO_ADD; i++) {
      // Configures the campaign network options
      NetworkSettings networkSettings =
          NetworkSettings.newBuilder()
              .setTargetGoogleSearch(true)
              .setTargetSearchNetwork(true)
              // Enables Display Expansion on Search campaigns. See
              // https://support.google.com/google-ads/answer/7193800 to learn more.
              .setTargetContentNetwork(true)
              .setTargetPartnerSearchNetwork(false)
              .build();

      // Creates the campaign.
      Campaign campaign =
          Campaign.newBuilder()
              .setName("Interplanetary Cruise #" + getPrintableDateTime())
              .setAdvertisingChannelType(AdvertisingChannelType.SEARCH)
              // Recommendation: Set the campaign to PAUSED when creating it to prevent
              // the ads from immediately serving. Set to ENABLED once you've added
              // targeting and the ads are ready to serve
              .setStatus(CampaignStatus.PAUSED)
              // Sets the bidding strategy and budget.
              .setManualCpc(ManualCpc.newBuilder().build())
              .setCampaignBudget(budgetResourceName)
              // Adds the networkSettings configured above.
              .setNetworkSettings(networkSettings)
              // Declares whether this campaign serves political ads targeting the EU.
              .setContainsEuPoliticalAdvertising(DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING)
              // Optional: Sets the start & end dates.
              .setStartDateTime(new DateTime().plusDays(1).toString("yyyy-MM-dd 00:00:00"))
              .setEndDateTime(new DateTime().plusDays(30).toString("yyyy-MM-dd 23:59:59"))
              .build();

      CampaignOperation op = CampaignOperation.newBuilder().setCreate(campaign).build();
      operations.add(op);
    }

    try (CampaignServiceClient campaignServiceClient =
        googleAdsClient.getLatestVersion().createCampaignServiceClient()) {
      MutateCampaignsResponse response =
          campaignServiceClient.mutateCampaigns(Long.toString(customerId), operations);
      System.out.printf("Added %d campaigns:%n", response.getResultsCount());
      for (MutateCampaignResult result : response.getResultsList()) {
        System.out.println(result.getResourceName());
      }
    }
  }
}
AddCampaigns.java


```

```
// Copyright 2019 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

using CommandLine;
using Google.Ads.Gax.Examples;
using Google.Ads.GoogleAds.Config;
using Google.Ads.GoogleAds.Extensions.Config;
using Google.Ads.GoogleAds.Lib;
using Google.Ads.GoogleAds.V24.Common;
using Google.Ads.GoogleAds.V24.Errors;
using Google.Ads.GoogleAds.V24.Resources;
using Google.Ads.GoogleAds.V24.Services;
using System;
using System.Collections.Generic;
using System.Configuration;
using static Google.Ads.GoogleAds.V24.Enums.AdvertisingChannelTypeEnum.Types;
using static Google.Ads.GoogleAds.V24.Enums.BudgetDeliveryMethodEnum.Types;
using static Google.Ads.GoogleAds.V24.Enums.CampaignStatusEnum.Types;
using static Google.Ads.GoogleAds.V24.Enums.EuPoliticalAdvertisingStatusEnum.Types;
using static Google.Ads.GoogleAds.V24.Resources.Campaign.Types;

namespace Google.Ads.GoogleAds.Examples.V24
{
    /// <summary>
    /// This code example adds campaigns.
    /// </summary>
    public class AddCampaigns : ExampleBase
    {
        /// <summary>
        /// Command line options for running the <see cref="AddCampaigns"/> example.
        /// </summary>
        public class Options : OptionsBase
        {
            /// <summary>
            /// The Google Ads customer ID for which the call is made.
            /// </summary>
            [Option("customerId", Required = true, HelpText =\
                "The Google Ads customer ID for which the call is made.")]
            public long CustomerId { get; set; }
        }

        /// <summary>
        /// Main method, to run this code example as a standalone application.
        /// </summary>
        /// <param name="args">The command line arguments.</param>
        public static void Main(string[] args)
        {
            Options options = ExampleUtilities.ParseCommandLine<Options>(args);

            AddCampaigns codeExample = new AddCampaigns();
            Console.WriteLine(codeExample.Description);
            codeExample.Run(new GoogleAdsClient(),
                options.CustomerId);
        }

        /// <summary>
        /// Number of campaigns to create.
        /// </summary>
        private const int NUM_CAMPAIGNS_TO_CREATE = 5;

        /// <summary>
        /// Returns a description about the code example.
        /// </summary>
        public override string Description => "This code example adds campaigns. To get " +
            "campaigns, run GetCampaign.cs.";

        /// <summary>
        /// Runs the code example.
        /// </summary>
        /// <param name="client">The Google Ads client.</param>
        /// <param name="customerId">The Google Ads customer ID for which the call is made.</param>
        public void Run(GoogleAdsClient client, long customerId)
        {
            // Get the CampaignService.
            CampaignServiceClient campaignService = client.GetService(Services.V24.CampaignService);

            // Create a budget to be used for the campaign.
            string budget = CreateBudget(client, customerId);

            List<CampaignOperation> operations = new List<CampaignOperation>();

            for (int i = 0; i < NUM_CAMPAIGNS_TO_CREATE; i++)
            {
                // Create the campaign.
                Campaign campaign = new Campaign()
                {
                    Name = "Interplanetary Cruise #" + ExampleUtilities.GetRandomString(),
                    AdvertisingChannelType = AdvertisingChannelType.Search,

                    // Recommendation: Set the campaign to PAUSED when creating it to prevent
                    // the ads from immediately serving. Set to ENABLED once you've added
                    // targeting and the ads are ready to serve
                    Status = CampaignStatus.Paused,

                    // Set the bidding strategy and budget.
                    ManualCpc = new ManualCpc(),
                    CampaignBudget = budget,

                    // Set the campaign network options.
                    NetworkSettings = new NetworkSettings
                    {
                        TargetGoogleSearch = true,
                        TargetSearchNetwork = true,
                        // Enable Display Expansion on Search campaigns. See
                        // https://support.google.com/google-ads/answer/7193800 to learn more.
                        TargetContentNetwork = true,
                        TargetPartnerSearchNetwork = false
                    },

                    // Declare whether or not this campaign contains political ads targeting the EU.
                    ContainsEuPoliticalAdvertising = EuPoliticalAdvertisingStatus.DoesNotContainEuPoliticalAdvertising,

                    // Optional: Set the start date.
                    StartDateTime = DateTime.Now.AddDays(1).ToString("yyyyMMdd 00:00:00"),

                    // Optional: Set the end date.
                    EndDateTime = DateTime.Now.AddYears(1).ToString("yyyyMMdd 23:59:59"),
                };

                // Create the operation.
                operations.Add(new CampaignOperation() { Create = campaign });
            }
            try
            {
                // Add the campaigns.
                MutateCampaignsResponse retVal = campaignService.MutateCampaigns(
                    customerId.ToString(), operations);

                // Display the results.
                if (retVal.Results.Count > 0)
                {
                    foreach (MutateCampaignResult newCampaign in retVal.Results)
                    {
                        Console.WriteLine("Campaign with resource ID = '{0}' was added.",
                            newCampaign.ResourceName);
                    }
                }
                else
                {
                    Console.WriteLine("No campaigns were added.");
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

        /// <summary>
        /// Creates the budget for the campaign.
        /// </summary>
        /// <param name="client">The Google Ads client.</param>
        /// <param name="customerId">The Google Ads customer ID for which the call is made.</param>
        /// <returns>The resource name of the newly created campaign budget.</returns>
        private static string CreateBudget(GoogleAdsClient client, long customerId)
        {
            // Get the BudgetService.
            CampaignBudgetServiceClient budgetService = client.GetService(
                Services.V24.CampaignBudgetService);

            // Create the campaign budget.
            CampaignBudget budget = new CampaignBudget()
            {
                Name = "Interplanetary Cruise Budget #" + ExampleUtilities.GetRandomString(),
                DeliveryMethod = BudgetDeliveryMethod.Standard,
                AmountMicros = 500000
            };

            // Create the operation.
            CampaignBudgetOperation budgetOperation = new CampaignBudgetOperation()
            {
                Create = budget
            };

            // Create the campaign budget.
            MutateCampaignBudgetsResponse response = budgetService.MutateCampaignBudgets(
                customerId.ToString(), new CampaignBudgetOperation[] { budgetOperation });
            return response.Results[0].ResourceName;
        }
    }
}
AddCampaigns.cs


```

```
<?php

/**
 * Copyright 2018 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

namespace Google\Ads\GoogleAds\Examples\BasicOperations;

require __DIR__ . '/../../vendor/autoload.php';

use GetOpt\GetOpt;
use Google\Ads\GoogleAds\Examples\Utils\ArgumentNames;
use Google\Ads\GoogleAds\Examples\Utils\ArgumentParser;
use Google\Ads\GoogleAds\Examples\Utils\Helper;
use Google\Ads\GoogleAds\Lib\V24\GoogleAdsClient;
use Google\Ads\GoogleAds\Lib\V24\GoogleAdsClientBuilder;
use Google\Ads\GoogleAds\Lib\V24\GoogleAdsException;
use Google\Ads\GoogleAds\Lib\OAuth2TokenBuilder;
use Google\Ads\GoogleAds\V24\Common\ManualCpc;
use Google\Ads\GoogleAds\V24\Enums\AdvertisingChannelTypeEnum\AdvertisingChannelType;
use Google\Ads\GoogleAds\V24\Enums\BudgetDeliveryMethodEnum\BudgetDeliveryMethod;
use Google\Ads\GoogleAds\V24\Enums\CampaignStatusEnum\CampaignStatus;
use Google\Ads\GoogleAds\V24\Enums\EuPoliticalAdvertisingStatusEnum\EuPoliticalAdvertisingStatus;
use Google\Ads\GoogleAds\V24\Errors\GoogleAdsError;
use Google\Ads\GoogleAds\V24\Resources\Campaign;
use Google\Ads\GoogleAds\V24\Resources\Campaign\NetworkSettings;
use Google\Ads\GoogleAds\V24\Resources\CampaignBudget;
use Google\Ads\GoogleAds\V24\Services\CampaignBudgetOperation;
use Google\Ads\GoogleAds\V24\Services\CampaignOperation;
use Google\Ads\GoogleAds\V24\Services\MutateCampaignsRequest;
use Google\Ads\GoogleAds\V24\Services\MutateCampaignBudgetsRequest;
use Google\ApiCore\ApiException;

/** This example adds new campaigns to an account. */
class AddCampaigns
{
    private const CUSTOMER_ID = 'INSERT_CUSTOMER_ID_HERE';
    private const NUMBER_OF_CAMPAIGNS_TO_ADD = 2;

    public static function main()
    {
        // Either pass the required parameters for this example on the command line, or insert them
        // into the constants above.
        $options = (new ArgumentParser())->parseCommandArguments([\
            ArgumentNames::CUSTOMER_ID => GetOpt::REQUIRED_ARGUMENT\
        ]);

        // Generate a refreshable OAuth2 credential for authentication.
        $oAuth2Credential = (new OAuth2TokenBuilder())->fromFile()->build();

        // Construct a Google Ads client configured from a properties file and the
        // OAuth2 credentials above.
        $googleAdsClient = (new GoogleAdsClientBuilder())
            ->fromFile()
            ->withOAuth2Credential($oAuth2Credential)
            ->build();

        try {
            self::runExample(
                $googleAdsClient,
                $options[ArgumentNames::CUSTOMER_ID] ?: self::CUSTOMER_ID
            );
        } catch (GoogleAdsException $googleAdsException) {
            printf(
                "Request with ID '%s' has failed.%sGoogle Ads failure details:%s",
                $googleAdsException->getRequestId(),
                PHP_EOL,
                PHP_EOL
            );
            foreach ($googleAdsException->getGoogleAdsFailure()->getErrors() as $error) {
                /** @var GoogleAdsError $error */
                printf(
                    "\t%s: %s%s",
                    $error->getErrorCode()->getErrorCode(),
                    $error->getMessage(),
                    PHP_EOL
                );
            }
            exit(1);
        } catch (ApiException $apiException) {
            printf(
                "ApiException was thrown with message '%s'.%s",
                $apiException->getMessage(),
                PHP_EOL
            );
            exit(1);
        }
    }

    /**
     * Runs the example.
     *
     * @param GoogleAdsClient $googleAdsClient the Google Ads API client
     * @param int $customerId the customer ID
     */
    public static function runExample(GoogleAdsClient $googleAdsClient, int $customerId)
    {
        // Creates a single shared budget to be used by the campaigns added below.
        $budgetResourceName = self::addCampaignBudget($googleAdsClient, $customerId);

        // Configures the campaign network options.
        $networkSettings = new NetworkSettings([\
            'target_google_search' => true,\
            'target_search_network' => true,\
            // Enables Display Expansion on Search campaigns. See\
            // https://support.google.com/google-ads/answer/7193800 to learn more.\
            'target_content_network' => true,\
            'target_partner_search_network' => false\
        ]);

        $campaignOperations = [];
        for ($i = 0; $i < self::NUMBER_OF_CAMPAIGNS_TO_ADD; $i++) {
            // Creates a campaign.
            $campaign = new Campaign([\
                'name' => 'Interplanetary Cruise #' . Helper::getPrintableDatetime(),\
                'advertising_channel_type' => AdvertisingChannelType::SEARCH,\
                // Recommendation: Set the campaign to PAUSED when creating it to prevent\
                // the ads from immediately serving. Set to ENABLED once you've added\
                // targeting and the ads are ready to serve.\
                'status' => CampaignStatus::PAUSED,\
                // Sets the bidding strategy and budget.\
                'manual_cpc' => new ManualCpc(),\
                'campaign_budget' => $budgetResourceName,\
                // Adds the network settings configured above.\
                'network_settings' => $networkSettings,\
                // Declare whether or not this campaign serves political ads targeting the EU.\
                'contains_eu_political_advertising' =>\
                    EuPoliticalAdvertisingStatus::DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING,\
                // Optional: Sets the start and end dates.\
                'start_date_time' => date('Y-m-d 00:00:00', strtotime('+1 day')),\
                'end_date_time' => date('Y-m-d 23:59:59', strtotime('+1 month'))\
            ]);

            // Creates a campaign operation.
            $campaignOperation = new CampaignOperation();
            $campaignOperation->setCreate($campaign);
            $campaignOperations[] = $campaignOperation;
        }

        // Issues a mutate request to add campaigns.
        $campaignServiceClient = $googleAdsClient->getCampaignServiceClient();
        $response = $campaignServiceClient->mutateCampaigns(
            MutateCampaignsRequest::build($customerId, $campaignOperations)
        );

        printf("Added %d campaigns:%s", $response->getResults()->count(), PHP_EOL);

        foreach ($response->getResults() as $addedCampaign) {
            /** @var Campaign $addedCampaign */
            print "{$addedCampaign->getResourceName()}" . PHP_EOL;
        }
    }

    /**
     * Creates a new campaign budget in the specified client account.
     *
     * @param GoogleAdsClient $googleAdsClient the Google Ads API client
     * @param int $customerId the customer ID
     * @return string the resource name of the newly created budget
     */
    private static function addCampaignBudget(GoogleAdsClient $googleAdsClient, int $customerId)
    {
        // Creates a campaign budget.
        $budget = new CampaignBudget([\
            'name' => 'Interplanetary Cruise Budget #' . Helper::getPrintableDatetime(),\
            'delivery_method' => BudgetDeliveryMethod::STANDARD,\
            'amount_micros' => 500000\
        ]);

        // Creates a campaign budget operation.
        $campaignBudgetOperation = new CampaignBudgetOperation();
        $campaignBudgetOperation->setCreate($budget);

        // Issues a mutate request.
        $campaignBudgetServiceClient = $googleAdsClient->getCampaignBudgetServiceClient();
        $response = $campaignBudgetServiceClient->mutateCampaignBudgets(
            MutateCampaignBudgetsRequest::build($customerId, [$campaignBudgetOperation])
        );

        /** @var CampaignBudget $addedBudget */
        $addedBudget = $response->getResults()[0];
        printf("Added budget named '%s'%s", $addedBudget->getResourceName(), PHP_EOL);

        return $addedBudget->getResourceName();
    }
}

AddCampaigns::main();
AddCampaigns.php


```

```
#!/usr/bin/env python
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This example illustrates how to add a campaign.

To get campaigns, run get_campaigns.py.
"""

import argparse
import datetime
import sys
from typing import List
import uuid

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
from google.ads.googleads.v24.services.services.campaign_budget_service import (
    CampaignBudgetServiceClient,
)
from google.ads.googleads.v24.services.types.campaign_budget_service import (
    CampaignBudgetOperation,
    MutateCampaignBudgetsResponse,
)
from google.ads.googleads.v24.services.services.campaign_service import (
    CampaignServiceClient,
)
from google.ads.googleads.v24.services.types.campaign_service import (
    CampaignOperation,
    MutateCampaignsResponse,
)
from google.ads.googleads.v24.resources.types.campaign_budget import (
    CampaignBudget,
)
from google.ads.googleads.v24.resources.types.campaign import Campaign

_START_DATE_FORMAT: str = "%Y%m%d 00:00:00"
_END_DATE_FORMAT: str = "%Y%m%d 23:59:59"

def main(client: GoogleAdsClient, customer_id: str) -> None:
    campaign_budget_service: CampaignBudgetServiceClient = client.get_service(
        "CampaignBudgetService"
    )
    campaign_service: CampaignServiceClient = client.get_service(
        "CampaignService"
    )

    # Create a budget, which can be shared by multiple campaigns.
    campaign_budget_operation: CampaignBudgetOperation = client.get_type(
        "CampaignBudgetOperation"
    )
    campaign_budget: CampaignBudget = campaign_budget_operation.create
    campaign_budget.name = f"Interplanetary Budget {uuid.uuid4()}"
    campaign_budget.delivery_method = (
        client.enums.BudgetDeliveryMethodEnum.STANDARD
    )
    campaign_budget.amount_micros = 500000

    # Add budget.
    campaign_budget_response: MutateCampaignBudgetsResponse
    try:
        budget_operations: List[CampaignBudgetOperation] = [\
            campaign_budget_operation\
        ]
        campaign_budget_response = (
            campaign_budget_service.mutate_campaign_budgets(
                customer_id=customer_id,
                operations=budget_operations,
            )
        )
    except GoogleAdsException as ex:
        handle_googleads_exception(ex)
        # We are exiting in handle_googleads_exception so this return is not
        # strictly necessary, but it makes static analysis happier.
        return

    # Create campaign.
    campaign_operation: CampaignOperation = client.get_type("CampaignOperation")
    campaign: Campaign = campaign_operation.create
    campaign.name = f"Interplanetary Cruise {uuid.uuid4()}"
    campaign.advertising_channel_type = (
        client.enums.AdvertisingChannelTypeEnum.SEARCH
    )

    # Recommendation: Set the campaign to PAUSED when creating it to prevent
    # the ads from immediately serving. Set to ENABLED once you've added
    # targeting and the ads are ready to serve.
    campaign.status = client.enums.CampaignStatusEnum.PAUSED

    # Set the bidding strategy and budget.
    campaign.manual_cpc = client.get_type("ManualCpc")
    campaign.campaign_budget = campaign_budget_response.results[0].resource_name

    # Set the campaign network options.
    campaign.network_settings.target_google_search = True
    campaign.network_settings.target_search_network = True
    campaign.network_settings.target_partner_search_network = False
    # Enable Display Expansion on Search campaigns. For more details see:
    # https://support.google.com/google-ads/answer/7193800
    campaign.network_settings.target_content_network = True

    # Declare whether or not this campaign serves political ads targeting the
    # EU. Valid values are:
    #   CONTAINS_EU_POLITICAL_ADVERTISING
    #   DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING
    campaign.contains_eu_political_advertising = (
        client.enums.EuPoliticalAdvertisingStatusEnum.DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING
    )

    # Optional: Set the start date.
    start_time: datetime.date = datetime.date.today() + datetime.timedelta(
        days=1
    )
    campaign.start_date_time = datetime.date.strftime(
        start_time, _START_DATE_FORMAT
    )

    # Optional: Set the end date.
    end_time: datetime.date = start_time + datetime.timedelta(weeks=4)
    campaign.end_date_time = datetime.date.strftime(end_time, _END_DATE_FORMAT)

    # Add the campaign.
    campaign_response: MutateCampaignsResponse
    try:
        campaign_operations: List[CampaignOperation] = [campaign_operation]
        campaign_response = campaign_service.mutate_campaigns(
            customer_id=customer_id, operations=campaign_operations
        )
        print(f"Created campaign {campaign_response.results[0].resource_name}.")
    except GoogleAdsException as ex:
        handle_googleads_exception(ex)

def handle_googleads_exception(exception: GoogleAdsException) -> None:
    print(
        f'Request with ID "{exception.request_id}" failed with status '
        f'"{exception.error.code().name}" and includes the following errors:'
    )
    for error in exception.failure.errors:
        print(f'\tError with message "{error.message}".')
        if error.location:
            for field_path_element in error.location.field_path_elements:
                print(f"\t\tOn field: {field_path_element.field_name}")
    sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Adds a campaign for specified customer."
    )
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "-c",
        "--customer_id",
        type=str,
        required=True,
        help="The Google Ads customer ID.",
    )
    args: argparse.Namespace = parser.parse_args()

    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    googleads_client: GoogleAdsClient = GoogleAdsClient.load_from_storage(
        version="v24"
    )

    main(googleads_client, args.customer_id)
add_campaigns.py


```

```
#!/usr/bin/env ruby
# Encoding: utf-8
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This example adds a campaign. To get campaigns, run get_campaigns.rb.

require 'optparse'
require 'google/ads/google_ads'
require 'date'

def add_campaigns(customer_id)
  # GoogleAdsClient will read a config file from
  # ENV['HOME']/google_ads_config.rb when called without parameters
  client = Google::Ads::GoogleAds::GoogleAdsClient.new

  # Create a budget, which can be shared by multiple campaigns.
  campaign_budget = client.resource.campaign_budget do |cb|
    cb.name = "Interplanetary Budget #{(Time.new.to_f * 1000).to_i}"
    cb.delivery_method = :STANDARD
    cb.amount_micros = 500000
  end

  operation = client.operation.create_resource.campaign_budget(campaign_budget)

  # Add budget.
  return_budget = client.service.campaign_budget.mutate_campaign_budgets(
    customer_id: customer_id,
    operations: [operation],
  )

  # Create campaign.
  campaign = client.resource.campaign do |c|
    c.name = "Interplanetary Cruise #{(Time.new.to_f * 1000).to_i}"
    c.advertising_channel_type = :SEARCH

    # Recommendation: Set the campaign to PAUSED when creating it to prevent
    # the ads from immediately serving. Set to ENABLED once you've added
    # targeting and the ads are ready to serve.
    c.status = :PAUSED

    # Set the bidding strategy and budget.
    c.manual_cpc = client.resource.manual_cpc
    c.campaign_budget = return_budget.results.first.resource_name

    # Set the campaign network options.
    c.network_settings = client.resource.network_settings do |ns|
      ns.target_google_search = true
      ns.target_search_network = true
      # Enable Display Expansion on Search campaigns. See
      # https://support.google.com/google-ads/answer/7193800 to learn more.
      ns.target_content_network = true
      ns.target_partner_search_network = false
    end

    # Declare whether or not this campaign serves political ads targeting the EU.
    # Valid values are CONTAINS_EU_POLITICAL_ADVERTISING and
    # DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING.
    c.contains_eu_political_advertising = :DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING

    # Optional: Set the start date.
    c.start_date_time = DateTime.parse((Date.today + 1).to_s).strftime('%Y%m%d %H:%M:%S')

    # Optional: Set the end date.
    c.end_date_time = DateTime.parse((Date.today.next_year).to_s).strftime('%Y%m%d %H:%M:%S')
  end

  # Create the operation.
  campaign_operation = client.operation.create_resource.campaign(campaign)

  # Add the campaign.
  response = client.service.campaign.mutate_campaigns(
    customer_id: customer_id,
    operations: [campaign_operation],
  )

  puts "Created campaign #{response.results.first.resource_name}."
end

if __FILE__ == $0
  options = {}
  # The following parameter(s) should be provided to run the example. You can
  # either specify these by changing the INSERT_XXX_ID_HERE values below, or on
  # the command line.
  #
  # Parameters passed on the command line will override any parameters set in
  # code.
  #
  # Running the example with -h will print the command line usage.
  options[:customer_id] = 'INSERT_CUSTOMER_ID_HERE'

  OptionParser.new do |opts|
    opts.banner = sprintf('Usage: add_campaigns.rb [options]')

    opts.separator ''
    opts.separator 'Options:'

    opts.on('-C', '--customer-id CUSTOMER-ID', String, 'Customer ID') do |v|
      options[:customer_id] = v
    end

    opts.separator ''
    opts.separator 'Help:'

    opts.on_tail('-h', '--help', 'Show this message') do
      puts opts
      exit
    end
  end.parse!

  begin
    add_campaigns(options.fetch(:customer_id).tr("-", ""))
  rescue Google::Ads::GoogleAds::Errors::GoogleAdsError => e
    e.failure.errors.each do |error|
      STDERR.printf("Error with message: %s\n", error.message)
      if error.location
        error.location.field_path_elements.each do |field_path_element|
          STDERR.printf("\tOn field: %s\n", field_path_element.field_name)
        end
      end
      error.error_code.to_h.each do |k, v|
        next if v == :UNSPECIFIED
        STDERR.printf("\tType: %s\n\tCode: %s\n", k, v)
      end
    end
    raise
  end
end
add_campaigns.rb


```

```
#!/usr/bin/perl -w
#
# Copyright 2019, Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This example adds a campaign. To get campaigns, run get_campaigns.pl.

use strict;
use warnings;
use utf8;

use FindBin qw($Bin);
use lib "$Bin/../../lib";
use Google::Ads::GoogleAds::Client;
use Google::Ads::GoogleAds::Utils::GoogleAdsHelper;
use Google::Ads::GoogleAds::V24::Resources::CampaignBudget;
use Google::Ads::GoogleAds::V24::Resources::Campaign;
use Google::Ads::GoogleAds::V24::Resources::NetworkSettings;
use Google::Ads::GoogleAds::V24::Common::ManualCpc;
use Google::Ads::GoogleAds::V24::Enums::BudgetDeliveryMethodEnum   qw(STANDARD);
use Google::Ads::GoogleAds::V24::Enums::AdvertisingChannelTypeEnum qw(SEARCH);
use Google::Ads::GoogleAds::V24::Enums::CampaignStatusEnum         qw(PAUSED);
use Google::Ads::GoogleAds::V24::Enums::EuPoliticalAdvertisingStatusEnum
  qw(DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING);
use
  Google::Ads::GoogleAds::V24::Services::CampaignBudgetService::CampaignBudgetOperation;
use Google::Ads::GoogleAds::V24::Services::CampaignService::CampaignOperation;

use Getopt::Long qw(:config auto_help);
use Pod::Usage;
use Cwd          qw(abs_path);
use Data::Uniqid qw(uniqid);
use POSIX        qw(strftime);

# The following parameter(s) should be provided to run the example. You can
# either specify these by changing the INSERT_XXX_ID_HERE values below, or on
# the command line.
#
# Parameters passed on the command line will override any parameters set in
# code.
#
# Running the example with -h will print the command line usage.
my $customer_id = "INSERT_CUSTOMER_ID_HERE";

sub add_campaigns {
  my ($api_client, $customer_id) = @_;

  # Create a campaign budget, which can be shared by multiple campaigns.
  my $campaign_budget =
    Google::Ads::GoogleAds::V24::Resources::CampaignBudget->new({
      name           => "Interplanetary budget #" . uniqid(),
      deliveryMethod => STANDARD,
      amountMicros   => 500000
    });

  # Create a campaign budget operation.
  my $campaign_budget_operation =
    Google::Ads::GoogleAds::V24::Services::CampaignBudgetService::CampaignBudgetOperation
    ->new({create => $campaign_budget});

  # Add the campaign budget.
  my $campaign_budgets_response = $api_client->CampaignBudgetService()->mutate({
      customerId => $customer_id,
      operations => [$campaign_budget_operation]});

  # Create a campaign.
  my $campaign = Google::Ads::GoogleAds::V24::Resources::Campaign->new({
      name                   => "Interplanetary Cruise #" . uniqid(),
      advertisingChannelType => SEARCH,
      # Recommendation: Set the campaign to PAUSED when creating it to stop
      # the ads from immediately serving. Set to ENABLED once you've added
      # targeting and the ads are ready to serve.
      status => PAUSED,
      # Set the bidding strategy and budget.
      manualCpc      => Google::Ads::GoogleAds::V24::Common::ManualCpc->new(),
      campaignBudget => $campaign_budgets_response->{results}[0]{resourceName},
      # Set the campaign network options.
      networkSettings =>
        Google::Ads::GoogleAds::V24::Resources::NetworkSettings->new({
          targetGoogleSearch  => "true",
          targetSearchNetwork => "true",
          # Enable Display Expansion on Search campaigns. See
          # https://support.google.com/google-ads/answer/7193800 to learn more.
          targetContentNetwork       => "true",
          targetPartnerSearchNetwork => "false"
        }
        ),
      # Declare whether or not this campaign serves political ads targeting the EU.
      # Valid values are CONTAINS_EU_POLITICAL_ADVERTISING and
      # DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING.
      containsEuPoliticalAdvertising =>
        DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING,
      # Optional: Set the start datetime. The campaign starts tomorrow.
      startDateTime =>
        strftime("%Y%m%d 00:00:00", localtime(time + 60 * 60 * 24)),
      # Optional: Set the end datetime. The campaign runs for 30 days.
      endDateTime =>
        strftime("%Y%m%d 23:59:59", localtime(time + 60 * 60 * 24 * 30)),
    });

  # Create a campaign operation.
  my $campaign_operation =
    Google::Ads::GoogleAds::V24::Services::CampaignService::CampaignOperation->
    new({create => $campaign});

  # Add the campaign.
  my $campaigns_response = $api_client->CampaignService()->mutate({
      customerId => $customer_id,
      operations => [$campaign_operation]});

  printf "Created campaign '%s'.\n",
    $campaigns_response->{results}[0]{resourceName};

  return 1;
}

# Don't run the example if the file is being included.
if (abs_path($0) ne abs_path(__FILE__)) {
  return 1;
}

# Get Google Ads Client, credentials will be read from ~/googleads.properties.
my $api_client = Google::Ads::GoogleAds::Client->new();

# By default examples are set to die on any server returned fault.
$api_client->set_die_on_faults(1);

# Parameters passed on the command line will override any parameters set in code.
GetOptions("customer_id=s" => \$customer_id);

# Print the help message if the parameters are not initialized in the code nor
# in the command line.
pod2usage(2) if not check_params($customer_id);

# Call the example.
add_campaigns($api_client, $customer_id =~ s/-//gr);

=pod

=head1 NAME

add_campaigns

=head1 DESCRIPTION

This example adds a campaign. To get campaigns, run get_campaigns.pl.

=head1 SYNOPSIS

add_campaigns.pl [options]

    -help                       Show the help message.
    -customer_id                The Google Ads customer ID.

=cut
add_campaigns.pl


```

```
#!/bin/bash
# Copyright 2025 Google LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Creates a campaign budget.
#
# Variables:
#   API_VERSION,
#   CUSTOMER_ID,
#   DEVELOPER_TOKEN,
#   MANAGER_CUSTOMER_ID,
#   OAUTH2_ACCESS_TOKEN:
#     See https://developers.google.com/google-ads/api/rest/auth#request_headers
#     for details.
curl -f --request POST \
  "https://googleads.googleapis.com/v${API_VERSION}/customers/${CUSTOMER_ID}/campaignBudgets:mutate" \
  --header "Content-Type: application/json" \
  --header "Developer-Token: ${DEVELOPER_TOKEN}" \
  --header "login-customer-id: ${MANAGER_CUSTOMER_ID}" \
  --header "Authorization: Bearer ${OAUTH2_ACCESS_TOKEN}" \
  --data @- <<EOF
{
  "operations": [\
    {\
      "create": {\
        "name":"Interplanetary Cruise Budget #${RANDOM}",\
        "deliveryMethod":"STANDARD",\
        "amountMicros":500000\
      }\
    }\
  ]
}
EOF

# Creates a campaign.
#
# Variables:
#   API_VERSION,
#   CUSTOMER_ID,
#   DEVELOPER_TOKEN,
#   MANAGER_CUSTOMER_ID,
#   OAUTH2_ACCESS_TOKEN:
#     See https://developers.google.com/google-ads/api/rest/auth#request_headers
#     for details.
#   CAMPAIGN_BUDGET_RESOURCE_NAME:
#     The resource of the campaign budget as returned by the previous step.

curl -f --request POST \
  "https://googleads.googleapis.com/v${API_VERSION}/customers/${CUSTOMER_ID}/campaigns:mutate" \
  --header "Content-Type: application/json" \
  --header "Developer-Token: ${DEVELOPER_TOKEN}" \
  --header "login-customer-id: ${MANAGER_CUSTOMER_ID}" \
  --header "Authorization: Bearer ${OAUTH2_ACCESS_TOKEN}" \
  --data @- <<EOF
{
  "operations": [\
    {\
      "create": {\
        "campaignBudget": "${CAMPAIGN_BUDGET_RESOURCE_NAME}",\
        "name": "Interplanetary Cruise Campaign #${RANDOM}",\
        "advertisingChannelType": "SEARCH",\
        "status": "PAUSED",\
        "manualCpc": {},\
        "networkSettings": {\
          "targetGoogleSearch":true,\
          "targetSearchNetwork":true,\
          "targetContentNetwork":true,\
          "targetPartnerSearchNetwork":false\
        }\
      }\
    }\
  ]
}
EOF
add_campaigns.sh


```

## Campaign groups

You can use the [`CampaignGroupService`](https://developers.google.com/google-ads/api/reference/rpc/v24/CampaignGroupService) to
create [campaign groups](https://support.google.com/google-ads/answer/6393407) for
tracking the overall performance of multiple campaigns with similar goals.

The first step is to create a campaign group. Next, add the campaigns you want
to track to this campaign group. You can pick any combinations of Search,
Shopping, Display, or Video campaigns, subject to the following restrictions:

- Each campaign can only belong to one campaign group at a time.
- You can't add campaigns with shared budgets to a campaign group.

[Previous\\
\\
arrow\_back\\
\\
Overview](https://developers.google.com/google-ads/api/docs/campaigns/overview)

[Next\\
\\
Create ad groups\\
\\
arrow\_forward](https://developers.google.com/google-ads/api/docs/campaigns/create-ad-groups)

Was this helpful?



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-05-13 UTC."\],\[\],\[\]\]