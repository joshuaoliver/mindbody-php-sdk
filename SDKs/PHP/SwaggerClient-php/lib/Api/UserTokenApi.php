<?php
/**
 * UserTokenApi
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * MINDBODY Public API
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: v6
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 2.4.6
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Api;

use GuzzleHttp\Client;
use GuzzleHttp\ClientInterface;
use GuzzleHttp\Exception\RequestException;
use GuzzleHttp\Psr7\MultipartStream;
use GuzzleHttp\Psr7\Request;
use GuzzleHttp\RequestOptions;
use Swagger\Client\ApiException;
use Swagger\Client\Configuration;
use Swagger\Client\HeaderSelector;
use Swagger\Client\ObjectSerializer;

/**
 * UserTokenApi Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class UserTokenApi
{
    /**
     * @var ClientInterface
     */
    protected $client;

    /**
     * @var Configuration
     */
    protected $config;

    /**
     * @var HeaderSelector
     */
    protected $headerSelector;

    /**
     * @param ClientInterface $client
     * @param Configuration   $config
     * @param HeaderSelector  $selector
     */
    public function __construct(
        ClientInterface $client = null,
        Configuration $config = null,
        HeaderSelector $selector = null
    ) {
        $this->client = $client ?: new Client();
        $this->config = $config ?: new Configuration();
        $this->headerSelector = $selector ?: new HeaderSelector();
    }

    /**
     * @return Configuration
     */
    public function getConfig()
    {
        return $this->config;
    }

    /**
     * Operation userTokenIssue
     *
     * Get a staff user token.
     *
     * @param  \Swagger\Client\Model\IssueRequest $request request (required)
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version version (required)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return \Swagger\Client\Model\IssueResponse
     */
    public function userTokenIssue($request, $site_id, $version)
    {
        list($response) = $this->userTokenIssueWithHttpInfo($request, $site_id, $version);
        return $response;
    }

    /**
     * Operation userTokenIssueWithHttpInfo
     *
     * Get a staff user token.
     *
     * @param  \Swagger\Client\Model\IssueRequest $request (required)
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version (required)
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of \Swagger\Client\Model\IssueResponse, HTTP status code, HTTP response headers (array of strings)
     */
    public function userTokenIssueWithHttpInfo($request, $site_id, $version)
    {
        $returnType = '\Swagger\Client\Model\IssueResponse';
        $request = $this->userTokenIssueRequest($request, $site_id, $version);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if ($returnType !== 'string') {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        '\Swagger\Client\Model\IssueResponse',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation userTokenIssueAsync
     *
     * Get a staff user token.
     *
     * @param  \Swagger\Client\Model\IssueRequest $request (required)
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version (required)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function userTokenIssueAsync($request, $site_id, $version)
    {
        return $this->userTokenIssueAsyncWithHttpInfo($request, $site_id, $version)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation userTokenIssueAsyncWithHttpInfo
     *
     * Get a staff user token.
     *
     * @param  \Swagger\Client\Model\IssueRequest $request (required)
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version (required)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function userTokenIssueAsyncWithHttpInfo($request, $site_id, $version)
    {
        $returnType = '\Swagger\Client\Model\IssueResponse';
        $request = $this->userTokenIssueRequest($request, $site_id, $version);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'userTokenIssue'
     *
     * @param  \Swagger\Client\Model\IssueRequest $request (required)
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version (required)
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function userTokenIssueRequest($request, $site_id, $version)
    {
        // verify the required parameter 'request' is set
        if ($request === null || (is_array($request) && count($request) === 0)) {
            throw new \InvalidArgumentException(
                'Missing the required parameter $request when calling userTokenIssue'
            );
        }
        // verify the required parameter 'site_id' is set
        if ($site_id === null || (is_array($site_id) && count($site_id) === 0)) {
            throw new \InvalidArgumentException(
                'Missing the required parameter $site_id when calling userTokenIssue'
            );
        }
        // verify the required parameter 'version' is set
        if ($version === null || (is_array($version) && count($version) === 0)) {
            throw new \InvalidArgumentException(
                'Missing the required parameter $version when calling userTokenIssue'
            );
        }

        $resourcePath = '/public/v{version}/usertoken/issue';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;

        // header params
        if ($site_id !== null) {
            $headerParams['siteId'] = ObjectSerializer::toHeaderValue($site_id);
        }

        // path params
        if ($version !== null) {
            $resourcePath = str_replace(
                '{' . 'version' . '}',
                ObjectSerializer::toPathValue($version),
                $resourcePath
            );
        }

        // body params
        $_tempBody = null;
        if (isset($request)) {
            $_tempBody = $request;
        }

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'],
                ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded', 'multipart/form-data']
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }


        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'POST',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Operation userTokenRevoke
     *
     * Revoke a user token.
     *
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version version (required)
     * @param  string $authorization A staff user authorization token. (optional, default to )
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return object
     */
    public function userTokenRevoke($site_id, $version, $authorization = '')
    {
        list($response) = $this->userTokenRevokeWithHttpInfo($site_id, $version, $authorization);
        return $response;
    }

    /**
     * Operation userTokenRevokeWithHttpInfo
     *
     * Revoke a user token.
     *
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version (required)
     * @param  string $authorization A staff user authorization token. (optional, default to )
     *
     * @throws \Swagger\Client\ApiException on non-2xx response
     * @throws \InvalidArgumentException
     * @return array of object, HTTP status code, HTTP response headers (array of strings)
     */
    public function userTokenRevokeWithHttpInfo($site_id, $version, $authorization = '')
    {
        $returnType = 'object';
        $request = $this->userTokenRevokeRequest($site_id, $version, $authorization);

        try {
            $options = $this->createHttpClientOption();
            try {
                $response = $this->client->send($request, $options);
            } catch (RequestException $e) {
                throw new ApiException(
                    "[{$e->getCode()}] {$e->getMessage()}",
                    $e->getCode(),
                    $e->getResponse() ? $e->getResponse()->getHeaders() : null,
                    $e->getResponse() ? $e->getResponse()->getBody()->getContents() : null
                );
            }

            $statusCode = $response->getStatusCode();

            if ($statusCode < 200 || $statusCode > 299) {
                throw new ApiException(
                    sprintf(
                        '[%d] Error connecting to the API (%s)',
                        $statusCode,
                        $request->getUri()
                    ),
                    $statusCode,
                    $response->getHeaders(),
                    $response->getBody()
                );
            }

            $responseBody = $response->getBody();
            if ($returnType === '\SplFileObject') {
                $content = $responseBody; //stream goes to serializer
            } else {
                $content = $responseBody->getContents();
                if ($returnType !== 'string') {
                    $content = json_decode($content);
                }
            }

            return [
                ObjectSerializer::deserialize($content, $returnType, []),
                $response->getStatusCode(),
                $response->getHeaders()
            ];

        } catch (ApiException $e) {
            switch ($e->getCode()) {
                case 200:
                    $data = ObjectSerializer::deserialize(
                        $e->getResponseBody(),
                        'object',
                        $e->getResponseHeaders()
                    );
                    $e->setResponseObject($data);
                    break;
            }
            throw $e;
        }
    }

    /**
     * Operation userTokenRevokeAsync
     *
     * Revoke a user token.
     *
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version (required)
     * @param  string $authorization A staff user authorization token. (optional, default to )
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function userTokenRevokeAsync($site_id, $version, $authorization = '')
    {
        return $this->userTokenRevokeAsyncWithHttpInfo($site_id, $version, $authorization)
            ->then(
                function ($response) {
                    return $response[0];
                }
            );
    }

    /**
     * Operation userTokenRevokeAsyncWithHttpInfo
     *
     * Revoke a user token.
     *
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version (required)
     * @param  string $authorization A staff user authorization token. (optional, default to )
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Promise\PromiseInterface
     */
    public function userTokenRevokeAsyncWithHttpInfo($site_id, $version, $authorization = '')
    {
        $returnType = 'object';
        $request = $this->userTokenRevokeRequest($site_id, $version, $authorization);

        return $this->client
            ->sendAsync($request, $this->createHttpClientOption())
            ->then(
                function ($response) use ($returnType) {
                    $responseBody = $response->getBody();
                    if ($returnType === '\SplFileObject') {
                        $content = $responseBody; //stream goes to serializer
                    } else {
                        $content = $responseBody->getContents();
                        if ($returnType !== 'string') {
                            $content = json_decode($content);
                        }
                    }

                    return [
                        ObjectSerializer::deserialize($content, $returnType, []),
                        $response->getStatusCode(),
                        $response->getHeaders()
                    ];
                },
                function ($exception) {
                    $response = $exception->getResponse();
                    $statusCode = $response->getStatusCode();
                    throw new ApiException(
                        sprintf(
                            '[%d] Error connecting to the API (%s)',
                            $statusCode,
                            $exception->getRequest()->getUri()
                        ),
                        $statusCode,
                        $response->getHeaders(),
                        $response->getBody()
                    );
                }
            );
    }

    /**
     * Create request for operation 'userTokenRevoke'
     *
     * @param  string $site_id ID of the site from which to pull data. (required)
     * @param  string $version (required)
     * @param  string $authorization A staff user authorization token. (optional, default to )
     *
     * @throws \InvalidArgumentException
     * @return \GuzzleHttp\Psr7\Request
     */
    protected function userTokenRevokeRequest($site_id, $version, $authorization = '')
    {
        // verify the required parameter 'site_id' is set
        if ($site_id === null || (is_array($site_id) && count($site_id) === 0)) {
            throw new \InvalidArgumentException(
                'Missing the required parameter $site_id when calling userTokenRevoke'
            );
        }
        // verify the required parameter 'version' is set
        if ($version === null || (is_array($version) && count($version) === 0)) {
            throw new \InvalidArgumentException(
                'Missing the required parameter $version when calling userTokenRevoke'
            );
        }

        $resourcePath = '/public/v{version}/usertoken/revoke';
        $formParams = [];
        $queryParams = [];
        $headerParams = [];
        $httpBody = '';
        $multipart = false;

        // header params
        if ($site_id !== null) {
            $headerParams['siteId'] = ObjectSerializer::toHeaderValue($site_id);
        }
        // header params
        if ($authorization !== null) {
            $headerParams['authorization'] = ObjectSerializer::toHeaderValue($authorization);
        }

        // path params
        if ($version !== null) {
            $resourcePath = str_replace(
                '{' . 'version' . '}',
                ObjectSerializer::toPathValue($version),
                $resourcePath
            );
        }

        // body params
        $_tempBody = null;

        if ($multipart) {
            $headers = $this->headerSelector->selectHeadersForMultipart(
                ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data']
            );
        } else {
            $headers = $this->headerSelector->selectHeaders(
                ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'],
                []
            );
        }

        // for model (json/xml)
        if (isset($_tempBody)) {
            // $_tempBody is the method argument, if present
            $httpBody = $_tempBody;
            // \stdClass has no __toString(), so we should encode it manually
            if ($httpBody instanceof \stdClass && $headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($httpBody);
            }
        } elseif (count($formParams) > 0) {
            if ($multipart) {
                $multipartContents = [];
                foreach ($formParams as $formParamName => $formParamValue) {
                    $multipartContents[] = [
                        'name' => $formParamName,
                        'contents' => $formParamValue
                    ];
                }
                // for HTTP post (form)
                $httpBody = new MultipartStream($multipartContents);

            } elseif ($headers['Content-Type'] === 'application/json') {
                $httpBody = \GuzzleHttp\json_encode($formParams);

            } else {
                // for HTTP post (form)
                $httpBody = \GuzzleHttp\Psr7\build_query($formParams);
            }
        }


        $defaultHeaders = [];
        if ($this->config->getUserAgent()) {
            $defaultHeaders['User-Agent'] = $this->config->getUserAgent();
        }

        $headers = array_merge(
            $defaultHeaders,
            $headerParams,
            $headers
        );

        $query = \GuzzleHttp\Psr7\build_query($queryParams);
        return new Request(
            'DELETE',
            $this->config->getHost() . $resourcePath . ($query ? "?{$query}" : ''),
            $headers,
            $httpBody
        );
    }

    /**
     * Create http client option
     *
     * @throws \RuntimeException on file opening failure
     * @return array of http client options
     */
    protected function createHttpClientOption()
    {
        $options = [];
        if ($this->config->getDebug()) {
            $options[RequestOptions::DEBUG] = fopen($this->config->getDebugFile(), 'a');
            if (!$options[RequestOptions::DEBUG]) {
                throw new \RuntimeException('Failed to open the debug file: ' . $this->config->getDebugFile());
            }
        }

        return $options;
    }
}
