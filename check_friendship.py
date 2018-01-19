import tweepy
import json
import csv
from pymongo import MongoClient

consumer_key = "RZMGFtwvPzBcCgKdd1giWNTnD"
consumer_secret = "MkO0oNgYsiPomJtmU0nFPuubUm3XQ5O5ZZzbs54UitG8tiZY5F"
access_token = "243047872-DAJCVYpHECs6MBLTx0QoNNRaSyUHrFGXyzVicbpU"
access_token_secret = "OS24CNpPsi5ZcqtnLBagbi0V57wM19WyUwLBwroWc7wuf"

def check_friendship():
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60)

        retweeters = ['4ki4', 'ABC_EX123','AffPress', 'Affgenius', 'AffgeniusMarket', 'Affmatic', 'AskFlynn', 'AskMackintosh', 'AskNewborn', 'AskUniversity', 'BLACKCERT', 'BonkotuRyu', 'BsdHacker', 'CPAMarketingly', 'CareerTrend', 'CyberHitchhiker', 'DailyNewTech', 'DeveloperAgent', 'G76whizkidz', 'GaitondeGirish', 'Get_My_Ads_Team', 'HowToBuildWP', 'IS_RPHG', 'JPMGGA', 'LinuxSec', 'LivingRust', 'MMarketingly', 'Mark__LP', 'Miss_Lila_AW', 'MoreMinute', 'NextBigWeb', 'Niratama', 'NitriKx', 'OnlineMarketly', 'Ryo_armory', 'SENSUALDEENA','Sexygirlshote01', 'SigP226', 'SingaporeITServ', 'SolFreakOut', 'Sydney_TechJobs', 'Tagayashiichiro', 'Tech_McTechster', 'TheCloudNetwork', 'Yu_1_guitars', 'Zimshady9611', '_4daime', 'abacl7', 'amnesia828', 'ayakomuro', 'big_bad_bingo', 'caseybecking', 'cocoeyes02', 'cyross4vocaloid', 'd_yagi', 'deep_labman', 'diberidarshi', 'dkinyu', 'dnstcpres', 'drib__', 'eMarketingly', 'e_ruru', 'eilaperopero', 'favdragon_rean', 'final_z', 'floryn90', 'fushiroyama', 'ggtechmy', 'goura', 'hage_mango', 'heitor_lessa', 'hinami_net', 'iMarketingly', 'iamjuniorpeter', 'ikaro1192', 'inet_death', 'ionis_h', 'iruka3', 'ito_yusaku', 'junjjjjjjjjjjjj', 'k2wanko', 'kahlidsaeed', 'kaigaiseolab', 'kinneko', 'kotaro_gadget', 'ksonwp', 'kuronekodaisuki', 'linare530', 'mame_pika', 'marisblue', 'mariuskarma', 'marshmallowy', 'mattmcmullan', 'meswapnilwagh', 'mhz52', 'mizisu', 'motchang', 'mummycathcan','nanto_ponta', 'naofumi0628', 'newswire_nel', 'oatzvigator', 'openfinch', 'picopalu', 'prata0x', 'pygeek', 'r_o_r_o_r_o_r_o', 'robmlove', 'roht9', 'rvp', 'sakura280869', 'serverlesssuper', 'setu_setu', 'shahzarafridi1', 'shinkosu', 'soh_alternative', 'studydotcomjobs', 'syusui_s', 't160809', 'techusic_hero', 'terajiro', 'tmonkey7', 'tony_cleal', 'tw_unicorn', 'uproad3', 'ut_shiba', 'utollwi', 'vDVille', 'victimschizo', 'yagi_', 'ydaTakahiroSeki', 'yos316', 'yutorimasato']
        followers = []

        print(len(retweeters))

        for tweeter in retweeters:
                status = api.show_friendship(source_screen_name ='itm_enterprise',target_screen_name=tweeter)
                #print(status[0].following,status[1].following)
                if status[1].following:
                    followers.append(tweeter)

        print(followers)
        print(len(followers))

if __name__ == "__main__":
        check_friendship()



