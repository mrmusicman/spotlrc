curl "https://spclient.wg.spotify.com/color-lyrics/v2/track/%1/?format=json&vocalRemoval=false&market=from_token" -H "insert yours" -H "Accept: application/json" -H "Accept-Language: en" -H "Referer: https://open.spotify.com/" -H "app-platform: WebPlayer" -H "spotify-app-version: insert yours" -H "client-token: %2" -H "Origin: https://open.spotify.com" -H "DNT: 1" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-site" -H "authorization: Bearer %3" -H "Connection: keep-alive" --output %1.json
