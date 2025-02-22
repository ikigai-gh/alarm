## Alarm bot

### Signing in
1. Sign in at telegram page[https://my.telegram.org];
2. Save api_id, api_hash;
3. Pass previous values to the script `tg_sign_in.pyz`;
4. Enter your phone number and password if necessary;
5. Enter the code you've received from the telegram app;
6. Now you've got a session file (named `anon.session` by default). Place it near `alarm.py` script.

### Running bot
1. Copy `config.ini.example` to `config.ini` (or `config_dev.ini` for the testing purposes);
2. Populate it with the values according to the comments;
3. Run `build.sh` to get a docker image;
4. If you want to just test a bot run `dev.sh`. Otherwise, execute a `prod.sh` script.
