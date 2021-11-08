
import discum
import gspread


bot = discum.Client(token="NjExNTU4OTAwNDcwMTIwNDU3.YV4TSA.hIzAPU_1sQuvfEPjc_FHxSWrKpM")

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members


def get_data(id):
    print(id['Google'],id['URL'],id['Name_of_sheet'])
    members = get_members(id['URL'].split('/')[-2],id['URL'].split('/')[-1])
    memberslist = []

    print(members)
    for memberID in members:
        memberslist.append(memberID)

    import time
    import requests
    username_lst = []
    headers = {"Authorization":f"{id['TOKEN']}"}
    print('yes')
    for i in memberslist:
        r = requests.get(f'https://discord.com/api/v8/users/{i}', headers=headers).json()
        time.sleep(0.8)
        try:
            username_lst.append(r['username'])
            print(r['username'])
        except:
            time.sleep(2)

    gc = gspread.service_account("service_account.json")
    gc.create(id['Name_of_sheet'])
    z = gc.open(id['Name_of_sheet'])
    worksheet = z.get_worksheet(0)
    worksheet.update('A1', id['URL'])
    for i in range(2,len(username_lst)):
        time.sleep(0.8)
        try:
            worksheet.update(f'A{i}',username_lst[i])
        except:
            time.sleep(2)

    z.share(id['Google'], perm_type="user", role='writer')
    return



info = {
    'API_KEY': "AIzaSyB_AFM5wTenYRnfAaCYPNgLnSaKXhp8B5A"
}