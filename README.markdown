# typepadout #

`typepadout` is a command line tool for exporting a TypePad blog to local files.


## Installation ##

Install it as any other Python program:

    $ python setup.py install

If you don't want to install its dependencies system-wide, try installing it in a [virtual environment](http://www.virtualenv.org/).


## Configuring ##

First, you'll need a TypePad API key. Register an application on [the Developer page of typepad.com](http://www.typepad.com/account/access/developer) to get a key. Once you have a key, run the `configure` command:

    $ bin/typepadout configure
    Consumer Key: b658d74d5ef8653b
    Consumer Secret: fHHGZ1iI
    Application ID: 6p0120a96c7944970b
    To join your application u'new test site', follow this link and click "Allow":

    <https://www.typepad.com/secure/services/api/6p0120a96c7944970b/oauth-approve?oauth_token=df67...1c75>

    Enter the verifier code TypePad gave you: 74790350
    WARNING: Making batch request for 1 items

    Yay! This new access token authorizes this typepad.client to act as markpasc
    (6p00d83451ce6b69e2). Here's the token:

        Key:    BOGYsZiz2IB0kDzX
        Secret: RgNYgELkbPaMsKkw

    Pass this access token to typepad.client.add_credentials() to re-authorize as
    markpasc later.

    Configured!

After entering your secret key, open the authorization URL in your web browser. After approving your app, copy the verifier code TypePad shows you and paste it at the prompt. `typepadout` saves your access token to a configuration file at `~/.typepadout` so you don't need to keep your own copy of the access token.


## Usage ##

See `typepadout --help` for supported commands.

    $ typepadout -v verify
    INFO: Set log level to INFO
    INFO: Verified!

    $ bin/typepadout export 6a00d83451ce6b69e20120a81fb3a4970b --dir markpasc
    100% |##################################################################|

    $ ls -1 markpasc/ | wc -l
         154

    $
