# SwaggerClient-php
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This PHP package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v6
- Build package: io.swagger.codegen.languages.PhpClientCodegen

## Requirements

PHP 5.5 and later

## Installation & Usage
### Composer

To install the bindings via [Composer](http://getcomposer.org/), add the following to `composer.json`:

```
{
  "repositories": [
    {
      "type": "git",
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
    require_once('/path/to/SwaggerClient-php/vendor/autoload.php');
```

## Tests

To run the unit tests:

```
composer install
./vendor/bin/phpunit
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\AppointmentApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request = new \Swagger\Client\Model\AddAppointmentRequest(); // \Swagger\Client\Model\AddAppointmentRequest | 
$site_id = "site_id_example"; // string | ID of the site from which to pull data.
$version = "version_example"; // string | 
$authorization = ""; // string | A staff user authorization token.

try {
    $result = $apiInstance->appointmentAddApppointment($request, $site_id, $version, $authorization);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AppointmentApi->appointmentAddApppointment: ', $e->getMessage(), PHP_EOL;
}

?>
```

## Documentation for API Endpoints

All URIs are relative to *https://api.mindbodyonline.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppointmentApi* | [**appointmentAddApppointment**](docs/Api/AppointmentApi.md#appointmentaddapppointment) | **POST** /public/v{version}/appointment/addappointment | Book a new appointment.
*AppointmentApi* | [**appointmentGetActiveSessionTimes**](docs/Api/AppointmentApi.md#appointmentgetactivesessiontimes) | **GET** /public/v{version}/appointment/activesessiontimes | Get active session times.
*AppointmentApi* | [**appointmentGetAppointmentOptions**](docs/Api/AppointmentApi.md#appointmentgetappointmentoptions) | **GET** /public/v{version}/appointment/appointmentoptions | Get appointment-related settings.
*AppointmentApi* | [**appointmentGetBookableItems**](docs/Api/AppointmentApi.md#appointmentgetbookableitems) | **GET** /public/v{version}/appointment/bookableitems | Get staff appointment availability.
*AppointmentApi* | [**appointmentGetScheduleItems**](docs/Api/AppointmentApi.md#appointmentgetscheduleitems) | **GET** /public/v{version}/appointment/scheduleitems | Get appointment schedule.
*AppointmentApi* | [**appointmentGetStaffAppointments**](docs/Api/AppointmentApi.md#appointmentgetstaffappointments) | **GET** /public/v{version}/appointment/staffappointments | Get appointments grouped by staff member.
*AppointmentApi* | [**appointmentUpdateApppointment**](docs/Api/AppointmentApi.md#appointmentupdateapppointment) | **POST** /public/v{version}/appointment/updateappointment | Update an existing appointment.
*ClassApi* | [**classAddClientToClass**](docs/Api/ClassApi.md#classaddclienttoclass) | **POST** /public/v{version}/class/addclienttoclass | Book a client into a class.
*ClassApi* | [**classGetClassDescriptions**](docs/Api/ClassApi.md#classgetclassdescriptions) | **GET** /public/v{version}/class/classdescriptions | Get class descriptions.
*ClassApi* | [**classGetClassSchedules**](docs/Api/ClassApi.md#classgetclassschedules) | **GET** /public/v{version}/class/classschedules | Get class schedules.
*ClassApi* | [**classGetClassVisits**](docs/Api/ClassApi.md#classgetclassvisits) | **GET** /public/v{version}/class/classvisits | Get information about clients booked in a class.
*ClassApi* | [**classGetClasses**](docs/Api/ClassApi.md#classgetclasses) | **GET** /public/v{version}/class/classes | Get scheduled classes.
*ClassApi* | [**classGetWaitlistEntries**](docs/Api/ClassApi.md#classgetwaitlistentries) | **GET** /public/v{version}/class/waitlistentries | Get waiting list entries.
*ClassApi* | [**classRemoveClientFromClass**](docs/Api/ClassApi.md#classremoveclientfromclass) | **POST** /public/v{version}/class/removeclientfromclass | Remove a client from a class.
*ClassApi* | [**classRemoveFromWaitlist**](docs/Api/ClassApi.md#classremovefromwaitlist) | **POST** /public/v{version}/class/removefromwaitlist | Remove a client from a waiting list.
*ClassApi* | [**classSubstituteClassTeacher**](docs/Api/ClassApi.md#classsubstituteclassteacher) | **POST** /public/v{version}/class/substituteclassteacher | Substitute a class teacher.
*ClientApi* | [**clientAddArrival**](docs/Api/ClientApi.md#clientaddarrival) | **POST** /public/v{version}/client/addarrival | Add an arrival for a client.
*ClientApi* | [**clientAddClient**](docs/Api/ClientApi.md#clientaddclient) | **POST** /public/v{version}/client/addclient | Add a client to a site.
*ClientApi* | [**clientAddContactLog**](docs/Api/ClientApi.md#clientaddcontactlog) | **POST** /public/v{version}/client/addcontactlog | Add a contact log to a client&#39;s account.
*ClientApi* | [**clientGetActiveClientMemberships**](docs/Api/ClientApi.md#clientgetactiveclientmemberships) | **GET** /public/v{version}/client/activeclientmemberships | Get a client&#39;s active memberships.
*ClientApi* | [**clientGetClientAccountBalances**](docs/Api/ClientApi.md#clientgetclientaccountbalances) | **GET** /public/v{version}/client/clientaccountbalances | Get account balance information for one or more client(s).
*ClientApi* | [**clientGetClientContracts**](docs/Api/ClientApi.md#clientgetclientcontracts) | **GET** /public/v{version}/client/clientcontracts | Get contracts that a client has purchased.
*ClientApi* | [**clientGetClientFormulaNotes**](docs/Api/ClientApi.md#clientgetclientformulanotes) | **GET** /public/v{version}/client/clientformulanotes | Get a client&#39;s formula notes.
*ClientApi* | [**clientGetClientIndexes**](docs/Api/ClientApi.md#clientgetclientindexes) | **GET** /public/v{version}/client/clientindexes | Get a site&#39;s configured client indexes and client index values.
*ClientApi* | [**clientGetClientPurchases**](docs/Api/ClientApi.md#clientgetclientpurchases) | **GET** /public/v{version}/client/clientpurchases | Get a client&#39;s purchase history.
*ClientApi* | [**clientGetClientReferralTypes**](docs/Api/ClientApi.md#clientgetclientreferraltypes) | **GET** /public/v{version}/client/clientreferraltypes | Get a site&#39;s configured client referral types.
*ClientApi* | [**clientGetClientServices**](docs/Api/ClientApi.md#clientgetclientservices) | **GET** /public/v{version}/client/clientservices | Get pricing options that a client has purchased.
*ClientApi* | [**clientGetClientVisits**](docs/Api/ClientApi.md#clientgetclientvisits) | **GET** /public/v{version}/client/clientvisits | Get a client&#39;s visit history.
*ClientApi* | [**clientGetClients**](docs/Api/ClientApi.md#clientgetclients) | **GET** /public/v{version}/client/clients | Get clients.
*ClientApi* | [**clientGetContactLogs**](docs/Api/ClientApi.md#clientgetcontactlogs) | **GET** /public/v{version}/client/contactlogs | Get contact logs on a client&#39;s account.
*ClientApi* | [**clientGetCrossRegionalClientAssociations**](docs/Api/ClientApi.md#clientgetcrossregionalclientassociations) | **GET** /public/v{version}/client/crossregionalclientassociations | Get a client&#39;s cross regional site associations.
*ClientApi* | [**clientGetCustomClientFields**](docs/Api/ClientApi.md#clientgetcustomclientfields) | **GET** /public/v{version}/client/customclientfields | Get a site&#39;s configured custom client fields.
*ClientApi* | [**clientGetRequiredClientFields**](docs/Api/ClientApi.md#clientgetrequiredclientfields) | **GET** /public/v{version}/client/requiredclientfields | Get client required fields for a site.
*ClientApi* | [**clientSendPasswordResetEmail**](docs/Api/ClientApi.md#clientsendpasswordresetemail) | **POST** /public/v{version}/client/sendpasswordresetemail | Send a password reset email to a client.
*ClientApi* | [**clientUpdateClient**](docs/Api/ClientApi.md#clientupdateclient) | **POST** /public/v{version}/client/updateclient | Update a client at a site.
*ClientApi* | [**clientUpdateClientService**](docs/Api/ClientApi.md#clientupdateclientservice) | **POST** /public/v{version}/client/updateclientservice | Update a client&#39;s purchase pricing option.
*ClientApi* | [**clientUpdateClientVisit**](docs/Api/ClientApi.md#clientupdateclientvisit) | **POST** /public/v{version}/client/updateclientvisit | Update a client&#39;s visit.
*ClientApi* | [**clientUpdateContactLog**](docs/Api/ClientApi.md#clientupdatecontactlog) | **POST** /public/v{version}/client/updatecontactlog | Update a contact log on a client&#39;s account.
*ClientApi* | [**clientUploadClientDocument**](docs/Api/ClientApi.md#clientuploadclientdocument) | **POST** /public/v{version}/client/uploadclientdocument | Upload a document to a client&#39;s profile.
*ClientApi* | [**clientUploadClientPhoto**](docs/Api/ClientApi.md#clientuploadclientphoto) | **POST** /public/v{version}/client/uploadclientphoto | Upload a profile photo to a client&#39;s profile.
*EnrollmentApi* | [**enrollmentAddClientToEnrollment**](docs/Api/EnrollmentApi.md#enrollmentaddclienttoenrollment) | **POST** /public/v{version}/enrollment/addclienttoenrollment | Book a client into an enrollment.
*EnrollmentApi* | [**enrollmentGetEnrollments**](docs/Api/EnrollmentApi.md#enrollmentgetenrollments) | **GET** /public/v{version}/enrollment/enrollments | Get enrollments scheduled at a site.
*PayrollApi* | [**payrollGetClassPayroll**](docs/Api/PayrollApi.md#payrollgetclasspayroll) | **GET** /public/v{version}/payroll/classes | Get class payroll for staff members.
*PayrollApi* | [**payrollGetTimeClock**](docs/Api/PayrollApi.md#payrollgettimeclock) | **GET** /public/v{version}/payroll/timeclock | Get time card payroll for staff members.
*SaleApi* | [**saleCheckoutShoppingCart**](docs/Api/SaleApi.md#salecheckoutshoppingcart) | **POST** /public/v{version}/sale/checkoutshoppingcart | Purchase pricing options, packages, retail products, or tips for a client.
*SaleApi* | [**saleGetAcceptedCardTypes**](docs/Api/SaleApi.md#salegetacceptedcardtypes) | **GET** /public/v{version}/sale/acceptedcardtypes | Get credit cards types that a site accepts.
*SaleApi* | [**saleGetContracts**](docs/Api/SaleApi.md#salegetcontracts) | **GET** /public/v{version}/sale/contracts | Get contracts available for purchase at a site.
*SaleApi* | [**saleGetCustomPaymentMethods**](docs/Api/SaleApi.md#salegetcustompaymentmethods) | **GET** /public/v{version}/sale/custompaymentmethods | Get payment methods that can be used to pay for sales at a site.
*SaleApi* | [**saleGetGiftCards**](docs/Api/SaleApi.md#salegetgiftcards) | **GET** /public/v{version}/sale/giftcards | Get gift cards available for purchase at a site.
*SaleApi* | [**saleGetPackages**](docs/Api/SaleApi.md#salegetpackages) | **GET** /public/v{version}/sale/packages | Get packages available for purchase at a site.
*SaleApi* | [**saleGetProducts**](docs/Api/SaleApi.md#salegetproducts) | **GET** /public/v{version}/sale/products | Get retail products available for purchase at a site.
*SaleApi* | [**saleGetSales**](docs/Api/SaleApi.md#salegetsales) | **GET** /public/v{version}/sale/sales | Get sales completed at a site.
*SaleApi* | [**saleGetServices**](docs/Api/SaleApi.md#salegetservices) | **GET** /public/v{version}/sale/services | Get pricing options available for purchase at a site
*SaleApi* | [**salePurchaseContract**](docs/Api/SaleApi.md#salepurchasecontract) | **POST** /public/v{version}/sale/purchasecontract | Purchase a contract for a client.
*SaleApi* | [**salePurchaseGiftCard**](docs/Api/SaleApi.md#salepurchasegiftcard) | **POST** /public/v{version}/sale/purchasegiftcard | Purchase a gift card for a client.
*SiteApi* | [**siteGetActivationCode**](docs/Api/SiteApi.md#sitegetactivationcode) | **GET** /public/v{version}/site/activationcode | Get an activation code for a site.
*SiteApi* | [**siteGetLocations**](docs/Api/SiteApi.md#sitegetlocations) | **GET** /public/v{version}/site/locations | Get locations for a site.
*SiteApi* | [**siteGetPrograms**](docs/Api/SiteApi.md#sitegetprograms) | **GET** /public/v{version}/site/programs | Get service categories offered at a site.
*SiteApi* | [**siteGetResources**](docs/Api/SiteApi.md#sitegetresources) | **GET** /public/v{version}/site/resources | Get resources used at a site.
*SiteApi* | [**siteGetSessionTypes**](docs/Api/SiteApi.md#sitegetsessiontypes) | **GET** /public/v{version}/site/sessiontypes | Get the session types used at a site.
*SiteApi* | [**siteGetSites**](docs/Api/SiteApi.md#sitegetsites) | **GET** /public/v{version}/site/sites | Get all sites that can be accessed by an API Key.
*StaffApi* | [**staffGetStaff**](docs/Api/StaffApi.md#staffgetstaff) | **GET** /public/v{version}/staff/staff | Get staff members at a site.
*StaffApi* | [**staffGetStaffPermissions**](docs/Api/StaffApi.md#staffgetstaffpermissions) | **GET** /public/v{version}/staff/staffpermissions | Get configured staff permissions for a staff member.
*UserTokenApi* | [**userTokenIssue**](docs/Api/UserTokenApi.md#usertokenissue) | **POST** /public/v{version}/usertoken/issue | Get a staff user token.
*UserTokenApi* | [**userTokenRevoke**](docs/Api/UserTokenApi.md#usertokenrevoke) | **DELETE** /public/v{version}/usertoken/revoke | Revoke a user token.


## Documentation For Models

 - [AddAppointmentRequest](docs/Model/AddAppointmentRequest.md)
 - [AddAppointmentResponse](docs/Model/AddAppointmentResponse.md)
 - [AddArrivalRequest](docs/Model/AddArrivalRequest.md)
 - [AddArrivalResponse](docs/Model/AddArrivalResponse.md)
 - [AddClientRequest](docs/Model/AddClientRequest.md)
 - [AddClientResponse](docs/Model/AddClientResponse.md)
 - [AddClientToClassRequest](docs/Model/AddClientToClassRequest.md)
 - [AddClientToClassResponse](docs/Model/AddClientToClassResponse.md)
 - [AddClientToClassVisit](docs/Model/AddClientToClassVisit.md)
 - [AddClientToEnrollmentRequest](docs/Model/AddClientToEnrollmentRequest.md)
 - [AddContactLogRequest](docs/Model/AddContactLogRequest.md)
 - [AddContactLogType](docs/Model/AddContactLogType.md)
 - [Amenity](docs/Model/Amenity.md)
 - [Appointment](docs/Model/Appointment.md)
 - [AppointmentOption](docs/Model/AppointmentOption.md)
 - [AssignedClientIndex](docs/Model/AssignedClientIndex.md)
 - [AutopaySchedule](docs/Model/AutopaySchedule.md)
 - [Availability](docs/Model/Availability.md)
 - [BookingWindow](docs/Model/BookingWindow.md)
 - [CheckoutAppointmentBookingRequest](docs/Model/CheckoutAppointmentBookingRequest.md)
 - [CheckoutItem](docs/Model/CheckoutItem.md)
 - [CheckoutItemWrapper](docs/Model/CheckoutItemWrapper.md)
 - [CheckoutPaymentInfo](docs/Model/CheckoutPaymentInfo.md)
 - [CheckoutShoppingCartRequest](docs/Model/CheckoutShoppingCartRequest.md)
 - [ClassDescription](docs/Model/ClassDescription.md)
 - [ClassPayrollEvent](docs/Model/ClassPayrollEvent.md)
 - [ClassSchedule](docs/Model/ClassSchedule.md)
 - [Client](docs/Model/Client.md)
 - [ClientContract](docs/Model/ClientContract.md)
 - [ClientCreditCard](docs/Model/ClientCreditCard.md)
 - [ClientDocument](docs/Model/ClientDocument.md)
 - [ClientIndex](docs/Model/ClientIndex.md)
 - [ClientIndexValue](docs/Model/ClientIndexValue.md)
 - [ClientMembership](docs/Model/ClientMembership.md)
 - [ClientPurchaseRecord](docs/Model/ClientPurchaseRecord.md)
 - [ClientRelationship](docs/Model/ClientRelationship.md)
 - [ClientService](docs/Model/ClientService.md)
 - [Color](docs/Model/Color.md)
 - [ContactLog](docs/Model/ContactLog.md)
 - [ContactLogComment](docs/Model/ContactLogComment.md)
 - [ContactLogSubType](docs/Model/ContactLogSubType.md)
 - [ContactLogType](docs/Model/ContactLogType.md)
 - [Contract](docs/Model/Contract.md)
 - [ContractItem](docs/Model/ContractItem.md)
 - [Course](docs/Model/Course.md)
 - [CreditCardInfo](docs/Model/CreditCardInfo.md)
 - [CrossRegionalClientAssociation](docs/Model/CrossRegionalClientAssociation.md)
 - [CustomClientField](docs/Model/CustomClientField.md)
 - [CustomClientFieldValue](docs/Model/CustomClientFieldValue.md)
 - [CustomPaymentMethod](docs/Model/CustomPaymentMethod.md)
 - [FormulaNote](docs/Model/FormulaNote.md)
 - [GetActivationCodeResponse](docs/Model/GetActivationCodeResponse.md)
 - [GetActiveClientMembershipsRequest](docs/Model/GetActiveClientMembershipsRequest.md)
 - [GetActiveClientMembershipsResponse](docs/Model/GetActiveClientMembershipsResponse.md)
 - [GetActiveSessionTimesRequest](docs/Model/GetActiveSessionTimesRequest.md)
 - [GetActiveSessionTimesResponse](docs/Model/GetActiveSessionTimesResponse.md)
 - [GetAppointmentOptionsResponse](docs/Model/GetAppointmentOptionsResponse.md)
 - [GetBookableItemsRequest](docs/Model/GetBookableItemsRequest.md)
 - [GetBookableItemsResponse](docs/Model/GetBookableItemsResponse.md)
 - [GetClassDescriptionsRequest](docs/Model/GetClassDescriptionsRequest.md)
 - [GetClassDescriptionsResponse](docs/Model/GetClassDescriptionsResponse.md)
 - [GetClassPayrollRequest](docs/Model/GetClassPayrollRequest.md)
 - [GetClassPayrollResponse](docs/Model/GetClassPayrollResponse.md)
 - [GetClassSchedulesRequest](docs/Model/GetClassSchedulesRequest.md)
 - [GetClassSchedulesResponse](docs/Model/GetClassSchedulesResponse.md)
 - [GetClassVisitsRequest](docs/Model/GetClassVisitsRequest.md)
 - [GetClassVisitsResponse](docs/Model/GetClassVisitsResponse.md)
 - [GetClassesRequest](docs/Model/GetClassesRequest.md)
 - [GetClassesResponse](docs/Model/GetClassesResponse.md)
 - [GetClientAccountBalancesRequest](docs/Model/GetClientAccountBalancesRequest.md)
 - [GetClientAccountBalancesResponse](docs/Model/GetClientAccountBalancesResponse.md)
 - [GetClientContractsRequest](docs/Model/GetClientContractsRequest.md)
 - [GetClientContractsResponse](docs/Model/GetClientContractsResponse.md)
 - [GetClientFormulaNotesRequest](docs/Model/GetClientFormulaNotesRequest.md)
 - [GetClientFormulaNotesResponse](docs/Model/GetClientFormulaNotesResponse.md)
 - [GetClientIndexesRequest](docs/Model/GetClientIndexesRequest.md)
 - [GetClientIndexesResponse](docs/Model/GetClientIndexesResponse.md)
 - [GetClientPurchasesRequest](docs/Model/GetClientPurchasesRequest.md)
 - [GetClientPurchasesResponse](docs/Model/GetClientPurchasesResponse.md)
 - [GetClientReferralTypesRequest](docs/Model/GetClientReferralTypesRequest.md)
 - [GetClientReferralTypesResponse](docs/Model/GetClientReferralTypesResponse.md)
 - [GetClientServicesRequest](docs/Model/GetClientServicesRequest.md)
 - [GetClientServicesResponse](docs/Model/GetClientServicesResponse.md)
 - [GetClientVisitsRequest](docs/Model/GetClientVisitsRequest.md)
 - [GetClientVisitsResponse](docs/Model/GetClientVisitsResponse.md)
 - [GetClientsRequest](docs/Model/GetClientsRequest.md)
 - [GetClientsResponse](docs/Model/GetClientsResponse.md)
 - [GetContactLogsRequest](docs/Model/GetContactLogsRequest.md)
 - [GetContactLogsResponse](docs/Model/GetContactLogsResponse.md)
 - [GetContractsRequest](docs/Model/GetContractsRequest.md)
 - [GetContractsResponse](docs/Model/GetContractsResponse.md)
 - [GetCrossRegionalClientAssociationsRequest](docs/Model/GetCrossRegionalClientAssociationsRequest.md)
 - [GetCrossRegionalClientAssociationsResponse](docs/Model/GetCrossRegionalClientAssociationsResponse.md)
 - [GetCustomClientFieldsRequest](docs/Model/GetCustomClientFieldsRequest.md)
 - [GetCustomClientFieldsResponse](docs/Model/GetCustomClientFieldsResponse.md)
 - [GetCustomPaymentMethodsRequest](docs/Model/GetCustomPaymentMethodsRequest.md)
 - [GetCustomPaymentMethodsResponse](docs/Model/GetCustomPaymentMethodsResponse.md)
 - [GetEnrollmentsRequest](docs/Model/GetEnrollmentsRequest.md)
 - [GetEnrollmentsResponse](docs/Model/GetEnrollmentsResponse.md)
 - [GetGiftCardResponse](docs/Model/GetGiftCardResponse.md)
 - [GetGiftCardsRequest](docs/Model/GetGiftCardsRequest.md)
 - [GetLocationsRequest](docs/Model/GetLocationsRequest.md)
 - [GetLocationsResponse](docs/Model/GetLocationsResponse.md)
 - [GetPackagesRequest](docs/Model/GetPackagesRequest.md)
 - [GetPackagesResponse](docs/Model/GetPackagesResponse.md)
 - [GetProductsRequest](docs/Model/GetProductsRequest.md)
 - [GetProductsResponse](docs/Model/GetProductsResponse.md)
 - [GetProgramsRequest](docs/Model/GetProgramsRequest.md)
 - [GetProgramsResponse](docs/Model/GetProgramsResponse.md)
 - [GetRequiredClientFieldsResponse](docs/Model/GetRequiredClientFieldsResponse.md)
 - [GetResourcesRequest](docs/Model/GetResourcesRequest.md)
 - [GetResourcesResponse](docs/Model/GetResourcesResponse.md)
 - [GetSalesRequest](docs/Model/GetSalesRequest.md)
 - [GetSalesResponse](docs/Model/GetSalesResponse.md)
 - [GetScheduleItemsRequest](docs/Model/GetScheduleItemsRequest.md)
 - [GetScheduleItemsResponse](docs/Model/GetScheduleItemsResponse.md)
 - [GetServicesRequest](docs/Model/GetServicesRequest.md)
 - [GetServicesResponse](docs/Model/GetServicesResponse.md)
 - [GetSessionTypesRequest](docs/Model/GetSessionTypesRequest.md)
 - [GetSessionTypesResponse](docs/Model/GetSessionTypesResponse.md)
 - [GetSitesRequest](docs/Model/GetSitesRequest.md)
 - [GetSitesResponse](docs/Model/GetSitesResponse.md)
 - [GetStaffAppointmentsRequest](docs/Model/GetStaffAppointmentsRequest.md)
 - [GetStaffAppointmentsResponse](docs/Model/GetStaffAppointmentsResponse.md)
 - [GetStaffPermissionsRequest](docs/Model/GetStaffPermissionsRequest.md)
 - [GetStaffPermissionsResponse](docs/Model/GetStaffPermissionsResponse.md)
 - [GetStaffRequest](docs/Model/GetStaffRequest.md)
 - [GetStaffResponse](docs/Model/GetStaffResponse.md)
 - [GetTimeClockRequest](docs/Model/GetTimeClockRequest.md)
 - [GetTimeClockResponse](docs/Model/GetTimeClockResponse.md)
 - [GetWaitlistEntriesRequest](docs/Model/GetWaitlistEntriesRequest.md)
 - [GetWaitlistEntriesResponse](docs/Model/GetWaitlistEntriesResponse.md)
 - [GiftCard](docs/Model/GiftCard.md)
 - [GiftCardLayout](docs/Model/GiftCardLayout.md)
 - [IssueRequest](docs/Model/IssueRequest.md)
 - [IssueResponse](docs/Model/IssueResponse.md)
 - [Level](docs/Model/Level.md)
 - [Liability](docs/Model/Liability.md)
 - [Location](docs/Model/Location.md)
 - [MembershipTypeRestriction](docs/Model/MembershipTypeRestriction.md)
 - [ModelClass](docs/Model/ModelClass.md)
 - [Package](docs/Model/Package.md)
 - [PaginationResponse](docs/Model/PaginationResponse.md)
 - [Product](docs/Model/Product.md)
 - [Program](docs/Model/Program.md)
 - [ProspectStage](docs/Model/ProspectStage.md)
 - [PurchaseContractRequest](docs/Model/PurchaseContractRequest.md)
 - [PurchaseContractResponse](docs/Model/PurchaseContractResponse.md)
 - [PurchaseGiftCardRequest](docs/Model/PurchaseGiftCardRequest.md)
 - [PurchaseGiftCardResponse](docs/Model/PurchaseGiftCardResponse.md)
 - [PurchasedItem](docs/Model/PurchasedItem.md)
 - [Relationship](docs/Model/Relationship.md)
 - [RemoveClientFromClassRequest](docs/Model/RemoveClientFromClassRequest.md)
 - [RemoveClientFromClassResponse](docs/Model/RemoveClientFromClassResponse.md)
 - [RemoveFromWaitlistRequest](docs/Model/RemoveFromWaitlistRequest.md)
 - [RemoveFromWaitlistResponse](docs/Model/RemoveFromWaitlistResponse.md)
 - [Resource](docs/Model/Resource.md)
 - [Sale](docs/Model/Sale.md)
 - [SalePayment](docs/Model/SalePayment.md)
 - [SalesRep](docs/Model/SalesRep.md)
 - [SendPasswordResetEmailRequest](docs/Model/SendPasswordResetEmailRequest.md)
 - [Service](docs/Model/Service.md)
 - [SessionType](docs/Model/SessionType.md)
 - [Site](docs/Model/Site.md)
 - [Size](docs/Model/Size.md)
 - [Staff](docs/Model/Staff.md)
 - [StaffPermissionGroup](docs/Model/StaffPermissionGroup.md)
 - [StoredCardInfo](docs/Model/StoredCardInfo.md)
 - [SubstituteClassTeacherRequest](docs/Model/SubstituteClassTeacherRequest.md)
 - [SubstituteClassTeacherResponse](docs/Model/SubstituteClassTeacherResponse.md)
 - [SubstituteTeacherClass](docs/Model/SubstituteTeacherClass.md)
 - [TimeCardEvent](docs/Model/TimeCardEvent.md)
 - [TimeClockReport](docs/Model/TimeClockReport.md)
 - [Unavailability](docs/Model/Unavailability.md)
 - [UpcomingAutopayEvent](docs/Model/UpcomingAutopayEvent.md)
 - [UpdateAppointmentRequest](docs/Model/UpdateAppointmentRequest.md)
 - [UpdateAppointmentResponse](docs/Model/UpdateAppointmentResponse.md)
 - [UpdateClientRequest](docs/Model/UpdateClientRequest.md)
 - [UpdateClientResponse](docs/Model/UpdateClientResponse.md)
 - [UpdateClientServiceRequest](docs/Model/UpdateClientServiceRequest.md)
 - [UpdateClientServiceResponse](docs/Model/UpdateClientServiceResponse.md)
 - [UpdateClientVisitRequest](docs/Model/UpdateClientVisitRequest.md)
 - [UpdateClientVisitResponse](docs/Model/UpdateClientVisitResponse.md)
 - [UpdateContactLogComment](docs/Model/UpdateContactLogComment.md)
 - [UpdateContactLogRequest](docs/Model/UpdateContactLogRequest.md)
 - [UpdateContactLogType](docs/Model/UpdateContactLogType.md)
 - [UploadClientDocumentRequest](docs/Model/UploadClientDocumentRequest.md)
 - [UploadClientDocumentResponse](docs/Model/UploadClientDocumentResponse.md)
 - [UploadClientPhotoRequest](docs/Model/UploadClientPhotoRequest.md)
 - [UploadClientPhotoResponse](docs/Model/UploadClientPhotoResponse.md)
 - [User](docs/Model/User.md)
 - [Visit](docs/Model/Visit.md)
 - [WaitlistEntry](docs/Model/WaitlistEntry.md)


## Documentation For Authorization


## API-Key

- **Type**: API key
- **API key parameter name**: API-Key
- **Location**: HTTP header


## Author




