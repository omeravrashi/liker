import facebook
import urllib,urllib3

def get_app_access_token(app_id, app_secret):
    """Get the access_token for the app.

    This token can be used for insights and creating test users.

    @arg app_id :type string :desc retrieved from the developer page
    @arg app_secret :type string :desc retrieved from the developer page

    Returns the application access_token.

    """
    # Get an app access token
    args = {'grant_type': 'client_credentials',
            'client_id': app_id,
            'client_secret': app_secret}

    f = urllib2.urlopen("https://graph.facebook.com/oauth/access_token?" +
                              urllib.urlencode(args))

    try:
        result = f.read().split("=")[1]
    finally:
        f.close()

    return result

graph = facebook.GraphAPI(get_app_access_token("123176628339657", "0e756e68570169af049f1e3631a1b92e"))
print(graph.get_connections(id='1594455870606288', connection_name='likes', summary='true'))
